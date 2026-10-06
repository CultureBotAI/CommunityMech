"""Preserve positive observations without treating models as resolved mechanisms."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-wetup-elusimicrobia-batch49.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    return ledger, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in ledger["records"]]


def test_viral_predation_direction_and_ecosystem_participants():
    _, (doc, _) = records()
    activity, death, carbon = doc["ecological_interactions"]
    for node in [activity, carbon]:
        assert node["scope"] == "COMMUNITY_LEVEL"
        assert not {"interaction_type", "source_taxon", "target_taxon"} & node.keys()
        assert [p["preferred_term"] for p in node["participating_taxa"]] == [
            t["taxon_term"]["preferred_term"] for t in doc["taxonomy"]
        ]
    assert death["scope"] == "PAIRWISE" and death["interaction_type"] == "PREDATION"
    assert death["source_taxon"]["term"]["id"] == "NCBITaxon:10239"
    assert death["target_taxon"]["term"]["id"] == "NCBITaxon:2"
    assert carbon["metabolites"][0]["term"]["id"] == "CHEBI:16526"


def test_wetup_observation_and_modeled_mortality_are_distinct():
    _, (doc, _) = records()
    activity, death, carbon = doc["ecological_interactions"]
    assert "four-fold biomass increase" in activity["description"]
    assert "does not exclude nonintegrating temperate" in activity["description"]
    assert activity["evidence"][0]["evidence_source"] == "COMPUTATIONAL"
    assert activity["evidence"][0]["supports"] == "PARTIAL"
    assert activity["evidence"][1]["evidence_source"] == "IN_VITRO"
    assert "below 1% to 46.6%" in death["description"]
    assert "200 to 1 virions per cell" in death["description"]
    assert "not directly counted lysis" in death["description"]
    for node in [death, carbon]:
        assert all(e["supports"] == "PARTIAL" for e in node["evidence"])
        assert all(e["evidence_source"] == "COMPUTATIONAL" for e in node["evidence"])
    assert "six bacterial 16S copies" in doc["discussions"][0]["rationale"]


def test_viral_arrows_are_qualified_and_carbon_is_not_isolated_flux():
    _, (doc, _) = records()
    activity, death, carbon = doc["ecological_interactions"]
    assert activity["downstream"][0]["target"] == death["name"]
    assert activity["downstream"][0]["description"].startswith("PARTIAL -")
    assert death["downstream"][0]["target"] == carbon["name"]
    assert death["downstream"][0]["description"].startswith("HYPOTHESIZED -")
    assert "does not isolate the viral share of CO2" in death["downstream"][0]["description"]
    assert "downstream" not in carbon


def test_comparative_habitat_labels_do_not_become_self_exchange():
    _, (_, doc) = records()
    comparison, *intrinsic = doc["ecological_interactions"]
    assert comparison["scope"] == "COMMUNITY_LEVEL"
    members = comparison["participating_taxa"]
    assert len(members) == 2 and members[0]["term"] == members[1]["term"]
    assert [p["preferred_term"] for p in members] == [
        t["taxon_term"]["preferred_term"] for t in doc["taxonomy"]
    ]
    assert members[0]["preferred_term"] != members[1]["preferred_term"]
    assert "not a demonstrated coexisting community" in comparison["description"]
    for node in intrinsic:
        assert node["scope"] == "PAIRWISE" and node["source_taxon"] == members[0]
        assert not {"target_taxon", "participating_taxa"} & node.keys()
    for node in doc["ecological_interactions"]:
        assert not {"interaction_type", "downstream"} & node.keys()


def test_genomic_loci_and_predicted_functions_keep_distinct_support():
    _, (_, doc) = records()
    comparison, respiration, acetogenesis, paralog = doc["ecological_interactions"]
    for node in doc["ecological_interactions"]:
        assert all(e["evidence_source"] == "COMPUTATIONAL" for e in node["evidence"])
    assert comparison["evidence"][0]["supports"] == "SUPPORT"
    assert respiration["evidence"][0]["supports"] == "PARTIAL"
    assert acetogenesis["evidence"][0]["supports"] == "PARTIAL"
    assert [e["supports"] for e in paralog["evidence"]] == ["SUPPORT", "PARTIAL"]
    assert "not evidence of nitrogen fixation" in acetogenesis["description"]
    assert "do not demonstrate nitrogen fixation" in paralog["description"]
    assert "Predicted" in acetogenesis["biological_processes"][0]["notes"]
    assert "Hypothesized" in paralog["biological_processes"][0]["notes"]


def test_every_node_and_arrow_has_a_hash_bound_review_decision():
    ledger, docs = records()
    assert ledger["review_mode"] == "source_based_self_adversarial_review"
    assert ledger["independent_approval"] is False and ledger["issues"] == [1490, 1491]
    assert ledger["issue_deduplication"]["ignored_hidden_local_search"] is True
    for row, doc in zip(ledger["records"], docs, strict=True):
        assert [n["node"] for n in row["node_decisions"]] == [
            n["name"] for n in doc["ecological_interactions"]
        ]
        assert row["status"] == "reviewed" and row["removed_node_decisions"] == []
        assert len(row["edges_before"]) == len(row["retained_edge_decisions"]) + len(
            row["removed_edge_decisions"]
        )
        assert len(row["edges_after"]) == len(row["retained_edge_decisions"])
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert len(row["history_files"]) == 1 and (ROOT / row["history_files"][0]).is_file()
        assert doc["curation_history"][-1]["llm_assisted"] is True
        names = {n["name"] for n in doc["ecological_interactions"]}
        for gap in doc["discussions"]:
            assert gap["status"] == "OPEN"
            assert all(a.split("#", 1)[1] in names for a in gap["attaches_to"])
    assert sum(len(r["edges_before"]) for r in ledger["records"]) == 5
    assert sum(len(r["edges_after"]) for r in ledger["records"]) == 2
    for path, digest in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
