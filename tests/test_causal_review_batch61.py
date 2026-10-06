"""Keep LBNL causal claims within the measured community and model boundaries."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-lbnl-batch61.yaml"
B = "LBNL_Brachypodium_Drought_SynCom15"
G = "LBNL_Human_Gut_Interaction_SynCom"
S = "LBNL_Switchgrass_Soil_SynCom16"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = {Path(row["path"]).stem: row for row in ledger["records"]}
    docs = {name: yaml.safe_load((ROOT / row["path"]).read_text()) for name, row in rows.items()}
    return ledger, rows, docs


def test_brachypodium_retains_functional_potential_not_assembly_procedures():
    _, rows, docs = records()
    genes, phenotypes, *_ = docs[B]["ecological_interactions"]
    assert len(docs[B]["ecological_interactions"]) == 5
    assert len(rows[B]["removed_node_decisions"]) == 2
    assert "gene presence does not establish expression" in genes["description"]
    assert all(ev["supports"] == "PARTIAL" for ev in genes["evidence"])
    assert "not measured transfer" in genes["metabolites"][0]["notes"]
    assert "member-level phenotypes" in phenotypes["description"]
    assert "not direct community flux" in phenotypes["description"]


def test_brachypodium_liquid_persistence_is_not_uniform_fifteen_member_stability():
    ledger, _, docs = records()
    persistence = docs[B]["ecological_interactions"][2]
    assert "six strains were undetectable or below 0.1%" in persistence["description"]
    assert "more balanced 16S relative profiles" in persistence["description"]
    assert "absolute viable counts" in persistence["description"]
    assert [ev["evidence_source"] for ev in persistence["evidence"]] == ["IN_VIVO", "IN_VITRO"]
    assert persistence["evidence"][0]["snippet"] == ledger["primary_matched_fragments"][3]
    assert persistence["evidence"][-1]["snippet"] == ledger["primary_matched_fragments"][0]
    assert not any(n.get("downstream") for n in docs[B]["ecological_interactions"])


def test_brachypodium_rewatering_and_spatial_results_keep_their_context():
    _, _, docs = records()
    recovery, location = docs[B]["ecological_interactions"][3:]
    assert "after drought followed by rewatering" in recovery["description"]
    assert "no significant differences" in recovery["description"]
    assert "during sustained drought" in recovery["description"]
    assert recovery["evidence"][0]["evidence_source"] == "IN_VIVO"
    assert "some other strains were instead enriched at the base" in location["description"]
    assert "HYPOTHESIZED" in location["description"]
    assert "do not trace migration" in location["description"]
    assert all(ev["evidence_source"] == "IN_VIVO" for ev in location["evidence"])


def test_gut_dynamics_does_not_encode_universal_acetate_crossfeeding():
    _, _, docs = records()
    dynamics, topology, feedback = docs[G]["ecological_interactions"]
    assert "metabolites" not in dynamics and "downstream" not in dynamics
    assert len(dynamics["evidence"]) == 2
    assert "not absence of higher-order effects" in dynamics["description"]
    assert "not direct viable-cell counts" in dynamics["description"]
    assert all("interaction_type" not in n for n in [dynamics, topology, feedback])
    assert "prior-literature example" in docs[G]["discussions"][-1]["rationale"]


def test_gut_positive_negative_model_feedback_is_preserved():
    _, rows, docs = records()
    _, topology, feedback = docs[G]["ecological_interactions"]
    (edge,) = topology["downstream"]
    assert edge["target"] == feedback["name"]
    assert edge["description"].startswith("PARTIAL - in the fitted pairwise gLV models")
    assert "negative feedback" in edge["description"]
    assert "broader tested growth-rate range than mutual inhibition" in edge["description"]
    assert "experimentally coexisting example" in feedback["description"]
    assert topology["evidence"][0]["evidence_source"] == "COMPUTATIONAL"
    assert feedback["evidence"][0]["evidence_source"] == "COMPUTATIONAL"
    assert len(rows[G]["retained_edge_decisions"]) == len(rows[G]["removed_edge_decisions"]) == 1


def test_soil_assay_memberships_are_not_all_the_final_sixteen():
    ledger, rows, docs = records()
    nutrient, ratio, host = docs[S]["ecological_interactions"]
    assert len(rows[S]["removed_node_decisions"]) == 2
    assert "initial equally mixed 18-strain" in nutrient["description"]
    assert "17/18-strain starting-ratio panels" in ratio["description"]
    assert "later 16-member dropout experiments are distinct" in ratio["description"]
    assert "17 or 18 isolates" in host["description"]
    assert nutrient["evidence"][-1]["snippet"] == ledger["primary_matched_fragments"][1]
    assert host["evidence"][-1]["snippet"] == ledger["primary_matched_fragments"][2]
    assert not any(n.get("downstream") for n in docs[S]["ecological_interactions"])


def test_soil_host_composition_is_not_mutual_benefit_or_absolute_viability():
    _, _, docs = records()
    nutrient, ratio, host = docs[S]["ecological_interactions"]
    assert "does not demonstrate increased absolute viable abundance" in nutrient["description"]
    assert "relative sequencing is not a direct viable-cell count" in ratio["description"]
    assert "not demonstrated reciprocal benefit" in host["description"]
    assert "single inoculum batch" in host["description"]
    assert "did not significantly change overall EcoFAB composition" in host["description"]
    assert all(ev["evidence_source"] == "IN_VIVO" for ev in host["evidence"])
    assert host["biological_processes"][0]["term"]["id"] == "GO:0044419"


def test_batch61_canonical_aggregate_and_cached_evidence_remain_explicit():
    ledger, _, docs = records()
    for path, digest in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
    for doc in docs.values():
        assert len(doc["taxonomy"]) == 1
        for node in doc["ecological_interactions"]:
            assert [t["term"]["id"] for t in node["participating_taxa"]] == ["NCBITaxon:2"]
        assert "aggregate placeholder" in doc["discussions"][-1]["rationale"]
        assert "#1548" in doc["discussions"][-1]["rationale"]
    assert ledger["unresolved_non_graph_issues"] == [1548]
    assert ledger["edison"]["provider_submissions"] == 0


def test_batch61_all_nodes_arrows_anchors_and_history_are_accounted_for():
    ledger, rows, docs = records()
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1545, 1546, 1547]
    assert sum(len(r["node_decisions"]) for r in rows.values()) == 11
    assert sum(len(r["removed_node_decisions"]) for r in rows.values()) == 4
    assert sum(len(r["edges_before"]) for r in rows.values()) == 2
    assert sum(len(r["edges_after"]) for r in rows.values()) == 1
    for name, row in rows.items():
        doc = docs[name]
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert doc["curation_history"][-1]["llm_assisted"] is True
        assert len(row["history_files"]) == 1 and row["status"] == "reviewed"
        assert row["source_review"]["all_retained_graph_snippets_primary_matched"] is True
        names = {n["name"] for n in doc["ecological_interactions"]}
        assert {d["node"] for d in row["node_decisions"]} == names
        assert {a.split("#", 1)[1] for a in doc["discussions"][-1]["attaches_to"]} == names
        assert doc["discussions"][-1]["status"] == "OPEN"
