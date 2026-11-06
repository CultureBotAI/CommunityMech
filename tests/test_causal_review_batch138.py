"""Verify Cycle 6 Stage 2 causal graph curation for CommunityMech:000501-000504 (batch 138)."""

import hashlib
import json
from copy import deepcopy
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261104-stage2-four-records-batch138.yaml"
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


def _check_batch138_invariants(ledger: dict, rows: list[dict], docs: list[dict]) -> None:
    assert len(rows) == 4
    assert ledger["independent_approval"] is False
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert ledger["reviewed_counts"] == {
        "retained_nodes": 9,
        "removed_nodes": 0,
        "retained_arrows": 0,
        "removed_arrows": 0,
        "renamed_nodes": 0,
        "graph_quotations": 27,
        "discussion_quotations": 3,
    }
    assert [row["id"] for row in rows] == [
        "CommunityMech:000501",
        "CommunityMech:000502",
        "CommunityMech:000503",
        "CommunityMech:000504",
    ]

    expected_node_edge_counts = {
        "CommunityMech:000501": (3, 0),
        "CommunityMech:000502": (2, 0),
        "CommunityMech:000503": (2, 0),
        "CommunityMech:000504": (2, 0),
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
            for ev in n.get("evidence") or []:
                cache_path = _ref_to_cache_path(ev["reference"])
                assert cache_path.exists(), f"Missing cache {cache_path} for {row['id']}"
                norm_snippet = " ".join(ev["snippet"].split())
                norm_cache = " ".join(cache_path.read_text().split())
                assert (
                    norm_snippet in norm_cache
                ), f"Snippet mismatch in {row['id']}: {ev['reference']}"

    assert "33.81-59.52%" in rows[0]["summary"]
    assert "7-day HPLC assay" in docs[1]["ecological_interactions"][0]["description"]
    assert (
        "7-day naphthalene biodegradation rate"
        in docs[2]["ecological_interactions"][0]["description"]
    )
    assert "7-day HPLC assay" in docs[3]["ecological_interactions"][0]["description"]
    for pah_doc in docs[1:4]:
        serialized = json.dumps(pah_doc)
        assert "bentonite" not in serialized.lower()
        assert "6 days" not in serialized.lower()


def test_batch138_covers_c6s1_records_with_verified_hashes_and_history():
    ledger, rows, docs = records()
    _check_batch138_invariants(ledger, rows, docs)


def test_causal_graph_review_summary_covers_all_498_records():
    summary = json.loads(SUMMARY.read_text())
    assert summary["records"] >= 498
    assert summary["nodes"] >= 1480
    assert summary["edges"] >= 586
    assert summary["records_without_nodes"] <= 10
    assert summary["records"] - summary["records_without_edges"] >= 301
    assert summary["review_status_counts"].get("needs_research") == 54
    assert summary["review_status_counts"].get("reviewed", 0) >= 444
    assert summary["structural_defects"] == []


def test_the_check_can_actually_fail():
    ledger, rows, docs = records()
    # Control arm: unmutated copy passes cleanly
    _check_batch138_invariants(deepcopy(ledger), deepcopy(rows), deepcopy(docs))

    # Mutated arm 1: corrupting curation_history action on CommunityMech:000501 fails
    bad_docs = deepcopy(docs)
    bad_docs[0]["curation_history"][-1]["action"] = "IMPORTED"
    with pytest.raises(AssertionError):
        _check_batch138_invariants(deepcopy(ledger), deepcopy(rows), bad_docs)

    # Mutated arm 2: corrupting a cached snippet on CommunityMech:000502 fails
    bad_docs_snippet = deepcopy(docs)
    bad_docs_snippet[1]["ecological_interactions"][0]["evidence"][0][
        "snippet"
    ] = "nonexistent fabricated snippet text that is not in references_cache"
    with pytest.raises(AssertionError, match="Snippet mismatch"):
        _check_batch138_invariants(deepcopy(ledger), deepcopy(rows), bad_docs_snippet)

    # Mutated arm 3: injecting unsupported bentonite/6 days wording into PAH record fails
    bad_docs_protocol = deepcopy(docs)
    bad_docs_protocol[2]["ecological_interactions"][0]["description"] += " bentonite clay 6 days"
    with pytest.raises(AssertionError):
        _check_batch138_invariants(deepcopy(ledger), deepcopy(rows), bad_docs_protocol)
