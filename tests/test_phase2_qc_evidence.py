"""Retain native skipped/failed evidence without promoting it to a pass (#2809)."""

import hashlib
import importlib
import json
from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "status,exit_code,accepted",
    [
        ("PASSED", 0, True),
        ("FAILED", 1, True),
        ("COMPLETED WITH SKIPS", 0, True),
        ("COMPLETED WITH SKIPS", 1, False),
        ("PASSED", 1, False),
        ("FAILED", 0, False),
    ],
)
def test_native_receipt_disposition_is_preserved(
    tmp_path, monkeypatch, status, exit_code, accepted
):
    monkeypatch.syspath_prepend(str(Path(__file__).parents[1] / "scripts/adhoc"))
    module = importlib.import_module("export_phase2_qc_evidence_20261115")
    state = tmp_path / ".temp/m5-completion-20261114"
    state.mkdir(parents=True)
    output = tmp_path / "reports/technical-evidence"
    monkeypatch.setattr(module, "ROOT", tmp_path)
    monkeypatch.setattr(module, "STATE", state)
    monkeypatch.setattr(module, "OUTPUT", output)
    name = "phase2-test-qc"
    raw = b"Native ontology preflight unavailable; later stages not run.\n"
    log = state / f"{name}.log"
    log.write_bytes(raw)
    (state / f"{name}.exit").write_text(f"{exit_code}\n")
    stages = [{"recipe": "validate-terms-all", "status": "NOT RUN"}]
    receipt = {
        "name": name,
        "head": "a" * 40,
        "finished_at": "2026-11-15T00:00:00Z",
        "status": status,
        "exit_code": exit_code,
        "stages": stages,
        "log": str(log.relative_to(tmp_path)),
        "log_bytes": len(raw),
        "log_sha256": hashlib.sha256(raw).hexdigest(),
    }
    (state / f"{name}.json").write_text(json.dumps(receipt))
    if not accepted:
        with pytest.raises(ValueError, match="incomplete or inconsistent"):
            module.export(name)
        assert not output.exists()
        return
    module.export(name)
    saved = json.loads((output / f"{name}.receipt.json").read_text())
    assert saved["status"] == status
    assert saved["exit_code"] == exit_code
    assert saved["stages"] == stages
    assert (output / f"{name}.log.txt").read_bytes() == raw
