"""Retained findings and exact Git/native-command evidence (#2791/#2792)."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import subprocess
from pathlib import Path

import pytest

SCRIPT = (
    Path(__file__).resolve().parents[1] / "scripts/adhoc/summarize_m5_native_references_20261114.py"
)
SPEC = importlib.util.spec_from_file_location("m5_native_reference_summary", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
A = "kb/communities/A.yaml"
B = "data/isolates/B.yaml"
C = "kb/communities/C.yaml"
D = "kb/communities/D.yaml"


@pytest.fixture
def pinned_tree(tmp_path, monkeypatch):
    """A real isolated commit, without global hooks, signing or personal identity."""
    subprocess.run(
        ["git", "init", "-q", "-b", "fixture-reference-inventory", str(tmp_path)], check=True
    )
    for name in (A, B, C):
        path = tmp_path / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("fixture: true\n")
    subprocess.run(["git", "add", "."], cwd=tmp_path, check=True)
    subprocess.run(
        [
            "git",
            "-c",
            "user.name=Fixture",
            "-c",
            "user.email=fixture@example.invalid",
            "-c",
            "commit.gpgsign=false",
            "-c",
            "core.hooksPath=/dev/null",
            "commit",
            "-qm",
            "Pin reference inventory fixture",
        ],
        cwd=tmp_path,
        check=True,
    )
    revision = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=tmp_path, text=True
    ).strip()
    monkeypatch.setattr(MODULE, "REPO", tmp_path)
    return revision, f"{A}\n{B}\n{C}\n".encode()


def passed(name):
    return (
        f"\\nValidating references in {name}...\n"
        "Validation Summary:\n  Files validated: 1\n  Total checks: 0\n"
        "  All validations passed!\n"
    )


def failed(name, message="No content available for reference: PMID:1"):
    return (
        f"\\nValidating references in {name}...\n"
        f"    [ERROR] {message}\n"
        "      Location: evidence[0].snippet\n      Reference: PMID:1\n"
        "Validation Summary:\n  Files validated: 1\n  Total checks: 1\n"
        "  Issues found in 1 file(s) (1 validation issue(s))\n"
    )


def receipt(data, revision):
    return {
        "head": revision,
        "log_sha256": hashlib.sha256(data).hexdigest(),
        "log_bytes": len(data),
        "command": [
            "/opt/homebrew/bin/just",
            "--verbose",
            "--no-dotenv",
            "--color",
            "never",
            "qc-references",
        ],
        "dry_run": False,
        "diagnostic_no_deps": False,
        "started_at": "2026-11-14T22:00:00+00:00",
        "finished_at": "2026-11-14T23:00:00+00:00",
        "exit_code": 1,
        "status": "FAILED",
        "stages": [{"recipe": "validate-references-all", "status": "FAILED"}],
    }


def test_fetch_failure_is_separate_from_passed_validation_and_unfinished_tail():
    data = (
        passed(A).replace(
            "Validation Summary:",
            "Download failed for https://example.invalid - status 403\nValidation Summary:",
        )
        + f"\\nValidating references in {B}...\nCache directory: references_cache\n"
    ).encode()
    result = MODULE.summarize(data)
    assert result["records_completed"] == 1
    assert result["records_native_passed"] == 1
    assert result["records_incomplete"] == 1
    assert result["native_findings_by_severity"] == {}
    assert len(result["records"][0]["acquisition_messages"]) == 1


def test_inventory_distinguishes_missing_unexpected_duplicate_and_incomplete(pinned_tree):
    revision, expected = pinned_tree
    data = (passed(A) + passed(A) + passed(D) + f"\\nValidating references in {B}...\n").encode()
    result = MODULE.summarize(data, expected_data=expected, revision=revision)
    assert result["coverage"] == {
        "expected_revision": revision,
        "expected_inventory_sha256": hashlib.sha256(f"{A}\n{B}\n{C}\n".encode()).hexdigest(),
        "expected_records": 3,
        "git_inventory_verified": True,
        "missing_records": [C],
        "unexpected_records": [D],
        "duplicate_records": [A],
        "incomplete_records": [B],
        "complete": False,
    }
    assert result["records_started"] == 4
    assert result["unique_records_started"] == 3


def test_complete_coverage_retains_failed_command_and_exact_native_finding(pinned_tree):
    revision, expected = pinned_tree
    data = (passed(A) + failed(B) + passed(C)).encode()
    result = MODULE.summarize(
        data, expected_data=expected, revision=revision, receipt=receipt(data, revision)
    )
    assert result["coverage"]["complete"] is True
    assert result["native_command"]["exit_code"] == 1
    assert result["records_native_passed"] == 2
    assert result["records_with_native_findings"] == 1
    assert result["records"][1]["findings"][0] == {
        "severity": "ERROR",
        "message": "No content available for reference: PMID:1",
        "category": "source_content_unavailable",
        "location": "evidence[0].snippet",
        "reference": "PMID:1",
    }


@pytest.mark.parametrize(
    ("key", "value"),
    [
        ("head", "b" * 40),
        ("log_sha256", "0" * 64),
        ("log_bytes", 1),
        ("command", ["just", "--dry-run", "qc-references"]),
        ("command", ["just", "--no-deps", "qc-references"]),
        ("command", ["just", "qc"]),
        ("command", ["python", "helper.py", "qc-references"]),
        ("command", ["/opt/homebrew/bin/just", "--justfile", "alternate.just", "qc-references"]),
        ("dry_run", True),
        ("diagnostic_no_deps", True),
        ("dry_run", None),
        ("started_at", None),
        ("finished_at", None),
        ("finished_at", "2026-11-14T21:00:00+00:00"),
        ("finished_at", "2026-11-14T23:00:00"),
        ("exit_code", None),
        ("exit_code", True),
        ("status", "RUNNING"),
        ("stages", [{"recipe": "validate-references-all", "status": "NOT RUN"}]),
    ],
)
def test_final_receipt_mismatch_is_rejected(key, value, pinned_tree):
    revision, expected = pinned_tree
    data = failed(A).encode()
    changed = copy.deepcopy(receipt(data, revision))
    changed[key] = value
    with pytest.raises(ValueError):
        MODULE.summarize(data, expected_data=expected, revision=revision, receipt=changed)


def test_truncated_saved_inventory_cannot_certify_partial_sweep(pinned_tree):
    revision, _ = pinned_tree
    with pytest.raises(ValueError, match="exact local Git tree"):
        MODULE.summarize(passed(A).encode(), expected_data=f"{A}\n".encode(), revision=revision)


def test_unavailable_revision_is_not_an_inventory_label(pinned_tree):
    _, expected = pinned_tree
    with pytest.raises(ValueError, match="unavailable"):
        MODULE.summarize(passed(A).encode(), expected_data=expected, revision="f" * 40)


def test_native_counter_disagreement_is_rejected():
    data = failed(A).replace("Total checks: 1", "Total checks: 0").encode()
    with pytest.raises(ValueError, match="count does not reconcile"):
        MODULE.summarize(data)


def test_public_derivative_omits_raw_lines_and_redacts_retained_messages(monkeypatch):
    monkeypatch.syspath_prepend(str(SCRIPT.parent))
    private = "person@example.invalid /Users/example/private ghp_" + "x" * 30
    raw = MODULE.summarize(failed(A, private).encode())
    public = MODULE.public_derivative(raw)
    encoded = json.dumps(public)
    assert "native_lines" not in encoded
    assert "acquisition_messages" not in encoded
    assert "person@example.invalid" not in encoded
    assert "/Users/example" not in encoded
    assert "ghp_" not in encoded
    assert public["public_derivative"]["redactions"]["email_address"] == 1
    assert raw["records"][0]["findings"][0]["message"] == private


def test_unknown_canary_record_is_rejected():
    with pytest.raises(ValueError, match="exactly once"):
        MODULE.summarize(passed(A).encode(), B)
