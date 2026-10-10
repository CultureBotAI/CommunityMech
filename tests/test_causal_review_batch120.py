"""Keep positive outcomes distinct from unmeasured ecological mechanisms."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261008-four-records-batch120.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / row["path"]).read_text()) for row in rows]


def test_arsenic_preserves_direct_carbon_cross_feeding():
    _, _, docs = records()
    node = docs[0]["ecological_interactions"][0]
    assert node["interaction_type"] == "CROSS_FEEDING"
    assert node["scope"] == "PAIRWISE"
    assert node["source_taxon"]["preferred_term"] == "Thermoleptolyngbya sichuanensis XZ-Cy5"
    assert node["target_taxon"]["preferred_term"] == "Chelatococcus sp. XZ-Ab1"
    assert "direct evidence of photoautotroph-derived carbon" in node["evidence"][1]["snippet"]
    assert "an identified secreted molecule" in node["description"]


def test_arsenic_mutualism_keeps_actual_reciprocal_growth_evidence():
    _, _, docs = records()
    node = docs[0]["ecological_interactions"][1]
    assert node["interaction_type"] == "MUTUALISM"
    assert node["source_taxon"]["preferred_term"] == "Chelatococcus sp. XZ-Ab1"
    assert "promoted growth" in node["evidence"][0]["snippet"]
    assert node["evidence"][0]["supports"] == "SUPPORT"
    assert "reciprocal heterotrophic benefit" in node["description"]


def test_arsenic_genomic_routes_are_not_traced_oxygen_or_nitrogen():
    _, _, docs = records()
    doc = docs[0]
    node = doc["ecological_interactions"][1]
    assert node["evidence"][-1]["supports"] == "PARTIAL"
    assert "not a demonstrated oxygen-source requirement" in node["evidence"][-1]["explanation"]
    assert "No nitrogen transfer" in node["description"]
    assert "not direct tracing" in node["description"]
    assert len(doc["discussions"]) == 2
    assert not any(n.get("downstream") for n in doc["ecological_interactions"])


def test_biomethanation_external_gas_is_not_interspecies_cross_feeding():
    _, _, docs = records()
    node = docs[1]["ecological_interactions"][0]
    assert "interaction_type" not in node
    assert "pressurised gas cylinders" in node["evidence"][0]["snippet"]
    assert "reaching 86% by day 69" in node["evidence"][1]["snippet"]
    assert "exceeding 90% was proposed, not observed" in node["description"]
    assert {m["term"]["id"] for m in node["metabolites"]} == {
        "CHEBI:18276",
        "CHEBI:16526",
        "CHEBI:16183",
    }


def test_biomethanation_group_counts_are_not_taxon_specific_activity():
    _, _, docs = records()
    node = docs[1]["ecological_interactions"][0]
    assert node["evidence"][2]["supports"] == "PARTIAL"
    assert "not taxon-resolved flux measurements" in node["description"]
    assert "overlapping taxonomic summaries" in node["description"]
    assert "single proof-of-concept CSTR" in node["description"]
    assert len(node["participating_taxa"]) == 3


def test_biomethanation_vfa_pools_do_not_prove_thermodynamic_syntrophy():
    _, _, docs = records()
    node = docs[1]["ecological_interactions"][1]
    assert "interaction_type" not in node
    assert "73% acetate" in node["evidence"][0]["snippet"]
    assert all(e["supports"] == "PARTIAL" for e in node["evidence"][1:4])
    assert "phase-1" in node["evidence"][4]["explanation"]
    assert "does not establish phase-4 sampling timing" in node["evidence"][4]["explanation"]
    assert "Washout and substrate-pool changes remain alternatives" in node["description"]
    assert "product-removal-dependent thermodynamic cooperation" in node["description"]
    assert not node.get("downstream")


def test_compost_maturation_is_not_demonstrated_member_mutualism():
    _, _, docs = records()
    node = docs[2]["ecological_interactions"][0]
    assert "interaction_type" not in node
    assert "enhanced humification" in node["evidence"][0]["snippet"]
    assert node["evidence"][1]["evidence_source"] == "COMPUTATIONAL"
    assert node["evidence"][1]["supports"] == "PARTIAL"
    assert "Mantel correlation" in node["description"]


def test_compost_preserves_rebound_and_later_reported_attenuation():
    _, _, docs = records()
    node = docs[2]["ecological_interactions"][1]
    assert "interaction_type" not in node and "biological_processes" not in node
    assert (
        "transient ARG rebound followed by profound attenuation" in node["evidence"][1]["snippet"]
    )
    assert node["evidence"][1]["evidence_source"] == "COMPUTATIONAL"
    assert "eliminating high-risk pathogens" in node["evidence"][0]["snippet"]
    assert "every viable pathogen" in node["description"]
    assert "not" in node["description"] or "without" in node["description"]


def test_compost_hgt_is_potential_not_measured_transfer_frequency():
    _, _, docs = records()
    node = docs[2]["ecological_interactions"][2]
    assert "interaction_type" not in node
    assert all(e["evidence_source"] == "COMPUTATIONAL" for e in node["evidence"])
    assert "potential host-gene associations by 26.6%" in node["evidence"][1]["snippet"]
    assert node["evidence"][2]["supports"] == "PARTIAL"
    assert "not measurements of conjugation frequency" in node["description"]
    assert "not a directly measured transfer rate" in node["biological_processes"][0]["notes"]


def test_compost_retains_partial_environmental_mediation_not_common_cause_arrow():
    _, rows, docs = records()
    maturation, attenuation, _ = docs[2]["ecological_interactions"]
    assert len(maturation["downstream"]) == 1
    assert maturation["downstream"][0]["target"] == attenuation["name"]
    assert maturation["downstream"][0]["description"].startswith("PARTIAL:")
    assert len(rows[2]["removed_edge_decisions"]) == 1
    assert "Shared SynCom inoculation" in rows[2]["removed_edge_decisions"][0]["rationale"]


def test_tobacco_prebiotic_results_are_isolate_specific_with_y878_null():
    _, _, docs = records()
    node = docs[3]["ecological_interactions"][0]
    assert "interaction_type" not in node
    assert "Vitamin C increased Y364" in node["description"]
    assert "increased Y832" in node["description"]
    assert "for Y878, none" in node["evidence"][1]["snippet"]
    assert "tomato root exudates" in node["description"]


def test_tobacco_chea_marker_and_compatibility_are_not_colonization_measurements():
    _, _, docs = records()
    node = docs[3]["ecological_interactions"][1]
    assert "interaction_type" not in node and "biological_processes" not in node
    assert "metabolites" not in node
    assert "showed mutual compatibility" in node["evidence"][0]["snippet"]
    assert (
        "lacked cheA gene, still displayed strong antagonistic activity"
        in node["evidence"][1]["snippet"]
    )
    assert "not directly measured root migration or colonization" in node["description"]


def test_tobacco_positive_field_result_is_a_combined_treatment():
    _, _, docs = records()
    node = docs[3]["ecological_interactions"][2]
    assert "interaction_type" not in node and "biological_processes" not in node
    assert "nearly doubled crop yield" in node["evidence"][1]["snippet"]
    assert all(e["evidence_source"] == "IN_VIVO" for e in node["evidence"])
    assert "positive combined-treatment result" in node["description"]
    assert "qPCR abundance is not a direct viable-cell count" in node["description"]


def test_tobacco_existing_arrows_do_not_prove_the_unique_mediator():
    _, _, docs = records()
    a, b, c = docs[3]["ecological_interactions"]
    assert a["downstream"][0]["target"] == b["name"]
    assert b["downstream"][0]["target"] == c["name"]
    assert "PARTIAL for growth as the mediator" in a["downstream"][0]["description"]
    assert b["downstream"][0]["description"].startswith("PARTIAL:")
    assert "cow-manure fertilization" in b["downstream"][0]["description"]
    assert (
        "future studies should include non-chemotactic"
        in docs[3]["discussions"][-1]["evidence"][0]["snippet"]
    )


def test_review_accounts_for_all_nodes_arrows_and_preserves_caches():
    ledger, rows, docs = records()
    counts = ledger["reviewed_counts"]
    assert counts["original_nodes"] == counts["retained_nodes"] == 10
    assert counts["removed_nodes"] == 0 and counts["renamed_nodes"] == 6
    assert (counts["original_arrows"], counts["retained_arrows"], counts["removed_arrows"]) == (
        4,
        3,
        1,
    )
    assert (counts["graph_quotations"], counts["discussion_quotations"]) == (27, 6)
    assert ledger["cache_changes"] == [] and not ledger["independent_approval"]
    assert ledger["edison"]["new_nodes_or_directions"] == 0
    for row, doc in zip(rows, docs, strict=True):
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        names = [n["name"] for n in doc["ecological_interactions"]]
        assert [r["node"] for r in row["node_decisions"]] == names
        assert len(row["history_files"]) == 1 and doc["curation_history"][-1]["llm_assisted"]
        for node in doc["ecological_interactions"]:
            assert "downstream" not in node or node["downstream"]
            assert all(e["target"] in names for e in node.get("downstream", []))
