"""Historical/current tracer bridge controls for #2957, 2026-11-16.

Only synthetic fixture copies are mutated. Original reviews, sources, receipt
hashes and scientific outcomes remain immutable; no native measurement is rerun.
"""

import ast
import copy
import inspect

import pytest
import wetland_identity_gtdb_successor as guard
import yaml
from test_wetland_identity_successor import identity_case, verify  # noqa: F401

SOURCE_PATHS = [guard.REFERENCE_IMPLEMENTATION_ARCHIVE, guard.REFERENCE_IMPLEMENTATION]


def test_only_unchanged_tracer_functions_are_used_for_historical_verification(
    identity_case,  # noqa: F811
):
    root = identity_case[0]
    old, current = [(root / name).read_bytes() for name in SOURCE_PATHS]
    assert old != current
    assert guard.mapping.digest(old) == guard.REFERENCE_HISTORICAL_SHA
    assert guard.mapping.digest(current) == guard.REFERENCE_SUCCESSOR_SHA
    trees = [
        {node.name: node for node in ast.parse(raw).body if isinstance(node, ast.FunctionDef)}
        for raw in (old, current)
    ]
    used = {"raw_reference", "snippet_surfaces"}
    for name in used:
        assert ast.dump(trees[0][name]) == ast.dump(trees[1][name])
    calls = {
        ast.unparse(node.func).removeprefix("measured.native.")
        for node in ast.walk(ast.parse(inspect.getsource(guard.diagnostic.verify_references)))
        if isinstance(node, ast.Call) and ast.unparse(node.func).startswith("measured.native.")
    }
    assert calls == used
    assert verify(identity_case)["scientific_review"] is False


@pytest.mark.parametrize("name", SOURCE_PATHS)
def test_changed_implementation_refuses_then_restores(identity_case, name):  # noqa: F811
    assert verify(identity_case)["verdict"] == "needs_curation"
    location = identity_case[0] / name
    original = location.read_bytes()
    try:
        location.write_bytes(original + b"\n# changed implementation\n")
        assert location.read_bytes() != original
        with pytest.raises(AssertionError, match="proof artifact hash differs"):
            verify(identity_case)
    finally:
        location.write_bytes(original)
    assert verify(identity_case)["verdict"] == "needs_curation"


@pytest.mark.parametrize("name", SOURCE_PATHS)
def test_missing_implementation_refuses_then_restores(identity_case, name):  # noqa: F811
    assert verify(identity_case)["verdict"] == "needs_curation"
    location = identity_case[0] / name
    original = location.read_bytes()
    try:
        location.unlink()
        with pytest.raises(FileNotFoundError):
            verify(identity_case)
    finally:
        location.write_bytes(original)
    assert verify(identity_case)["verdict"] == "needs_curation"


@pytest.mark.parametrize("name", SOURCE_PATHS)
def test_symlinked_implementation_refuses_then_restores(identity_case, name):  # noqa: F811
    assert verify(identity_case)["verdict"] == "needs_curation"
    root = identity_case[0]
    location = root / name
    original = location.read_bytes()
    copied = root / "other-source.txt"
    copied.write_bytes(original)
    try:
        location.unlink()
        location.symlink_to(copied)
        with pytest.raises(AssertionError, match="unsafe proof artifact path"):
            verify(identity_case)
    finally:
        location.unlink()
        location.write_bytes(original)
    assert verify(identity_case)["verdict"] == "needs_curation"


@pytest.mark.parametrize("name", SOURCE_PATHS)
def test_implementation_changed_after_capture_refuses_then_restores(
    identity_case, name  # noqa: F811
):
    root, proof, original, intermediate, _retained = identity_case
    artifacts = guard.mapping.Artifacts(root)
    guard.verify_identity(artifacts, proof, original, intermediate)
    artifacts.verify()
    location = root / name
    before = location.read_bytes()
    try:
        location.write_bytes(before + b"\n# replaced after capture\n")
        with pytest.raises(AssertionError, match="changed during admission"):
            artifacts.verify()
    finally:
        location.write_bytes(before)
    artifacts.verify()
    assert verify(identity_case)["verdict"] == "needs_curation"


def test_replacing_historical_review_hash_with_current_hash_refuses(identity_case):  # noqa: F811
    assert verify(identity_case)["verdict"] == "needs_curation"
    root, proof, _original, _intermediate, _retained = identity_case
    before_proof = copy.deepcopy(proof)
    item = proof["diagnostic_review"]
    location = root / item["path"]
    before = location.read_bytes()
    review = yaml.safe_load(before)
    old_input = next(
        row for row in review["source"]["inputs"] if row["path"] == guard.REFERENCE_IMPLEMENTATION
    )
    assert old_input["sha256"] == guard.REFERENCE_HISTORICAL_SHA
    old_input["sha256"] = guard.REFERENCE_SUCCESSOR_SHA
    try:
        location.write_text(yaml.safe_dump(review, sort_keys=False))
        item["sha256"] = guard.mapping.digest(location.read_bytes())
        with pytest.raises(AssertionError, match="exact historical tracer input required"):
            verify(identity_case)
    finally:
        location.write_bytes(before)
        proof.clear()
        proof.update(before_proof)
    assert verify(identity_case)["verdict"] == "needs_curation"


def test_wrong_execution_revision_refuses_then_restores(identity_case):  # noqa: F811
    assert verify(identity_case)["verdict"] == "needs_curation"
    proof = identity_case[1]
    original = proof["execution_revision"]
    try:
        proof["execution_revision"] = "0" * 40
        with pytest.raises(AssertionError, match="fixed identity intermediate required"):
            verify(identity_case)
    finally:
        proof["execution_revision"] = original
    assert verify(identity_case)["verdict"] == "needs_curation"
