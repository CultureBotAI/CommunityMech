"""Preserve source, model and completion limits from the seventh graph review."""

from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]


def record(stem):
    return yaml.safe_load((ROOT / "kb/communities" / f"{stem}.yaml").read_text())


def nodes(stem):
    return record(stem)["ecological_interactions"]


@pytest.mark.parametrize(
    "stem,partner,fraction",
    [
        ("BioModels_MODEL1806250003_Spittlebug_Sulcia_Sodalis", "Sodalis", 15),
        ("BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia", "Baumannia", 10),
        ("BioModels_MODEL1806250005_Cicada_Sulcia_Hodgkinia", "Hodgkinia", 30),
    ],
)
def test_insect_flux_fractions_are_not_nitrogen_atom_concentrations(stem, partner, fraction):
    sulcia, other, community = nodes(stem)
    assert "66-80%" in sulcia["description"]
    assert f"{fraction}%" in other["description"]
    assert any(e["snippet"] == f"{fraction}% for {partner}" for e in other["evidence"])
    for node in (sulcia, other, community):
        assert node["interaction_type"] == "MUTUALISM"
        assert not node.get("downstream")
        assert all(e["evidence_source"] == "COMPUTATIONAL" for e in node["evidence"])
        assert all(m["term"]["id"] != "CHEBI:25555" for m in node.get("metabolites", []))
        assert all("concentration" not in m for m in node.get("metabolites", []))
    assert community["evidence"][1]["supports"] == "PARTIAL"


def test_nasal_workflow_and_unverified_mediation_stay_removed():
    exchange, growth = nodes("BioModels_MODEL2209060002_DPigrum_SAureus_Community")
    for node in (exchange, growth):
        assert "interaction_type" not in node
        assert not node.get("downstream")
    assert "does not depend" in exchange["description"]
    assert "objective weights" in growth["description"]
    assert growth["evidence"][0]["supports"] == "PARTIAL"
    assert growth["evidence"][-1]["supports"] == "SUPPORT"


def test_mouse_models_do_not_form_an_aging_to_host_causal_chain():
    beneficial, competitive, host = nodes("BioModels_MODEL2310020001_Mouse_Metaorganism_Model")
    assert competitive["interaction_type"] == "COMPETITION"
    assert "interaction_type" not in beneficial
    assert "interaction_type" not in host
    assert "metabolites" not in beneficial
    assert "metabolites" not in competitive
    assert not any(n.get("downstream") for n in (beneficial, competitive, host))
    assert host["evidence"][1]["supports"] == "PARTIAL"


def test_kefir_preserves_experimental_mutualism_without_recipient_to_pool_arrows():
    proteolysis, suppression, lactate, acetobacter, yeast = nodes(
        "BioModels_MODEL2204300001_Kefir_Community_Model"
    )
    assert proteolysis["interaction_type"] == lactate["interaction_type"] == "MUTUALISM"
    assert proteolysis["downstream"][0]["target"] == lactate["name"]
    assert proteolysis["downstream"][0]["description"].startswith("PARTIAL")
    assert not lactate.get("downstream")
    assert "interaction_type" not in suppression
    for node in (lactate, acetobacter, yeast):
        assert node["metabolites"][0]["term"]["id"] == "CHEBI:24996"
        assert "concentration" not in node["metabolites"][0]
        assert node["evidence"][0]["evidence_source"] == "IN_VITRO"
    assert "7-12" not in lactate["metabolites"][0]["notes"]
    assert "no appreciable" in acetobacter["evidence"][0]["explanation"]
    assert "grow appreciably in plain whey" in yeast["description"]


def test_infant_resource_sharing_keeps_both_qualified_donor_arrows():
    bifido, recipients, other = nodes("BioModels_MODEL2405300001_Infant_Gut_HMO_SynCom")
    for donor in (bifido, other):
        assert donor["downstream"][0]["target"] == recipients["name"]
        assert donor["downstream"][0]["description"].startswith("PARTIAL")
    assert all(n["interaction_type"] == "CROSS_FEEDING" for n in (bifido, recipients, other))
    assert "four of six" in bifido["description"]
    assert "Gas production and transfer were inferred" in recipients["description"]
    ovatus = next(
        t for t in recipients["participating_taxa"] if t["preferred_term"] == "Bacteroides ovatus"
    )
    assert ovatus["term"]["id"] == "NCBITaxon:28116"


def test_banana_retains_reciprocal_inhibition_not_design_or_disease_as_competition():
    pots, inhibition, staggered = nodes("Banana_Fusarium_Biocontrol_SynCom12")
    assert "interaction_type" not in pots
    assert "interaction_type" not in staggered
    assert inhibition["interaction_type"] == "COMPETITION"
    assert inhibition["evidence"][1]["supports"] == "PARTIAL"
    assert "transient" in staggered["description"]
    assert not any(n.get("downstream") for n in (pots, inhibition, staggered))


def test_bioasteroid_images_and_elemental_yields_do_not_prove_mediation():
    leach, film, antagonism = nodes("BioAsteroid_ISS_Chondrite_Biomining_Consortium")
    assert all("interaction_type" not in n for n in (leach, film, antagonism))
    assert not any(n.get("downstream") for n in (leach, film, antagonism))
    assert "nonsignificant" in antagonism["description"]
    assert antagonism["evidence"][0]["supports"] == "PARTIAL"
    assert all(m["term"]["id"] != "CHEBI:29036" for m in leach["metabolites"])
    assert leach["metabolites"][0]["term"]["label"] == "palladium atom"


def test_sewage_observations_do_not_assert_viral_activity_or_complete_haplotypes():
    graph = nodes("Bay_Area_Sewage_SARS_CoV2_Surveillance_Community")
    assert len(graph) == 3
    assert not any(n.get("downstream") or n.get("biological_processes") for n in graph)
    assert all(e["evidence_source"] == "COMPUTATIONAL" for n in graph for e in n["evidence"])
    assert graph[-1]["evidence"][0]["supports"] == "PARTIAL"
    assert "not all resolved strain haplotypes" in graph[0]["description"]


def test_bayan_partial_remediation_is_not_a_completed_review():
    graph = nodes("Bayan_Obo_REE_Tailings_Consortium")
    assert len(graph) == 1
    assert "participating_taxa" not in graph[0]
    assert not graph[0].get("metabolites")
    assert not graph[0].get("downstream")
    assert "interaction_type" not in graph[0]
    assert graph[0]["evidence"][0]["reference"] == "doi:10.1016/j.cej.2024.153492"
    ledger = yaml.safe_load(
        (
            ROOT / "reports/causal_graph_review/decisions/20261005-twelve-records-batch7.yaml"
        ).read_text()
    )
    rows = ledger["records"]
    incomplete = [r for r in rows if r["status"] != "reviewed"]
    assert [(r["id"], r["status"]) for r in incomplete] == [
        ("CommunityMech:000005", "needs_research")
    ]
    unchanged = [r for r in rows if r["outcome"] == "unchanged"]
    assert [r["id"] for r in unchanged] == ["CommunityMech:000428"]
    assert unchanged[0]["history_file"] is None
    assert unchanged[0]["original_sha256"] == unchanged[0]["record_sha256"]
    assert sum(len(r["removed_node_decisions"]) for r in rows) == 10
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 17
