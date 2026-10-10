"""Preserve assay, hypothesis and identity limits from the eighth graph review."""

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def record(stem):
    return yaml.safe_load((ROOT / "kb/communities" / f"{stem}.yaml").read_text())


def nodes(stem):
    return record(stem)["ecological_interactions"]


def test_biorock_percent_of_control_and_single_strain_scope():
    ree, vanadium, panel = nodes("BioRock_ISS_Basalt_Biomining_Consortium")
    assert "184.92-283.22% OF" in vanadium["description"]
    assert "84.92-183.22%" in vanadium["description"]
    assert "p=0.124" in ree["description"]
    assert "p=0.055" in panel["description"]
    assert "single-strain" in ree["description"]
    assert not ree.get("metabolites")
    for node in (ree, vanadium, panel):
        assert "interaction_type" not in node
        assert not node.get("biological_processes")
        assert not node.get("downstream")


def test_sponge_keeps_conditional_mechanisms_not_summary_arrows():
    nitrify, network, host, stable, delta, balance = nodes(
        "BioModels_MODEL2407300002_Sponge_Holobiont_Network"
    )
    assert nitrify["interaction_type"] == "CROSS_FEEDING"
    assert network["interaction_type"] == delta["interaction_type"] == "CROSS_FEEDING"
    for node in (host, stable, balance):
        assert "interaction_type" not in node
    assert nitrify["downstream"][0]["target"] == stable["name"]
    assert host["downstream"][0]["target"] == network["name"]
    assert not network.get("downstream")
    assert "cell-removal rate" in stable["description"]
    assert "final AOA:NOB population ratio by its initial value" in stable["description"]
    assert "not absolute population-size bounds" in stable["description"]
    assert "Host respiration is excluded" in balance["description"]
    assert "hypotaurine" in delta["description"]
    assert all("concentration" not in m for m in nitrify["metabolites"])
    assert nitrify["biological_processes"][0]["preferred_term"] == "ammonia oxidation"


def test_bosea_keeps_handoff_not_soil_to_toxicity_mediation():
    handoff, soil, toxicity = nodes("Bosea_Pseudomonas_Dimethachlon_Degradation_Consortium")
    assert handoff["interaction_type"] == "CROSS_FEEDING"
    assert handoff["source_taxon"]["term"] == {"id": "NCBITaxon:85413", "label": "Allobosea"}
    assert handoff["downstream"][0]["target"] == soil["name"]
    assert handoff["downstream"][0]["description"].startswith("PARTIAL")
    assert not soil.get("downstream")
    assert all("interaction_type" not in node for node in (soil, toxicity))
    assert toxicity["evidence"][0]["evidence_source"] == "OTHER"
    assert "unresolved" in toxicity["evidence"][0]["explanation"]
    assert "not universal safety" in toxicity["description"]


def test_bothnian_preserves_experimental_syntrophy_and_partial_auxiliary_roles():
    core, secondary, auxiliary = nodes("Bothnian_Bay_GAC_Dependent_CIET_SAO_Consortium")
    assert core["interaction_type"] == secondary["interaction_type"] == "SYNTROPHY"
    assert auxiliary["interaction_type"] == "CROSS_FEEDING"
    assert core["evidence"][1]["evidence_source"] == "IN_VITRO"
    assert core["evidence"][1]["supports"] == "SUPPORT"
    assert "0.06%" in core["description"]
    assert "not demonstrably absent" in core["description"]
    assert all(
        e["supports"] == "PARTIAL" for node in (secondary, auxiliary) for e in node["evidence"]
    )


def test_brachypodium_keeps_source_hypothesis_not_measured_exudate_selection():
    hypothesis, taxa, genes = nodes("Brachypodium_Young_Root_Rhizosphere_EcoFAB_Community")
    assert hypothesis["name"].startswith("Hypothesized")
    assert hypothesis["evidence"][0]["supports"] == "PARTIAL"
    assert "edaphic factors" in hypothesis["evidence"][0]["snippet"]
    assert {e["target"] for e in hypothesis["downstream"]} == {taxa["name"], genes["name"]}
    assert all(e["description"].startswith("HYPOTHESIZED") for e in hypothesis["downstream"])
    assert "no uniform overall trend" in taxa["description"]
    assert "gene-abundance patterns, not expression" in genes["description"]
    for node in (hypothesis, taxa, genes):
        assert "interaction_type" not in node
        assert not node.get("metabolites")
        assert not node.get("biological_processes")


def test_buchnera_keeps_evolutionary_hypotheses_not_thermodynamic_syntrophy():
    trp, takeover, persistence = nodes("Buchnera_Serratia_Cinara_Cedri_Endosymbiont_Consortium")
    assert trp["interaction_type"] == takeover["interaction_type"] == "CROSS_FEEDING"
    assert "interaction_type" not in persistence
    assert persistence["name"].startswith("Inferred")
    assert "anthranilate, not tryptophan" in trp["metabolites"][0]["notes"]
    for node in (trp, takeover):
        assert node["downstream"][0]["target"] == persistence["name"]
        assert node["downstream"][0]["description"].startswith("HYPOTHESIZED")
    assert all(
        e["supports"] == "PARTIAL" for n in (trp, takeover, persistence) for e in n["evidence"]
    )


def test_yb2_and_rumen_activity_does_not_imply_partitioning_or_mutualism():
    complement, loss = nodes("Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium")
    assert complement["downstream"][0]["target"] == loss["name"]
    assert complement["downstream"][0]["description"].startswith("PARTIAL")
    assert complement["evidence"][0]["supports"] == "PARTIAL"
    assert "4.30% +/- 0.11%" in loss["description"]
    pair, triple = nodes("Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium")
    assert "does not define the percentage denominator" in pair["description"]
    assert pair["target_taxon"]["term"]["label"] == "Pseudoselenomonas ruminantium"
    assert triple["participating_taxa"][2]["term"]["label"] == "Hominimerdicola alba"
    assert not pair.get("downstream") and not triple.get("downstream")
    for node in (complement, loss, pair, triple):
        assert "interaction_type" not in node


def test_crc_retains_only_qualified_metabolic_mediation():
    colonize, suppress, metabolism, disease = nodes("CRC_Fusobacterium_Control_SynCom")
    assert not colonize.get("downstream")
    assert not suppress.get("downstream")
    assert all("interaction_type" not in n for n in (colonize, suppress, metabolism, disease))
    assert "mixed before gavage" in colonize["description"]
    assert "slowed" in suppress["metabolites"][0]["notes"]
    assert metabolism["downstream"][0]["target"] == disease["name"]
    assert metabolism["downstream"][0]["description"].startswith("PARTIAL")
    assert metabolism["evidence"][0]["supports"] == "PARTIAL"
    assert "nonsignificant" in disease["description"]
    assert "GO:0006568" not in str(
        [n.get("biological_processes", []) for n in (colonize, suppress, metabolism, disease)]
    )


def test_calcium_separates_compounds_exudates_and_pots():
    compounds, exudates, pots = nodes("Calcium_Tomato_Bacterial_Wilt_SynCom")
    assert compounds["downstream"][0]["target"] == exudates["name"]
    assert compounds["downstream"][0]["description"].startswith("HYPOTHESIZED")
    assert not exudates.get("downstream")
    assert "Gene copies are not viable-cell counts" in exudates["description"]
    assert "74.07% to 0%" in pots["description"]
    assert "not demonstrated pathogen eradication" in pots["description"]
    assert not pots.get("biological_processes")
    assert all("interaction_type" not in n for n in (compounds, exudates, pots))


def test_cable_historical_partial_review_and_mechanism_bounds_are_preserved():
    graph = nodes("Cable_Bacteria_Photosynthetic_Biofilm_Sediment")
    oxygen, conduction, response = graph
    assert oxygen["interaction_type"] == "CROSS_FEEDING"
    assert all("interaction_type" not in n for n in (conduction, response))
    assert oxygen["downstream"][0]["target"] == conduction["name"]
    assert conduction["downstream"][0]["target"] == response["name"]
    assert "NCBITaxon:3041" not in str(graph)
    assert "reciprocal benefit to the phototrophs is not established" in oxygen["description"]
    assert not any(n.get("participating_taxa") for n in graph)
    ledger = yaml.safe_load(
        (
            ROOT / "reports/causal_graph_review/decisions/20261005-twelve-records-batch8.yaml"
        ).read_text()
    )
    rows = ledger["records"]
    assert [(r["id"], r["status"]) for r in rows if r["status"] != "reviewed"] == [
        ("CommunityMech:000145", "needs_research")
    ]
    unchanged = [r for r in rows if r["outcome"] == "unchanged"]
    assert [r["id"] for r in unchanged] == ["CommunityMech:000447"]
    assert unchanged[0]["history_file"] is None
    assert unchanged[0]["original_sha256"] == unchanged[0]["record_sha256"]
    assert sum(len(r["removed_node_decisions"]) for r in rows) == 2
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 6
