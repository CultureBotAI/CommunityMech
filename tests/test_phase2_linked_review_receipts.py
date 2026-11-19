"""Reject substituted/incomplete native proof before linked review save."""

import importlib
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts/adhoc"))
builder = importlib.import_module("build_phase2_linked_review_20261115")


@pytest.fixture
def prepared(tmp_path, monkeypatch):
    state = tmp_path / ".temp/phase2-science-20261115"
    state.mkdir(parents=True)
    monkeypatch.setattr(builder, "ROOT", tmp_path)
    monkeypatch.setattr(builder, "STATE", state)
    target = tmp_path / builder.TARGETS["ecofab"]
    target.parent.mkdir(parents=True)
    target.write_text("record proof fixture\n")
    runner = tmp_path / "scripts/adhoc/check_phase2_linked_records_20261115.py"
    runner.parent.mkdir(parents=True)
    runner.write_text("runner proof fixture\n")
    bound = {builder.TARGETS["ecofab"]: builder.sha(target), "schema.yaml": "schema-hash"}
    monkeypatch.setattr(builder, "current_gate_inputs", lambda: bound)
    name = "linked-ecofab-schema-002"
    log = state / (name + ".log")
    log.write_text("native success fixture\n")
    (state / (name + ".exit")).write_text("0\n")
    receipt = {
        "name": name,
        "head": builder.BASE,
        "record": builder.TARGETS["ecofab"],
        "gate": "schema",
        "command": builder.expected_command("ecofab", "schema", name),
        "exit_code": 0,
        "status": "PASSED",
        "runner_sha256": builder.sha(runner),
        "inputs_unchanged": True,
        "record_worktree_sha256": builder.sha(target),
        "inputs": bound.copy(),
        "log": builder.relative(log),
        "log_sha256": builder.sha(log),
    }
    path = state / (name + ".json")
    path.write_text(json.dumps(receipt))
    return path, receipt, log


def test_complete_current_native_control_accepted(prepared):
    path, receipt, _ = prepared
    assert builder.verify_receipt("ecofab", "schema") == (path, receipt)


@pytest.mark.parametrize(
    "mutation", ["revision", "command", "input_omission", "hash", "changed_flag", "runner"]
)
def test_receipt_scope_and_provenance_mutations_rejected(prepared, mutation):
    path, receipt, _ = prepared
    if mutation == "revision":
        receipt["head"] = "0" * 40
    elif mutation == "command":
        receipt["command"][-1] = builder.TARGETS["lbnl"]
    elif mutation == "input_omission":
        del receipt["inputs"]["schema.yaml"]
    elif mutation == "hash":
        receipt["record_worktree_sha256"] = "0" * 64
    elif mutation == "changed_flag":
        receipt["inputs_unchanged"] = False
    else:
        receipt["runner_sha256"] = "0" * 64
    path.write_text(json.dumps(receipt))
    with pytest.raises(ValueError, match="unbound or incomplete native receipt"):
        builder.verify_receipt("ecofab", "schema")


def test_native_log_mutation_rejected(prepared):
    _, _, log = prepared
    log.write_text("different native outcome\n")
    with pytest.raises(ValueError, match="unbound or incomplete native receipt"):
        builder.verify_receipt("ecofab", "schema")


def test_exit_file_mutation_rejected(prepared):
    path, _, _ = prepared
    path.with_suffix(".exit").write_text("1\n")
    with pytest.raises(ValueError, match="unbound or incomplete native receipt"):
        builder.verify_receipt("ecofab", "schema")
