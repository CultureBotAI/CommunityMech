"""A dry run or unrelated success cannot unlock the final M5 batch (#2803)."""

import hashlib
import importlib
import json
import sys
from pathlib import Path

import pytest


@pytest.fixture
def driver(tmp_path, monkeypatch):
    monkeypatch.syspath_prepend(str(Path(__file__).parents[1] / "scripts/adhoc"))
    module = importlib.import_module("run_phase2_qc_20261115")
    state = tmp_path / ".temp/m5-completion-20261114"
    state.mkdir(parents=True)
    monkeypatch.setattr(module, "ROOT", tmp_path)
    monkeypatch.setattr(module, "STATE", state)
    monkeypatch.setattr(module, "missing_history", lambda: [])
    revision = "a" * 40
    monkeypatch.setattr(module, "git", lambda *args: revision if args[0] == "rev-parse" else "")
    monkeypatch.setattr(module.shutil, "which", lambda *args, **kwargs: "/usr/local/bin/just")
    calls = []
    monkeypatch.setattr(module, "run_check", lambda *args, **kwargs: calls.append(args) or 0)
    monkeypatch.setattr(
        sys, "argv", ["driver", "qc", "--attempt", "test", "--expected-revision", revision]
    )
    log = state / "phase2-test-canary.log"
    log.write_text("Native strict validation completed.\n")
    exit_path = state / "phase2-test-canary.exit"
    exit_path.write_text("0\n")
    receipt = {
        "name": "phase2-test-canary",
        "head": revision,
        "exit_code": 0,
        "status": "PASSED",
        "dry_run": False,
        "diagnostic_no_deps": False,
        "finished_at": "2026-11-15T00:00:00Z",
        "command": [
            "/usr/local/bin/just",
            "--verbose",
            "--no-dotenv",
            "--color",
            "never",
            "validate-strict",
            module.RECORD,
        ],
        "stages": [{"recipe": "validate-strict", "status": "PASSED"}],
        "log": str(log.relative_to(tmp_path)),
        "log_sha256": hashlib.sha256(log.read_bytes()).hexdigest(),
    }
    path = state / "phase2-test-canary.json"
    return module, receipt, path, exit_path, calls


def test_finalized_exact_canary_receipt_unlocks_batch_control(driver):
    module, receipt, path, _, calls = driver
    path.write_text(json.dumps(receipt))
    assert module.main() == 0
    assert calls == [("phase2-test-qc", ["qc"])]


def test_missing_immutable_review_base_prevents_expensive_qc(driver, monkeypatch):
    module, receipt, path, _, calls = driver
    path.write_text(json.dumps(receipt))
    monkeypatch.setattr(module, "missing_history", lambda: ["b" * 40])
    with pytest.raises(SystemExit):
        module.main()
    assert not calls


@pytest.mark.parametrize("suffix", ["main", "--force", "abc", ""])
def test_native_history_command_requires_immutable_objects_only(driver, suffix):
    module, _, _, _, calls = driver
    path = module.ROOT / ".github/workflows/validate-strict.yaml"
    path.parent.mkdir(parents=True)
    path.write_text(
        "      - name: Fetch historical cache review bases\n"
        "        run: |\n          git fetch --no-tags origin " + suffix + "\n"
    )
    with pytest.raises(ValueError, match="historical-base prerequisite"):
        module.historical_command()
    assert not calls


@pytest.mark.parametrize(
    "change", ["dry_run", "command", "unfinished", "stage", "exit_artifact", "skipped"]
)
def test_invalid_canary_never_dispatches_completion(driver, change):
    module, receipt, path, exit_path, calls = driver
    if change == "dry_run":
        receipt["dry_run"] = True
    elif change == "command":
        receipt["command"][-2:] = ["validate-scalars", module.RECORD]
    elif change == "unfinished":
        receipt.pop("finished_at")
    elif change == "stage":
        receipt["stages"] = [{"recipe": "validate-strict", "status": "NOT RUN"}]
    elif change == "exit_artifact":
        exit_path.write_text("1\n")
    else:
        receipt["status"] = "COMPLETED WITH SKIPS"
    path.write_text(json.dumps(receipt))
    with pytest.raises(SystemExit):
        module.main()
    assert not calls
