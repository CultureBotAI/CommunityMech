"""Pin assay boundaries, source contradictions and incomplete graph expansion."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-three-records-batch42.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    return ledger, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in ledger["records"]]


def test_fucoidan_panel_is_not_a_single_mutualistic_mineralizing_community():
    _, docs = records()
    complement, landscape = docs[0]["ecological_interactions"]
    assert complement["evidence"][0]["evidence_source"] == "IN_VITRO"
    assert "not measured CO2 mineralization" in complement["description"]
    assert "without requiring contact or small-molecule cross-feeding" in complement["description"]
    for boundary in [
        "five-member F40/F56/V69/F94/V4 subset",
        "distinct from reciprocal fitness benefit",
        "total inoculum varied with richness",
        "mutualistic V69/G88 pair lies outside this panel",
    ]:
        assert boundary in landscape["description"]
    for node in [complement, landscape]:
        assert "interaction_type" not in node and "downstream" not in node
        assert len(node["participating_taxa"]) == 7
        assert "NCBITaxon:3063958" not in {p["term"]["id"] for p in node["participating_taxa"]}


def test_fucoidan_v4_citation_artifact_is_resolved_without_rewriting_cache():
    ledger, docs = records()
    alias = next(d for d in docs[0]["discussions"] if d["discussion_id"] == "v4_lentimonas_alias")
    assert alias["status"] == "RESOLVED"
    assert "superscript link to reference 3" in alias["rationale"]
    source = ledger["records"][0]["source_review"]["PMID:42649294"]
    assert "V4<sup>" in source["receipt"]["v4_citation_dom"]
    assert 'aria-label="Reference 3"' in source["receipt"]["v4_citation_dom"]
    assert "strain V43" in (ROOT / source["cache"]).read_text()
    assert "original spreadsheet" in source["scope"]


def test_genia_predictions_do_not_become_measured_cross_feeding():
    _, docs = records()
    potential, removal, dynamics = docs[1]["ecological_interactions"]
    assert potential["description"].startswith("HYPOTHESIZED:")
    assert potential["evidence"][0]["evidence_source"] == "COMPUTATIONAL"
    assert potential["evidence"][0]["supports"] == "PARTIAL"
    assert "downstream" not in potential and "biological_processes" not in potential
    for node in [potential, removal, dynamics]:
        assert "interaction_type" not in node
        assert len(node["participating_taxa"]) == 9
    assert "93.1%" in removal["description"] and "87.1%" in removal["description"]
    assert "distinct seven-day mixed-pollutant experiment" in removal["description"]
    assert "not independent certification" in removal["description"]


def test_genia_retained_arrow_is_only_the_bounded_management_intervention():
    _, docs = records()
    _, removal, dynamics = docs[1]["ecological_interactions"]
    (arrow,) = dynamics["downstream"]
    assert arrow["target"] == removal["name"]
    assert arrow["description"].startswith("PARTIAL:")
    assert "Dilution/remixing changes handling as well as ratios" in arrow["description"]
    assert "lignin difference was not significant" in arrow["description"]
    assert "relative DNA composition" in dynamics["description"]
    assert dynamics["evidence"][-1]["supports"] == "PARTIAL"


def test_genia_source_arithmetic_is_not_certified_treatment_mass_balance():
    ledger, docs = records()
    values = ledger["arithmetic_checks"]
    assert abs(values["pfos_only_fluorine_mg_l"] - 11.9833) < 0.0001
    assert 10.33 < values["atrazine_nitrogen_mg_l"] < 10.34
    assert "true denominators remain unresolved" in values["limitations"]
    rationale = docs[1]["discussions"][-1]["rationale"]
    assert "PFOA/PFOS mixture" in rationale
    assert "rather than a blanket impossibility claim" in rationale
    assert ledger["open_nongraph_followups"] == [1468]


def test_transwell_umbrella_removed_without_combining_distinct_assays():
    ledger, docs = records()
    reporter, timeseries = docs[2]["ecological_interactions"]
    assert "Replated Cv026" in reporter["description"]
    assert "separate three-member" in reporter["description"]
    assert "977 features are not 977 identified metabolites" in timeseries["description"]
    assert "identified separately by polar HILIC-MS/MS" in timeseries["description"]
    assert "does not selectively establish the cause" in timeseries["description"]
    assert [t["taxon_term"]["term"]["id"] for t in docs[2]["taxonomy"]] == ["NCBITaxon:2"]
    for node in [reporter, timeseries]:
        assert not any(
            k in node for k in ["downstream", "source_taxon", "target_taxon", "participating_taxa"]
        )
    (removed,) = ledger["records"][2]["removed_node_decisions"]
    assert removed["node"] == "Exometabolite-Mediated Interaction"
    assert "SC11,368" in docs[2]["discussions"][-1]["rationale"]


def test_batch42_pending_expansions_and_edison_dryruns_remain_explicit():
    ledger, _ = records()
    assert [r["status"] for r in ledger["records"]] == [
        "needs_research",
        "reviewed",
        "needs_research",
    ]
    assert ledger["issues"] == [1466]
    assert ledger["open_graph_research"] == [1465, 1467]
    assert len(ledger["edison"]) == 2
    assert [j["dryrun_meta"]["query_chars"] for j in ledger["edison"]] == [15343, 8368]
    for job in ledger["edison"]:
        meta = job["dryrun_meta"]
        assert meta["status"] == "dry-run"
        assert hashlib.sha256(meta["query"].encode()).hexdigest() == meta["query_sha256"]
        assert job["provider_job_submitted"] is job["provider_credits_spent"] is False


def test_batch42_dispositions_history_participants_and_source_receipts():
    ledger, docs = records()
    assert ledger["independent_approval"] is False
    assert ledger["base_commit"] == ledger["baseline_commit"]
    assert ledger["issue_deduplication"]["ignored_hidden_local_search"] is True
    assert sum(len(r["node_decisions"]) for r in ledger["records"]) == 7
    assert sum(len(r["removed_node_decisions"]) for r in ledger["records"]) == 1
    assert sum(len(r["retained_edge_decisions"]) for r in ledger["records"]) == 1
    assert sum(len(r["removed_edge_decisions"]) for r in ledger["records"]) == 1
    assert sum(len(r["renamed_nodes"]) for r in ledger["records"]) == 3
    for path, expected in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == expected
    for row, doc in zip(ledger["records"], docs, strict=True):
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert len(row["history_files"]) == 1 and (ROOT / row["history_files"][0]).is_file()
        assert doc["curation_history"][-1]["llm_assisted"] is True
        canonical = {t["taxon_term"]["term"]["id"]: t["taxon_term"] for t in doc["taxonomy"]}
        names = {n["name"] for n in doc["ecological_interactions"]}
        for node in doc["ecological_interactions"]:
            for term in node.get("participating_taxa", []):
                expected = canonical[term["term"]["id"]]
                assert term["term"] == expected["term"]
                assert term["preferred_term"] == expected["preferred_term"]
            assert all(
                e["target"] in names and e["target"] != node["name"]
                for e in node.get("downstream", [])
            )
        assert all(
            a.split("#", 1)[1] in names for a in doc["discussions"][-1].get("attaches_to", [])
        )


def test_batch42_reference_counter_correction_and_real_failure_are_preserved():
    import json

    receipt = json.loads(
        (
            ROOT
            / "reports/causal_graph_review/reference-validator-correction-20261006-batch42.json"
        ).read_text()
    )
    assert receipt["issue"] == 1469
    assert receipt["cli"]["counter_statement"] == "Total checks: {len(all_results)}"
    assert "issues, not number of executed checks" in receipt["cli"]["interpretation"]
    assert receipt["canary_exit"] == 0 and "5 passed" in receipt["canary_output"]
    assert receipt["baseline_reference_exit"] == 1
    assert len(receipt["missing_snippets"]) == 14
    assert receipt["all_14_findings_match_supplement_sidecar"] is True
    assert receipt["original_taxonomy_unchanged"] is True
    assert receipt["baseline_snippet_audit"]["unchanged_counts"]["MISMATCH"] == 15
    assert receipt["baseline_snippet_audit"]["unchanged_counts"]["MATCH"] == 35
    assert "14" in receipt["initial_failed_attempt"]["results"][-1]["output_tail"]
    for path, digest in receipt["historical_candidate_files"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
    ledger, _ = records()
    assert "reports issue counts as Total checks" in " ".join(ledger["limitations"])
