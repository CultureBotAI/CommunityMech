"""Native gate scope/hash controls for reusable GTDB exports, #2848, 2026-11-15."""

import copy
import importlib.util
import json
import shlex
from pathlib import Path

import pytest


@pytest.fixture
def gate(tmp_path, monkeypatch):
    root = Path(__file__).resolve().parents[1]
    monkeypatch.syspath_prepend(str(root / "scripts/adhoc"))
    spec = importlib.util.spec_from_file_location(
        "gtdb_export_gate_test", root / "scripts/adhoc/export_scoped_gtdb_evidence_20261115.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    monkeypatch.setattr(module, "ROOT", tmp_path)
    monkeypatch.setattr(module.audit, "ROOT", tmp_path)
    row = {
        "target": "data/isolates/test.yaml",
        "target_id": "CommunityMech:000555",
        "after_sha256": "a" * 64,
    }
    command = ["just", "--verbose", "--no-dotenv", "--color", "never", "validate", row["target"]]
    directory = tmp_path / ".temp/schema"
    log = b"Native schema check passed\n"
    receipt = {
        "revision": "b" * 40,
        "plan": False,
        "inputs": {"/native/root/" + row["target"]: row["after_sha256"]},
        "exit_code": 0,
        "finished_at": "2026-11-15T00:00:00Z",
        "execution_inputs_unchanged": True,
        "log_sha256": module.audit.digest(log),
        "log_bytes": len(log),
        "command": command,
    }
    captured = {
        directory / "receipt.json": json.dumps(receipt).encode(),
        directory / "native.log": log,
        directory / "native.exit": b"0\n",
    }
    review = {
        "source": {"inputs": []},
        "checks": [
            {
                "check_id": "schema",
                "required": True,
                "status": "passed",
                "exit_code": 0,
                "target_ids": [row["target_id"]],
                "command": shlex.join(command),
            }
        ],
    }
    rebind(module, review, captured)
    return module, review, captured, row, directory, receipt


def rebind(module, review, captured):
    review["source"]["inputs"] = [
        {"path": str(path.relative_to(module.ROOT)), "sha256": module.audit.digest(raw)}
        for path, raw in captured.items()
    ]


def invoke(gate):
    module, review, captured, row, directory, _receipt = gate
    return module.gate_payload(review, captured, row, "schema", directory, "schema", "b" * 40)


def test_actual_scope_and_raw_hashes_are_retained(gate):
    module, _review, captured, _row, directory, _receipt = gate
    log, exit_raw, raw = invoke(gate)
    receipt = json.loads(raw)
    proof = receipt["public_evidence"]
    assert proof["raw_receipt_sha256"] == module.audit.digest(captured[directory / "receipt.json"])
    assert proof["raw_log_sha256"] == module.audit.digest(captured[directory / "native.log"])
    assert proof["raw_exit_sha256"] == module.audit.digest(exit_raw)
    assert proof["public_log_sha256"] == module.audit.digest(log)


def test_successor_links_each_public_triplet_to_its_bound_raw_bytes(gate):
    module, review, captured, row, directory, _receipt = gate
    values = module.gate_payload(review, captured, row, "schema", directory, "schema", "b" * 40)
    payloads, proof = module.gate_artifacts(
        captured, directory, module.ROOT / "reports", "unit", "schema", "schema", values
    )
    assert proof["check_id"] == "schema" and set(proof) == {"check_id", "log", "exit", "receipt"}
    for key, raw_name in (
        ("log", "native.log"),
        ("exit", "native.exit"),
        ("receipt", "receipt.json"),
    ):
        item = proof[key]
        assert item["sha256"] == module.audit.digest(payloads[module.ROOT / item["path"]])
        assert item["raw_path"] == str((directory / raw_name).relative_to(module.ROOT))
        assert item["raw_sha256"] == module.audit.digest(captured[directory / raw_name])
    assert proof["receipt"]["sha256"] != proof["receipt"]["raw_sha256"]
    source = directory / "native.log"
    saved = captured.pop(source)
    with pytest.raises(KeyError):
        module.gate_artifacts(
            captured, directory, module.ROOT / "reports", "unit", "schema", "schema", values
        )
    captured[source] = saved
    assert module.gate_artifacts(
        captured, directory, module.ROOT / "reports", "unit", "schema", "schema", values
    ) == (payloads, proof)


@pytest.mark.parametrize(
    "mutation",
    [
        "revision",
        "plan",
        "record_hash",
        "exit",
        "log",
        "command",
        "saved_target",
        "required",
        "unchanged",
    ],
)
def test_rehashed_wrong_gate_refuses_and_restored_control_passes(gate, mutation):
    module, review, captured, row, directory, receipt = gate
    old_review, old_capture = copy.deepcopy(review), captured.copy()
    changed = copy.deepcopy(receipt)
    if mutation == "revision":
        changed["revision"] = "c" * 40
    elif mutation == "plan":
        changed["plan"] = True
    elif mutation == "record_hash":
        changed["inputs"]["/native/root/" + row["target"]] = "c" * 64
    elif mutation == "exit":
        changed["exit_code"] = 1
        captured[directory / "native.exit"] = b"1\n"
    elif mutation == "log":
        captured[directory / "native.log"] = b"unbound different log\n"
    elif mutation == "command":
        changed["command"][-1] = "data/isolates/other.yaml"
        review["checks"][0]["command"] = shlex.join(changed["command"])
    elif mutation == "saved_target":
        review["checks"][0]["target_ids"] = ["CommunityMech:000001"]
    elif mutation == "required":
        review["checks"][0]["required"] = False
    else:
        changed["execution_inputs_unchanged"] = False
    captured[directory / "receipt.json"] = json.dumps(changed).encode()
    rebind(module, review, captured)
    with pytest.raises(ValueError):
        invoke(gate)
    review.clear()
    review.update(old_review)
    captured.clear()
    captured.update(old_capture)
    assert invoke(gate)[1] == b"0\n"


def test_metadata_copy_is_byte_identical_and_bound(gate):
    module, review, captured, _row, directory, _receipt = gate
    source = directory / "source.json"
    captured[source] = b'{"native_result":{"via":"ncbi_id"}}\n'
    rebind(module, review, captured)
    raw, artifact = module.raw_metadata(
        review, source, module.ROOT / "reports/source.json", captured
    )
    assert raw == captured[source]
    assert artifact["sha256"] == artifact["raw_sha256"] == module.audit.digest(raw)


def test_metadata_requiring_redaction_cannot_be_byte_identical(gate):
    module, review, captured, _row, directory, _receipt = gate
    source = directory / "source.json"
    captured[source] = b'{"path":"/Users/example/private/input"}\n'
    rebind(module, review, captured)
    with pytest.raises(ValueError, match="private content"):
        module.raw_metadata(review, source, module.ROOT / "reports/source.json", captured)


@pytest.mark.parametrize("overlap", ["exporter", "auditor", "redactor", "config"])
def test_overlapping_reviewed_implementation_cannot_replace_capture(gate, overlap):
    module, _review, _captured, _row, _directory, _receipt = gate
    source = module.ROOT / (overlap + ".txt")
    original = b"exact bytes already bound by saved review\n"
    source.write_bytes(original)
    captured = {source: original}
    source.write_bytes(b"changed after native validate_pair\n")
    module.capture_additional(captured, [source])
    assert captured[source] == original
    output = module.ROOT / "reports/restored.json"
    with pytest.raises(ValueError, match="captured input changed"):
        module.audit.publish(captured, {output: b"public metadata\n"})
    assert not output.exists()
    source.write_bytes(original)
    module.audit.publish(captured, {output: b"public metadata\n"})
    assert output.read_bytes() == b"public metadata\n"
