"""Scouting must dedup against every record root, not just kb/communities.

`scout_communities.py` reports a paper as NEW when no curated record cites it.
It built that index from `kb/communities/` alone -- but `data/isolates/` holds
records with the same root class, and **5 references are cited only from there**.
Each would have been reported as a new community to go and curate, when it is
already curated.

This is the shape this repository keeps hitting: `data/isolates` outside every
validation glob (#350), `kb/taxa` outside every CI trigger (#471), a hardcoded
root list that cannot notice a new member (#689). The fix is the same one --
read `default_record_roots()` rather than naming a directory -- so a root added
later is covered without anyone remembering this file.

The consequence here is wasted work rather than a wrong record, which is why it
sat unnoticed: a false NEW sends a curator to research a community that already
exists, and nothing fails.
"""

from __future__ import annotations

import importlib.util
import pathlib

import pytest

from communitymech.paths import default_record_roots

REPO = pathlib.Path(__file__).parent.parent
SCRIPT = REPO / "scripts" / "scout_communities.py"


@pytest.fixture(scope="module")
def scout():
    """Load the scout from source (a stale .pyc must not stand in -- #693)."""
    spec = importlib.util.spec_from_file_location("_scout_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_the_index_is_not_empty(scout):
    """Guard on the guard: an empty index would make everything look NEW."""
    index = scout.build_dedup_index()
    assert len(index["cited_pmids"]) > 300, index["cited_pmids"]
    assert len(index["name_token_sets"]) > 300


def test_every_record_root_is_scanned(scout):
    """The file list covers each root, counted against the roots themselves."""
    expected = sum(len(list(root.glob("*.yaml"))) for root in default_record_roots())
    assert expected > 300, "the record roots are empty; this test would prove nothing"
    assert len(scout.record_files()) == expected


def _cited(paths) -> set[str]:
    """Every reference these files cite, normalised."""
    import re

    pattern = re.compile(r"reference:\s*((?:PMID|doi):\S+)", re.IGNORECASE)
    found: set[str] = set()
    for path in paths:
        found.update(m.lower().rstrip(".,;") for m in pattern.findall(path.read_text()))
    return found


def test_every_root_contributes_its_unique_references(scout):
    """A reference unique to ANY root must be in the index.

    Named no directory on purpose. The first version of this test globbed
    `kb/communities` to compute the difference, and #689's guard flagged it --
    correctly, and with the right advice: fix it rather than record it. Asking
    the question per-root instead is both root-agnostic and stronger, since it
    holds for a root added later without this file being touched.
    """
    roots = default_record_roots()
    assert len(roots) > 1, "only one record root; this test cannot distinguish anything"

    files = scout.record_files()
    index = scout.build_dedup_index()
    indexed = {f"pmid:{p}" for p in index["cited_pmids"]} | {
        f"doi:{d}" for d in index["cited_dois"]
    }

    checked_any = False
    for root in roots:
        mine = [path for path in files if path.parent == root]
        others = [path for path in files if path.parent != root]
        if not mine or not others:
            continue
        unique = _cited(mine) - _cited(others)
        if not unique:
            continue
        checked_any = True
        missing = sorted(reference for reference in unique if reference not in indexed)
        assert missing == [], (
            f"these references are cited only from {root.name} and are absent "
            f"from the dedup index, so scouting would report them as NEW papers "
            f"to curate when they are already curated:\n  " + "\n  ".join(missing)
        )

    assert checked_any, (
        "no root has a reference unique to it, so this test cannot tell a scan "
        "of every root from a scan of one"
    )
