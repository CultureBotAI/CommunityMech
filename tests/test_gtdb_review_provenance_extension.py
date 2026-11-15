"""Capture/projection controls for the additive #2892 wrapper, 2026-11-15."""

import hashlib
import importlib
import json
from pathlib import Path
from types import SimpleNamespace

import pytest

ROOT = Path(__file__).resolve().parents[1]


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


@pytest.fixture
def case(tmp_path, monkeypatch):
    monkeypatch.syspath_prepend(str(ROOT / "scripts/adhoc"))
    wrapper = importlib.import_module("extend_gtdb_review_provenance_20261115")
    monkeypatch.setattr(wrapper.core, "ROOT", tmp_path)
    monkeypatch.setattr(wrapper.core, "STATE", tmp_path / ".temp")
    monkeypatch.setattr(wrapper.builder, "ROOT", tmp_path)
    monkeypatch.setattr(wrapper.core, "head", lambda: "a" * 40)
    names = [
        "scripts/adhoc/extend_gtdb_review_provenance_20261115.py",
        "scripts/adhoc/build_gtdb_batch_diagnostic_20261115.py",
        ".temp/issue.json",
        "reviews/structured/old/review.yaml",
        "kb/communities/record.yaml",
    ]
    for name in names:
        path = tmp_path / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(name)
    monkeypatch.setattr(wrapper, "__file__", str(tmp_path / names[0]))
    monkeypatch.setattr(wrapper.builder, "__file__", str(tmp_path / names[1]))
    monkeypatch.setattr(wrapper, "BUILDER_SHA", digest((tmp_path / names[1]).read_bytes()))
    config = {
        "additional_review_inputs": {
            name: digest((tmp_path / name).read_bytes()) for name in names[2:4]
        }
    }
    config_path = tmp_path / "reports/config.json"
    config_path.parent.mkdir()
    config_path.write_text(json.dumps(config))
    state = {"during_build": None, "inspection_drift": False, "base_digest_drift": False}

    def build(config_name, config_sha, output_name, revision):
        output = tmp_path / output_name
        output.mkdir()
        target = names[4]
        value = digest((tmp_path / target).read_bytes())
        review = {
            "targets": [{"target_id": "CommunityMech:999998", "path": target}],
            "source": {"git_revision": revision, "inputs": [{"path": target, "sha256": value}]},
        }
        if state["base_digest_drift"]:
            review["source"]["inputs"][0]["sha256"] = "0" * 64
        raw = json.dumps(review).encode()
        (output / "review.json").write_bytes(raw)
        (output / "inspection.json").write_text("{}")
        if state["during_build"]:
            (tmp_path / state["during_build"]).write_text("changed during build")
        return {"review": output_name + "/review.json", "sha256": digest(raw)}

    def inspect_source(root, targets, paths):
        rows = [{"path": name, "sha256": digest((root / name).read_bytes())} for name in paths]
        if state["inspection_drift"]:
            rows[0]["sha256"] = "0" * 64
        return {"source": {"git_revision": "a" * 40, "inputs": rows}}

    monkeypatch.setattr(wrapper.builder, "build", build)
    monkeypatch.setattr(
        wrapper.builder,
        "native_review",
        lambda: SimpleNamespace(inspect_source=inspect_source, validate_review=lambda review: None),
    )

    def run(attempt):
        return wrapper.build(
            "reports/config.json",
            digest(config_path.read_bytes()),
            ".temp/" + attempt,
            "a" * 40,
            digest((tmp_path / names[0]).read_bytes()),
        )

    return tmp_path, state, run, names


@pytest.mark.parametrize("changed", ["issue", "prior_review", "config"])
def test_actual_capture_mutation_refuses_and_restores(case, changed):
    root, state, run, names = case
    assert run("positive")["additional_provenance_inputs"] == 2
    name = {"issue": names[2], "prior_review": names[3], "config": "reports/config.json"}[changed]
    original = (root / name).read_bytes()
    state["during_build"] = name
    with pytest.raises(ValueError, match="changed|hash"):
        run("mutated")
    assert not (root / ".temp/mutated/review.json").exists()
    (root / name).write_bytes(original)
    state["during_build"] = None
    restored = run("restored")
    assert restored["inputs_unchanged"]
    final = json.loads((root / restored["review"]).read_bytes())
    assert {names[2], names[3]}.issubset(row["path"] for row in final["source"]["inputs"])


@pytest.mark.parametrize("fault", ["inspection_drift", "base_digest_drift"])
def test_inspected_or_builder_bytes_must_equal_capture(case, fault):
    root, state, run, _names = case
    assert run("positive")["native_validation"]
    state[fault] = True
    with pytest.raises(ValueError, match="capture|changed"):
        run("mutated")
    assert not (root / ".temp/mutated/review.json").exists()
    state[fault] = False
    assert run("restored")["inputs_unchanged"]


def test_duplicate_output_refuses_before_builder(case):
    root, _state, run, _names = case
    result = run("positive")
    path = root / result["review"]
    before = path.read_bytes(), path.stat().st_mtime_ns
    with pytest.raises(ValueError, match="exclusive"):
        run("positive")
    assert (path.read_bytes(), path.stat().st_mtime_ns) == before
