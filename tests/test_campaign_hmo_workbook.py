"""Guard immutable HMO source-reader receipt provenance for #2845, 2026-11-15."""

import importlib.util
import json
import sys
from pathlib import Path

import pytest
from openpyxl import Workbook

SCRIPT = (
    Path(__file__).resolve().parents[1] / "scripts/adhoc/inspect_campaign_hmo_workbook_20261115.py"
)
SPEC = importlib.util.spec_from_file_location("hmo_workbook", SCRIPT)
assert SPEC and SPEC.loader
reader = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(reader)


def test_receipt_change_during_workbook_read_fails_closed(tmp_path, monkeypatch, capsys):
    state = tmp_path / ".temp/campaign-resume-20261115"
    output = state / "capture"
    output.mkdir(parents=True)
    path = output / "source.xlsx"
    workbook = Workbook()
    workbook.active["A1"] = "Concentration"
    workbook.active["B1"] = "source unit preserved"
    workbook.save(path)
    workbook.close()
    receipt = output / "asset.receipt.json"
    entry = {"filename": path.name, "sha256": reader.sha(path), "bytes": path.stat().st_size}
    original = (json.dumps(entry) + "\n").encode()
    receipt.write_bytes(original)
    monkeypatch.setattr(reader, "ROOT", tmp_path)
    monkeypatch.setattr(reader, "STATE", state)
    monkeypatch.setattr(sys, "argv", [str(SCRIPT), str(receipt), "--sheet", "Sheet"])
    reader.main()
    assert json.loads(capsys.readouterr().out)["receipt_sha256"] == reader.sha(receipt)

    load = reader.load_workbook

    def changed_receipt(*args, **kwargs):
        result = load(*args, **kwargs)
        receipt.write_bytes(original + b" ")
        return result

    with monkeypatch.context() as patch:
        patch.setattr(reader, "load_workbook", changed_receipt)
        with pytest.raises(ValueError, match="receipt changed"):
            reader.main()
    assert not capsys.readouterr().out
    receipt.write_bytes(original)
    reader.main()
    assert json.loads(capsys.readouterr().out)["receipt_sha256"] == reader.sha(receipt)
