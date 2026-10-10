"""Keep source-bounded observations distinct from workflows and inferred mechanisms."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261007-four-records-batch88.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / row["path"]).read_text()) for row in rows]


def test_propanotroph_outcomes_and_qualified_directions_survive():
    _, rows, docs = records()
    nodes = docs[0]["ecological_interactions"]
    assert len(nodes) == 4 and len(rows[0]["edges_after"]) == 3
    assert all("interaction_type" not in n and "source_taxon" not in n for n in nodes)
    assert "sustained TCE degradation" in nodes[0]["description"]
    assert "sustained cDCE degradation" in nodes[1]["description"]
    assert all(e["description"].startswith("PARTIAL:") for e in nodes[2]["downstream"])
    assert nodes[3]["downstream"][0]["description"].startswith("HYPOTHESIZED:")


def test_propanotroph_gene_content_is_not_activity_or_crossfeeding():
    _, _, docs = records()
    nodes = docs[0]["ecological_interactions"]
    assert "Gene expression was not examined" in nodes[0]["description"]
    assert "does not establish which organisms or enzymes" in nodes[1]["description"]
    assert "separate enrichment treatments" in nodes[2]["description"]
    assert "#765" in docs[0]["discussions"][-1]["rationale"]


def test_prymnesium_correlations_are_not_reversed_into_new_arrows():
    _, rows, docs = records()
    outcome, biosynthesis, uptake, carbon = docs[1]["ecological_interactions"]
    assert all("downstream" not in n for n in [outcome, biosynthesis, uptake])
    assert carbon["downstream"][0]["target"] == outcome["name"]
    assert carbon["downstream"][0]["description"].startswith("HYPOTHESIZED:")
    assert len(rows[1]["removed_edge_decisions"]) == 2
    assert "positive observations" in outcome["description"]


def test_prymnesium_attribution_and_flux_limits_remain_visible():
    _, _, docs = records()
    nodes = docs[1]["ecological_interactions"]
    assert len(nodes[1]["participating_taxa"]) == 2
    assert "disagree on one producer identity" in nodes[1]["description"]
    assert "not directly quantify vitamin flux" in nodes[2]["description"]
    assert all("interaction_type" not in n for n in nodes)
    assert "#1728" in docs[1]["discussions"][-1]["rationale"]
    assert "no detected extracellular B12" in docs[1]["discussions"][-1]["rationale"]


def test_aniline_positive_removal_is_not_certified_mineralization():
    _, _, docs = records()
    (node,) = docs[2]["ecological_interactions"]
    assert len(node["evidence"]) == 2
    assert "91.28%" in node["evidence"][0]["snippet"]
    assert "73.06%" in node["evidence"][1]["snippet"]
    assert "do not by themselves establish complete mineralization" in node["description"]
    assert "downstream" not in node and "interaction_type" not in node
    assert "Supplements were not inspected" in docs[2]["discussions"][-1]["rationale"]


def test_factorial_workflow_removed_without_biological_mechanism_invention():
    _, rows, docs = records()
    (node,) = docs[3]["ecological_interactions"]
    assert "statistical" in node["description"]
    assert "ranking is illustrative" in node["description"]
    assert "not a linear biomass measure" in node["description"]
    assert len(node["participating_taxa"]) == 3
    assert len(rows[3]["removed_node_decisions"]) == 1
    assert "downstream" not in node
    assert "#1729" in docs[3]["discussions"][-1]["rationale"]


def test_all_original_nodes_edges_and_anchors_have_dispositions():
    _, rows, docs = records()
    assert sum(len(r["node_decisions"]) for r in rows) == 10
    assert sum(len(r["removed_node_decisions"]) for r in rows) == 1
    assert sum(len(r["edges_before"]) for r in rows) == 6
    assert sum(len(r["retained_edge_decisions"]) for r in rows) == 4
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 2
    for row, doc in zip(rows, docs, strict=True):
        names = {n["name"] for n in doc["ecological_interactions"]}
        assert names == {n["node"] for n in row["node_decisions"]}
        assert all(e["target"] in names for e in row["edges_after"])
        assert all(
            a.split("#", 1)[1] in names for d in doc["discussions"] for a in d["attaches_to"]
        )


def test_fresh_and_cached_source_verification_are_not_conflated():
    ledger, _, _ = records()
    assert ledger["primary_graph_snippet_count"] == 18
    assert len(ledger["discussion_snippet_checks"]) == 7
    checks = ledger["snippet_checks"] + ledger["discussion_snippet_checks"]
    cached = [c for c in checks if not c["independent_primary_match"]]
    assert len(cached) == 4
    assert {c["reference"] for c in cached} == {"PMID:42153623"}


def test_history_no_spend_and_unfinished_followups_are_explicit():
    ledger, rows, docs = records()
    assert not ledger["independent_approval"]
    assert ledger["issues"] == [1724, 1725, 1726, 1727]
    assert ledger["unresolved_non_graph_issues"] == [765, 1728, 1729]
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert ledger["edison"]["dry_runs"] == []
    for row, doc in zip(rows, docs, strict=True):
        assert row["curation_events_added"] == len(row["history_files"]) == 1
        assert row["status"] == "reviewed" and doc["curation_history"][-1]["llm_assisted"]


def test_reviewed_records_and_caches_are_hash_bound():
    ledger, rows, _ = records()
    assert ledger["cache_changes"] == []
    for row in rows:
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
    for path, digest in ledger["primary_artifacts"].items():
        if path.startswith("references_cache/"):
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
