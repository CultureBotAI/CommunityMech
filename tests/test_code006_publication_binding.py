"""Post-audit raw artifact mutation must stop publication, #2855."""

import hashlib
import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def artifacts(tmp_path, monkeypatch):
    monkeypatch.syspath_prepend(str(ROOT / "scripts/adhoc"))
    spec = importlib.util.spec_from_file_location(
        "canary_publisher", ROOT / "scripts/adhoc/publish_code006_canary_20261115.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    monkeypatch.setattr(module, "ROOT", tmp_path)
    log, exit_path = tmp_path / "native.log", tmp_path / "native.exit"
    log.write_bytes(b"2 passed in 1.00s\n")
    exit_path.write_bytes(b"0\n")
    review = {
        "source": {
            "inputs": [
                {"path": path.name, "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
                for path in (log, exit_path)
            ]
        }
    }
    return module, review, log, exit_path


def test_original_bytes_match_saved_review(artifacts):
    module, review, log, exit_path = artifacts
    assert module.checked_native_bytes(review, log, exit_path, 0) == (
        log.read_bytes(),
        exit_path.read_bytes(),
    )


@pytest.mark.parametrize("artifact", ["log", "exit"])
def test_post_audit_mutation_refused_then_restored(artifacts, artifact):
    module, review, log, exit_path = artifacts
    assert module.checked_native_bytes(review, log, exit_path, 0)
    path = log if artifact == "log" else exit_path
    original = path.read_bytes()
    # Exit remains semantically zero: only exact byte binding catches this.
    path.write_bytes(b"1 passed in 1.00s\n" if artifact == "log" else b"00\n")
    assert path.read_bytes() != original
    with pytest.raises(ValueError, match="saved review"):
        module.checked_native_bytes(review, log, exit_path, 0)
    path.write_bytes(original)
    assert module.checked_native_bytes(review, log, exit_path, 0)


@pytest.mark.parametrize("kind", ["absent", "duplicate"])
def test_missing_or_duplicate_binding_refused(artifacts, kind):
    module, review, log, exit_path = artifacts
    rows = review["source"]["inputs"]
    if kind == "absent":
        rows.pop(0)
    else:
        rows.append(rows[0].copy())
    with pytest.raises(ValueError, match="saved review"):
        module.checked_native_bytes(review, log, exit_path, 0)
