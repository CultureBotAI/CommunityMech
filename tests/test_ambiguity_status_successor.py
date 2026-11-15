"""Actual-proof mutation/restoration controls for the #2848 status successor."""

import json
import subprocess
from pathlib import Path

import ambiguity_status_successor as successor
import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
BEFORE = "b6dc768bf6f705611933fc50882d91957225ef1e32c61330e1adb717fe175790"


@pytest.fixture
def evidence(tmp_path):
    manifest = json.loads((ROOT / successor.MANIFEST).read_bytes())
    entry = manifest["records"][0]
    git_dir = subprocess.check_output(
        ["git", "rev-parse", "--absolute-git-dir"], cwd=ROOT, text=True
    ).strip()
    (tmp_path / ".git").write_text("gitdir: " + git_dir + "\n")
    names = [entry["target"], successor.LEDGER, "scripts/gtdb_ground.py"] + [
        value["path"]
        for value in entry.values()
        if isinstance(value, dict) and "path" in value and "sha256" in value
    ]
    for name in names:
        path = tmp_path / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes((ROOT / name).read_bytes())
    return tmp_path, manifest, entry


def verify(evidence):
    root, manifest, _ = evidence
    return successor.current_record_sha256(root, successor.TARGET, BEFORE, manifest=manifest)


def test_actual_successor_and_immutable_predecessor_are_distinct(evidence):
    root, manifest, entry = evidence
    assert verify(evidence) == entry["after_sha256"]
    old = subprocess.check_output(
        ["git", "show", f"{successor.BASELINE}:{successor.TARGET}"], cwd=root
    )
    assert successor.digest(old) == BEFORE
    assert (
        successor.current_record_sha256(
            root, successor.TARGET, BEFORE, manifest={"records": []}, current=old
        )
        == BEFORE
    )
    with pytest.raises(AssertionError):
        successor.current_record_sha256(
            root, successor.TARGET, BEFORE, manifest={**manifest, "records": []}
        )
    assert verify(evidence) == entry["after_sha256"]


@pytest.mark.parametrize(
    "mutation", ["selected_species", "missing_candidate", "stock", "evidence", "event"]
)
def test_rehashed_current_biology_or_ambiguity_change_fails(evidence, mutation):
    root, _, entry = evidence
    assert verify(evidence) == entry["after_sha256"]
    path = root / entry["target"]
    original = path.read_bytes()
    document = yaml.safe_load(original)
    term = document["taxonomy"][0]["taxon_term"]
    if mutation == "selected_species":
        term["gtdb_classification"] = {"gtdb_id": successor.OPTIONS[0]}
    elif mutation == "missing_candidate":
        term["gtdb_candidates"].pop()
    elif mutation == "stock":
        document["taxonomy"][0]["strain_designation"]["strain_name"] = "different stock"
    elif mutation == "evidence":
        document["ecological_interactions"][0]["evidence"][0]["snippet"] = "unsupported evidence"
    else:
        document["curation_history"][-1]["curator"] = "invented reviewer"
    path.write_text(yaml.safe_dump(document))
    assert path.read_bytes() != original
    entry["after_sha256"] = successor.digest(path.read_bytes())
    with pytest.raises(AssertionError):
        verify(evidence)
    path.write_bytes(original)
    entry["after_sha256"] = successor.digest(original)
    assert verify(evidence) == entry["after_sha256"]


@pytest.mark.parametrize(
    "key", ["application_receipt", "history_sidecar", "native_recomputation", "review_markdown"]
)
def test_rehashed_public_proof_still_requires_immutable_review_binding(evidence, key):
    root, _, entry = evidence
    assert verify(evidence) == entry["after_sha256"]
    binding = entry[key]
    path = root / binding["path"]
    original = path.read_bytes()
    path.write_bytes(original + b"\n ")
    assert path.read_bytes() != original
    binding["sha256"] = successor.digest(path.read_bytes())
    if "raw_sha256" in binding:
        binding["raw_sha256"] = binding["sha256"]
    with pytest.raises(AssertionError):
        verify(evidence)
    path.write_bytes(original)
    binding["sha256"] = successor.digest(original)
    if "raw_sha256" in binding:
        binding["raw_sha256"] = binding["sha256"]
    assert verify(evidence) == entry["after_sha256"]


def test_scientific_scope_promotion_fails(evidence):
    root, _, entry = evidence
    assert verify(evidence) == entry["after_sha256"]
    binding = entry["diagnostic_review"]
    path = root / binding["path"]
    original = path.read_bytes()
    doc = yaml.safe_load(original)
    doc["scientific_review"] = True
    path.write_text(yaml.safe_dump(doc))
    binding["sha256"] = successor.digest(path.read_bytes())
    with pytest.raises(AssertionError):
        verify(evidence)
    path.write_bytes(original)
    binding["sha256"] = successor.digest(original)
    assert verify(evidence) == entry["after_sha256"]


def test_old_ledger_and_unrelated_records_have_no_exception(evidence):
    root, _, entry = evidence
    assert verify(evidence) == entry["after_sha256"]
    ledger = root / successor.LEDGER
    original = ledger.read_bytes()
    ledger.write_bytes(original + b"\n# rewritten ledger\n")
    with pytest.raises(AssertionError):
        verify(evidence)
    ledger.write_bytes(original)
    assert verify(evidence) == entry["after_sha256"]
    path = "data/isolates/unrelated.yaml"
    (root / path).write_bytes(b"old")
    old_hash = successor.digest(b"old")
    assert successor.current_record_sha256(root, path, old_hash) == old_hash
    (root / path).write_bytes(b"changed")
    with pytest.raises(AssertionError):
        successor.current_record_sha256(root, path, old_hash)
