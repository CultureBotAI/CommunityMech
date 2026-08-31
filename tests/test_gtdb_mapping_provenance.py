"""A grounding must record which crosswalk produced it (#624).

`gtdb_classification.mapping_source` is written on every block and used to read:

    kg-microbe NCBI2GTDB.tsv.gz; GTDB release latest (built 2026-07-25)

**"latest" was a hardcoded literal.** Nothing read a GTDB release; the word was
typed into an f-string. And the only varying part came from
`mapping_path.stat().st_mtime` -- a filesystem timestamp, not a property of the
data. It changes on copy, checkout or rsync; two different crosswalks can share
one; the same crosswalk has different ones on two machines.

So a block recorded nothing identifying the input it came from. That is what
makes `audit_grounding_provenance.py`'s 78 DRIFTED blocks uninterpretable: there
is no way to distinguish "grounded against an older crosswalk" from "wrong".

The property that matters is not that the string contains a hash. It is that the
string tracks CONTENT and not the clock -- so the tests below change each
independently and assert the digest moves with one and not the other. A test
that only checked for the word "sha256" would pass on an implementation that
hashed the mtime.
"""

from __future__ import annotations

import gzip
import importlib.util
import pathlib
import re

import pytest
import yaml

REPO = pathlib.Path(__file__).parent.parent
SCRIPT = REPO / "scripts" / "gtdb_ground.py"

_SHA_IN_SOURCE = re.compile(r"sha256:([0-9a-f]{16})")


@pytest.fixture(scope="module")
def ground():
    """Load the grounder from source (no bytecode can shadow it -- #693)."""
    spec = importlib.util.spec_from_file_location("_gtdb_ground_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def crosswalk(tmp_path):
    path = tmp_path / "NCBI2GTDB.tsv.gz"
    with gzip.open(path, "wt") as handle:
        handle.write("taxid\tgtdb\n1234\ts__Escherichia coli\n")
    return path


def _slot_description(schema: dict, slot: str) -> str:
    """The `description` of a slot, wherever it is attribute-defined."""
    found = []

    def walk(node):
        if isinstance(node, dict):
            for key, value in node.items():
                if key == slot and isinstance(value, dict) and "description" in value:
                    found.append(value["description"])
                walk(value)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(schema)
    return found[0] if found else ""


def test_the_provenance_names_a_content_digest(ground, crosswalk):
    source = ground.describe_mapping(crosswalk)
    assert _SHA_IN_SOURCE.search(source), source
    assert "NCBI2GTDB.tsv.gz" in source


def test_the_digest_does_not_move_when_only_the_mtime_does(ground, crosswalk):
    """The bug, stated as a property.

    The old string's only varying part was the mtime. If this fails, the
    provenance is once again reporting the clock rather than the data.
    """
    before = ground.describe_mapping(crosswalk)
    import os

    os.utime(crosswalk, (0, 0))
    after = ground.describe_mapping(crosswalk)

    assert _SHA_IN_SOURCE.search(before).group(1) == _SHA_IN_SOURCE.search(after).group(1), (
        "the digest changed when only the file's timestamp did, so it is not "
        "derived from the crosswalk's content (#624)"
    )


def test_the_digest_moves_when_the_content_does(ground, crosswalk, tmp_path):
    """...and the other direction, so the test above cannot pass vacuously.

    An implementation returning a constant would satisfy the mtime test
    perfectly.
    """
    before = ground.describe_mapping(crosswalk)
    other = tmp_path / "other.tsv.gz"
    with gzip.open(other, "wt") as handle:
        handle.write("taxid\tgtdb\n5678\ts__Bacillus subtilis\n")

    assert _SHA_IN_SOURCE.search(before).group(1) != _SHA_IN_SOURCE.search(
        ground.describe_mapping(other)
    ).group(1), "two different crosswalks produced the same digest"


def test_no_grounding_claims_a_release_it_never_read(ground, crosswalk):
    """`latest` is not a release, and it was never read from anything."""
    source = ground.describe_mapping(crosswalk)
    assert "release latest" not in source.lower(), (
        "the provenance string still claims a 'release latest' that nothing "
        "reads -- it was a literal in an f-string (#624)"
    )


def test_the_schema_documents_the_format_it_gets(ground, crosswalk):
    """The schema's example must be an example of what is actually written.

    A canonical file whose example no longer matches the emitter is the drift
    CLAUDE.md's generated-files table exists to prevent, and it is what sent me
    looking for a GTDB release that was never recorded.
    """
    schema = yaml.safe_load(
        (REPO / "src" / "communitymech" / "schema" / "communitymech.yaml").read_text(
            encoding="utf-8"
        )
    )
    described = _slot_description(schema, "mapping_source")
    assert described, "mapping_source has no description in the schema"

    # The EXAMPLE, not the prose. The description may well discuss the old form
    # -- it does, to say why it was replaced -- and forbidding the phrase
    # anywhere would police vocabulary rather than check the contract. What has
    # to be right is the string it holds up as an example of the real thing.
    examples = re.findall(r'"([^"]*NCBI2GTDB[^"]*)"', described)
    assert examples, f"no NCBI2GTDB example in the description: {described!r}"
    assert any("sha256" in e for e in examples), examples
    assert not any(
        "release latest" in e for e in examples
    ), f"the schema still holds up the old string as its example (#624): {examples}"
