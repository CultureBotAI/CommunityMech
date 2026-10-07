"""Preserve observations while bounding mediation and repairing an arrow source."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261007-four-records-batch89.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / row["path"]).read_text()) for row in rows]


def test_waxy_removal_and_partial_mechanisms_survive():
    _, rows, docs = records()
    interface, model, removal = docs[0]["ecological_interactions"]
    assert len(rows[0]["edges_after"]) == 2
    assert interface["interaction_type"] == "CROSS_FEEDING"
    assert interface["description"].startswith("PARTIAL:")
    assert model["description"].startswith("PARTIAL:")
    assert "85.5%" in removal["description"]
    assert all("interaction_type" not in n for n in [model, removal])


def test_docking_is_not_independent_functional_validation():
    _, _, docs = records()
    evidence = docs[0]["discussions"][-1]["evidence"][-1]
    assert evidence["evidence_source"] == "COMPUTATIONAL"
    assert "not independent biological validation" in evidence["explanation"]
    assert "not evidence that perturbations were absent" in docs[0]["discussions"][-1]["rationale"]


def test_nitrate_response_is_not_partitioning_or_verified_flux():
    _, _, docs = records()
    (node,) = docs[1]["ecological_interactions"]
    assert "interaction_type" not in node and "downstream" not in node
    assert len(node["evidence"]) == len(node["participating_taxa"]) == 3
    assert "measurement type unresolved" in node["description"]
    assert "not verified transcription" in node["evidence"][1]["explanation"]
    assert (
        "does not establish whole-system nitrogen loss" in docs[1]["discussions"][-1]["rationale"]
    )


def test_bifenthrin_transformations_are_not_assimilation_or_fitness():
    _, rows, docs = records()
    division, transfer, removal = docs[2]["ecological_interactions"]
    assert len(rows[2]["edges_after"]) == 2
    assert transfer["interaction_type"] == "CROSS_FEEDING"
    assert "directly traced carbon assimilation" in transfer["description"]
    assert "not isolate that mediator" in division["description"]
    assert "complete mineralization or reciprocal partner fitness" in removal["description"]
    assert all("interaction_type" not in n for n in [division, removal])


def test_contact_arrow_is_reattached_without_inventing_a_claim():
    _, rows, docs = records()
    spread, comigration, contact = docs[3]["ecological_interactions"]
    assert "downstream" not in comigration
    assert spread["downstream"][0]["target"] == comigration["name"]
    assert contact["downstream"][0]["target"] == spread["name"]
    (correction,) = rows[3]["mechanical_edge_source_corrections"]
    old = next(e for e in rows[3]["edges_before"] if e["source"] == comigration["name"])
    new = contact["downstream"][0]
    assert old["target"] == new["target"]
    assert old["description"] == new["description"] == correction["description"]
    assert correction["original_source"] == comigration["name"]
    assert correction["corrected_source"] == contact["name"]


def test_social_joint_phenotype_does_not_assign_an_inducer_or_mutualism():
    _, _, docs = records()
    nodes = docs[3]["ecological_interactions"]
    assert all(n["scope"] == "COMMUNITY_LEVEL" for n in nodes)
    assert all(
        "interaction_type" not in n and "source_taxon" not in n and "target_taxon" not in n
        for n in nodes
    )
    canonical = [t["taxon_term"] for t in docs[3]["taxonomy"]]
    for node in nodes:
        assert node["participating_taxa"] == [
            {k: t[k] for k in ["preferred_term", "term"]} for t in canonical
        ]
    assert "semipermeable separation prevented it" in nodes[2]["description"]
    assert "#1736" in docs[3]["discussions"][-1]["rationale"]


def test_all_original_nodes_edges_and_graph_anchors_have_dispositions():
    _, rows, docs = records()
    assert sum(len(r["node_decisions"]) for r in rows) == 10
    assert sum(len(r["removed_node_decisions"]) for r in rows) == 0
    assert sum(len(r["edges_before"]) for r in rows) == 6
    assert sum(len(r["retained_edge_decisions"]) for r in rows) == 6
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 0
    for row, doc in zip(rows, docs, strict=True):
        names = {n["name"] for n in doc["ecological_interactions"]}
        assert names == {n["node"] for n in row["node_decisions"]}
        assert all(e["target"] in names for e in row["edges_after"])
        assert all(
            a.split("#", 1)[1] in names
            for d in doc["discussions"]
            for a in d["attaches_to"]
            if a.startswith("ecological_interactions#")
        )


def test_source_matches_are_not_full_text_certification():
    ledger, _, _ = records()
    assert ledger["primary_graph_snippet_count"] == 18
    assert len(ledger["discussion_snippet_checks"]) == 8
    checks = ledger["snippet_checks"] + ledger["discussion_snippet_checks"]
    assert len(checks) == 26 and all(c["independent_primary_match"] for c in checks)
    assert len(ledger["source_access"]) == 5


def test_history_no_spend_and_unfinished_followups_are_explicit():
    ledger, rows, docs = records()
    assert not ledger["independent_approval"]
    assert ledger["issues"] == [1732, 1733, 1734, 1735]
    assert ledger["unresolved_non_graph_issues"] == [1736]
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
