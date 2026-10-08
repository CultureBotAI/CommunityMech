"""Primary-supported LC1 identity does not certify unaudited methods or mediation."""

import copy
import hashlib
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "kb/communities/Synechococcus_Halomonas_Light_Driven_PHB_Coculture.yaml"
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261008-halomonas-identity-batch126.yaml"
QUOTE = "Halomonas boliviensis LC1 (DSM 15516)"


def assert_identity(doc):
    carbon, product, _ = doc["ecological_interactions"]
    assert carbon["target_taxon"]["term"] == {
        "id": "NCBITaxon:1072583",
        "label": "Vreelandella boliviensis LC1",
    }
    for node in (carbon, product):
        assert "Introduction" in node["description"]
        assert any(e["snippet"] == QUOTE and e["supports"] == "SUPPORT" for e in node["evidence"])
    assert "strain-specific attribution" in carbon["description"]
    assert "LC1 identity is supported" in product["description"]


def assert_limits(doc):
    carbon, product, partition = doc["ecological_interactions"]
    assert "Complete medium inputs remain unverified" in carbon["description"]
    assert "exact assay details await full Methods" in product["description"]
    assert "31%" in product["description"] and "five months" in product["description"]
    assert "interaction_type" not in partition
    assert partition["downstream"][0]["description"].startswith("HYPOTHESIZED/PARTIAL:")
    discussion = doc["discussions"][0]
    assert discussion["status"] == "OPEN" and "#1860" in discussion["rationale"]
    assert "not for the resolved LC1 identity" in discussion["rationale"]


def test_identity_and_remaining_limits():
    doc = yaml.safe_load(PATH.read_text())
    assert_identity(doc)
    assert_limits(doc)


def test_supersession_preserves_topology_history_and_research_status():
    ledger = yaml.safe_load(LEDGER.read_text())
    row = ledger["records"][0]
    parent = next(
        r
        for r in yaml.safe_load((ROOT / row["supersedes_review"]["review_file"]).read_text())[
            "records"
        ]
        if r["id"] == row["id"]
    )
    assert row["status"] == parent["status"] == "needs_research"
    assert (
        row["original_sha256"]
        == parent["record_sha256"]
        == row["supersedes_review"]["record_sha256"]
    )
    assert row["record_sha256"] == hashlib.sha256(PATH.read_bytes()).hexdigest()
    doc = yaml.safe_load(PATH.read_text())
    edges = [
        dict(source=n["name"], **e)
        for n in doc["ecological_interactions"]
        for e in n.get("downstream", [])
    ]
    assert edges == row["edges_before"] == row["edges_after"] == parent["edges_after"]
    assert len(doc["ecological_interactions"]) == 3 and len(edges) == 2
    assert len(doc["curation_history"]) == 2 and doc["curation_history"][-1]["llm_assisted"]
    assert len(row["history_files"]) == 1 and (ROOT / row["history_files"][0]).is_file()
    assert ledger["edison"] == {"required": False, "provider_submissions": 0, "credits_spent": 0}
    assert not ledger["independent_approval"]


def test_cache_is_short_attributed_and_not_mislabeled_as_full_text():
    ledger = yaml.safe_load(LEDGER.read_text())
    change = ledger["cache_changes"][0]
    cache = (ROOT / change["path"]).read_text()
    assert hashlib.sha256(cache.encode()).hexdigest() == change["after_sha256"]
    assert change["path"].endswith(".md") and change["appended_excerpt_words"] == 5
    appendix = cache.split("## Primary-source identity excerpt", 1)[1]
    assert QUOTE in appendix and "publisher-indexed" in appendix
    assert "not a full-text import" in appendix and "All rights reserved" in appendix
    assert len(appendix) < 650
    assert "not a successful direct full-text download" in ledger["source_access"]["retrieval_mode"]


@pytest.mark.parametrize("mutation", ["identity", "medium", "mediation", "gap_closed"])
def test_control_mutation_restored_control(mutation):
    doc = yaml.safe_load(PATH.read_text())
    assert_identity(doc)
    assert_limits(doc)
    altered = copy.deepcopy(doc)
    check = assert_limits
    if mutation == "identity":
        altered["ecological_interactions"][0]["evidence"] = altered["ecological_interactions"][0][
            "evidence"
        ][:-1]
        check = assert_identity
    elif mutation == "medium":
        altered["ecological_interactions"][0][
            "description"
        ] = "Complete medium inputs are verified."
    elif mutation == "mediation":
        altered["ecological_interactions"][2]["downstream"][0][
            "description"
        ] = "Proven exclusive encapsulation mediation."
    else:
        altered["discussions"][0]["status"] = "RESOLVED"
    assert altered != doc
    with pytest.raises(AssertionError):
        check(altered)
    check(doc)
