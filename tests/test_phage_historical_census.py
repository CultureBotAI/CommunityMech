"""Actual proof and restoration controls for the historical phage census (#2947).

2026-11-16. The shared fixture captures one published proof in an isolated
directory; current canonical/source bytes and historical ledgers stay untouched.
"""

from pathlib import Path

import genus_gtdb_successors as registry
import pytest
import test_phage_review_regressions as phage
import yaml
from test_scoped_gtdb_actual_successor import build_actual

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(params=phage.PHAGE_BEFORE, ids=("467", "468"))
def actual(tmp_path, monkeypatch, request):
    allowed = registry.ALLOWANCES[request.param]
    result = build_actual(
        tmp_path,
        monkeypatch,
        proof_root=ROOT,
        manifest=allowed["manifest"]["path"],
        manifest_sha=allowed["manifest"]["sha256"],
        baseline_revision=allowed["baseline_revision"],
        historical_llm=True,
    )
    monkeypatch.setattr(phage, "ROOT", tmp_path)
    return result


def check(actual):
    root, proof, _, _, _ = actual
    historical = phage._historical_members(root / proof["target"])
    count = 4 if "Alseth" in proof["target"] else 5
    assert len(historical) == count + 1
    assert (
        sum(row["taxon_term"]["gtdb_grounding_status"] == "UNRESOLVED" for row in historical)
        == count
    )
    assert historical[-1]["taxon_term"]["gtdb_grounding_status"] == "NO_GTDB_EQUIVALENT"
    current = yaml.safe_load((root / proof["target"]).read_bytes())
    assert all(
        row["taxon_term"]["gtdb_grounding_status"] != "UNRESOLVED" for row in current["taxonomy"]
    )
    if "PHA_" in proof["target"]:
        phage._review_contract(current)  # Current biology, never a predecessor substitution.


def test_actual_current_proofs_preserve_the_original_phage_census(actual):
    check(actual)


@pytest.mark.parametrize("artifact", ["current", "manifest", "native_recomputation"])
def test_changed_current_or_proof_inputs_refuse_then_restore(actual, artifact):
    root, proof, allowed, _, _ = actual
    check(actual)
    if artifact == "current":
        path = root / proof["target"]
    elif artifact == "manifest":
        path = root / allowed[proof["target"]]["manifest"]["path"]
    else:
        path = root / proof[artifact]["path"]
    original = path.read_bytes()
    path.write_bytes(original + b"\n ")
    assert path.read_bytes() != original
    try:
        with pytest.raises(AssertionError):
            check(actual)
    finally:
        path.write_bytes(original)
    check(actual)


def test_unknown_record_has_no_historical_projection(actual):
    root, _, _, _, _ = actual
    check(actual)
    with pytest.raises(AssertionError, match="no historical phage census allowance"):
        phage._historical_members(root / "kb/communities/Unreviewed.yaml")
    check(actual)
