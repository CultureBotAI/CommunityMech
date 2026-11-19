"""Bind Phase 2 records to completed source assessments without changing old reviews (#2816)."""

import hashlib
import subprocess
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.record_review import render_markdown, validate_review  # noqa: E402

BASELINE = "68699871415fda3c9eebf20382a315f9f3c7b17a"
MANIFEST = "reports/phase2-completion-20261115/scientific-successor-provenance-003.yaml"
TARGETS = {
    "kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml": "CommunityMech:000025",
    "kb/communities/LBNL_Switchgrass_Soil_SynCom16.yaml": "CommunityMech:000087",
    "kb/communities/LBNL_Brachypodium_Drought_SynCom15.yaml": "CommunityMech:000088",
    "kb/communities/LBNL_Human_Gut_Interaction_SynCom.yaml": "CommunityMech:000122",
    "kb/communities/Brachypodium_Natural_Variation_Dopamine_SynCom16.yaml": "CommunityMech:000516",
}


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def historical_bytes(root, path):
    """Old semantic regression checks retain the exact pre-Phase-2 record."""
    if path not in TARGETS:
        return (root / path).read_bytes()
    return subprocess.check_output(["git", "show", f"{BASELINE}:{path}"], cwd=root)


def artifact_bytes(root, artifact):
    path = Path(artifact["path"])
    assert not path.is_absolute() and ".." not in path.parts
    resolved = (root / path).resolve()
    assert resolved.is_relative_to(root.resolve())
    raw = resolved.read_bytes()
    assert digest(raw) == artifact["sha256"], str(path)
    return raw


def validate_assessment(review, path, record_hash):
    """Coverage declarations must identify and actually assess the exact record."""
    identifier = TARGETS[path]
    assert review["repository"] == "CultureBotAI/CommunityMech"
    assert review["completion"] == "completed" and review["scientific_review"] is True
    assert review["scope"]["coverage"] == "full"
    assert identifier in review["scope"]["reviewed_target_ids"]
    targets = [row for row in review["targets"] if row["path"] == path]
    assert len(targets) == 1 and targets[0]["target_id"] == identifier
    assert not targets[0].get("selector"), "a field-only assessment cannot cover the whole record"
    inputs = [row for row in review["source"]["inputs"] if row["path"] == path]
    assert len(inputs) == 1 and inputs[0]["sha256"] == record_hash
    evidence = {row["evidence_id"]: row for row in review["evidence"]}
    assessments = [row for row in review["assessments"] if identifier in row["target_ids"]]
    assert assessments, "listed targets without actual assessments are not successors"
    assert any(
        evidence[key]["kind"] == "primary_source"
        for assessment in assessments
        for key in assessment["evidence_ids"]
    ), "at least one actual assessment must use primary-source evidence"


def reviewed_input(review, path, sha256):
    """#2818: an independently rehashed manifest cannot invent reviewed inputs."""
    matches = [item for item in review["source"]["inputs"] if item["path"] == path]
    assert len(matches) == 1 and matches[0]["sha256"] == sha256, path


def current_record_sha256(root, path, predecessor_hash, *, current=None, manifest=None):
    current = (root / path).read_bytes() if current is None else current
    if path not in TARGETS:
        assert digest(current) == predecessor_hash
        return predecessor_hash
    manifest = yaml.safe_load((root / MANIFEST).read_bytes()) if manifest is None else manifest
    assert manifest["source_baseline"] == BASELINE
    assert manifest["independent_approval"] is False
    assert {row["path"] for row in manifest["records"]} == set(TARGETS)
    assert len(manifest["records"]) == len(TARGETS)
    rows = [row for row in manifest["records"] if row["path"] == path]
    assert len(rows) == 1
    row = rows[0]
    assert row["id"] == TARGETS[path]
    before_raw = historical_bytes(root, path)
    assert digest(before_raw) == predecessor_hash == row["before_sha256"]
    assert digest(current) == row["after_sha256"]
    review = yaml.safe_load(artifact_bytes(root, row["scientific_review"]))
    validate_review(review)
    validate_assessment(review, path, row["after_sha256"])
    assert row["curation_receipts"], "an assessment is not proof that curation was applied"
    previous_hash = predecessor_hash
    for artifact in row["curation_receipts"]:
        assert artifact["sha256"] == artifact["raw_sha256"], "receipt must retain exact raw bytes"
        reviewed_input(review, artifact["raw_path"], artifact["raw_sha256"])
        receipt = yaml.safe_load(artifact_bytes(root, artifact))
        assert receipt.get("path", receipt.get("target")) == path
        assert receipt.get("applied") is True or receipt.get("applied_at")
        assert receipt["before_sha256"] == previous_hash
        previous_hash = receipt["after_sha256"]
    assert previous_hash == row["after_sha256"], "curation receipt chain is incomplete"
    before, after = yaml.safe_load(before_raw), yaml.safe_load(current)
    assert before["id"] == after["id"] == row["id"]
    previous_events = before.get("curation_history", [])
    events = after.get("curation_history", [])
    assert events[: len(previous_events)] == previous_events
    assert len(events) > len(previous_events)
    assert all(event.get("llm_assisted") is True for event in events[len(previous_events) :])
    assert row["history_sidecars"]
    for artifact in row["history_sidecars"]:
        reviewed_input(review, artifact["path"], artifact["sha256"])
        sidecar = yaml.safe_load(artifact_bytes(root, artifact))
        assert sidecar["target"]["path"] == path and sidecar["target"]["kind"] == "record"
        assert sidecar["events"]
    assert artifact_bytes(root, row["review_markdown"]).decode() == render_markdown(review)
    return row["after_sha256"]
