"""Actual 393 two-transition proof, native matrix and tamper controls, 2026-11-15.

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
TARGET = registry.TARGET
ENTRY = registry.ALLOWANCES[TARGET]
COMPOSITE = json.loads((ROOT / ENTRY["manifest"]["path"]).read_bytes())


@pytest.fixture
def actual(tmp_path, monkeypatch):
    allowed = COMPOSITE["mapping_allowance"]
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
def composed(actual, monkeypatch):
    root, _mapping_proof, _mapping_allowed, retained, _historical_llm = actual
    proof = copy.deepcopy(COMPOSITE)
    allowed = copy.deepcopy(registry.ALLOWANCES)
    names = {ENTRY["manifest"]["path"]}
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
            f"{ENTRY['baseline_revision']}:{TARGET}",
            f"{COMPOSITE['intermediate_revision']}:{TARGET}",
        }
        return subprocess.run(command, cwd=ROOT, capture_output=True, check=True, **kwargs).stdout

    monkeypatch.setattr(composite.subprocess, "check_output", actual_git)
    return root, proof, allowed, retained


def admit(case):
    root, _proof, allowed, _retained = case
    return composite.admit(root, TARGET, registry.BEFORE[TARGET], allowed)


def repin(case):
    root, proof, allowed, _retained = case
    raw = (json.dumps(proof, indent=2) + "\n").encode()
    item = allowed[TARGET]["manifest"]
    (root / item["path"]).write_bytes(raw)
    item["sha256"] = composite.mapping.digest(raw)


def test_actual_composite_preserves_original_and_real_intermediate(composed):
    result = admit(composed)
    assert result.changed
    assert result.current_sha256 == COMPOSITE["after_sha256"]
    assert composite.mapping.digest(result.historical_bytes) == registry.BEFORE[TARGET]
    assert result.historical_bytes != (composed[0] / TARGET).read_bytes()


@pytest.mark.parametrize(
    "key", ["source_plan", "application_receipt", "stage_receipt", "history_sidecar"]
)
def test_actual_rehashed_note_artifact_requires_saved_binding(composed, key):
    assert admit(composed).changed
    root, proof, _allowed, _retained = composed
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
    root, proof, _allowed, _retained = composed
    original = composite.historical_bytes(root, ENTRY["baseline_revision"], TARGET)
    intermediate = composite.historical_bytes(root, proof["intermediate_revision"], TARGET)
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
    root, proof, _allowed, _retained = composed
    saved = copy.deepcopy(proof)
    proof["intermediate_revision"] = ENTRY["baseline_revision"]
    proof["mapping_allowance"]["baseline_revision"] = ENTRY["baseline_revision"]
    repin(composed)
    with pytest.raises(AssertionError, match="exact composite chain"):
        admit(composed)
    proof.clear()
    proof.update(saved)
    repin(composed)
    with pytest.raises(AssertionError, match="unknown changed record"):
        registry.admit_note_mapping_successor(
            root, "kb/communities/Unreviewed.yaml", registry.BEFORE[TARGET], current=b"changed"
        )
    assert admit(composed).changed


def test_registry_uses_the_actual_frozen_composite():
    assert (
        composite.mapping.digest((ROOT / ENTRY["manifest"]["path"]).read_bytes())
        == ENTRY["manifest"]["sha256"]
    )
    result = registry.admit_note_mapping_successor(ROOT, TARGET, registry.BEFORE[TARGET])
    assert result.changed and result.current_sha256 == COMPOSITE["after_sha256"]
