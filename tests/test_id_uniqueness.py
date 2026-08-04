"""The CommunityMech id is a primary key, so assert it actually is one.

Nothing checked this before, and it turned out not to hold: four ids were used
twice, because `data/isolates/` carries `CommunityMech:` identifiers while
sitting outside every gate — no workflow's `paths:` filter mentions it and
`validate-strict` walks a glob that excludes it. New records were then minted by
scanning only `kb/communities/`, so they reused ids the isolates already held
(#310).

Two records answering to one id means anything resolving it gets whichever the
tool read first — silently, and differently on different machines.

The sweep is directory-agnostic on purpose: it globs the repo for anything
declaring a `CommunityMech:` id, so a *new* directory of records cannot
reintroduce the gap the way `data/isolates/` did.
"""

import collections
import re
from pathlib import Path

import pytest

REPO = Path(__file__).parent.parent

# Where records may legitimately live. Anything outside these that declares an
# id is reported too — see test_no_id_bearing_records_outside_known_dirs.
RECORD_DIRS = ("kb/communities", "kb/taxa", "data/isolates")

# Paths that legitimately mention ids without owning them: fixtures, caches and
# prose. `tests/data` holds deliberate copies of real records.
EXCLUDED = ("tests/data", "references_cache", ".git", "site", "docs", "notes")

ID_RE = re.compile(r"^id:\s*(CommunityMech:\d+)\s*$", re.M)


def _declared_ids():
    """Every (id, path) pair declared anywhere in the repo."""
    found = []
    for path in sorted(REPO.glob("**/*.yaml")):
        rel = path.relative_to(REPO).as_posix()
        if any(rel.startswith(skip) for skip in EXCLUDED):
            continue
        match = ID_RE.search(path.read_text())
        if match:
            found.append((match.group(1), rel))
    return found


@pytest.fixture(scope="module")
def declared():
    found = _declared_ids()
    # A relative-path glob that matches nothing passes vacuously; make an empty
    # sweep a failure rather than a silent success.
    assert len(found) > 300, f"expected the full KB, swept only {len(found)} records"
    return found


def test_every_communitymech_id_is_used_exactly_once(declared):
    by_id = collections.defaultdict(list)
    for identifier, rel in declared:
        by_id[identifier].append(rel)

    collisions = {i: paths for i, paths in by_id.items() if len(paths) > 1}
    assert not collisions, "ids used more than once:\n" + "\n".join(
        f"  {i}\n" + "\n".join(f"      {p}" for p in paths)
        for i, paths in sorted(collisions.items())
    )


def test_no_id_bearing_records_outside_known_dirs(declared):
    """A new record directory must be added to the gates, not just created.

    `data/isolates/` was real enough to hold production identifiers and
    invisible enough that nothing validated it. This makes that combination
    impossible to reach silently.
    """
    strays = sorted(rel for _, rel in declared if not any(rel.startswith(d) for d in RECORD_DIRS))
    assert not strays, (
        "these declare a CommunityMech id but live outside "
        f"{RECORD_DIRS}; add the directory to RECORD_DIRS and to the validation "
        "gates, or move the records:\n" + "\n".join(f"  {s}" for s in strays)
    )


def test_isolates_are_actually_single_organism(declared):
    """`data/isolates/` is defined by its README as monocultures.

    SPRUCE sat there with four taxa and a colliding id, unvalidated, because
    nothing checked either property (#310).
    """
    import yaml

    offenders = []
    for path in sorted((REPO / "data/isolates").glob("*.yaml")):
        data = yaml.safe_load(path.read_text()) or {}
        taxa = data.get("taxonomy") or []
        if len(taxa) != 1:
            offenders.append(f"{path.name}: {len(taxa)} taxa")

    assert not offenders, (
        "data/isolates/ holds single-organism records by definition; these are "
        "communities and belong in kb/communities/:\n" + "\n".join(f"  {o}" for o in offenders)
    )


def test_isolates_pass_schema_validation():
    """`data/isolates/` sat outside every validation gate, and rotted there.

    Two of its five records were schema-invalid on `main` — `associated_datasets`
    entries using `name:` where the slot is `title:`, and dataset_type values
    (`METAGENOME`, `METATRANSCRIPTOME`) that are not in the enum. Nobody knew,
    because `validate-strict` walks a glob that excludes the directory (#310).
    """
    import subprocess

    from linkml_runtime.utils.schemaview import SchemaView  # noqa: F401  (import cost only)

    schema = REPO / "src/communitymech/schema/communitymech.yaml"
    records = sorted((REPO / "data/isolates").glob("*.yaml"))
    assert records, "no isolate records found"

    failures = []
    for record in records:
        result = subprocess.run(
            ["uv", "run", "linkml-validate", "-s", str(schema), str(record)],
            capture_output=True,
            text=True,
            cwd=REPO,
        )
        if result.returncode != 0:
            failures.append(f"{record.name}:\n{result.stdout.strip()}")

    assert not failures, "schema-invalid isolate records:\n" + "\n".join(failures)
