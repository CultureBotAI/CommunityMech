"""Retain native identities and skipped/failed outcomes without promotion (#2809/#2839)."""

import hashlib
import importlib
import json
from pathlib import Path

import pytest


@pytest.mark.parametrize("name", ["phase2-test-qc", "phase2-code005-qc-references"])
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
    tmp_path, monkeypatch, name, status, exit_code, accepted
):
    monkeypatch.syspath_prepend(str(Path(__file__).parents[1] / "scripts/adhoc"))
    module = importlib.import_module("export_phase2_qc_evidence_20261115")
    state = tmp_path / ".temp/m5-completion-20261114"
    state.mkdir(parents=True)
    output = tmp_path / "reports/technical-evidence"
    monkeypatch.setattr(module, "ROOT", tmp_path)
    monkeypatch.setattr(module, "STATE", state)
    monkeypatch.setattr(module, "OUTPUT", output)
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
    assert saved["name"] == name
    assert saved["status"] == status
    assert saved["exit_code"] == exit_code
    assert saved["stages"] == stages
    assert (output / f"{name}.log.txt").read_bytes() == raw
    for kind, suffix in (("receipt", "json"), ("log", "log"), ("exit", "exit")):
        assert (
            saved["public_evidence"][f"raw_{kind}_sha256"]
            == hashlib.sha256((state / f"{name}.{suffix}").read_bytes()).hexdigest()
        )
