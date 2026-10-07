"""Preserve positive outcomes while bounding system identity and mechanism claims."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261007-four-records-batch86.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in rows]


def test_pleuromutilin_keeps_positive_degradation_and_proposed_products():
    _, rows, docs = records()
    nodes = docs[0]["ecological_interactions"]
    assert len(nodes) == 2 and "91.97%" in nodes[0]["description"]
    assert nodes[1]["description"].startswith("HYPOTHESIZED:")
    assert "Differential abundance" in nodes[1]["description"]
    assert all("interaction_type" not in n and "downstream" not in n for n in nodes)
    assert all(len(n["participating_taxa"]) == 5 for n in nodes)
    assert len(rows[0]["removed_node_decisions"]) == 4


def test_pleuromutilin_context_and_missing_topology_remain_explicit():
    _, rows, docs = records()
    text = docs[0]["discussions"][-1]["rationale"]
    assert "Natural En4" in text and "no inhibition zones" in text
    assert "W12" in text and "W10" in text
    assert rows[0]["status"] == "needs_research" and 1715 in rows[0]["issues"]
    assert "no new structure is added" in text


def test_vanadium_preserves_controlled_precipitation_at_enrichment_scope():
    _, rows, docs = records()
    reduction, precipitation = docs[1]["ecological_interactions"]
    assert reduction["downstream"][0]["target"] == precipitation["name"]
    assert "autoclaved" in precipitation["description"]
    assert "no-vanadate controls" in precipitation["description"]
    assert "6 mM acetate and 1.5 mM vanadate" in reduction["description"]
    assert len(rows[1]["removed_node_decisions"]) == 2
    assert len(rows[1]["removed_edge_decisions"]) == 1
    assert "which formed VIV precipitates" in precipitation["evidence"][0]["snippet"]


def test_vanadium_does_not_credit_unsupported_canonical_partners():
    _, _, docs = records()
    nodes = docs[1]["ecological_interactions"]
    assert len(docs[1]["taxonomy"]) == 4
    for n in nodes:
        assert n["scope"] == "COMMUNITY_LEVEL"
        assert len(n["participating_taxa"]) == 1
        assert n["participating_taxa"][0]["term"]["id"] == "NCBITaxon:52972"
        assert not ({"source_taxon", "target_taxon", "interaction_type", "metabolites"} & n.keys())
    assert nodes[0]["evidence"][1]["evidence_source"] == "COMPUTATIONAL"
    assert "PARTIAL" in nodes[0]["description"]
    text = docs[1]["discussions"][-1]["rationale"]
    assert "Hunan" in text and "Acidithiobacillus ferrooxidans" in text
    assert "#1716" in text


def test_populus_keeps_two_qualified_biological_directions():
    _, rows, docs = records()
    nodes = docs[2]["ecological_interactions"]
    assert len(nodes) == 3 and len(rows[2]["removed_node_decisions"]) == 2
    assert len(rows[2]["removed_edge_decisions"]) == 3
    for n in nodes[:2]:
        assert n["downstream"][0]["target"] == nodes[2]["name"]
        assert n["downstream"][0]["description"].startswith("PARTIAL:")
    assert all(e["evidence_source"] == "IN_VIVO" for n in nodes for e in n["evidence"])
    assert "alternative" in nodes[2]["description"]
    assert "biological_processes" not in nodes[1]


def test_poultry_mechanism_is_hypothesized_not_niche_partitioning():
    _, rows, docs = records()
    nodes = docs[3]["ecological_interactions"]
    assert len(nodes) == 3 and rows[3]["removed_edge_decisions"] == []
    assert nodes[0]["description"].startswith("HYPOTHESIZED:")
    assert all(e["description"].startswith("HYPOTHESIZED:") for e in nodes[0]["downstream"])
    assert all(len(n["participating_taxa"]) == 3 for n in nodes)
    assert all("interaction_type" not in n for n in nodes)
    assert "total mixed-versus-single inoculum volume ambiguous" in nodes[0]["description"]
    assert "170 mW/m2" in nodes[1]["description"]


def test_poultry_cod_discrepancy_is_not_silently_corrected():
    _, _, docs = records()
    cod = docs[3]["ecological_interactions"][2]
    assert "2150-to-436" in cod["description"] and "2150-to-335" in cod["description"]
    assert "Do not silently swap" in cod["description"]
    assert "biomass assimilation and abiotic changes" in cod["description"]
    assert docs[3]["environmental_factors"][2]["value"] == "84.4"


def test_all_nodes_edges_and_anchors_have_dispositions():
    ledger, rows, docs = records()
    assert sum(len(r["node_decisions"]) for r in rows) == 10
    assert sum(len(r["removed_node_decisions"]) for r in rows) == 8
    assert sum(len(r["edges_before"]) for r in rows) == 11
    assert sum(len(r["retained_edge_decisions"]) for r in rows) == 5
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 6
    assert ledger["primary_graph_snippet_count"] == 11
    assert len(ledger["discussion_snippet_checks"]) == 8
    for row, doc in zip(rows, docs, strict=True):
        names = {n["name"] for n in doc["ecological_interactions"]}
        assert names == {n["node"] for n in row["node_decisions"]}
        assert all(
            e["target"] in names
            for n in doc["ecological_interactions"]
            for e in n.get("downstream", [])
        )
        assert all(
            a.split("#", 1)[1] in names
            for d in doc["discussions"]
            for a in d["attaches_to"]
            if a.startswith("ecological_interactions#")
        )


def test_supplement_cache_has_explicit_not_full_text_provenance():
    ledger, _, _ = records()
    assert len(ledger["cache_changes"]) == 1
    cache = (ROOT / ledger["cache_changes"][0]["path"]).read_text()
    assert "content_type: abstract_only" in cache
    assert "Public Supplement Figure S2 (not main-article full text)" in cache
    assert "Original PDF SHA256:" in cache
    assert "which formed VIV precipitates" in cache


def test_history_and_unfinished_lifecycle_are_explicit():
    ledger, rows, docs = records()
    assert not ledger["independent_approval"]
    assert ledger["issues"] == [1711, 1712, 1713, 1714]
    assert ledger["unresolved_research_issues"] == [1715]
    assert ledger["unresolved_non_graph_issues"] == [1716]
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert ledger["edison"]["dry_runs"][0]["query_chars"] == 11100
    for row, doc in zip(rows, docs, strict=True):
        assert row["curation_events_added"] == len(row["history_files"]) == 1
        assert doc["curation_history"][-1]["llm_assisted"]
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
