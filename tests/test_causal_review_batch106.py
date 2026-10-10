"""Guard source boundaries, omics interpretation and retained causal hypotheses."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261008-four-records-batch106.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in rows]


def test_species_pair_observations_do_not_form_cross_study_arrows():
    _, _, docs = records()
    nodes = docs[0]["ecological_interactions"]
    assert len(nodes) == 6 and all(not n.get("downstream") for n in nodes)
    assert [n.get("interaction_type") for n in nodes] == [
        None,
        None,
        "MUTUALISM",
        "COLONIZATION_FACILITATION",
        None,
        None,
    ]
    assert "HYPOTHESIZED/PARTIAL:" in nodes[2]["description"]
    assert nodes[2]["evidence"][0]["supports"] == "PARTIAL"
    assert nodes[2]["evidence"][0]["evidence_source"] == "COMPUTATIONAL"
    assert nodes[2]["evidence"][1]["evidence_source"] == "IN_VITRO"
    assert len(nodes[3]["evidence"]) == 3
    assert "without importing a hyphal requirement" in nodes[3]["description"]


def test_transcript_associations_are_not_virulence_or_colonization():
    _, _, docs = records()
    transcript = docs[0]["ecological_interactions"][-1]
    assert transcript["name"] == "Study-Specific Candida Transcript Response"
    assert "interaction_type" not in transcript
    assert [p["term"]["id"] for p in transcript["biological_processes"]] == ["GO:0010467"]
    assert len(transcript["evidence"]) == 1
    assert transcript["evidence"][0]["evidence_source"] == "COMPUTATIONAL"
    assert "not demonstrated changes in genotype" in transcript["description"]
    assert "computational_provenance" in transcript["evidence"][0]
    assert all("computational_provenance" not in e for e in docs[0]["discussions"][-1]["evidence"])


def test_mire_scopes_omics_and_retains_only_the_fen_niche_hypothesis():
    _, _, docs = records()
    doc = docs[1]
    archaea, bacteria, niche, gradient = doc["ecological_interactions"]
    for node, index in [(archaea, 1), (bacteria, 2), (niche, 1)]:
        assert node["participating_taxa"] == [
            {k: doc["taxonomy"][index]["taxon_term"][k] for k in ["preferred_term", "term"]}
        ]
        assert "source_taxon" not in node
    assert all("interaction_type" not in n for n in [archaea, bacteria, gradient])
    assert niche["interaction_type"] == "NICHE_PARTITIONING"
    assert "fen" in niche["description"] and niche["evidence"][1]["supports"] == "PARTIAL"
    assert niche["downstream"][0]["target"] == archaea["name"]
    assert niche["downstream"][0]["description"].startswith("HYPOTHESIZED/PARTIAL:")
    assert all(not n.get("downstream") for n in [archaea, bacteria, gradient])
    evidence = [e for n in doc["ecological_interactions"] for e in n["evidence"]]
    assert len(evidence) == 8
    assert all(e["reference"] == "PMID:38063415" for e in evidence)
    assert all(
        e["evidence_source"] == "COMPUTATIONAL" and e["computational_provenance"] for e in evidence
    )
    assert "wrong recipient route" in bacteria["description"]


def test_pesticide_performance_and_gene_presence_do_not_assert_mutualism():
    _, _, docs = records()
    growth, genes, removal, toxicity = docs[2]["ecological_interactions"]
    assert all("interaction_type" not in n for n in [growth, genes, removal, toxicity])
    assert "six-member immobilized" in growth["description"]
    assert genes["name"] == "C1 Herbicide-Catabolism Gene Detection"
    assert "not measured expression" in genes["description"]
    assert genes["evidence"][0]["supports"] == "SUPPORT"
    assert "complete mineralization" in removal["description"]
    assert toxicity["evidence"][0]["supports"] == "SUPPORT"


def test_pesticide_existing_directions_remain_qualified_not_deleted():
    _, _, docs = records()
    growth, genes, removal, toxicity = docs[2]["ecological_interactions"]
    assert genes["downstream"][0]["target"] == removal["name"]
    assert removal["downstream"][0]["target"] == toxicity["name"]
    assert all(
        n["downstream"][0]["description"].startswith("HYPOTHESIZED/PARTIAL:")
        for n in [genes, removal]
    )
    assert not growth.get("downstream") and not toxicity.get("downstream")


def test_aquifer_workflow_is_not_an_ecological_node_and_potential_is_not_flux():
    _, rows, docs = records()
    perturbation, decline, potential, flow = docs[3]["ecological_interactions"]
    assert [n["node"] for n in rows[3]["removed_node_decisions"]] == [
        "Native Carboxydocella Genome Resolution"
    ]
    assert perturbation["downstream"][0]["target"] == decline["name"]
    assert potential["downstream"][0]["target"] == flow["name"]
    assert all(
        n["downstream"][0]["description"].startswith("HYPOTHESIZED/PARTIAL:")
        for n in [perturbation, potential]
    )
    assert "does not establish absolute cell loss" in decline["description"]
    for node in [potential, flow]:
        assert node["evidence"][0]["evidence_source"] == "COMPUTATIONAL"
        assert node["evidence"][0]["computational_provenance"]["prediction_type"] == "OTHER"
    assert flow["evidence"][0]["supports"] == "PARTIAL"
    assert (
        "Removed two Subsurface Carboxydocella analysis edges"
        in docs[3]["curation_history"][0]["changes"]
    )


def test_all_original_nodes_and_directions_have_dispositions():
    ledger, rows, docs = records()
    assert sum(len(r["node_decisions"]) for r in rows) == 18
    assert sum(len(r["removed_node_decisions"]) for r in rows) == 1
    assert sum(len(r["renamed_nodes"]) for r in rows) == 8
    assert sum(len(r["retained_edge_decisions"]) for r in rows) == 5
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 5
    for row, doc in zip(rows, docs, strict=True):
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert row["status"] == "reviewed"
        assert row["curation_events_added"] == len(row["history_files"]) == 1
        assert (ROOT / row["history_files"][0]).is_file()
        assert doc["curation_history"][-1]["llm_assisted"]
    assert ledger["primary_graph_snippet_count"] == len(ledger["snippet_checks"]) == 29
    assert len(ledger["discussion_snippet_checks"]) == 7
    assert all(
        c["cache_matched"] and c["independent_primary_match"]
        for c in ledger["snippet_checks"] + ledger["discussion_snippet_checks"]
    )


def test_followups_and_provider_scope_are_not_silently_resolved():
    ledger, _, _ = records()
    assert ledger["issues"] == [1829, 1830, 1831, 1832]
    assert ledger["unresolved_non_graph_issues"] == [1833]
    assert ledger["unresolved_research_issues"] == []
    assert not ledger["independent_approval"]
    assert ledger["cache_changes"] == []
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert ledger["issue_deduplication"]["matching_issues"] == [294, 691, 763, 764]
