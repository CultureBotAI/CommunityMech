"""Actual source-bound near-tie addition controls for #2947, 2026-11-16."""

import copy
from pathlib import Path

import genus_gtdb_successors as registry
import pytest
import test_gtdb_near_tie_marker as near
import yaml
from test_scoped_gtdb_actual_successor import build_actual

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def actual(tmp_path, monkeypatch):
    allowed = registry.ALLOWANCES[near.ALGAL]
    result = build_actual(
        tmp_path,
        monkeypatch,
        proof_root=ROOT,
        manifest=allowed["manifest"]["path"],
        manifest_sha=allowed["manifest"]["sha256"],
        baseline_revision=allowed["baseline_revision"],
        historical_llm=True,
    )
    monkeypatch.setattr(near, "REPO", tmp_path)
    return result


def block(root):
    return yaml.safe_load((root / near.ALGAL).read_bytes())["taxonomy"][2]["taxon_term"][
        "gtdb_classification"
    ]


def test_actual_13_of_24_reference_addition_requires_complete_proof(actual):
    root, _, _, _, _ = actual
    assert near._known_uncurated_near_tie(near.ALGAL, block(root))


@pytest.mark.parametrize("field,value", [("total_genomes", 25), ("gtdb_id", "GTDB:p__Bacillota_A")])
def test_changed_inspected_block_refuses_then_restores(actual, field, value):
    root, _, _, _, _ = actual
    original = block(root)
    assert near._known_uncurated_near_tie(near.ALGAL, original)
    changed = copy.deepcopy(original)
    changed[field] = value
    assert changed != original
    with pytest.raises(AssertionError, match="inspected near-tie block differs"):
        near._known_uncurated_near_tie(near.ALGAL, changed)
    assert near._known_uncurated_near_tie(near.ALGAL, original)


@pytest.mark.parametrize("artifact", ["current", "manifest", "native_recomputation"])
def test_changed_proof_bytes_refuse_then_restore(actual, artifact):
    root, proof, allowed, _, _ = actual
    original_block = block(root)
    assert near._known_uncurated_near_tie(near.ALGAL, original_block)
    if artifact == "current":
        path = root / near.ALGAL
    elif artifact == "manifest":
        path = root / allowed[near.ALGAL]["manifest"]["path"]
    else:
        path = root / proof[artifact]["path"]
    original = path.read_bytes()
    path.write_bytes(original + b"\n ")
    assert path.read_bytes() != original
    try:
        with pytest.raises(AssertionError):
            near._known_uncurated_near_tie(near.ALGAL, original_block)
    finally:
        path.write_bytes(original)
    assert near._known_uncurated_near_tie(near.ALGAL, original_block)


def test_unknown_non_bacillota_addition_is_not_silently_admitted(actual):
    root, _, _, _, _ = actual
    original = block(root)
    assert near._known_uncurated_near_tie(near.ALGAL, original)
    assert not near._known_uncurated_near_tie("kb/communities/Unknown.yaml", original)
    assert near._known_uncurated_near_tie(near.ALGAL, original)
