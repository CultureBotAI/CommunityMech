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
#
# These are built from synthetic rows and synthetic records, not from the KB.
# The first version read the pre-withdrawal record off `main` via `git show`,
# which had two problems: CI checks out at depth 1 so there is no `main` ref and
# every test skipped, and the guard looked for *any* `gtdb_classification` — the
# record has a second one — so once this merged the fixture would return the
# post-withdrawal file and the suite would fail on `main` (#394 review).
# Synthetic fixtures need neither a mapping nor a git ref, so they run in CI.
# ---------------------------------------------------------------------------


def _rank_row(gtdb_genus, genomes, ncbi_genus="Testgenus"):
    """A crosswalk row matching NCBI genus `ncbi_genus` at genus rank."""
    cells = [""] * 20
    cells[2], cells[9], cells[17] = genomes, ncbi_genus, gtdb_genus
    cells[10] = f"{ncbi_genus} namedspecies"
    return cells


TIED_ROWS = {"testgenus": [_rank_row("g__Alpha", "50"), _rank_row("g__Beta", "50")]}
DECIDED_ROWS = {"testgenus": [_rank_row("g__Alpha", "90"), _rank_row("g__Beta", "10")]}


def _record(tmp_path, name="rec.yaml", grounded=True, extra_taxon=False):
    """A community record whose taxon is grounded to g__Alpha."""
    entries = [
        {
            "taxon_term": {
                "preferred_term": "Testgenus sp. X",
                "term": {"id": "NCBITaxon:1", "label": "Testgenus"},
                **(
                    {
                        "gtdb_classification": {
                            "gtdb_id": "GTDB:g__Alpha",
                            "gtdb_taxon": "g__Alpha",
                            "ncbi_source_id": "NCBITaxon:1",
                            "majority_fraction": 0.5,
                            "mapping_source": "test",
                        }
                    }
                    if grounded
                    else {}
                ),
                "notes": "a sibling that must survive",
            }
        }
    ]
    if extra_taxon:
        entries.append(
            {
                "taxon_term": {
                    "preferred_term": "Other sp. Y",
                    "term": {"id": "NCBITaxon:2", "label": "Othergenus"},
                    "gtdb_classification": {
                        "gtdb_id": "GTDB:g__Kept",
                        "gtdb_taxon": "g__Kept",
                        "ncbi_source_id": "NCBITaxon:2",
                        "majority_fraction": 0.9,
                        "mapping_source": "test",
                    },
                }
            }
        )
    path = tmp_path / name
    path.write_text(yaml.dump({"taxonomy": entries}, sort_keys=False, allow_unicode=True))
    return path


def test_withdrawal_removes_an_ambiguous_block_and_nothing_else(gtdb, tmp_path):
    record = _record(tmp_path, extra_taxon=True)
    before = yaml.safe_load(record.read_text())

    removed = gtdb.withdraw_ambiguous(record, {}, {}, TIED_ROWS)

    after = yaml.safe_load(record.read_text())
    assert removed == 1
    assert "gtdb_classification" not in after["taxonomy"][0]["taxon_term"]
    assert after["taxonomy"][0]["taxon_term"]["notes"] == "a sibling that must survive"
    assert after["taxonomy"][1]["taxon_term"]["gtdb_classification"]["gtdb_id"] == "GTDB:g__Kept"

    def stripped(document):
        for entry in document["taxonomy"]:
            entry["taxon_term"].pop("gtdb_classification", None)
        return document

    assert stripped(before) == stripped(after)


def test_withdrawal_leaves_a_decided_grounding_alone(gtdb, tmp_path):
    """Only an ambiguous recompute withdraws — a clear majority must survive."""
    record = _record(tmp_path)
    before = record.read_text()

    assert gtdb.withdraw_ambiguous(record, {}, {}, DECIDED_ROWS) == 0
    assert record.read_text() == before


def test_withdrawal_skips_a_curated_pin(gtdb, tmp_path, monkeypatch):
    """The pin, exercised — not merely present.

    The first version of this test used the real Pelobacter record, whose taxon
    recomputes to a *non*-ambiguous g__Seleniibacterium, so it survived with or
    without the curated check and the mutant lived (#394 review).
    """
    record = _record(tmp_path, name="curated.yaml")
    monkeypatch.setitem(gtdb.CURATED_GROUNDINGS, ("curated.yaml", "NCBITaxon:1"), "pinned")

    assert gtdb.withdraw_ambiguous(record, {}, {}, TIED_ROWS) == 0
    kept = yaml.safe_load(record.read_text())["taxonomy"][0]["taxon_term"]
    assert kept["gtdb_classification"]["gtdb_id"] == "GTDB:g__Alpha"


def test_withdrawal_ignores_a_taxon_that_merely_fails_to_resolve(gtdb, tmp_path):
    """A mapping build that loses rows must not strip groundings KB-wide."""
    record = _record(tmp_path)
    before = record.read_text()

    assert gtdb.withdraw_ambiguous(record, {}, {}, {}) == 0
    assert record.read_text() == before


def test_the_withdrawal_gate_refuses_an_addition(gtdb, tmp_path):
    """The gate itself, which no test reached before.

    `test_withdrawal_refuses_to_add` only asserted that a second pass returns 0,
    and a second pass exits at `if not any(drop_entry)` long before the gate — so
    deleting the "removals only" branch killed nothing (#394 review).
    """
    record = _record(tmp_path)
    grounded_after = record.read_text()
    nothing_before = {"taxonomy": [{"taxon_term": {"term": {"id": "NCBITaxon:1"}}}]}

    with pytest.raises(SystemExit, match="created a gtdb_classification"):
        gtdb._assert_only_grounding_changed(record, nothing_before, grounded_after, withdraw=True)


def test_the_withdrawal_gate_refuses_a_no_op_write(gtdb, tmp_path):
    """`was == now` guards against a write that removed nothing."""
    record = _record(tmp_path)
    document = yaml.safe_load(record.read_text())

    with pytest.raises(SystemExit, match="removed nothing"):
        gtdb._assert_only_grounding_changed(record, document, record.read_text(), withdraw=True)


@pytest.mark.parametrize("indent", [4, 6], ids=["4-space", "6-space"])
def test_withdrawal_handles_both_indent_styles(gtdb, tmp_path, indent):
    """`_block_span` hardcoded 4, so withdrawal was inoperable on data/isolates.

    It failed safe rather than corrupting, but it is the same assumption
    `_status_spans` was fixed for in #392 and the new mode reintroduced it.
    """
    lead = " " * (indent - 4)
    record = tmp_path / f"indent{indent}.yaml"
    record.write_text(
        "taxonomy:\n"
        f"{lead}- taxon_term:\n"
        f"{lead}    preferred_term: Testgenus sp. X\n"
        f"{lead}    term:\n"
        f"{lead}      id: NCBITaxon:1\n"
        f"{lead}      label: Testgenus\n"
        f"{lead}    gtdb_classification:\n"
        f"{lead}      gtdb_id: GTDB:g__Alpha\n"
        f"{lead}      majority_fraction: 0.5\n"
        f"{lead}    notes: must survive\n"
    )

    assert gtdb.withdraw_ambiguous(record, {}, {}, TIED_ROWS) == 1

    after = yaml.safe_load(record.read_text())["taxonomy"][0]["taxon_term"]
    assert "gtdb_classification" not in after
    assert after["notes"] == "must survive"


# ---------------------------------------------------------------------------
# The curated flag (#384): protection that travels with the data.
# ---------------------------------------------------------------------------


def _curated_record(tmp_path, note="because the vote is wrong here"):
    document = {
        "taxonomy": [
            {
                "taxon_term": {
                    "preferred_term": "Testgenus sp. X",
                    "term": {"id": "NCBITaxon:1", "label": "Testgenus"},
                    "gtdb_classification": {
                        "curated": True,
                        "curation_note": note,
                        "gtdb_id": "GTDB:g__Pinned",
                        "gtdb_taxon": "g__Pinned",
                        "ncbi_source_id": "NCBITaxon:1",
                        "majority_fraction": 0.9,
                        "mapping_source": "test",
                    },
                }
            }
        ]
    }
    path = tmp_path / "curated.yaml"
    path.write_text(yaml.dump(document, sort_keys=False, allow_unicode=True))
    return path


def test_the_flag_protects_a_refresh_with_the_list_empty(gtdb, tmp_path, monkeypatch):
    """The whole point: a list only protects what someone remembered to add.

    *Chlorobium* was curated and unlisted, and survived earlier sweeps only
    because its recompute happened to yield no id — a side effect, not a
    decision (#376, #384).
    """
    monkeypatch.setattr(gtdb, "CURATED_GROUNDINGS", {})
    record = _curated_record(tmp_path)

    gtdb.apply_to_community(record, {}, {}, DECIDED_ROWS, "test-source", refresh=True)

    kept = yaml.safe_load(record.read_text())["taxonomy"][0]["taxon_term"]
    assert kept["gtdb_classification"]["gtdb_id"] == "GTDB:g__Pinned"


def test_the_flag_protects_withdrawal_with_the_list_empty(gtdb, tmp_path, monkeypatch):
    monkeypatch.setattr(gtdb, "CURATED_GROUNDINGS", {})
    record = _curated_record(tmp_path)

    assert gtdb.withdraw_ambiguous(record, {}, {}, TIED_ROWS) == 0
    kept = yaml.safe_load(record.read_text())["taxonomy"][0]["taxon_term"]
    assert kept["gtdb_classification"]["gtdb_id"] == "GTDB:g__Pinned"


def test_the_skip_message_does_not_crash_on_a_flag_only_pin(gtdb, tmp_path, monkeypatch, capsys):
    """The message indexed the list unconditionally and raised KeyError.

    That fired for exactly the case the flag exists for — a block protected by
    its own flag and absent from the list. The canary caught it before any sweep.
    """
    monkeypatch.setattr(gtdb, "CURATED_GROUNDINGS", {})
    record = _curated_record(tmp_path, note="a distinctive reason")

    gtdb.apply_to_community(record, {}, {}, DECIDED_ROWS, "test-source", refresh=True)

    assert "a distinctive reason" in capsys.readouterr().err


def test_every_curated_pin_carries_a_note_and_a_value():
    """Derived, not a hard-coded set.

    The first version asserted equality against a literal pair, so a curator
    adding a legitimate third pin got a red suite until they remembered to edit
    the test — reintroducing the very "list someone must remember" this PR argues
    against. What matters is that each pin is complete and that its value is
    recorded, so a silent change to a pinned grounding fails.
    """
    pins = {}
    for path in sorted((REPO / "kb/communities").glob("*.yaml")):
        for entry in yaml.safe_load(path.read_text()).get("taxonomy") or []:
            term_block = entry.get("taxon_term") or {}
            block = term_block.get("gtdb_classification") or {}
            if block.get("curated"):
                key = (path.name, (term_block.get("term") or {}).get("id"))
                pins[key] = block.get("gtdb_id")
                assert block.get("curation_note"), f"{path.name}: curated with no note"

    assert pins, "no curated pins found; the flag protects nothing"
    # The two known pins are value-pinned, so a mapping build that makes either
    # resolve cannot change the stored answer without failing here. Additional
    # pins are welcome and need no edit.
    known = {
        ("Dehalococcoides_Pelobacter_Acetylene_TCE_Coculture.yaml", "NCBITaxon:18"): (
            "GTDB:g__Syntrophotalea"
        ),
        ("Chlorochromatium_Aggregatum_Phototrophic_Consortium.yaml", "NCBITaxon:340177"): (
            "GTDB:g__Chlorobium"
        ),
    }
    for key, expected in known.items():
        assert pins.get(key) == expected, f"{key} is pinned to {pins.get(key)}, expected {expected}"


def test_a_false_flag_does_not_freeze_a_block(gtdb, tmp_path, monkeypatch):
    """`curated: false` means "checked, the tool is right" — not "never touch"."""
    monkeypatch.setattr(gtdb, "CURATED_GROUNDINGS", {})
    record = _curated_record(tmp_path)
    document = yaml.safe_load(record.read_text())
    document["taxonomy"][0]["taxon_term"]["gtdb_classification"]["curated"] = False
    record.write_text(yaml.dump(document, sort_keys=False, allow_unicode=True))

    assert (
        gtdb.withdraw_ambiguous(record, {}, {}, TIED_ROWS) == 1
    ), "curated: false must not protect the block"


def test_a_note_alone_does_not_protect(gtdb, tmp_path, monkeypatch):
    """Only the flag protects. A note is documentation, not a lock."""
    monkeypatch.setattr(gtdb, "CURATED_GROUNDINGS", {})
    record = _curated_record(tmp_path)
    document = yaml.safe_load(record.read_text())
    del document["taxonomy"][0]["taxon_term"]["gtdb_classification"]["curated"]
    record.write_text(yaml.dump(document, sort_keys=False, allow_unicode=True))

    assert gtdb.withdraw_ambiguous(record, {}, {}, TIED_ROWS) == 1


def test_the_write_gate_refuses_to_drop_a_pin(gtdb, tmp_path):
    """Losing the flag is the regression the flag exists to prevent.

    `_block` never emits `curated`, and the gate pops gtdb_classification
    wholesale before comparing, so a path that failed to detect the flag would
    rewrite the block and delete the evidence it was ever curated (#397 review).
    """
    record = _curated_record(tmp_path)
    before = yaml.safe_load(record.read_text())
    unpinned = yaml.safe_load(record.read_text())
    del unpinned["taxonomy"][0]["taxon_term"]["gtdb_classification"]["curated"]

    with pytest.raises(SystemExit, match="dropped `curated`"):
        gtdb._assert_only_grounding_changed(
            record, before, yaml.dump(unpinned, sort_keys=False, allow_unicode=True), refresh=True
        )
