"""Three actual status-only proofs reuse shared tamper controls, #2848, 2026-11-15."""

import json
from pathlib import Path

import ambiguity_gtdb_successors as registry
import pytest
from test_scoped_gtdb_actual_successor import (
    build_actual,
    test_actual_rehashed_tampering_refuses_and_restores,  # noqa: F401
    test_actual_shared_engine_successor_admits_and_retains_old_history,  # noqa: F401
)

ROOT = Path(__file__).resolve().parents[1]
TARGETS = {
    "373": "kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml",
    "365": "kb/communities/Baijiu_Pit_Mud_Hexanoic_Acid_SynCom_G4.yaml",
    "003": "kb/communities/At_RSPHERE_SynCom.yaml",
}


@pytest.fixture(params=TARGETS, ids=TARGETS)
def actual(tmp_path, monkeypatch, request):
    allowed = registry.ALLOWANCES[TARGETS[request.param]]
    return build_actual(
        tmp_path,
        monkeypatch,
        proof_root=ROOT,
        manifest=allowed["manifest"]["path"],
        manifest_sha=allowed["manifest"]["sha256"],
        baseline_revision=allowed["baseline_revision"],
        historical_llm=True,
    )


@pytest.mark.parametrize("target", TARGETS.values(), ids=TARGETS)
def test_registry_admits_actual_refuses_unknown_change_and_restores(target):
    allowed = registry.ALLOWANCES[target]
    proof = json.loads((ROOT / allowed["manifest"]["path"]).read_bytes())
    assert registry.BEFORE[target] == proof["before_sha256"]
    result = registry.admit_status_successor(ROOT, target, registry.BEFORE[target])
    assert result.changed and result.current_sha256 == proof["after_sha256"]
    with pytest.raises(AssertionError, match="unknown changed record"):
        registry.admit_status_successor(
            ROOT, "kb/communities/Unreviewed.yaml", proof["before_sha256"], current=b"changed"
        )
    assert registry.admit_status_successor(ROOT, target, registry.BEFORE[target]).changed
