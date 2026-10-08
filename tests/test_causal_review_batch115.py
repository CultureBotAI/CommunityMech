"""Separate mineral roles, reactor predictions and evidence-backed causal links."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261008-three-records-batch115.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in rows]


def test_pyrite_roles_and_perturbations_are_not_pairwise_exchange():
    _, _, docs = records()
    nodes = docs[0]["ecological_interactions"]
    assert len(nodes) == 6
    assert all(n["scope"] == "COMMUNITY_LEVEL" for n in nodes)
    assert all("interaction_type" not in n for n in nodes)
    assert [len(n["participating_taxa"]) for n in nodes] == [1, 1, 1, 3, 3, 3]
    assert all(e["evidence_source"] == "IN_VITRO" for n in nodes for e in n["evidence"])


def test_biogenic_dsf_survives_without_endogenous_consortium_overclaim():
    _, _, docs = records()
    node = docs[0]["ecological_interactions"][4]
    assert node["name"] == "Responses to Added DSF and BDSF"
    assert "confirmed biogenic DSF" in node["description"]
    assert "nanomolar" in node["description"] and "2 uM each" in node["description"]
    assert "does not prove the micromolar treatment phenotype" in node["description"]
    assert "fatty-acid stress" in node["description"]
    assert node["evidence"][1]["supports"] == "SUPPORT"
    assert node["evidence"][2]["supports"] == "PARTIAL"


def test_ahl_treatment_is_not_production_or_exact_l_reagents():
    _, _, docs = records()
    node = docs[0]["ecological_interactions"][5]
    assert "5 uM each" in node["description"]
    assert "DL-homoserine-lactone reagents" in node["description"]
    assert "do not demonstrate A. caldus production of AHLs" in node["description"]
    assert "not a direct motility-rate measurement" in node["description"]
    assert "metabolites" not in node
    assert node["evidence"][0]["supports"] == "PARTIAL"


def test_sulfobacillus_comparator_and_time_context_are_preserved():
    _, _, docs = records()
    node = docs[0]["ecological_interactions"][2]
    assert "not relative to L. ferriphilum biofilms" in node["description"]
    assert "precolonization could impair leaching" in node["description"]
    assert "7 and 14 days was not significantly changed" in node["description"]
    assert "40 C, not the species growth optimum" in node["description"]


def test_mineral_loop_is_not_nutrient_exchange_or_always_beneficial():
    _, _, docs = records()
    a, _, _, d, _, _ = docs[0]["ecological_interactions"]
    assert a["downstream"][0]["target"] == d["name"]
    assert d["downstream"][0]["target"] == a["name"]
    assert "redox-potential window" in a["downstream"][0]["description"]
    assert "without asserting a measured interspecies" in d["downstream"][0]["description"]
    assert "without assigning the Calvin-Benson-Bassham pathway" in a["description"]


def test_afipia_pathway_is_predicted_not_measured_cross_feeding():
    _, _, docs = records()
    a = docs[1]["ecological_interactions"][0]
    assert a["description"].startswith("PARTIAL:")
    assert "not measured flux through this exact strain" in a["description"]
    assert a["evidence"][0]["evidence_source"] == "COMPUTATIONAL"
    assert a["evidence"][0]["supports"] == "PARTIAL"
    assert len(a["participating_taxa"]) == 1
    assert a["participating_taxa"][0]["term"]["id"] == "NCBITaxon:1033"
    assert "interaction_type" not in a


def test_selection_to_potential_does_not_mediate_biofilm_loss():
    _, _, docs = records()
    a, b, c = docs[1]["ecological_interactions"]
    assert len(b["downstream"]) == 1 and b["downstream"][0]["target"] == a["name"]
    assert "not induction of the pathway" in b["downstream"][0]["description"]
    assert "R2 and R3 were held at 250 mg/L" in b["description"]
    assert "R3 stably degraded" in c["description"]
    assert "HYPOTHESIZED:" in c["description"]
    assert "nor was the outcome shown to be caused by Afipia dominance" in c["description"]
    assert c["evidence"][0]["supports"] == "PARTIAL"


def test_acidiphilium_is_ferric_reduction_not_ferrous_oxidation():
    _, _, docs = records()
    a, b, _, _ = docs[2]["ecological_interactions"]
    assert "ferric-iron reduction, producing ferrous iron" in b["description"]
    assert "does not assign ferrous-iron oxidation" in b["description"]
    assert "electron acceptor" in a["downstream"][0]["description"]
    assert (
        "not a measured transfer of autotroph-derived organic carbon"
        in a["downstream"][0]["description"]
    )
    assert "concentration" not in a["metabolites"][0]


def test_phototrophy_and_fungal_presence_do_not_prove_carbon_delivery():
    _, _, docs = records()
    doc = docs[2]
    nodes = doc["ecological_interactions"]
    assert len(nodes) == 4
    assert sum(len(n.get("downstream", [])) for n in nodes) == 1
    assert "downstream" not in nodes[2]
    assert nodes[2]["evidence"][0]["evidence_source"] == "REVIEW"
    gap = doc["discussions"][-1]
    assert "Basidiomycota presence is not rejected" in gap["rationale"]
    assert "Hortaea werneckii belongs to Ascomycota" in gap["rationale"]
    assert gap["evidence"][0]["evidence_source"] == "REVIEW"
    assert all(t["term"]["id"] != "NCBITaxon:5204" for n in nodes for t in n["participating_taxa"])


def test_dispositions_account_for_every_original_node_and_arrow():
    ledger, rows, _ = records()
    c = ledger["reviewed_counts"]
    assert (c["original_nodes"], c["retained_nodes"], c["removed_nodes"]) == (14, 13, 1)
    assert (c["original_arrows"], c["retained_arrows"], c["removed_arrows"]) == (7, 4, 3)
    assert c["renamed_nodes"] == 4
    assert c["graph_quotations"] == 21 and c["discussion_quotations"] == 4
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 3
    assert ledger["issues"] == [1893, 1894, 1895]
    assert ledger["unresolved_non_graph_issues"] == [1896, 1897, 1898]
    assert all(p["fresh_source_literal_match"] for p in ledger["snippet_checks"])
    assert sum(p["independent_primary_match"] for p in ledger["snippet_checks"]) == 20
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0


def test_hashes_histories_participant_subsets_and_anchors_are_guarded():
    ledger, rows, docs = records()
    assert not ledger["independent_approval"]
    for row, doc in zip(rows, docs, strict=True):
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert row["curation_events_added"] == len(row["history_files"]) == 1
        assert (ROOT / row["history_files"][0]).exists()
        assert doc["curation_history"][-1]["llm_assisted"] is True
        canonical = [
            {k: t["taxon_term"][k] for k in ["preferred_term", "term"]} for t in doc["taxonomy"]
        ]
        names = {n["name"] for n in doc["ecological_interactions"]}
        for node in doc["ecological_interactions"]:
            assert all(t in canonical for t in node["participating_taxa"])
            assert all(e["target"] in names for e in node.get("downstream", []))
        for gap in doc["discussions"]:
            assert all(a.split("#", 1)[1] in names for a in gap["attaches_to"])
