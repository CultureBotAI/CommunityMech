"""Exercise real file/HEAD drift refusal and restoration, #2897, 2026-11-15."""

import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

SCRIPT = (
    Path(__file__).resolve().parents[1]
    / "scripts/adhoc/inspect_gtdb_assignment_progress_20261115.py"
)


@pytest.mark.parametrize("fault", ["file", "head"])
def test_actual_snapshot_drift_refuses_and_restores(tmp_path, monkeypatch, fault):
    spec = importlib.util.spec_from_file_location("assignment_inventory", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    def git(*args):
        return subprocess.run(
            [
                "git",
                "-c",
                "user.name=Codex",
                "-c",
                "user.email=codex@users.noreply.github.com",
                *args,
            ],
            cwd=tmp_path,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()

    git("init", "-b", "inventory-control")
    record = tmp_path / "record.yaml"
    original = b"id: CommunityMech:000001\n"
    record.write_bytes(original)
    ledger = tmp_path / "assignments.json"
    ledger.write_text(
        json.dumps(
            {
                "records": [
                    {
                        "record_id": "CommunityMech:000001",
                        "record": "record.yaml",
                        "lane": "species",
                        "baseline_sha256": hashlib.sha256(original).hexdigest(),
                    }
                ]
            }
        )
    )
    git("add", "record.yaml", "assignments.json")
    git("-c", "commit.gpgsign=false", "commit", "-m", "Synthetic inventory control")
    initial_head = git("rev-parse", "HEAD")
    monkeypatch.setattr(module, "ROOT", tmp_path)
    monkeypatch.setattr(module, "LEDGER", ledger)
    monkeypatch.setattr(module, "LEDGER_SHA", hashlib.sha256(ledger.read_bytes()).hexdigest())

    def invoke(name):
        output = tmp_path / name
        monkeypatch.setattr(sys, "argv", [str(SCRIPT), "--output", str(output)])
        module.main()
        result = json.loads(output.read_text())
        assert result["counts"] == {"unchanged_from_assignment": 1}
        assert result["captured_inputs_unchanged"] is True
        assert result["revision"] == initial_head

    invoke("positive-before.json")
    injected = []
    with monkeypatch.context() as injection:
        if fault == "file":
            original_read = Path.read_bytes

            def read_then_mutate(path):
                content = original_read(path)
                if path == record and not injected:
                    record.write_bytes(b"id: CommunityMech:000999\n")
                    injected.append(True)
                return content

            injection.setattr(Path, "read_bytes", read_then_mutate)
            expected = "captured input changed during inventory"
        else:
            original_command = subprocess.check_output

            def read_head_then_commit(*args, **kwargs):
                result = original_command(*args, **kwargs)
                if not injected:
                    git(
                        "-c",
                        "commit.gpgsign=false",
                        "commit",
                        "--allow-empty",
                        "-m",
                        "Injected drift",
                    )
                    injected.append(True)
                return result

            injection.setattr(subprocess, "check_output", read_head_then_commit)
            expected = "checkout revision changed during inventory"
        with pytest.raises(ValueError, match=expected):
            invoke("must-not-exist.json")
    assert injected == [True]
    assert not (tmp_path / "must-not-exist.json").exists()
    if fault == "file":
        assert record.read_bytes() != original
        record.write_bytes(original)
    else:
        assert git("rev-parse", "HEAD") != initial_head
        git("switch", "-c", "restored-control", initial_head)
    invoke("positive-after.json")
