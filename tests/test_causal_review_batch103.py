"""Guard source-system attribution and the difference between observation and mechanism."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261008-four-records-batch103.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in rows]


def test_corrinoid_directions_are_hypotheses_not_measured_transfer():
    _, _, docs = records()
    supply, response, reservoir = docs[0]["ecological_interactions"]
    assert all("interaction_type" not in n for n in [supply, response, reservoir])
    assert supply["downstream"][0]["target"] == reservoir["name"]
    assert reservoir["downstream"][0]["target"] == response["name"]
    assert all(
        n["downstream"][0]["description"].startswith("HYPOTHESIZED:") for n in [supply, reservoir]
    )
    ev = supply["evidence"][0]
    assert ev["supports"] == "PARTIAL" and ev["evidence_source"] == "COMPUTATIONAL"
    assert ev["computational_provenance"]["tools"][0]["tool_name"] == "DRAM"
    assert "tool_version" not in ev["computational_provenance"]["tools"][0]


def test_corrinoid_pool_and_amendments_have_distinct_scope():
    _, _, docs = records()
    _, response, reservoir = docs[0]["ecological_interactions"]
    assert response["metabolites"][0]["term"]["id"] == "CHEBI:33913"
    assert "largely lost" in response["description"]
    assert "predominantly cobalamin" in reservoir["description"]
    assert "does not separate intracellular from extracellular" in reservoir["description"]
    assert "accessibility to resident microbes remains unclear" in reservoir["description"]
    assert reservoir["evidence"][1]["supports"] == "PARTIAL"


def test_src1_subset_is_not_silently_reidentified_or_credited():
    ledger, rows, docs = records()
    assert docs[1]["id"] == "CommunityMech:000063"
    assert docs[1]["ecological_interactions"] == []
    assert rows[1]["status"] == "needs_research"
    assert len(rows[1]["removed_node_decisions"]) == 4
    discussion = docs[1]["discussions"][-1]
    assert "57 strains" in discussion["rationale"]
    assert "16-20-member" in discussion["rationale"]
    assert "attaches_to" not in discussion
    assert discussion["evidence"][0]["supports"] == "NO_EVIDENCE"
    assert ledger["unresolved_research_issues"] == [1813]


def test_src2v4_preserves_results_without_fitness_or_mediation_inference():
    _, _, docs = records()
    stability, growth, flavonoid = docs[2]["ecological_interactions"]
    assert all(
        "interaction_type" not in n and not n.get("downstream")
        for n in [stability, growth, flavonoid]
    )
    assert "Nonsignificance does not establish invariant abundance" in stability["description"]
    assert "prose and figure caption differ" in stability["description"]
    assert "heat-killed treatment did not significantly" in growth["description"]
    assert "not demonstrated reciprocal microbial fitness benefit" in growth["description"]
    assert "do not establish that flavonoids facilitate colonization" in flavonoid["description"]
    assert (
        "correlations restricted to SRC2v4-treated samples were not significant"
        in flavonoid["description"]
    )


def test_salt_pond_preserves_associations_and_activity_without_partner_claims():
    _, _, docs = records()
    restoration, archaea, bacteria, chemistry = docs[3]["ecological_interactions"]
    assert all(
        "interaction_type" not in n and not n.get("downstream")
        for n in [restoration, archaea, bacteria, chemistry]
    )
    assert "does not isolate restoration as a cause" in restoration["description"]
    assert "syntrophic product-removal feedback" in archaea["description"]
    assert any(e["evidence_source"] == "IN_VITRO" for e in archaea["evidence"])
    assert "not bacterial exclusivity" in bacteria["description"]
    assert bacteria["evidence"][0]["supports"] == "PARTIAL"
    assert "do not demonstrate sulfate-driven methanogenesis" in chemistry["description"]
    for node in [restoration, archaea, bacteria]:
        assert (
            node["evidence"][0]["computational_provenance"]["prediction_type"]
            == "STATISTICAL_INFERENCE"
        )


def test_salt_pond_participants_are_canonical_identity_only():
    _, _, docs = records()
    doc = docs[3]
    for node, taxon in [
        (doc["ecological_interactions"][1], doc["taxonomy"][2]),
        (doc["ecological_interactions"][2], doc["taxonomy"][1]),
    ]:
        assert node["scope"] == "COMMUNITY_LEVEL"
        assert "source_taxon" not in node and "target_taxon" not in node
        assert node["participating_taxa"] == [
            {k: taxon["taxon_term"][k] for k in ["preferred_term", "term"]}
        ]


def test_decisions_cover_all_original_nodes_and_directions():
    ledger, rows, docs = records()
    assert sum(len(r["node_decisions"]) for r in rows) == 10
    assert sum(len(r["removed_node_decisions"]) for r in rows) == 4
    assert sum(len(r["renamed_nodes"]) for r in rows) == 8
    assert sum(len(r["retained_edge_decisions"]) for r in rows) == 2
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 0
    for row, doc in zip(rows, docs, strict=True):
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert row["curation_events_added"] == len(row["history_files"]) == 1
        assert (ROOT / row["history_files"][0]).is_file()
        assert doc["curation_history"][-1]["llm_assisted"]
    assert ledger["primary_graph_snippet_count"] == len(ledger["snippet_checks"]) == 16
    assert len(ledger["discussion_snippet_checks"]) == 4
    assert all(
        c["cache_matched"] and c["independent_primary_match"]
        for c in ledger["snippet_checks"] + ledger["discussion_snippet_checks"]
    )


def test_followups_and_paid_authorization_are_not_silently_resolved():
    ledger, _, _ = records()
    assert ledger["issues"] == [1809, 1810, 1811, 1812]
    assert ledger["unresolved_non_graph_issues"] == [1814]
    assert not ledger["independent_approval"]
    assert ledger["cache_changes"] == []
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert ledger["issue_deduplication"]["matching_issues"] == [
        529,
        543,
        650,
        652,
        782,
        783,
        784,
        785,
        786,
        788,
        790,
        1281,
    ]
