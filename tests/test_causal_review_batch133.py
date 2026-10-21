"""Verify Stage 2 causal graph curation for CommunityMech:000469-000483 (batch 133)."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = (
    ROOT / "reports/causal_graph_review/decisions/20261020-stage2-fifteen-records-batch133.yaml"
)


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / row["path"]).read_text()) for row in rows]


def test_batch133_covers_all_fifteen_stage1_records_with_verified_hashes_and_history():
    ledger, rows, docs = records()
    assert len(rows) == 15
    assert ledger["independent_approval"] is False
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert ledger["reviewed_counts"] == {
        "retained_nodes": 45,
        "removed_nodes": 0,
        "retained_arrows": 30,
        "removed_arrows": 0,
        "renamed_nodes": 0,
        "graph_quotations": 45,
        "discussion_quotations": 0,
    }
    expected_ids = [f"CommunityMech:000{i}" for i in range(469, 484)]
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


def test_batch133_each_record_has_three_nodes_two_directed_edges_and_verbatim_abstract_snippets():
    _, rows, docs = records()
    for row, doc in zip(rows, docs, strict=True):
        nodes = doc["ecological_interactions"]
        assert len(nodes) == 3, f"{row['id']} expected 3 nodes"
        names = [n["name"] for n in nodes]
        assert len(set(names)) == 3
        edges = [(n["name"], d["target"]) for n in nodes for d in (n.get("downstream") or [])]
        assert len(edges) == 2, f"{row['id']} expected 2 directed causal edges"
        assert len(row["edges_before"]) in {0, 1}
        assert len(row["edges_after"]) == 2
        assert len(row["retained_edge_decisions"]) == 2

        canonical = [
            {k: t["taxon_term"][k] for k in ["preferred_term", "term"]} for t in doc["taxonomy"]
        ]
        for n in nodes:
            assert n.get("scope") in {"PAIRWISE", "COMMUNITY_LEVEL"}
            if n["scope"] == "COMMUNITY_LEVEL":
                ptaxa = n.get("participating_taxa") or []
                assert len(ptaxa) >= 2
                assert all(t in canonical and set(t) == {"preferred_term", "term"} for t in ptaxa)
            else:
                assert "source_taxon" in n
            for d in n.get("downstream") or []:
                assert d["target"] in names
                assert len(d.get("description", "")) > 20
            for ev in n.get("evidence") or []:
                ref = ev["reference"]
                assert ref.startswith("PMID:")
                pmid = ref.split(":", 1)[1]
                cache_path = ROOT / "references_cache" / f"PMID_{pmid}.txt"
                assert cache_path.exists()
                norm_snippet = " ".join(ev["snippet"].split())
                norm_cache = " ".join(cache_path.read_text().split())
                assert norm_snippet in norm_cache
