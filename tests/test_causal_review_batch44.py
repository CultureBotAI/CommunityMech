"""Guard inferred flux, gross removal and host endpoints against stronger claims."""

import hashlib
import runpy
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-three-records-batch44.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    return ledger, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in ledger["records"]]


def test_ufmp_roles_and_both_arrows_remain_hypotheses():
    _, (doc, _, _) = records()
    first, chain, transfer = doc["ecological_interactions"]
    for node in (first, chain, transfer):
        assert node["description"].startswith("HYPOTHESIZED:")
        assert "source_taxon" not in node and "target_taxon" not in node
        assert "interaction_type" not in node
        assert all(e["supports"] == "PARTIAL" for e in node["evidence"])
        assert all(e["evidence_source"] == "COMPUTATIONAL" for e in node["evidence"])
        assert all(m["term"]["id"] != "CHEBI:422" for m in node.get("metabolites", []))
    assert [len(n["participating_taxa"]) for n in (first, chain, transfer)] == [6, 3, 5]
    assert "LCO1 is proposed to use lactose directly" in chain["description"]
    assert "assignment is inconclusive" in chain["description"]
    assert "predominantly produce butyrate" in chain["description"]
    assert "did not directly trace ATO3-to-CLOS1" in transfer["description"]
    assert first["downstream"][0]["target"] == transfer["name"]
    assert transfer["downstream"][0]["target"] == chain["name"]
    for node in (first, transfer):
        assert node["downstream"][0]["description"].startswith("HYPOTHESIZED:")


def test_ufmp_precise_guilds_do_not_invent_an_sph2_interaction():
    _, (doc, _, _) = records()
    ranker = runpy.run_path(str(ROOT / "scripts/rank_causal_graph_readiness.py"))
    connected = ranker["_connected_taxa"](doc["ecological_interactions"], doc["taxonomy"])
    canonical = {t["taxon_term"]["preferred_term"] for t in doc["taxonomy"]}
    assert len(connected) == 9
    assert canonical - connected == {"RUG023 sp. (MAG SPH2)"}
    assert "disconnected warning" in doc["discussions"][-1]["rationale"]


def test_gom_metrics_and_inoculum_limit_the_comparative_claim():
    _, (_, doc, _) = records()
    alk, arom, output = doc["ecological_interactions"]
    assert "60% at day 30" in alk["description"]
    assert "45% at day 75" in alk["description"]
    assert "not all 12" in arom["description"]
    assert "16% at day 75" in arom["description"]
    assert all(m["term"]["id"] != "CHEBI:28851" for m in arom["metabolites"])
    assert "did not subtract abiotic-control removal" in output["description"]
    assert "1e8 CFU/mL per strain" in output["description"]
    assert "not a total-inoculum-matched synergy test" in output["description"]
    for node in doc["ecological_interactions"]:
        assert len(node["participating_taxa"]) == 4
        assert "interaction_type" not in node and "downstream" not in node


def test_garlic_workflow_is_not_an_interaction_or_a_garlic_yield_assay():
    _, (_, _, doc) = records()
    (node,) = doc["ecological_interactions"]
    assert node["name"] == "Radish Seedling Length Response to Pseudomonas SynCom6"
    assert node["evidence"][0]["evidence_source"] == "IN_VIVO"
    assert "two-day incubator assay" in node["description"]
    assert "not a garlic field-yield result" in node["description"]
    assert "unresolved umbrella" in node["description"]
    assert "B8-7 alone did not promote growth" in node["description"]
    assert "downstream" not in node
    assert node["participating_taxa"][0]["term"] == doc["taxonomy"][0]["taxon_term"]["term"]
    assert "2026-10-02" in doc["discussions"][-1]["rationale"]


def test_every_original_node_and_arrow_has_a_decision():
    ledger, docs = records()
    assert ledger["review_mode"] == "source_based_self_adversarial_review"
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1474, 1475, 1476]
    assert sum(len(r["node_decisions"]) for r in ledger["records"]) == 7
    assert sum(len(r["removed_node_decisions"]) for r in ledger["records"]) == 2
    assert sum(len(r["retained_edge_decisions"]) for r in ledger["records"]) == 2
    assert sum(len(r["removed_edge_decisions"]) for r in ledger["records"]) == 2
    for row, doc in zip(ledger["records"], docs, strict=True):
        assert row["status"] == "reviewed"
        assert row["record_sha256"] == hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest()
        assert len(row["history_files"]) == 1 and (ROOT / row["history_files"][0]).is_file()
        assert doc["curation_history"][-1]["llm_assisted"] is True
        assert doc["discussions"][-1]["status"] == "OPEN"
        assert len(row["node_decisions"]) + len(row["removed_node_decisions"]) == 3


def test_source_hashes_and_scope_are_not_overcredited():
    ledger, _ = records()
    for path, digest in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
    assert ledger["issue_deduplication"]["ignored_hidden_local_search"] is True
    gom = ledger["records"][1]["source_review"]["doi:10.3389/fmars.2022.962071"]
    assert "one Methods sentence" in gom["scope"]
    assert len(gom["publisher"]["html_sha256"]) == 64
    assert any("non-graph raw blocks" in text for text in ledger["limitations"])
