"""Native inspection must bind the assessed snapshots, including transient edits (#2864)."""

import importlib.util
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts/adhoc"))
spec = importlib.util.spec_from_file_location(
    "ambiguity_assessment_capture", ROOT / "scripts/adhoc/build_ambiguity_diagnostic_20261115.py"
)
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


def setup_inspection(tmp_path, monkeypatch):
    monkeypatch.setattr(builder, "ROOT", tmp_path)
    path = tmp_path / "native.log"
    original = b"Validation passed\n"
    path.write_bytes(original)
    captures = {path: path.read_bytes()}

    def inspect(*_args, **_kwargs):
        return json.dumps(
            {
                "source": {
                    "git_revision": builder.check.REVISION,
                    "inputs": [{"path": path.name, "sha256": builder.digest(path.read_bytes())}],
                }
            }
        ).encode()

    monkeypatch.setattr(builder.subprocess, "check_output", inspect)
    return path, original, captures, inspect


def test_inspected_transient_bytes_cannot_replace_assessed_bytes(tmp_path, monkeypatch):
    path, original, captures, inspect = setup_inspection(tmp_path, monkeypatch)
    assert builder.inspect_captured(captures, ["native-inspect"], tmp_path)

    def transient(*args, **kwargs):
        path.write_bytes(b"Validation failed\n")
        assert path.read_bytes() != original
        result = inspect(*args, **kwargs)
        path.write_bytes(original)
        assert path.read_bytes() == original
        return result

    monkeypatch.setattr(builder.subprocess, "check_output", transient)
    with pytest.raises(ValueError, match="inspection.*captured"):
        builder.inspect_captured(captures, ["native-inspect"], tmp_path)
    assert path.read_bytes() == original
    monkeypatch.setattr(builder.subprocess, "check_output", inspect)
    assert builder.inspect_captured(captures, ["native-inspect"], tmp_path)


@pytest.mark.parametrize("mutation", ["missing", "extra", "duplicate"])
def test_inspection_requires_exact_captured_repository_set(tmp_path, monkeypatch, mutation):
    _, _, captures, inspect = setup_inspection(tmp_path, monkeypatch)
    assert builder.inspect_captured(captures, ["native-inspect"], tmp_path)

    def changed(*args, **kwargs):
        doc = json.loads(inspect(*args, **kwargs))
        rows = doc["source"]["inputs"]
        if mutation == "missing":
            rows.clear()
        elif mutation == "extra":
            rows.append({"path": "unassessed.log", "sha256": "0" * 64})
        else:
            rows.append(dict(rows[0]))
        return json.dumps(doc).encode()

    monkeypatch.setattr(builder.subprocess, "check_output", changed)
    with pytest.raises(ValueError, match="inspection.*captured"):
        builder.inspect_captured(captures, ["native-inspect"], tmp_path)
    monkeypatch.setattr(builder.subprocess, "check_output", inspect)
    assert builder.inspect_captured(captures, ["native-inspect"], tmp_path)
