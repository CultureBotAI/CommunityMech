"""Verify actual second-group species proofs with the shared mutation engine.

#2848, 2026-11-15. Explicit production pins and public metadata only; the
name-fallback 347 canary precedes any remaining-record application. Original
biological assertions continue to inspect current records in their own callers.
"""

from pathlib import Path

import pytest
import scoped_gtdb_successor as successor
import test_scoped_gtdb_actual_successor as controls
from gtdb_species_batch_successors_20261115 import ALLOWANCES

ROOT = Path(__file__).resolve().parents[1]
TARGETS = {
    "347": "kb/communities/Bacillus_siamensis_vallismortis_HT_Masson_Pine_SynCom.yaml",
    "481": "kb/communities/Delftia_Klebsiella_Light_Driven_Hydrogen_Denitrifying_Coculture.yaml",
    "432": "kb/communities/FourSpecies_Aerobic_Lung_Microbiome_Model.yaml",
    "411": "kb/communities/Glutamicibacter_S11_Aquaculture_Nitrogen_Removal_SynCom.yaml",
    "472": "kb/communities/Halobacillus_Black_Gram_Halophilic_PGPR_Consortium.yaml",
    "341": "kb/communities/Priestia_Pseudomonas_Rice_Arsenic_Stress_SynCom.yaml",
    "361": "kb/communities/RH1_Glyphosate_Streptomyces_Consortium.yaml",
    "378": "kb/communities/Soy_Sauce_Temporal_SevenSpecies_SynCom.yaml",
    "408": "kb/communities/Viili_Fungus_Bacterium_EPS_SynCom.yaml",
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


def test_unlisted_changed_record_cannot_reuse_second_species_proof(actual):
    root, proof, _allowed, _retained, _historical_llm = actual
    unrelated = "kb/communities/Unlisted_second_species_record.yaml"
    (root / unrelated).write_bytes((root / proof["target"]).read_bytes())
    with pytest.raises(AssertionError, match="unknown changed record"):
        successor.admit(root, unrelated, proof["before_sha256"], ALLOWANCES)
    assert controls.check(actual).changed
