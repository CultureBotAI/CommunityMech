"""Preserve positive maize phenotypes without conflating assays or mechanisms."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-maize-batch67.yaml"
A = "Maize_Benzoxazinoid_Metabolizing_SynComs"
B = "Maize_Drought_Response_SynCom"
C = "Maize_Root_Simplified_Community"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = {Path(r["path"]).stem: r for r in ledger["records"]}
    docs = {name: yaml.safe_load((ROOT / r["path"]).read_text()) for name, r in rows.items()}
    return ledger, rows, docs


def test_mboa_conversion_keeps_perturbations_and_qualitative_limits():
    _, _, docs = records()
    node = docs[A]["ecological_interactions"][0]
    for phrase in ["Removing Microbacterium", "five of six", "n=1", "extracellular AMP"]:
        assert phrase in node["description"]
    assert node["downstream"][0]["description"].startswith("PARTIAL -")
    assert "HMPAA toxicity was not tested" in node["downstream"][0]["description"]
    assert "interaction_type" not in node


def test_mboa_relative_composition_does_not_prove_bulk_growth_mediation():
    _, rows, docs = records()
    _, composition, performance = docs[A]["ecological_interactions"]
    assert "susceptible Chitinophaga LMN1" in composition["description"]
    assert "downstream" not in composition
    for phrase in ["sole supplied carbon", "LMB2-only", "total CFU", "both SynComs"]:
        assert phrase in performance["description"]
    assert len(rows[A]["removed_edge_decisions"]) == 1


def test_drought_root_otus_and_prior_genomes_are_distinct_evidence():
    _, _, docs = records()
    _, colonization, recruitment, transporter, *_ = docs[B]["ecological_interactions"]
    for phrase in ["53 days", "Fourteen of 23", "16 under drought", "not absolute viable"]:
        assert phrase in colonization["description"]
    assert len(colonization["downstream"]) == 1
    assert "632 of 17437" in recruitment["description"]
    assert transporter["evidence"][0]["evidence_source"] == "COMPUTATIONAL"
    assert transporter["evidence"][0]["supports"] == "PARTIAL"
    assert "Prior genomic" in transporter["description"]
    assert "not drought-induced" in transporter["description"]


def test_drought_temperature_recovery_and_yield_keep_genotype_and_assay_limits():
    _, rows, docs = records()
    physiology, recovery, outcome = docs[B]["ecological_interactions"][4:]
    assert "higher leaf temperature" in physiology["description"]
    assert "72-79 days" in physiology["description"]
    assert all(e["description"].startswith("HYPOTHESIZED -") for e in physiology["downstream"])
    for phrase in ["84 days", "DKB had not visibly bent", "rewatering at 80 days"]:
        assert phrase in recovery["description"]
    assert "downstream" not in recovery
    for phrase in ["117 days", "38.7 versus 9.8", "42.7 versus 12.4", "SX showed no significant"]:
        assert phrase in outcome["description"]
    assert len(rows[B]["edges_before"]) == 9 and len(rows[B]["edges_after"]) == 7
    assert all("biological_processes" not in n for n in docs[B]["ecological_interactions"][4:])
    for node in docs[B]["ecological_interactions"][:4] + docs[A]["ecological_interactions"]:
        assert [p["term"]["id"] for p in node["biological_processes"]] == ["GO:0044419"]


def test_root_keystone_is_host_dependent_community_perturbation():
    _, rows, docs = records()
    assembly, keystone, _ = docs[C]["ecological_interactions"]
    assert "15 days" in assembly["description"]
    assert keystone["scope"] == "COMMUNITY_LEVEL"
    assert len(keystone["participating_taxa"]) == 8
    assert not any(k in keystone for k in ["interaction_type", "source_taxon", "target_taxon"])
    for phrase in ["absolute CFUs", "unplanted MS agar", "not direct pairwise competition"]:
        assert phrase in keystone["description"]
    assert rows[C]["edges_before"] == rows[C]["edges_after"] == []


def test_root_biocontrol_is_positive_without_eradication_or_immune_claim():
    _, _, docs = records()
    node = docs[C]["ecological_interactions"][2]
    for phrase in ["reduced seedling-blight", "day 10", "weaker protection", "immune activation"]:
        assert phrase in node["description"]
    assert "interaction_type" not in node and "biological_processes" not in node
    assert len(node["participating_taxa"]) == 9
    assert {t["term"]["id"] for t in node["participating_taxa"]} >= {
        "NCBITaxon:4577",
        "NCBITaxon:117187",
    }


def test_batch67_caches_canonical_terms_and_non_graph_aliases_preserved():
    ledger, _, docs = records()
    for path, digest in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
    for doc in docs.values():
        canonical = {
            t["taxon_term"]["preferred_term"]: t["taxon_term"]["term"] for t in doc["taxonomy"]
        }
        for node in doc["ecological_interactions"]:
            for taxon in node["participating_taxa"]:
                assert canonical[taxon["preferred_term"]] == taxon["term"]
        assert "#1580" in doc["discussions"][-1]["rationale"]
    assert docs[B]["engineering_design"]["evidence"][0]["evidence_source"] == "IN_VITRO"
    assert docs[B]["ecological_interactions"][0]["evidence"][0]["evidence_source"] == "IN_VIVO"
    assert ledger["unresolved_non_graph_issues"] == [1580]
    assert ledger["primary_graph_snippet_count"] == 16


def test_batch67_whole_node_and_arrow_ledger_with_append_only_history():
    ledger, rows, docs = records()
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1577, 1578, 1579]
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert sum(len(r["node_decisions"]) for r in rows.values()) == 13
    assert sum(len(r["retained_edge_decisions"]) for r in rows.values()) == 8
    assert sum(len(r["removed_edge_decisions"]) for r in rows.values()) == 3
    for name, row in rows.items():
        doc = docs[name]
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert doc["curation_history"][-1]["llm_assisted"] is True
        assert len(row["history_files"]) == 1 and row["status"] == "reviewed"
        names = {n["name"] for n in doc["ecological_interactions"]}
        assert {d["node"] for d in row["node_decisions"]} == names
        before = {(e["source"], e["target"]) for e in row["edges_before"]}
        kept = {(e["source"], e["target"]) for e in row["retained_edge_decisions"]}
        removed = {(e["source"], e["target"]) for e in row["removed_edge_decisions"]}
        assert not kept & removed and kept | removed == before
        assert {a.split("#", 1)[1] for a in doc["discussions"][-1]["attaches_to"]} == names
