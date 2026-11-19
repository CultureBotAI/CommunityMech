"""Capture-to-publication mutation controls for BR1 exporter #2860."""

import importlib.util
import json
from pathlib import Path

import pytest


@pytest.fixture
def snapshot(tmp_path, monkeypatch):
    source = (
        Path(__file__).resolve().parents[1]
        / "scripts/adhoc/export_br1_grounding_evidence_20261115.py"
    )
    spec = importlib.util.spec_from_file_location("br1_export_control", source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    root = tmp_path / "repo"
    root.mkdir()
    review_path = root / "review.yaml"
    paths = {
        "source": root / "source.json",
        "log": root / "native.log",
        "exit": root / "native.exit",
        "review": review_path,
        "markdown": root / "review.md",
        "schema": root / "schema/record_review.yaml",
    }
    paths["schema"].parent.mkdir()
    for key, raw in {
        "source": b'{"species":"accepted"}\n',
        "log": b"Native passed\n",
        "exit": b"0\n",
        "markdown": b"Derived review\n",
        "schema": b"name: controlled\n",
    }.items():
        paths[key].write_bytes(raw)
    review = {
        "source": {
            "inputs": [
                {"path": path.name, "sha256": module.digest(path.read_bytes())}
                for path in (paths["source"], paths["log"], paths["exit"])
            ]
        }
    }
    review_path.write_text(json.dumps(review))
    monkeypatch.setattr(module, "ROOT", root)
    monkeypatch.setattr(module, "REVIEW_SHA", module.digest(review_path.read_bytes()))
    return module, root, paths, review


def test_capture_hash_parse_and_export_use_same_bytes(snapshot, monkeypatch):
    module, root, paths, _ = snapshot
    original = Path.read_bytes
    reads = {}

    def counted(path):
        reads[path] = reads.get(path, 0) + 1
        return original(path)

    monkeypatch.setattr(Path, "read_bytes", counted)
    review, captured = module.capture_inputs(paths["review"])
    raw, proof = module.raw_metadata(review, paths["source"], root / "public.json", captured)
    assert all(count == 1 for count in reads.values())
    assert json.loads(raw)["species"] == "accepted"
    assert proof["sha256"] == proof["raw_sha256"] == module.digest(raw)
    assert module.FrozenSchema(captured[paths["schema"]]).read_text() == "name: controlled\n"
    module.publish(captured, {root / "public.json": raw})
    assert (root / "public.json").read_bytes() == raw


@pytest.mark.parametrize("changed", ["source", "log", "exit", "review", "markdown", "schema"])
def test_changed_capture_refuses_then_restored_bytes_publish(snapshot, changed):
    module, root, paths, _ = snapshot
    review, captured = module.capture_inputs(paths["review"])
    first, _ = module.raw_metadata(review, paths["source"], root / "positive.json", captured)
    module.publish(captured, {root / "positive.json": first})
    assert (root / "positive.json").read_bytes() == first
    original = captured[paths[changed]]
    paths[changed].write_bytes(original + b"changed after capture\n")
    # Even a later export request consumes the original captured bytes, never
    # the changed file; publication nevertheless refuses stale evidence.
    raw, proof = module.raw_metadata(review, paths["source"], root / "restored.json", captured)
    assert raw == first and proof["sha256"] == module.digest(first)
    with pytest.raises(ValueError, match="captured input changed"):
        module.publish(captured, {root / "restored.json": raw})
    assert not (root / "restored.json").exists()
    paths[changed].write_bytes(original)
    module.publish(captured, {root / "restored.json": raw})
    assert (root / "restored.json").read_bytes() == first


def test_changed_source_before_capture_is_not_newly_attested(snapshot):
    module, _root, paths, _ = snapshot
    paths["source"].write_bytes(b'{"species":"unreviewed"}\n')
    with pytest.raises(ValueError, match="saved diagnostic input differs"):
        module.capture_inputs(paths["review"])


def test_changed_immutable_review_refused(snapshot):
    module, _root, paths, _ = snapshot
    paths["review"].write_bytes(paths["review"].read_bytes() + b"\n")
    with pytest.raises(ValueError, match="immutable accepted review bytes differ"):
        module.capture_inputs(paths["review"])


def test_existing_output_is_never_replaced(snapshot):
    module, root, paths, _ = snapshot
    _, captured = module.capture_inputs(paths["review"])
    output = root / "existing.json"
    output.write_bytes(b"prior artifact")
    with pytest.raises(ValueError, match="exclusive"):
        module.publish(captured, {output: b"new artifact"})
    assert output.read_bytes() == b"prior artifact"
