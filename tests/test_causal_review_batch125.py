"""Diatom identity repair must not manufacture species, partners, or mechanisms."""

import copy
import hashlib
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
STEM = "Cable_Bacteria_Photosynthetic_Biofilm_Sediment"
PATH = ROOT / "kb/communities" / f"{STEM}.yaml"
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261008-cable-biofilm-batch125.yaml"


def record():
    return yaml.safe_load(PATH.read_text())


def assert_roster(doc):
    cable, diatoms = doc["taxonomy"]
    assert cable["taxon_term"]["term"]["id"] == "NCBITaxon:213121"
    assert cable["functional_role"] == ["CROSS_FEEDER"]
    assert diatoms["taxon_term"]["term"] == {
        "id": "NCBITaxon:2836",
        "label": "Bacillariophyta",
    }
    assert diatoms["taxon_term"]["gtdb_grounding_status"] == "NO_GTDB_EQUIVALENT"
    assert "does not identify a species" in diatoms["taxon_term"]["notes"]
    assert "defined two-member culture" in diatoms["taxon_term"]["notes"]
    assert diatoms["evidence"][0]["snippet"] == "dominated by diatoms"


def assert_chemistry(doc):
    sulfide = doc["related_ingredients"][0]
    assert sulfide["chebi_term"] == {"id": "CHEBI:16136", "label": "hydrogen sulfide"}
    assert "H2S and HS-" in sulfide["relevance"]
    assert "does not identify all dissolved sulfide as H2S" in sulfide["relevance"]
    assert "no exclusive molecular uptake mechanism" in sulfide["evidence"][0]["explanation"]


def assert_graph(doc):
    oxygen, conduction, response = doc["ecological_interactions"]
    assert oxygen["interaction_type"] == "CROSS_FEEDING"
    assert "reciprocal benefit to the phototrophs is not established" in oxygen["description"]
    assert "not species-resolved partners" in oxygen["description"]
    assert "proposed mechanisms" in conduction["description"]
    assert "not independent sediment-core replicates" in response["description"]
    assert "nonsignificant current-density contrasts" in response["description"]
    assert "inconsistent reported sulfide-depth significance" in response["description"]
    assert all(n["scope"] == "COMMUNITY_LEVEL" for n in (oxygen, conduction, response))
    assert all(not n.get("participating_taxa") for n in (oxygen, conduction, response))
    assert all("interaction_type" not in n for n in (conduction, response))
    assert oxygen["downstream"][0]["target"] == conduction["name"]
    assert conduction["downstream"][0]["target"] == response["name"]
    assert not response.get("downstream")


def test_identity_chemistry_and_retained_graph():
    doc = record()
    assert_roster(doc)
    assert_chemistry(doc)
    assert_graph(doc)
    assert "NCBITaxon:3041" not in str(doc)
    assert "CHEBI:15138" not in str(doc)
    assert doc["discussions"][0]["status"] == "OPEN"
    assert "remain unresolved" in doc["discussions"][0]["rationale"]


def test_review_supersession_preserves_historical_gap_and_topology():
    ledger = yaml.safe_load(LEDGER.read_text())
    row = ledger["records"][0]
    parent_path = ROOT / row["supersedes_review"]["review_file"]
    parent = next(
        r for r in yaml.safe_load(parent_path.read_text())["records"] if r["id"] == row["id"]
    )
    assert parent["status"] == "needs_research"
    assert row["status"] == "reviewed"
    assert (
        row["original_sha256"]
        == row["supersedes_review"]["record_sha256"]
        == parent["record_sha256"]
    )
    assert row["record_sha256"] == hashlib.sha256(PATH.read_bytes()).hexdigest()
    doc = record()
    edges = [
        dict(source=n["name"], **e)
        for n in doc["ecological_interactions"]
        for e in n.get("downstream", [])
    ]
    assert edges == row["edges_before"] == row["edges_after"] == parent["edges_after"]
    assert len(edges) == 2 and len(row["node_decisions"]) == 3
    assert ledger["edison"] == {"required": False, "provider_submissions": 0, "credits_spent": 0}
    assert not ledger["independent_approval"]
    assert len(row["history_files"]) == 1
    assert (ROOT / row["history_files"][0]).is_file()
    assert len(doc["curation_history"]) == 2
    assert doc["curation_history"][-1]["llm_assisted"]


def test_short_attributed_cache_appendix_and_source_scope():
    ledger = yaml.safe_load(LEDGER.read_text())
    change = ledger["cache_changes"][0]
    cache = (ROOT / change["path"]).read_text()
    assert hashlib.sha256(cache.encode()).hexdigest() == change["after_sha256"]
    appendix = cache.split("## Primary-source excerpts", 1)[1]
    assert "PMC4292484" in appendix and "American Society for Microbiology" in appendix
    assert change["appended_excerpt_words"] == 8
    assert len(appendix) < 500
    assert len(ledger["snippet_checks"]) == 11
    assert all(
        c["literal_primary_match"] and c["literal_cache_match"] for c in ledger["snippet_checks"]
    )
    assert "Figure pixels, supplement, raw data" in ledger["limitations"][0]


@pytest.mark.parametrize(
    "mutation",
    ["green_algae", "syntrophy", "sulfide_dianion", "unqualified_uptake", "mutual_benefit"],
)
def test_scientific_regression_probes(mutation):
    doc = record()
    for check in (assert_roster, assert_chemistry, assert_graph):
        check(doc)
    altered = copy.deepcopy(doc)
    if mutation == "green_algae":
        altered["taxonomy"][1]["taxon_term"]["term"] = {
            "id": "NCBITaxon:3041",
            "label": "Chlorophyta",
        }
        check = assert_roster
    elif mutation == "syntrophy":
        altered["taxonomy"][0]["functional_role"].append("SYNTROPHIC_PARTNER")
        check = assert_roster
    elif mutation == "sulfide_dianion":
        altered["related_ingredients"][0]["chebi_term"] = {
            "id": "CHEBI:15138",
            "label": "sulfide(2-)",
        }
        check = assert_chemistry
    elif mutation == "unqualified_uptake":
        altered["related_ingredients"][0]["evidence"][0][
            "explanation"
        ] = "Establishes exclusive molecular uptake."
        check = assert_chemistry
    else:
        altered["ecological_interactions"][0]["description"] = "Reciprocal benefit is established."
        check = assert_graph
    assert altered != doc
    with pytest.raises(AssertionError):
        check(altered)
    check(doc)
