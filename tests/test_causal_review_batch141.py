"""Verify Cycle 9 Stage 2 causal graph curation for CommunityMech:000515-000521 (batch 141)."""

import hashlib
import json
from copy import deepcopy
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261106-stage2-seven-records-batch141.yaml"
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


def _check_batch141_invariants(ledger: dict, rows: list[dict], docs: list[dict]) -> None:
    assert len(rows) == 7
    assert ledger["independent_approval"] is False
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert ledger["reviewed_counts"] == {
        "retained_nodes": 21,
        "removed_nodes": 0,
        "retained_arrows": 2,
        "removed_arrows": 0,
        "renamed_nodes": 0,
        "graph_quotations": 55,
        "discussion_quotations": 5,
    }
    assert [row["id"] for row in rows] == [
        "CommunityMech:000515",
        "CommunityMech:000516",
        "CommunityMech:000517",
        "CommunityMech:000518",
        "CommunityMech:000519",
        "CommunityMech:000520",
        "CommunityMech:000521",
    ]

    expected_node_edge_counts = {
        "CommunityMech:000515": (2, 0),
        "CommunityMech:000516": (5, 0),
        "CommunityMech:000517": (4, 0),
        "CommunityMech:000518": (3, 0),
        "CommunityMech:000519": (2, 1),
        "CommunityMech:000520": (2, 1),
        "CommunityMech:000521": (3, 0),
    }

    expected_evidence_counts = {
        "CommunityMech:000515": 2,
        "CommunityMech:000516": 8,
        "CommunityMech:000517": 13,
        "CommunityMech:000518": 9,
        "CommunityMech:000519": 7,
        "CommunityMech:000520": 8,
        "CommunityMech:000521": 8,
    }

    changed_ids = {
        "CommunityMech:000517",
        "CommunityMech:000518",
        "CommunityMech:000519",
        "CommunityMech:000520",
        "CommunityMech:000521",
    }

    for row, doc in zip(rows, docs, strict=True):
        assert row["status"] == "reviewed"
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        if row["id"] in changed_ids:
            assert row["outcome"] == "changed"
            assert row["original_sha256"] != row["record_sha256"]
            assert row["curation_events_added"] == 1
            assert len(row["history_files"]) >= 1
            assert all((ROOT / hf).exists() for hf in row["history_files"])
            assert doc["curation_history"][-1]["action"] == "CURATE_CAUSAL_GRAPH"
            assert doc["curation_history"][-1]["llm_assisted"] is True
        else:
            assert row["outcome"] == "unchanged"
            assert row["original_sha256"] == row["record_sha256"]
            assert row["curation_events_added"] == 0

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
                assert len(ptaxa) >= 1
                assert all(t in canonical and set(t) == {"preferred_term", "term"} for t in ptaxa)
            for d in n.get("downstream") or []:
                assert d["target"] in names
                assert len(d.get("description", "")) > 20
            ev_list = n.get("evidence") or []
            total_ev += len(ev_list)
            norm_node_snippets = [" ".join(ev["snippet"].split()) for ev in ev_list]
            for idx_a, snip_a in enumerate(norm_node_snippets):
                for idx_b, snip_b in enumerate(norm_node_snippets):
                    if idx_a != idx_b:
                        assert (
                            snip_a not in snip_b
                        ), f"Redundant substring snippet in {row['id']} node {n['name']}"
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

        if row["id"] in changed_ids:
            discussions = doc.get("discussions") or []
            assert len(discussions) == 1
            assert discussions[0]["kind"] == "KNOWLEDGE_GAP"

    assert (
        "highest maximum fermentative efficiency (Delta pHmax, Figure 7B)"
        in docs[2]["ecological_interactions"][0]["description"]
    )
    assert (
        "null across 10^3, 10^5, or 10^7 CFU g^-1 in unplanted soil over 32 days"
        in docs[3]["ecological_interactions"][0]["description"]
    )
    assert (
        "61.62-fold (to 2.08 mW m^-2 versus 128.20 mW m^-2 without ethanol)"
        in docs[4]["ecological_interactions"][0]["description"]
    )
    assert (
        "SO2-BS1 reached 3.65 uM riboflavin and 243.71 mW m^-2"
        in docs[5]["ecological_interactions"][0]["description"]
    )
    assert (
        "zero cross-inhibition across the 9-isolate Mueller-Hinton compatibility matrix"
        in docs[6]["ecological_interactions"][0]["description"]
    )


def test_batch141_covers_c9s1_records_with_verified_hashes_and_history():
    ledger, rows, docs = records()
    _check_batch141_invariants(ledger, rows, docs)


def test_causal_graph_review_summary_covers_all_515_records():
    summary = json.loads(SUMMARY.read_text())
    assert summary["records"] >= 515
    assert summary["nodes"] >= 1514
    assert summary["edges"] >= 589
    assert summary["records_without_nodes"] <= 10
    assert summary["records"] - summary["records_without_edges"] >= 304
    assert summary["review_status_counts"].get("needs_research") == 54
    assert summary["review_status_counts"].get("reviewed", 0) >= 461
    assert summary["structural_defects"] == []


def test_the_check_can_actually_fail():
    ledger, rows, docs = records()
    # Control arm: unmutated copy passes cleanly
    _check_batch141_invariants(deepcopy(ledger), deepcopy(rows), deepcopy(docs))

    # Mutated arm 1: corrupting curation_history action on CommunityMech:000517 fails
    bad_docs = deepcopy(docs)
    bad_docs[2]["curation_history"][-1]["action"] = "IMPORTED"
    with pytest.raises(AssertionError):
        _check_batch141_invariants(deepcopy(ledger), deepcopy(rows), bad_docs)

    # Mutated arm 2: corrupting a cached snippet on CommunityMech:000518 fails
    bad_docs_snippet = deepcopy(docs)
    bad_docs_snippet[3]["ecological_interactions"][0]["evidence"][0][
        "snippet"
    ] = "nonexistent fabricated snippet text that is not in references_cache"
    with pytest.raises(AssertionError, match="Snippet mismatch"):
        _check_batch141_invariants(deepcopy(ledger), deepcopy(rows), bad_docs_snippet)

    # Mutated arm 3: dropping the retained downstream edge from CommunityMech:000519 fails
    bad_docs_edge = deepcopy(docs)
    bad_docs_edge[4]["ecological_interactions"][0]["downstream"] = []
    with pytest.raises(AssertionError, match="expected 1 directed causal edges"):
        _check_batch141_invariants(deepcopy(ledger), deepcopy(rows), bad_docs_edge)

    # Mutated arm 4: duplicating a snippet on the same node in CommunityMech:000517 fails
    bad_docs_dup = deepcopy(docs)
    bad_docs_dup[2]["ecological_interactions"][0]["evidence"][2]["snippet"] = bad_docs_dup[2][
        "ecological_interactions"
    ][0]["evidence"][0]["snippet"]
    with pytest.raises(AssertionError, match="Redundant substring snippet"):
        _check_batch141_invariants(deepcopy(ledger), deepcopy(rows), bad_docs_dup)
