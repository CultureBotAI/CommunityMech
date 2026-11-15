"""Actual 393/409/338/435 two-transition proofs and tamper controls, 2026-11-15.

Only public artifacts are copied into isolated fixtures. Both historical Git
reads use the actual immutable repository baselines; no mapping core is mocked.
"""

import copy
import json
import subprocess
from pathlib import Path

import pytest
import source_note_gtdb_successor as composite
import source_note_gtdb_successors as registry
from test_scoped_gtdb_actual_successor import (
    build_actual,
    test_actual_rehashed_tampering_refuses_and_restores,  # noqa: F401
    test_actual_shared_engine_successor_admits_and_retains_old_history,  # noqa: F401
)

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(params=tuple(registry.BEFORE))
def case(request):
    target = request.param
    entry = registry.ALLOWANCES[target]
    proof = json.loads((ROOT / entry["manifest"]["path"]).read_bytes())
    return target, entry, proof


@pytest.fixture
def actual(tmp_path, monkeypatch, case):
    allowed = case[2]["mapping_allowance"]
    return build_actual(
        tmp_path,
        monkeypatch,
        proof_root=ROOT,
        manifest=allowed["manifest"]["path"],
        manifest_sha=allowed["manifest"]["sha256"],
        baseline_revision=allowed["baseline_revision"],
        historical_llm=True,
    )


@pytest.fixture
def composed(actual, monkeypatch, case):
    root, _mapping_proof, _mapping_allowed, retained, _historical_llm = actual
    target, entry, original_proof = case
    proof = copy.deepcopy(original_proof)
    allowed = copy.deepcopy(registry.ALLOWANCES)
    names = {entry["manifest"]["path"]}
    names.update(item["path"] for item in proof["note_transition"].values())
    for name in names:
        raw = (ROOT / name).read_bytes()
        retained[name] = raw
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)

    def actual_git(command, *, cwd, **kwargs):
        assert Path(cwd) == root
        assert command[:2] == ["git", "show"] and len(command) == 3
        assert command[2] in {
            f"{entry['baseline_revision']}:{target}",
            f"{original_proof['intermediate_revision']}:{target}",
        }
        return subprocess.run(command, cwd=ROOT, capture_output=True, check=True, **kwargs).stdout

    monkeypatch.setattr(composite.subprocess, "check_output", actual_git)
    return root, proof, allowed, retained, case


def admit(case):
    root, _proof, allowed, _retained, (target, _entry, _original_proof) = case
    return composite.admit(root, target, registry.BEFORE[target], allowed)


def repin(case):
    root, proof, allowed, _retained, (target, _entry, _original_proof) = case
    raw = (json.dumps(proof, indent=2) + "\n").encode()
    item = allowed[target]["manifest"]
    (root / item["path"]).write_bytes(raw)
    item["sha256"] = composite.mapping.digest(raw)


def test_actual_composite_preserves_original_and_real_intermediate(composed):
    target, _entry, original_proof = composed[4]
    result = admit(composed)
    assert result.changed
    assert result.current_sha256 == original_proof["after_sha256"]
    assert composite.mapping.digest(result.historical_bytes) == registry.BEFORE[target]
    assert result.historical_bytes != (composed[0] / target).read_bytes()


@pytest.mark.parametrize(
    "key", ["source_plan", "application_receipt", "stage_receipt", "history_sidecar"]
)
def test_actual_rehashed_note_artifact_requires_saved_binding(composed, key):
    assert admit(composed).changed
    root, proof, _allowed, _retained, _case = composed
    item = proof["note_transition"][key]
    original_item = copy.deepcopy(item)
    location = root / item["path"]
    original = location.read_bytes()
    changed = original + b"\n "
    location.write_bytes(changed)
    item["sha256"] = composite.mapping.digest(changed)
    if "raw_sha256" in item:
        item["raw_sha256"] = item["sha256"]
    repin(composed)
    with pytest.raises(AssertionError, match="saved input differs"):
        admit(composed)
    location.write_bytes(original)
    proof["note_transition"][key] = original_item
    repin(composed)
    assert admit(composed).changed


@pytest.mark.parametrize("field", ["before", "after", "existing_stock", "existing_descriptor"])
def test_actual_note_projection_refuses_changed_scope_and_restores(composed, field):
    root, proof, _allowed, _retained, (target, entry, _original_proof) = composed
    original = composite.historical_bytes(root, entry["baseline_revision"], target)
    intermediate = composite.historical_bytes(root, proof["intermediate_revision"], target)
    note = {
        key: json.loads((root / proof["note_transition"][key]["path"]).read_bytes())
        for key in ("source_plan", "application_receipt", "stage_receipt")
    }
    plan = copy.deepcopy(note["source_plan"])
    plan["notes"][0][field] = "unreviewed"
    with pytest.raises(AssertionError, match="known old|undeclared content"):
        composite.verify_note_transition(
            original, intermediate, plan, note["application_receipt"], note["stage_receipt"]
        )
    composite.verify_note_transition(
        original,
        intermediate,
        note["source_plan"],
        note["application_receipt"],
        note["stage_receipt"],
    )
    assert admit(composed).changed


def test_actual_wrong_baseline_and_unknown_changed_record_refuse(composed):
    assert admit(composed).changed
    root, proof, _allowed, _retained, (target, entry, _original_proof) = composed
    saved = copy.deepcopy(proof)
    proof["intermediate_revision"] = entry["baseline_revision"]
    proof["mapping_allowance"]["baseline_revision"] = entry["baseline_revision"]
    repin(composed)
    with pytest.raises(AssertionError, match="exact composite chain"):
        admit(composed)
    proof.clear()
    proof.update(saved)
    repin(composed)
    with pytest.raises(AssertionError, match="unknown changed record"):
        registry.admit_note_mapping_successor(
            root, "kb/communities/Unreviewed.yaml", registry.BEFORE[target], current=b"changed"
        )
    assert admit(composed).changed


def test_registry_uses_the_actual_frozen_composite(case):
    target, entry, proof = case
    assert (
        composite.mapping.digest((ROOT / entry["manifest"]["path"]).read_bytes())
        == entry["manifest"]["sha256"]
    )
    result = registry.admit_note_mapping_successor(ROOT, target, registry.BEFORE[target])
    assert result.changed and result.current_sha256 == proof["after_sha256"]
