"""Reject underscoped/stale post-curation gate substitutions (#2781), 2026-11-14."""

import importlib.util
from pathlib import Path

import pytest

SCRIPT = (
    Path(__file__).resolve().parents[1] / "scripts/adhoc/build_m5_postcuration_review_20261114.py"
)
REVISION = "a" * 40
OTHER_REVISION = "b" * 40
JUST = ["/opt/homebrew/bin/just", "--verbose", "--no-dotenv", "--color", "never"]


@pytest.fixture
def verifier(tmp_path, monkeypatch):
    spec = importlib.util.spec_from_file_location("m5_delta_builder", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.ROOT = tmp_path
    path = tmp_path / "validated-input.txt"
    path.write_bytes(b"frozen current input\n")
    monkeypatch.setattr(
        module.subprocess, "check_output", lambda *args, **kwargs: b"frozen current input\n"
    )
    return module


def receipt(command, revision=REVISION):
    return {"head": revision, "command": command, "exit_code": 0, "skip_markers": []}


def check(module, key, value):
    return module.verify_gate_binding(key, value, {}, REVISION, ["validated-input.txt"], set())


def test_full_scope_shared_controls_pass(verifier):
    for key, command in (
        ("all.history-all", JUST + ["validate-history"]),
        ("all.docs-current", JUST + ["check-docs-current"]),
        ("all.cache-tests", ["uv", "run", "pytest", *verifier.CACHE_TESTS, "-q"]),
        ("all.cache-tests", JUST + ["test"]),
    ):
        assert check(verifier, key, receipt(command))


@pytest.mark.parametrize(
    "key,command",
    [
        ("all.history-all", JUST + ["validate-history"]),
        ("all.docs-current", JUST + ["check-docs-current"]),
        ("all.cache-tests", JUST + ["test"]),
    ],
)
def test_every_shared_gate_rejects_wrong_revision(verifier, key, command):
    with pytest.raises(ValueError, match="revision differs"):
        check(verifier, key, receipt(command, OTHER_REVISION))


def test_single_record_history_is_not_all_history(verifier):
    with pytest.raises(ValueError, match="exact unscoped"):
        check(
            verifier,
            "all.history-all",
            receipt(JUST + ["validate-history", "history/records/EcoFAB_Ring_Trial_SynCom17"]),
        )


@pytest.mark.parametrize(
    "selection",
    [
        [
            "tests/test_no_new_bracketed_snippets.py::test_unchanged_asgard_nife_quote_matches_its_committed_article",
            "-q",
        ],
        ["tests/test_cache_supplements.py", "-q"],
        [],
    ],
)
def test_wrong_pytest_canary_is_not_cache_scope(verifier, selection):
    with pytest.raises(ValueError, match="required full test scope"):
        check(verifier, "all.cache-tests", receipt(["uv", "run", "pytest", *selection]))


def test_shared_gate_rejects_current_input_drift(verifier):
    (verifier.ROOT / "validated-input.txt").write_bytes(b"changed input\n")
    with pytest.raises(ValueError, match="validation input changed"):
        check(verifier, "all.docs-current", receipt(JUST + ["check-docs-current"]))


def test_failed_qc_test_stage_is_not_pass(verifier):
    value = receipt(JUST + ["qc-references"])
    value.update(exit_code=1, stages=[{"recipe": "test", "status": "FAILED"}])
    assert not check(verifier, "all.cache-tests", value)
    value["stages"] = [
        {"recipe": "test", "status": "PASSED"},
        {"recipe": "validate-all", "status": "FAILED"},
    ]
    assert check(verifier, "all.cache-tests", value)
