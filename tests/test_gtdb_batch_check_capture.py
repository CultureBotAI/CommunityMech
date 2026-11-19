"""Protect captured AFTER bytes and actual gate receipts, #2848, 2026-11-15."""

import importlib.util
import json
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def harness(tmp_path, monkeypatch):
    source = ROOT / "scripts/adhoc/check_gtdb_batch_unit_20261115.py"
    spec = importlib.util.spec_from_file_location("batch_check_capture", source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    root = tmp_path / "repo"
    state = root / ".temp/unit"
    state.mkdir(parents=True)
    target = root / "data/isolates/Fixture.yaml"
    target.parent.mkdir(parents=True)
    target.write_bytes(b"accepted current fixture")
    table = state / "kg-microbe/data/raw/NCBI2GTDB.tsv.gz"
    table.parent.mkdir(parents=True)
    table.write_bytes(b"synthetic retained mapping")
    applied = state / "applied/receipt.json"
    applied.parent.mkdir()
    before = applied.with_name("before.yaml")
    before.write_bytes(b"original fixture")
    receipt = {
        "applied": True,
        "execution_revision": "f" * 40,
        "target": str(target.relative_to(root)),
        "before_sha256": module.digest(before.read_bytes()),
        "after_sha256": module.digest(target.read_bytes()),
        "inputs": {
            str(p.relative_to(root)): module.digest(p.read_bytes()) for p in (target, table)
        },
    }
    # The actual application inputs describe the original target.
    receipt["inputs"][receipt["target"]] = receipt["before_sha256"]
    applied.write_text(json.dumps(receipt))
    config = state / "check.json"
    config.write_text(
        json.dumps(
            {
                "target": receipt["target"],
                "after_sha256": receipt["after_sha256"],
                "before_sha256": receipt["before_sha256"],
                "application_receipt": str(applied.relative_to(root)),
                "application_receipt_sha256": module.digest(applied.read_bytes()),
                "crosswalk": str(table.relative_to(root)),
                "crosswalk_sha256": module.digest(table.read_bytes()),
            }
        )
    )
    for name in (
        "uv.lock",
        "justfile",
        "src/communitymech/schema/communitymech.yaml",
        "src/communitymech/schema/history.yaml",
    ):
        p = root / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(b"fixed fixture dependency")
    helper_copy = root / source.relative_to(ROOT)
    helper_copy.parent.mkdir(parents=True)
    helper_copy.write_bytes(source.read_bytes())
    monkeypatch.setattr(module, "ROOT", root)
    monkeypatch.setattr(module, "__file__", str(helper_copy))
    monkeypatch.setattr(module, "head", lambda _root=None: "f" * 40)
    calls = []

    def native(command, **kwargs):
        calls.append(command)
        kwargs["stdout"].write(b"fixture native output persisted\n")
        return subprocess.CompletedProcess(command, 0)

    monkeypatch.setattr(module.subprocess, "run", native)
    return module, root, target, config, table, calls


def invoke(harness, suffix="001"):
    module, root, _, config, *_ = harness
    return module.run(
        str(config.relative_to(root)),
        module.digest(config.read_bytes()),
        "schema",
        ".temp/unit/check-" + suffix,
        "f" * 40,
    )


def test_actual_triplet_and_captured_target_persist(harness):
    module, root, target, _, _, calls = harness
    result = invoke(harness)
    assert result["inputs"][str(target)] == module.digest(target.read_bytes())
    assert result["execution_inputs_unchanged"] and len(calls) == 1
    output = root / ".temp/unit/check-001"
    assert (output / "native.exit").read_bytes() == b"0\n"
    assert (output / "native.log").stat().st_size > 0
    assert json.loads((output / "receipt.json").read_bytes()) == result


def test_target_mutated_before_capture_is_refused_and_restore_runs(harness, monkeypatch):
    module, _, target, _, _, calls = harness
    before = target.read_bytes()
    capture = module.capture

    def mutate(captured, location, expected=None):
        if location == target:
            target.write_bytes(b"transient unreviewed target")
        return capture(captured, location, expected)

    monkeypatch.setattr(module, "capture", mutate)
    with pytest.raises(ValueError, match="accepted input changed"):
        invoke(harness)
    assert not calls
    target.write_bytes(before)
    monkeypatch.setattr(module, "capture", capture)
    assert invoke(harness)["exit_code"] == 0


@pytest.mark.parametrize("changed", ["target", "table"])
def test_change_during_gate_cannot_get_success_receipt(harness, monkeypatch, changed):
    module, root, target, _, table, _ = harness
    actual = module.subprocess.run
    location = target if changed == "target" else table
    before = location.read_bytes()

    def mutate(command, **kwargs):
        result = actual(command, **kwargs)
        location.write_bytes(before + b" changed")
        return result

    monkeypatch.setattr(module.subprocess, "run", mutate)
    with pytest.raises(ValueError, match="execution inputs changed"):
        invoke(harness)
    assert (root / ".temp/unit/check-001/native.exit").read_bytes() == b"0\n"
    assert not (root / ".temp/unit/check-001/receipt.json").exists()
    location.write_bytes(before)
    monkeypatch.setattr(module.subprocess, "run", actual)
    assert invoke(harness, "restored")["exit_code"] == 0
