"""Regression and mutation-proof gate for Cycle 12 Stage 2 Batch 144 causal-graph review."""

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
BATCH144_LEDGER = (
    ROOT
    / "reports"
    / "causal_graph_review"
    / "decisions"
    / "20261108-stage2-five-records-batch144.yaml"
)

EXPECTED_BATCH144_RECORDS = {
    "CommunityMech:000531": {
        "path": "data/isolates/Microbacterium_BR1_Sulfadiazine_Cleaving_Isolate_Baseline.yaml",
        "original_sha256": "149a6ab7149a19719ff9e73f58a650b744327ec2306350af2f495cbd85e81531",
        "record_sha256": "c0326c5cdaf678c922659c33dbe4fe1b5717be2bf79dab54d672f160574c0fe5",
        "nodes": 1,
        "edges": 0,
        "evidence_count": 5,
    },
    "CommunityMech:000532": {
        "path": "data/isolates/Terrabacter_2APm3_Sulfadiazine_Isolate_Baseline.yaml",
        "original_sha256": "677193069c629cbbecdaad6e13fb53881e3ead1c644725acab370fe1cfdd2b5c",
        "record_sha256": "81c8fd983bc57050595d7a4d51b64acdf2617ce9fea0f03f7ec9db4fa617c05e",
        "nodes": 1,
        "edges": 0,
        "evidence_count": 5,
    },
    "CommunityMech:000533": {
        "path": "data/isolates/Achromobacter_SL8_Cadmium_Immobilization_Isolate_Baseline.yaml",
        "original_sha256": "9570a1bcd8115e59d8dedd2a31760f6acccdbb030f0d98f5670cd0af203c556f",
        "record_sha256": "0680fbc0c1ee94f3a79ce13d9c6b3d8b91317022addca4c095195a37974b6d0e",
        "nodes": 1,
        "edges": 0,
        "evidence_count": 6,
    },
    "CommunityMech:000534": {
        "path": "data/isolates/Enterobacter_SL12_Cadmium_Immobilization_Isolate_Baseline.yaml",
        "original_sha256": "e35dcd4e7772a4525d707fe454bdd188c2500e8bfc8024fb1ec0d989b290cb0f",
        "record_sha256": "68a2f6ea9b523e7db0eacf6ef1a87af5227cd3f6c7e93be14facffc265232796",
        "nodes": 1,
        "edges": 0,
        "evidence_count": 6,
    },
    "CommunityMech:000535": {
        "path": "kb/communities/Ogataea_Str3_Leu2_Auxotrophic_CrossFeeding_Coculture.yaml",
        "original_sha256": "cf4a1289c42b61654ff9fa1407a55cad4bf9b22f0c829235b26c8705c2ffe282",
        "record_sha256": "be16aa69ef1611a0d1d452da9e20ccea58a5497d912ce167819f706fdb57a401",
        "nodes": 1,
        "edges": 0,
        "evidence_count": 6,
    },
}


def validate_batch144_entry(review: dict, doc: dict, digest: str) -> None:
    """Validate a single Batch 144 review entry against its record and SHA-256."""
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


def test_batch144_ledger_matches_curated_records() -> None:
    """Verify Batch 144 ledger covers 000531-000535 with exact hashes and evidence counts."""
    assert BATCH144_LEDGER.is_file(), f"Missing Batch 144 ledger: {BATCH144_LEDGER}"
    ledger = yaml.safe_load(BATCH144_LEDGER.read_text(encoding="utf-8"))
    records = ledger["records"]
    assert [r["id"] for r in records] == list(EXPECTED_BATCH144_RECORDS)
    indexed = index_reviews(records)
    assert len(indexed) == 5

    for row in records:
        rec_id = row["id"]
        expected = EXPECTED_BATCH144_RECORDS[rec_id]
        assert row["path"] == expected["path"]
        assert row["original_sha256"] == expected["original_sha256"]
        assert row["record_sha256"] == expected["record_sha256"]

        yaml_path = ROOT / row["path"]
        digest = hashlib.sha256(yaml_path.read_bytes()).hexdigest()
        assert digest == expected["record_sha256"]
        doc = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))

        validate_batch144_entry(row, doc, digest)

        nodes = doc.get("ecological_interactions") or []
        edges = [e for n in nodes for e in (n.get("downstream") or [])]
        assert len(nodes) == expected["nodes"]
        assert len(edges) == expected["edges"]
        assert len(nodes[0]["evidence"]) == expected["evidence_count"]


def test_the_check_can_actually_fail() -> None:
    """Prove validate_batch144_entry fails across 5 distinct mutation arms after a green control."""
    ledger = yaml.safe_load(BATCH144_LEDGER.read_text(encoding="utf-8"))
    sample_review = yaml.safe_load(yaml.safe_dump(ledger["records"][0]))
    sample_path = ROOT / sample_review["path"]
    sample_digest = hashlib.sha256(sample_path.read_bytes()).hexdigest()
    sample_doc = yaml.safe_load(sample_path.read_text(encoding="utf-8"))

    # Control arm: unmutated copy passes cleanly.
    validate_batch144_entry(sample_review, sample_doc, sample_digest)

    # Mutation arm 1: stale record_sha256 turns review_status into 'stale'.
    mut_review_hash = yaml.safe_load(yaml.safe_dump(sample_review))
    mut_review_hash["record_sha256"] = "0" * 64
    assert mut_review_hash["record_sha256"] != sample_digest
    with pytest.raises(ValueError, match="Expected status 'reviewed'"):
        validate_batch144_entry(mut_review_hash, sample_doc, sample_digest)

    # Mutation arm 2: blank node rationale is rejected by review_status.
    mut_review_rationale = yaml.safe_load(yaml.safe_dump(sample_review))
    mut_review_rationale["node_decisions"][0]["rationale"] = "   "
    with pytest.raises(ValueError, match="Blank node rationale"):
        validate_batch144_entry(mut_review_rationale, sample_doc, sample_digest)

    # Mutation arm 3: removing CURATE_CAUSAL_GRAPH from curation_history is rejected.
    mut_doc_history = yaml.safe_load(yaml.safe_dump(sample_doc))
    mut_doc_history["curation_history"] = [
        ev
        for ev in mut_doc_history["curation_history"]
        if ev.get("action") != "CURATE_CAUSAL_GRAPH"
    ]
    with pytest.raises(ValueError, match="Missing CURATE_CAUSAL_GRAPH"):
        validate_batch144_entry(sample_review, mut_doc_history, sample_digest)

    # Mutation arm 4: bracketed text in an interaction snippet is rejected.
    mut_doc_bracket = yaml.safe_load(yaml.safe_dump(sample_doc))
    mut_doc_bracket["ecological_interactions"][0]["evidence"][0]["snippet"] += " [1]"
    with pytest.raises(ValueError, match="Bracket character found"):
        validate_batch144_entry(sample_review, mut_doc_bracket, sample_digest)

    # Mutation arm 5: empty source_backed_gaps is rejected.
    mut_review_gaps = yaml.safe_load(yaml.safe_dump(sample_review))
    mut_review_gaps["source_backed_gaps"] = []
    with pytest.raises(ValueError, match="Missing source_backed_gaps"):
        validate_batch144_entry(mut_review_gaps, sample_doc, sample_digest)

    # Restore verification: original inputs remain valid immediately after all mutations.
    validate_batch144_entry(sample_review, sample_doc, sample_digest)
