"""Keep measured observations distinct from workflow and inferred interactions."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261007-four-records-batch102.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in rows]


def test_vinegar_preserves_precursor_transfer_without_membership_arrows():
    _, _, docs = records()
    donor, ester, flavor, acid, endpoint = docs[0]["ecological_interactions"]
    assert donor["interaction_type"] == "CROSS_FEEDING"
    assert "source_taxon" not in donor and "target_taxon" not in donor
    assert donor["downstream"][0]["target"] == ester["name"]
    assert donor["downstream"][0]["description"].startswith("PARTIAL:")
    assert "excludes S. cerevisiae" in donor["downstream"][0]["description"]
    for node in [ester, flavor, acid, endpoint]:
        assert "interaction_type" not in node and not node.get("downstream")
    assert "not a universal optimum" in endpoint["description"]
    assert "without tracing pyruvate exchange" in endpoint["description"]
    assert endpoint["evidence"][2]["supports"] == "PARTIAL"


def test_skincom_retains_observations_without_procedure_or_mediation_claims():
    _, _, docs = records()
    diversity, detection, response = docs[1]["ecological_interactions"]
    assert all(
        not n.get("downstream") and "interaction_type" not in n
        for n in [diversity, detection, response]
    )
    assert "detected in both conditions" in diversity["description"]
    assert "HYPOTHESIZED:" in detection["description"]
    assert detection["evidence"][0]["supports"] == "PARTIAL"
    assert "a particular facilitating partner" in detection["description"]


def test_skincom_concordance_is_not_significance_replication():
    _, _, docs = records()
    response = docs[1]["ecological_interactions"][2]
    assert "66% agreement in the direction" in response["description"]
    assert "13 participants" in response["description"]
    assert "Only one human comparison was statistically significant" in response["description"]
    assert "not replication of significant effects" in response["description"]
    assert any(
        "No other changes were statistically significant" in e["snippet"]
        for e in response["evidence"]
    )


def test_soil_bgc_preserves_predictions_not_producer_or_niche_phenotypes():
    _, _, docs = records()
    heterogeneous, lap, environment = docs[2]["ecological_interactions"]
    for node in [heterogeneous, lap, environment]:
        assert "interaction_type" not in node and "biological_processes" not in node
        assert not node.get("downstream")
    assert "Linear Azole/Azoline-Containing Peptide" in lap["name"]
    assert "not linaridin" in lap["description"]
    assert "not measured peptide production" in lap["description"]
    for node in [heterogeneous, lap]:
        ev = node["evidence"][0]
        assert ev["evidence_source"] == "COMPUTATIONAL"
        assert ev["computational_provenance"]["tools"][0]["tool_version"] == "4.0"
    assert "more ketosynthase domains" in environment["description"]
    assert "not broadly different" in environment["description"]


def test_soil_cpr_distinguishes_detection_inference_and_realized_function():
    _, _, docs = records()
    rarity, dependence, respiration = docs[3]["ecological_interactions"]
    for node in [rarity, dependence, respiration]:
        assert "interaction_type" not in node and "biological_processes" not in node
        assert not node.get("downstream")
    assert "coverage-based estimates, not direct counts" in rarity["description"]
    assert "not natural population growth" in rarity["description"]
    assert "nondetection does not establish ecological absence" in rarity["description"]
    assert dependence["description"].startswith("HYPOTHESIZED:")
    assert "neutral effect on a host" in dependence["description"]
    assert "not extended to DPANN" in respiration["description"]
    assert "neither realized respiration nor an adaptive benefit" in respiration["description"]
    assert all(
        e["evidence_source"] == "COMPUTATIONAL" and e["supports"] == "PARTIAL"
        for n in [dependence, respiration]
        for e in n["evidence"]
    )


def test_narrowed_participants_use_only_canonical_identity():
    _, _, docs = records()
    for doc, index, members in [(docs[2], 0, [0, 1, 2]), (docs[2], 1, [3]), (docs[3], 2, [0])]:
        node = doc["ecological_interactions"][index]
        assert node["scope"] == "COMMUNITY_LEVEL"
        assert node["participating_taxa"] == [
            {k: doc["taxonomy"][i]["taxon_term"][k] for k in ["preferred_term", "term"]}
            for i in members
        ]
    assert (
        docs[2]["taxonomy"][2]["taxon_term"]["gtdb_classification"]["gtdb_id"]
        == "GTDB:c__Dormibacteria"
    )


def test_decisions_cover_every_original_node_and_direction():
    ledger, rows, docs = records()
    assert sum(len(r["node_decisions"]) for r in rows) == 14
    assert sum(len(r["removed_node_decisions"]) for r in rows) == 6
    assert sum(len(r["renamed_nodes"]) for r in rows) == 8
    assert sum(len(r["retained_edge_decisions"]) for r in rows) == 1
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 3
    for row, doc in zip(rows, docs, strict=True):
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert row["curation_events_added"] == len(row["history_files"]) == 1
        assert (ROOT / row["history_files"][0]).is_file()
        assert doc["curation_history"][-1]["llm_assisted"]
    assert ledger["primary_graph_snippet_count"] == len(ledger["snippet_checks"]) == 21
    assert len(ledger["discussion_snippet_checks"]) == 4
    assert all(
        c["cache_matched"] and c["independent_primary_match"]
        for c in ledger["snippet_checks"] + ledger["discussion_snippet_checks"]
    )


def test_followups_and_authorization_are_not_silently_resolved():
    ledger, _, _ = records()
    assert ledger["issues"] == [1803, 1804, 1805, 1806]
    assert ledger["unresolved_non_graph_issues"] == [1807]
    assert not ledger["independent_approval"]
    assert ledger["cache_changes"] == []
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert ledger["issue_deduplication"]["matching_issues"] == [445, 529, 949, 1042, 1043, 1044]
