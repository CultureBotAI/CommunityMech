"""Keep measured growth and perturbations without reversing or inventing mechanisms."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-geobacter-pseudomonas-batch47.yaml"


def record():
    ledger = yaml.safe_load(LEDGER.read_text())
    row = ledger["records"][0]
    return ledger, row, yaml.safe_load((ROOT / row["path"]).read_text())


def test_donor_direction_and_positive_cytochrome_growth_evidence_survive():
    _, _, doc = record()
    growth, transfer, _, _ = doc["ecological_interactions"]
    assert transfer["source_taxon"]["term"] == doc["taxonomy"][1]["taxon_term"]["term"]
    assert transfer["target_taxon"]["term"] == doc["taxonomy"][0]["taxon_term"]["term"]
    assert transfer["interaction_type"] == "SYNTROPHY"
    assert "stunted growth" in transfer["description"]
    assert "omcZ- and omcS-deficient" in transfer["description"]
    assert "phenazine-deficient Pseudomonas cocultures still grew" in transfer["description"]
    assert "not direct electron-flux measurement" in transfer["description"]
    assert "pleiotropic mutant effects" in transfer["description"]
    assert {e["supports"] for e in transfer["evidence"]} == {"SUPPORT", "PARTIAL"}
    assert all(e["evidence_source"] == "IN_VITRO" for e in transfer["evidence"])
    (arrow,) = transfer["downstream"]
    assert arrow["target"] == growth["name"]
    assert arrow["description"].startswith("PARTIAL:")
    assert "not a causal claim that protein upregulation itself" in arrow["description"]


def test_community_observations_do_not_assert_competition_or_chronology_causation():
    _, _, doc = record()
    growth, _, adaptation, _ = doc["ecological_interactions"]
    for node in [growth, adaptation]:
        assert node["scope"] == "COMMUNITY_LEVEL"
        assert [p["term"] for p in node["participating_taxa"]] == [
            t["taxon_term"]["term"] for t in doc["taxonomy"]
        ]
        assert not {"interaction_type", "source_taxon", "target_taxon", "downstream"} & node.keys()
    assert "metabolites" not in adaptation
    assert "could not be isolated" in adaptation["description"]
    assert "not proof that either variant causes dominance" in adaptation["description"]
    assert "inactive cells or extracellular DNA" in adaptation["description"]
    assert "HybA and FdnG" in adaptation["description"]
    assert "does not quantify their fluxes" in adaptation["description"]
    assert adaptation["evidence"][0]["supports"] == "PARTIAL"
    assert adaptation["evidence"][-1]["supports"] == "SUPPORT"
    assert all(e["evidence_source"] == "IN_VITRO" for e in adaptation["evidence"])


def test_added_compound_response_is_not_endogenous_pseudomonas_pressure():
    _, _, doc = record()
    phenazine = doc["ecological_interactions"][3]
    assert phenazine["scope"] == "PAIRWISE"
    assert phenazine["source_taxon"]["term"] == doc["taxonomy"][0]["taxon_term"]["term"]
    assert (
        not {"interaction_type", "target_taxon", "participating_taxa", "downstream"}
        & phenazine.keys()
    )
    assert "Added commercial" in phenazine["description"]
    assert "below detection in all cocultures" in phenazine["description"]
    assert "did not select" in phenazine["description"]
    assert "does not exclude every phenazine derivative" in phenazine["description"]
    assert all(e["supports"] == "SUPPORT" for e in phenazine["evidence"])


def test_gaps_preserve_unresolved_routes_and_primary_duration_discrepancy():
    _, _, doc = record()
    names = {n["name"] for n in doc["ecological_interactions"]}
    assert len(doc["discussions"]) == 2
    for gap in doc["discussions"]:
        assert gap["kind"] == "KNOWLEDGE_GAP" and gap["status"] == "OPEN"
        assert all(a.split("#", 1)[1] in names for a in gap["attaches_to"])
    assert "HybA/FdnG" in doc["discussions"][0]["rationale"]
    assert "duration units" in doc["discussions"][1]["rationale"]
    assert "no precise duration is asserted" in doc["discussions"][1]["rationale"]


def test_all_original_nodes_and_arrows_have_hash_bound_decisions():
    ledger, row, doc = record()
    assert ledger["review_mode"] == "source_based_self_adversarial_review"
    assert ledger["independent_approval"] is False and ledger["issues"] == [1485]
    assert row["status"] == "reviewed"
    assert len(row["node_decisions"]) == len(doc["ecological_interactions"]) == 4
    assert row["removed_node_decisions"] == []
    assert len(row["edges_before"]) == 2 and len(row["edges_after"]) == 1
    assert len(row["retained_edge_decisions"]) == len(row["removed_edge_decisions"]) == 1
    assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
    assert len(row["history_files"]) == 1 and (ROOT / row["history_files"][0]).is_file()
    assert doc["curation_history"][-1]["llm_assisted"] is True
    for path, digest in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
    assert "abstract only" in row["source_review"]["PMID:28992596"]["scope"]
    assert ledger["issue_deduplication"]["ignored_hidden_local_search"] is True
