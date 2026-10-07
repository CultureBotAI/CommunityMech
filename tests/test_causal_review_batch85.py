"""Keep positive endpoints separate from workflow and untested mediation."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261007-four-records-batch85.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in rows]


def test_denitrification_positives_survive_workflow_removal():
    _, rows, docs = records()
    nodes = docs[0]["ecological_interactions"]
    assert len(nodes) == 3
    assert (
        "greater productivity, denitrification rate and temporal stability"
        in nodes[0]["description"]
    )
    assert "generation 50" in nodes[1]["description"]
    assert "overyielding and asynchronous" in nodes[2]["description"]
    assert all(n.get("interaction_type") is None for n in nodes)
    assert all("downstream" not in n for n in nodes)
    assert len(rows[0]["removed_node_decisions"]) == 2
    assert len(rows[0]["removed_edge_decisions"]) == 4
    assert "200 generations" in docs[0]["engineering_design"]["perturbation_design"]


def test_denitrification_direction_and_exact_system_limits_remain_open():
    _, rows, docs = records()
    assert rows[0]["status"] == "needs_research" and 1706 in rows[0]["issues"]
    text = docs[0]["discussions"][-1]["rationale"]
    assert "not interchangeable" in text and "no new reversed arrow" in text
    assert (
        "isolate Paracoccus abundance as the causal driver"
        in docs[0]["ecological_interactions"][1]["description"]
    )


def test_beverage_empty_graph_is_not_misreported_as_complete():
    _, rows, docs = records()
    assert "ecological_interactions" not in docs[1]
    assert rows[1]["status"] == "needs_research" and rows[1]["issues"] == [1707]
    assert set(rows[1]["allowed_changed_fields"]) == {"discussions", "curation_history"}
    text = docs[1]["discussions"][-1]["rationale"]
    assert "9.32 and 7.05" in text and "BALB/c mice" in text
    assert "specific compound, or benefit in humans" in text
    assert docs[1]["discussions"][0]["discussion_id"] == "ccma_beverage_coculture_conditions"


def test_refinery_removal_keeps_monoculture_counterexample_and_arm_uncertainty():
    _, rows, docs = records()
    assert docs[2]["ecological_interactions"] == []
    assert rows[2]["status"] == "needs_research" and rows[2]["issues"] == [1708]
    text = docs[2]["discussions"][-1]["rationale"]
    assert "72% COD and 96.4%" in text and "80.4%" in text
    assert "Pico monoculture" in text and "62.2%" in text
    assert "does not resolve the Pico/Pico-Bac arm" in text
    assert "does not establish complete mineralization" in text


def test_pine_compatibility_is_not_stability_or_resource_partitioning():
    _, _, docs = records()
    node = docs[3]["ecological_interactions"][0]
    assert node["name"] == "Compatibility of Selected Endophytic Isolates"
    assert "no inhibition zones" in node["description"]
    assert "not demonstrated long-term stable coexistence" in node["description"]
    assert "metabolites" not in node and "biological_processes" not in node
    assert len(node["participating_taxa"]) == 5


def test_pine_inhibition_has_correct_assays_and_strain_participants():
    _, _, docs = records()
    node = docs[3]["ecological_interactions"][1]
    assert "Phomopsis sp." in node["description"]
    assert "cell-free fermentation supernatants" in node["description"]
    assert {t["preferred_term"] for t in node["participating_taxa"]} == {
        "Paenibacillus terrae RE7",
        "Bacillus velezensis NA3",
        "Bacillus subtilis NA11",
    }
    assert "RC1 and OB3 are not among" in node["description"]
    assert "biological_processes" not in node


def test_pine_positive_host_endpoints_are_in_vivo_without_mutualism():
    _, rows, docs = records()
    nodes = docs[3]["ecological_interactions"]
    assert "significantly increased" in nodes[2]["description"]
    assert "19.1% and 157.3%" in nodes[3]["description"]
    assert all(e["evidence_source"] == "IN_VIVO" for n in nodes[2:] for e in n["evidence"])
    assert "metabolites" not in nodes[2] and "biological_processes" not in nodes[2]
    assert all("interaction_type" not in n and "downstream" not in n for n in nodes)
    assert len(rows[3]["removed_edge_decisions"]) == 2


def test_pine_disease_control_not_implied_by_enzymes():
    _, rows, docs = records()
    text = docs[3]["ecological_interactions"][3]["description"]
    assert "do not alone demonstrate priming" in text
    assert "subsequent in planta biocontrol evaluation" in text
    assert rows[3]["status"] == "reviewed" and 1709 in rows[3]["issues"]


def test_every_original_node_arrow_and_anchor_has_disposition():
    ledger, rows, docs = records()
    assert sum(len(r["node_decisions"]) for r in rows) == 7
    assert sum(len(r["removed_node_decisions"]) for r in rows) == 2
    assert sum(len(r["edges_before"]) for r in rows) == 6
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 6
    assert all(r["edges_after"] == [] for r in rows)
    assert ledger["primary_graph_snippet_count"] == 8
    assert len(ledger["discussion_snippet_checks"]) == 8
    for row, doc in zip(rows, docs, strict=True):
        names = {n["name"] for n in doc.get("ecological_interactions", [])}
        assert names == {n["node"] for n in row["node_decisions"]}
        assert all(
            a.split("#", 1)[1] in names
            for d in doc["discussions"]
            for a in d["attaches_to"]
            if a.startswith("ecological_interactions#")
        )


def test_sources_history_and_pending_lifecycle_are_explicit():
    ledger, rows, docs = records()
    assert not ledger["independent_approval"]
    assert ledger["issues"] == [1704, 1705]
    assert ledger["unresolved_research_issues"] == [1706, 1707, 1708]
    assert ledger["unresolved_non_graph_issues"] == [1709]
    assert ledger["cache_changes"] == []
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert [d["query_chars"] for d in ledger["edison"]["dry_runs"]] == [11340, 7735, 8529]
    for row, doc in zip(rows, docs, strict=True):
        assert row["curation_events_added"] == len(row["history_files"]) == 1
        assert doc["curation_history"][-1]["llm_assisted"]
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
