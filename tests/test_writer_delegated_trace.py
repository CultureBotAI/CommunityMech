"""Recognize actual reviewed delegation, never a filename exemption (#2857)."""

import hashlib
import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
WRITER = "scripts/adhoc/apply_code006_genus_grounding_20261115.py"
DELEGATE = "scripts/adhoc/stage_code006_genus_grounding_20261115.py"


@pytest.fixture
def harness(tmp_path, monkeypatch):
    spec = importlib.util.spec_from_file_location(
        "delegated_audit", ROOT / "scripts/audit_writers.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    monkeypatch.setattr(module, "_ROOT", tmp_path, raising=False)
    for name in (WRITER, DELEGATE):
        path = tmp_path / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes((ROOT / name).read_bytes())
    return module, tmp_path


def test_exact_guarded_delegate_retains_trace_and_write_guards(harness):
    module, root = harness
    row = module.audit(root / WRITER, "")
    assert row["writes_yaml"] == "yes"
    assert row["appends_curation_history"] == "yes"
    assert row["has_write_safeguard"] == "yes"
    assert row["validates_before_write"] == "yes"


@pytest.mark.parametrize("mutation", ["check", "delegate", "event", "guard", "hash", "missing"])
def test_changed_or_missing_implementation_refused_then_restored(harness, mutation):
    module, root = harness
    writer = root / WRITER
    assert module.audit(writer, "")["appends_curation_history"] == "yes"
    path = root / (WRITER if mutation in {"check", "delegate", "guard", "hash"} else DELEGATE)
    original = path.read_bytes()
    if mutation == "missing":
        path.unlink()
    elif mutation == "hash":
        path.write_bytes(original + b"\n# unreviewed implementation change\n")
    else:
        old, new = {
            "check": (b"= check(original, stage,", b"= unchecked(original, stage,"),
            "delegate": (b"staging.verify_semantics(", b"staging.unchecked_semantics("),
            "event": (b"native.record_curation_event(", b"native.unchecked_event("),
            "guard": (b"guarded.digest(candidate) != candidate_sha", b"False"),
        }[mutation]
        assert original.count(old) == 1
        path.write_bytes(original.replace(old, new))
        assert path.read_bytes() != original
    assert module.audit(writer, "")["appends_curation_history"] == "no"
    assert module.audit(writer, "")["has_write_safeguard"] == "no"
    path.write_bytes(original)
    assert module.audit(writer, "")["appends_curation_history"] == "yes"


@pytest.mark.parametrize(
    "filename,old,new",
    [
        (WRITER, b"= check(original, stage,", b"= unchecked(original, stage,"),
        (WRITER, b"staging.verify_semantics(", b"staging.unchecked_semantics("),
        (WRITER, b"guarded.verify_inputs(receipt)", b"guarded.unchecked_inputs(receipt)"),
        (WRITER, b"guarded.write_validated_community(", b"guarded.unchecked_writer("),
        (DELEGATE, b"native.record_curation_event(", b"native.unchecked_event("),
    ],
)
def test_structural_calls_required_even_with_test_only_updated_hash(
    harness, monkeypatch, filename, old, new
):
    """Independently exercise AST guards beyond the immutable-hash guard."""
    module, root = harness
    writer, path = root / WRITER, root / filename
    assert module._reviewed_delegated_trace(writer)
    original = path.read_bytes()
    expected_count = 2 if old == b"guarded.verify_inputs(receipt)" else 1
    assert original.count(old) == expected_count
    changed = original.replace(old, new)
    path.write_bytes(changed)
    assert path.read_bytes() != original
    original_contract = module._DELEGATED_TRACE[WRITER]
    contract = list(original_contract)
    contract[0 if filename == WRITER else 2] = hashlib.sha256(changed).hexdigest()
    monkeypatch.setattr(module, "_DELEGATED_TRACE", {WRITER: tuple(contract)})
    assert not module._reviewed_delegated_trace(writer)
    path.write_bytes(original)
    monkeypatch.setattr(module, "_DELEGATED_TRACE", {WRITER: original_contract})
    assert module._reviewed_delegated_trace(writer)
