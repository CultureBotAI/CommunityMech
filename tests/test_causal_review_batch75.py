"""Preserve measured outcomes without promoting inferred mechanisms to facts."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261007-four-records-batch75.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    docs = [yaml.safe_load((ROOT / row["path"]).read_text()) for row in rows]
    return ledger, rows, docs


def test_sparse_feed_graph_is_reviewed_unchanged():
    _, rows, docs = records()
    row = rows[0]
    assert row["status"] == "reviewed" and row["outcome"] == "unchanged"
    assert row["record_sha256"] == row["original_sha256"]
    assert row["curation_events_added"] == 0 and row["history_files"] == []
    nodes = docs[0]["ecological_interactions"]
    assert len(nodes) == 2 and all("downstream" not in n for n in nodes)
    assert nodes[1]["evidence"][0]["supports"] == "PARTIAL"


def test_digestion_preserves_treatment_comparators_and_qualifies_mediation():
    _, _, docs = records()
    staged, transfer, selection = docs[1]["ecological_interactions"]
    for term in ["22%", "8%", "Both consortia", "1.6-fold", "native microbiome"]:
        assert term in staged["description"]
    assert staged["evidence"][0]["supports"] == "PARTIAL"
    assert staged["evidence"][1]["supports"] == "SUPPORT"
    assert staged["downstream"][0]["target"] == transfer["name"]
    assert transfer["downstream"][0]["target"] == selection["name"]
    for node in [staged, transfer]:
        assert node["downstream"][0]["description"].startswith("HYPOTHESIZED -")


def test_metagenomic_potential_is_not_expression_syntrophy_or_competition():
    _, _, docs = records()
    _, transfer, selection = docs[1]["ecological_interactions"]
    assert transfer["name"].startswith("Putative")
    assert "does not establish transcription" in transfer["description"]
    assert "direct electrical transfer" in transfer["description"]
    assert "interaction_type" not in transfer and "interaction_type" not in selection
    assert "SynCom-J produced a more robust network" in selection["description"]
    assert "not universally greater network stability" in selection["description"]


def test_corn_fraction_contributions_remain_without_mutualism():
    _, _, docs = records()
    cellulose, hemi, lignin, total = docs[2]["ecological_interactions"]
    for node, percent in zip(
        [cellulose, hemi, lignin], ["34.91%", "45.94%", "23.34%"], strict=True
    ):
        assert percent in node["description"]
        assert node["downstream"][0]["target"] == total["name"]
    assert all("interaction_type" not in n for n in [cellulose, hemi, lignin, total])
    assert hemi["evidence"][1]["supports"] == "PARTIAL"
    assert "not a necessity test" in hemi["evidence"][1]["explanation"]
    assert hemi["evidence"][2]["supports"] == "SUPPORT"
    assert "HYPOTHESIZED" in lignin["downstream"][0]["description"]
    assert "not additive whole-straw yield" in total["description"]


def test_probiotic_growth_is_retained_and_missing_outcome_stays_unresolved():
    ledger, rows, docs = records()
    (node,) = docs[3]["ecological_interactions"]
    for term in ["higher viable counts", "1%", "promoted monoculture growth", "PARTIAL"]:
        assert term in node["description"]
    assert "does not establish absence of antagonism" in node["description"]
    assert [e["supports"] for e in node["evidence"]] == ["SUPPORT", "PARTIAL", "SUPPORT"]
    assert docs[3]["discussions"][0]["discussion_id"] == "cicc_mmv_msra_causality_unresolved"
    assert rows[3]["status"] == "needs_research"
    assert ledger["unresolved_research_issues"] == [1629]
    assert ledger["unresolved_non_graph_issues"] == [1630]
    assert ledger["edison"]["target"] == "CommunityMech:000425"
    assert ledger["edison"]["dry_run_complete"] is True
    assert ledger["edison"]["provider_submissions"] == 0
    assert "downstream" not in node


def test_every_existing_node_and_arrow_is_accounted_for():
    ledger, rows, docs = records()
    assert sum(len(r["node_decisions"]) for r in rows) == 10
    assert sum(len(r["edges_before"]) for r in rows) == 5
    assert sum(len(r["edges_after"]) for r in rows) == 5
    assert (
        ledger["primary_graph_snippet_count"] == ledger["cache_matched_graph_snippet_count"] == 19
    )
    assert all(c["independent_primary_match"] for c in ledger["snippet_checks"])
    for row, doc in zip(rows, docs, strict=True):
        renames = row["renamed_nodes"]
        original = {
            (renames.get(e["source"], e["source"]), renames.get(e["target"], e["target"]))
            for e in row["edges_before"]
        }
        assert original == {(e["source"], e["target"]) for e in row["edges_after"]}
        assert row["removed_edge_decisions"] == []
        names = {n["name"] for n in doc["ecological_interactions"]}
        assert names == {n["node"] for n in row["node_decisions"]}
        assert all(
            a.split("#", 1)[1] in names
            for d in doc.get("discussions", [])
            for a in d["attaches_to"]
            if a.startswith("ecological_interactions#")
        )


def test_record_hashes_and_only_changed_record_histories_match():
    ledger, rows, docs = records()
    assert ledger["independent_approval"] is False
    assert sum(row["curation_events_added"] for row in rows) == 3
    for row, doc in zip(rows, docs, strict=True):
        expected = row["record_sha256"]
        if row["id"] == "CommunityMech:000274":
            followup = yaml.safe_load(
                (
                    ROOT
                    / "reports/causal_graph_review/decisions/20261007-five-records-batch91.yaml"
                ).read_text()
            )
            current = next(r for r in followup["records"] if r["path"] == row["path"])
            assert current["original_sha256"] == expected
            assert current["supersedes_review"] == {
                "review_file": str(LEDGER.relative_to(ROOT)),
                "record_sha256": expected,
            }
            expected = current["record_sha256"]
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == expected
        changed = row["outcome"] == "changed"
        assert row["curation_events_added"] == len(row["history_files"]) == int(changed)
        if changed:
            assert row["allowed_changed_fields"] == [
                "curation_history",
                "discussions",
                "ecological_interactions",
            ]
            assert doc["curation_history"][-1]["llm_assisted"] is True
        else:
            assert row["allowed_changed_fields"] == []
        assert all((ROOT / p).exists() for p in row["history_files"])
