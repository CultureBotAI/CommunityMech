"""Review regression: candidate+manifest forgery and validation-time source drift.

The temporary root is an isolated toy repository surface; native closed-schema
validation still runs. Namespace injection supplies the reviewed external digests
to both the old (ignoring them) and repaired main implementation.
"""

import argparse
import importlib.util
import json
from pathlib import Path

import pytest
import yaml

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/adhoc/curate_gut_record_20261115.py"
SPEC = importlib.util.spec_from_file_location("gut_curator_guard", SCRIPT)
curator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(curator)


@pytest.fixture
def staged(tmp_path, monkeypatch):
    target = tmp_path / curator.TARGET
    target.parent.mkdir(parents=True)
    baseline = {"id": "CommunityMech:000122", "name": "Test gut", "curation_history": []}
    original = yaml.safe_dump(baseline).encode()
    target.write_bytes(original)
    state = tmp_path / ".temp/staged"
    state.mkdir(parents=True)
    source = tmp_path / ".temp/source.txt"
    source.write_text("Reviewed source\n")
    candidate = dict(baseline, description="Reviewed description")
    event = curator.record_curation_event(
        candidate, curator="codex", action="EDIT", changes="Control", llm_assisted=True
    )
    raw = yaml.safe_dump(candidate).encode()
    (state / "candidate.yaml").write_bytes(raw)
    receipt = {
        "target": curator.TARGET,
        "before_sha256": curator.digest(original),
        "after_sha256": curator.digest(raw),
        "event": event,
        "inputs": {".temp/source.txt": curator.digest(source.read_bytes())},
    }
    (state / "receipt.json").write_text(json.dumps(receipt))
    args = argparse.Namespace(
        output=tmp_path / ".temp/applied",
        apply_staged=state,
        reviewed_candidate_sha256=curator.digest(raw),
        reviewed_receipt_sha256=curator.digest((state / "receipt.json").read_bytes()),
    )
    monkeypatch.setattr(curator, "ROOT", tmp_path)
    monkeypatch.setattr(curator, "STATE", tmp_path / ".temp")
    monkeypatch.setattr(curator, "BEFORE", curator.digest(original))
    monkeypatch.setattr(argparse.ArgumentParser, "parse_args", lambda self: args)
    return target, original, state, source, args, receipt


def test_reviewed_native_control_persists(staged):
    target, original, state, source, args, receipt = staged
    curator.main()
    assert target.read_bytes() == (state / "candidate.yaml").read_bytes()
    assert target.read_bytes() != original
    assert json.loads((args.output / "receipt.json").read_bytes())["applied"]


def test_joint_candidate_receipt_forgery_refused(staged):
    target, original, state, source, args, receipt = staged
    candidate = yaml.safe_load((state / "candidate.yaml").read_bytes())
    candidate["description"] = "Unreviewed scientific claim"
    raw = yaml.safe_dump(candidate).encode()
    (state / "candidate.yaml").write_bytes(raw)
    receipt["after_sha256"] = curator.digest(raw)
    (state / "receipt.json").write_text(json.dumps(receipt))
    with pytest.raises(ValueError, match="reviewed"):
        curator.main()
    assert target.read_bytes() == original


def test_validation_time_source_change_refused(staged, monkeypatch):
    target, original, state, source, args, receipt = staged
    native = curator.write_validated_community

    def changed_after_validation(document, path):
        native(document, path)
        source.write_text("Changed while validation ran\n")

    monkeypatch.setattr(curator, "write_validated_community", changed_after_validation)
    with pytest.raises(ValueError, match="input changed"):
        curator.main()
    assert target.read_bytes() == original


def test_receipt_wrong_target_refused(staged):
    target, original, state, source, args, receipt = staged
    receipt["target"] = "kb/communities/Other.yaml"
    (state / "receipt.json").write_text(json.dumps(receipt))
    args.reviewed_receipt_sha256 = curator.digest((state / "receipt.json").read_bytes())
    with pytest.raises(ValueError, match="target"):
        curator.main()
    assert target.read_bytes() == original
