"""Protect historical biology while the actual first successor is staged (#2848)."""

import copy
from pathlib import Path

import batch147_genus_successor as successor
import pytest
from test_code006_isolate_genus_candidate import candidate  # noqa: F401

ROOT = Path(__file__).resolve().parents[1]


def target(before):
    return next(path for path, row in successor.TARGETS.items() if row[0] == before["id"])


def test_exact_scoped_mapping_preserves_scientific_projection(candidate):  # noqa: F811
    _stage, _native, before, after, _block, _row = candidate
    successor.unchanged_science(before, after, target(before))


@pytest.mark.parametrize("field", ["graph", "quote", "identity", "count", "history", "curated"])
def test_rehashed_biology_or_unreviewed_mapping_cannot_be_admitted(candidate, field):  # noqa: F811
    _stage, _native, before, after, _block, _row = candidate
    original = copy.deepcopy(after)
    path = target(before)
    successor.unchanged_science(before, after, path)
    if field == "graph":
        after["ecological_interactions"][0]["description"] += " Invented mechanism."
    elif field == "quote":
        after["taxonomy"][0]["evidence"][0]["snippet"] += " Invented evidence."
    elif field == "identity":
        after["taxonomy"][0]["taxon_term"]["term"]["id"] = "NCBITaxon:2"
    elif field == "count":
        after["taxonomy"][0]["taxon_term"]["gtdb_classification"]["total_genomes"] += 1
    elif field == "history":
        after["curation_history"][0]["changes"] = "Rewritten historical event"
    else:
        after["taxonomy"][0]["taxon_term"]["gtdb_classification"]["curated"] = True
    assert after != original
    with pytest.raises(AssertionError):
        successor.unchanged_science(before, after, path)
    successor.unchanged_science(before, original, path)


def test_other_record_has_no_successor_allowance(tmp_path):
    with pytest.raises(AssertionError, match="other batch147"):
        successor.current_record_sha256(
            tmp_path, "data/isolates/other.yaml", "0" * 64, current=b"changed"
        )


def test_changed_selected_record_requires_actual_proof(candidate):  # noqa: F811
    _stage, _native, before, after, _block, _row = candidate
    path = target(before)
    old = successor.historical_bytes(ROOT, path)
    assert successor.current_record_sha256(
        ROOT, path, successor.digest(old), current=old
    ) == successor.digest(old)
    import yaml

    with pytest.raises(AssertionError):
        successor.current_record_sha256(
            ROOT,
            path,
            successor.digest(old),
            current=yaml.safe_dump(after).encode(),
            manifest={"records": []},
        )


def test_immutable_before_arm_does_not_read_changed_current_file(candidate, tmp_path):  # noqa: F811
    _stage, _native, before, _after, _block, _row = candidate
    path = target(before)
    old = successor.historical_bytes(ROOT, path)
    current = tmp_path / path
    current.parent.mkdir(parents=True)
    current.write_bytes(b"current canonical deliberately differs\n")
    assert current.read_bytes() != old
    assert successor.current_record_sha256(
        tmp_path, path, successor.digest(old), current=old
    ) == successor.digest(old)
