"""Exercise exact candidate/event/input refusal for #2848, 2026-11-15."""

import copy
import importlib.util
import json
import subprocess
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "ambiguity_apply", ROOT / "scripts/adhoc/apply_ambiguity_status_canary_20261115.py"
)
APPLY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(APPLY)


def setup_case(tmp_path, monkeypatch):
    original = subprocess.check_output(
        ["git", "show", "68699871415fda3c9eebf20382a315f9f3c7b17a:" + APPLY.stage.RECORD], cwd=ROOT
    )
    assert APPLY.sha(original) == APPLY.stage.BEFORE
    before = yaml.safe_load(original)
    after = copy.deepcopy(before)
    term = after["taxonomy"][0]["taxon_term"]
    term["gtdb_grounding_status"] = "AMBIGUOUS"
    term["gtdb_candidates"] = APPLY.stage.OPTIONS.copy()
    event = APPLY.record_curation_event(
        after,
        curator="gtdb_ground.py",
        action="GTDB_SET_STATUS",
        changes="Wrote gtdb_grounding_status on 1 taxonomy entries (#294, #395).",
        timestamp="2026-11-15T05:54:19Z",
    )
    canonical = tmp_path / APPLY.stage.RECORD
    canonical.parent.mkdir(parents=True)
    canonical.write_bytes(original)
    private = tmp_path / APPLY.STATE
    staging = private / "candidate-001"
    staging.mkdir(parents=True)
    candidate = staging / canonical.name
    candidate.write_text(yaml.safe_dump(after))
    input_name = "scripts/adhoc/stage_ambiguity_status_canary_20261115.py"
    copied_stager = tmp_path / input_name
    copied_stager.parent.mkdir(parents=True)
    copied_stager.write_bytes(APPLY.STAGER.read_bytes())
    for relative in (
        "src/communitymech/validation/write_validated.py",
        "src/communitymech/schema/communitymech.yaml",
        "src/communitymech/curate/curation_event.py",
    ):
        path = tmp_path / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes((ROOT / relative).read_bytes())
    for filename, raw in (
        ("native.log", b"actual native command fixture\n"),
        ("native.exit", b"0\n"),
        ("candidate.diff", b"fixture diff\n"),
    ):
        (staging / filename).write_bytes(raw)
    revision = "1" * 40
    proof = {
        "record": APPLY.stage.RECORD,
        "record_id": "CommunityMech:000546",
        "candidate_sha256": APPLY.sha(candidate.read_bytes()),
        "canonical_apply": False,
        "native_exit_code": 0,
        "execution_revision": revision,
        "source_inputs_unchanged": True,
        "inputs": {input_name: APPLY.sha(copied_stager.read_bytes())},
        "native_log_sha256": APPLY.sha((staging / "native.log").read_bytes()),
        "native_exit_sha256": APPLY.sha((staging / "native.exit").read_bytes()),
        "diff_sha256": APPLY.sha((staging / "candidate.diff").read_bytes()),
        "appended_native_inline_history": event,
    }
    receipt = staging / "receipt.json"
    receipt.write_text(json.dumps(proof))
    monkeypatch.setattr(APPLY, "ROOT", tmp_path)
    monkeypatch.setattr(APPLY, "STAGER", copied_stager)
    monkeypatch.setattr(APPLY, "head", lambda: revision)
    # The applier's own source is captured too, under the isolated checkout.
    self_path = tmp_path / "scripts/adhoc/apply_ambiguity_status_canary_20261115.py"
    self_path.write_bytes(Path(APPLY.__file__).read_bytes())
    monkeypatch.setattr(APPLY, "__file__", str(self_path))
    monkeypatch.setattr(
        APPLY, "write_validated_community", lambda doc, path: path.write_text(yaml.safe_dump(doc))
    )
    return candidate, receipt, canonical, copied_stager, revision, before, after, proof


def test_complete_native_event_is_required(tmp_path, monkeypatch):
    *_, before, after, proof = setup_case(tmp_path, monkeypatch)
    APPLY.verify_candidate(before, after, proof)
    changed = copy.deepcopy(after)
    changed["curation_history"][-1]["curator"] = "invented attribution"
    forged = copy.deepcopy(proof)
    forged["appended_native_inline_history"] = changed["curation_history"][-1]
    with pytest.raises(ValueError, match="full native event"):
        APPLY.verify_candidate(before, changed, forged)
    APPLY.verify_candidate(before, after, proof)


def test_fixture_ignores_changed_current_record(tmp_path, monkeypatch):
    target = ROOT / APPLY.stage.RECORD
    original_reader = Path.read_bytes
    changed = yaml.safe_load(original_reader(target))
    changed["taxonomy"][0]["taxon_term"]["gtdb_grounding_status"] = "AMBIGUOUS"
    changed_raw = yaml.safe_dump(changed).encode()
    assert APPLY.sha(changed_raw) != APPLY.stage.BEFORE
    monkeypatch.setattr(
        Path, "read_bytes", lambda path: changed_raw if path == target else original_reader(path)
    )
    _, _, canonical, _, _, before, *_ = setup_case(tmp_path, monkeypatch)
    assert APPLY.sha(canonical.read_bytes()) == APPLY.stage.BEFORE
    assert before["taxonomy"][0]["taxon_term"]["gtdb_grounding_status"] == "UNRESOLVED"


def test_source_change_during_validation_refuses_apply_and_restores(tmp_path, monkeypatch):
    candidate, receipt, canonical, source, revision, *_ = setup_case(tmp_path, monkeypatch)
    original, source_raw = canonical.read_bytes(), source.read_bytes()
    args = (candidate, APPLY.sha(candidate.read_bytes()), APPLY.sha(receipt.read_bytes()))
    positive = tmp_path / APPLY.STATE / "positive"
    APPLY.execute(*args, positive, revision)
    assert (positive / "receipt.json").is_file() and canonical.read_bytes() == original

    def mutating_validator(doc, path):
        path.write_text(yaml.safe_dump(doc))
        source.write_bytes(source_raw + b"\n# changed during validation\n")

    monkeypatch.setattr(APPLY, "write_validated_community", mutating_validator)
    rejected = tmp_path / APPLY.STATE / "rejected"
    with pytest.raises(ValueError, match="input changed"):
        APPLY.execute(*args, rejected, revision, apply=True)
    assert source.read_bytes() != source_raw
    assert canonical.read_bytes() == original and not (rejected / "receipt.json").exists()
    source.write_bytes(source_raw)
    monkeypatch.setattr(
        APPLY, "write_validated_community", lambda doc, path: path.write_text(yaml.safe_dump(doc))
    )
    restored = tmp_path / APPLY.STATE / "restored"
    result = APPLY.execute(*args, restored, revision, apply=True)
    assert result["applied"] is True and canonical.read_bytes() == candidate.read_bytes()
