"""Separate observed conditional product yields from their proposed mediator."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-clostridium-batch45.yaml"


def record():
    ledger = yaml.safe_load(LEDGER.read_text())
    row = ledger["records"][0]
    return ledger, row, yaml.safe_load((ROOT / row["path"]).read_text())


def test_electron_transfer_is_an_inferred_balance_not_measured_uptake():
    _, _, doc = record()
    transfer, response = doc["ecological_interactions"]
    assert transfer["description"].startswith("HYPOTHESIZED:")
    assert "does not directly measure electron uptake" in transfer["description"]
    assert "10% electron allocation to biomass" in transfer["description"]
    assert "remaining 90%" in transfer["description"]
    assert "not a measured flux" in transfer["description"]
    assert all(e["supports"] == "PARTIAL" for e in transfer["evidence"])
    (arrow,) = transfer["downstream"]
    assert arrow["target"] == response["name"]
    assert arrow["description"].startswith("HYPOTHESIZED:")
    assert "do not selectively establish" in arrow["description"]


def test_product_yields_are_conditional_not_mutualism_or_a_duplicate_event():
    _, _, doc = record()
    transfer, response = doc["ecological_interactions"]
    assert "two responsive cultures among four" in response["description"]
    assert "At 72 h" in response["description"]
    assert "eight of twelve" in response["description"]
    assert "regressions use those responders" in response["description"]
    assert "Clostridium growth was reduced" in response["description"]
    assert "do not establish mutual benefit" in response["description"]
    assert response["evidence"][0]["supports"] == "SUPPORT"
    assert "downstream" not in response
    for node in [transfer, response]:
        assert "interaction_type" not in node
        assert node["scope"] == "COMMUNITY_LEVEL"
        assert [p["term"] for p in node["participating_taxa"]] == [
            t["taxon_term"]["term"] for t in doc["taxonomy"]
        ]
    assert all(p["term"]["id"] != "GO:0022900" for p in response["biological_processes"])


def test_discussion_anchors_move_and_paywalled_assay_stays_unverified():
    _, _, doc = record()
    transfer, response = doc["ecological_interactions"]
    discussion = doc["discussions"][0]
    assert discussion["attaches_to"] == [
        "ecological_interactions#" + n["name"] for n in [transfer, response]
    ]
    assert "proposes, rather than measures" in discussion["rationale"]
    assert "pending-rename note is obsolete" in discussion["rationale"]
    assert "spent-medium result was not verified" in discussion["rationale"]
    assert all(e["supports"] == "PARTIAL" for e in discussion["evidence"])
    assert doc["discussions"][-1]["status"] == "OPEN"


def test_all_original_nodes_and_arrows_have_hash_bound_decisions():
    ledger, row, doc = record()
    assert ledger["review_mode"] == "source_based_self_adversarial_review"
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1478]
    assert len(ledger["records"]) == 1
    assert len(row["node_decisions"]) == 2
    assert len(row["removed_node_decisions"]) == 1
    assert len(row["retained_edge_decisions"]) == 1
    assert len(row["removed_edge_decisions"]) == 1
    assert len(row["edges_before"]) == 2 and len(row["edges_after"]) == 1
    assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
    assert len(row["history_files"]) == 1
    assert (ROOT / row["history_files"][0]).is_file()
    assert doc["curation_history"][-1]["llm_assisted"] is True
    assert ledger["issue_deduplication"]["ignored_hidden_local_search"] is True
    for path, digest in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
    assert "abstract only" in row["source_review"]["PMID:34939136"]["scope"]
    assert any("non-graph raw blocks" in value for value in ledger["limitations"])
