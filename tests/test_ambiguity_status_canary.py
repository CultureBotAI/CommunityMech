"""Prove the #2848 canary retains biology and complete alternatives, 2026-11-15."""

import copy
import hashlib
import importlib.util
import subprocess
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "ambiguity_canary", ROOT / "scripts/adhoc/stage_ambiguity_status_canary_20261115.py"
)
CANARY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CANARY)


def pair():
    raw = subprocess.check_output(
        ["git", "show", "68699871415fda3c9eebf20382a315f9f3c7b17a:" + CANARY.RECORD], cwd=ROOT
    )
    assert hashlib.sha256(raw).hexdigest() == CANARY.BEFORE
    before = yaml.safe_load(raw)
    after = copy.deepcopy(before)
    term = after["taxonomy"][0]["taxon_term"]
    term["gtdb_grounding_status"] = "AMBIGUOUS"
    term["gtdb_candidates"] = CANARY.OPTIONS.copy()
    after["curation_history"].append({"action": "GTDB_SET_STATUS"})
    CANARY.verify_semantics(before, after)
    return before, after


def test_fixture_ignores_changed_current_record(monkeypatch):
    _, changed = pair()
    changed_raw = yaml.safe_dump(changed).encode()
    target = ROOT / CANARY.RECORD
    original_reader = Path.read_bytes
    monkeypatch.setattr(
        Path, "read_bytes", lambda path: changed_raw if path == target else original_reader(path)
    )
    before, after = pair()
    assert before["taxonomy"][0]["taxon_term"]["gtdb_grounding_status"] == "UNRESOLVED"
    CANARY.verify_semantics(before, after)


@pytest.mark.parametrize(
    "mutation", ["one_species", "missing_candidate", "stock", "biology", "old_history"]
)
def test_guard_refuses_scope_drift_and_restores(mutation):
    before, after = pair()
    changed = copy.deepcopy(after)
    term = changed["taxonomy"][0]["taxon_term"]
    if mutation == "one_species":
        term["gtdb_grounding_status"] = "GROUNDED"
        term["gtdb_classification"] = {"gtdb_id": CANARY.OPTIONS[0]}
    elif mutation == "missing_candidate":
        term["gtdb_candidates"].pop()
    elif mutation == "stock":
        changed["taxonomy"][0]["strain_designation"]["strain_name"] = "different stock"
    elif mutation == "biology":
        changed["ecological_interactions"][0]["evidence"][0]["snippet"] = "invented evidence"
    else:
        changed["curation_history"][0]["changes"] = "rewritten history"
    assert changed != after
    with pytest.raises(ValueError):
        CANARY.verify_semantics(before, changed)
    CANARY.verify_semantics(before, after)
