"""Real native matcher and captured-input controls for the fixed471 wrapper."""

import importlib.util
import json
from pathlib import Path

import pytest

from tests.test_reference_assertion_coverage import fixture_repo  # noqa: F401

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "wetland_measured", ROOT / "scripts/adhoc/measure_wetland_identity_references_20261115.py"
)
wrapper = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(wrapper)


@pytest.fixture
def working(fixture_repo, monkeypatch):  # noqa: F811
    root = fixture_repo
    target = root / wrapper.TARGET
    target.parent.mkdir(parents=True)
    target.write_text(json.dumps({"evidence": [{"reference": "PMID:1", "snippet": "alpha"}]}))
    for name in ("uv.lock", "pyproject.toml", "scripts/reference_assertion_coverage.py"):
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("fixture implementation\n")
    helper = root / "scripts/adhoc/measure.py"
    helper.parent.mkdir(parents=True)
    helper.write_text("fixture wrapper\n")
    monkeypatch.setattr(wrapper, "ROOT", root)
    monkeypatch.setattr(wrapper, "__file__", str(helper))
    monkeypatch.setattr(wrapper.native, "git", lambda *args: wrapper.REVISION)
    monkeypatch.setattr(wrapper, "AFTER", wrapper.native.digest(target.read_bytes()))
    return root, target


def test_actual_native_positive_mismatch_restoration(working, monkeypatch):
    root, target = working
    original = target.read_bytes()
    receipts = []
    for index, raw in enumerate((original, original.replace(b"alpha", b"absent text"), original)):
        target.write_bytes(raw)
        monkeypatch.setattr(wrapper, "AFTER", wrapper.native.digest(raw))
        receipts.append(wrapper.run(f".temp/case-{index}"))
        measured = json.loads((root / f".temp/case-{index}/measurement.json").read_bytes())
        assert measured["counts"]["snippet_occurrences_compared"] == 1
        assert measured["measurement_valid"]
        assert receipts[-1]["after_sha256"] == wrapper.native.digest(raw)
    assert [r["exit_code"] for r in receipts] == [0, 1, 0]
    assert receipts[0]["counts"] == receipts[2]["counts"]


@pytest.mark.parametrize(
    "name",
    [
        wrapper.TARGET,
        "references_cache/PMID_1.md",
        wrapper.native.CONFIG,
        "scripts/reference_assertion_coverage.py",
        "scripts/adhoc/measure.py",
    ],
)
def test_changed_input_refusal_then_restore(working, monkeypatch, name):
    root, _ = working
    path = root / name
    original = path.read_bytes()
    real = wrapper.native.measure

    def change(*args):
        result = real(*args)
        # Preserve valid YAML so the captured-input comparison, rather than a
        # parser error, must reject the changed configuration (#2956).
        suffix = b"\n# changed\n" if name == wrapper.native.CONFIG else b"\nchanged\n"
        path.write_bytes(original + suffix)
        assert path.read_bytes() != original
        return result

    monkeypatch.setattr(wrapper.native, "measure", change)
    with pytest.raises(ValueError, match="changed"):
        wrapper.run(".temp/refused")
    assert not (root / ".temp/refused/receipt.json").exists()
    assert not (root / ".temp/refused/measurement.json").exists()
    path.write_bytes(original)
    monkeypatch.setattr(wrapper.native, "measure", real)
    assert wrapper.run(".temp/restored")["exit_code"] == 0


def test_plan_exclusive_output_and_wrong_after(working):
    root, target = working
    assert wrapper.run(".temp/plan", plan=True)["plan"]
    assert not (root / ".temp/plan").exists()
    wrapper.run(".temp/actual")
    with pytest.raises(ValueError, match="exclusive"):
        wrapper.run(".temp/actual")
    target.write_bytes(target.read_bytes() + b"\n")
    with pytest.raises(ValueError, match="AFTER"):
        wrapper.run(".temp/wrong-after")
    assert not (root / ".temp/wrong-after").exists()
