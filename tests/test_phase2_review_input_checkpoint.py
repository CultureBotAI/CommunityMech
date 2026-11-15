"""Exact private checkpoint controls: no substitutions or destructive reruns."""

import importlib.util
import json
from copy import deepcopy
from pathlib import Path

import pytest

HELPER = (
    Path(__file__).resolve().parents[1]
    / "scripts/adhoc/checkpoint_phase2_review_inputs_20261115.py"
)
SPEC = importlib.util.spec_from_file_location("phase2_checkpoint", HELPER)
CHECKPOINT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECKPOINT)


@pytest.fixture
def planned(tmp_path, monkeypatch):
    monkeypatch.setattr(CHECKPOINT, "ROOT", tmp_path)
    reviews = []
    for index, raw in enumerate((b"earlier helper bytes\n", b"later helper bytes\n")):
        root = tmp_path / f"source-{index}"
        source = root / "scripts/adhoc/helper.py"
        source.parent.mkdir(parents=True)
        source.write_bytes(raw)
        identifier = f"20261115T00000{index}Z-test"
        reviews.append(
            {
                "review_id": identifier,
                "source_checkout": str(root),
                "optional": False,
                "status": "ready",
                "files": [
                    {
                        "original_path": "scripts/adhoc/helper.py",
                        "snapshot_path": f"{identifier}/inputs/scripts/adhoc/helper.py",
                        "expected_sha256": CHECKPOINT.digest(raw),
                        "bytes": len(raw),
                        "role": "input",
                    }
                ],
            }
        )
    return {"status": "ready", "reviews": reviews}, tmp_path / ".temp/snapshot-001"


def test_same_original_path_preserves_distinct_review_versions(planned):
    plan, destination = planned
    result = CHECKPOINT.snapshot(plan, destination)
    assert result["files_verified"] == 2
    manifest = json.loads((destination / "manifest.json").read_bytes())
    assert {row["original_path"] for row in manifest["files"]} == {"scripts/adhoc/helper.py"}
    assert len({row["sha256"] for row in manifest["files"]}) == 2
    assert len({row["path"] for row in manifest["files"]}) == 2
    assert CHECKPOINT.verify(destination) == result


def test_changed_source_is_refused_before_creating_any_snapshot(planned):
    plan, destination = planned
    root = Path(plan["reviews"][0]["source_checkout"])
    (root / "scripts/adhoc/helper.py").write_text("unreviewed changed source")
    with pytest.raises(ValueError, match="changed after planning"):
        CHECKPOINT.snapshot(plan, destination)
    assert not destination.exists()


@pytest.mark.parametrize("partial", [True, False])
def test_existing_partial_or_complete_attempt_remains_byte_identical(planned, partial):
    plan, destination = planned
    if partial:
        destination.mkdir(parents=True)
        (destination / "retained.txt").write_bytes(b"partial failure is retained\n")
    else:
        CHECKPOINT.snapshot(plan, destination)
    before = {
        path: (path.read_bytes(), path.stat().st_mtime_ns)
        for path in destination.rglob("*")
        if path.is_file()
    }
    with pytest.raises(ValueError, match="already exists"):
        CHECKPOINT.snapshot(plan, destination)
    assert before == {path: (path.read_bytes(), path.stat().st_mtime_ns) for path in before}


def test_destination_escape_and_environment_file_are_rejected(planned):
    plan, destination = planned
    bad = deepcopy(plan)
    bad["reviews"][0]["files"][0]["snapshot_path"] = "../escape.py"
    with pytest.raises(ValueError, match="unsafe declared path"):
        CHECKPOINT.snapshot(bad, destination)
    assert not destination.exists()
    with pytest.raises(ValueError, match="credential"):
        CHECKPOINT.input_bytes(Path(plan["reviews"][0]["source_checkout"]), ".env")


def test_tampered_snapshot_or_added_file_cannot_verify(planned):
    plan, destination = planned
    CHECKPOINT.snapshot(plan, destination)
    item = destination / plan["reviews"][0]["files"][0]["snapshot_path"]
    original = item.read_bytes()
    item.write_bytes(b"different bytes")
    with pytest.raises(ValueError, match="hash or size"):
        CHECKPOINT.verify(destination)
    item.write_bytes(original)
    CHECKPOINT.verify(destination)
    (destination / "unexpected.txt").write_bytes(b"unreviewed")
    with pytest.raises(ValueError, match="membership differs"):
        CHECKPOINT.verify(destination)
