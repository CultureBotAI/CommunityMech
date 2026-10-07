"""Keep evidence modality, microbial facilitation and host outcomes distinct."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261007-four-records-batch97.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in rows]


def test_candida_positive_interactions_and_modality_survive():
    _, _, docs = records()
    biofilm, eps, outcome = docs[0]["ecological_interactions"]
    assert biofilm["interaction_type"] == "MUTUALISM"
    assert eps["interaction_type"] == "COLONIZATION_FACILITATION"
    assert eps["evidence"][0]["evidence_source"] == "IN_VITRO"
    assert eps["downstream"][0]["target"] == biofilm["name"]
    assert biofilm["downstream"][0]["target"] == outcome["name"]
    assert biofilm["downstream"][0]["description"].startswith("PARTIAL:")


def test_selenomonas_retains_experimental_structure_support():
    _, _, docs = records()
    entrapment, biofilm, _ = docs[1]["ecological_interactions"]
    assert entrapment["interaction_type"] == "COLONIZATION_FACILITATION"
    assert entrapment["source_taxon"]["term"]["id"] == "NCBITaxon:1309"
    assert entrapment["target_taxon"]["term"]["id"] == "NCBITaxon:69823"
    assert all(n["evidence"][0]["evidence_source"] == "IN_VITRO" for n in [entrapment, biofilm])
    assert not entrapment["downstream"][0]["description"].startswith("PARTIAL:")
    assert "matrix-disruption" in biofilm["description"]
    assert biofilm["downstream"][0]["description"].startswith("PARTIAL:")


def test_veillonella_expression_is_not_catalytic_activity():
    _, _, docs = records()
    expression, biofilm, outcome = docs[2]["ecological_interactions"]
    assert "interaction_type" not in expression
    assert "do not independently measure catalytic enzyme activity" in expression["description"]
    assert len(expression["evidence"]) == 2
    assert biofilm["evidence"][0]["evidence_source"] == "IN_VITRO"
    assert all(
        n["downstream"][0]["description"].startswith("PARTIAL:") for n in [expression, biofilm]
    )
    assert outcome["name"] == "Rodent Coinfection Caries Outcome"
    assert "human adult severe caries" in outcome["description"]


def test_composite_and_host_outcomes_name_exact_members():
    _, _, docs = records()
    for doc in docs[:3]:
        expected = [
            {k: t["taxon_term"][k] for k in ["preferred_term", "term"]} for t in doc["taxonomy"]
        ]
        for node in doc["ecological_interactions"]:
            if node["scope"] != "COMMUNITY_LEVEL":
                continue
            assert not any(k in node for k in ["interaction_type", "source_taxon", "target_taxon"])
            assert node["participating_taxa"] == expected
            assert len(expected) == 2
        assert doc["ecological_interactions"][-1]["scope"] == "COMMUNITY_LEVEL"
        assert all(
            e["evidence_source"] == "IN_VIVO"
            for e in doc["ecological_interactions"][-1]["evidence"]
        )


def test_battery_facilitation_is_not_neutral_fitness():
    _, _, docs = records()
    detox, reduction = docs[3]["ecological_interactions"]
    assert detox["scope"] == "PAIRWISE" and "interaction_type" not in detox
    assert "unaffected" in detox["description"]
    assert detox["downstream"][0]["target"] == reduction["name"]
    assert "predecessor" in detox["downstream"][0]["description"]
    assert "not a quantitative partition" in reduction["description"]
    assert docs[3]["discussions"][0]["discussion_id"] == "SO3_BS3_SCALE_UP_STABILITY"


def test_all_nodes_and_directions_have_dispositions():
    _, rows, docs = records()
    assert sum(len(r["node_decisions"]) for r in rows) == 11
    assert sum(len(r["renamed_nodes"]) for r in rows) == 5
    assert sum(len(r["edges_before"]) for r in rows) == 7
    assert sum(len(r["retained_edge_decisions"]) for r in rows) == 7
    for row, doc in zip(rows, docs, strict=True):
        assert row["removed_node_decisions"] == row["removed_edge_decisions"] == []
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert {r["node"] for r in row["node_decisions"]} == {
            n["name"] for n in doc["ecological_interactions"]
        }
        for edge in row["retained_edge_decisions"]:
            assert all(
                row["renamed_nodes"].get(edge["before"][k], edge["before"][k]) == edge["after"][k]
                for k in ["source", "target"]
            )


def test_source_proofs_and_append_only_history():
    ledger, rows, docs = records()
    assert len(ledger["snippet_checks"]) == ledger["primary_graph_snippet_count"] == 16
    assert len(ledger["discussion_snippet_checks"]) == 4
    assert all(
        c["cache_matched"] and c["independent_primary_match"]
        for c in ledger["snippet_checks"] + ledger["discussion_snippet_checks"]
    )
    for row, doc in zip(rows, docs, strict=True):
        assert row["allowed_changed_fields"] == [
            "curation_history",
            "discussions",
            "ecological_interactions",
        ]
        assert row["curation_events_added"] == len(row["history_files"])
        assert row["curation_events_added"] == (
            2 if doc["id"] in ["CommunityMech:000084", "CommunityMech:000385"] else 1
        )
        assert doc["curation_history"][-1]["llm_assisted"]
        assert (ROOT / row["history_files"][0]).is_file()


def test_unresolved_scope_is_not_certified():
    ledger, _, _ = records()
    assert ledger["issues"] == [1772, 1773, 1774, 1775]
    assert ledger["unresolved_non_graph_issues"] == [1776]
    assert ledger["cache_changes"] == []
    assert not ledger["independent_approval"]
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert any("HTTP500" in s for s in ledger["limitations"])
    assert any("cross-sectional" in s for s in ledger["limitations"])
