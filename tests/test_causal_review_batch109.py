"""Preserve positive outcomes without transferring evidence across assays or strains."""

import hashlib
import runpy
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261008-six-records-batch109.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / row["path"]).read_text()) for row in rows]


def test_fuqu_comparators_are_not_construction_causality_or_mutualism():
    _, rows, docs = records()
    nodes = docs[0]["ecological_interactions"]
    assert len(nodes) == 1
    outcome = nodes[0]
    assert "interaction_type" not in outcome and not outcome.get("downstream")
    assert "0.45, 0.40 and 0.64" in outcome["description"]
    assert "ethanol did not differ significantly" in outcome["description"]
    assert len(outcome["participating_taxa"]) == 13
    assert len(rows[0]["removed_node_decisions"]) == len(rows[0]["removed_edge_decisions"]) == 2


def test_syncom_y_preserves_reciprocal_biofilm_growth_not_just_total_biomass():
    _, _, docs = records()
    biofilm, outcome, _, _ = docs[1]["ecological_interactions"]
    assert biofilm["interaction_type"] == "MUTUALISM"
    assert "cell-equivalent abundance of both strains" in biofilm["description"]
    assert "WB abundance did not increase in the planktonic fraction" in biofilm["description"]
    assert "growth of both strains" in biofilm["evidence"][1]["snippet"]
    assert "interaction_type" not in outcome and "biological_processes" not in outcome
    assert "18.33%" in outcome["description"] and "79.13%" in outcome["description"]
    assert biofilm["downstream"][0]["description"].startswith("HYPOTHESIZED/PARTIAL:")


def test_syncom_y_positive_additions_are_not_direct_transfer():
    _, _, docs = records()
    forward = docs[1]["ecological_interactions"][2]
    assert "not direct donor-to-recipient transfer" in forward["description"]
    assert "Malate and guanosine were also included" in forward["description"]
    assert all(e["supports"] == "PARTIAL" for e in forward["evidence"])
    assert forward["downstream"][0]["description"].startswith("HYPOTHESIZED/PARTIAL:")


def test_syncom_y_reverse_additions_were_negative_not_untested():
    _, _, docs = records()
    reverse = docs[1]["ecological_interactions"][3]
    assert "did not significantly enhance" in reverse["description"]
    assert "does not prove that exchange is absent" in reverse["description"]
    result = reverse["evidence"][1]
    assert result["evidence_source"] == "IN_VITRO" and result["supports"] == "PARTIAL"
    assert "did not result in a significant enhancement" in result["snippet"]


def test_syncom_y_model_inputs_and_versions_are_not_invented():
    _, _, docs = records()
    predictions = docs[1]["ecological_interactions"][2:]
    for n in predictions:
        e = next(e for e in n["evidence"] if e["evidence_source"] == "COMPUTATIONAL")
        p = e["computational_provenance"]
        assert e["supports"] == "PARTIAL" and p["prediction_type"] == "FLUX_BALANCE_ANALYSIS"
        assert "input_accession" not in p
        assert all("tool_version" not in tool for tool in p["tools"])
        assert [t["tool_name"] for t in p["tools"]] == [
            "CarveMe",
            "COBRA Toolbox",
            "Flux Balance Analysis (FBA)",
        ]
        assert "RNA-seq, not verified genome inputs" in p["parameters"]


def test_azotobacter_growth_mutualism_is_distinct_from_phb_endpoint():
    _, _, docs = records()
    carbon, nitrogen, outcome = docs[2]["ecological_interactions"]
    assert carbon["interaction_type"] == "CROSS_FEEDING"
    assert nitrogen["interaction_type"] == "MUTUALISM"
    assert "neither member grows alone" in nitrogen["description"]
    assert (
        "not a claimed donor-to-recipient transfer product" in nitrogen["metabolites"][0]["notes"]
    )
    assert "interaction_type" not in outcome and "biological_processes" not in outcome
    assert outcome["scope"] == "COMMUNITY_LEVEL" and len(outcome["evidence"]) == 1
    assert "potential product, not demonstrated production" in outcome["description"]
    assert all(
        n["downstream"][0]["description"].startswith("HYPOTHESIZED/PARTIAL:")
        for n in [carbon, nitrogen]
    )


def test_bacillus168_does_not_inherit_3610_or_other_partner_persistence():
    _, rows, docs = records()
    carbon, growth = docs[3]["ecological_interactions"]
    assert carbon["target_taxon"]["preferred_term"] == "Bacillus subtilis 168"
    assert "3610" in carbon["description"] and "PARTIAL" in growth["description"]
    assert not growth.get("downstream") and "interaction_type" not in growth
    assert "does not establish weeks-to-months persistence" in growth["description"]
    assert "B. subtilis 168 produces alpha-amylase" in growth["evidence"][1]["snippet"]
    assert (
        rows[3]["removed_node_decisions"][0]["node"]
        == "Sucrose-Dependent Long-Term Consortium Stabilization"
    )


def test_ecoli_early_growth_is_not_sucrose_exclusive_or_a_concentration():
    _, _, docs = records()
    carbon, growth, reverse = docs[4]["ecological_interactions"]
    assert "concentration" not in carbon["metabolites"][0]
    assert "independently of induced sucrose export" in carbon["description"]
    assert "more than two weeks" in growth["evidence"][0]["snippet"]
    assert "interaction_type" not in growth
    assert reverse["interaction_type"] == "MUTUALISM"
    assert growth["downstream"][0]["description"].startswith("HYPOTHESIZED/PARTIAL:")


def test_yeast_parental_control_persistence_and_product_boundaries_remain():
    _, _, docs = records()
    carbon, growth, reverse = docs[5]["ecological_interactions"]
    assert carbon["target_taxon"]["preferred_term"] == "Saccharomyces cerevisiae W303Clump"
    assert "more than two months" in growth["description"]
    assert "two-month duration is not assigned to that diurnal assay" in growth["description"]
    assert "Parental W303 did not grow" in growth["description"]
    assert "does not demonstrate a bioproduct" in growth["description"]
    assert "interaction_type" not in growth and reverse["interaction_type"] == "MUTUALISM"
    assert "HYPOTHESIZED/PARTIAL" in growth["downstream"][0]["description"]


def test_all_original_nodes_and_edges_have_dispositions_without_extensions():
    ledger, rows, docs = records()
    assert ledger["reviewed_counts"] == {
        "retained_nodes": 16,
        "removed_nodes": 3,
        "retained_arrows": 9,
        "removed_arrows": 3,
        "renamed_nodes": 3,
        "graph_quotations": 28,
        "discussion_quotations": 6,
    }
    assert sum(len(r["edges_before"]) for r in rows) == 12
    assert sum(len(d["ecological_interactions"]) for d in docs) == 16
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert ledger["unresolved_non_graph_issues"] == [1855]
    assert ledger["issues"] == [1849, 1850, 1851, 1852, 1853, 1854]


def test_hashes_histories_and_canonical_identity_only_scope_are_explicit():
    ledger, rows, docs = records()
    assert ledger["independent_approval"] is False
    for row, doc in zip(rows, docs, strict=True):
        assert row["status"] == "reviewed"
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert set(row["allowed_changed_fields"]) == {
            "ecological_interactions",
            "discussions",
            "curation_history",
        }
        assert row["curation_events_added"] == len(row["history_files"]) == 1
        assert (ROOT / row["history_files"][0]).exists()
        assert doc["curation_history"][-1]["llm_assisted"] is True
        names = {n["name"] for n in doc["ecological_interactions"]}
        canonical = [
            {k: t["taxon_term"][k] for k in ["preferred_term", "term"]} for t in doc["taxonomy"]
        ]
        for n in doc["ecological_interactions"]:
            assert all(e["target"] in names for e in n.get("downstream", []))
            assert all(
                t in canonical and set(t) == {"preferred_term", "term"}
                for t in n.get("participating_taxa", [])
            )


def test_current_scope_census_tracks_later_source_bounded_repairs():
    # Batch119 moves Bacillus protection to all three THOR members: one more sole credit.
    # Batch124 adds yogurt's two named participants to mixed-scope records, not sole credit.
    survey = runpy.run_path(str(ROOT / "tests/test_community_level_connectivity_credit.py"))[
        "_survey"
    ]()
    assert survey == {
        "records": 460,
        "with_community_level": 415,
        "mixed": 137,
        "community_level_only": 278,
        "taxa": 1570,
        "credited_solely_by_the_rule": 1281,
    }
