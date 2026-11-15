"""Actual genus proofs share the full positive/mutation engine, #2848, 2026-11-15."""

import json
from pathlib import Path

import genus_gtdb_successors as registry
import pytest
from test_scoped_gtdb_actual_successor import (
    build_actual,
    test_actual_rehashed_tampering_refuses_and_restores,  # noqa: F401
    test_actual_shared_engine_successor_admits_and_retains_old_history,  # noqa: F401
)

ROOT = Path(__file__).resolve().parents[1]
TARGETS = {
    "467": "kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml",
    "475": "kb/communities/Cold_Seep_ANME_SRB_Carbon_Monoxide_Syntrophic_Consortium.yaml",
    "350": "kb/communities/High_Ammonia_Biogas_0B_Butyrate_Oxidizing_Enrichment.yaml",
    "364": "kb/communities/Sclerotinia_Sclerotia_12Strain_Biocontrol_SynCom.yaml",
    "458": "kb/communities/Alfalfa_Stress_Adapted_Bacterial_SynCom.yaml",
    "456": "kb/communities/Caragana_Wheat_Drought_SynCom15.yaml",
    "384": "kb/communities/Dairy_Wastewater_Algal_Cyanobacterial_Cultivation_Panel.yaml",
    "415": "kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml",
    "477": "kb/communities/Cucumber_Low_Phosphorus_Cross_Kingdom_Biocontrol_SynCom.yaml",
    "353": "kb/communities/Hualgayoc_Acidic_Sulfate_Reducing_AMD_Consortium.yaml",
    "440": "kb/communities/Electrostimulated_Toluene_Methanogenic_Microbiota.yaml",
    "447": "kb/communities/Brocadia_Low_Nitrogen_Anammox_Consortium.yaml",
    "433": "kb/communities/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium.yaml",
    "474": "kb/communities/Whale_Fall_Vallitalea_Trichloromonas_Chitin_EET_Consortium.yaml",
    "403": "kb/communities/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom.yaml",
    "410": "kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml",
    "372": "kb/communities/Pseudomonas_Klebsiella_Alcaligenes_FeII_Nitrogen_Removal_SynCom.yaml",
    "349": "kb/communities/Bothnian_Bay_GAC_Dependent_CIET_SAO_Consortium.yaml",
    "424": "kb/communities/QY2S1_Dehalogenimonas_BFR_Bioremediation_Consortium.yaml",
    "342": "kb/communities/Nitratireductor_Gordonia_Z123_LDPE_Degradation_SynCom.yaml",
    "390": "kb/communities/Microalgae_Cyanobacteria_Bioactive_Peptide_Consortia.yaml",
    "406": "kb/communities/Meghalaya_Bacillus_Consortia_A22ED9.yaml",
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
def test_production_registry_admits_exact_actual_and_refuses_unlisted_change(target):
    allowed = registry.ALLOWANCES[target]
    proof = json.loads((ROOT / allowed["manifest"]["path"]).read_bytes())
    result = registry.admit_genus_successor(ROOT, target, proof["before_sha256"])
    assert result.changed and result.current_sha256 == proof["after_sha256"]
    with pytest.raises(AssertionError, match="unknown changed record"):
        registry.admit_genus_successor(
            ROOT, "kb/communities/Unreviewed.yaml", proof["before_sha256"], current=b"changed"
        )
    assert registry.admit_genus_successor(ROOT, target, proof["before_sha256"]).changed
