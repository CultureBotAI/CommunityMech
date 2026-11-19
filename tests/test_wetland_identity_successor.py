"""Actual public471 identity proof, rehashed refusals and restoration, 2026-11-15.

No private snapshot or fresh scientific source is needed. Copies are confined
to pytest fixtures; the executed identity/mapping evidence stays immutable.
"""

import copy
import json
import subprocess
from pathlib import Path

import pytest
import wetland_identity_gtdb_successor as guard

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = (
    "reports/gtdb-wetland-identity-20261115/identity-evidence-001/471-identity-intermediate.json"
)
MANIFEST_SHA = "11fe5a66014a64bd7e329eb1a29a0c78aeb589605700ae967683a228da53c0af"
ORIGINAL_REVISION = "68699871415fda3c9eebf20382a315f9f3c7b17a"
# Fixture input only: the published native identity checkpoint, not a claim
# that ROOT has integrated it. A production composite must pin that maintained
# intermediate separately once the parent integration step is available.
IDENTITY_SOURCE_REVISION = "38f11cfac83036ed7e2feeea8cb19db74eed3306"


def artifact_paths(value):
    if isinstance(value, dict):
        if "path" in value and "sha256" in value:
            yield value["path"]
        for item in value.values():
            yield from artifact_paths(item)
    elif isinstance(value, list):
        for item in value:
            yield from artifact_paths(item)


@pytest.fixture
def identity_case(tmp_path):
    raw = (ROOT / MANIFEST).read_bytes()
    assert guard.mapping.digest(raw) == MANIFEST_SHA
    proof = json.loads(raw)
    names = set(artifact_paths(proof))
    names.add(guard.REFERENCE_IMPLEMENTATION_ARCHIVE)
    names.update(
        str(Path(module.__file__).resolve().relative_to(ROOT))
        for module in (
            guard.diagnostic,
            guard.diagnostic.identity,
            guard.diagnostic.measured,
            guard.diagnostic.measured.native,
            guard.publisher,
        )
    )
    retained = {name: (ROOT / name).read_bytes() for name in names}
    for name, content in retained.items():
        location = tmp_path / name
        location.parent.mkdir(parents=True, exist_ok=True)
        location.write_bytes(content)
    original, intermediate = (
        subprocess.run(
            ["git", "show", revision + ":" + guard.TARGET],
            cwd=ROOT,
            capture_output=True,
            check=True,
        ).stdout
        for revision in (ORIGINAL_REVISION, IDENTITY_SOURCE_REVISION)
    )
    assert guard.mapping.digest(original) == guard.BEFORE
    assert guard.mapping.digest(intermediate) == guard.INTERMEDIATE
    return tmp_path, proof, original, intermediate, retained


def verify(case):
    root, proof, original, intermediate, _retained = case
    artifacts = guard.mapping.Artifacts(root)
    review = guard.verify_identity(artifacts, proof, original, intermediate)
    artifacts.verify()
    return review


def test_actual_identity_chain_keeps_needs_curation_and_two_findings(identity_case):
    review = verify(identity_case)
    assert review["verdict"] == "needs_curation"
    assert review["scientific_review"] is False
    assert {row["issue_key"] for row in review["findings"]} == {
        "communitymech-2898",
        "communitymech-2899",
    }
    assert len(review["checks"]) == 10


def test_every_identity_manifest_artifact_is_in_git_with_exact_bytes():
    """Working-tree presence is insufficient for public recovery (#2922)."""
    proof = json.loads((ROOT / MANIFEST).read_bytes())
    for name in sorted(set(artifact_paths(proof))):
        result = subprocess.run(
            ["git", "show", ":" + name], cwd=ROOT, capture_output=True, check=False
        )
        assert result.returncode == 0, "manifest artifact missing from Git index: " + name
        assert result.stdout == (ROOT / name).read_bytes(), "Git artifact bytes differ: " + name


@pytest.mark.parametrize(
    "name",
    [
        "coverage",
        "native_exit",
        "measurement_exit",
        "wrong_target",
        "start_time",
        "outer_command",
        "wrong_after",
        "assertion_text",
        "cache_identity",
        "raw_digest",
        "sidecar",
        "plan",
    ],
)
def test_rehashed_public_identity_tampering_refuses_then_restores(identity_case, name):
    assert verify(identity_case)["verdict"] == "needs_curation"
    root, proof, _original, _intermediate, retained = identity_case
    saved = copy.deepcopy(proof)
    items = proof["reference_measurement"]
    if name in {"coverage", "native_exit", "wrong_target", "assertion_text", "cache_identity"}:
        item = items["measurement.json"]
    elif name in {"measurement_exit", "wrong_after"}:
        item = items["receipt.json"]
    elif name == "start_time":
        item = items["started.json"]
    elif name == "outer_command":
        item = proof["reference_commands"]["reference-measurement"]["json"]
    elif name == "raw_digest":
        item = items["measurement.json"]
        item["raw_sha256"] = "0" * 64
    elif name == "sidecar":
        item = proof["history_sidecar"]
    else:
        item = proof["source_plan"]
    location = root / item["path"]
    if name in {"sidecar", "plan"}:
        location.write_bytes(location.read_bytes() + b"\n ")
    elif name != "raw_digest":
        value = json.loads(location.read_bytes())
        if name == "coverage":
            value["assertion_coverage_complete"] = False
        elif name == "native_exit":
            value["native_exit_code"] = 1
        elif name == "wrong_target":
            value["records"][0]["record"] = "kb/communities/Other.yaml"
        elif name == "assertion_text":
            value["records"][0]["assertions"][0]["text_sha256"] = "0" * 64
        elif name == "cache_identity":
            value["records"][0]["assertions"][0]["cache"]["sha256"] = "0" * 64
        elif name == "measurement_exit":
            value["exit_code"] = 1
        elif name == "wrong_after":
            value["after_sha256"] = "0" * 64
        elif name == "start_time":
            value["started_at"] = "2099-01-01T00:00:00+00:00"
        elif name == "outer_command":
            value["command"][-1] += "-different"
        location.write_bytes(guard.encoded(value))
    item["sha256"] = guard.mapping.digest(location.read_bytes())
    # Mutations are real, with updated public hashes; refusal must concern
    # actual semantic/raw-link contracts rather than a stale outer digest.
    assert proof != saved
    with pytest.raises((AssertionError, ValueError)):
        verify(identity_case)
    for path, raw in retained.items():
        (root / path).write_bytes(raw)
    proof.clear()
    proof.update(saved)
    assert verify(identity_case)["verdict"] == "needs_curation"


def test_identity_snapshot_mutation_after_capture_is_refused(identity_case):
    root, proof, original, intermediate, retained = identity_case
    artifacts = guard.mapping.Artifacts(root)
    guard.verify_identity(artifacts, proof, original, intermediate)
    source = root / proof["source_plan"]["path"]
    source.write_bytes(source.read_bytes() + b"\n")
    with pytest.raises(AssertionError, match="changed during admission"):
        artifacts.verify()
    source.write_bytes(retained[proof["source_plan"]["path"]])
    artifacts.verify()
    assert verify(identity_case)["verdict"] == "needs_curation"
