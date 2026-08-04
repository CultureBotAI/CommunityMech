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
# `kb/taxa` is deliberately absent: its ids are `CommunityMech:taxon:NNNNNN`,
# a different space from the record ids this module governs.
RECORD_DIRS = ("kb/communities", "data/isolates")

# Paths that legitimately mention ids without owning them: fixtures, caches and
# prose. `tests/data` holds deliberate copies of real records.
EXCLUDED = (
    "tests/data",
    "references_cache",
    ".git",
    ".venv",  # ~160 dependency YAMLs; leaving them in made the sweep machine-dependent
    "site",
    "docs",
    "notes",
)

# Quoting is ordinary YAML, and an id in quotes must not be able to slip the
# gate: `id: "CommunityMech:000320"` was invisible to every check here (#351).
# Trailing comments are tolerated for the same reason.
ID_RE = re.compile(r"""^id:[ \t]*['"]?(CommunityMech:\d+)['"]?[ \t\r]*(?:\#[^\n]*)?$""", re.M)


def _declared_ids():
    """Every (id, path) pair declared anywhere in the repo."""
    found = []
    for path in sorted([*REPO.glob("**/*.yaml"), *REPO.glob("**/*.yml")]):
        rel = path.relative_to(REPO)
        # Compare path *components*, not the string. Under `startswith`, a
        # `notes_archive/` would be excluded outright and a `data/isolates_v2/`
        # would count as a known directory, purely because the names share a
        # prefix (#351). Neither exists today; this is prophylactic.
        if _under(rel, EXCLUDED):
            continue
        for identifier in _ids_in(path):
            found.append((identifier, rel.as_posix()))
    return found


def _ids_in(path: Path) -> list:
    """Every record id declared in one file.

    findall, not search: a second document in one file declares a second id, and
    taking only the first hid it. Extracted so that behaviour is reachable from a
    test — inlined, reverting it to `search` passed the whole suite (#354).
    """
    return ID_RE.findall(path.read_text())


def _under(rel: Path, roots) -> bool:
    """True if `rel` sits inside one of `roots`, matching whole path components."""
    parts = rel.parts
    return any(parts[: len(Path(r).parts)] == Path(r).parts for r in roots)


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
    strays = sorted(rel for _, rel in declared if not _under(Path(rel), RECORD_DIRS))
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


# ---------------------------------------------------------------------------
# The sweep internals. None of these shapes exist in the KB today, so without
# direct tests every one of them is dead code — which is how a regression got
# in: hardening the pattern for quotes silently dropped `\r`, and nothing
# noticed because no record uses CRLF (#354).
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "line",
    [
        "id: CommunityMech:000320",
        'id: "CommunityMech:000320"',
        "id: 'CommunityMech:000320'",
        "id: CommunityMech:000320  # a trailing comment",
        "id:\tCommunityMech:000320",
        "id: CommunityMech:000320\r",  # CRLF
        'id: "CommunityMech:000320"\r',
    ],
)
def test_id_regex_matches_every_legitimate_spelling(line):
    assert ID_RE.findall(line) == ["CommunityMech:000320"], f"missed: {line!r}"


@pytest.mark.parametrize(
    "line",
    [
        "grid: CommunityMech:000320",  # not the `id` key
        "id: CommunityMech:taxon:000001",  # a different id space
        "  id: CommunityMech:000320",  # nested, not a record id
        "- id: CommunityMech:000320",  # list item, not a record id
        "# id: CommunityMech:000320",  # commented out
    ],
)
def test_id_regex_ignores_what_is_not_a_record_id(line):
    assert ID_RE.findall(line) == [], f"false positive: {line!r}"


def test_sweep_finds_every_document_in_a_multi_document_file(tmp_path):
    """`search` returned only the first, so a second declaration was invisible.

    Goes through `_ids_in`, the function the sweep actually calls — asserting on
    `ID_RE` directly left the sweep free to keep using `search`.
    """
    record = tmp_path / "two_docs.yaml"
    record.write_text("id: CommunityMech:000001\n---\nid: CommunityMech:000002\n")
    assert _ids_in(record) == ["CommunityMech:000001", "CommunityMech:000002"]


@pytest.mark.parametrize(
    ("rel", "roots", "expected"),
    [
        ("kb/communities/x.yaml", ("kb/communities",), True),
        ("data/isolates/x.yaml", ("kb/communities", "data/isolates"), True),
        # The prefix bug: these share a name prefix but are different directories.
        ("kb/communities_draft/x.yaml", ("kb/communities",), False),
        ("data/isolates_v2/x.yaml", ("data/isolates",), False),
        ("notes_archive/x.yaml", ("notes",), False),
        ("notes/deep/x.yaml", ("notes",), True),
    ],
)
def test_under_matches_whole_path_components(rel, roots, expected):
    assert _under(Path(rel), roots) is expected
