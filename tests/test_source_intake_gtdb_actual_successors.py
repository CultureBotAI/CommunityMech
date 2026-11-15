"""Reuse actual-proof mutation controls for source intake, #2848, 2026-11-15."""

import json
from pathlib import Path

import pytest
import source_intake_gtdb_successors as registry
from test_scoped_gtdb_actual_successor import (
    build_actual,
    test_actual_rehashed_tampering_refuses_and_restores,  # noqa: F401
    test_actual_shared_engine_successor_admits_and_retains_old_history,  # noqa: F401
)

ROOT = Path(__file__).resolve().parents[1]
TARGETS = {"344": registry.KZ_PATH}


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
    result = registry.admit_source_intake_successor(ROOT, target, registry.BEFORE[target])
    assert result.changed and result.current_sha256 == proof["after_sha256"]
    with pytest.raises(AssertionError, match="unknown changed record"):
        registry.admit_source_intake_successor(
            ROOT, "kb/communities/Unreviewed.yaml", proof["before_sha256"], current=b"changed"
        )
    assert registry.admit_source_intake_successor(ROOT, target, registry.BEFORE[target]).changed
