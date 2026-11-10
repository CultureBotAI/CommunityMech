"""Regression and mutation-proof gate for Cycle 14 Stage 2 Batch 146 causal-graph review."""

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
BATCH146_LEDGER = (
    ROOT
    / "reports"
    / "causal_graph_review"
    / "decisions"
    / "20261110-stage2-seven-records-batch146.yaml"
)

EXPECTED_BATCH146_RECORDS = {
    "CommunityMech:000542": {
        "path": "data/isolates/Escherichia_Coli_GL10_Glucose_D_Lactate_Isolate_Baseline.yaml",
        "original_sha256": "12e55314ccdfb2fdf6753f3c22654d25670a6e2d5fcd84209a503506fbe7c19c",
        "record_sha256": "a747c09cf287a252aa4e8fc66485fd6aa337d320cb7903c8a92d101a44855dc0",
        "nodes": 1,
        "edges": 0,
        "evidence_counts": [6],
    },
    "CommunityMech:000543": {
        "path": "data/isolates/Escherichia_Coli_XL12_Xylose_D_Lactate_Isolate_Baseline.yaml",
        "original_sha256": "f5573eb7c8d6718b478066b8fb6952e6a759ddd3db8632a67cee971342b96bf0",
        "record_sha256": "c19c097c6068fa07ecdd2e9533d2d6a2225637a5a594ff14b21ef3a86f6d2e9f",
        "nodes": 1,
        "edges": 0,
        "evidence_counts": [6],
    },
    "CommunityMech:000544": {
        "path": "data/isolates/Escherichia_Coli_XL5_PTS_Deficient_D_Lactate_Isolate_Baseline.yaml",
        "original_sha256": "2c8b31a3d82c238314608825e0308d7ca16c350d8bb26db99d2e9c07f3976585",
        "record_sha256": "4105ae978347925a7541a5bd66f6ceadc35bd4bda35683f70bffca35b36ab79f",
        "nodes": 1,
        "edges": 0,
        "evidence_counts": [6],
    },
    "CommunityMech:000545": {
        "path": "data/isolates/Bifidobacterium_Bifidum_JCM1254_2FL_FOS_Monoculture_Baseline.yaml",
        "original_sha256": "188b2c8b44448da8a202bcf02736499ce936f3b1f3710d9d84219fa8c2eafabe",
        "record_sha256": "8190e352c3a803e85e2ab6b64a1791a6f14b2ea93dab2173c1ef653ea9e0a216",
        "nodes": 1,
        "edges": 0,
        "evidence_counts": [5],
    },
    "CommunityMech:000546": {
        "path": (
            "data/isolates/" "Faecalibacterium_Prausnitzii_A2_165_2FL_FOS_Monoculture_Baseline.yaml"
        ),
        "original_sha256": "7a4f13515e398c841e8d9289b276f3ebcfaa3480fa8ac130c1d7607747645019",
        "record_sha256": "b6dc768bf6f705611933fc50882d91957225ef1e32c61330e1adb717fe175790",
        "nodes": 1,
        "edges": 0,
        "evidence_counts": [5],
    },
    "CommunityMech:000547": {
        "path": (
            "data/isolates/"
            "Ramichloridium_Apiculatum_CMS1_Wollastonite_Bioleaching_Isolate_Baseline.yaml"
        ),
        "original_sha256": "3335d6f85de2f74993a0939861ec17b507e879891fca3cc5413193c072a33e8d",
        "record_sha256": "51488eb2b3634242b8e7d7f0a455f24d58cda968242831f830c1e10dfae9fded",
        "nodes": 1,
        "edges": 0,
        "evidence_counts": [6],
    },
    "CommunityMech:000548": {
        "path": (
            "data/isolates/"
            "Talaromyces_Pseudofuniculosus_Hzt3_Wollastonite_Bioleaching_Isolate_Baseline.yaml"
        ),
        "original_sha256": "e669bcf94e266f41adb84d0a3fd3b6b1977b4e6908cbce5197c4834dccaafb1f",
        "record_sha256": "209e5fe1388451b952502b2ca65a621d155e8d6542a0095152fe2d6935bf716f",
        "nodes": 1,
        "edges": 0,
        "evidence_counts": [6],
    },
}


def validate_batch146_entry(review: dict, doc: dict, digest: str) -> None:
    """Validate a single Batch 146 review entry against its record and SHA-256."""
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


def test_batch146_ledger_matches_curated_records() -> None:
    """Verify Batch 146 ledger covers 000542-000548 with exact hashes and evidence counts."""
    assert BATCH146_LEDGER.is_file(), f"Missing Batch 146 ledger: {BATCH146_LEDGER}"
    ledger = yaml.safe_load(BATCH146_LEDGER.read_text(encoding="utf-8"))
    records = ledger["records"]
    assert [r["id"] for r in records] == list(EXPECTED_BATCH146_RECORDS)
    indexed = index_reviews(records)
    assert len(indexed) == 7

    for row in records:
        rec_id = row["id"]
        expected = EXPECTED_BATCH146_RECORDS[rec_id]
        assert row["path"] == expected["path"]
        assert row["original_sha256"] == expected["original_sha256"]
        assert row["record_sha256"] == expected["record_sha256"]

        yaml_path = ROOT / row["path"]
        digest = hashlib.sha256(yaml_path.read_bytes()).hexdigest()
        assert digest == expected["record_sha256"]
        doc = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))

        validate_batch146_entry(row, doc, digest)

        nodes = doc.get("ecological_interactions") or []
        edges = [e for n in nodes for e in (n.get("downstream") or [])]
        assert len(nodes) == expected["nodes"]
        assert len(edges) == expected["edges"]
        assert [len(n["evidence"]) for n in nodes] == expected["evidence_counts"]


def test_the_check_can_actually_fail() -> None:
    """Prove validate_batch146_entry fails across 5 distinct mutation arms after a green control."""
    ledger = yaml.safe_load(BATCH146_LEDGER.read_text(encoding="utf-8"))
    sample_review = yaml.safe_load(yaml.safe_dump(ledger["records"][6]))
    sample_path = ROOT / sample_review["path"]
    sample_digest = hashlib.sha256(sample_path.read_bytes()).hexdigest()
    sample_doc = yaml.safe_load(sample_path.read_text(encoding="utf-8"))

    # Control arm: unmutated copy passes cleanly.
    validate_batch146_entry(sample_review, sample_doc, sample_digest)

    # Mutation arm 1: stale record_sha256 turns review_status into 'stale'.
    mut_review_hash = yaml.safe_load(yaml.safe_dump(sample_review))
    mut_review_hash["record_sha256"] = "0" * 64
    assert mut_review_hash["record_sha256"] != sample_digest
    with pytest.raises(ValueError, match="Expected status 'reviewed'"):
        validate_batch146_entry(mut_review_hash, sample_doc, sample_digest)

    # Mutation arm 2: blank node rationale is rejected by review_status.
    mut_review_rationale = yaml.safe_load(yaml.safe_dump(sample_review))
    mut_review_rationale["node_decisions"][0]["rationale"] = "   "
    with pytest.raises(ValueError, match="Blank node rationale"):
        validate_batch146_entry(mut_review_rationale, sample_doc, sample_digest)

    # Mutation arm 3: removing CURATE_CAUSAL_GRAPH from curation_history is rejected.
    mut_doc_history = yaml.safe_load(yaml.safe_dump(sample_doc))
    mut_doc_history["curation_history"] = [
        ev
        for ev in mut_doc_history["curation_history"]
        if ev.get("action") != "CURATE_CAUSAL_GRAPH"
    ]
    with pytest.raises(ValueError, match="Missing CURATE_CAUSAL_GRAPH"):
        validate_batch146_entry(sample_review, mut_doc_history, sample_digest)

    # Mutation arm 4: bracketed text in an interaction snippet is rejected.
    mut_doc_bracket = yaml.safe_load(yaml.safe_dump(sample_doc))
    mut_doc_bracket["ecological_interactions"][0]["evidence"][0]["snippet"] += " [1]"
    with pytest.raises(ValueError, match="Bracket character found"):
        validate_batch146_entry(sample_review, mut_doc_bracket, sample_digest)

    # Mutation arm 5: empty source_backed_gaps is rejected.
    mut_review_gaps = yaml.safe_load(yaml.safe_dump(sample_review))
    mut_review_gaps["source_backed_gaps"] = []
    with pytest.raises(ValueError, match="Missing source_backed_gaps"):
        validate_batch146_entry(mut_review_gaps, sample_doc, sample_digest)

    # Restore verification: original inputs remain valid immediately after all mutations.
    validate_batch146_entry(sample_review, sample_doc, sample_digest)
