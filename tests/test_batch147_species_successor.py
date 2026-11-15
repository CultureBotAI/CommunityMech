"""Actual JMP134 successor and adversarial biology/proof controls, #2848."""

import copy
import json
from pathlib import Path

import batch147_species_successor as successor
import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]


def test_actual_saved_species_successor_passes():
    assert (
        successor.current_record_sha256(ROOT, successor.TARGET, successor.BEFORE) == successor.AFTER
    )


def test_original686_hash_and_biology_stay_available():
    original = successor.historical_bytes(ROOT, successor.TARGET)
    assert successor.digest(original) == successor.BEFORE
    assert (
        successor.current_record_sha256(ROOT, successor.TARGET, successor.BEFORE, current=original)
        == successor.BEFORE
    )


def test_unknown_changed_record_has_no_allowance(tmp_path):
    with pytest.raises(AssertionError, match="other batch147"):
        successor.current_record_sha256(
            tmp_path, "data/isolates/unknown.yaml", "0" * 64, current=b"changed"
        )


@pytest.mark.parametrize(
    "field", ["stock", "quote", "graph", "discussion", "count", "history", "curated"]
)
def test_rehashed_scientific_or_population_change_refuses_then_restores(field):
    before = yaml.safe_load(successor.historical_bytes(ROOT, successor.TARGET))
    after = yaml.safe_load((ROOT / successor.TARGET).read_bytes())
    original = copy.deepcopy(after)
    successor.unchanged_science(before, after)
    if field == "stock":
        after["taxonomy"][0]["taxon_term"]["term"]["id"] = "NCBITaxon:106590"
    elif field == "quote":
        after["taxonomy"][0]["evidence"][0]["snippet"] += " Invented."
    elif field == "graph":
        after["ecological_interactions"][0]["description"] += " Invented mechanism."
    elif field == "discussion":
        after["discussions"][0]["status"] = "RESOLVED"
    elif field == "count":
        after["taxonomy"][0]["taxon_term"]["gtdb_classification"]["total_genomes"] = 2
    elif field == "history":
        after["curation_history"][0]["changes"] += " Rewritten."
    else:
        after["taxonomy"][0]["taxon_term"]["gtdb_classification"]["curated"] = True
    with pytest.raises(AssertionError):
        successor.unchanged_science(before, after)
    successor.unchanged_science(before, original)


@pytest.fixture
def actual_proof(tmp_path, monkeypatch):
    proof = json.loads((ROOT / successor.MANIFEST).read_bytes())
    historical = successor.historical_bytes(ROOT, successor.TARGET)
    current = (ROOT / successor.TARGET).read_bytes()
    names = [successor.TARGET]
    names.extend(
        proof[key]["path"]
        for key in (
            "diagnostic_review",
            "review_markdown",
            "application_receipt",
            "grounding_evidence",
            "native_recomputation",
            "history_sidecar",
        )
    )
    for name in names:
        path = tmp_path / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes((ROOT / name).read_bytes())
    # Preserve actual git-show686 bytes from the real repository; this isolated
    # file fixture exercises proof mutation without editing the working tree.
    monkeypatch.setattr(successor, "historical_bytes", lambda root, path: historical)
    return tmp_path, proof, current


def run_fixture(actual_proof):
    root, proof, current = actual_proof
    return successor.current_record_sha256(
        root, successor.TARGET, successor.BEFORE, manifest=proof, current=current
    )


@pytest.mark.parametrize(
    "kind",
    [
        "application_receipt",
        "grounding_evidence",
        "native_recomputation",
        "history_sidecar",
        "diagnostic_review",
    ],
)
def test_rehashed_actual_artifact_mutation_refuses_and_restoration_passes(actual_proof, kind):
    root, proof, _current = actual_proof
    assert run_fixture(actual_proof) == successor.AFTER
    original_item = copy.deepcopy(proof[kind])
    path = root / original_item["path"]
    original_raw = path.read_bytes()
    path.write_bytes(original_raw + b"\n")
    proof[kind]["sha256"] = successor.digest(path.read_bytes())
    if "raw_sha256" in proof[kind]:
        proof[kind]["raw_sha256"] = proof[kind]["sha256"]
    with pytest.raises(AssertionError):
        run_fixture(actual_proof)
    path.write_bytes(original_raw)
    proof[kind] = original_item
    assert run_fixture(actual_proof) == successor.AFTER


def test_incomplete_check_claim_refuses(actual_proof):
    _root, proof, _current = actual_proof
    assert run_fixture(actual_proof) == successor.AFTER
    original = proof["required_checks"].copy()
    proof["required_checks"].remove("terms")
    with pytest.raises(AssertionError):
        run_fixture(actual_proof)
    proof["required_checks"] = original
    assert run_fixture(actual_proof) == successor.AFTER
