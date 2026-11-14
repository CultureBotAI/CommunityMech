"""Mutation controls for the explicit M5 predecessor/successor chain (#2782)."""

from copy import deepcopy
from pathlib import Path

import pytest
import yaml
from m5_review_successor import (
    assert_cache_successor,
    assert_header_only_cache_change,
    current_record_sha256,
    load_provenance,
    original,
)

ROOT = Path(__file__).resolve().parents[1]


def record_case(identifier):
    provenance = load_provenance(ROOT)
    successor = next(row for row in provenance["records"] if row["id"] == identifier)
    predecessor = ROOT / successor["supersedes_review"]["review_file"]
    row = next(
        row for row in yaml.safe_load(predecessor.read_text())["records"] if row["id"] == identifier
    )
    return provenance, predecessor, row


@pytest.mark.parametrize(
    "identifier", ["CommunityMech:000025", "CommunityMech:000515", "CommunityMech:000516"]
)
def test_reviewed_successor_chain_and_current_record_mutation(identifier):
    provenance, predecessor, row = record_case(identifier)
    current_record_sha256(ROOT, predecessor, row, provenance=provenance)
    with pytest.raises(AssertionError):
        current_record_sha256(
            ROOT,
            predecessor,
            row,
            provenance=provenance,
            current=(ROOT / row["path"]).read_bytes() + b"\n# unreviewed change\n",
        )


@pytest.mark.parametrize("mutation", ["predecessor", "receipt", "review", "current_digest"])
def test_broken_successor_bindings_are_rejected(mutation):
    provenance, predecessor, row = record_case("CommunityMech:000516")
    changed = deepcopy(provenance)
    successor = next(item for item in changed["records"] if item["id"] == row["id"])
    if mutation == "predecessor":
        successor["supersedes_review"]["record_sha256"] = "0" * 64
    elif mutation == "receipt":
        successor["curation_receipts"][0]["sha256"] = "0" * 64
    elif mutation == "review":
        successor["scientific_review"]["sha256"] = "0" * 64
    else:
        successor["record_sha256"] = "0" * 64
    with pytest.raises(AssertionError):
        current_record_sha256(ROOT, predecessor, row, provenance=changed)


def test_all_header_corrections_preserve_exact_article_bodies_and_identity():
    for correction in load_provenance(ROOT)["cache_corrections"]:
        path = correction["path"]
        previous = original(ROOT, path)
        current = (ROOT / path).read_bytes()
        assert_cache_successor(ROOT, path, correction["original_sha256"])
        with pytest.raises(AssertionError, match="article body changed"):
            assert_header_only_cache_change(previous, current + b"\nChanged source body.\n")
        with pytest.raises(AssertionError, match="cache identity"):
            assert_header_only_cache_change(
                previous, current.replace(b"reference_id:", b"wrong_reference_id:", 1)
            )


def test_cache_chain_rejects_a_wrong_predecessor_or_receipt():
    provenance = load_provenance(ROOT)
    correction = provenance["cache_corrections"][0]
    with pytest.raises(AssertionError):
        assert_cache_successor(ROOT, correction["path"], "0" * 64)
    changed = deepcopy(provenance)
    changed["cache_corrections"][0]["receipt"]["sha256"] = "0" * 64
    with pytest.raises(AssertionError):
        assert_cache_successor(
            ROOT, correction["path"], correction["original_sha256"], provenance=changed
        )
