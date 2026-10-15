"""Keep separate isolate measurements scoped to their named assay participants."""

import csv
import hashlib
import subprocess
from copy import deepcopy
from pathlib import Path

import pytest
import yaml

from communitymech.network.auditor import NetworkIntegrityAuditor

ROOT = Path(__file__).resolve().parents[1]
TARGET = "kb/communities/Okeke_Lu_Cellulolytic_Consortium.yaml"
BASE = "f42697b3660d8832a54852f9b3593aafe229bc6b"
LEDGER = "reports/causal_graph_review/decisions/20261015-okeke-participants.yaml"
EXPECTED = (
    {"Pseudoxanthomonas byssovorax DB1", "Microbacterium oxydans DB2"},
    {"Microbacterium oxydans DB2", "Klebsiella sp. DB13"},
)


def document():
    return yaml.safe_load((ROOT / TARGET).read_text())


def assert_participants(doc):
    members = {t["taxon_term"]["preferred_term"]: t["taxon_term"]["term"] for t in doc["taxonomy"]}
    for node, expected in zip(doc["ecological_interactions"][:2], EXPECTED, strict=True):
        assert node["scope"] == "COMMUNITY_LEVEL"
        participants = node.get("participating_taxa", [])
        assert len(participants) == 2
        assert {p["preferred_term"] for p in participants} == expected
        assert all(p["term"] == members[p["preferred_term"]] for p in participants)
        assert "source_taxon" not in node and "target_taxon" not in node


def test_exact_canonical_isolate_subsets():
    assert_participants(document())


@pytest.mark.parametrize("index", [0, 1])
def test_isolated_node_does_not_credit_members_outside_named_subset(tmp_path, index):
    # Exclusion from these reported values does not imply an inactive or untested isolate.
    doc = document()
    all_members = {t["taxon_term"]["preferred_term"] for t in doc["taxonomy"]}
    node = deepcopy(doc["ecological_interactions"][index])
    node.pop("downstream", None)
    doc["ecological_interactions"] = [node]
    doc.pop("discussions", None)
    path = tmp_path / "assay.yaml"
    path.write_text(yaml.safe_dump(doc))
    issues = NetworkIntegrityAuditor(tmp_path).audit_community(path)
    disconnected = {i["taxon"] for i in issues if i["type"] == "DISCONNECTED"}
    assert disconnected == all_members - EXPECTED[index]


def test_only_participants_and_one_curation_event_change():
    before = yaml.safe_load(subprocess.check_output(["git", "show", f"{BASE}:{TARGET}"], cwd=ROOT))
    after = document()
    assert set(before) == set(after)
    assert {k for k in before if before[k] != after[k]} == {
        "ecological_interactions",
        "curation_history",
    }
    assert after["curation_history"][:-1] == before["curation_history"]
    assert after["curation_history"][-1]["llm_assisted"] is True
    for old, new in zip(
        before["ecological_interactions"], after["ecological_interactions"], strict=True
    ):
        assert old == {k: v for k, v in new.items() if k != "participating_taxa"}
    assert after["ecological_interactions"][2] == before["ecological_interactions"][2]
    assert after["discussions"][0]["status"] == "OPEN"
    cache = "references_cache/PMID_20859703.txt"
    assert (ROOT / cache).read_bytes() == subprocess.check_output(
        ["git", "show", f"{BASE}:{cache}"], cwd=ROOT
    )


def test_participant_guard_rejects_missing_empty_and_wrong_subsets():
    control = document()
    assert_participants(control)
    for replacement in (None, [], [control["taxonomy"][2]["taxon_term"]]):
        mutated = deepcopy(control)
        node = mutated["ecological_interactions"][0]
        if replacement is None:
            del node["participating_taxa"]
            assert "participating_taxa" not in node
        else:
            node["participating_taxa"] = replacement
            assert node["participating_taxa"] == replacement
        with pytest.raises(AssertionError):
            assert_participants(mutated)
        assert_participants(control)


def test_successor_preserves_lineage_topology_and_research_status():
    row = yaml.safe_load((ROOT / LEDGER).read_text())["records"][0]
    prior = next(
        r
        for r in yaml.safe_load((ROOT / row["supersedes_review"]["review_file"]).read_text())[
            "records"
        ]
        if r["id"] == row["id"]
    )
    assert (
        row["original_sha256"]
        == prior["record_sha256"]
        == row["supersedes_review"]["record_sha256"]
    )
    assert row["record_sha256"] == hashlib.sha256((ROOT / TARGET).read_bytes()).hexdigest()
    assert row["status"] == "needs_research" and row["open_research_issue"] == 1657
    doc = document()
    actual_edges = [
        {"source": n["name"], **e}
        for n in doc["ecological_interactions"]
        for e in n.get("downstream", [])
    ]
    assert len(actual_edges) == 2 and row["edges_before"] == row["edges_after"] == actual_edges
    assert [d["node"] for d in row["node_decisions"]] == [
        n["name"] for n in doc["ecological_interactions"]
    ]
    with (ROOT / "reports/causal_graph_review/inventory.tsv").open() as handle:
        entry = next(r for r in csv.DictReader(handle, delimiter="\t") if r["id"] == row["id"])
    assert entry["review_status"] == "needs_research" and entry["review_file"] == LEDGER
