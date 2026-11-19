"""Reviewed one-status application boundaries; no canonical fixture writes (#2848)."""

import copy
import importlib.util
import json
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parents[1]


@pytest.fixture
def harness(tmp_path, monkeypatch):
    source = REPO / "scripts/adhoc/apply_code006_gtdb_status_20261115.py"
    spec = importlib.util.spec_from_file_location("gtdb_apply_guard", source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    root = tmp_path / "repo"
    state = root / ".temp/gtdb-code006-20261115"
    stage = state / "stage"
    stage.mkdir(parents=True)
    target = root / module.TARGET
    target.parent.mkdir(parents=True)
    # Use a current valid record as a shape fixture, never an unavailable
    # historical Git object. The production baseline constant is not changed.
    before = yaml.safe_load((REPO / module.TARGET).read_bytes())
    before["taxonomy"][1]["taxon_term"].pop("gtdb_classification", None)
    before["taxonomy"][1]["taxon_term"]["gtdb_grounding_status"] = "UNRESOLVED"
    original = yaml.safe_dump(before, sort_keys=False).encode()
    target.write_bytes(original)
    native = root / "scripts/gtdb_ground.py"
    native.parent.mkdir()
    native.write_text("# immutable input fixture\n")
    source_input = root / "source.txt"
    source_input.write_text("reviewed source\n")
    after = copy.deepcopy(before)
    after["taxonomy"][1]["taxon_term"]["gtdb_grounding_status"] = "NOT_ATTEMPTED"
    event = module.record_curation_event(
        after,
        curator="gtdb_ground.py",
        action="GTDB_SET_STATUS",
        changes="Wrote gtdb_grounding_status on 1 taxonomy entries (#294, #395).",
        timestamp="2026-11-15T00:00:00Z",
    )
    candidate = stage / target.name
    candidate.write_text(yaml.safe_dump(after, sort_keys=False))
    candidate_sha = module.digest(candidate.read_bytes())
    receipt = {
        "code_revision": module.STAGING_REVISION,
        "canonical_apply": False,
        "exit_code": 0,
        "candidate_sha256": candidate_sha,
        "source_inputs_unchanged": True,
        "appended_native_inline_history": event,
        "inputs": {
            str(p.relative_to(root)): module.digest(p.read_bytes())
            for p in (target, native, source_input)
        },
    }
    receipt_path = stage / "receipt.json"
    receipt_path.write_text(json.dumps(receipt))
    receipt_sha = module.digest(receipt_path.read_bytes())
    monkeypatch.setattr(module, "ROOT", root)
    monkeypatch.setattr(module, "STATE", state)
    monkeypatch.setattr(module, "BASELINE", module.digest(original))
    monkeypatch.setattr(module, "current_head", lambda: "reviewed-execution-revision")
    return module, stage, target, source_input, candidate_sha, receipt_sha


def run(harness, **kwargs):
    module, stage, _target, _source, candidate_sha, receipt_sha = harness
    return module.apply(
        stage,
        stage.parent / "apply",
        candidate_sha,
        receipt_sha,
        "reviewed-execution-revision",
        **kwargs,
    )


def test_native_positive_persists_exact_reviewed_candidate(harness):
    module, stage, target, _source, candidate_sha, _receipt_sha = harness
    result = run(harness)
    assert result["applied"] is True
    assert module.digest(target.read_bytes()) == candidate_sha
    assert target.read_bytes() == (stage / target.name).read_bytes()
    assert (stage.parent / "apply/validated.yaml").stat().st_size > 0
    assert (stage.parent / "apply/receipt.json").stat().st_size > 0


def test_plan_leaves_no_outputs_or_canonical_change(harness):
    _module, stage, target, *_ = harness
    original = target.read_bytes()
    assert run(harness, plan=True)["planned"] is True
    assert target.read_bytes() == original
    assert not (stage.parent / "apply").exists()


def test_candidate_and_receipt_forgery_does_not_replace_external_hashes(harness):
    module, stage, target, *_ = harness
    original = target.read_bytes()
    candidate = stage / target.name
    candidate.write_bytes(candidate.read_bytes().replace(b"Mycobacterium", b"Otherbacterium"))
    receipt_path = stage / "receipt.json"
    receipt = json.loads(receipt_path.read_bytes())
    receipt["candidate_sha256"] = module.digest(candidate.read_bytes())
    receipt_path.write_text(json.dumps(receipt))
    with pytest.raises(ValueError, match="externally reviewed"):
        run(harness)
    assert target.read_bytes() == original


def test_wrong_baseline_refused(harness):
    _module, _stage, target, *_ = harness
    target.write_bytes(target.read_bytes() + b"# concurrent change\n")
    changed = target.read_bytes()
    with pytest.raises(ValueError, match="provenance differs"):
        run(harness)
    assert target.read_bytes() == changed


def test_stale_source_before_validation_refused(harness):
    _module, _stage, target, source, *_ = harness
    original = target.read_bytes()
    source.write_text("changed source\n")
    with pytest.raises(ValueError, match="reviewed input changed"):
        run(harness)
    assert target.read_bytes() == original


@pytest.mark.parametrize("change", ["source", "candidate", "canonical"])
def test_post_validation_changes_refused(harness, monkeypatch, change):
    module, stage, target, source, *_ = harness
    original = target.read_bytes()

    def controlled_validator(doc, path):
        path.write_text(yaml.safe_dump(doc))
        selected = {"source": source, "candidate": stage / target.name, "canonical": target}[change]
        selected.write_bytes(selected.read_bytes() + b"# changed during validation\n")

    monkeypatch.setattr(module, "write_validated_community", controlled_validator)
    with pytest.raises(ValueError, match="reviewed input changed|concurrent"):
        run(harness)
    assert not (stage.parent / "apply/receipt.json").exists()
    assert target.read_bytes() == original + (
        b"# changed during validation\n" if change == "canonical" else b""
    )
