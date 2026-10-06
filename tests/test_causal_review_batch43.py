"""Pin strain-specific perturbations, community observations and exact census credit."""

import copy
import hashlib
import runpy
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-variovorax-batch43.yaml"


def record():
    ledger = yaml.safe_load(LEDGER.read_text())
    (row,) = ledger["records"]
    return ledger, row, yaml.safe_load((ROOT / row["path"]).read_text())


def test_compartment_dna_enrichment_is_not_absolute_colonization_or_competition():
    _, _, doc = record()
    enrichment, competition, _ = doc["ecological_interactions"]
    assert "relative DNA compartment association" in enrichment["description"]
    assert "normalized read abundance" in enrichment["description"]
    assert "absolute read abundance" not in enrichment["description"]
    assert "not absolute colonization efficiency" in enrichment["description"]
    assert "putative species" in enrichment["description"]
    assert competition["description"].startswith("HYPOTHESIZED:")
    assert "not directly measured depletion" in competition["description"]
    assert all(e["supports"] == "PARTIAL" for e in competition["evidence"])
    for node in [enrichment, competition]:
        assert len(node["participating_taxa"]) == 28
        assert len({p["preferred_term"] for p in node["participating_taxa"]}) == 28
        assert len({p["term"]["id"] for p in node["participating_taxa"]}) == 1


def test_fucose_mutant_result_is_canonical_cf313_only():
    _, _, doc = record()
    node = doc["ecological_interactions"][2]
    assert node["scope"] == "PAIRWISE"
    canonical = doc["taxonomy"][8]["taxon_term"]
    assert node["source_taxon"] == {
        "preferred_term": canonical["preferred_term"],
        "term": canonical["term"],
    }
    assert canonical["preferred_term"] == "Variovorax sp. CF313"
    assert "target_taxon" not in node and "participating_taxa" not in node
    for boundary in [
        "PMI12_01353",
        "P=0.0022",
        "not facilitation of other strains",
        "Gene presence alone is not sufficient",
        "host fucose was not quantified",
        "full-panel mutant replacement are not established",
    ]:
        assert boundary in node["description"]
    assert node["metabolites"][0]["term"] == doc["related_ingredients"][0]["chebi_term"]
    assert [e["evidence_source"] for e in node["evidence"]] == ["IN_VITRO", "IN_VIVO", "IN_VITRO"]


def test_all_original_nodes_and_arrows_have_decisions_without_new_structure():
    ledger, row, doc = record()
    assert row["status"] == "reviewed" and ledger["independent_approval"] is False
    assert len(row["node_decisions"]) == len(row["renamed_nodes"]) == 3
    assert len(row["removed_edge_decisions"]) == len(row["edges_before"]) == 2
    assert row["edges_after"] == row["retained_edge_decisions"] == []
    for node in doc["ecological_interactions"]:
        assert not any(
            k in node for k in ["downstream", "interaction_type", "biological_processes"]
        )
    assert doc["discussions"][-1]["status"] == "OPEN"
    assert "no figure images" in doc["discussions"][-1]["rationale"]


def test_hashes_history_and_source_limitations_are_retained():
    ledger, row, doc = record()
    assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
    assert len(row["history_files"]) == 1 and (ROOT / row["history_files"][0]).is_file()
    assert doc["curation_history"][-1]["llm_assisted"] is True
    assert ledger["issue_deduplication"]["ignored_hidden_local_search"] is True
    assert ledger["base_commit"] == ledger["baseline_commit"]
    for path, digest in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
    source = row["source_review"]["PMID:41543249"]
    assert "stale abstract_only" in source["scope"]
    assert "no figure images" in source["scope"]


def test_survey_uses_exact_names_not_the_shared_genus_id(monkeypatch):
    _, _, doc = record()
    module = runpy.run_path(str(ROOT / "tests/test_community_level_connectivity_credit.py"))
    survey = module["_survey"]
    monkeypatch.setitem(
        survey.__globals__,
        "record_files",
        lambda: [ROOT / "kb/communities/GLBRC_Populus_Variovorax_SynCom28.yaml"],
    )
    result = survey()
    assert result == {
        "records": 1,
        "with_community_level": 1,
        "mixed": 1,
        "community_level_only": 0,
        "taxa": 28,
        "credited_solely_by_the_rule": 27,
    }
    ranker = module["ranker"]
    intrinsic = copy.deepcopy(doc["ecological_interactions"][2])
    intrinsic["source_taxon"] = {"term": {"id": "NCBITaxon:34072"}}
    assert ranker._connected_taxa([intrinsic], doc["taxonomy"]) == set()
