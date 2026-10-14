"""Parent grounding must not silently reassert an unsupported genus identity."""

import hashlib
import json
import subprocess
from copy import deepcopy
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
BASE = "8df89370be840a4b58a9d8a7407c66c7471a5085"
RECORD = "kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml"
LEDGER = "reports/causal_graph_review/decisions/20261014-spring-parent-rank-batch129.yaml"
SOURCE = "reports/causal_graph_review/sources/20261014-spring-parent-rank.json"


def baseline_bytes():
    return subprocess.check_output(["git", "show", f"{BASE}:{RECORD}"], cwd=ROOT)


def current():
    return yaml.safe_load((ROOT / RECORD).read_text())


def assert_parent_boundary(doc):
    taxon = doc["taxonomy"][1]["taxon_term"]
    participant = doc["ecological_interactions"][0]["participating_taxa"][1]
    assert taxon["term"] == {"id": "NCBITaxon:1236", "label": "Gammaproteobacteria"}
    assert participant == {k: taxon[k] for k in ("preferred_term", "term")}
    assert "unresolved genus" in taxon["preferred_term"]
    assert "parent-rank anchor, not an exact assignment" in taxon["notes"]
    assert "no claim extends to all Gammaproteobacteria" in taxon["notes"]
    block = taxon["gtdb_classification"]
    assert block["gtdb_id"] == "GTDB:c__Gammaproteobacteria"
    assert block["gtdb_taxon"] == "Gammaproteobacteria"
    assert block["gtdb_lineage"] == "d__Bacteria;p__Pseudomonadota;c__Gammaproteobacteria"
    assert block["ncbi_source_id"] == "NCBITaxon:1236"
    assert block["curated"] is True
    assert not {"majority_fraction", "support_genomes", "total_genomes"} & set(block)
    assert "study GTDB release unspecified" in block["mapping_source"]
    assert "leaves genus blank" in doc["ecological_interactions"][0]["description"]
    assert "needs_research" in doc["discussions"][0]["rationale"]
    assert doc["discussions"][0]["status"] == "OPEN"


def test_repaired_record_and_original_failure():
    assert_parent_boundary(current())
    with pytest.raises(AssertionError):
        assert_parent_boundary(yaml.safe_load(baseline_bytes()))
    assert_parent_boundary(current())


@pytest.mark.parametrize(
    "mutation",
    ["genus", "stale_graph", "gtdb_genus", "vote", "exact_identity", "all_class", "closed"],
)
def test_control_mutation_restoration(mutation):
    control = current()
    assert_parent_boundary(control)
    changed = deepcopy(control)
    taxon = changed["taxonomy"][1]["taxon_term"]
    if mutation == "genus":
        taxon["term"] = {"id": "NCBITaxon:1021", "label": "Beggiatoa"}
    elif mutation == "stale_graph":
        changed["ecological_interactions"][0]["participating_taxa"][1]["term"][
            "id"
        ] = "NCBITaxon:1021"
    elif mutation == "gtdb_genus":
        taxon["gtdb_classification"]["gtdb_id"] = "GTDB:g__Beggiatoa"
    elif mutation == "vote":
        taxon["gtdb_classification"]["support_genomes"] = 9
    elif mutation == "exact_identity":
        taxon["notes"] = "An exact genus assignment."
    elif mutation == "all_class":
        taxon["notes"] = taxon["notes"].replace(
            "no claim extends to all Gammaproteobacteria", "the claim extends to every member"
        )
    else:
        changed["discussions"][0]["status"] = "RESOLVED"
    assert changed != control
    with pytest.raises(AssertionError):
        assert_parent_boundary(changed)
    assert_parent_boundary(control)


def test_primary_class_evidence_and_source_rank_conflict():
    source = json.loads((ROOT / SOURCE).read_text())
    assert source["workbook_matches_prior_sha256"] is True
    rows = {row["row"]: row for row in source["classification_rows"]}
    assert all(";c__Gammaproteobacteria;" in rows[i]["gtdb_lineage"] for i in (5, 12, 68, 69))
    assert all(rows[i]["gtdb_lineage"].endswith(";g__;s__") for i in (5, 12, 68, 69))
    assert rows[5]["gtdb_lineage"].endswith(";f__Beggiatoaceae;g__;s__")
    assert rows[68]["gtdb_lineage"].endswith(";f__;g__;s__")
    taxa = {t["id"]: t for t in source["ncbi_taxa"]}
    assert (taxa["1236"]["name"], taxa["1236"]["rank"]) == ("Gammaproteobacteria", "class")
    assert taxa["1021"]["lineage"].endswith("Thiotrichales; Thiotrichaceae")
    doc = current()
    added = doc["taxonomy"][1]["evidence"][-1]
    assert added == doc["ecological_interactions"][0]["evidence"][1]
    assert added["evidence_source"] == "COMPUTATIONAL"
    assert "parent-rank anchor only" in added["explanation"]
    primary = " ".join(p for item in source["inspected_passages"] for p in item["paragraphs"])
    assert added["snippet"] in primary
    cache = " ".join((ROOT / "references_cache/PMID_38273328.md").read_text().split())
    assert added["snippet"] in cache


def test_successor_is_hash_bound_and_changes_only_reviewed_fields():
    old_bytes = baseline_bytes()
    old, doc = yaml.safe_load(old_bytes), current()
    ledger = yaml.safe_load((ROOT / LEDGER).read_text())
    row = ledger["records"][0]
    prior = yaml.safe_load((ROOT / row["supersedes_review"]["review_file"]).read_text())["records"][
        0
    ]
    assert row["original_sha256"] == hashlib.sha256(old_bytes).hexdigest() == prior["record_sha256"]
    assert row["supersedes_review"]["record_sha256"] == prior["record_sha256"]
    assert row["record_sha256"] == hashlib.sha256((ROOT / RECORD).read_bytes()).hexdigest()
    assert {k for k in doc if old[k] != doc[k]} == set(row["allowed_changed_fields"])
    assert doc["ecological_interactions"][1:] == old["ecological_interactions"][1:]
    assert [n["name"] for n in doc["ecological_interactions"]] == [
        n["name"] for n in old["ecological_interactions"]
    ]
    assert all(not n.get("downstream") for n in doc["ecological_interactions"])
    assert row["status"] == "needs_research" and row["issues"] == [1841]
    assert doc["curation_history"][:-1] == old["curation_history"]
    assert doc["curation_history"][-1]["llm_assisted"] is True
    assert len(row["history_files"]) == 2
    assert ledger["edison"]["provider_submissions"] == 0
    assert not ledger["independent_approval"]
