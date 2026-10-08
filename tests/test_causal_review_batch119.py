"""Preserve measured results without mixing strains, assay roles or causal levels."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261008-four-records-batch119.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / row["path"]).read_text()) for row in rows]


def test_thor_inhibition_is_locus_dependent_not_bilateral_competition():
    _, _, docs = records()
    node = docs[0]["ecological_interactions"][0]
    assert "UW101" in node["name"] and "interaction_type" not in node
    assert "deletion of the koreenceine locus" in node["evidence"][0]["snippet"]
    assert "was not affected by coculture" in node["evidence"][1]["snippet"]
    assert all(e["reference"] == "PMID:35435700" for e in node["evidence"])


def test_thor_expression_retains_the_correct_denominator_and_indirect_limit():
    _, _, docs = records()
    first, expression, _ = docs[0]["ecological_interactions"]
    assert "interaction_type" not in expression
    assert "greater-than-twofold pairwise response" in expression["description"]
    assert "not of each whole genome" in expression["description"]
    assert expression["evidence"][1]["supports"] == "PARTIAL"
    assert "indirect effects" in expression["evidence"][1]["snippet"]
    assert first["downstream"][0]["target"] == expression["name"]
    assert "PARTIAL" in first["downstream"][0]["description"]


def test_thor_protection_has_three_participants_and_variant_bounded_chemistry():
    _, _, docs = records()
    first, _, protection = docs[0]["ecological_interactions"]
    assert protection["scope"] == "COMMUNITY_LEVEL"
    assert "interaction_type" not in protection
    assert "source_taxon" not in protection and "target_taxon" not in protection
    assert len(protection["participating_taxa"]) == 3
    assert "not facilitation of P. koreensis colonization" in protection["description"]
    assert protection["evidence"][0]["reference"] == "PMID:35435700"
    assert protection["evidence"][1]["reference"] == "PMID:30837345"
    assert protection["evidence"][1]["supports"] == "PARTIAL"
    assert protection["downstream"][0]["target"] == first["name"]
    assert "CI04, not UW101" in protection["downstream"][0]["description"]


def test_thor_ci04_biofilm_is_context_not_a_uw101_node():
    _, rows, docs = records()
    doc = docs[0]
    assert len(doc["ecological_interactions"]) == 3
    assert len(rows[0]["removed_node_decisions"]) == 1
    assert "Emergent Three-Member Biofilm Formation" not in [
        n["name"] for n in doc["ecological_interactions"]
    ]
    discussion = doc["discussions"][-1]
    assert "CI04" in discussion["prompt"] and "UW101" in discussion["prompt"]
    assert "increased the maximum biofilm" in discussion["evidence"][1]["snippet"]


def test_tyq1_seven_positive_biofilms_do_not_erase_the_sx_attraction_exception():
    _, _, docs = records()
    node = docs[1]["ecological_interactions"][1]
    assert "interaction_type" not in node
    assert "all strains" in node["evidence"][0]["snippet"]
    assert "exception of SX" in node["evidence"][1]["snippet"]
    assert all(e["evidence_source"] == "IN_VITRO" for e in node["evidence"])


def test_tyq1_cross_feeding_keeps_medium_direction_and_as_limits():
    _, _, docs = records()
    node = docs[1]["ecological_interactions"][2]
    assert node["interaction_type"] == "CROSS_FEEDING"
    assert "all seven enriched strains" in node["evidence"][0]["snippet"]
    assert "Except for AS" in node["evidence"][1]["snippet"]
    assert "did not influence TYQ1growth" in node["evidence"][2]["snippet"]
    assert node["evidence"][3]["evidence_source"] == "COMPUTATIONAL"
    assert "not measured metabolite fluxes" in node["description"]
    assert "in-silico" in node["description"]


def test_tyq1_biological_omission_is_positive_but_not_specific_mediation():
    _, _, docs = records()
    nodes = docs[1]["ecological_interactions"]
    assert "interaction_type" not in nodes[3]
    assert "lost its inhibitory function" in nodes[3]["evidence"][1]["snippet"]
    assert nodes[3]["evidence"][1]["evidence_source"] == "IN_VIVO"
    assert nodes[3]["evidence"][2]["supports"] == "PARTIAL"
    edges = [e for n in nodes for e in n.get("downstream", [])]
    assert len(edges) == 4 and all(e["description"].startswith("PARTIAL:") for e in edges)
    assert "transient" in nodes[1]["downstream"][0]["description"]


def test_teosinte_preparation_is_not_an_ecological_node():
    _, rows, docs = records()
    doc = docs[2]
    assert len(doc["ecological_interactions"]) == 4
    assert len(rows[2]["removed_node_decisions"]) == 2
    assert all("Formulation" not in n["name"] for n in doc["ecological_interactions"])
    assert doc["engineering_design"] and doc["growth_media"]


def test_teosinte_field_effects_remain_without_claiming_nitrogen_flux():
    _, _, docs = records()
    treatment, outcome, _, _ = docs[2]["ecological_interactions"]
    assert "interaction_type" not in treatment and "interaction_type" not in outcome
    assert "biological_processes" not in treatment
    assert all(e["evidence_source"] == "IN_VIVO" for e in treatment["evidence"])
    assert len(treatment["downstream"]) == 2
    assert "treatment-level effect" in treatment["downstream"][0]["description"]
    assert {p["term"]["id"] for p in outcome["biological_processes"]} == {"GO:0040007"}
    assert "not measurements of nitrogen-fixation flux" in outcome["description"]


def test_teosinte_soil_association_network_is_not_mutualism_or_necessity():
    _, _, docs = records()
    _, _, composition, network = docs[2]["ecological_interactions"]
    assert "interaction_type" not in composition and "interaction_type" not in network
    assert "Relative abundance does not prove absolute" in composition["description"]
    assert "biological_processes" not in network and not network.get("downstream")
    assert all(e["evidence_source"] == "COMPUTATIONAL" for e in network["evidence"])
    assert network["evidence"][0]["supports"] == "PARTIAL"
    assert "correlated changes in abundance" in network["evidence"][-1]["snippet"]


def test_mcafes_selection_keeps_both_experimental_directions():
    _, _, docs = records()
    nodes = docs[3]["ecological_interactions"]
    assert all("interaction_type" not in n for n in nodes)
    assert "not one fixed consortium" in nodes[0]["description"]
    assert [e["target"] for e in nodes[0]["downstream"]] == [nodes[1]["name"], nodes[2]["name"]]
    assert len(nodes[1]["participating_taxa"]) == 3


def test_mcafes_abundance_classes_are_not_direct_growth_rates_or_hub_membership():
    _, _, docs = records()
    node = docs[3]["ecological_interactions"][2]
    assert "participating_taxa" not in node
    assert "not measured isolate growth rates" in node["description"]
    assert "generations 6 and 9" in node["description"]
    assert "not substituted" in node["description"]


def test_mcafes_hubs_are_computational_not_necessary_ecological_functions():
    _, _, docs = records()
    for node in docs[3]["ecological_interactions"][3:5]:
        assert "interaction_type" not in node and "biological_processes" not in node
        assert all(e["evidence_source"] == "COMPUTATIONAL" for e in node["evidence"])
    hub = docs[3]["ecological_interactions"][3]
    assert "90% quantile" in hub["evidence"][-1]["snippet"]
    assert "not establish" in hub["description"]


def test_mcafes_revival_is_positive_for_five_selected_stocks_only():
    _, _, docs = records()
    node = docs[3]["ecological_interactions"][5]
    assert "participating_taxa" not in node
    assert "Five selected" in node["description"]
    assert "does not establish universal revival" in node["description"]
    assert "less stable" in node["description"]
    assert node["evidence"][0]["evidence_source"] == "IN_VITRO"
    assert node["evidence"][1]["evidence_source"] == "COMPUTATIONAL"


def test_review_accounts_for_all_nodes_arrows_and_append_only_cache():
    ledger, rows, docs = records()
    counts = ledger["reviewed_counts"]
    assert (counts["original_nodes"], counts["retained_nodes"], counts["removed_nodes"]) == (
        20,
        17,
        3,
    )
    assert counts["renamed_nodes"] == 9
    assert counts["original_arrows"] == counts["retained_arrows"] == 10
    assert counts["removed_arrows"] == 0
    assert (counts["graph_quotations"], counts["discussion_quotations"]) == (38, 5)
    assert len(ledger["cache_changes"]) == 1 and not ledger["independent_approval"]
    assert ledger["cache_changes"][0]["path"] == "references_cache/PMID_35435700.md"
    assert len(ledger["cache_changes"][0]["quotations"]) == 4
    assert ledger["edison"]["new_nodes_or_directions"] == 0
    for row, doc in zip(rows, docs, strict=True):
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        names = [n["name"] for n in doc["ecological_interactions"]]
        assert [r["node"] for r in row["node_decisions"]] == names
        assert len(row["history_files"]) == 1 and doc["curation_history"][-1]["llm_assisted"]
        for node in doc["ecological_interactions"]:
            assert "downstream" not in node or node["downstream"]
            assert all(e["target"] in names for e in node.get("downstream", []))
