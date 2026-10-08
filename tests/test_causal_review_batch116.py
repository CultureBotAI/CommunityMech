"""Keep resource delivery distinct from recipient outcomes and causal mediation."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261008-three-records-batch116.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in rows]


def test_isobutanol_product_is_a_recipient_outcome():
    _, _, docs = records()
    a, b, c = docs[0]["ecological_interactions"]
    assert a["interaction_type"] == "CROSS_FEEDING" and a["scope"] == "PAIRWISE"
    assert b["scope"] == c["scope"] == "COMMUNITY_LEVEL"
    assert [t["term"]["id"] for t in b["participating_taxa"]] == ["NCBITaxon:562"]
    assert len(c["participating_taxa"]) == 2
    assert "interaction_type" not in b and "interaction_type" not in c
    assert "not assumed to describe the same assay" in b["description"]


def test_experimental_model_validation_survives_conditional_stability():
    _, _, docs = records()
    a, _, c = docs[0]["ecological_interactions"]
    assert "mathematical model that was experimentally validated" in c["description"]
    assert "not stable coexistence under every starting ratio" in c["description"]
    assert "Full-paper access was unavailable" in c["description"]
    assert all(e["supports"] == "PARTIAL" for e in c["evidence"])
    edge = a["downstream"][1]
    assert edge["target"] == c["name"] and edge["description"].startswith("PARTIAL:")
    assert "hydrolysis alone is not sufficient" in edge["description"]


def test_lactate_link_keeps_fungal_and_lab_redox_contributions():
    _, _, docs = records()
    a, b, _ = docs[1]["ecological_interactions"]
    assert a["interaction_type"] == b["interaction_type"] == "CROSS_FEEDING"
    assert "Fungal oxygen consumption first lowers dissolved oxygen" in b["description"]
    assert "LAB inoculation lowers redox potential further" in b["description"]
    assert "LAB alone cannot maintain anoxia" in b["description"]
    assert "CHEBI:18222" not in [m["term"]["id"] for m in a["metabolites"]]
    assert "not cellulose hydrolysis" in a["description"]


def test_butyrate_requires_co_substrate_and_preserves_rescue_evidence():
    _, _, docs = records()
    _, b, c = docs[1]["ecological_interactions"]
    assert c["scope"] == "COMMUNITY_LEVEL" and "interaction_type" not in c
    assert [t["term"]["id"] for t in c["participating_taxa"]] == ["NCBITaxon:1519"]
    assert "Lactate alone is insufficient" in c["description"]
    assert "acetate addition restores it" in c["description"]
    assert "glucose can also serve as co-substrate" in c["description"]
    assert b["downstream"][0]["target"] == c["name"]
    assert "Acetate or glucose must also be available" in b["downstream"][0]["description"]
    assert c["evidence"][1]["supports"] == "SUPPORT"
    assert "main text" in c["evidence"][1]["explanation"]


def test_lactate_arms_and_pretreated_benchmark_are_not_conflated():
    _, _, docs = records()
    c = docs[1]["ecological_interactions"][2]
    assert "L. brevis are separate experimental arms" in c["description"]
    assert "three-member consortium" in c["description"]
    assert "after steam pretreatment" in c["description"]
    assert "four-member arm is not that benchmark" in c["description"]


def test_filamentous_initial_glucose_and_conditional_commensalism_survive():
    _, _, docs = records()
    a, b, _ = docs[2]["ecological_interactions"]
    assert "Both partners can first grow on glucose" in a["description"]
    assert "not a claim that its genome lacks cellulase genes" in a["description"]
    assert b["scope"] == "COMMUNITY_LEVEL" and "interaction_type" not in b
    assert [t["term"]["id"] for t in b["participating_taxa"]] == ["NCBITaxon:100226"]
    assert "commensalism following early nutrient competition" in b["description"]
    assert a["downstream"][0]["target"] == b["name"]


def test_dependence_does_not_mediate_all_treatment_responses():
    _, _, docs = records()
    _, b, c = docs[2]["ecological_interactions"]
    assert "downstream" not in b
    assert c["interaction_type"] == "COMPETITION"
    assert len(c["participating_taxa"]) == 2
    assert "causal mediation by hydrolysate dependence is unresolved" in c["description"]


def test_viability_relative_advantage_and_fluorescence_limits_are_explicit():
    _, _, docs = records()
    c = docs[2]["ecological_interactions"][2]
    assert "do not attribute that reversal to the tag" in c["description"]
    assert "not absolute bacterial growth stimulation" in c["description"]
    assert "not exact cell counts in every condition" in c["description"]


def test_cache_append_is_bounded_and_version_located():
    ledger, _, docs = records()
    change = ledger["cache_changes"][0]
    assert len(ledger["cache_changes"]) == 1 and change["quote_words"] == 19
    text = (ROOT / change["path"]).read_text()
    assert "main text p. 6 (not supplementary material)" in text
    assert "not a full-text import or a license assertion" in text
    snippet = docs[1]["ecological_interactions"][2]["evidence"][1]["snippet"]
    assert len(snippet.split()) == 19 and snippet in text
    assert (
        hashlib.sha256((ROOT / change["path"]).read_bytes()).hexdigest() == change["after_sha256"]
    )


def test_every_node_and_arrow_has_an_explicit_disposition():
    ledger, rows, _ = records()
    c = ledger["reviewed_counts"]
    assert (c["original_nodes"], c["retained_nodes"], c["removed_nodes"]) == (9, 9, 0)
    assert (c["original_arrows"], c["retained_arrows"], c["removed_arrows"]) == (6, 5, 1)
    assert c["renamed_nodes"] == 4
    assert c["graph_quotations"] == 16 and c["discussion_quotations"] == 3
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 1
    assert ledger["issues"] == [1901, 1902, 1903]
    assert ledger["unresolved_non_graph_issues"] == [1904, 1905]
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0


def test_canonical_participants_hashes_histories_and_anchors_are_guarded():
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
        for n in doc["ecological_interactions"]:
            assert all(t in canonical for t in n.get("participating_taxa", []))
            assert all(e["target"] in names for e in n.get("downstream", []))
        for d in doc["discussions"]:
            assert all(a.split("#", 1)[1] in names for a in d["attaches_to"])
    assert docs[0]["taxonomy"][0]["taxon_term"]["term"]["id"] == "NCBITaxon:51453"
    assert docs[2]["taxonomy"][0]["taxon_term"]["term"]["id"] == "NCBITaxon:1344414"
