"""Protect assay attribution without converting hypotheses into new causal edges."""

import hashlib
import subprocess
from copy import deepcopy
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
TARGET = "kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml"
BASE = "a6feb9194b199d255148557d6c5b3c3e129631f0"
LEDGER = "reports/causal_graph_review/decisions/20261015-parachlorella-assays.yaml"


def document():
    return yaml.safe_load((ROOT / TARGET).read_text())


def assert_assay_scope(doc):
    gas, growth, eps, product = doc["ecological_interactions"]
    assert product["name"] == "Coculture Algal Cell Increase and Relative Lipid Signal"
    for phrase in (
        "P. kessleri cell concentration",
        "day 12",
        "4.8-fold",
        "2.8-fold",
        "day-14",
        "bulk Nile Red fluorescence",
        "3437 +/- 17",
        "14195 +/- 216",
        "4.3-fold",
        "4.13",
        "2 micrograms/mL",
        "2.5",
        "No species separation",
        "not lipid mass",
    ):
        assert phrase in product["description"]
    assert product["scope"] == "COMMUNITY_LEVEL"
    assert "full 4.8-fold comparison includes medium enrichment" in growth["description"]
    assert growth["evidence"][0]["supports"] == "PARTIAL"
    assert gas["description"].startswith("HYPOTHESIZED -")
    assert eps["description"].startswith("HYPOTHESIZED -")
    for node, prefix in ((gas, "HYPOTHESIZED -"), (growth, "PARTIAL -")):
        assert len(node["downstream"]) == 1
        assert node["downstream"][0]["target"] == product["name"]
        assert node["downstream"][0]["description"].startswith(prefix)
    assert "downstream" not in eps and "downstream" not in product
    assert all("interaction_type" not in n for n in (gas, growth, eps, product))
    names = {n["name"] for n in doc["ecological_interactions"]}
    assert all(a.split("#", 1)[1] in names for a in doc["discussions"][0]["attaches_to"])


def test_exact_assay_boundaries_and_retained_topology():
    assert_assay_scope(document())


def test_guard_rejects_conflation_and_stale_links():
    control = document()
    assert_assay_scope(control)
    for change in ("description", "edge", "support", "anchor"):
        mutated = deepcopy(control)
        if change == "description":
            mutated["ecological_interactions"][3]["description"] = "Fourfold biomass and lipid mass"
        elif change == "edge":
            mutated["ecological_interactions"][0]["downstream"][0]["target"] = "old endpoint"
        elif change == "support":
            mutated["ecological_interactions"][1]["evidence"][0]["supports"] = "SUPPORT"
        else:
            mutated["discussions"][0]["attaches_to"][0] = "ecological_interactions#old endpoint"
        assert mutated != control
        with pytest.raises(AssertionError):
            assert_assay_scope(mutated)
        assert_assay_scope(control)


def test_nongraph_metadata_eps_and_append_only_history_preserved():
    before = yaml.safe_load(subprocess.check_output(["git", "show", f"{BASE}:{TARGET}"], cwd=ROOT))
    after = document()
    assert {k for k in before if before[k] != after[k]} == {
        "ecological_interactions",
        "discussions",
        "curation_history",
    }
    assert before["ecological_interactions"][2] == after["ecological_interactions"][2]
    assert before["curation_history"] == after["curation_history"][:-1]
    assert after["curation_history"][-1]["llm_assisted"] is True
    assert after["discussions"][0]["status"] == "OPEN"


def test_source_excerpt_presence_and_research_lineage():
    doc = document()
    cache = " ".join((ROOT / "references_cache/PMID_42217804.md").read_text().split())
    for node in doc["ecological_interactions"]:
        for ev in node["evidence"]:
            assert " ".join(ev["snippet"].split()) in cache
    row = yaml.safe_load((ROOT / LEDGER).read_text())["records"][0]
    prior = next(
        r
        for r in yaml.safe_load((ROOT / row["supersedes_review"]["review_file"]).read_text())[
            "records"
        ]
        if r["id"] == doc["id"]
    )
    assert (
        row["original_sha256"]
        == prior["record_sha256"]
        == row["supersedes_review"]["record_sha256"]
    )
    assert row["record_sha256"] == hashlib.sha256((ROOT / TARGET).read_bytes()).hexdigest()
    assert row["status"] == "needs_research" and row["open_research_issue"] == 1681
    actual = [
        {"source": n["name"], **e}
        for n in doc["ecological_interactions"]
        for e in n.get("downstream", [])
    ]
    assert actual == row["edges_after"] and len(actual) == 2
    assert len(row["node_decisions"]) == 4
