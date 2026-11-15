"""Keep R226 extraction bound to captured bytes across source mutation (#2870)."""

import io
import json
import sys
from pathlib import Path

import openpyxl
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts/adhoc"))
import verify_r226_retained_sources_20261115 as verifier  # noqa: E402


def workbook_bytes(count):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Species"
    sheet.append(["NCBI species", "Number of genomes"])
    sheet.append(["s__Paenibacillus polymyxa", count])
    stream = io.BytesIO()
    workbook.save(stream)
    workbook.close()
    return stream.getvalue()


def test_mutation_between_capture_and_parse_cannot_substitute_rows(tmp_path, monkeypatch):
    monkeypatch.setattr(verifier, "ROOT", tmp_path)
    source = tmp_path / "source.xlsx"
    source.write_bytes(workbook_bytes(128))
    captured = {}
    raw = verifier.capture(captured, source.name, verifier.sha(source.read_bytes()))
    source.write_bytes(workbook_bytes(999))
    rows = verifier.workbook_rows(raw)
    assert rows[0]["matches"] == [{"row": 2, "values": ["s__Paenibacillus polymyxa", 128]}]
    with pytest.raises(ValueError, match="changed during verification"):
        verifier.unchanged(captured)
    source.write_bytes(raw)
    verifier.unchanged(captured)


def test_changed_source_refused_before_parse(tmp_path, monkeypatch):
    monkeypatch.setattr(verifier, "ROOT", tmp_path)
    source = tmp_path / "source.xlsx"
    expected = verifier.sha(workbook_bytes(128))
    source.write_bytes(workbook_bytes(999))
    with pytest.raises(ValueError, match="input hash differs"):
        verifier.capture({}, source.name, expected)


@pytest.mark.parametrize(
    "field,value",
    [
        ("url", "https://example.invalid/source"),
        ("status", 404),
        ("bytes", 999),
        ("sha256", "0" * 64),
    ],
)
def test_download_receipt_substitution_refused(tmp_path, monkeypatch, field, value):
    monkeypatch.setattr(verifier, "ROOT", tmp_path)
    raw = b"captured source"
    (tmp_path / "source").write_bytes(raw)
    receipt = {
        "url": verifier.BASE + "source",
        "status": 200,
        "bytes": len(raw),
        "sha256": verifier.sha(raw),
    }
    receipt[field] = value
    (tmp_path / "source.receipt.json").write_text(json.dumps(receipt))
    with pytest.raises(ValueError, match="does not bind its bytes"):
        verifier.verified_download({}, "", "source", verifier.sha(raw))


def test_public_receipt_is_labeled_and_preserves_original():
    receipt = {
        "command": ["python", "reporter", "--ncbi-db", "/private/local.db"],
        "exit_code": 0,
        "log_sha256": "a" * 64,
    }
    raw = json.dumps(receipt).encode()
    result = verifier.sanitized_receipt(receipt, verifier.sha(raw))
    assert receipt["command"][-1] == "/private/local.db"
    assert result["command"][-1] == "<local NCBI taxonomy database>"
    assert result["exit_code"] == receipt["exit_code"]
    assert result["log_sha256"] == receipt["log_sha256"]
    assert result["public_derivative"]["raw_receipt_sha256"] == verifier.sha(raw)
    assert result["public_derivative"]["sanitized_fields"] == ["command[3]"]
