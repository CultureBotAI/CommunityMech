"""Exercise third-group public proofs through the unchanged shared mutation engine.

#2848, 2026-11-15. Exact production registry pins and public evidence only.
The B8-1 canary precedes all remaining applications; no scientific predicates
or admission policy are replaced by this fixture adapter.
"""

from pathlib import Path

import pytest
import scoped_gtdb_successor as successor
import test_scoped_gtdb_actual_successor as controls
from gtdb_species_batch_successors_20261115 import ALLOWANCES

ROOT = Path(__file__).resolve().parents[1]
TARGETS = {
    "549": "data/isolates/Bacillus_Paramycoides_B81_PAH_Biodegradation_Isolate_Baseline.yaml",
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


def test_unlisted_changed_record_cannot_reuse_third_species_proof(actual):
    root, proof, _allowed, _retained, _historical_llm = actual
    unrelated = "kb/communities/Unlisted_third_species_record.yaml"
    (root / unrelated).parent.mkdir(parents=True, exist_ok=True)
    (root / unrelated).write_bytes((root / proof["target"]).read_bytes())
    with pytest.raises(AssertionError, match="unknown changed record"):
        successor.admit(root, unrelated, proof["before_sha256"], ALLOWANCES)
    assert controls.check(actual).changed
