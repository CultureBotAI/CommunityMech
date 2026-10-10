"""Bound nutrient exchange and plant benefits to the evidence actually available."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261007-four-records-batch94.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in rows]


def test_reciprocal_exchange_directions_and_strain_context():
    _, _, docs = records()
    nitrogen, carbon, combined = docs[0]["ecological_interactions"]
    assert all(n["interaction_type"] == "CROSS_FEEDING" for n in [nitrogen, carbon, combined])
    assert (
        nitrogen["source_taxon"]["term"]["id"]
        == carbon["target_taxon"]["term"]["id"]
        == "NCBITaxon:1076"
    )
    assert (
        nitrogen["target_taxon"]["term"]["id"]
        == carbon["source_taxon"]["term"]["id"]
        == "NCBITaxon:562"
    )
    assert "recipient adaptation" in nitrogen["description"]
    assert "not a universal wild-type phenotype" in combined["description"]
    assert [n["downstream"][0]["target"] for n in [nitrogen, carbon]] == [combined["name"]] * 2


def test_carbon_transfer_excludes_unverified_products():
    _, _, docs = records()
    carbon = docs[0]["ecological_interactions"][1]
    assert "acetate, lactate and succinate" in carbon["description"]
    assert "excludes formate" in carbon["description"]
    assert "ethanol excretion is not evidence" in carbon["description"]
    assert "exception of formate" in carbon["evidence"][0]["snippet"]


def test_magnetite_real_cycle_and_charge_direction():
    _, _, docs = records()
    sharing, oxidation, reduction, battery = docs[1]["ecological_interactions"]
    assert oxidation["downstream"][0]["target"] == reduction["name"]
    assert reduction["downstream"][0]["target"] == oxidation["name"]
    assert "discharges" in oxidation["downstream"][1]["description"]
    assert "charges magnetite with electrons" in reduction["downstream"][1]["description"]
    assert "External light and electron-donor supply" in battery["description"]
    assert sum(len(n.get("downstream", [])) for n in [sharing, oxidation, reduction, battery]) == 5


def test_magnetite_community_scope_and_primary_provenance():
    _, _, docs = records()
    for node in docs[1]["ecological_interactions"]:
        assert node["scope"] == "COMMUNITY_LEVEL"
        assert "interaction_type" not in node
        assert "source_taxon" not in node and "target_taxon" not in node
        assert {t["term"]["id"] for t in node["participating_taxa"]} == {
            "NCBITaxon:395960",
            "NCBITaxon:35554",
        }
        assert all(e["reference"] == "PMID:25814583" for e in node["evidence"])
        assert "GO:0006826" not in str(node)
    assert "does not require obligacy" in docs[1]["discussions"][0]["rationale"]


def test_acid_soil_measured_yield_and_uncertain_mediation():
    _, _, docs = records()
    doc = docs[2]
    carbon, mitigation, phosphorus, outcome = doc["ecological_interactions"]
    assert all("Assembly" not in n["name"] for n in doc["ecological_interactions"])
    assert "assembly_strategy" in doc["engineering_design"]
    assert phosphorus["description"].startswith("HYPOTHESIZED:")
    assert phosphorus["evidence"][0]["supports"] == "PARTIAL"
    assert "26.36%" in outcome["description"]
    assert outcome["evidence"][0]["supports"] == "SUPPORT"
    assert all(
        e["description"].startswith(("HYPOTHESIZED:", "PARTIAL:"))
        for n in [carbon, mitigation, phosphorus]
        for e in n["downstream"]
    )
    assert "not the complete primary main text" in doc["discussions"][0]["rationale"]


def test_duckweed_efficacy_is_not_chemical_or_field_certification():
    _, _, docs = records()
    growth, control, outcome = docs[3]["ecological_interactions"]
    assert all("interaction_type" not in n for n in [growth, control, outcome])
    assert growth["evidence"][0]["supports"] == "PARTIAL"
    assert control["evidence"][0]["supports"] == "SUPPORT"
    assert "70%" in control["description"]
    assert all(n["downstream"][0]["description"].startswith("PARTIAL:") for n in [growth, control])
    assert all(m["term"]["id"] != "CHEBI:16982" for m in growth["metabolites"])
    assert "field efficacy" in outcome["description"]
    gap = docs[3]["discussions"][0]
    assert "were not measured" in gap["rationale"] and "conflicts" in gap["rationale"]
    assert "genetic necessity" in gap["evidence"][0]["snippet"]


def test_complete_dispositions_without_new_topology():
    _, rows, docs = records()
    assert sum(len(r["node_decisions"]) for r in rows) == 14
    assert sum(len(r["removed_node_decisions"]) for r in rows) == 1
    assert sum(len(r["edges_before"]) for r in rows) == 14
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 1
    assert sum(len(r["retained_edge_decisions"]) for r in rows) == 13
    for row, doc in zip(rows, docs, strict=True):
        assert {r["node"] for r in row["node_decisions"]} == {
            n["name"] for n in doc["ecological_interactions"]
        }
        assert not row["renamed_nodes"]
        for decision in row["retained_edge_decisions"]:
            assert all(decision["before"][k] == decision["after"][k] for k in ["source", "target"])
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]


def test_source_history_and_unresolved_scope():
    ledger, rows, docs = records()
    checks = ledger["snippet_checks"] + ledger["discussion_snippet_checks"]
    assert len(checks) == 21
    assert all(c["cache_matched"] and c["independent_primary_match"] for c in checks)
    assert ledger["primary_graph_snippet_count"] == 17 and ledger["cache_changes"] == []
    assert ledger["issues"] == [1755, 1756, 1757, 1758]
    assert ledger["unresolved_non_graph_issues"] == [1759]
    assert not ledger["independent_approval"]
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert ledger["edison"]["dry_runs"] == []
    for row, doc in zip(rows, docs, strict=True):
        assert row["curation_events_added"] == len(row["history_files"]) == 1
        assert doc["curation_history"][-1]["llm_assisted"]
        assert (ROOT / row["history_files"][0]).is_file()
