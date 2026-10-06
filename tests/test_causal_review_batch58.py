"""Pin R2A/MOPS attribution, assay boundaries and complete review coverage."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-r2a-batch58.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    row = ledger["records"][0]
    return ledger, row, yaml.safe_load((ROOT / row["path"]).read_text())


def test_r2a_removes_misassigned_node_and_both_unsupported_arrows():
    _, row, doc = records()
    nodes = doc["ecological_interactions"]
    assert [n["name"] for n in nodes] == [
        "Predicted R2A Community Metabolite Exchange",
        "Pseudomonas Competitive Antagonism",
    ]
    assert len(row["edges_before"]) == 2
    assert not row["edges_after"]
    assert all("downstream" not in n for n in nodes)
    assert row["removed_node_decisions"][0]["node"] == (
        "Variovorax Cross-Feeding on Community Metabolites"
    )


def test_r2a_prediction_does_not_claim_experimental_flux_or_complete_membership():
    _, _, doc = records()
    node = doc["ecological_interactions"][0]
    assert node["description"].startswith("PARTIAL - ")
    assert "Sphingobium sp. AP49, not Variovorax CF313" in node["description"]
    assert "not measurements of exchange flux" in node["description"]
    assert "does not confirm metabolite transfer" in node["description"]
    assert "protein-based abundance estimates differ" in node["description"]
    assert "carbon uptake calibrated" in node["description"]
    assert "interaction_type" not in node and "source_taxon" not in node
    assert [t["preferred_term"] for t in node["participating_taxa"]] == [
        "Pantoea sp. YR343",
        "Pseudomonas sp. GM17",
    ]
    assert node["evidence"][0]["evidence_source"] == "COMPUTATIONAL"
    assert all("concentration" not in m for m in node["metabolites"])


def test_r2a_preserves_agar_inhibition_without_metabolite_rescue_claim():
    _, _, doc = records()
    node = doc["ecological_interactions"][1]
    assert node["scope"] == "PAIRWISE"
    assert node["source_taxon"]["preferred_term"] == "Pseudomonas sp. GM17"
    assert node["target_taxon"]["preferred_term"] == "Variovorax sp. CF313"
    assert "5 microliters" in node["description"]
    assert "25 degrees C for 48 hours" in node["description"]
    assert "HYPOTHESIZED" in node["description"]
    assert "liquid-versus-static-agar" in node["description"]
    assert "No selective metabolite rescue" in node["description"]
    assert node["evidence"][0]["evidence_source"] == "IN_VITRO"


def test_r2a_every_node_arrow_and_open_anchor_is_accounted_for():
    ledger, row, doc = records()
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1532]
    assert ledger["unresolved_non_graph_issues"] == [1533]
    assert row["status"] == "reviewed"
    assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
    names = {n["name"] for n in doc["ecological_interactions"]}
    assert {r["node"] for r in row["node_decisions"]} == names
    assert len(row["removed_node_decisions"]) == 1
    assert not row["retained_edge_decisions"]
    assert len(row["removed_edge_decisions"]) == 2
    assert {(e["source"], e["target"]) for e in row["removed_edge_decisions"]} == {
        (e["source"], e["target"]) for e in row["edges_before"]
    }
    discussion = doc["discussions"][-1]
    assert discussion["status"] == "OPEN" and discussion["kind"] == "KNOWLEDGE_GAP"
    assert {a.split("#", 1)[1] for a in discussion["attaches_to"]} == names
    assert doc["curation_history"][-1]["llm_assisted"] is True


def test_r2a_canonical_metadata_and_source_scope_remain_explicit():
    ledger, row, doc = records()
    assert [t["taxon_term"]["term"]["id"] for t in doc["taxonomy"]] == [
        "NCBITaxon:53335",
        "NCBITaxon:306",
        "NCBITaxon:34072",
    ]
    assert "#1533" in doc["discussions"][-1]["rationale"]
    assert ledger["primary_graph_fragments_verified"] == 4
    assert "no figure pixels" in row["source_review"]["scope"]
    assert row["source_review"]["cache_provenance_certified"] is False
    assert ledger["issue_deduplication"]["ignored_hidden_local_search"] is True
    assert ledger["baseline_commit"] != ledger["base_commit"]
    transition = ledger["ancestry_transition"]
    assert transition["old_head"] == ledger["baseline_commit"]
    assert transition["new_head"] == ledger["base_commit"]
    assert transition["unchanged_tree"] == ledger["base_tree"]
    for path, digest in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
