"""Keep direct transfer and protective outcomes distinct from inferred mediation."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261008-four-records-batch107.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / row["path"]).read_text()) for row in rows]


def test_suillus_preserves_direct_transfer_and_host_benefit():
    _, _, docs = records()
    recruit, cue, vitamin, host = docs[0]["ecological_interactions"]
    assert recruit["interaction_type"] == "COLONIZATION_FACILITATION"
    assert "primarily enhanced swimming and swarming" in recruit["description"]
    assert "interaction_type" not in cue
    assert vitamin["interaction_type"] == "CROSS_FEEDING"
    assert "13C12-thiamine" in vitamin["evidence"][1]["snippet"]
    assert host["interaction_type"] == "MUTUALISM"
    assert "dry weight, root activity, and phosphorus" in host["evidence"][1]["snippet"]
    assert all(
        n["downstream"][0]["description"].startswith("HYPOTHESIZED/PARTIAL:")
        for n in [recruit, vitamin]
    )
    assert cue["downstream"][0]["target"] == vitamin["name"]


def test_spring_keeps_observations_without_spatial_causation_or_commensalism():
    _, rows, docs = records()
    nodes = docs[1]["ecological_interactions"]
    assert len(nodes) == 3
    assert all("interaction_type" not in n and not n.get("downstream") for n in nodes)
    assert "protein-associated elemental sulfur granules" in nodes[0]["description"]
    assert "source_taxon" not in nodes[0]
    assert "FISH" in nodes[1]["description"]
    assert len(rows[1]["removed_edge_decisions"]) == 2


def test_spring_identity_gap_cannot_be_counted_as_completed_review():
    ledger, rows, docs = records()
    assert rows[1]["status"] == "needs_research"
    assert ledger["unresolved_research_issues"] == [1841]
    assert 1841 in rows[1]["issues"]
    assert "not established" in docs[1]["ecological_interactions"][0]["description"]
    assert "51%" in docs[1]["discussions"][-1]["rationale"]
    assert "not verify" in docs[1]["ecological_interactions"][1]["description"]


def test_computational_evidence_stays_on_predictions_not_discussion_schema():
    _, _, docs = records()
    spring = docs[1]["ecological_interactions"][2]
    for index, e in enumerate(spring["evidence"]):
        assert e["supports"] == "PARTIAL" and e["evidence_source"] == "COMPUTATIONAL"
        expected = {"METABOLIC", "AlphaFold2"} | ({"HydDB"} if index == 0 else set())
        assert {t["tool_name"] for t in e["computational_provenance"]["tools"]} == expected
    exchange = docs[2]["ecological_interactions"][0]
    assert exchange["evidence"][0]["supports"] == "PARTIAL"
    assert exchange["evidence"][0]["computational_provenance"]["tools"][0]["tool_version"] == "2.0"
    assert exchange["evidence"][1]["evidence_source"] == "IN_VITRO"
    assert all(
        "computational_provenance" not in e
        for d in docs
        for x in d["discussions"]
        for e in x["evidence"]
    )


def test_chicken_preserves_immune_and_protective_outcomes_without_exclusive_mediation():
    _, _, docs = records()
    exchange, immune, protection = docs[2]["ecological_interactions"]
    assert exchange["interaction_type"] == "CROSS_FEEDING"
    assert "interaction_type" not in immune and "biological_processes" not in immune
    assert "flow cytometry" in immune["evidence"][1]["snippet"]
    assert "interaction_type" not in protection
    assert "may not be solely attributed" in protection["evidence"][1]["snippet"]
    assert immune["downstream"][0]["target"] == protection["name"]
    assert all(
        n["downstream"][0]["description"].startswith("HYPOTHESIZED/PARTIAL:")
        for n in [exchange, immune]
    )


def test_arc_preserves_rhizobia_boundary_and_poststorage_aflatoxin_endpoint():
    _, _, docs = records()
    doc = docs[3]
    suppression, nodulation, outcome = doc["ecological_interactions"]
    assert "interaction_type" not in suppression
    assert "After 12 months of natural storage" in suppression["evidence"][1]["snippet"]
    assert nodulation["interaction_type"] == "COLONIZATION_FACILITATION"
    assert "ARC alone did not induce nodulation" in nodulation["evidence"][1]["snippet"]
    assert "interaction_type" not in outcome
    assert "GO:0050832" not in [p["term"]["id"] for p in outcome["biological_processes"]]
    assert len(doc["engineering_design"]["counter_selection"]) == 1
    assert doc["engineering_design"]["counter_selection"][0]["excluded_count"] == 3
    for node, indexes in [(suppression, [0, 1, 3, 4]), (nodulation, [0, 1, 2, 4])]:
        assert node["participating_taxa"] == [
            {k: doc["taxonomy"][i]["taxon_term"][k] for k in ["preferred_term", "term"]}
            for i in indexes
        ]
        assert node["downstream"][0]["target"] == outcome["name"]
        assert node["downstream"][0]["description"].startswith("HYPOTHESIZED/PARTIAL:")


def test_all_original_nodes_and_directions_have_dispositions_without_extensions():
    ledger, rows, docs = records()
    assert sum(len(d["ecological_interactions"]) for d in docs) == 13
    assert sum(len(r["edges_before"]) for r in rows) == 9
    assert sum(len(r["edges_after"]) for r in rows) == 7
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 2
    assert sum(len(r["renamed_nodes"]) for r in rows) == 5
    assert not any(r["removed_node_decisions"] for r in rows)
    assert ledger["edison"]["provider_submissions"] == 0
    assert ledger["edison"]["credits_spent"] == 0
    for row in rows:
        assert len(row["retained_edge_decisions"]) == len(row["edges_after"])


def test_review_hashes_histories_and_non_graph_boundaries_are_explicit():
    ledger, rows, docs = records()
    assert ledger["independent_approval"] is False
    assert [r["status"] for r in rows] == ["reviewed", "needs_research", "reviewed", "reviewed"]
    for row, doc in zip(rows, docs, strict=True):
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert set(row["allowed_changed_fields"]) == {
            "ecological_interactions",
            "discussions",
            "curation_history",
        }
        expected_events = 2 if row["id"] == "CommunityMech:000222" else 1
        assert len(row["history_files"]) == row["curation_events_added"] == expected_events
        assert (ROOT / row["history_files"][0]).exists()
        assert doc["curation_history"][-1]["llm_assisted"] is True
        names = {n["name"] for n in doc["ecological_interactions"]}
        assert all(
            e["target"] in names
            for n in doc["ecological_interactions"]
            for e in n.get("downstream", [])
        )
