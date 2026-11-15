"""Issue metadata and hashes must describe one immutable snapshot (#2859)."""

import importlib.util
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "issue_snapshot", ROOT / "scripts/adhoc/snapshot_code006_reference_issue_states_20261115.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_real_file_change_after_capture_is_refused_then_restored(tmp_path):
    paths = {number: tmp_path / f"issue-{number}.json" for number in (596, 703)}
    for number, path in paths.items():
        path.write_text(
            json.dumps(
                {
                    "issue": {
                        "number": number,
                        "url": f"https://github.com/{MODULE.REPO}/issues/{number}",
                        "state": "OPEN",
                    }
                }
            )
        )
    observations, hashes, captured = MODULE.capture_snapshots(paths)
    MODULE.verify_snapshots(paths, captured)
    assert all(hashes[str(n)] == MODULE.digest(captured[n]) for n in paths)
    # Change a later snapshot, rather than the canary, after parsing it.
    mutated = json.loads(paths[703].read_bytes())
    mutated["issue"]["state"] = "CLOSED"
    paths[703].write_text(json.dumps(mutated))
    assert paths[703].read_bytes() != captured[703]
    assert observations["703"]["issue"]["state"] == "OPEN"
    with pytest.raises(ValueError, match="changed before publication"):
        MODULE.verify_snapshots(paths, captured)
    paths[703].write_bytes(captured[703])
    MODULE.verify_snapshots(paths, captured)


def test_digest_uses_the_same_read_as_parsed_metadata(tmp_path, monkeypatch):
    path = tmp_path / "issue-596.json"
    original = json.dumps(
        {
            "issue": {
                "number": 596,
                "state": "OPEN",
                "url": f"https://github.com/{MODULE.REPO}/issues/596",
            }
        }
    ).encode()
    calls = []

    def read_once(self):
        calls.append(self)
        if len(calls) > 1:
            raise AssertionError("parse and digest must not perform independent reads")
        return original

    monkeypatch.setattr(Path, "read_bytes", read_once)
    observations, hashes, captured = MODULE.capture_snapshots({596: path})
    assert observations["596"]["issue"]["state"] == "OPEN"
    assert hashes["596"] == MODULE.digest(original)
    assert captured[596] == original
    assert calls == [path]
