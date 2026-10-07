"""Separate exact-system chemistry, cross-feeding and inferred partner benefits."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261007-four-records-batch93.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in rows]


def test_rammelsberg_uses_the_exact_study_without_pairwise_benefit_claims():
    _, _, docs = records()
    nodes = docs[0]["ecological_interactions"]
    assert len(nodes) == 3
    for node in nodes:
        assert node["scope"] == "COMMUNITY_LEVEL"
        assert "interaction_type" not in node
        assert "source_taxon" not in node and "target_taxon" not in node
        assert {t["term"]["id"] for t in node["participating_taxa"]} == {
            "NCBITaxon:920",
            "NCBITaxon:930",
        }
        assert "not an exhaustive community" in node["description"]
        assert all(e["reference"] == "doi:10.1016/j.hydromet.2020.105443" for e in node["evidence"])
    assert "91% cobalt and 57% copper" in nodes[1]["description"]
    assert "66% cobalt and 33% copper" in nodes[1]["description"]


def test_rammelsberg_keeps_iron_dissolution_but_not_unsupported_feedback():
    _, _, docs = records()
    iron, metals, sulfur = docs[0]["ecological_interactions"]
    assert iron["downstream"][0]["target"] == metals["name"]
    assert "iron(II) to iron(III)" in iron["downstream"][0]["description"]
    assert "downstream" not in metals and "downstream" not in sulfur
    assert "biological_processes" not in iron
    assert "indigenous organisms" in docs[0]["discussions"][-1]["rationale"]


def test_bde47_preserves_forward_cross_feeding_without_reverse_rescue():
    _, _, docs = records()
    init, conversion, outcome = docs[1]["ecological_interactions"]
    assert init["interaction_type"] == "CROSS_FEEDING"
    assert init["source_taxon"]["term"]["id"] == "NCBITaxon:160791"
    assert init["target_taxon"]["term"]["id"] == "NCBITaxon:264198"
    assert init["downstream"][0]["target"] == conversion["name"]
    assert conversion["name"] == "JMP134 2,4-dibromophenol conversion"
    assert conversion["scope"] == "COMMUNITY_LEVEL"
    assert "target_taxon" not in conversion and "interaction_type" not in conversion
    assert "not evidence of a reverse metabolite transfer" in conversion["description"]
    assert conversion["downstream"][0]["target"] == outcome["name"]


def test_bde47_distinguishes_parent_disappearance_from_intermediate_clearance():
    _, _, docs = records()
    _, conversion, outcome = docs[1]["ecological_interactions"]
    assert "not required for disappearance" in conversion["downstream"][0]["description"]
    assert "only the monoculture accumulated" in outcome["description"]
    assert "not an empirical closed carbon balance" in outcome["description"]
    assert "interaction_type" not in outcome
    assert all(e["supports"] == "SUPPORT" for e in outcome["evidence"])
    assert docs[1]["discussions"][0]["discussion_id"] == "bde47-monoculture-comparison"
    assert "does not assert obligacy" in docs[1]["discussions"][-1]["rationale"]


def test_ramc_remains_byte_identical_without_succinate_arrow():
    _, rows, docs = records()
    row, doc = rows[2], docs[2]
    assert row["outcome"] == "unchanged" and row["allowed_changed_fields"] == []
    assert row["original_sha256"] == row["record_sha256"]
    assert row["history_files"] == [] and row["curation_events_added"] == 0
    (node,) = doc["ecological_interactions"]
    assert node["interaction_type"] == "NICHE_PARTITIONING" and "downstream" not in node
    assert all(e["supports"] == "SUPPORT" for e in node["evidence"])
    assert "succinate" in str(doc["discussions"]).lower()


def test_ppow_separates_inferred_roles_from_bulk_removal_and_control_conflict():
    _, _, docs = records()
    (node,) = docs[3]["ecological_interactions"]
    assert node["description"].startswith("HYPOTHESIZED:")
    assert node["interaction_type"] == "NICHE_PARTITIONING" and "downstream" not in node
    assert [e["supports"] for e in node["evidence"]] == ["PARTIAL"] * 3 + ["SUPPORT"]
    assert docs[3]["discussions"][0]["discussion_id"] == "ppow_syncom_member_mechanism"
    gap = docs[3]["discussions"][-1]
    assert gap["discussion_id"] == "ppow_control_reporting_conflict"
    assert "Methods2.4" in gap["rationale"] and "conclusion" in gap["rationale"]
    assert len(gap["evidence"]) == 2


def test_all_original_nodes_and_edges_have_dispositions_and_no_new_direction():
    _, rows, docs = records()
    assert sum(len(r["node_decisions"]) for r in rows) == 8
    assert sum(len(r["removed_node_decisions"]) for r in rows) == 1
    assert sum(len(r["edges_before"]) for r in rows) == 6
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 3
    assert sum(len(r["retained_edge_decisions"]) for r in rows) == 3
    for row, doc in zip(rows, docs, strict=True):
        assert {r["node"] for r in row["node_decisions"]} == {
            n["name"] for n in doc["ecological_interactions"]
        }
        for decision in row["retained_edge_decisions"]:
            before, after = decision["before"], decision["after"]
            for key in ["source", "target"]:
                assert row["renamed_nodes"].get(before[key], before[key]) == after[key]
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]


def test_source_provenance_history_and_unresolved_scope_are_honest():
    ledger, rows, docs = records()
    checks = ledger["snippet_checks"] + ledger["discussion_snippet_checks"]
    assert len(checks) == 22 and all(c["cache_matched"] for c in checks)
    assert sum(c["independent_primary_match"] for c in checks) == 21
    assert len(ledger["cache_changes"]) == 2
    assert ledger["cache_changes"][0]["prior_cache_files_preserved"] == 921
    assert ledger["issues"] == [1750, 1751, 1752]
    assert ledger["unresolved_non_graph_issues"] == [1753]
    assert not ledger["independent_approval"]
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert ledger["edison"]["dry_runs"] == []
    assert [r["curation_events_added"] for r in rows] == [1, 1, 0, 1]
    for row, doc in zip(rows, docs, strict=True):
        if row["outcome"] == "changed":
            assert doc["curation_history"][-1]["llm_assisted"]
            assert (ROOT / row["history_files"][0]).is_file()
