"""Require exact native inspection coverage for batch diagnostics, #2864, 2026-11-15."""

import copy
import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def case(tmp_path, monkeypatch):
    monkeypatch.syspath_prepend(str(ROOT / "scripts/adhoc"))
    source = ROOT / "scripts/adhoc/build_gtdb_batch_diagnostic_20261115.py"
    spec = importlib.util.spec_from_file_location("batch_review_capture", source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    monkeypatch.setattr(module, "ROOT", tmp_path)
    captured = {tmp_path / "record.yaml": b"accepted record", tmp_path / "source.json": b"source"}
    inspection = {
        "source": {
            "git_revision": "f" * 40,
            "inputs": [
                {"path": p.name, "sha256": module.core.sha(raw)} for p, raw in captured.items()
            ],
        }
    }
    return module, captured, inspection


def test_complete_exact_native_inspection_control(case):
    module, captured, inspection = case
    module.verify_inspection(inspection, captured, "f" * 40)


@pytest.mark.parametrize("mutation", ["transient", "missing", "extra", "duplicate", "revision"])
def test_inspection_deviation_refuses_and_restored_control_passes(case, mutation):
    module, captured, inspection = case
    altered = copy.deepcopy(inspection)
    rows = altered["source"]["inputs"]
    if mutation == "transient":
        rows[0]["sha256"] = "0" * 64
    elif mutation == "missing":
        rows.pop()
    elif mutation == "extra":
        rows.append({"path": "unassessed.yaml", "sha256": "0" * 64})
    elif mutation == "duplicate":
        rows.append(copy.deepcopy(rows[0]))
    else:
        altered["source"]["git_revision"] = "0" * 40
    with pytest.raises(ValueError, match="complete assessed capture"):
        module.verify_inspection(altered, captured, "f" * 40)
    module.verify_inspection(inspection, captured, "f" * 40)
