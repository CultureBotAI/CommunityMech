"""Actual guarded BR1 write controls for #2849; no scientific acceptance inference."""

import copy
import importlib.util
import json
import subprocess
from pathlib import Path

import pytest
import yaml


@pytest.fixture
def controlled(tmp_path, monkeypatch):
    repo = Path(__file__).resolve().parents[1]
    source = repo / "scripts/adhoc/curate_br1_grounding_20261115.py"
    spec = importlib.util.spec_from_file_location("br1_guard", source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    # Native CI explicitly fetches this historical base, including after squash (#2858).
    original = subprocess.check_output(
        ["git", "show", "68699871415fda3c9eebf20382a315f9f3c7b17a:" + module.TARGET],
        cwd=repo,
    )
    assert module.sha(original) == module.BEFORE
    report = json.loads((repo / module.REPORT).read_bytes())
    assert module.sha((repo / module.REPORT).read_bytes()) == module.REPORT_SHA
    # These focused controls exercise replacement refusal, not authority verification.
    block = {"gtdb_id": module.NEW_ID, "gtdb_lineage": report["r220_lineage"]}
    root = tmp_path / "repo"
    state = root / ".temp/br1-source-review-20261115"
    stage = state / "staged"
    stage.mkdir(parents=True)
    target = root / module.TARGET
    target.parent.mkdir(parents=True)
    target.write_bytes(original)
    evidence = root / "source.json"
    evidence.write_bytes(b"reviewed source bytes")
    inputs = {"source.json": module.sha(evidence.read_bytes())}
    monkeypatch.setattr(module, "ROOT", root)
    monkeypatch.setattr(module, "STATE", state)
    monkeypatch.setattr(module, "source_block", lambda: (block, inputs))
    monkeypatch.setattr(module, "current_head", lambda: "1" * 40)
    after = yaml.safe_load(original)
    after["taxonomy"][0]["taxon_term"]["gtdb_classification"] = copy.deepcopy(block)
    after["description"] = after["description"].replace(module.OLD_ID, module.NEW_ID, 1)
    after["curation_history"].append(
        {
            "timestamp": "2026-11-15T05:30:00Z",
            "curator": "codex",
            "action": "EDIT",
            "changes": module.SUMMARY,
            "llm_assisted": True,
        }
    )
    candidate = stage / "candidate.yaml"
    candidate.write_text(yaml.safe_dump(after))
    proof = {
        "target": module.TARGET,
        "before_sha256": module.BEFORE,
        "after_sha256": module.sha(candidate.read_bytes()),
        "applied": False,
        "inputs": inputs,
    }
    candidate.with_name("receipt.json").write_text(json.dumps(proof))

    def writer(document, path):
        # Native schema writing is exercised separately by the real candidate.
        path.write_text(yaml.safe_dump(document))
        marker = state / "mutate"
        if marker.exists():
            kind = marker.read_text()
            if kind == "source":
                evidence.write_bytes(b"changed during native validation")
            elif kind == "record":
                target.write_bytes(original + b"# concurrent change\n")
            elif kind == "candidate":
                candidate.write_bytes(candidate.read_bytes() + b"# changed\n")
            elif kind == "receipt":
                candidate.with_name("receipt.json").write_text("{}")
            elif kind == "revision":
                monkeypatch.setattr(module, "current_head", lambda: "2" * 40)

    monkeypatch.setattr(module, "write_validated_community", writer)
    return module, state, target, original, candidate, proof


def apply(case, name):
    module, state, _target, _original, candidate, proof = case
    return module.execute(
        state / name,
        candidate,
        proof["after_sha256"],
        module.sha(candidate.with_name("receipt.json").read_bytes()),
        expected_revision="1" * 40,
    )


def test_actual_guard_persists_exact_accepted_candidate(controlled):
    module, state, target, original, candidate, _proof = controlled
    apply(controlled, "positive")
    assert target.read_bytes() == candidate.read_bytes() != original
    receipt = json.loads((state / "positive/receipt.json").read_bytes())
    assert receipt["applied"] is True
    assert receipt["after_sha256"] == module.sha(target.read_bytes())
    assert receipt["before_sha256"] == module.sha(original)


@pytest.mark.parametrize("kind", ["source", "record", "candidate", "receipt", "revision"])
def test_changes_during_validation_refuse_replacement(controlled, kind):
    _module, state, target, original, candidate, _proof = controlled
    (state / "mutate").write_text(kind)
    with pytest.raises(ValueError, match="changed"):
        apply(controlled, "negative-" + kind)
    assert target.read_bytes() == (
        original + b"# concurrent change\n" if kind == "record" else original
    )
    assert target.read_bytes() != candidate.read_bytes()
    assert not (state / ("negative-" + kind) / "receipt.json").exists()


@pytest.mark.parametrize("kind", ["phenotype", "description", "history", "block"])
def test_resigned_but_unapproved_semantic_delta_refused(controlled, kind):
    module, state, target, original, candidate, proof = controlled
    changed = yaml.safe_load(candidate.read_bytes())
    if kind == "phenotype":
        changed["ecological_interactions"][0]["description"] = "Unapproved claim"
    elif kind == "description":
        changed["description"] += " Unapproved claim."
    elif kind == "history":
        changed["curation_history"][0]["changes"] = "Rewritten history"
    elif kind == "block":
        changed["taxonomy"][0]["taxon_term"]["gtdb_classification"]["total_genomes"] = 2
    candidate.write_text(yaml.safe_dump(changed))
    proof["after_sha256"] = module.sha(candidate.read_bytes())
    candidate.with_name("receipt.json").write_text(json.dumps(proof))
    with pytest.raises(ValueError):
        apply(controlled, "scope-" + kind)
    assert target.read_bytes() == original
    assert not (state / ("scope-" + kind)).exists()


def test_wrong_reviewed_candidate_hash_refuses_before_output(controlled):
    _module, state, target, original, _candidate, proof = controlled
    proof["after_sha256"] = "0" * 64
    with pytest.raises(ValueError, match="mismatch"):
        apply(controlled, "wrong-hash")
    assert target.read_bytes() == original
    assert not (state / "wrong-hash").exists()
