"""Preserve positive perturbations while bounding their proposed mediators."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261007-four-records-batch81.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in rows]


def test_ppcp_removal_is_preserved_without_assigning_exchange():
    _, rows, docs = records()
    (node,) = docs[0]["ecological_interactions"]
    assert "interaction_type" not in node and "downstream" not in node
    assert len(node["participating_taxa"]) == len(docs[0]["taxonomy"]) == 3
    assert all(s in node["description"] for s in ["97.83%", "68.19%", "85.34%", "8 h"])
    assert "mineralization" in node["description"]
    assert rows[0]["status"] == "needs_research" and 1672 in rows[0]["issues"]


def test_phb_integration_and_positive_causal_contribution_survive():
    _, _, docs = records()
    integration, photo, dark, robust = docs[1]["ecological_interactions"]
    assert all("interaction_type" not in n for n in [integration, photo, dark, robust])
    assert integration["downstream"][0]["target"] == photo["name"]
    assert "colony PCR" in integration["description"]
    assert all(s in integration["downstream"][0]["description"] for s in ["48%", "50%", "10%"])
    assert "downstream" not in dark and "downstream" not in robust


def test_phb_bulk_localization_and_reactor_yields_are_distinct():
    _, _, docs = records()
    _, photo, dark, robust = docs[1]["ecological_interactions"]
    assert "HPLC measured bulk PHB" in photo["description"]
    assert photo["evidence"][1]["supports"] == "PARTIAL"
    assert all(s in dark["description"] for s in ["38%", "23 mg/L", "55%", "250 mg/L"])
    assert all(s in robust["description"] for s in ["33%", "4 L", "22%", "8 L", "38 C"])
    assert "nonsterility alone" in robust["description"]


def test_phb_resilience_is_positive_but_oxygen_mediation_is_open():
    _, _, docs = records()
    oxygen = next(
        d
        for d in docs[1]["discussions"]
        if d["discussion_id"] == "DISCUSSION-PPHET-OXYGEN-SCAVENGING"
    )
    assert oxygen["status"] == "OPEN"
    assert oxygen["evidence"][0]["evidence_source"] == "OTHER"
    assert oxygen["evidence"][0]["supports"] == "PARTIAL"
    assert docs[1]["ecological_interactions"][-1]["evidence"][0]["supports"] == "SUPPORT"


def test_rice_positive_methane_and_exudate_perturbations_survive():
    _, rows, docs = records()
    _, exudate, _, methane = docs[2]["ecological_interactions"]
    assert "living rice host" in exudate["description"]
    assert "not an abiotic source" in exudate["description"]
    assert exudate["evidence"][0]["supports"] == methane["evidence"][0]["supports"] == "SUPPORT"
    assert all(s in methane["description"] for s in ["38%", "58%", "tub level", "focused on PSY1"])
    assert rows[2]["status"] == "needs_research" and 1673 in rows[2]["issues"]
    assert len(exudate["downstream"]) == 1


def test_rice_three_mechanistic_arrows_remain_qualified():
    _, _, docs = records()
    oxidation, exudate, production, methane = docs[2]["ecological_interactions"]
    for node in [oxidation, exudate, production]:
        assert len(node["downstream"]) == 1
        assert node["downstream"][0]["description"].startswith(("HYPOTHESIZED -", "PARTIAL -"))
    assert (
        oxidation["downstream"][0]["target"]
        == production["downstream"][0]["target"]
        == methane["name"]
    )
    assert "little direct effect" in exudate["downstream"][0]["description"]
    assert (
        production["evidence"][1]["evidence_source"]
        == methane["evidence"][1]["evidence_source"]
        == "COMPUTATIONAL"
    )
    assert (
        production["participating_taxa"][0]["preferred_term"]
        != exudate["participating_taxa"][0]["preferred_term"]
    )


def test_panax_mixed_filtrates_are_not_coculture_secretion():
    _, _, docs = records()
    disease, filtrate, _, _ = docs[3]["ecological_interactions"]
    assert "56%" in disease["description"] and "61%" in disease["description"]
    assert "separately grown" in filtrate["description"]
    assert "surface-spread" in filtrate["description"]
    assert all(s in filtrate["description"] for s in ["24%", "30%", "38%"])
    assert "interaction_type" not in disease and "interaction_type" not in filtrate


def test_panax_root_biomarkers_and_correlations_do_not_resolve_mediation():
    _, _, docs = records()
    _, _, defense, fungi = docs[3]["ecological_interactions"]
    assert all(s in defense["description"] for s in ["POD", "133%", "173%", "SOD", "155%", "62%"])
    assert "distal-tissue" in defense["description"]
    assert "correlation-network outcomes" in fungi["description"]
    assert "biological_processes" not in fungi
    assert all("downstream" not in n for n in docs[3]["ecological_interactions"])


def test_all_original_nodes_and_arrows_have_retained_decisions():
    ledger, rows, docs = records()
    assert sum(len(r["node_decisions"]) for r in rows) == 13
    assert (
        sum(len(r["edges_before"]) for r in rows) == sum(len(r["edges_after"]) for r in rows) == 4
    )
    assert (
        ledger["primary_graph_snippet_count"]
        == ledger["independent_fresh_primary_graph_snippet_count"]
        == 28
    )
    for row, doc in zip(rows, docs, strict=True):
        assert not row["removed_node_decisions"] and not row["removed_edge_decisions"]
        renames = row["renamed_nodes"]

        def pairs(edges, mapping=renames):
            return {
                (mapping.get(e["source"], e["source"]), mapping.get(e["target"], e["target"]))
                for e in edges
            }

        assert pairs(row["edges_before"]) == pairs(row["edges_after"])
        names = {n["name"] for n in doc["ecological_interactions"]}
        assert names == {n["node"] for n in row["node_decisions"]}
        assert all(
            a.split("#", 1)[1] in names
            for d in doc["discussions"]
            for a in d["attaches_to"]
            if a.startswith("ecological_interactions#")
        )


def test_history_source_scope_and_research_remain_explicit():
    ledger, rows, docs = records()
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1668, 1669, 1670, 1671]
    assert ledger["unresolved_research_issues"] == [1672, 1673]
    assert ledger["unresolved_non_graph_issues"] == [1674]
    assert ledger["cache_changes"] == []
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert ledger["edison"]["dry_runs"][0]["query_chars"] == 15422
    for row, doc in zip(rows, docs, strict=True):
        assert set(row["allowed_changed_fields"]) == {
            "ecological_interactions",
            "discussions",
            "curation_history",
        }
        assert row["curation_events_added"] == len(row["history_files"]) == 1
        assert all((ROOT / p).exists() for p in row["history_files"])
        assert doc["curation_history"][-1]["llm_assisted"] is True
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
