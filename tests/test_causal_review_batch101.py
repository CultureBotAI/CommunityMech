"""Separate transfer direction, experimental configuration and outcome attribution."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261007-four-records-batch101.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in rows]


def test_fe0_keeps_reported_route_without_unverified_feedback():
    _, _, docs = records()
    donor, transfer, recipient = docs[0]["ecological_interactions"]
    assert all("interaction_type" not in n for n in [donor, transfer, recipient])
    assert donor["downstream"][0]["target"] == transfer["name"]
    assert transfer["downstream"][0]["target"] == recipient["name"]
    assert transfer["source_taxon"]["term"]["id"] == "NCBITaxon:70863"
    assert transfer["target_taxon"]["term"]["id"] == "NCBITaxon:287"
    assert "product-removal feedback" in transfer["description"]
    assert "not by itself proof" in transfer["description"]
    assert "direct electron cross-feeding" in transfer["description"]


def test_starch_keeps_only_one_way_provisioning_and_configuration_bound_current():
    _, _, docs = records()
    supply, current = docs[1]["ecological_interactions"]
    assert supply["interaction_type"] == "CROSS_FEEDING"
    assert supply["source_taxon"]["term"]["id"] == "NCBITaxon:1335"
    assert supply["target_taxon"]["term"]["id"] == "NCBITaxon:211586"
    assert supply["downstream"][0]["target"] == current["name"]
    assert "interaction_type" not in current
    assert "source_taxon" not in current and "target_taxon" not in current
    assert not current.get("downstream")
    assert "after removal of the fermenter" in supply["description"]
    assert (
        "two-step EGT broth experiment, not to the simultaneous coculture" in current["description"]
    )
    assert "parallel EGP configuration also" in current["description"]
    assert any("performed simultaneously" in e["snippet"] for e in current["evidence"])
    assert any("with electricity generation" in e["snippet"] for e in current["evidence"])


def test_scoped_participants_preserve_exact_canonical_identity_only():
    _, _, docs = records()
    for doc, index, members in [(docs[1], 1, [0]), (docs[2], 0, [0, 1])]:
        node = doc["ecological_interactions"][index]
        assert node["scope"] == "COMMUNITY_LEVEL"
        assert "source_taxon" not in node and "target_taxon" not in node
        assert node["participating_taxa"] == [
            {k: doc["taxonomy"][i]["taxon_term"][k] for k in ["preferred_term", "term"]}
            for i in members
        ]


def test_pda_preserves_indicator_result_without_flux_or_feedback_equivalence():
    _, _, docs = records()
    aggregation, transfer, indicator = docs[2]["ecological_interactions"]
    assert all("interaction_type" not in n for n in [aggregation, transfer, indicator])
    for node, target in [(aggregation, transfer), (transfer, indicator)]:
        assert node["downstream"][0]["target"] == target["name"]
        assert node["downstream"][0]["description"].startswith("PARTIAL:")
    assert "elimination of all mediated transfer" in transfer["description"]
    assert "380% higher" in indicator["description"]
    assert "without equating" in indicator["description"]
    assert "total electron flux" in indicator["description"]


def test_shrimp_remains_unchanged_and_does_not_gain_unsupported_edges():
    _, rows, docs = records()
    row, doc = rows[3], docs[3]
    assert row["outcome"] == "unchanged"
    assert row["original_sha256"] == row["record_sha256"]
    assert row["curation_events_added"] == 0 and row["history_files"] == []
    (node,) = doc["ecological_interactions"]
    assert node["scope"] == "COMMUNITY_LEVEL"
    assert "interaction_type" not in node and not node.get("downstream")
    assert "rather than a genus-to-pathogen antagonism edge" in node["description"]


def test_decision_coverage_and_append_only_provenance():
    ledger, rows, docs = records()
    assert sum(len(r["node_decisions"]) for r in rows) == 9
    assert sum(len(r["removed_node_decisions"]) for r in rows) == 1
    assert sum(len(r["renamed_nodes"]) for r in rows) == 3
    assert sum(len(r["retained_edge_decisions"]) for r in rows) == 5
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 1
    for row, doc in zip(rows, docs, strict=True):
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        count = int(row["outcome"] == "changed")
        assert row["curation_events_added"] == len(row["history_files"]) == count
        if count:
            assert (ROOT / row["history_files"][0]).is_file()
            assert doc["curation_history"][-1]["llm_assisted"]
        names = {n["name"] for n in doc["ecological_interactions"]}
        assert all(
            e["target"] in names
            for n in doc["ecological_interactions"]
            for e in n.get("downstream", [])
        )
    assert ledger["primary_graph_snippet_count"] == len(ledger["snippet_checks"]) == 15
    assert len(ledger["discussion_snippet_checks"]) == 3
    assert all(
        c["cache_matched"] and c["independent_primary_match"]
        for c in ledger["snippet_checks"] + ledger["discussion_snippet_checks"]
    )


def test_followups_access_limits_and_authorization_are_preserved():
    ledger, _, _ = records()
    assert ledger["issues"] == [1798, 1799, 1800]
    assert ledger["unresolved_non_graph_issues"] == [1801]
    assert not ledger["independent_approval"]
    assert ledger["cache_changes"] == []
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert ledger["issue_deduplication"]["matching_issues"] == [1105, 1106]
