"""Preserve source and assay distinctions from the sixth graph review."""

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def nodes(stem):
    return yaml.safe_load((ROOT / "kb/communities" / f"{stem}.yaml").read_text())[
        "ecological_interactions"
    ]


def test_plant_workflow_arrows_stay_removed_but_experimental_nodes_remain():
    for stem in (
        "Bacillus_Saccharomyces_Daqu_Spatial_Cooperation_SynCom",
        "Bacillus_siamensis_vallismortis_HT_Masson_Pine_SynCom",
    ):
        graph = nodes(stem)
        assert len(graph) == 3
        assert not any(n.get("downstream") for n in graph)
        assert all("interaction_type" not in n for n in graph)
        assert graph[0]["evidence"][0]["supports"] == "SUPPORT"


def test_inferred_metabolic_routes_preserve_measured_mutualism():
    formate, fructan, benefit = nodes("Bacteroides_Methanobrevibacter_Gnotobiotic_Mouse_Mutualism")
    assert formate["evidence"][0]["supports"] == "PARTIAL"
    assert fructan["evidence"][0]["supports"] == "SUPPORT"
    assert benefit["interaction_type"] == "MUTUALISM"
    for n in (formate, fructan):
        assert n["interaction_type"] == "SYNTROPHY"
        assert n["downstream"][0]["description"].startswith("PARTIAL")
    niche, response, pools = nodes("Bacteroides_Eubacterium_Gnotobiotic_Gut_Model")
    assert niche["interaction_type"] == "NICHE_PARTITIONING"
    assert response["interaction_type"] == "CROSS_FEEDING"
    assert response["evidence"][1]["supports"] == "PARTIAL"
    assert "interaction_type" not in pools
    assert "concentration" in pools["description"]


def test_hmo_constraint_is_not_cause_of_donor_hydrolysis():
    graph = nodes("Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding")
    assert len(graph) == 6
    assert not graph[0].get("downstream")
    assert sum(len(n.get("downstream", [])) for n in graph) == 4
    for n in graph:
        assert all(e["description"].startswith("PARTIAL") for e in n.get("downstream", []))
        assert all(m["term"]["id"] != "CHEBI:36219" for m in n.get("metabolites", []))
    assert graph[2]["interaction_type"] == "CROSS_FEEDING"
    assert graph[2]["evidence"][0]["supports"] == "PARTIAL"
    assert graph[2]["evidence"][1]["supports"] == "SUPPORT"
    assert all("interaction_type" not in n for i, n in enumerate(graph) if i != 2)


def test_vaginal_paired_fitness_does_not_type_every_assay_as_predation():
    contact, growth, replication, pathway, pools, host = nodes(
        "Bifidobacterium_Trichomonas_Vaginal_Coculture"
    )
    assert not contact.get("downstream")
    assert growth["interaction_type"] == "PREDATION"
    assert "does not establish ingestion" in growth["description"]
    assert "metabolites" not in growth
    assert all("interaction_type" not in n for n in (contact, replication, pathway, pools, host))
    for n in (replication, pathway, pools):
        assert n["downstream"][0]["description"].startswith("PARTIAL")
        assert n["evidence"][0]["supports"] == "SUPPORT"
    assert pools["metabolites"][0]["term"]["id"] == "CHEBI:35366"
    assert host["name"] == "Adhesin Transcripts and HeLa Nonprotection"


def test_2fl_peak_is_distinct_from_putative_acetate_exchange():
    peak, transfer = nodes("Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture")
    assert "interaction_type" not in peak
    assert len(peak["evidence"]) == 3
    assert peak["evidence"][2]["supports"] == "PARTIAL"
    assert transfer["interaction_type"] == "CROSS_FEEDING"
    assert transfer["evidence"][2]["supports"] == "PARTIAL"
    assert [m["term"]["id"] for m in transfer["metabolites"]] == ["CHEBI:30089"]


def test_industrial_niche_models_remain_explicitly_partial():
    pet = nodes("Bacillus_Pseudomonas_Galveston_PET_Consortium")[0]
    performance, partition = nodes("Baia_de_Todos_os_Santos_Mangrove_Alkane_Degrading_Consortium")
    for n in (pet, partition):
        assert n["interaction_type"] == "NICHE_PARTITIONING"
        assert n["description"].startswith("PARTIAL")
    assert "interaction_type" not in performance
    assert performance["evidence"][1]["supports"] == "PARTIAL"
    assert "one batch reactor" in performance["description"]


def test_unchanged_reviews_do_not_manufacture_history_or_edits():
    ledger = yaml.safe_load(
        (
            ROOT / "reports/causal_graph_review/decisions/20261005-eleven-records-batch6.yaml"
        ).read_text()
    )
    rows = ledger["records"]
    assert len(rows) == 11
    unchanged = [r for r in rows if r["outcome"] == "unchanged"]
    assert {r["id"] for r in unchanged} == {"CommunityMech:000464", "CommunityMech:000365"}
    assert all(r["history_file"] is None for r in unchanged)
    assert all(r["original_sha256"] == r["record_sha256"] for r in unchanged)
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 8
    assert sum(len(r["node_decisions"]) for r in rows) == 32
    sulfate, remodeling = nodes("Bacteroides_Desulfovibrio_Carrageenan_H2S_Coculture")
    assert sulfate["interaction_type"] == "CROSS_FEEDING"
    assert "metabolites" not in remodeling
    assert not any(n.get("downstream") for n in (sulfate, remodeling))
