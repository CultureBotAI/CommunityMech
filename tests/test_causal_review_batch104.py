"""Guard workflow removal, source-system mapping and observation/mechanism boundaries."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261008-four-records-batch104.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in rows]


def test_sauce_keeps_bounded_endpoints_without_assembly_or_niche_claims():
    _, _, docs = records()
    (node,) = docs[0]["ecological_interactions"]
    assert node["name"] == "Laboratory Soy-Sauce Flavor Outcomes"
    assert "interaction_type" not in node and not node.get("downstream")
    assert len(node["evidence"]) == 3
    assert "laboratory comparison" in node["description"]
    assert "not proof of reduced competition" in node["description"]
    assert "ambiguous fold-change wording is not reinterpreted" in node["description"]


def test_chlorophyll_patterns_do_not_encode_selection_as_an_interaction():
    _, _, docs = records()
    genotype, succession, _ = docs[1]["ecological_interactions"]
    assert "metabolites" not in genotype and "metabolites" not in succession
    assert genotype["evidence"][0]["supports"] == "PARTIAL"
    assert "early pattern before selection" in genotype["description"]
    assert "unresolved pressures" in genotype["description"]
    assert "community-composition evidence" in succession["description"]
    assert "IAA/siderophore-mediated" in succession["description"]
    assert "biological_processes" not in succession
    assert genotype["participating_taxa"][0]["term"]["id"] == "NCBITaxon:374"


def test_chlorophyll_table_limits_are_not_replaced_by_blanket_significance():
    _, _, docs = records()
    phenotype = docs[1]["ecological_interactions"][2]
    assert "non-sterile-soil pots" in phenotype["description"]
    assert "shared significance letters" in phenotype["description"]
    assert "not uniformly significant superiority" in phenotype["description"]
    assert "Chlorophyll content did not differ" in phenotype["description"]
    assert "not field deployment" in phenotype["description"]
    assert phenotype["evidence"][0]["supports"] == "PARTIAL"


def test_sf_mapping_gap_preserves_positive_source_observations():
    ledger, rows, docs = records()
    assert docs[2]["id"] == "CommunityMech:000064"
    assert docs[2]["ecological_interactions"] == []
    assert rows[2]["status"] == "needs_research"
    assert len(rows[2]["removed_node_decisions"]) == 3
    discussion = docs[2]["discussions"][-1]
    assert "attaches_to" not in discussion
    assert "not a rejection" in discussion["rationale"]
    assert "HTTP403" in discussion["rationale"]
    assert len(discussion["evidence"]) == 2
    assert all(e["supports"] == "PARTIAL" for e in discussion["evidence"])
    assert ledger["unresolved_research_issues"] == [1820]


def test_soymilk_indirect_evidence_is_qualified_with_bounded_provenance():
    _, _, docs = records()
    for node in docs[3]["ecological_interactions"]:
        assert "HYPOTHESIZED:" in node["description"]
        assert "interaction_type" not in node and not node.get("downstream")
        ev = node["evidence"][0]
        assert ev["supports"] == "PARTIAL" and ev["evidence_source"] == "COMPUTATIONAL"
        provenance = ev["computational_provenance"]
        assert provenance["prediction_type"] == "STATISTICAL_INFERENCE"
        assert "abstract-level" in provenance["model_source"]
        assert "tools" not in provenance
    assert "not traced transfer" in docs[3]["ecological_interactions"][1]["description"]


def test_soymilk_succession_participants_are_canonical_identity_only():
    _, _, docs = records()
    doc = docs[3]
    assert doc["ecological_interactions"][0]["participating_taxa"] == [
        {k: doc["taxonomy"][i]["taxon_term"][k] for k in ["preferred_term", "term"]} for i in [0, 2]
    ]


def test_all_original_nodes_and_directions_have_dispositions():
    ledger, rows, docs = records()
    assert sum(len(r["node_decisions"]) for r in rows) == 6
    assert sum(len(r["removed_node_decisions"]) for r in rows) == 5
    assert sum(len(r["renamed_nodes"]) for r in rows) == 6
    assert sum(len(r["retained_edge_decisions"]) for r in rows) == 0
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 6
    for row, doc in zip(rows, docs, strict=True):
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert row["curation_events_added"] == len(row["history_files"]) == 1
        assert (ROOT / row["history_files"][0]).is_file()
        assert doc["curation_history"][-1]["llm_assisted"]
        assert all(
            "interaction_type" not in n and not n.get("downstream")
            for n in doc["ecological_interactions"]
        )
    assert ledger["primary_graph_snippet_count"] == len(ledger["snippet_checks"]) == 9
    assert len(ledger["discussion_snippet_checks"]) == 5
    assert all(
        c["cache_matched"] and c["independent_primary_match"]
        for c in ledger["snippet_checks"] + ledger["discussion_snippet_checks"]
    )


def test_followups_and_authorization_are_not_silently_resolved():
    ledger, _, _ = records()
    assert ledger["issues"] == [1816, 1817, 1818, 1819]
    assert ledger["unresolved_non_graph_issues"] == [1821]
    assert not ledger["independent_approval"]
    assert ledger["cache_changes"] == []
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert ledger["issue_deduplication"]["matching_issues"] == [497, 899]
