"""Preserve measured outcomes while bounding hypotheses and missing graph work."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261007-four-records-batch77.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in rows]


def test_empty_nasal_graph_is_an_explicit_research_gap_not_a_completed_review():
    ledger, rows, docs = records()
    row, doc = rows[0], docs[0]
    assert not doc.get("ecological_interactions")
    assert row["status"] == "needs_research" and row["outcome"] == "unchanged"
    assert row["original_sha256"] == row["record_sha256"]
    assert row["curation_events_added"] == 0 and not row["history_files"]
    assert row["issues"] == [1640]
    assert ledger["unresolved_research_issues"] == [1640, 1641]


def test_xylan_positive_outcomes_survive_with_qualified_mediation():
    _, _, docs = records()
    transfer, utilization, enzymes = docs[1]["ecological_interactions"]
    assert all(n["interaction_type"] == "SYNTROPHY" for n in [transfer, utilization, enzymes])
    assert all(
        e["supports"] == "SUPPORT" for n in [transfer, utilization, enzymes] for e in n["evidence"]
    )
    assert transfer["source_taxon"]["term"]["id"] == "NCBITaxon:4757"
    assert transfer["target_taxon"]["term"]["id"] == "NCBITaxon:2173"
    assert [e["target"] for e in transfer["downstream"]] == [utilization["name"], enzymes["name"]]
    assert transfer["downstream"][0]["description"].startswith("PARTIAL -")
    assert transfer["downstream"][1]["description"].startswith("HYPOTHESIZED -")
    assert "catabolite repression" in transfer["downstream"][1]["description"]


def test_xylan_utilization_is_not_depolymerization_or_uniform_enzyme_response():
    _, _, docs = records()
    transfer, utilization, enzymes = docs[1]["ecological_interactions"]
    assert "alone did not utilize xylan" in transfer["description"]
    assert "18-day" in utilization["description"]
    assert (
        "does not imply a corresponding increase in polymer depolymerization"
        in utilization["description"]
    )
    for phrase in [
        "normalized to fungal protein",
        "not uniform fold changes",
        "endopeptidase was not increased",
    ]:
        assert phrase in enzymes["description"]


def test_ngawha_positive_gene_evidence_is_not_resolved_activity_for_every_member():
    _, _, docs = records()
    nodes = docs[2]["ecological_interactions"]
    potential = nodes[1]
    assert "hgcA/hgcB" in potential["description"]
    assert "could not be assigned to a resolved genome" in potential["description"]
    assert "sequencing-depth bounded" in potential["description"]
    assert "paralog filtering" in potential["description"]
    assert [e["supports"] for e in potential["evidence"]] == ["PARTIAL", "SUPPORT"]
    assert all(e["evidence_source"] == "COMPUTATIONAL" for e in potential["evidence"])
    assert all(
        "downstream" not in n and "interaction_type" not in n and "biological_processes" not in n
        for n in nodes
    )


def test_ngawha_measured_gaseous_mercury_is_preserved_without_biotic_attribution():
    _, _, docs = records()
    _, _, diversity, emission, model = docs[2]["ecological_interactions"]
    assert "does not demonstrate temporal stability" in diversity["description"]
    assert emission["name"] == "Measured Gaseous Mercury With Unresolved Microbial Contribution"
    assert "was measured above Tiger and Cub Baths" in emission["description"]
    assert "not an isolated microbial emission rate" in emission["description"]
    assert "deep geological inputs" in emission["description"]
    assert emission["evidence"][0]["supports"] == "SUPPORT"
    assert model["description"].startswith("HYPOTHESIZED -")
    assert model["evidence"][0]["supports"] == "PARTIAL"


def test_ldpe_proteomic_model_and_actual_outcomes_remain_distinct():
    _, rows, docs = records()
    row, doc = rows[3], docs[3]
    (node,) = doc["ecological_interactions"]
    assert row["status"] == "needs_research" and row["issues"] == [1639, 1641]
    assert "genomic and proteomic" in node["description"]
    assert node["evidence"][0]["supports"] == "PARTIAL"
    assert "interaction_type" not in node and "downstream" not in node
    assert "recombinant MCO1/Lcp3" in node["description"]
    rationale = doc["discussions"][-1]["rationale"]
    for phrase in [
        "9.98%",
        "50.88%",
        "half-dose",
        "not isotope-traced",
        "full-dose-matched synergy",
    ]:
        assert phrase in rationale
    assert doc["discussions"][0]["discussion_id"] == "z123_strain_specific_ldpe_steps"


def test_ngawha_cache_addition_is_bounded_and_provenance_tagged():
    ledger, _, docs = records()
    (change,) = ledger["cache_changes"]
    cache = ROOT / change["path"]
    assert hashlib.sha256(cache.read_bytes()).hexdigest() == change["sha256"]
    text = cache.read_text()
    assert "abstract_with_selected_author_manuscript_excerpts" in text
    assert "https://www.osti.gov/servlets/purl/1661210" in text
    assert "dde4319ba9bd4ee4fd8789cea57733f67a88220341c48780b6c1a7215a909701" in text
    nodes = docs[2]["ecological_interactions"]
    quotes = [e["snippet"] for n in [nodes[1], nodes[3]] for e in n["evidence"]]
    assert sum(len(q.split()) for q in quotes) == change["added_quoted_words"] == 22
    assert all(q in text for q in quotes)


def test_all_nodes_and_arrows_are_accounted_for_without_unapproved_extension():
    ledger, rows, docs = records()
    assert sum(len(r["node_decisions"]) for r in rows) == 9
    assert sum(len(r["edges_before"]) for r in rows) == 3
    assert sum(len(r["edges_after"]) for r in rows) == 2
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 1
    assert (
        ledger["primary_graph_snippet_count"] == ledger["cache_matched_graph_snippet_count"] == 12
    )
    assert all(c["independent_primary_match"] for c in ledger["snippet_checks"])
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert [(d["community_id"], d["query_chars"]) for d in ledger["edison"]["dry_runs"]] == [
        ("CommunityMech:000395", 10512),
        ("CommunityMech:000342", 8208),
    ]
    for row, doc in zip(rows, docs, strict=True):
        rename = row["renamed_nodes"]
        before = {
            (rename.get(e["source"], e["source"]), rename.get(e["target"], e["target"]))
            for e in row["edges_before"]
        }
        after = {(e["source"], e["target"]) for e in row["edges_after"]}
        removed = {
            (rename.get(e["source"], e["source"]), rename.get(e["target"], e["target"]))
            for e in row["removed_edge_decisions"]
        }
        assert after.isdisjoint(removed) and after | removed == before
        names = {n["name"] for n in doc.get("ecological_interactions", [])}
        assert names == {n["node"] for n in row["node_decisions"]}
        assert all(
            a.split("#", 1)[1] in names
            for d in doc.get("discussions", [])
            for a in d["attaches_to"]
            if a.startswith("ecological_interactions#")
        )


def test_scoped_histories_and_issue_lifecycle_remain_explicit():
    ledger, rows, docs = records()
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1637, 1638, 1639]
    assert ledger["unresolved_non_graph_issues"] == [1642]
    assert sum(r["curation_events_added"] for r in rows) == 3
    for row, doc in zip(rows, docs, strict=True):
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        changed = row["outcome"] == "changed"
        assert row["curation_events_added"] == len(row["history_files"]) == int(changed)
        assert row["allowed_changed_fields"] == (
            ["curation_history", "discussions", "ecological_interactions"] if changed else []
        )
        if changed:
            assert doc["curation_history"][-1]["llm_assisted"] is True
        assert all((ROOT / p).exists() for p in row["history_files"])
