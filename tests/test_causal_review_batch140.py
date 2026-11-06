"""Verify Cycle 8 Stage 2 causal graph curation for CommunityMech:000510-000514 (batch 140)."""

import hashlib
import json
from copy import deepcopy
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261105-stage2-five-records-batch140.yaml"
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


def _check_batch140_invariants(ledger: dict, rows: list[dict], docs: list[dict]) -> None:
    assert len(rows) == 5
    assert ledger["independent_approval"] is False
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert ledger["reviewed_counts"] == {
        "retained_nodes": 8,
        "removed_nodes": 0,
        "retained_arrows": 1,
        "removed_arrows": 0,
        "renamed_nodes": 0,
        "graph_quotations": 28,
        "discussion_quotations": 6,
    }
    assert [row["id"] for row in rows] == [
        "CommunityMech:000510",
        "CommunityMech:000511",
        "CommunityMech:000512",
        "CommunityMech:000513",
        "CommunityMech:000514",
    ]

    expected_node_edge_counts = {
        "CommunityMech:000510": (2, 1),
        "CommunityMech:000511": (1, 0),
        "CommunityMech:000512": (1, 0),
        "CommunityMech:000513": (2, 0),
        "CommunityMech:000514": (2, 0),
    }

    expected_evidence_counts = {
        "CommunityMech:000510": 7,
        "CommunityMech:000511": 4,
        "CommunityMech:000512": 4,
        "CommunityMech:000513": 6,
        "CommunityMech:000514": 7,
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
        exp_nodes, exp_edges = expected_node_edge_counts[row["id"]]
        assert len(nodes) == exp_nodes, f"{row['id']} expected {exp_nodes} nodes"
        names = [n["name"] for n in nodes]
        assert len(set(names)) == exp_nodes
        edges = [(n["name"], d["target"]) for n in nodes for d in (n.get("downstream") or [])]
        assert len(edges) == exp_edges, f"{row['id']} expected {exp_edges} directed causal edges"
        assert len(row["edges_after"]) == exp_edges
        assert len(row["retained_edge_decisions"]) == exp_edges

        canonical = [
            {k: t["taxon_term"][k] for k in ["preferred_term", "term"]} for t in doc["taxonomy"]
        ]
        total_ev = 0
        for n in nodes:
            assert n.get("scope") in {"PAIRWISE", "COMMUNITY_LEVEL"}
            if n["scope"] == "PAIRWISE":
                assert set(n["source_taxon"]) == {"preferred_term", "term"}
                assert set(n["target_taxon"]) == {"preferred_term", "term"}
                assert n["source_taxon"] in canonical
                assert n["target_taxon"] in canonical
            else:
                ptaxa = n.get("participating_taxa") or []
                assert len(ptaxa) == len(canonical)
                assert all(t in canonical and set(t) == {"preferred_term", "term"} for t in ptaxa)
            for d in n.get("downstream") or []:
                assert d["target"] in names
                assert len(d.get("description", "")) > 20
            ev_list = n.get("evidence") or []
            total_ev += len(ev_list)
            for ev in ev_list:
                assert "[" not in ev["snippet"]
                cache_path = _ref_to_cache_path(ev["reference"])
                assert cache_path.exists(), f"Missing cache {cache_path} for {row['id']}"
                norm_snippet = " ".join(ev["snippet"].split())
                norm_cache = " ".join(cache_path.read_text().split())
                assert (
                    norm_snippet in norm_cache
                ), f"Snippet mismatch in {row['id']}: {ev['reference']}"

        assert total_ev == expected_evidence_counts[row["id"]]

        discussions = doc.get("discussions") or []
        assert len(discussions) == 1
        assert discussions[0]["kind"] == "KNOWLEDGE_GAP"

    assert "HdrABC/HdrL Sfum_0819-0824" in docs[0]["ecological_interactions"][0]["description"]
    assert (
        "PC1 explaining ~70% of proteomic variance"
        in docs[0]["ecological_interactions"][1]["description"]
    )
    assert (
        "no extracellular formate accumulation detected in the biculture"
        in docs[1]["ecological_interactions"][0]["description"]
    )
    assert (
        "0.15 ± 0.006 to 0.26 ± 0.02 mmol/L/day"
        in docs[2]["ecological_interactions"][0]["description"]
    )
    assert (
        "Rhodococcus sp. OAS809 (68 ± 33%" in docs[3]["ecological_interactions"][0]["description"]
    )
    assert "40.62% to 76.56%" in docs[4]["ecological_interactions"][0]["description"]


def test_batch140_covers_c8s1_records_with_verified_hashes_and_history():
    ledger, rows, docs = records()
    _check_batch140_invariants(ledger, rows, docs)


def test_causal_graph_review_summary_covers_all_508_records():
    summary = json.loads(SUMMARY.read_text())
    assert summary["records"] >= 508
    assert summary["nodes"] >= 1493
    assert summary["edges"] >= 587
    assert summary["records_without_nodes"] <= 10
    assert summary["records"] - summary["records_without_edges"] >= 302
    assert summary["review_status_counts"].get("needs_research") == 54
    assert summary["review_status_counts"].get("reviewed", 0) >= 454
    assert summary["structural_defects"] == []


def test_the_check_can_actually_fail():
    ledger, rows, docs = records()
    # Control arm: unmutated copy passes cleanly
    _check_batch140_invariants(deepcopy(ledger), deepcopy(rows), deepcopy(docs))

    # Mutated arm 1: corrupting curation_history action on CommunityMech:000510 fails
    bad_docs = deepcopy(docs)
    bad_docs[0]["curation_history"][-1]["action"] = "IMPORTED"
    with pytest.raises(AssertionError):
        _check_batch140_invariants(deepcopy(ledger), deepcopy(rows), bad_docs)

    # Mutated arm 2: corrupting a cached snippet on CommunityMech:000511 fails
    bad_docs_snippet = deepcopy(docs)
    bad_docs_snippet[1]["ecological_interactions"][0]["evidence"][0][
        "snippet"
    ] = "nonexistent fabricated snippet text that is not in references_cache"
    with pytest.raises(AssertionError, match="Snippet mismatch"):
        _check_batch140_invariants(deepcopy(ledger), deepcopy(rows), bad_docs_snippet)

    # Mutated arm 3: dropping the retained downstream edge from CommunityMech:000510 fails
    bad_docs_edge = deepcopy(docs)
    bad_docs_edge[0]["ecological_interactions"][0]["downstream"] = []
    with pytest.raises(AssertionError, match="expected 1 directed causal edges"):
        _check_batch140_invariants(deepcopy(ledger), deepcopy(rows), bad_docs_edge)
