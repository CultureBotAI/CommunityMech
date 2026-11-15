"""Exercise nine actual species proofs through the shared mutation engine.

#2848, 2026-11-15. Explicit production pins, public artifacts and historical
Git bytes only; each mutation is refused and restored in an isolated fixture.
"""

from pathlib import Path

import pytest
import test_scoped_gtdb_actual_successor as controls
from gtdb_species_batch_successors_20261115 import ALLOWANCES

ROOT = Path(__file__).resolve().parents[1]
TARGETS = {
    "053": "kb/communities/Phenol_Carboxylation_Consortium.yaml",
    "313": "kb/communities/Chlorella_Keystone_Taxa_Antifungal_SynCom.yaml",
    "362": "kb/communities/Sphingobium_Nitrososphaera_Phenanthrene_Carbon_SynCom.yaml",
    "396": "kb/communities/Clostridial_isoDCA_Mini_Consortium.yaml",
    "397": "kb/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.yaml",
    "426": "kb/communities/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium.yaml",
    "431": "kb/communities/Parmigiano_NWS_Set2_LAB_Triculture.yaml",
    "517": "kb/communities/Parmigiano_NWS_Set1_LAB_Triculture.yaml",
    "522": "kb/communities/Parmigiano_NWS_Set3_LAB_Triculture.yaml",
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
