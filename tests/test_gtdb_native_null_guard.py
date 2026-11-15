"""Exercise native-null status refusals, #2888, 2026-11-15.

These are guard controls using a real record baseline and synthetic observations,
not a measurement of the crosswalk or evidence of actual M5 application.
"""

import copy
import importlib.util
from pathlib import Path

import pytest
import scoped_gtdb_successor as proof
import yaml

ROOT = Path(__file__).resolve().parents[1]
BASE = "68699871415fda3c9eebf20382a315f9f3c7b17a"
TARGET = (
    "kb/communities/"
    "Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium.yaml"
)


@pytest.fixture
def case():
    location = ROOT / "scripts/adhoc/gtdb_batch_curation_20261115.py"
    spec = importlib.util.spec_from_file_location("null_guard", location)
    guard = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(guard)
    native = guard.native_module()
    # Keep this independent of the later canonical correction.
    before = yaml.safe_load(
        guard.subprocess.check_output(["git", "show", f"{BASE}:{TARGET}"], cwd=ROOT)
    )
    occurrence = {
        "taxonomy_index": 1,
        "existing_descriptor": copy.deepcopy(before["taxonomy"][1]["taxon_term"]),
        "term": copy.deepcopy(before["taxonomy"][1]["taxon_term"]["term"]),
        "strain_name": None,
        "native_result": None,
        "classify_status": {"status": "UNRESOLVED", "candidates": []},
        "manual_curated_reason": None,
        "manual_withheld_reason": None,
    }
    row = {"record": TARGET, "record_id": before["id"], "occurrences": [occurrence]}
    after = copy.deepcopy(before)
    descriptor = after["taxonomy"][1]["taxon_term"]
    descriptor["gtdb_grounding_status"] = "UNRESOLVED"
    descriptor.pop("gtdb_candidates")
    native.record_curation_event(
        after,
        curator="gtdb_ground.py",
        action="GTDB_SET_STATUS",
        changes="Wrote gtdb_grounding_status on 1 taxonomy entries (#294, #395).",
        timestamp="2026-11-15T00:00:00Z",
    )
    return guard, native, before, after, row


def verify(case):
    guard, native, before, after, row = case
    guard.verify_operations(row, ["--apply-status"])
    guard.verify_candidate(
        yaml.safe_dump(before).encode(), yaml.safe_dump(after).encode(), row, native, "unused"
    )
    proof.verify_projection(before, after, row, [1])


def test_only_stale_candidates_status_and_one_native_event_change(case):
    verify(case)
    guard, _native, before, after, row = case
    assert before["taxonomy"][1]["taxon_term"]["gtdb_grounding_status"] == "AMBIGUOUS"
    assert after["taxonomy"][1]["taxon_term"]["gtdb_grounding_status"] == "UNRESOLVED"
    with pytest.raises(ValueError, match="status-only"):
        guard.verify_operations(row, ["--apply", "--apply-status"])


@pytest.mark.parametrize(
    "mutation",
    [
        "withheld",
        "outside",
        "block",
        "manual",
        "manual_withheld",
        "missing_hold",
        "false_status",
        "candidates",
    ],
)
def test_null_cannot_override_blocks_domain_or_manual_decisions(case, mutation):
    guard, _native, before, after, row = case
    occurrence = row["occurrences"][0]
    original = copy.deepcopy(occurrence)
    if mutation in {"withheld", "outside"}:
        value = "WITHHELD" if mutation == "withheld" else "NO_GTDB_EQUIVALENT"
        for descriptor in (
            occurrence["existing_descriptor"],
            before["taxonomy"][1]["taxon_term"],
        ):
            descriptor["gtdb_grounding_status"] = value
    elif mutation == "block":
        for descriptor in (
            occurrence["existing_descriptor"],
            before["taxonomy"][1]["taxon_term"],
        ):
            descriptor["gtdb_classification"] = {"curated": True}
    elif mutation == "manual":
        occurrence["manual_curated_reason"] = "retained manual decision"
    elif mutation == "manual_withheld":
        occurrence["manual_withheld_reason"] = "retained manual withholding"
    elif mutation == "missing_hold":
        occurrence.pop("manual_withheld_reason")
    elif mutation == "false_status":
        occurrence["classify_status"]["status"] = "NO_GTDB_EQUIVALENT"
    else:
        occurrence["classify_status"]["candidates"] = ["GTDB:s__unsupported"]
    with pytest.raises(ValueError):
        guard.verify_operations(row, ["--apply-status"])
    with pytest.raises(AssertionError):
        proof.verify_projection(before, after, row, [1])
    row["occurrences"][0] = original
    before["taxonomy"][1]["taxon_term"] = copy.deepcopy(original["existing_descriptor"])
    verify(case)


@pytest.mark.parametrize(
    "status", ["UNRESOLVED", "WITHHELD", "NO_GTDB_EQUIVALENT", "NOT_ATTEMPTED"]
)
def test_fresh_native_classification_must_agree_before_staging(case, monkeypatch, status):
    guard, native, _before, _after, row = case
    observed = []

    def classify(*args, **kwargs):
        observed.append((args, kwargs))
        return status, []

    monkeypatch.setattr(native, "classify_status", classify)
    if status == "UNRESOLVED":
        guard.verify_fresh_unresolved(native, row, row["occurrences"][0], ({}, {}, {}))
    else:
        with pytest.raises(ValueError, match="fresh native null classification"):
            guard.verify_fresh_unresolved(native, row, row["occurrences"][0], ({}, {}, {}))
    args, kwargs = observed[0]
    assert args[:4] == (Path(TARGET).name, "NCBITaxon:971", "Pseudoselenomonas ruminantium", False)
    assert kwargs == {"preferred": "Selenomonas ruminantium"}


@pytest.mark.parametrize("mutation", ["unselected", "quote", "old_history", "extra_event"])
def test_null_does_not_admit_collateral_scientific_or_history_edits(case, mutation):
    guard, native, before, after, row = case
    original = copy.deepcopy(after)
    if mutation == "unselected":
        after["taxonomy"][0]["taxon_term"]["gtdb_candidates"].pop()
    elif mutation == "quote":
        after["description"] += " Unsupported claim."
    elif mutation == "old_history":
        after["curation_history"][0]["changes"] += " rewritten"
    else:
        after["curation_history"].append(copy.deepcopy(after["curation_history"][-1]))
    with pytest.raises(ValueError):
        guard.verify_candidate(
            yaml.safe_dump(before).encode(), yaml.safe_dump(after).encode(), row, native, "unused"
        )
    with pytest.raises(AssertionError):
        proof.verify_projection(before, after, row, [1])
    after.clear()
    after.update(original)
    verify(case)
