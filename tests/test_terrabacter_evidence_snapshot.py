"""Publication must reject input mutation after its initial binding (#2860)."""

import hashlib
import importlib.util
import json
from pathlib import Path

import pytest
import yaml


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


@pytest.fixture
def publisher(tmp_path, monkeypatch):
    root = Path(__file__).resolve().parents[1]
    spec = importlib.util.spec_from_file_location(
        "terrabacter_export", root / "scripts/adhoc/export_terrabacter_canary_20261115.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    monkeypatch.setattr(module, "ROOT", tmp_path)
    state = tmp_path / ".temp/gtdb-source-routes-2849-20261115"
    monkeypatch.setattr(module, "STATE", state)
    monkeypatch.setattr(module, "OUT", tmp_path / "reports/output")
    monkeypatch.setattr(module.sys, "argv", [str(spec.origin), "--plan"])
    files = {}

    def write(name, raw):
        path = tmp_path / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
        files[path] = raw
        return path

    target = write(module.TARGET, b"canonical reviewed bytes\n")
    monkeypatch.setattr(module, "AFTER", sha(files[target]))
    write(str((state / "terrabacter-applied-m5-001/receipt.json").relative_to(tmp_path)), b"{}\n")
    write(
        str((state / "terrabacter-diagnostic-001/native-route.json").relative_to(tmp_path)), b"{}\n"
    )
    write(module.SIDECAR, b"target: preserved\n")
    for gate in ("schema", "strict", "gtdb", "domain", "scalars", "history", "new-history"):
        prefix = state / f"terrabacter-canary-run-{gate}-001"
        log = b"Actual retained native result\n"
        write(str((prefix / "native.log").relative_to(tmp_path)), log)
        write(str((prefix / "native.exit").relative_to(tmp_path)), b"0\n")
        receipt = {
            "revision": module.REVISION,
            "plan": False,
            "inputs": {str(module.M5_ROOT / module.TARGET): module.AFTER},
            "exit_code": 0,
            "finished_at": "2026-11-15T05:29:00Z",
            "log_sha256": sha(log),
            "log_bytes": len(log),
        }
        write(str((prefix / "receipt.json").relative_to(tmp_path)), json.dumps(receipt).encode())
    review = {
        "source": {
            "git_revision": module.REVISION,
            "inputs": [
                {"path": str(path.relative_to(tmp_path)), "sha256": sha(raw)}
                for path, raw in files.items()
            ],
        }
    }
    review_path = write(
        f"reviews/structured/{module.REVIEW}/review.yaml", yaml.safe_dump(review).encode()
    )
    write(f"reviews/structured/{module.REVIEW}/review.md", b"Native derived Markdown fixture\n")
    return module, target, review_path, files


@pytest.mark.parametrize("artifact", ["canonical", "review", "native_exit"])
def test_mutation_during_preparation_refuses_before_output_then_restores(
    publisher, monkeypatch, capsys, artifact
):
    module, target, review_path, files = publisher
    module.main()
    assert json.loads(capsys.readouterr().out)["writes"] == 0
    mutated = {
        "canonical": target,
        "review": review_path,
        "native_exit": module.STATE / "terrabacter-canary-run-schema-001/native.exit",
    }[artifact]
    original = files[mutated]
    original_sanitize = module.sanitize
    changed = False

    def change_after_binding(text, counts):
        nonlocal changed
        if not changed:
            mutated.write_bytes(original + b" ")
            changed = True
        return original_sanitize(text, counts)

    monkeypatch.setattr(module, "sanitize", change_after_binding)
    with pytest.raises(ValueError, match="captured input changed before publication"):
        module.main()
    assert changed and mutated.read_bytes() == original + b" "
    assert not capsys.readouterr().out
    assert not module.OUT.exists()
    mutated.write_bytes(original)
    monkeypatch.setattr(module, "sanitize", original_sanitize)
    module.main()
    assert json.loads(capsys.readouterr().out)["writes"] == 0
