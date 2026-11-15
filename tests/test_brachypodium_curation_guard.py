"""One-record application preserves reviewed inputs across validation (#2814)."""

import importlib.util
import json
import sys
from pathlib import Path

import pytest
import yaml

HELPER = (
    Path(__file__).resolve().parents[1] / "scripts/adhoc/curate_phase2_brachypodium_20261115.py"
)


@pytest.mark.parametrize("source_changes", [False, True])
def test_reviewed_source_must_survive_native_validation(tmp_path, monkeypatch, source_changes):
    spec = importlib.util.spec_from_file_location("brachypodium_guard", HELPER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    state = tmp_path / ".temp/record"
    staged = state / "staged"
    staged.mkdir(parents=True)
    canonical = tmp_path / module.TARGET
    canonical.parent.mkdir(parents=True)
    original = yaml.safe_dump({"id": "CommunityMech:000088", "curation_history": []}).encode()
    canonical.write_bytes(original)
    reviewed_source = tmp_path / "source.txt"
    reviewed_source.write_text("inspected source")
    candidate = staged / "candidate.yaml"
    candidate.write_text(
        yaml.safe_dump({"id": "CommunityMech:000088", "curation_history": [{"action": "EDIT"}]})
    )
    expected = module.sha(candidate.read_bytes())
    (staged / "receipt.json").write_text(
        json.dumps(
            {
                "before_sha256": module.sha(original),
                "after_sha256": expected,
                "inputs": {"source.txt": module.sha(reviewed_source.read_bytes())},
            }
        )
    )
    for key, value in {
        "ROOT": tmp_path,
        "STATE": state,
        "BEFORE": module.sha(original),
        "SOURCE_SHA": {},
    }.items():
        monkeypatch.setattr(module, key, value)

    def validating_write(document, path):
        path.write_text(yaml.safe_dump(document))
        if source_changes:
            reviewed_source.write_text("changed during validation")

    monkeypatch.setattr(module, "write_validated_community", validating_write)
    monkeypatch.setattr(
        sys,
        "argv",
        [
            str(HELPER),
            "--output",
            str(state / "application"),
            "--apply-candidate",
            str(candidate),
            "--expected-candidate-sha256",
            expected,
        ],
    )
    if source_changes:
        with pytest.raises(ValueError, match="reviewed input changed during validation"):
            module.main()
        assert canonical.read_bytes() == original
        assert not (state / "application/receipt.json").exists()
    else:
        module.main()
        assert canonical.read_bytes() == candidate.read_bytes()
        assert json.loads((state / "application/receipt.json").read_text())["applied"]
