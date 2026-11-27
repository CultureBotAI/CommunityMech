"""Guard the read-only coverage inventory's scope and provenance distinctions."""

import copy
import importlib.util
import json
import subprocess
from pathlib import Path

import pytest
import yaml

HELPER = Path(__file__).parents[1] / "scripts/adhoc/inventory_resume_review_coverage_20261115.py"
SPEC = importlib.util.spec_from_file_location("resume_inventory", HELPER)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def example():
    record = {
        "path": "kb/communities/example.yaml",
        "record_id": "CommunityMech:1",
        "sha256": "a" * 64,
    }
    target = {"path": record["path"], "target_id": record["record_id"]}
    review = {
        "review_id": "20261115T000000Z-example",
        "finished_at": "2026-11-15T00:00:00Z",
        "repository": "CultureBotAI/CommunityMech",
        "kind": "record",
        "completion": "completed",
        "verdict": "needs_curation",
        "scientific_review": True,
        "scope": {"coverage": "full", "reviewed_target_ids": [record["record_id"]]},
        "targets": [target],
        "source": {"inputs": [{"path": record["path"], "sha256": "a" * 64}]},
    }
    return record, target, review


def test_full_scientific_declaration_is_distinct_from_truth_or_passing_verdict():
    record, target, review = example()
    actual = MODULE.occurrence(review, target, record)
    assert actual["declared_full_record_scientific_scope"]
    assert actual["current_record_bytes_match"]
    # An unresolved curation verdict does not erase a completed assessment.
    assert review["verdict"] == "needs_curation"


@pytest.mark.parametrize(
    "change", ["partial", "batch", "selector", "diagnostic", "failed", "identity", "unassessed"]
)
def test_narrow_or_non_scientific_bundles_do_not_become_full_record_coverage(change):
    record, target, review = example()
    if change == "partial":
        review["scope"]["coverage"] = "partial"
    elif change == "batch":
        review["kind"] = "batch"
    elif change == "selector":
        target["selector"] = "ecological_interactions[0]"
    elif change == "diagnostic":
        review["scientific_review"] = False
    elif change == "failed":
        review["completion"] = "failed"
    elif change == "identity":
        target["target_id"] = "CommunityMech:2"
        review["scope"]["reviewed_target_ids"] = ["CommunityMech:2"]
    else:
        review["scope"]["reviewed_target_ids"] = []
    actual = MODULE.occurrence(review, target, record)
    assert not actual["declared_full_record_scientific_scope"]
    if change == "batch":
        assert actual["declared_full_scientific_scope"]


def test_stale_target_remains_listed_without_becoming_current_coverage():
    record, target, review = example()
    record["sha256"] = "b" * 64
    record["reviews"] = [MODULE.occurrence(review, target, record)]
    summary = MODULE.summarize([record])
    assert summary["listed_in_validated_bundle"] == 1
    assert summary["declared_full_record_scientific_scope"] == 1
    assert summary["current_bytes_declared_full_record_scientific_scope"] == 0
    assert summary["listed_but_no_current_bytes_occurrence"] == 1


def test_missing_saved_target_hash_is_refused():
    record, target, review = example()
    review["source"]["inputs"] = []
    with pytest.raises(ValueError, match="no saved input hash"):
        MODULE.occurrence(review, target, record)


def native_fixture(tmp_path, monkeypatch):
    _, _, review = example()
    relative = "reviews/structured/20261115T000000Z-example/review.yaml"
    path = tmp_path / relative
    path.parent.mkdir(parents=True)
    path.write_text(yaml.safe_dump(review))
    row = {"path": relative, **{key: review[key] for key in MODULE.LIST_KEYS}}
    stdout = json.dumps([row])
    capture = {
        "format": "m5-native-review-list-capture-v1",
        "revision": "a" * 40,
        "command": [".venv/bin/python", "scripts/record_review.py", "list"],
        "exit_code": 0,
        "before_after_inputs_equal": True,
        "stdout": stdout,
        "stdout_sha256": MODULE.digest(stdout.encode()),
        "stderr": "",
        "stderr_sha256": MODULE.digest(b""),
        "validation_inputs": {"x": "bound"},
    }
    monkeypatch.setattr(MODULE, "validation_context", lambda root: {"x": "bound"})
    monkeypatch.setattr(MODULE, "review_paths", lambda root: [relative])
    return capture, row


def test_native_capture_control(tmp_path, monkeypatch):
    capture, row = native_fixture(tmp_path, monkeypatch)
    assert MODULE.validated_metadata(tmp_path, capture, "a" * 40) == [row]


@pytest.mark.parametrize(
    "change", ["revision", "failed", "hash", "context", "scope", "missing", "duplicate", "command"]
)
def test_invalid_native_capture_is_refused(tmp_path, monkeypatch, change):
    capture, row = native_fixture(tmp_path, monkeypatch)
    if change == "revision":
        capture["revision"] = "b" * 40
    elif change == "failed":
        capture["exit_code"] = 1
    elif change == "hash":
        capture["stdout"] += " "
    elif change == "context":
        capture["validation_inputs"] = {"x": "changed"}
    elif change == "command":
        capture["command"] = ["echo", "pretend-pass"]
    else:
        rows = [copy.deepcopy(row)]
        if change == "scope":
            rows[0]["scope"]["coverage"] = "partial"
        elif change == "missing":
            rows = []
        else:
            rows *= 2
        capture["stdout"] = json.dumps(rows)
        capture["stdout_sha256"] = MODULE.digest(capture["stdout"].encode())
    with pytest.raises(ValueError):
        MODULE.validated_metadata(tmp_path, capture, "a" * 40)


def git_fixture(tmp_path):
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    for directory in MODULE.ROOTS:
        (tmp_path / directory).mkdir(parents=True)
    record = tmp_path / "kb/communities/example.yaml"
    record.write_text("id: CommunityMech:1\n")
    subprocess.run(["git", "-C", str(tmp_path), "add", "kb"], check=True)
    subprocess.run(
        [
            "git",
            "-C",
            str(tmp_path),
            "-c",
            "user.name=Inventory test",
            "-c",
            "user.email=inventory@example.invalid",
            "commit",
            "-qm",
            "fixture",
        ],
        check=True,
    )
    revision = MODULE.git(tmp_path, "rev-parse", "HEAD").decode().strip()
    return record, revision


def test_exact_git_inventory_positive_control(tmp_path):
    _, revision = git_fixture(tmp_path)
    records = MODULE.record_inventory(tmp_path, revision, 1)
    assert [r["record_id"] for r in records] == ["CommunityMech:1"]


@pytest.mark.parametrize("change", ["dirty", "ignored", "count", "revision"])
def test_git_inventory_refuses_stale_or_incomplete_population(tmp_path, change):
    record, revision = git_fixture(tmp_path)
    count = 1
    if change == "dirty":
        record.write_text("id: CommunityMech:2\n")
    elif change == "ignored":
        (tmp_path / ".gitignore").write_text("data/isolates/ignored.yaml\n")
        (tmp_path / "data/isolates/ignored.yaml").write_text("id: CommunityMech:2\n")
    elif change == "count":
        count = 2
    else:
        revision = "b" * 40
    with pytest.raises(ValueError):
        MODULE.record_inventory(tmp_path, revision, count)
