"""Regression and mutation-proof gate tests for Cycle 10 Stage 2 causal-graph review (Batch 142)."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parents[1]
DECISION_FILE = (
    REPO / "reports/causal_graph_review/decisions/20261107-stage2-four-records-batch142.yaml"
)
SUMMARY_FILE = REPO / "reports/causal_graph_review/summary.json"
INVENTORY_FILE = REPO / "reports/causal_graph_review/inventory.tsv"


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _snippet_matches(snippet: str, cache_text: str) -> bool:
    return " ".join(snippet.split()) in " ".join(cache_text.split())


def verify_batch142_contract(
    decision_data: dict,
    records_by_id: dict[str, dict],
    record_hashes: dict[str, str],
    ref_caches: dict[str, str],
) -> None:
    """Validate Batch 142 causal-graph decision ledger and record invariants."""
    expected_ids = [
        "CommunityMech:000522",
        "CommunityMech:000523",
        "CommunityMech:000524",
        "CommunityMech:000525",
    ]
    entries = decision_data.get("records", [])
    entry_ids = [entry.get("id") for entry in entries]
    if entry_ids != expected_ids:
        raise AssertionError(f"Expected Batch 142 record IDs {expected_ids}, got {entry_ids}")

    total_nodes = 0
    total_edges = 0
    total_graph_quotes = 0
    for entry in entries:
        rec_id = entry["id"]
        if entry.get("status") != "reviewed":
            raise AssertionError(f"{rec_id} status must be 'reviewed', got {entry.get('status')}")
        if entry.get("record_sha256") != record_hashes.get(rec_id):
            raise AssertionError(
                f"{rec_id} record_sha256 mismatch: ledger={entry.get('record_sha256')} "
                f"vs disk={record_hashes.get(rec_id)}"
            )
        if entry.get("original_sha256") == entry.get("record_sha256"):
            raise AssertionError(f"{rec_id} was changed in Batch 142 so hashes must differ")

        record = records_by_id[rec_id]
        interactions = record.get("ecological_interactions") or []
        node_decisions = entry.get("node_decisions") or []
        if len(node_decisions) != len(interactions):
            raise AssertionError(
                f"{rec_id} node_decisions count {len(node_decisions)} != "
                f"record interactions {len(interactions)}"
            )

        for idx, (node, nd) in enumerate(zip(interactions, node_decisions, strict=True)):
            if nd.get("node") != node.get("name"):
                raise AssertionError(
                    f"{rec_id} node[{idx}] name mismatch: {nd.get('node')} != {node.get('name')}"
                )
            if nd.get("scope") != "COMMUNITY_LEVEL" or node.get("scope") != "COMMUNITY_LEVEL":
                raise AssertionError(f"{rec_id} node[{idx}] must have COMMUNITY_LEVEL scope")
            evs = node.get("evidence") or []
            if len(evs) < 2:
                raise AssertionError(f"{rec_id} node[{idx}] must have at least 2 EvidenceItems")
            norm_snippets: list[str] = []
            for ev in evs:
                snippet = ev.get("snippet", "")
                if "[" in snippet or "]" in snippet:
                    raise AssertionError(f"Bracketed text in {rec_id} snippet: {snippet}")
                ref = ev.get("reference", "")
                cache_text = ref_caches.get(ref, "")
                if not cache_text or not _snippet_matches(snippet, cache_text):
                    raise AssertionError(
                        f"Snippet does not match cached reference {ref} in {rec_id}: {snippet}"
                    )
                norm = " ".join(snippet.split())
                for prev in norm_snippets:
                    if norm in prev or prev in norm:
                        raise AssertionError(
                            f"Overlapping snippets in {rec_id} node {node.get('name')}: {snippet}"
                        )
                norm_snippets.append(norm)
                total_graph_quotes += 1
            total_nodes += 1

        record_edges = [
            {
                "source": node["name"],
                "target": edge["target"],
                "description": edge["description"],
            }
            for node in interactions
            for edge in (node.get("downstream") or [])
        ]
        if (entry.get("edges_after") or []) != record_edges:
            raise AssertionError(f"{rec_id} edges_after does not match record downstream edges")
        total_edges += len(record_edges)

        history = record.get("curation_history") or []
        if not history or history[-1].get("action") != "CURATE_CAUSAL_GRAPH":
            raise AssertionError(
                f"{rec_id} last curation_history action must be CURATE_CAUSAL_GRAPH"
            )

    counts = decision_data.get("reviewed_counts") or {}
    if counts.get("retained_nodes") != total_nodes:
        raise AssertionError(f"retained_nodes {counts.get('retained_nodes')} != {total_nodes}")
    if counts.get("retained_arrows") != total_edges:
        raise AssertionError(f"retained_arrows {counts.get('retained_arrows')} != {total_edges}")
    if counts.get("graph_quotations") != total_graph_quotes:
        raise AssertionError(
            f"graph_quotations {counts.get('graph_quotations')} != {total_graph_quotes}"
        )


def _load_real_inputs() -> tuple[dict, dict[str, dict], dict[str, str], dict[str, str]]:
    decision_data = yaml.safe_load(DECISION_FILE.read_text())
    records_by_id: dict[str, dict] = {}
    record_hashes: dict[str, str] = {}
    for entry in decision_data["records"]:
        path = REPO / entry["path"]
        records_by_id[entry["id"]] = yaml.safe_load(path.read_text())
        record_hashes[entry["id"]] = _sha256(path)
    ref_caches = {
        "PMID:41859451": (REPO / "references_cache/PMID_41859451.txt").read_text(),
        "PMID:42733304": (REPO / "references_cache/PMID_42733304.txt").read_text(),
    }
    return decision_data, records_by_id, record_hashes, ref_caches


def test_causal_review_batch142_contract_and_inventory() -> None:
    decision_data, records_by_id, record_hashes, ref_caches = _load_real_inputs()
    verify_batch142_contract(decision_data, records_by_id, record_hashes, ref_caches)

    for entry in decision_data["records"]:
        for hfile in entry["history_files"]:
            assert (REPO / hfile).is_file(), f"Missing history sidecar: {hfile}"

    summary = json.loads(SUMMARY_FILE.read_text())
    assert summary["records"] >= 519
    assert summary["nodes"] >= 1524
    assert summary["edges"] >= 590
    assert summary["review_status_counts"].get("reviewed", 0) >= 465
    assert summary["review_status_counts"].get("needs_research", 0) == 54
    assert summary["review_status_counts"].get("pending", 0) == 0
    assert summary["structural_defects"] == []

    inv_text = INVENTORY_FILE.read_text()
    for rec_id in (
        "CommunityMech:000522",
        "CommunityMech:000523",
        "CommunityMech:000524",
        "CommunityMech:000525",
    ):
        assert f"\t{rec_id}\t" in inv_text


def test_the_check_can_actually_fail() -> None:
    decision_data, records_by_id, record_hashes, ref_caches = _load_real_inputs()

    # 1. Control arm: unmutated copy passes
    verify_batch142_contract(
        copy.deepcopy(decision_data),
        copy.deepcopy(records_by_id),
        copy.deepcopy(record_hashes),
        copy.deepcopy(ref_caches),
    )

    # 2. Mutated arm A: corrupted SHA-256 hash in decision ledger fails
    mut_hashes = copy.deepcopy(record_hashes)
    mut_hashes["CommunityMech:000522"] = "0" * 64
    with pytest.raises(AssertionError, match="record_sha256 mismatch"):
        verify_batch142_contract(decision_data, records_by_id, mut_hashes, ref_caches)

    # 3. Mutated arm B: bracketed ellipsis in snippet fails
    mut_records_b = copy.deepcopy(records_by_id)
    mut_records_b["CommunityMech:000523"]["ecological_interactions"][0]["evidence"][0][
        "snippet"
    ] += " [...]"
    with pytest.raises(AssertionError, match="Bracketed text"):
        verify_batch142_contract(decision_data, mut_records_b, record_hashes, ref_caches)

    # 4. Mutated arm C: overlapping duplicate snippet on same node fails
    mut_records_c = copy.deepcopy(records_by_id)
    dup_snip = mut_records_c["CommunityMech:000524"]["ecological_interactions"][0]["evidence"][0][
        "snippet"
    ]
    mut_records_c["CommunityMech:000524"]["ecological_interactions"][0]["evidence"][1][
        "snippet"
    ] = dup_snip
    with pytest.raises(AssertionError, match="Overlapping snippets"):
        verify_batch142_contract(decision_data, mut_records_c, record_hashes, ref_caches)

    # 5. Mutated arm D: missing CURATE_CAUSAL_GRAPH history action fails
    mut_records_d = copy.deepcopy(records_by_id)
    mut_records_d["CommunityMech:000525"]["curation_history"][-1]["action"] = "CREATED"
    with pytest.raises(AssertionError, match="CURATE_CAUSAL_GRAPH"):
        verify_batch142_contract(decision_data, mut_records_d, record_hashes, ref_caches)
