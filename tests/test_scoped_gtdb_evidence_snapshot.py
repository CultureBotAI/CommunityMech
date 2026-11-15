"""Reusable exact captured-byte publication controls, #2848/#2860, 2026-11-15."""

import importlib.util
import json
from pathlib import Path

import pytest


@pytest.fixture
def snapshot(tmp_path, monkeypatch):
    source = Path(__file__).resolve().parents[1] / "scripts/adhoc/scoped_gtdb_evidence_20261115.py"
    spec = importlib.util.spec_from_file_location("scoped_gtdb_snapshot_test", source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    root = tmp_path / "repo"
    review_dir = root / "reviews/structured/20261115T000000Z-test"
    review_dir.mkdir(parents=True)
    paths = {
        "source": root / "source.json",
        "log": root / "native.log",
        "exit": root / "native.exit",
        "review": review_dir / "review.yaml",
        "markdown": review_dir / "review.md",
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
    paths["review"].write_text(json.dumps(review))
    monkeypatch.setattr(module, "ROOT", root)
    expected = module.digest(paths["review"].read_bytes())
    return module, root, paths, expected


def test_capture_parse_hash_export_use_identical_bytes(snapshot, monkeypatch):
    module, root, paths, expected = snapshot
    original = Path.read_bytes
    reads = {}

    def counted(path):
        reads[path] = reads.get(path, 0) + 1
        return original(path)

    monkeypatch.setattr(Path, "read_bytes", counted)
    review, captured = module.capture_inputs(paths["review"], expected)
    raw = captured[paths["source"]]
    assert module.bound(review, paths["source"], captured)["sha256"] == module.digest(raw)
    assert json.loads(raw)["species"] == "accepted"
    assert all(count == 1 for count in reads.values())
    assert module.FrozenSchema(captured[paths["schema"]]).read_text() == "name: controlled\n"
    output = root / "reports/source.json"
    module.publish(captured, {output: raw})
    assert output.read_bytes() == raw


@pytest.mark.parametrize("changed", ["source", "log", "exit", "review", "markdown", "schema"])
def test_changed_capture_refuses_then_restored_bytes_publish(snapshot, changed):
    module, root, paths, expected = snapshot
    _review, captured = module.capture_inputs(paths["review"], expected)
    original = captured[paths[changed]]
    paths[changed].write_bytes(original + b"changed\n")
    output = root / "reports/restored.json"
    with pytest.raises(ValueError, match="captured input changed"):
        module.publish(captured, {output: captured[paths["source"]]})
    assert not output.exists()
    paths[changed].write_bytes(original)
    module.publish(captured, {output: captured[paths["source"]]})
    assert output.read_bytes() == captured[paths["source"]]


def test_source_changed_before_capture_refuses(snapshot):
    module, _root, paths, expected = snapshot
    paths["source"].write_bytes(b"unreviewed")
    with pytest.raises(ValueError, match="saved diagnostic input differs"):
        module.capture_inputs(paths["review"], expected)


def test_immutable_review_changed_refuses(snapshot):
    module, _root, paths, expected = snapshot
    paths["review"].write_bytes(paths["review"].read_bytes() + b"\n")
    with pytest.raises(ValueError, match="immutable accepted review"):
        module.capture_inputs(paths["review"], expected)


def test_existing_output_preserved(snapshot):
    module, root, paths, expected = snapshot
    _review, captured = module.capture_inputs(paths["review"], expected)
    output = root / "reports/existing.json"
    output.parent.mkdir()
    output.write_bytes(b"prior")
    with pytest.raises(ValueError, match="exclusive"):
        module.publish(captured, {output: b"new"})
    assert output.read_bytes() == b"prior"


def test_canonical_output_refused(snapshot):
    module, root, paths, expected = snapshot
    _review, captured = module.capture_inputs(paths["review"], expected)
    output = root / "kb/communities/forbidden.yaml"
    with pytest.raises(ValueError, match="reports"):
        module.publish(captured, {output: b"new"})
    assert not output.exists()
