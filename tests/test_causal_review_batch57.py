"""Pin DVM assay boundaries and complete node/arrow review coverage."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-dvm-batch57.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    row = ledger["records"][0]
    return ledger, row, yaml.safe_load((ROOT / row["path"]).read_text())


def test_dvm_keeps_canonical_taxa_and_existing_graph_topology():
    _, row, doc = records()
    assert [t["taxon_term"]["term"]["id"] for t in doc["taxonomy"]] == [
        "NCBITaxon:881",
        "NCBITaxon:39152",
        "NCBITaxon:2208",
    ]
    nodes = doc["ecological_interactions"]
    assert len(nodes) == 4
    assert [n["scope"] for n in nodes] == [
        "COMMUNITY_LEVEL",
        "PAIRWISE",
        "PAIRWISE",
        "COMMUNITY_LEVEL",
    ]
    before = {(e["source"], e["target"]) for e in row["edges_before"]}
    after = {(e["source"], e["target"]) for e in row["edges_after"]}
    assert len(before) == 2 and before == after
    assert all(e["description"].startswith("PARTIAL - ") for e in row["edges_after"])


def test_dvm_preserves_positive_conversion_without_complete_acetate_use():
    _, _, doc = records()
    donor, _, mb, _ = doc["ecological_interactions"]
    assert "full lactate conversion" in donor["description"]
    assert "residual acetate remained" in donor["description"]
    assert "acetate is not a substrate for both" in donor["description"]
    assert "two syntrophy-enabling polymorphisms" in donor["description"]
    assert "higher methane output" in mb["description"]
    assert "not evidence for complete acetate use" in mb["description"]


def test_dvm_does_not_substitute_monoculture_or_pair_for_triculture_flux():
    _, _, doc = records()
    _, mm, mb, sulfate = doc["ecological_interactions"]
    assert "headspace already contained both gases" in mm["description"]
    assert "Separate monocultures" in mb["description"]
    assert "Mass balances in no-added-sulfate Dv-Mb pairs" in mb["description"]
    assert "shares in the tri-culture, are not resolved" in mb["description"]
    assert "7.5 mM" in sulfate["description"] and "15 mM" in sulfate["description"]
    assert "do not selectively isolate that mechanism" in sulfate["description"]
    for node in doc["ecological_interactions"]:
        assert all(e["reference"] == "doi:10.1098/rsif.2019.0129" for e in node["evidence"])
        assert all("concentration" not in m for m in node.get("metabolites", []))


def test_dvm_every_node_arrow_and_open_anchor_is_accounted_for():
    ledger, row, doc = records()
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1530]
    assert ledger["unresolved_non_graph_issues"] == [1364]
    assert row["status"] == "reviewed"
    assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
    names = {n["name"] for n in doc["ecological_interactions"]}
    assert len(row["node_decisions"]) == 4
    assert {r["node"] for r in row["node_decisions"]} == names
    assert not row["removed_node_decisions"] and not row["removed_edge_decisions"]
    assert len(row["retained_edge_decisions"]) == 2
    discussion = doc["discussions"][-1]
    assert discussion["status"] == "OPEN" and discussion["kind"] == "KNOWLEDGE_GAP"
    assert {a.split("#", 1)[1] for a in discussion["attaches_to"]} == names
    assert doc["curation_history"][-1]["llm_assisted"] is True


def test_dvm_primary_scope_and_cache_preservation_are_explicit():
    ledger, row, _ = records()
    assert ledger["primary_graph_fragments_verified"] == 7
    assert "1981 cached abstract only" in row["source_review"]["scope"]
    assert "no original images" in row["source_review"]["scope"]
    assert row["source_review"]["cache_provenance_certified"] is False
    assert ledger["issue_deduplication"]["ignored_hidden_local_search"] is True
    for path, digest in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
