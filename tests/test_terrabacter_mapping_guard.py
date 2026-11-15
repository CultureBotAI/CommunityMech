"""Reviewed mapping application must survive a source-change control (#2849)."""

import importlib.util
import json
from pathlib import Path

import pytest
import yaml


@pytest.fixture
def controlled(tmp_path, monkeypatch):
    source = (
        Path(__file__).resolve().parents[1] / "scripts/adhoc/curate_terrabacter_mapping_20261115.py"
    )
    spec = importlib.util.spec_from_file_location("terrabacter_guard", source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    root = tmp_path / "repo"
    state = root / ".temp/control"
    stage = state / "staged"
    stage.mkdir(parents=True)
    target = root / module.TARGET
    target.parent.mkdir(parents=True)
    before = {
        "id": "CommunityMech:000532",
        "taxonomy": [
            {
                "taxon_term": {
                    "term": {"id": "NCBITaxon:1472881", "label": "Terrabacter sp. 2APm3"},
                    "gtdb_classification": {"gtdb_id": "GTDB:g__Terrabacter"},
                }
            }
        ],
        "curation_history": [
            {"action": "ORIGINAL", "changes": "Original history must remain unchanged."}
        ],
    }
    original = yaml.safe_dump(before).encode()
    target.write_bytes(original)
    after = yaml.safe_load(original)
    after["taxonomy"][0]["taxon_term"]["gtdb_classification"].update(
        ncbi_source_id="NCBITaxon:53355",
        curated=True,
        curation_note="Source-supported manual genus correspondence; no exact stock genome.",
    )
    after["curation_history"].append(
        {"action": "EDIT", "changes": "Narrow source-supported mapping update."}
    )
    candidate = stage / "candidate.yaml"
    candidate.write_text(yaml.safe_dump(after))
    evidence = root / "source.txt"
    evidence.write_bytes(b"reviewed source bytes")
    proof = {
        "target": module.TARGET,
        "before_sha256": module.sha(original),
        "after_sha256": module.sha(candidate.read_bytes()),
        "applied": False,
        "inputs": {"source.txt": module.sha(evidence.read_bytes())},
    }
    (stage / "receipt.json").write_text(json.dumps(proof))
    monkeypatch.setattr(module, "ROOT", root)
    monkeypatch.setattr(module, "STATE", state)
    monkeypatch.setattr(module, "BEFORE", module.sha(original))
    monkeypatch.setattr(module, "current_head", lambda: "1" * 40)

    def writer(document, path):
        # The real native schema writer was separately exercised by candidate001.
        # This control isolates changes occurring inside that validation window.
        path.write_text(yaml.safe_dump(document))
        if (state / "change-source").exists():
            evidence.write_bytes(b"changed inside validation")

    monkeypatch.setattr(module, "write_validated_community", writer)
    return module, state, target, original, candidate, evidence, proof


def apply(module, output, candidate, candidate_sha):
    return module.execute(
        output,
        candidate,
        candidate_sha,
        module.sha(candidate.with_name("receipt.json").read_bytes()),
        expected_revision="1" * 40,
    )


def test_source_change_during_validation_refuses_apply_then_restores(controlled):
    module, state, target, original, candidate, evidence, proof = controlled
    apply(module, state / "positive", candidate, proof["after_sha256"])
    assert target.read_bytes() == candidate.read_bytes()
    assert json.loads((state / "positive/receipt.json").read_bytes())["applied"] is True
    target.write_bytes(original)
    marker = state / "change-source"
    marker.touch()
    with pytest.raises(ValueError, match="reviewed input changed"):
        apply(module, state / "mutated", candidate, proof["after_sha256"])
    assert evidence.read_bytes() == b"changed inside validation"
    assert target.read_bytes() == original
    assert not (state / "mutated/receipt.json").exists()
    evidence.write_bytes(b"reviewed source bytes")
    marker.unlink()
    apply(module, state / "restored", candidate, proof["after_sha256"])
    assert target.read_bytes() == candidate.read_bytes()


def test_wrong_reviewed_hash_refuses_before_output(controlled):
    module, state, target, original, candidate, _evidence, _proof = controlled
    with pytest.raises(ValueError, match="receipt/candidate mismatch"):
        apply(module, state / "wrong", candidate, "0" * 64)
    assert target.read_bytes() == original
    assert not (state / "wrong").exists()
