"""Mocked transport controls supplement the required real M5 transfer canary."""

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts/adhoc"))
import checkpoint_phase2_review_inputs_20261115 as core  # noqa: E402
import replicate_phase2_review_checkpoint_20261115 as transport  # noqa: E402

SPEC = importlib.util.spec_from_file_location("standalone_checkpoint_verifier", transport.VERIFIER)
VERIFIER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFIER)


@pytest.fixture
def staged(tmp_path, monkeypatch):
    monkeypatch.setattr(core, "ROOT", tmp_path)
    monkeypatch.setattr(transport, "ROOT", tmp_path)
    source = tmp_path / "source"
    source.mkdir()
    (source / "review.yaml").write_bytes(b"retained review bytes\n")
    (source / "native.log").write_bytes(b"native diagnostic bytes\n")
    files = []
    for name, role in (("review.yaml", "review_yaml"), ("native.log", "input")):
        raw = (source / name).read_bytes()
        files.append(
            {
                "original_path": name,
                "snapshot_path": "20261115T000000Z-toy/inputs/" + name,
                "expected_sha256": core.digest(raw),
                "bytes": len(raw),
                "role": role,
            }
        )
    snapshot = tmp_path / ".temp/snapshot"
    core.snapshot(
        {
            "status": "ready",
            "reviews": [
                {
                    "review_id": "20261115T000000Z-toy",
                    "status": "ready",
                    "source_checkout": str(source),
                    "files": files,
                }
            ],
        },
        snapshot,
    )
    directory = tmp_path / ".temp/transfer"
    plan = transport.prepare(snapshot, directory, "toy-001")
    return directory, plan


def fake_runner(directory, plan, calls, failure=None):
    def run(argv, capture_output, check):
        assert capture_output is True and check is False
        calls.append(argv)
        code, stdout = 0, b""
        if argv[0] == "ssh":
            text = argv[-1]
            if text.startswith("cd "):
                stdout = (transport.REMOTE_CHECKOUT + "\n").encode()
            elif "mkdir " in text and failure == "existing_destination":
                code = 1
            elif text.startswith("shasum "):
                expected = (
                    plan["standalone_verifier_sha256"]
                    if text.endswith("verify_checkpoint.py")
                    else plan["canary"]["sha256"]
                )
                if failure == "bad_canary" and not text.endswith("verify_checkpoint.py"):
                    expected = "0" * 64
                stdout = (expected + "  retained-file\n").encode()
            elif text.startswith("stat "):
                stdout = str(plan["canary"]["bytes"]).encode()
            elif text.startswith("/usr/bin/python3 "):
                result = VERIFIER.verify(
                    directory / "payload/snapshot", plan["snapshot"]["manifest_sha256"]
                )
                stdout = json.dumps(result).encode()
        return subprocess.CompletedProcess(argv, code, stdout, b"")

    return run


def test_canary_and_remaining_use_same_native_transport_then_verify_all(staged):
    directory, plan = staged
    calls = []
    result = transport.transfer(directory / "plan.json", run=fake_runner(directory, plan, calls))
    assert result["status"] == "verified"
    rsync_calls = [argv for argv in calls if argv[0] == "rsync"]
    assert len(rsync_calls) == 2
    assert rsync_calls[0][-2:] == rsync_calls[1][-2:]
    assert all("--ignore-existing" in argv and "--from0" in argv for argv in rsync_calls)
    assert all(not any(part.startswith("--delete") for part in argv) for argv in rsync_calls)
    assert result["remote_verification"]["files_verified"] == 2
    raw = (directory / "transfer-receipt.json").read_bytes()
    count = len(calls)
    with pytest.raises(ValueError, match="already attempted"):
        transport.transfer(directory / "plan.json", run=fake_runner(directory, plan, calls))
    assert len(calls) == count
    assert (directory / "transfer-receipt.json").read_bytes() == raw


@pytest.mark.parametrize("failure", ["bad_canary", "existing_destination"])
def test_failed_canary_or_existing_destination_never_fans_out(staged, failure):
    directory, plan = staged
    calls = []
    with pytest.raises((RuntimeError, ValueError)):
        transport.transfer(
            directory / "plan.json", run=fake_runner(directory, plan, calls, failure)
        )
    rsync_calls = [argv for argv in calls if argv[0] == "rsync"]
    assert len(rsync_calls) == (1 if failure == "bad_canary" else 0)
    receipt = json.loads((directory / "transfer-receipt.json").read_bytes())
    assert receipt["status"] == "failed" and "remote_verification" not in receipt


def test_rehashed_filelist_cannot_copy_undeclared_files(staged):
    directory, plan = staged
    extra = b"../../.env\0"
    (directory / "remaining.files").write_bytes(extra)
    plan["filelist_sha256"]["remaining.files"] = core.digest(extra)
    (directory / "plan.json").write_text(json.dumps(plan))
    calls = []
    with pytest.raises(ValueError, match="undeclared or missing"):
        transport.transfer(directory / "plan.json", run=fake_runner(directory, plan, calls))
    assert not calls and not (directory / "transfer-started.json").exists()
