"""Any grounding the tool would not produce must say a curator chose it (#369).

#369 audited all 366 grounded ids against the tool and found two blocks that
disagreed with it — one resolving to a *different rank*, one to nothing at all —
and called them drift between the release a block was written from and the
current `NCBI2GTDB`. Re-auditing now, both are gone: the *Chryseobacterium*
species/genus disagreement no longer occurs, and the *Chlorobium* block that
grounds to nothing carries `curated: true`, which is a curator saying so rather
than an unnoticed gap.

What that audit was really testing is an invariant worth keeping, so this makes
it standing rather than a one-off: **a stored grounding either matches what the
tool produces today, or is marked `curated: true`.** There is no third category.
A block in it would be a claim nobody is accountable for — the tool did not make
it and no curator signed it — and that is the state #294's status enum and
#384's pin exist to prevent.

Measured when written: 378 distinct grounded taxa, 11 blocks disagreeing with
the tool, **all 11 curated**. Nine are demotion or nomenclature pins (#445,
#451), two are the *Allobosea* rename the crosswalk predates (#365).

This needs the kg-microbe crosswalk and so skips where that is absent, CI
included — the same limitation as its neighbours. It earns its place anyway: the
audit it replaces was run by hand once, and the KB has changed under it twice
since.
"""

from __future__ import annotations

import importlib.util
import pathlib

import pytest
import yaml

REPO = pathlib.Path(__file__).parent.parent
RECORD_DIRS = ("kb/communities", "data/isolates")


@pytest.fixture(scope="module")
def gtdb():
    spec = importlib.util.spec_from_file_location("gtdb_ground", REPO / "scripts/gtdb_ground.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def mapping(gtdb):
    try:
        path = gtdb.resolve_kg_microbe_dir(None) / "data/raw/NCBI2GTDB.tsv.gz"
    except SystemExit as exc:
        pytest.skip(f"kg-microbe mapping unavailable: {str(exc).splitlines()[0]}")
    if not path.exists():
        pytest.skip(f"kg-microbe NCBI2GTDB mapping not available at {path}")
    return path


def _grounded_taxa():
    """(curie, label) -> [(record, stored gtdb_id, curated)] for every block."""
    taxa: dict[tuple[str, str], list[tuple[str, str, bool]]] = {}
    for directory in RECORD_DIRS:
        for path in sorted((REPO / directory).glob("*.yaml")):
            document = yaml.safe_load(path.read_text()) or {}
            for entry in document.get("taxonomy") or []:
                block = (entry or {}).get("taxon_term") or {}
                grounding = block.get("gtdb_classification")
                term = block.get("term")
                if not isinstance(grounding, dict) or not isinstance(term, dict):
                    continue
                if not term.get("id"):
                    continue
                taxa.setdefault((term["id"], term.get("label") or ""), []).append(
                    (path.name, grounding.get("gtdb_id"), grounding.get("curated") is True)
                )
    return taxa


@pytest.fixture(scope="module")
def audit(gtdb, mapping):
    """Every stored grounding beside what the tool produces for it now."""
    taxa = _grounded_taxa()
    want_ids, want_species, want_higher = set(), set(), set()
    for curie, label in taxa:
        clean = gtdb._clean_label(label)
        if gtdb._is_species(clean):
            want_ids.add(curie.split(":")[1])
            want_species |= set(gtdb.lookup_keys(label))
        elif clean:
            want_higher |= set(gtdb.lookup_keys(label))
    by_id, by_name, by_higher = gtdb.collect_rows(mapping, want_ids, want_species, want_higher)

    rows = []
    for (curie, label), uses in sorted(taxa.items()):
        found = gtdb.resolve_target(curie.split(":")[1], label, by_id, by_name, by_higher)
        now = None if found is None else found.get("gtdb_id")
        for record, stored, curated in uses:
            rows.append((record, label, stored, now, curated))
    return rows


def test_the_audit_actually_read_the_kb(audit):
    """Guard the fixture, so an empty read cannot make the next test vacuous."""
    assert len(audit) > 700, f"expected the KB's ~727 grounded blocks, read {len(audit)}"
    assert any(stored != now for _, _, stored, now, _ in audit), (
        "no block disagrees with the tool at all, which has not been true since "
        "#365 — the audit is probably not resolving anything"
    )


def test_a_block_the_tool_would_not_produce_is_curated(audit):
    """The invariant: tool-derived, or curator-signed. Never neither."""
    unexplained = [
        f"{record}: {label!r} stores {stored}, tool says {now}"
        for record, label, stored, now, curated in audit
        if stored != now and not curated
    ]
    assert unexplained == [], (
        "these groundings match neither the tool nor a curator's decision — either "
        "re-run `gtdb_ground.py --refresh --apply`, or pin them with `curated: true` "
        "and a `curation_note` saying why (#369):\n" + "\n".join(unexplained)
    )


def test_every_curated_block_says_why(audit):
    """A pin is only accountable if it carries its reason."""
    taxa = _grounded_taxa()
    curated_records = {record for _, uses in taxa.items() for record, _, curated in uses if curated}

    missing = []
    for directory in RECORD_DIRS:
        for path in sorted((REPO / directory).glob("*.yaml")):
            if path.name not in curated_records:
                continue
            document = yaml.safe_load(path.read_text()) or {}
            for entry in document.get("taxonomy") or []:
                block = (entry or {}).get("taxon_term") or {}
                grounding = block.get("gtdb_classification") or {}
                if grounding.get("curated") is True and not grounding.get("curation_note"):
                    missing.append(f"{path.name}: {block.get('preferred_term')}")
    assert missing == [], "curated without a note:\n" + "\n".join(missing)
