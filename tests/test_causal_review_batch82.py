"""Preserve positive phenotypes without cross-system or workflow causation."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261007-four-records-batch82.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in rows]


def test_tailings_retains_assayed_biology_without_external_membership_credit():
    _, rows, docs = records()
    nitrogen, metal, ochro = docs[0]["ecological_interactions"]
    assert all(n["scope"] == "PAIRWISE" for n in [nitrogen, metal, ochro])
    assert all(
        "downstream" not in n and "interaction_type" not in n for n in [nitrogen, metal, ochro]
    )
    assert metal["source_taxon"]["term"]["id"] == "NCBITaxon:1386"
    assert "PP1 belongs to Rhizobium" in nitrogen["description"]
    assert "separate nitrogen-free vermiculite" in nitrogen["description"]
    assert "83.05" in ochro["description"]
    assert "does not unambiguously allocate" in ochro["description"]
    assert "Cd/Zn inconsistencies" in nitrogen["description"]
    assert rows[0]["status"] == "needs_research" and 1680 in rows[0]["issues"]


def test_positive_soil_carbon_is_preserved_without_a_fabricated_pair():
    _, _, docs = records()
    carbon = next(
        d
        for d in docs[0]["discussions"]
        if d["discussion_id"] == "panzhihua-positive-soil-carbon-result"
    )
    assert "positive aggregate result is retained" in carbon["rationale"]
    assert "carbon dioxide" in carbon["rationale"]
    assert carbon["evidence"][0]["reference"] == "PMID:38744211"
    assert len(docs[0]["taxonomy"]) == 6
    assert all("metabolites" not in n for n in docs[0]["ecological_interactions"])


def test_algal_positive_output_and_qualified_arrows_remain():
    _, _, docs = records()
    gas, growth, eps, product = docs[1]["ecological_interactions"]
    assert product["name"] == "Fourfold Coculture Biomass and Lipid Increase"
    assert "fourfold" in product["description"]
    assert "metabolites" not in product
    assert len(gas["metabolites"]) == 2
    assert "day 6" in growth["description"]
    assert gas["downstream"][0]["target"] == growth["downstream"][0]["target"] == product["name"]
    assert gas["downstream"][0]["description"].startswith("HYPOTHESIZED -")
    assert growth["downstream"][0]["description"].startswith("PARTIAL -")
    assert all("interaction_type" not in n for n in [gas, growth, eps, product])


def test_eps_viability_and_adhesion_do_not_become_traced_uptake():
    _, rows, docs = records()
    gas, _, eps, _ = docs[1]["ecological_interactions"]
    assert all(e["supports"] == "PARTIAL" for n in [gas, eps] for e in n["evidence"])
    assert "68%" in eps["description"] and "FluidFM" in eps["description"]
    assert "do not by themselves demonstrate" in eps["description"]
    assert rows[1]["status"] == "needs_research" and 1681 in rows[1]["issues"]


def test_milk_preserves_positive_and_negative_composition_comparisons():
    _, _, docs = records()
    tri, pair, weaker, _ = docs[2]["ecological_interactions"]
    assert "not uniquely superior" in tri["description"]
    assert "higher maximum acidification rate than either" in pair["description"]
    assert (
        "lower maximum acidification rates than the corresponding monocultures"
        in weaker["description"]
    )
    assert "75.95%" in weaker["description"]
    assert all("downstream" not in n for n in docs[2]["ecological_interactions"])
    assert all("interaction_type" not in n for n in docs[2]["ecological_interactions"])
    assert all("functional_role" not in t for t in docs[2]["taxonomy"])


def test_milk_lactate_is_a_mixed_pool_not_exclusive_c5i3_production():
    _, _, docs = records()
    lactate = docs[2]["ecological_interactions"][-1]
    assert lactate["name"] == "Set 2 Triculture D-Lactate Accumulation"
    assert "not exclusive C5I3" in lactate["description"]
    assert "83% L-lactate" in lactate["description"]
    assert any(
        d["discussion_id"] == "nws_set2_molecular_cross_feeding_mechanisms"
        for d in docs[2]["discussions"]
    )


def test_peanut_workflow_is_removed_but_reported_sa_direction_survives():
    _, _, docs = records()
    sa, rootrot, toxin, growth = docs[3]["ecological_interactions"]
    assert sa["downstream"][0]["target"] == rootrot["name"]
    assert sa["downstream"][0]["description"].startswith("PARTIAL -")
    assert all("downstream" not in n for n in [rootrot, toxin, growth])
    assert "CS showing the best effect" in rootrot["description"]
    assert "pathway-necessity" in sa["evidence"][0]["explanation"]


def test_peanut_toxin_and_growth_scope_remain_bounded_and_aliases_survive():
    _, rows, docs = records()
    _, _, toxin, growth = docs[3]["ecological_interactions"]
    assert "chemical destruction" in toxin["description"]
    assert toxin["evidence"][1]["supports"] == "PARTIAL"
    assert "CS-specific growth effect size" in growth["description"]
    raw = (ROOT / rows[3]["path"]).read_text()
    assert "&id001" in raw and "*id001" in raw
    assert rows[3]["status"] == "needs_research" and 1682 in rows[3]["issues"]


def test_every_original_node_and_arrow_has_a_disposition():
    ledger, rows, docs = records()
    assert sum(len(r["node_decisions"]) for r in rows) == 15
    assert sum(len(r["removed_node_decisions"]) for r in rows) == 5
    assert sum(len(r["edges_before"]) for r in rows) == 11
    assert sum(len(r["edges_after"]) for r in rows) == 3
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 8
    assert (
        ledger["primary_graph_snippet_count"]
        == ledger["independent_fresh_primary_graph_snippet_count"]
        == 25
    )
    for row, doc in zip(rows, docs, strict=True):
        names = {n["name"] for n in doc["ecological_interactions"]}
        assert names == {n["node"] for n in row["node_decisions"]}
        assert all(
            e["target"] in names
            for n in doc["ecological_interactions"]
            for e in n.get("downstream", [])
        )
        assert all(
            a.split("#", 1)[1] in names
            for d in doc["discussions"]
            for a in d["attaches_to"]
            if a.startswith("ecological_interactions#")
        )


def test_history_source_and_lifecycle_boundaries_are_explicit():
    ledger, rows, docs = records()
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1676, 1677, 1678, 1679]
    assert ledger["unresolved_research_issues"] == [1680, 1681, 1682]
    assert ledger["unresolved_non_graph_issues"] == [1683]
    assert ledger["cache_changes"] == []
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert ledger["edison"]["dry_runs"][0]["query_chars"] == 9111
    for row, doc in zip(rows, docs, strict=True):
        assert set(row["allowed_changed_fields"]) == {
            "ecological_interactions",
            "discussions",
            "curation_history",
        }
        assert row["curation_events_added"] == len(row["history_files"]) == 1
        assert all((ROOT / p).exists() for p in row["history_files"])
        assert doc["curation_history"][-1]["llm_assisted"] is True
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
