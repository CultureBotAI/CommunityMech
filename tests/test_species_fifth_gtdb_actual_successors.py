"""Admit the fifth-group proofs through the unchanged shared mutation engine.

#2848, 2026-11-15. The Apple canary precedes the remaining eligible records.
Explicit production pins and public evidence preserve all prior biology;
the separate wetland stock-identity and causality findings remain held.
"""

from pathlib import Path

import pytest
import scoped_gtdb_successor as successor
import test_scoped_gtdb_actual_successor as controls
from gtdb_species_batch_successors_20261115 import ALLOWANCES, admission

ROOT = Path(__file__).resolve().parents[1]
TARGETS = {
    "377": "kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml",
}


@pytest.fixture(params=TARGETS, ids=TARGETS)
def actual(tmp_path, monkeypatch, request):
    target = TARGETS[request.param]
    pin = ALLOWANCES[target]
    result = controls.build_actual(
        tmp_path,
        monkeypatch,
        proof_root=ROOT,
        manifest=pin["manifest"]["path"],
        manifest_sha=pin["manifest"]["sha256"],
        baseline_revision=pin["baseline_revision"],
        historical_llm=True,
    )
    assert result[1]["target"] == target
    assert result[2] == {target: pin}
    return result


test_actual_shared_engine_successor_admits_and_retains_old_history = (
    controls.test_actual_shared_engine_successor_admits_and_retains_old_history
)
test_actual_rehashed_tampering_refuses_and_restores = (
    controls.test_actual_rehashed_tampering_refuses_and_restores
)


def test_unlisted_changed_record_cannot_reuse_fifth_species_proof(actual):
    root, proof, _allowed, _retained, _historical_llm = actual
    unrelated = "kb/communities/Unlisted_fifth_species_record.yaml"
    (root / unrelated).parent.mkdir(parents=True, exist_ok=True)
    (root / unrelated).write_bytes((root / proof["target"]).read_bytes())
    with pytest.raises(AssertionError, match="unknown changed record"):
        successor.admit(root, unrelated, proof["before_sha256"], ALLOWANCES)
    assert controls.check(actual).changed


def test_current_apple_record_has_strict_production_admission():
    result = admission(
        ROOT,
        TARGETS["377"],
        "1f2e836d0bcd5ff68622188aa5eff6d82b0d7c30d9c1a0b6191ea52f0a8e0a94",
    )
    assert result.changed
    assert result.current_sha256 == (
        "9c99bb5106378c324d3fc54e96399291a7b408abdef6827f98ac59801f555b0f"
    )
