"""Protect the durable M5 evidence index and interrupted-run provenance (#2779)."""

import hashlib
import importlib.util
import json
from pathlib import Path

import pytest

SCRIPT = (
    Path(__file__).resolve().parents[1] / "scripts/adhoc/export_m5_technical_evidence_20261114.py"
)


@pytest.fixture
def exporter(tmp_path, monkeypatch):
    spec = importlib.util.spec_from_file_location("m5_evidence_export", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.ROOT = tmp_path
    module.STATE = tmp_path / ".temp/m5-completion-20261114"
    module.OUT = tmp_path / "reports/m5-completion-20261114/technical-evidence"
    module.STATE.mkdir(parents=True)
    monkeypatch.setattr("sys.argv", [str(SCRIPT)])
    return module


def add_run(module, name, exit_code=0):
    log = module.STATE / f"{name}.log"
    log.write_text(f"Native output for {name}: exit {exit_code}\n")
    (module.STATE / f"{name}.exit").write_text(f"{exit_code}\n")
    result = {
        "name": name,
        "command": ["just", "qc"],
        "status": "PASSED" if exit_code == 0 else "FAILED",
        "exit_code": exit_code,
        "log": str(log.relative_to(module.ROOT)),
        "log_sha256": hashlib.sha256(log.read_bytes()).hexdigest(),
    }
    (module.STATE / f"{name}.json").write_text(json.dumps(result))


def snapshot(directory):
    return {
        str(path.relative_to(directory)): (path.read_bytes(), path.stat().st_mtime_ns)
        for path in directory.rglob("*")
        if path.is_file()
    }


def test_filtered_export_preserves_previous_index_entries(exporter, monkeypatch):
    add_run(exporter, "old-failed", 1)
    exporter.main()
    original = snapshot(exporter.OUT)
    add_run(exporter, "new-passed")
    monkeypatch.setattr("sys.argv", [str(SCRIPT), "--name", "new-passed"])
    exporter.main()
    index = (exporter.OUT / "README.md").read_text()
    assert "| old-failed | FAILED | 1 |" in index
    assert "| new-passed | PASSED | 0 |" in index
    for name, retained in original.items():
        if name != "README.md":
            path = exporter.OUT / name
            assert (path.read_bytes(), path.stat().st_mtime_ns) == retained


def test_unknown_selection_changes_no_published_evidence(exporter, monkeypatch):
    add_run(exporter, "old-failed", 1)
    exporter.main()
    before = snapshot(exporter.OUT)
    monkeypatch.setattr("sys.argv", [str(SCRIPT), "--name", "missing"])
    with pytest.raises(SystemExit) as error:
        exporter.main()
    assert error.value.code == 2
    assert snapshot(exporter.OUT) == before


def test_superseded_baseline_is_not_a_repository_failure(exporter):
    add_run(exporter, "diagnostic-validate-terms-all", 143)
    for name in ("baseline-diagnostic-interruption", "baseline-diagnostic-termination"):
        (exporter.STATE / f"{name}.json").write_text(json.dumps({"reason": "superseded"}))
    exporter.main()
    result = json.loads((exporter.OUT / "diagnostic-validate-terms-all.receipt.json").read_text())
    assert result["attempt_disposition"] == "SUPERSEDED BASELINE; INTERRUPTED"
    report = (exporter.OUT.parent / "technical-checks.md").read_text()
    assert "Superseded baseline" in report
    assert "Invalid launcher environment" not in report
    for name in ("baseline-diagnostic-interruption", "baseline-diagnostic-termination"):
        assert (exporter.OUT / f"{name}.json").stat().st_size > 0


def test_named_attempt_controls_preserve_both_versions(exporter):
    names = (
        "final-sync-plan",
        "final-sync-receipt",
        "final-orchestration-inputs",
    )
    for name in names:
        (exporter.STATE / f"{name}.json").write_text(json.dumps({"attempt": "first"}))
    exporter.main()
    first = snapshot(exporter.OUT)
    later = [name.replace("final-", "final-c2-", 1) for name in names]
    later.append("c1-reference-supersession")
    for name in later:
        (exporter.STATE / f"{name}.json").write_text(json.dumps({"attempt": "second"}))
    exporter.main()
    for name in later:
        source = exporter.STATE / f"{name}.json"
        published = json.loads((exporter.OUT / f"{name}.json").read_text())
        assert published["source_sha256"] == hashlib.sha256(source.read_bytes()).hexdigest()
        assert published["receipt"] == {"attempt": "second"}
    for name, retained in first.items():
        if name != "README.md":
            path = exporter.OUT / name
            assert (path.read_bytes(), path.stat().st_mtime_ns) == retained
