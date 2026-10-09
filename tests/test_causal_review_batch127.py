"""Supplementary genus assignments cannot certify species or imaged-cell identity."""

import copy
import hashlib
import json
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / "kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml"
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261008-spring-identity-batch127.yaml"


def assert_identity(doc):
    taxon = doc["taxonomy"][0]["taxon_term"]
    assert taxon["term"] == {"id": "NCBITaxon:1030", "label": "Thiothrix"}
    block = taxon["gtdb_classification"]
    assert block["gtdb_id"] == "GTDB:g__Thiothrix"
    assert block["ncbi_source_id"] == "NCBITaxon:1030"
    assert block["curated"] and "row104" in block["curation_note"]
    assert "release unspecified" in block["mapping_source"]
    assert not any(k in block for k in ("total_genomes", "support_genomes", "majority_fraction"))
    a, pair, _ = doc["ecological_interactions"]
    assert a["participating_taxa"][0]["term"] == pair["target_taxon"]["term"] == taxon["term"]
    for owner in (doc["taxonomy"][0], a, pair):
        evidence = owner["evidence"][-1]
        assert evidence["evidence_source"] == "COMPUTATIONAL"
        assert evidence["snippet"].endswith(";g__Thiothrix;s__")
        assert evidence["computational_provenance"]["tools"][0]["tool_name"] == "iQ-TREE"


def assert_limits(doc):
    a, pair, prediction = doc["ecological_interactions"]
    assert "Thiothrix nivea is not established" in a["description"]
    assert "Beggiatoa-related canonical participant remains unresolved" in a["description"]
    assert "do not verify a CPR-Thiothrix pair" in pair["description"]
    assert "FISH" in pair["description"] and pair["description"].startswith("HYPOTHESIZED/PARTIAL:")
    assert "not demonstrated enzyme activity" in prediction["description"]
    assert all(
        not n.get("downstream") and "interaction_type" not in n for n in (a, pair, prediction)
    )
    discussion = doc["discussions"][0]
    assert discussion["status"] == "OPEN" and "#1841" in discussion["rationale"]
    assert "needs_research" in discussion["rationale"]


def test_genus_repair_preserves_unresolved_boundaries():
    doc = yaml.safe_load(RECORD.read_text())
    assert_identity(doc)
    assert_limits(doc)


def test_primary_rows_reproduce_genus_not_species_and_conflicting_genus_gap():
    ledger = yaml.safe_load(LEDGER.read_text())
    path = ROOT / ledger["source_access"]["manifest"]
    assert hashlib.sha256(path.read_bytes()).hexdigest() == ledger["source_access"]["sha256"]
    source = json.loads(path.read_text())
    assert source["identical_downloads"]
    assert source["downloads"][0]["sha256"] == source["downloads"][1]["sha256"]
    rows = {r["row"]: r for r in source["classification_rows"]}
    assert rows[104]["genome"] == "ALUMROCK_MS4_Thiothrix_nivea-related_50_537_curated"
    assert rows[104]["gtdb_lineage"].endswith(";g__Thiothrix;s__")
    assert rows[104]["column_D"] == "N/A"
    assert rows[5]["gtdb_lineage"].endswith(";f__Beggiatoaceae;g__;s__")
    assert not source["classification_sheet_has_header"]


def test_hash_linked_history_cache_and_no_extension():
    ledger = yaml.safe_load(LEDGER.read_text())
    row = ledger["records"][0]
    parent = next(
        r
        for r in yaml.safe_load((ROOT / row["supersedes_review"]["review_file"]).read_text())[
            "records"
        ]
        if r["id"] == row["id"]
    )
    assert (
        row["original_sha256"]
        == parent["record_sha256"]
        == row["supersedes_review"]["record_sha256"]
    )
    successor = yaml.safe_load(
        (
            ROOT / "reports/causal_graph_review/decisions/20261009-spring-lineage-batch128.yaml"
        ).read_text()
    )["records"][0]
    assert successor["supersedes_review"] == {
        "review_file": str(LEDGER.relative_to(ROOT)),
        "record_sha256": row["record_sha256"],
    }
    assert successor["original_sha256"] == row["record_sha256"]
    assert successor["record_sha256"] == hashlib.sha256(RECORD.read_bytes()).hexdigest()
    assert row["status"] == parent["status"] == "needs_research"
    assert row["edges_before"] == row["edges_after"] == []
    assert len(row["node_decisions"]) == 3 and len(row["history_files"]) == 1
    assert (ROOT / row["history_files"][0]).is_file()
    assert len(yaml.safe_load(RECORD.read_text())["curation_history"]) == 4
    assert ledger["edison"] == {"required": False, "provider_submissions": 0, "credits_spent": 0}
    assert ledger["independent_approval"] is False
    change = ledger["cache_changes"][0]
    assert (
        hashlib.sha256((ROOT / change["path"]).read_bytes()).hexdigest() == change["after_sha256"]
    )
    assert change["original_prefix_preserved"]


@pytest.mark.parametrize(
    "mutation", ["species", "stale_link", "vote", "confirmed_pair", "closed_gap"]
)
def test_control_mutation_restored_control(mutation):
    doc = yaml.safe_load(RECORD.read_text())
    assert_identity(doc)
    assert_limits(doc)
    altered = copy.deepcopy(doc)
    check = assert_identity
    if mutation == "species":
        altered["taxonomy"][0]["taxon_term"]["term"]["id"] = "NCBITaxon:1031"
    elif mutation == "stale_link":
        altered["ecological_interactions"][1]["target_taxon"]["term"]["id"] = "NCBITaxon:1031"
    elif mutation == "vote":
        altered["taxonomy"][0]["taxon_term"]["gtdb_classification"]["total_genomes"] = 2
    elif mutation == "confirmed_pair":
        altered["ecological_interactions"][1]["description"] = "Confirmed CPR-Thiothrix exchange."
        check = assert_limits
    else:
        altered["discussions"][0]["status"] = "RESOLVED"
        check = assert_limits
    with pytest.raises(AssertionError):
        check(altered)
    check(doc)
