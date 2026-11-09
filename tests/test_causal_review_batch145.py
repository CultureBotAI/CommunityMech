"""Regression and mutation-proof gate for Cycle 13 Stage 2 Batch 145 causal-graph review."""

from __future__ import annotations

import hashlib
import importlib.util
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "causal_review_inventory", ROOT / "reports/causal_graph_review/build_inventory.py"
)
assert SPEC is not None and SPEC.loader is not None
_inventory = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(_inventory)
index_reviews = _inventory.index_reviews
review_status = _inventory.review_status
BATCH145_LEDGER = (
    ROOT
    / "reports"
    / "causal_graph_review"
    / "decisions"
    / "20261109-stage2-six-records-batch145.yaml"
)

EXPECTED_BATCH145_RECORDS = {
    "CommunityMech:000536": {
        "path": "data/isolates/Pseudomonas_ZM1_Prometryn_Degrading_Isolate_Baseline.yaml",
        "original_sha256": "67480cb95671fc3ac087c6c939796a7898089493ea3eddb23904f4efa9d83807",
        "record_sha256": "e600a10abb5375a5f013fd189c67d16b0ae8cedebc1032c5c28526f206e786f1",
        "nodes": 1,
        "edges": 0,
        "evidence_counts": [6],
    },
    "CommunityMech:000537": {
        "path": "data/isolates/Achromobacter_ZM2_Prometryn_Degrading_Isolate_Baseline.yaml",
        "original_sha256": "e023b1735aa37a14b5a81a476d44c5c69c767224be161e2b19a27e93983a2821",
        "record_sha256": "1473199ef62f7ecfc0cef4a07469f452050a512ce973c24ddc0d049587feeb7e",
        "nodes": 1,
        "edges": 0,
        "evidence_counts": [6],
    },
    "CommunityMech:000538": {
        "path": "data/isolates/Stenotrophomonas_ZM3_Prometryn_Degrading_Isolate_Baseline.yaml",
        "original_sha256": "ce4fa1d8c26084c9eb66071499a18a0409b1c23533a33719b2cd66eae421fac4",
        "record_sha256": "d8d5b3564c9a94a868e278f7d04b23999b02ddfeda1e72b89495ec8402a35fa3",
        "nodes": 1,
        "edges": 0,
        "evidence_counts": [6],
    },
    "CommunityMech:000539": {
        "path": (
            "data/isolates/" "Rhodopseudomonas_Palustris_CGA676_Anaerobic_Monoculture_Baseline.yaml"
        ),
        "original_sha256": "72a714951fe8ddd79e3108b4a78595ec4e707f1d241dd236193278303eddf310",
        "record_sha256": "ad02b70b47aa8cd86d7949e08c3ce23366c1caec6c5463c74cd45a9396aac666",
        "nodes": 1,
        "edges": 0,
        "evidence_counts": [7],
    },
    "CommunityMech:000540": {
        "path": "data/isolates/Escherichia_Coli_PFM2_Anaerobic_Monoculture_Baseline.yaml",
        "original_sha256": "7a3ddab08e70b1b6f4313a05174481162fa5a3851695be97d08a36402f2243de",
        "record_sha256": "991e85326303854835a6a7481d1599e068f4d67411856fbb8092620953919b18",
        "nodes": 1,
        "edges": 0,
        "evidence_counts": [7],
    },
    "CommunityMech:000541": {
        "path": (
            "kb/communities/"
            "Rhodopseudomonas_CGA676_Ecoli_PFM2_DeltaPurH_Adenine_Competition_Coculture.yaml"
        ),
        "original_sha256": "f9225d426a29b1ed835f59723f18ab950e21c6ba210605c344319b361f303895",
        "record_sha256": "19eb2a05854e12882277cdc6646edf9f9c5fc91f4392cc080fc2b09bcb9b0382",
        "nodes": 2,
        "edges": 1,
        "evidence_counts": [4, 5],
    },
}


def validate_batch145_entry(review: dict, doc: dict, digest: str) -> None:
    """Validate a single Batch 145 review entry against its record and SHA-256."""
    status = review_status(doc, digest, review)
    if status != "reviewed":
        raise ValueError(f"Expected status 'reviewed' for {doc['id']}, got {status!r}")
    curation_actions = [ev.get("action") for ev in (doc.get("curation_history") or [])]
    if "CURATE_CAUSAL_GRAPH" not in curation_actions:
        raise ValueError(f"Missing CURATE_CAUSAL_GRAPH curation event in {doc['id']}")
    nodes = doc.get("ecological_interactions") or []
    for node in nodes:
        for ev in node.get("evidence") or []:
            snip = ev.get("snippet", "")
            if "[" in snip or "]" in snip:
                raise ValueError(f"Bracket character found in snippet of {doc['id']}: {snip!r}")
    if not review.get("source_backed_gaps"):
        raise ValueError(f"Missing source_backed_gaps on {doc['id']}")


def test_batch145_ledger_matches_curated_records() -> None:
    """Verify Batch 145 ledger covers 000536-000541 with exact hashes and evidence counts."""
    assert BATCH145_LEDGER.is_file(), f"Missing Batch 145 ledger: {BATCH145_LEDGER}"
    ledger = yaml.safe_load(BATCH145_LEDGER.read_text(encoding="utf-8"))
    records = ledger["records"]
    assert [r["id"] for r in records] == list(EXPECTED_BATCH145_RECORDS)
    indexed = index_reviews(records)
    assert len(indexed) == 6

    for row in records:
        rec_id = row["id"]
        expected = EXPECTED_BATCH145_RECORDS[rec_id]
        assert row["path"] == expected["path"]
        assert row["original_sha256"] == expected["original_sha256"]
        assert row["record_sha256"] == expected["record_sha256"]

        yaml_path = ROOT / row["path"]
        digest = hashlib.sha256(yaml_path.read_bytes()).hexdigest()
        assert digest == expected["record_sha256"]
        doc = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))

        validate_batch145_entry(row, doc, digest)

        nodes = doc.get("ecological_interactions") or []
        edges = [e for n in nodes for e in (n.get("downstream") or [])]
        assert len(nodes) == expected["nodes"]
        assert len(edges) == expected["edges"]
        assert [len(n["evidence"]) for n in nodes] == expected["evidence_counts"]


def test_the_check_can_actually_fail() -> None:
    """Prove validate_batch145_entry fails across 5 distinct mutation arms after a green control."""
    ledger = yaml.safe_load(BATCH145_LEDGER.read_text(encoding="utf-8"))
    sample_review = yaml.safe_load(yaml.safe_dump(ledger["records"][5]))
    sample_path = ROOT / sample_review["path"]
    sample_digest = hashlib.sha256(sample_path.read_bytes()).hexdigest()
    sample_doc = yaml.safe_load(sample_path.read_text(encoding="utf-8"))

    # Control arm: unmutated copy passes cleanly.
    validate_batch145_entry(sample_review, sample_doc, sample_digest)

    # Mutation arm 1: stale record_sha256 turns review_status into 'stale'.
    mut_review_hash = yaml.safe_load(yaml.safe_dump(sample_review))
    mut_review_hash["record_sha256"] = "0" * 64
    assert mut_review_hash["record_sha256"] != sample_digest
    with pytest.raises(ValueError, match="Expected status 'reviewed'"):
        validate_batch145_entry(mut_review_hash, sample_doc, sample_digest)

    # Mutation arm 2: blank node rationale is rejected by review_status.
    mut_review_rationale = yaml.safe_load(yaml.safe_dump(sample_review))
    mut_review_rationale["node_decisions"][0]["rationale"] = "   "
    with pytest.raises(ValueError, match="Blank node rationale"):
        validate_batch145_entry(mut_review_rationale, sample_doc, sample_digest)

    # Mutation arm 3: removing CURATE_CAUSAL_GRAPH from curation_history is rejected.
    mut_doc_history = yaml.safe_load(yaml.safe_dump(sample_doc))
    mut_doc_history["curation_history"] = [
        ev
        for ev in mut_doc_history["curation_history"]
        if ev.get("action") != "CURATE_CAUSAL_GRAPH"
    ]
    with pytest.raises(ValueError, match="Missing CURATE_CAUSAL_GRAPH"):
        validate_batch145_entry(sample_review, mut_doc_history, sample_digest)

    # Mutation arm 4: bracketed text in an interaction snippet is rejected.
    mut_doc_bracket = yaml.safe_load(yaml.safe_dump(sample_doc))
    mut_doc_bracket["ecological_interactions"][0]["evidence"][0]["snippet"] += " [1]"
    with pytest.raises(ValueError, match="Bracket character found"):
        validate_batch145_entry(sample_review, mut_doc_bracket, sample_digest)

    # Mutation arm 5: empty source_backed_gaps is rejected.
    mut_review_gaps = yaml.safe_load(yaml.safe_dump(sample_review))
    mut_review_gaps["source_backed_gaps"] = []
    with pytest.raises(ValueError, match="Missing source_backed_gaps"):
        validate_batch145_entry(mut_review_gaps, sample_doc, sample_digest)

    # Restore verification: original inputs remain valid immediately after all mutations.
    validate_batch145_entry(sample_review, sample_doc, sample_digest)
