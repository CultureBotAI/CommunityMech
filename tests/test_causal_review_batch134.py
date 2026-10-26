"""Verify Cycle 2 Stage 2 causal graph curation for CommunityMech:000484-000490 (batch 134)."""

import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261025-stage2-seven-records-batch134.yaml"
SUMMARY = ROOT / "reports/causal_graph_review/summary.json"


def _ref_to_cache_path(ref: str) -> Path:
    cache_dir = ROOT / "references_cache"
    if ref.startswith("PMID:"):
        return cache_dir / f"PMID_{ref.split(':', 1)[1]}.txt"
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


def test_batch134_covers_all_seven_c2s1_records_with_verified_hashes_and_history():
    ledger, rows, docs = records()
    assert len(rows) == 7
    assert ledger["independent_approval"] is False
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert ledger["reviewed_counts"] == {
        "retained_nodes": 17,
        "removed_nodes": 0,
        "retained_arrows": 10,
        "removed_arrows": 0,
        "renamed_nodes": 0,
        "graph_quotations": 39,
        "discussion_quotations": 0,
    }
    expected_ids = [f"CommunityMech:000{i}" for i in range(484, 491)]
    assert [row["id"] for row in rows] == expected_ids

    for row, doc in zip(rows, docs, strict=True):
        assert row["status"] == "reviewed"
        assert row["original_sha256"] != row["record_sha256"]
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert set(row["allowed_changed_fields"]) == {
            "ecological_interactions",
            "curation_history",
        }
        assert row["curation_events_added"] == len(row["history_files"]) == 1
        assert (ROOT / row["history_files"][0]).exists()
        assert doc["curation_history"][-1]["action"] == "CURATE_CAUSAL_GRAPH"
        assert doc["curation_history"][-1]["llm_assisted"] is True


def test_batch134_nodes_edges_scope_and_verbatim_cached_snippets():
    _, rows, docs = records()
    expected_node_edge_counts = {
        "CommunityMech:000484": (3, 2),
        "CommunityMech:000485": (3, 2),
        "CommunityMech:000486": (2, 1),
        "CommunityMech:000487": (2, 1),
        "CommunityMech:000488": (2, 1),
        "CommunityMech:000489": (3, 2),
        "CommunityMech:000490": (2, 1),
    }
    for row, doc in zip(rows, docs, strict=True):
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
        is_isolate = row["path"].startswith("data/isolates/")
        for n in nodes:
            assert n.get("scope") in {"PAIRWISE", "COMMUNITY_LEVEL"}
            if is_isolate:
                assert n["scope"] == "COMMUNITY_LEVEL"
                assert "participating_taxa" not in n
                assert n["source_taxon"] in canonical
            elif n["scope"] == "COMMUNITY_LEVEL":
                ptaxa = n.get("participating_taxa") or []
                assert len(ptaxa) >= 2
                assert all(t in canonical and set(t) == {"preferred_term", "term"} for t in ptaxa)
            else:
                assert "source_taxon" in n
                assert "target_taxon" in n
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


def test_causal_graph_review_summary_covers_all_484_records():
    summary = json.loads(SUMMARY.read_text())
    assert summary["records"] >= 484
    assert summary["nodes"] >= 1445
    assert summary["edges"] >= 573
    assert summary["records_without_nodes"] <= 10
    assert summary["records_without_edges"] <= 190
    assert summary["review_status_counts"].get("needs_research") == 54
    assert summary["review_status_counts"].get("reviewed", 0) >= 430
    assert summary["structural_defects"] == []
