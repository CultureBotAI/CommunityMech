"""Assessment bytes must equal native inspection bytes and final disk bytes (#2864)."""

import hashlib
import importlib.util
from pathlib import Path

import pytest

SOURCE = (
    Path(__file__).resolve().parents[1]
    / "scripts/adhoc/build_code006_isolate_assessment_20261115.py"
)
spec = importlib.util.spec_from_file_location("isolate_assessment", SOURCE)
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


def inspection(path, root):
    return {
        "source": {
            "inputs": [
                {
                    "path": str(path.relative_to(root)),
                    "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                }
            ]
        }
    }


def test_assessed_bytes_cannot_change_before_native_inspection(tmp_path, monkeypatch):
    monkeypatch.setattr(builder, "ROOT", tmp_path)
    log = tmp_path / "native.log"
    original = b"2 passed\n"
    log.write_bytes(original)
    captured = builder.CapturedInputs()
    assert "2 passed" in captured.text(log)  # actual assessment precedes native inspect
    captured.verify(inspection(log, tmp_path))
    log.write_bytes(b"2 failed\n")
    assert log.read_bytes() != original
    # Native inspection correctly hashes the *new* file; it cannot retroactively
    # attach that replacement to the previous passing assessment.
    changed_inspection = inspection(log, tmp_path)
    with pytest.raises(ValueError, match="after assessment snapshot"):
        captured.verify(changed_inspection)
    log.write_bytes(original)
    captured.verify(inspection(log, tmp_path))
    assert captured.text(log) == original.decode()


def test_native_inspection_must_contain_exact_assessed_digest(tmp_path, monkeypatch):
    monkeypatch.setattr(builder, "ROOT", tmp_path)
    path = tmp_path / "receipt.json"
    path.write_bytes(b'{"passed":true}\n')
    captured = builder.CapturedInputs()
    captured.read(path)
    good = inspection(path, tmp_path)
    captured.verify(good)
    wrong = inspection(path, tmp_path)
    wrong["source"]["inputs"][0]["sha256"] = "0" * 64
    with pytest.raises(ValueError, match="native inspection differs"):
        captured.verify(wrong)
    with pytest.raises(ValueError, match="native inspection differs"):
        captured.verify({"source": {"inputs": []}})
    captured.verify(good)


def test_parse_and_hash_use_one_capture(tmp_path, monkeypatch):
    path = tmp_path / "gate.log"
    path.write_bytes(b"passed\n")
    original = Path.read_bytes
    reads = []

    def counted(item):
        reads.append(item)
        return original(item)

    monkeypatch.setattr(Path, "read_bytes", counted)
    captured = builder.CapturedInputs()
    assert captured.text(path) == "passed\n"
    assert captured.sha(path) == hashlib.sha256(b"passed\n").hexdigest()
    assert captured.read(path) == b"passed\n"
    assert reads == [path]
