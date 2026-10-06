"""Keep positive DIET evidence, exact systems and unfinished acetate branches distinct."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-methanogens-batch46.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    return ledger, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in ledger["records"]]


def test_methanosaeta_uses_defined_coculture_evidence_without_aggregate_necessity():
    _, (doc, _) = records()
    donor, transfer, methane = doc["ecological_interactions"]
    assert donor["name"] == "Geobacter Ethanol Oxidation"
    assert "not a claim" in donor["description"]
    assert "Aggregate formation itself was not selectively perturbed" in transfer["description"]
    assert "Methanosaeta concilii" in transfer["description"]
    assert "methanogen electron-entry components remain unresolved" in transfer["description"]
    assert "roughly one-third" in methane["description"]
    assert "not all methane" in methane["description"]
    assert "missing acetate branch" in methane["description"]
    assert donor["downstream"][0]["target"] == transfer["name"]
    assert transfer["downstream"][0]["target"] == methane["name"]
    assert "not acetate carbon" in donor["downstream"][0]["description"]
    assert "interaction_type" not in donor and "interaction_type" not in methane
    assert transfer["interaction_type"] == "SYNTROPHY"
    for node in doc["ecological_interactions"]:
        assert node["evidence"][0]["supports"] == "SUPPORT"
        assert "most abundant bacteria" not in node["evidence"][0]["snippet"]


def test_resolving_source_access_does_not_complete_the_missing_branch():
    ledger, (doc, _) = records()
    resolved, mechanism, todo = doc["discussions"]
    assert resolved["discussion_id"] == "kg-geobacter-methanosaeta-acetate-route-unresolved"
    assert resolved["status"] == "RESOLVED"
    assert resolved["resolved_date"] == "2026-10-06"
    assert "#1482" in resolved["resolution_note"]
    assert "does not mark the graph complete" in resolved["resolution_note"]
    assert mechanism["kind"] == "KNOWLEDGE_GAP" and mechanism["status"] == "OPEN"
    assert todo["kind"] == "CURATION_TODO" and todo["status"] == "OPEN"
    names = {n["name"] for n in doc["ecological_interactions"]}
    for discussion in doc["discussions"]:
        assert all(a.split("#", 1)[1] in names for a in discussion["attaches_to"])
    assert ledger["records"][0]["status"] == "needs_research"


def test_methanosarcina_preserves_positive_diet_without_total_methane_overclaim():
    _, (_, doc) = records()
    donor, methane, _ = doc["ecological_interactions"]
    assert "oxidizes ethanol to acetate" in donor["description"]
    assert "condition-dependent" in donor["description"]
    assert "granular activated carbon" in donor["description"]
    assert "not an isotope measurement" in methane["description"]
    assert "historical, not timeless uniqueness" in methane["description"]
    assert "proposed for future testing" in methane["description"]
    assert donor["downstream"][0]["target"] == methane["name"]
    assert donor["evidence"][0]["supports"] == "SUPPORT"
    assert methane["participating_taxa"][1]["term"] == doc["taxonomy"][1]["taxon_term"]["term"]


def test_hcp_phenotype_is_not_niche_partitioning_secretion_or_selective_antagonism():
    _, (_, doc) = records()
    donor, _, hcp = doc["ecological_interactions"]
    assert hcp["name"] == "Hcp-Associated Delay of DIET Establishment"
    for field in ["interaction_type", "source_taxon", "biological_processes"]:
        assert field not in hcp
    assert "G. sulfurreducens partner, not M. barkeri" in hcp["description"]
    assert "expose pleiotropy" in hcp["description"]
    assert "protein secretion or killing was not measured" in hcp["description"]
    arrow = hcp["downstream"][0]
    assert arrow["description"].startswith("HYPOTHESIZED NEGATIVE:")
    assert arrow["target"] == donor["name"]
    assert "establishment timing" in arrow["description"]
    assert [e["supports"] for e in hcp["evidence"]] == ["SUPPORT"] * 3 + ["PARTIAL"]
    assert "different medium" in doc["discussions"][0]["rationale"]
    assert "radiotracer results must not be imported" in doc["discussions"][0]["rationale"]


def test_every_existing_node_and_arrow_has_a_decision_but_expansion_is_open():
    ledger, docs = records()
    assert ledger["review_mode"] == "source_based_self_adversarial_review"
    assert ledger["independent_approval"] is False
    assert ledger["repair_issues"] == [1480, 1481]
    assert ledger["open_research_issues"] == [1482, 1483]
    assert sum(len(r["node_decisions"]) for r in ledger["records"]) == 6
    assert sum(len(r["retained_edge_decisions"]) for r in ledger["records"]) == 4
    for row, doc in zip(ledger["records"], docs, strict=True):
        assert row["status"] == "needs_research"
        assert not row["removed_node_decisions"] and not row["removed_edge_decisions"]
        assert len(row["edges_before"]) == len(row["edges_after"]) == 2
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert len(row["history_files"]) == 1 and (ROOT / row["history_files"][0]).is_file()
        assert doc["curation_history"][-1]["llm_assisted"] is True
        assert doc["discussions"][-1]["kind"] == "CURATION_TODO"


def test_sources_and_separate_dry_runs_do_not_claim_paid_reports():
    ledger, _ = records()
    assert ledger["issue_deduplication"]["ignored_hidden_local_search"] is True
    assert ledger["pre_source_baseline"]["selected_record_and_cache_hashes_match_current"]
    for path, digest in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
    assert [d["query_chars"] for d in ledger["edison"]] == [13233, 13853]
    for dryrun in ledger["edison"]:
        assert dryrun["status"] == "dry-run"
        assert dryrun["provider_calls"] == dryrun["provider_credits_spent"] == 0
        assert len(dryrun["meta_sha256"]) == len(dryrun["query_sha256"]) == 64
    assert any("non-graph raw blocks" in s for s in ledger["limitations"])
    assert any("#1091" in s for s in ledger["limitations"])
