"""Active taxonomy uses normalized names; primary evidence remains verbatim."""

import copy
import hashlib
import json
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261009-spring-lineage-batch128.yaml"


def documents():
    ledger = yaml.safe_load(LEDGER.read_text())
    row = ledger["records"][0]
    return ledger, row, yaml.safe_load((ROOT / row["path"]).read_text())


def assert_nomenclature(doc, source):
    raw = next(r["gtdb_lineage"] for r in source["classification_rows"] if r["row"] == 104)
    assert raw.split(";")[1] == "p__Proteobacteria"
    block = doc["taxonomy"][0]["taxon_term"]["gtdb_classification"]
    expected = raw.removesuffix(";s__").split(";")
    expected[1] = "p__Pseudomonadota"
    assert block["gtdb_lineage"].split(";") == expected
    assert block["gtdb_id"] == "GTDB:g__Thiothrix"
    assert "not a release-specific reclassification" in block["curation_note"]
    assert "R08-RS214" in block["curation_note"]
    assert "release unspecified" in block["mapping_source"]
    owners = [doc["taxonomy"][0], *doc["ecological_interactions"][:2]]
    assert all(owner["evidence"][-1]["snippet"] == raw for owner in owners)


def test_normalized_active_lineage_retains_verbatim_primary_evidence():
    ledger, _, doc = documents()
    source = json.loads((ROOT / ledger["source_access"]["manifest"]).read_text())
    assert_nomenclature(doc, source)


def test_immutable_successor_and_unchanged_graph():
    ledger, row, doc = documents()
    parent_path = ROOT / row["supersedes_review"]["review_file"]
    parent = yaml.safe_load(parent_path.read_text())["records"][0]
    assert (
        hashlib.sha256(parent_path.read_bytes()).hexdigest()
        == ledger["preservation"]["previous_ledger_sha256"]
    )
    assert (
        parent["record_sha256"]
        == row["original_sha256"]
        == row["supersedes_review"]["record_sha256"]
    )
    assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
    assert (
        hashlib.sha256(
            json.dumps(doc["ecological_interactions"], sort_keys=True).encode()
        ).hexdigest()
        == ledger["preservation"]["ecological_interactions_sha256"]
    )
    assert row["status"] == parent["status"] == "needs_research"
    assert set(row["allowed_changed_fields"]) == {"taxonomy", "curation_history"}
    assert len(doc["curation_history"]) == 4
    assert row["curation_events_added"] == len(row["history_files"]) == 1
    assert (ROOT / row["history_files"][0]).is_file()
    assert ledger["edison"] == {"required": False, "provider_submissions": 0, "credits_spent": 0}
    assert ledger["independent_approval"] is False


@pytest.mark.parametrize(
    "mutation", ["old_active_name", "rewritten_quote", "rewritten_source", "missing_provenance"]
)
def test_control_mutation_restored_control(mutation):
    ledger, _, doc = documents()
    source = json.loads((ROOT / ledger["source_access"]["manifest"]).read_text())
    assert_nomenclature(doc, source)
    altered, changed_source = copy.deepcopy(doc), copy.deepcopy(source)
    block = altered["taxonomy"][0]["taxon_term"]["gtdb_classification"]
    if mutation == "old_active_name":
        block["gtdb_lineage"] = block["gtdb_lineage"].replace(
            "p__Pseudomonadota", "p__Proteobacteria"
        )
    elif mutation == "rewritten_quote":
        altered["ecological_interactions"][0]["evidence"][-1]["snippet"] = (
            block["gtdb_lineage"] + ";s__"
        )
    elif mutation == "rewritten_source":
        next(r for r in changed_source["classification_rows"] if r["row"] == 104)[
            "gtdb_lineage"
        ] = (block["gtdb_lineage"] + ";s__")
    else:
        block["curation_note"] = "A current genome classification."
    with pytest.raises(AssertionError):
        assert_nomenclature(altered, changed_source)
    assert_nomenclature(doc, source)
