"""Keep treatment identity and inferential limits in four reviewed causal graphs."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261008-four-records-batch118.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / row["path"]).read_text()) for row in rows]


def test_viili_retains_validated_nitrogen_and_tested_eps_maximum():
    _, _, docs = records()
    nitrogen, _, outcome = docs[0]["ecological_interactions"]
    assert nitrogen["interaction_type"] == "CROSS_FEEDING"
    assert "depletion/supplementation" in nitrogen["description"]
    assert "independent of growth" in nitrogen["description"]
    assert {m["term"]["id"] for m in nitrogen["metabolites"]} == {
        "CHEBI:27266",
        "CHEBI:33709",
    }
    assert "among all tested microbial combinations" in outcome["evidence"][0]["snippet"]
    assert len(outcome["participating_taxa"]) == 3


def test_viili_ai2_regulation_is_not_fungal_nutrient_transfer():
    _, _, docs = records()
    signal = docs[0]["ecological_interactions"][1]
    assert "interaction_type" not in signal
    assert "not evidence that G. candidum supplies AI-2" in signal["description"]
    assert signal["evidence"][1]["supports"] == "SUPPORT"
    assert "activation and inhibition" in signal["evidence"][1]["snippet"]
    assert signal["evidence"][2]["supports"] == "PARTIAL"


def test_viili_signaling_bridge_is_partial_but_eps_regulation_is_supported():
    _, _, docs = records()
    nitrogen, signal, outcome = docs[0]["ecological_interactions"]
    assert nitrogen["downstream"][0]["target"] == signal["name"]
    assert nitrogen["downstream"][0]["description"].startswith("PARTIAL:")
    assert "growth effects" in nitrogen["downstream"][0]["description"]
    assert signal["downstream"][0]["target"] == outcome["name"]
    assert "positive regulation" in signal["downstream"][0]["description"]
    assert "sole explanation" in signal["downstream"][0]["description"]


def test_sludge_fraction_participants_are_not_all_five_genera():
    _, _, docs = records()
    division, biofilm, suspension, _ = docs[1]["ecological_interactions"]
    assert division["interaction_type"] == "NICHE_PARTITIONING"
    assert "not an exhaustive membership" in division["description"]
    assert [t["preferred_term"] for t in biofilm["participating_taxa"]] == [
        "Syntrophomonas",
        "Geobacter",
        "Hydrogenophaga",
    ]
    assert [t["preferred_term"] for t in suspension["participating_taxa"]] == [
        "Sedimentibacter",
        "Petrimonas",
    ]
    assert "interaction_type" not in biofilm and "interaction_type" not in suspension


def test_sludge_eet_model_is_not_a_route_resolved_intervention():
    _, _, docs = records()
    model = docs[1]["ecological_interactions"][3]
    assert "interaction_type" not in model
    assert model["description"].startswith("PARTIAL:")
    assert "interruption/rescue" in model["description"]
    assert model["evidence"][0]["evidence_source"] == "COMPUTATIONAL"
    assert model["evidence"][0]["supports"] == "PARTIAL"
    assert "Partial least squares path modeling" in model["evidence"][0]["snippet"]
    assert len(model["downstream"]) == 2
    assert all(e["description"].startswith("PARTIAL:") for e in model["downstream"])


def test_watermelon_seven_positive_partners_are_not_seven_mutualisms():
    _, _, docs = records()
    facilitation = docs[2]["ecological_interactions"][0]
    assert facilitation["interaction_type"] == "CROSS_FEEDING"
    assert "only three" in facilitation["description"]
    assert "seven strains enhanced" in facilitation["evidence"][0]["snippet"]
    assert "three strains engaged in mutualistic interactions" in (
        facilitation["evidence"][1]["snippet"]
    )


def test_watermelon_candidates_do_not_establish_specific_metabolite_transfer():
    _, _, docs = records()
    facilitation = docs[2]["ecological_interactions"][0]
    assert "metabolites" not in facilitation and "biological_processes" not in facilitation
    assert "not compound-specific rescue" in facilitation["description"]
    assert "resolved stereochemistry" in facilitation["description"]
    assert facilitation["evidence"][2]["supports"] == "PARTIAL"


def test_ssc8_growth_does_not_inherit_parent_pathogen_challenge():
    _, _, docs = records()
    outcome = docs[2]["ecological_interactions"][1]
    assert outcome["name"] == "SSC8 watermelon growth promotion without added pathogen"
    assert "interaction_type" not in outcome and "biological_processes" not in outcome
    assert "must not be assigned to SSC8" in outcome["description"]
    assert "no added pathogen" in outcome["description"]
    assert "none of the treatments" in outcome["evidence"][0]["snippet"]
    assert "comparable to the initial SynCom" in outcome["evidence"][1]["snippet"]


def test_ssc8_has_no_parent_biofilm_node_or_cross_experiment_arrows():
    _, rows, docs = records()
    nodes = docs[2]["ecological_interactions"]
    assert len(nodes) == 2 and not any(n.get("downstream") for n in nodes)
    assert len(rows[2]["removed_node_decisions"]) == 1
    assert len(rows[2]["removed_edge_decisions"]) == 2
    assert "Pseudomonas Biofilm Pathway Enrichment" not in [n["name"] for n in nodes]


def test_wetland_treatment_responses_are_not_causes_of_fitted_subnetwork():
    _, rows, docs = records()
    sulfate, oxygen, _ = docs[3]["ecological_interactions"]
    assert not sulfate.get("downstream") and not oxygen.get("downstream")
    assert len(rows[3]["removed_edge_decisions"]) == 2
    assert sulfate["interaction_type"] == "COMPETITION"
    assert sulfate["evidence"][0]["supports"] == "SUPPORT"
    assert sulfate["evidence"][1]["evidence_source"] == "COMPUTATIONAL"
    assert sulfate["evidence"][1]["supports"] == "PARTIAL"
    assert "direct acetate competition" in sulfate["description"]
    assert "interaction_type" not in oxygen
    assert "residual methane" in oxygen["description"]


def test_wetland_model_is_not_directly_measured_cross_feeding():
    _, _, docs = records()
    model = docs[3]["ecological_interactions"][2]
    assert "interaction_type" not in model
    assert "nine-reaction" in model["description"]
    assert "not directly measured interspecies transfer" in model["description"]
    assert "not evidence of universally enhanced sulfate reduction" in model["description"]
    assert all(e["supports"] == "PARTIAL" for e in model["evidence"])
    assert [t["preferred_term"] for t in model["participating_taxa"]] == [
        "wetland soil bacterial guilds"
    ]


def test_review_accounts_for_every_node_arrow_and_unchanged_cache():
    ledger, rows, docs = records()
    counts = ledger["reviewed_counts"]
    assert counts["original_nodes"] == 13 and counts["retained_nodes"] == 12
    assert counts["removed_nodes"] == 1 and counts["renamed_nodes"] == 4
    assert counts["original_arrows"] == 8 and counts["retained_arrows"] == 4
    assert counts["removed_arrows"] == 4
    assert counts["graph_quotations"] == 25 and counts["discussion_quotations"] == 4
    assert ledger["cache_changes"] == [] and not ledger["independent_approval"]
    assert ledger["edison"]["new_nodes_or_directions"] == 0
    for row, doc in zip(rows, docs, strict=True):
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == (
            row["record_sha256"]
        )
        names = [n["name"] for n in doc["ecological_interactions"]]
        assert [r["node"] for r in row["node_decisions"]] == names
        assert len(row["history_files"]) == 1
        assert doc["curation_history"][-1]["llm_assisted"]
        for node in doc["ecological_interactions"]:
            assert "downstream" not in node or node["downstream"]
            assert all(e["target"] in names for e in node.get("downstream", []))
