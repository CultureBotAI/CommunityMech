"""Verify Cycle 4 Stage 2 causal graph curation for CommunityMech:000496 (batch 136)."""

import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261031-stage2-one-record-batch136.yaml"
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


def test_batch136_covers_c4s1_record_with_verified_hash_and_history():
    ledger, rows, docs = records()
    assert len(rows) == 1
    assert ledger["independent_approval"] is False
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert ledger["reviewed_counts"] == {
        "retained_nodes": 4,
        "removed_nodes": 0,
        "retained_arrows": 3,
        "removed_arrows": 0,
        "renamed_nodes": 1,
        "graph_quotations": 10,
        "discussion_quotations": 0,
    }
    assert [row["id"] for row in rows] == ["CommunityMech:000496"]

    for row, doc in zip(rows, docs, strict=True):
        assert row["status"] == "reviewed"
        assert row["original_sha256"] != row["record_sha256"]
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert set(row["allowed_changed_fields"]) == {
            "ecological_interactions",
            "discussions",
            "curation_history",
        }
        assert row["curation_events_added"] == 1
        assert len(row["history_files"]) >= 1
        assert all((ROOT / hf).exists() for hf in row["history_files"])
        assert doc["curation_history"][-1]["action"] == "CURATE_CAUSAL_GRAPH"
        assert doc["curation_history"][-1]["llm_assisted"] is True
        assert doc["discussions"][0]["attaches_to"] == [
            (
                "ecological_interactions#"
                "Predicted Emergent Cyanobacterial Ammonium and Organic Acid Cross-Feeding"
            ),
            (
                "ecological_interactions#"
                "Predicted Reciprocal Methanotroph Carbon and Glutamine Cross-Feeding"
            ),
        ]


def test_batch136_nodes_edges_scope_and_verbatim_cached_snippets():
    _, rows, docs = records()
    expected_node_edge_counts = {
        "CommunityMech:000496": (4, 3),
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
        for n in nodes:
            assert n.get("scope") == "PAIRWISE"
            assert {k: n["source_taxon"][k] for k in ["preferred_term", "term"]} in canonical
            assert {k: n["target_taxon"][k] for k in ["preferred_term", "term"]} in canonical
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


def test_causal_graph_review_summary_covers_all_490_records():
    summary = json.loads(SUMMARY.read_text())
    assert summary["records"] >= 490
    assert summary["nodes"] >= 1463
    assert summary["edges"] >= 585
    assert summary["records_without_nodes"] <= 10
    assert summary["records_without_edges"] <= 190
    assert summary["review_status_counts"].get("needs_research") == 54
    assert summary["review_status_counts"].get("reviewed", 0) >= 436
    assert summary["structural_defects"] == []
