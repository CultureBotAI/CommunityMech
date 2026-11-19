"""Actual source-bound near-tie addition controls for #2947, 2026-11-16."""

import copy
from pathlib import Path

import genus_gtdb_successors as registry
import pytest
import shrimp_lane_gtdb_successors as shrimp
import test_gtdb_near_tie_marker as near
import yaml
from test_scoped_gtdb_actual_successor import build_actual

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(params=["415", "416-archaea", "416-bacteria"])
def actual(tmp_path, monkeypatch, request):
    name, index, allowances = {
        "415": (near.ALGAL, 2, registry.ALLOWANCES),
        "416-archaea": (shrimp.THERMO_PATH, 0, shrimp.ALLOWANCES),
        "416-bacteria": (shrimp.THERMO_PATH, 1, shrimp.ALLOWANCES),
    }[request.param]
    allowed = allowances[name]
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
    return result, name, index


def block(root, name, index):
    return yaml.safe_load((root / name).read_bytes())["taxonomy"][index]["taxon_term"][
        "gtdb_classification"
    ]


def test_actual_reference_addition_requires_complete_proof(actual):
    (root, _, _, _, _), name, index = actual
    assert near._known_uncurated_near_tie(name, block(root, name, index))


@pytest.mark.parametrize(
    "field,value",
    [("total_genomes", 25), ("gtdb_id", "GTDB:p__Bacillota_A"), ("gtdb_id", "GTDB:p__Other")],
)
def test_changed_inspected_block_refuses_then_restores(actual, field, value):
    (root, _, _, _, _), name, index = actual
    original = block(root, name, index)
    assert near._known_uncurated_near_tie(name, original)
    changed = copy.deepcopy(original)
    if field == "gtdb_id" and value == original[field]:
        value = "GTDB:p__Methanobacteriota"
    changed[field] = value
    assert changed != original
    with pytest.raises(AssertionError, match="inspected near-tie block differs"):
        near._known_uncurated_near_tie(name, changed)
    assert near._known_uncurated_near_tie(name, original)


@pytest.mark.parametrize("artifact", ["current", "manifest", "native_recomputation"])
def test_changed_proof_bytes_refuse_then_restore(actual, artifact):
    (root, proof, allowed, _, _), name, index = actual
    original_block = block(root, name, index)
    assert near._known_uncurated_near_tie(name, original_block)
    if artifact == "current":
        path = root / name
    elif artifact == "manifest":
        path = root / allowed[name]["manifest"]["path"]
    else:
        path = root / proof[artifact]["path"]
    original = path.read_bytes()
    path.write_bytes(original + b"\n ")
    assert path.read_bytes() != original
    try:
        with pytest.raises(AssertionError):
            near._known_uncurated_near_tie(name, original_block)
    finally:
        path.write_bytes(original)
    assert near._known_uncurated_near_tie(name, original_block)


def test_unknown_non_bacillota_addition_is_not_silently_admitted(actual):
    (root, _, _, _, _), name, index = actual
    original = block(root, name, index)
    assert near._known_uncurated_near_tie(name, original)
    unknown = copy.deepcopy(original)
    unknown["gtdb_id"] = "GTDB:p__Methanobacteriota"
    assert not near._known_uncurated_near_tie("kb/communities/Unknown.yaml", unknown)
    assert near._known_uncurated_near_tie(name, original)
