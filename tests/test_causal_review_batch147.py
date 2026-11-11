"""Regression and mutation-proof gate for Cycle 15 Stage 2 Batch 147 causal-graph review."""

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
BATCH147_LEDGER = (
    ROOT
    / "reports"
    / "causal_graph_review"
    / "decisions"
    / "20261110-stage2-seven-records-batch147.yaml"
)

EXPECTED_BATCH147_RECORDS = {
    "CommunityMech:000549": {
        "path": "data/isolates/Bacillus_Paramycoides_B81_PAH_Biodegradation_Isolate_Baseline.yaml",
        "original_sha256": "a1862a927c0ca56a7e40609f59363639ed5a26d069fa5b7bd2c99eb3b58d6d6c",
        "record_sha256": "cb226c9c70b14d042991de11ef4a7b3677790ffd8a93549332e213dc4946b04e",
        "nodes": 1,
        "edges": 0,
        "evidence_counts": [5],
    },
    "CommunityMech:000550": {
        "path": "data/isolates/Bacillus_Paranthracis_A1_PAH_Biofilm_Isolate_Baseline.yaml",
        "original_sha256": "00fd3bda9890bf7019498d875a3232c172626e73b843154abad6c87839917440",
        "record_sha256": "3b4fa9c9579fe2f3c0b94f2c1c55ec6b8f36bb5e22d4c5f9718aeb798cc15988",
        "nodes": 1,
        "edges": 0,
        "evidence_counts": [5],
    },
    "CommunityMech:000551": {
        "path": "data/isolates/Bacillus_Licheniformis_A3_PAH_Biofilm_Isolate_Baseline.yaml",
        "original_sha256": "41dbfbc369e49f004c9db2f31dcb3191c3a65eaca5d2b96fb6d6d85d456521c8",
        "record_sha256": "de118e18969d2bfaddac33e51e49d5481ec224427441cf90d1faa5c18438d73b",
        "nodes": 1,
        "edges": 0,
        "evidence_counts": [5],
    },
    "CommunityMech:000552": {
        "path": (
            "data/isolates/Pelagerythrobacter_N7_Halophilic_Pyrene_Oxidation_Isolate_Baseline.yaml"
        ),
        "original_sha256": "114c68f88dd909ca39612f3b4929585abad575a980eecdf98f14d74ed10f683f",
        "record_sha256": "16d14ed3792a286afedaa4f17ba1c1773ebb04c6a7e8fc622cb7d946ce4c9610",
        "nodes": 1,
        "edges": 0,
        "evidence_counts": [5],
    },
    "CommunityMech:000553": {
        "path": (
            "data/isolates/"
            "Salinicola_A11_Halophilic_Bioemulsifier_Decarboxylase_Isolate_Baseline.yaml"
        ),
        "original_sha256": "a23fb3d2c224143a308222c8f06715211d6ab811eb37245f74c1cda08ed8f526",
        "record_sha256": "82b65eee0a1216e8a26c875a17206c3060b2304223a3eac2fcb1171de79aee4b",
        "nodes": 1,
        "edges": 0,
        "evidence_counts": [5],
    },
    "CommunityMech:000554": {
        "path": (
            "data/isolates/"
            "Rhizorhabdus_Wittichii_YL_JM2C_BDE47_Dioxygenase_Isolate_Baseline.yaml"
        ),
        "original_sha256": "f1dc3f787b96588c6145262ee6f8b19d872536d1f8ecd880e35cddd869e97af7",
        "record_sha256": "e70a8434bd8db3852302899814f08a19d97c0e9d73a6636cb7715295642fdf59",
        "nodes": 1,
        "edges": 0,
        "evidence_counts": [5],
    },
    "CommunityMech:000555": {
        "path": (
            "data/isolates/Cupriavidus_Necator_JMP134_24DBP_Hydroxylase_Isolate_Baseline.yaml"
        ),
        "original_sha256": "c97c0c57afa5f49062a9a7a0e61cc029fe7ed08161103118847a340fa836e9b8",
        "record_sha256": "429964cbf945c41b2e89b57a072718158cf674e03786ef34b1ef96fe9247995e",
        "nodes": 1,
        "edges": 0,
        "evidence_counts": [5],
    },
}


def validate_batch147_entry(review: dict, doc: dict, digest: str) -> None:
    """Validate a single Batch 147 review entry against its record and SHA-256."""
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


def test_batch147_ledger_matches_curated_records() -> None:
    """Verify Batch 147 ledger covers 000549-000555 with exact hashes and evidence counts."""
    assert BATCH147_LEDGER.is_file(), f"Missing Batch 147 ledger: {BATCH147_LEDGER}"
    ledger = yaml.safe_load(BATCH147_LEDGER.read_text(encoding="utf-8"))
    records = ledger["records"]
    assert [r["id"] for r in records] == list(EXPECTED_BATCH147_RECORDS)
    indexed = index_reviews(records)
    assert len(indexed) == 7

    for row in records:
        rec_id = row["id"]
        expected = EXPECTED_BATCH147_RECORDS[rec_id]
        assert row["path"] == expected["path"]
        assert row["original_sha256"] == expected["original_sha256"]
        assert row["record_sha256"] == expected["record_sha256"]

        yaml_path = ROOT / row["path"]
        digest = hashlib.sha256(yaml_path.read_bytes()).hexdigest()
        assert digest == expected["record_sha256"]
        doc = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))

        validate_batch147_entry(row, doc, digest)

        nodes = doc.get("ecological_interactions") or []
        edges = [e for n in nodes for e in (n.get("downstream") or [])]
        assert len(nodes) == expected["nodes"]
        assert len(edges) == expected["edges"]
        assert [len(n["evidence"]) for n in nodes] == expected["evidence_counts"]


def test_the_check_can_actually_fail() -> None:
    """Prove validate_batch147_entry fails across 5 distinct mutation arms after a green control."""
    ledger = yaml.safe_load(BATCH147_LEDGER.read_text(encoding="utf-8"))
    sample_review = yaml.safe_load(yaml.safe_dump(ledger["records"][6]))
    sample_path = ROOT / sample_review["path"]
    sample_digest = hashlib.sha256(sample_path.read_bytes()).hexdigest()
    sample_doc = yaml.safe_load(sample_path.read_text(encoding="utf-8"))

    # Control arm: unmutated copy passes cleanly.
    validate_batch147_entry(sample_review, sample_doc, sample_digest)

    # Mutation arm 1: stale record_sha256 turns review_status into 'stale'.
    mut_review_hash = yaml.safe_load(yaml.safe_dump(sample_review))
    mut_review_hash["record_sha256"] = "0" * 64
    assert mut_review_hash["record_sha256"] != sample_digest
    with pytest.raises(ValueError, match="Expected status 'reviewed'"):
        validate_batch147_entry(mut_review_hash, sample_doc, sample_digest)

    # Mutation arm 2: blank node rationale is rejected by review_status.
    mut_review_rationale = yaml.safe_load(yaml.safe_dump(sample_review))
    mut_review_rationale["node_decisions"][0]["rationale"] = "   "
    with pytest.raises(ValueError, match="Blank node rationale"):
        validate_batch147_entry(mut_review_rationale, sample_doc, sample_digest)

    # Mutation arm 3: removing CURATE_CAUSAL_GRAPH from curation_history is rejected.
    mut_doc_history = yaml.safe_load(yaml.safe_dump(sample_doc))
    mut_doc_history["curation_history"] = [
        ev
        for ev in mut_doc_history["curation_history"]
        if ev.get("action") != "CURATE_CAUSAL_GRAPH"
    ]
    with pytest.raises(ValueError, match="Missing CURATE_CAUSAL_GRAPH"):
        validate_batch147_entry(sample_review, mut_doc_history, sample_digest)

    # Mutation arm 4: bracketed text in an interaction snippet is rejected.
    mut_doc_bracket = yaml.safe_load(yaml.safe_dump(sample_doc))
    mut_doc_bracket["ecological_interactions"][0]["evidence"][0]["snippet"] += " [1]"
    with pytest.raises(ValueError, match="Bracket character found"):
        validate_batch147_entry(sample_review, mut_doc_bracket, sample_digest)

    # Mutation arm 5: empty source_backed_gaps is rejected.
    mut_review_gaps = yaml.safe_load(yaml.safe_dump(sample_review))
    mut_review_gaps["source_backed_gaps"] = []
    with pytest.raises(ValueError, match="Missing source_backed_gaps"):
        validate_batch147_entry(mut_review_gaps, sample_doc, sample_digest)

    # Restore verification: original inputs remain valid immediately after all mutations.
    validate_batch147_entry(sample_review, sample_doc, sample_digest)
