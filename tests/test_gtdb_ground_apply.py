"""Regression tests for `gtdb_ground.py --apply`'s insertion positioning.

`apply_to_community` keyed its blocks by bare NCBITaxon id and inserted at the
first line bearing that id. Records may legitimately list one id many times —
`GLBRC_Populus_Variovorax_SynCom28` has 28 isolates all grounded to
NCBITaxon:34072 (genus *Variovorax*) — so the block landed on a *different*
taxonomy entry than the one that needed it. When the first occurrence was
already grounded, that entry got a second `gtdb_classification` key while the
27 that needed one stayed empty.

Neither symptom was visible downstream: PyYAML keeps the last of two duplicate
keys silently, so `linkml-validate` passed, and the under-grounding just looked
like taxa GTDB could not map. It was caught only by comparing blocks written
(28) against grounded taxa gained (17).

These tests patch `resolve_target` so they exercise the positioning logic alone
and need no kg-microbe checkout — the mapping table is a 2.9 MB gzip that is not
present in CI.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import gtdb_ground  # noqa: E402

GROUNDED_BLOCK = {
    "gtdb_id": "GTDB:g__Variovorax",
    "gtdb_taxon": "Variovorax",
    "gtdb_lineage": "d__Bacteria;p__Pseudomonadota;g__Variovorax",
    "ncbi_source_id": "NCBITaxon:34072",
    "majority_fraction": 0.99,
    "is_reclassified": False,
    "mapping_source": "test",
}


def _entry(preferred: str, grounded: bool) -> str:
    block = (
        "\n".join(
            [
                "    gtdb_classification:",
                *[f"      {k}: {v}" for k, v in GROUNDED_BLOCK.items()],
            ]
        )
        + "\n"
        if grounded
        else ""
    )
    return (
        f"- taxon_term:\n"
        f"    preferred_term: {preferred}\n"
        f"    term:\n"
        f"      id: NCBITaxon:34072\n"
        f"      label: Variovorax\n"
        f"{block}"
    )


def _write_community(tmp_path: Path, grounded_flags: list[bool]) -> Path:
    entries = "\n".join(_entry(f"Variovorax isolate {i}", g) for i, g in enumerate(grounded_flags))
    path = tmp_path / "Repeated_Id.yaml"
    path.write_text(f"id: CommunityMech:000001\nname: Repeated id record\ntaxonomy:\n{entries}\n")
    return path


@pytest.fixture
def always_grounds(monkeypatch):
    """Make every taxon resolve, so only the positioning logic is under test."""
    monkeypatch.setattr(
        gtdb_ground,
        "resolve_target",
        lambda ncbi_id, label, by_id, by_name, by_higher: {
            "gtdb_id": GROUNDED_BLOCK["gtdb_id"],
            "gtdb_taxon": GROUNDED_BLOCK["gtdb_taxon"],
            "gtdb_lineage": GROUNDED_BLOCK["gtdb_lineage"],
            "ncbi_source_id": GROUNDED_BLOCK["ncbi_source_id"],
            "majority_fraction": GROUNDED_BLOCK["majority_fraction"],
            "is_reclassified": GROUNDED_BLOCK["is_reclassified"],
            "via": "ncbi_id",
        },
    )


def _apply(path: Path) -> int:
    return gtdb_ground.apply_to_community(path, {}, {}, {}, "test")


def _count_keys(path: Path) -> int:
    """Count `gtdb_classification:` keys textually — parsing hides duplicates."""
    return sum(
        1 for line in path.read_text().splitlines() if line.strip() == "gtdb_classification:"
    )


def _count_grounded(path: Path) -> int:
    doc = yaml.safe_load(path.read_text())
    return sum(bool(t["taxon_term"].get("gtdb_classification")) for t in doc["taxonomy"])


def test_repeated_id_grounds_the_entry_that_needs_it(tmp_path, always_grounds):
    """First entry already grounded, second not: the block goes to the second.

    This is the exact shape that produced the bug — keying by id sent the block
    to the first occurrence, duplicating it there.
    """
    path = _write_community(tmp_path, [True, False])

    assert _apply(path) == 1
    assert _count_keys(path) == 2, "one block per entry, not a duplicate on the first"
    assert _count_grounded(path) == 2

    doc = yaml.safe_load(path.read_text())
    assert (
        doc["taxonomy"][1]["taxon_term"]["gtdb_classification"]["gtdb_id"] == "GTDB:g__Variovorax"
    )


def test_every_ungrounded_entry_of_a_repeated_id_is_grounded(tmp_path, always_grounds):
    """The 28-isolate case: one grounded, many not — all of them get a block."""
    path = _write_community(tmp_path, [True] + [False] * 27)

    assert _apply(path) == 27
    assert _count_keys(path) == 28
    assert _count_grounded(path) == 28


def test_apply_is_idempotent(tmp_path, always_grounds):
    """Re-running must add nothing — the second pass is where duplicates appeared."""
    path = _write_community(tmp_path, [False, False])

    assert _apply(path) == 2
    before = path.read_text()
    assert _apply(path) == 0
    assert path.read_text() == before, "a second --apply changed the file"
    assert _count_keys(path) == 2


def test_refuses_to_edit_when_anchors_do_not_line_up(tmp_path, always_grounds):
    """A stray NCBITaxon id/label pair makes positions ambiguous — bail, don't guess.

    Inserting at a wrong offset is silent corruption, so the script must fail
    loudly rather than pick an interpretation.
    """
    path = _write_community(tmp_path, [False])
    path.write_text(
        path.read_text() + "    decoy:\n      id: NCBITaxon:99999\n      label: Decoy\n"
    )

    with pytest.raises(SystemExit, match="refusing to edit"):
        _apply(path)
