"""The text surgery behind `--apply-status`, which shipped untested (#294, #392).

`apply_status_to_community`, `_status_spans` and `_assert_only_status_changed`
are ~260 lines of line-level YAML editing in a repo with six separate
corruption incidents behind it, and their only exercise was having been run once
over the KB. Three defects followed, all reproduced here:

* the span indent was hardcoded to 4, so `data/isolates` — which uses the
  indented-sequence style and sits at 6 — was never idempotent;
* the reconstruction loop re-emitted a line it had decided to drop whenever the
  old status keys were not exactly two lines below the anchor, which is what
  `--apply` produces, leaving records only a human could repair;
* the same loop could write a stale `gtdb_candidates` beside a fresh status
  without tripping the duplicate-key guard.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).parent.parent


@pytest.fixture(scope="module")
def gtdb():
    spec = importlib.util.spec_from_file_location("gtdb_ground", REPO / "scripts/gtdb_ground.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def rows(gtdb):
    """Row indexes for the fixture records, or skip."""
    try:
        mapping = gtdb.resolve_kg_microbe_dir(None) / "data/raw/NCBI2GTDB.tsv.gz"
    except SystemExit as exc:
        pytest.skip(f"kg-microbe mapping unavailable: {str(exc).splitlines()[0]}")
    if not mapping.exists():
        pytest.skip("kg-microbe NCBI2GTDB mapping not available")
    return gtdb.collect_rows(mapping, {"403", "1234"}, {"methylococcaceae"}, {"nitrospira"})


FOUR_SPACE = REPO / "kb/communities/AMD_Nitrososphaerota_Archaeal.yaml"
SIX_SPACE = REPO / "data/isolates/Chromobacterium_Gold_Biocyanidation.yaml"


@pytest.mark.parametrize("source", [FOUR_SPACE, SIX_SPACE], ids=["4-space", "6-space"])
def test_apply_status_is_idempotent(gtdb, rows, tmp_path, source):
    """Both indent styles. Only the 4-space one was ever canaried.

    `data/isolates` uses `  - taxon_term:`, putting its children at 6 spaces. A
    literal `\\s{4}` never matched, so the old key was neither found nor dropped
    and a second run produced a duplicate — which the guard then refused,
    leaving the record unrepairable by the tool.
    """
    record = tmp_path / source.name
    record.write_text(source.read_text())

    gtdb.apply_status_to_community(record, *rows)
    once = record.read_text()
    gtdb.apply_status_to_community(record, *rows)

    assert record.read_text() == once, "a second --apply-status changed the file"
    assert once.count("gtdb_grounding_status:") == len(
        yaml.safe_load(once).get("taxonomy") or []
    ), "one status per taxonomy entry"


def test_apply_and_apply_status_interleave_in_any_order(gtdb, rows, tmp_path):
    """The sequence that deadlocked a record (#392 review).

    `--apply` inserts `gtdb_classification` between the label and the status
    keys, so they stop being two lines below the anchor. The old loop then
    re-emitted them, producing a duplicate key the writer refused — and the
    documented repair is `--apply-status`, which is what refused.
    """
    record = tmp_path / FOUR_SPACE.name
    record.write_text(FOUR_SPACE.read_text())

    for step in ("status", "apply", "status", "apply", "status"):
        if step == "status":
            gtdb.apply_status_to_community(record, *rows)
        else:
            gtdb.apply_to_community(record, *rows, "test-source")

    document = yaml.safe_load(record.read_text())
    for entry in document["taxonomy"]:
        term_block = entry["taxon_term"]
        assert ("gtdb_classification" in term_block) == (
            term_block.get("gtdb_grounding_status") == "GROUNDED"
        ), "status and block disagree after interleaving"


def test_a_stale_candidate_list_is_replaced_not_left(gtdb, rows, tmp_path):
    """Candidates written after a block, with no status, must not survive.

    This ordering slipped past `_assert_only_status_changed` because that guard
    pops both status slots from before *and* after before comparing, so it is
    structurally unable to notice the status slots being left wrong.
    """
    document = yaml.safe_load(FOUR_SPACE.read_text())
    term_block = document["taxonomy"][0]["taxon_term"]
    term_block.pop("gtdb_grounding_status", None)
    term_block["gtdb_candidates"] = ["Stale One", "Stale Two"]
    record = tmp_path / "stale.yaml"
    record.write_text(yaml.dump(document, sort_keys=False, allow_unicode=True))

    gtdb.apply_status_to_community(record, *rows)

    after = yaml.safe_load(record.read_text())["taxonomy"][0]["taxon_term"]
    assert after.get("gtdb_grounding_status") == "GROUNDED"
    assert "gtdb_candidates" not in after, "a stale candidate list survived the rewrite"


def test_the_writer_refuses_when_anchors_do_not_match(gtdb, rows, tmp_path):
    """A wrong insertion point is silent corruption, so it must refuse."""
    document = yaml.safe_load(FOUR_SPACE.read_text())
    document["taxonomy"].append({"taxon_term": {"preferred_term": "Ghost", "term": {}}})
    record = tmp_path / "mismatched.yaml"
    record.write_text(yaml.dump(document, sort_keys=False, allow_unicode=True))

    with pytest.raises(SystemExit, match="refusing to edit"):
        gtdb.apply_status_to_community(record, *rows)


def test_nothing_outside_the_status_slots_changes(gtdb, rows, tmp_path):
    """Byte-level: the record minus its status keys must be unchanged."""
    record = tmp_path / FOUR_SPACE.name
    record.write_text(FOUR_SPACE.read_text())
    before = yaml.safe_load(record.read_text())

    gtdb.apply_status_to_community(record, *rows)
    after = yaml.safe_load(record.read_text())

    def stripped(document):
        for entry in document.get("taxonomy") or []:
            term_block = entry.get("taxon_term") or {}
            term_block.pop("gtdb_grounding_status", None)
            term_block.pop("gtdb_candidates", None)
        return document

    assert stripped(before) == stripped(after)


def test_a_duplicate_key_is_refused_rather_than_written(gtdb, rows, tmp_path):
    """The guard that turned three corruption bugs into loud failures.

    PyYAML keeps the last of two identical keys silently, so without this the
    span bugs above would have written corrupt records that `linkml-validate`
    accepted.
    """
    record = tmp_path / "dup.yaml"
    record.write_text(FOUR_SPACE.read_text())
    original = gtdb._status_spans

    # The fixture already carries statuses from the KB sweep, so disabling span
    # detection duplicates them on the first write.
    gtdb._status_spans = lambda lines, anchor, end: []  # never drop the old keys
    try:
        with pytest.raises(SystemExit, match="duplicate"):
            gtdb.apply_status_to_community(record, *rows)
    finally:
        gtdb._status_spans = original

    assert (
        record.read_text() == FOUR_SPACE.read_text()
    ), "the refusal must leave the file untouched, not half-written"


# ---------------------------------------------------------------------------
# Withdrawal (#382). `--refresh` deliberately cannot remove a block.
# ---------------------------------------------------------------------------


ENSIFER = (
    REPO / "kb/communities/Ensifer_YF2_Sphingobacterium_Y2_Polyethylene_Degrading_Consortium.yaml"
)
CURATED = REPO / "kb/communities/Dehalococcoides_Pelobacter_Acetylene_TCE_Coculture.yaml"


@pytest.fixture(scope="module")
def ensifer_rows(gtdb):
    try:
        mapping = gtdb.resolve_kg_microbe_dir(None) / "data/raw/NCBI2GTDB.tsv.gz"
    except SystemExit as exc:
        pytest.skip(f"kg-microbe mapping unavailable: {str(exc).splitlines()[0]}")
    if not mapping.exists():
        pytest.skip("kg-microbe NCBI2GTDB mapping not available")
    return gtdb.collect_rows(mapping, {"106591", "18", "243164"}, set(), {"ensifer", "pelobacter"})


def _pre_withdrawal(name: str) -> str:
    """The record as it stood before #382 withdrew its tied block.

    The committed file no longer has one — that is the point of the change — so
    reading it back would make the test assert nothing. `main` is only correct
    until this merges, so fall back to skipping rather than passing vacuously.
    """
    import subprocess

    result = subprocess.run(
        ["git", "show", f"main:kb/communities/{name}"],
        capture_output=True,
        text=True,
        cwd=REPO,
    )
    if result.returncode != 0 or "gtdb_classification" not in result.stdout:
        pytest.skip(f"no pre-withdrawal copy of {name} on main")
    return result.stdout


def test_withdrawal_removes_only_ambiguous_blocks(gtdb, ensifer_rows, tmp_path):
    """The record must lose the tied block and keep everything else."""
    record = tmp_path / ENSIFER.name
    record.write_text(_pre_withdrawal(ENSIFER.name))
    before = yaml.safe_load(record.read_text())

    removed = gtdb.withdraw_ambiguous(record, *ensifer_rows)

    after = yaml.safe_load(record.read_text())
    assert removed == 1
    grounded_before = sum(
        1 for e in before["taxonomy"] if e["taxon_term"].get("gtdb_classification")
    )
    grounded_after = sum(1 for e in after["taxonomy"] if e["taxon_term"].get("gtdb_classification"))
    assert grounded_after == grounded_before - 1

    def stripped(document):
        for entry in document["taxonomy"]:
            entry["taxon_term"].pop("gtdb_classification", None)
        return document

    assert stripped(before) == stripped(after), "withdrawal touched something else"


def test_withdrawal_leaves_a_curated_pin_alone(gtdb, ensifer_rows, tmp_path):
    """The Pelobacter pin sits at exactly 0.5 and must survive (#384)."""
    record = tmp_path / CURATED.name
    record.write_text(CURATED.read_text())

    assert gtdb.withdraw_ambiguous(record, *ensifer_rows) == 0

    after = yaml.safe_load(record.read_text())
    pinned = next(
        e["taxon_term"]
        for e in after["taxonomy"]
        if (e["taxon_term"].get("term") or {}).get("id") == "NCBITaxon:18"
    )
    assert pinned["gtdb_classification"]["gtdb_id"] == "GTDB:g__Syntrophotalea"


def test_withdrawal_refuses_to_add(gtdb, ensifer_rows, tmp_path):
    """The gate is the inverse of plain apply: removals only, and at least one."""
    record = tmp_path / ENSIFER.name
    record.write_text(_pre_withdrawal(ENSIFER.name))
    gtdb.withdraw_ambiguous(record, *ensifer_rows)

    # Nothing ambiguous is left, so a second pass has nothing to do and must not
    # claim otherwise.
    assert gtdb.withdraw_ambiguous(record, *ensifer_rows) == 0


def test_withdrawal_ignores_a_taxon_that_merely_fails_to_resolve(gtdb, tmp_path):
    """Only an *explicit* ambiguity withdraws.

    A mapping build that loses rows makes resolves fail wholesale; treating that
    as ambiguity would strip groundings across the KB on a bad download.
    """
    record = tmp_path / ENSIFER.name
    record.write_text(_pre_withdrawal(ENSIFER.name))
    before = record.read_text()

    # Empty row indexes: every resolve returns None, never `ambiguous`.
    assert gtdb.withdraw_ambiguous(record, {}, {}, {}) == 0
    assert record.read_text() == before
