"""#2831: native guarded write controls for the historical-scope correction."""

import argparse
import importlib.util
import json
import subprocess
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "gut_historical_scope", ROOT / "scripts/adhoc/curate_gut_historical_scope_20261115.py"
)
curator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(curator)


@pytest.fixture
def staged(tmp_path, monkeypatch):
    original = subprocess.check_output(
        ["git", "show", "de4c6450dd3e42f205c2f7e8f11b8fe44f03bd6b:" + curator.TARGET],
        cwd=ROOT,
    )
    assert curator.digest(original) == curator.BASELINE
    before = curator.load(original)
    target = tmp_path / curator.TARGET
    target.parent.mkdir(parents=True)
    target.write_bytes(original)
    stage = tmp_path / ".temp/staged"
    stage.mkdir(parents=True)
    source = tmp_path / ".temp/source.txt"
    source.write_text("Reviewed source")
    after = curator.revised(before)
    event = curator.record_curation_event(
        after, curator="codex", action="EDIT", changes=curator.SUMMARY, llm_assisted=True
    )
    candidate = yaml.safe_dump(after).encode()
    (stage / "candidate.yaml").write_bytes(candidate)
    receipt = {
        "target": curator.TARGET,
        "before_sha256": curator.digest(original),
        "after_sha256": curator.digest(candidate),
        "event": event,
        "inputs": {".temp/source.txt": curator.digest(source.read_bytes())},
        "applied": False,
    }
    (stage / "receipt.json").write_text(json.dumps(receipt))
    args = argparse.Namespace(
        output=tmp_path / ".temp/applied",
        apply_staged=stage,
        reviewed_candidate_sha256=curator.digest(candidate),
        reviewed_receipt_sha256=curator.digest((stage / "receipt.json").read_bytes()),
    )
    monkeypatch.setattr(curator, "ROOT", tmp_path)
    monkeypatch.setattr(curator, "STATE", tmp_path / ".temp")
    monkeypatch.setattr(curator, "BASELINE", curator.digest(original))
    monkeypatch.setattr(argparse.ArgumentParser, "parse_args", lambda self: args)
    return target, original, stage, source, args, receipt


def test_native_control_persists_only_discussion_and_append_only_history(staged):
    target, original, stage, source, args, receipt = staged
    curator.main()
    assert target.read_bytes() == (stage / "candidate.yaml").read_bytes()
    assert target.read_bytes() != original
    before, after = curator.load(original), curator.load(target.read_bytes())
    for key in before.keys() - {"discussions", "curation_history"}:
        assert before[key] == after[key]
    assert after["curation_history"][:-1] == before["curation_history"]
    assert json.loads((args.output / "receipt.json").read_bytes())["applied"]


@pytest.mark.parametrize("replace_external_hashes", [False, True])
def test_forged_candidate_manifest_cannot_change_an_unreviewed_assertion(
    staged, replace_external_hashes
):
    target, original, stage, source, args, receipt = staged
    after = curator.load((stage / "candidate.yaml").read_bytes())
    after["description"] = "An unreviewed scientific claim"
    candidate = yaml.safe_dump(after).encode()
    (stage / "candidate.yaml").write_bytes(candidate)
    receipt["after_sha256"] = curator.digest(candidate)
    (stage / "receipt.json").write_text(json.dumps(receipt))
    if replace_external_hashes:
        args.reviewed_candidate_sha256 = curator.digest(candidate)
        args.reviewed_receipt_sha256 = curator.digest((stage / "receipt.json").read_bytes())
    with pytest.raises(ValueError, match="reviewed"):
        curator.main()
    assert target.read_bytes() == original


def test_source_changed_during_native_validation_prevents_apply(staged, monkeypatch):
    target, original, stage, source, args, receipt = staged
    native = curator.write_validated_community

    def changed_after_validation(document, path):
        native(document, path)
        source.write_text("Changed source")

    monkeypatch.setattr(curator, "write_validated_community", changed_after_validation)
    with pytest.raises(ValueError, match="input changed"):
        curator.main()
    assert target.read_bytes() == original


def test_wrong_target_receipt_is_refused_even_with_its_hash(staged):
    target, original, stage, source, args, receipt = staged
    receipt["target"] = "kb/communities/Other.yaml"
    (stage / "receipt.json").write_text(json.dumps(receipt))
    args.reviewed_receipt_sha256 = curator.digest((stage / "receipt.json").read_bytes())
    with pytest.raises(ValueError, match="target"):
        curator.main()
    assert target.read_bytes() == original
