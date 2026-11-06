"""Verify Cycle 7 Stage 2 causal graph curation for CommunityMech:000505-000509 (batch 139)."""

import hashlib
import json
from copy import deepcopy
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261105-stage2-five-records-batch139.yaml"
SUMMARY = ROOT / "reports/causal_graph_review/summary.json"


def _ref_to_cache_path(ref: str) -> Path:
    cache_dir = ROOT / "references_cache"
    if ref.startswith("PMID:"):
        pmid = ref.split(":", 1)[1]
        txt = cache_dir / f"PMID_{pmid}.txt"
        if txt.exists():
            return txt
        md = cache_dir / f"PMID_{pmid}.md"
        if md.exists():
            return md
        return txt
    if ref.lower().startswith("doi:"):
        raw = ref.split(":", 1)[1]
        slug = raw.lower().replace("/", "_").replace(".", "_")
        txt = cache_dir / f"DOI_{slug}.txt"
        if txt.exists():
            return txt
        md = cache_dir / f"doi_{raw.replace('/', '_')}.md"
        if md.exists():
            return md
        return txt
    raise ValueError(f"Unsupported reference format: {ref}")


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / row["path"]).read_text()) for row in rows]


def _check_batch139_invariants(ledger: dict, rows: list[dict], docs: list[dict]) -> None:
    assert len(rows) == 5
    assert ledger["independent_approval"] is False
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert ledger["reviewed_counts"] == {
        "retained_nodes": 5,
        "removed_nodes": 0,
        "retained_arrows": 0,
        "removed_arrows": 0,
        "renamed_nodes": 0,
        "graph_quotations": 21,
        "discussion_quotations": 5,
    }
    assert [row["id"] for row in rows] == [
        "CommunityMech:000505",
        "CommunityMech:000506",
        "CommunityMech:000507",
        "CommunityMech:000508",
        "CommunityMech:000509",
    ]

    expected_evidence_counts = {
        "CommunityMech:000505": 5,
        "CommunityMech:000506": 4,
        "CommunityMech:000507": 4,
        "CommunityMech:000508": 4,
        "CommunityMech:000509": 4,
    }

    for row, doc in zip(rows, docs, strict=True):
        assert row["status"] == "reviewed"
        assert row["original_sha256"] != row["record_sha256"]
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert row["curation_events_added"] == 1
        assert len(row["history_files"]) >= 1
        assert all((ROOT / hf).exists() for hf in row["history_files"])
        assert doc["curation_history"][-1]["action"] == "CURATE_CAUSAL_GRAPH"
        assert doc["curation_history"][-1]["llm_assisted"] is True

        nodes = doc["ecological_interactions"]
        assert len(nodes) == 1, f"{row['id']} expected 1 COMMUNITY_LEVEL node"
        names = [n["name"] for n in nodes]
        assert len(set(names)) == 1
        edges = [(n["name"], d["target"]) for n in nodes for d in (n.get("downstream") or [])]
        assert len(edges) == 0, f"{row['id']} expected 0 directed causal edges"
        assert len(row["edges_after"]) == 0
        assert len(row["retained_edge_decisions"]) == 0

        canonical = [
            {k: t["taxon_term"][k] for k in ["preferred_term", "term"]} for t in doc["taxonomy"]
        ]
        for n in nodes:
            assert n.get("scope") == "COMMUNITY_LEVEL"
            ptaxa = n.get("participating_taxa") or []
            assert len(ptaxa) == len(canonical)
            assert all(t in canonical and set(t) == {"preferred_term", "term"} for t in ptaxa)
            ev_list = n.get("evidence") or []
            assert len(ev_list) == expected_evidence_counts[row["id"]]
            for ev in ev_list:
                cache_path = _ref_to_cache_path(ev["reference"])
                assert cache_path.exists(), f"Missing cache {cache_path} for {row['id']}"
                norm_snippet = " ".join(ev["snippet"].split())
                norm_cache = " ".join(cache_path.read_text().split())
                assert (
                    norm_snippet in norm_cache
                ), f"Snippet mismatch in {row['id']}: {ev['reference']}"

        discussions = doc.get("discussions") or []
        assert len(discussions) == 1
        assert discussions[0]["kind"] == "KNOWLEDGE_GAP"

    assert "73 min 2 s" in docs[0]["ecological_interactions"][0]["description"]
    assert "128 min 12 s" in docs[0]["ecological_interactions"][0]["description"]
    assert "121 min 4 s" in docs[1]["ecological_interactions"][0]["description"]
    assert "80 min 6 s" in docs[2]["ecological_interactions"][0]["description"]
    assert "49 min 6 s" in docs[3]["ecological_interactions"][0]["description"]
    assert "49 min 6 s" in docs[4]["ecological_interactions"][0]["description"]


def test_batch139_covers_c7s1_records_with_verified_hashes_and_history():
    ledger, rows, docs = records()
    _check_batch139_invariants(ledger, rows, docs)


def test_causal_graph_review_summary_covers_all_503_records():
    summary = json.loads(SUMMARY.read_text())
    assert summary["records"] >= 503
    assert summary["nodes"] >= 1485
    assert summary["edges"] >= 586
    assert summary["records_without_nodes"] <= 10
    assert summary["records"] - summary["records_without_edges"] >= 301
    assert summary["review_status_counts"].get("needs_research") == 54
    assert summary["review_status_counts"].get("reviewed", 0) >= 449
    assert summary["structural_defects"] == []


def test_the_check_can_actually_fail():
    ledger, rows, docs = records()
    # Control arm: unmutated copy passes cleanly
    _check_batch139_invariants(deepcopy(ledger), deepcopy(rows), deepcopy(docs))

    # Mutated arm 1: corrupting curation_history action on CommunityMech:000505 fails
    bad_docs = deepcopy(docs)
    bad_docs[0]["curation_history"][-1]["action"] = "IMPORTED"
    with pytest.raises(AssertionError):
        _check_batch139_invariants(deepcopy(ledger), deepcopy(rows), bad_docs)

    # Mutated arm 2: corrupting a cached snippet on CommunityMech:000506 fails
    bad_docs_snippet = deepcopy(docs)
    bad_docs_snippet[1]["ecological_interactions"][0]["evidence"][0][
        "snippet"
    ] = "nonexistent fabricated snippet text that is not in references_cache"
    with pytest.raises(AssertionError, match="Snippet mismatch"):
        _check_batch139_invariants(deepcopy(ledger), deepcopy(rows), bad_docs_snippet)

    # Mutated arm 3: dropping a participating taxon from CommunityMech:000509 fails
    bad_docs_ptaxa = deepcopy(docs)
    bad_docs_ptaxa[4]["ecological_interactions"][0]["participating_taxa"].pop()
    with pytest.raises(AssertionError):
        _check_batch139_invariants(deepcopy(ledger), deepcopy(rows), bad_docs_ptaxa)
