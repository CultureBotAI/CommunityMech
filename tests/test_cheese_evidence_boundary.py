"""Keep explicit evidence limits without silently closing the cheese research gap."""

import csv
import hashlib
import subprocess
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
TARGET = "kb/communities/Cheese_Rind_InSitu_InVitro_Model_Community.yaml"
BASE = "aafb95ba7442031eef348d072a184a248c4b54ad"
LEDGER = "reports/causal_graph_review/decisions/20261015-cheese-evidence.yaml"


def documents():
    before = yaml.safe_load(subprocess.check_output(["git", "show", f"{BASE}:{TARGET}"], cwd=ROOT))
    after = yaml.safe_load((ROOT / TARGET).read_text())
    return before, after


def test_changes_are_limited_to_graph_wording_discussion_and_one_event():
    before, after = documents()
    assert {k for k in before if before[k] != after[k]} == {
        "ecological_interactions",
        "discussions",
        "curation_history",
    }
    assert after["curation_history"][:-1] == before["curation_history"]
    assert after["curation_history"][-1]["llm_assisted"] is True
    for old, new in zip(
        before["ecological_interactions"], after["ecological_interactions"], strict=True
    ):
        assert {k: v for k, v in old.items() if k != "description"} == {
            k: v for k, v in new.items() if k != "description"
        }


def test_unresolved_mechanisms_do_not_borrow_the_succession_snippet():
    _, doc = documents()
    assembly, deacidification, succession = doc["ecological_interactions"]
    assert assembly["description"].startswith("HYPOTHESIZED")
    assert "not a moisture-specific effect" in assembly["description"]
    assert deacidification["description"].startswith("PARTIAL")
    assert "not a mechanism established by the retained abstract" in deacidification["description"]
    assert "without assigning pH mediation or responsive pairs" in deacidification["description"]
    assert not assembly.get("evidence") and not deacidification.get("evidence")
    assert len(succession["evidence"]) == 1
    assert "does not establish exact timing" in succession["description"]
    assert all(not n.get("downstream") for n in doc["ecological_interactions"])
    assert doc["discussions"][-1]["status"] == "OPEN"
    assert (
        "Search-index membership and protocol leads are not verified"
        in doc["discussions"][-1]["rationale"]
    )


def test_successor_keeps_exact_hash_lineage_and_research_status():
    row = yaml.safe_load((ROOT / LEDGER).read_text())["records"][0]
    prior_path = row["supersedes_review"]["review_file"]
    prior = next(
        r
        for r in yaml.safe_load((ROOT / prior_path).read_text())["records"]
        if r["id"] == row["id"]
    )
    assert (
        row["original_sha256"]
        == prior["record_sha256"]
        == row["supersedes_review"]["record_sha256"]
    )
    assert row["record_sha256"] == hashlib.sha256((ROOT / TARGET).read_bytes()).hexdigest()
    assert row["status"] == "needs_research" and row["open_issue"] == 765
    assert row["edges_before"] == row["edges_after"] == []
    _, doc = documents()
    assert [d["node"] for d in row["node_decisions"]] == [
        n["name"] for n in doc["ecological_interactions"]
    ]
    with (ROOT / "reports/causal_graph_review/inventory.tsv").open() as handle:
        inventory = next(r for r in csv.DictReader(handle, delimiter="\t") if r["id"] == row["id"])
    assert inventory["review_status"] == "needs_research"
    assert inventory["review_file"] == LEDGER


def test_both_abstract_caches_are_byte_preserved():
    for suffix in ("md", "txt"):
        path = f"references_cache/PMID_25036636.{suffix}"
        assert (ROOT / path).read_bytes() == subprocess.check_output(
            ["git", "show", f"{BASE}:{path}"], cwd=ROOT
        )
