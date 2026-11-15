"""Actual471 two-leg proof fixture and unchanged mapping controls, 2026-11-15.

The intermediate is the published identity source checkpoint, not an asserted
ROOT integration. No production registry/caller is enabled by this fixture.
"""

import copy
import subprocess

import pytest
import wetland_identity_gtdb_successor as guard
from test_scoped_gtdb_actual_successor import (
    build_actual,
    test_actual_rehashed_tampering_refuses_and_restores,  # noqa: F401
    test_actual_shared_engine_successor_admits_and_retains_old_history,  # noqa: F401
)
from test_wetland_identity_successor import (
    IDENTITY_SOURCE_REVISION,
    MANIFEST,
    MANIFEST_SHA,
    ORIGINAL_REVISION,
    ROOT,
    identity_case,  # noqa: F401
)

MAPPING_MANIFEST = "reports/gtdb-wetland-mapping-20261115/471-mapping-001-successor.json"
MAPPING_SHA = "0e043890bd5c2df05f3ff350d877af65461a00755e0394da770a2db7e7b52889"


@pytest.fixture
def actual(tmp_path, monkeypatch):
    return build_actual(
        tmp_path,
        monkeypatch,
        proof_root=ROOT,
        manifest=MAPPING_MANIFEST,
        manifest_sha=MAPPING_SHA,
        baseline_revision=IDENTITY_SOURCE_REVISION,
        historical_llm=True,
    )


@pytest.fixture
def composed(actual, identity_case, monkeypatch):  # noqa: F811
    root, mapping_proof, _mapping_allowed, _retained, _historical_llm = actual
    assert identity_case[0] == root
    identity_raw = (ROOT / MANIFEST).read_bytes()
    identity_path = root / MANIFEST
    identity_path.parent.mkdir(parents=True, exist_ok=True)
    identity_path.write_bytes(identity_raw)
    proof = {
        "target": guard.TARGET,
        "before_sha256": guard.BEFORE,
        "intermediate_revision": IDENTITY_SOURCE_REVISION,
        "intermediate_sha256": guard.INTERMEDIATE,
        "after_sha256": mapping_proof["after_sha256"],
        "scientific_review": False,
        "identity_manifest": {"path": MANIFEST, "sha256": MANIFEST_SHA},
        "mapping_allowance": {
            "baseline_revision": IDENTITY_SOURCE_REVISION,
            "manifest": {"path": MAPPING_MANIFEST, "sha256": MAPPING_SHA},
        },
    }
    name = "reports/gtdb-wetland-mapping-20261115/471-composite-fixture.json"
    raw = guard.encoded(proof)
    (root / name).write_bytes(raw)
    allowed = {
        guard.TARGET: {
            "baseline_revision": ORIGINAL_REVISION,
            "manifest": {"path": name, "sha256": guard.mapping.digest(raw)},
        }
    }

    def actual_git(command, *, cwd, **kwargs):
        assert cwd == root
        assert command[:2] == ["git", "show"] and command[2] in {
            ORIGINAL_REVISION + ":" + guard.TARGET,
            IDENTITY_SOURCE_REVISION + ":" + guard.TARGET,
        }
        return subprocess.run(command, cwd=ROOT, capture_output=True, check=True, **kwargs).stdout

    monkeypatch.setattr(guard.notes.subprocess, "check_output", actual_git)
    return root, proof, allowed, identity_case


def admit(case):
    root, _proof, allowed, _identity_case = case
    return guard.admit(root, guard.TARGET, guard.BEFORE, allowed)


def repin(case):
    root, proof, allowed, _identity_case = case
    item = allowed[guard.TARGET]["manifest"]
    raw = guard.encoded(proof)
    (root / item["path"]).write_bytes(raw)
    item["sha256"] = guard.mapping.digest(raw)


def test_actual_two_leg_chain_returns_original_history(composed):
    result = admit(composed)
    assert result.changed
    assert result.current_sha256 == composed[1]["after_sha256"]
    assert result.historical_bytes == composed[3][2]
    assert result.historical_bytes != composed[3][3]


@pytest.mark.parametrize("field", ["intermediate_revision", "identity_manifest"])
def test_composite_wrong_transition_refuses_then_restores(composed, field):
    assert admit(composed).changed
    _root, proof, _allowed, _identity_case = composed
    original = copy.deepcopy(proof)
    if field == "intermediate_revision":
        proof[field] = ORIGINAL_REVISION
        proof["mapping_allowance"]["baseline_revision"] = ORIGINAL_REVISION
    else:
        proof[field]["sha256"] = "0" * 64
    repin(composed)
    with pytest.raises(AssertionError):
        admit(composed)
    proof.clear()
    proof.update(original)
    repin(composed)
    assert admit(composed).changed


def test_composite_unknown_target_refuses(composed):
    root, _proof, allowed, _identity_case = composed
    with pytest.raises(AssertionError, match="unknown identity-mapping"):
        guard.admit(
            root, "kb/communities/Unreviewed.yaml", guard.BEFORE, allowed, current=b"changed"
        )
    assert admit(composed).changed
