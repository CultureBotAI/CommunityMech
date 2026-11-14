"""Exercise isolated retry provenance for M5 helper issue #2783 (2026-11-14).

Inputs: toy Git repositories and mocked native check execution. Outputs: temporary
plans, backups and receipts only; no actual M5 access or long-running QC.
"""

import hashlib
import importlib.util
import json
import subprocess
from pathlib import Path
from unittest.mock import Mock

import pytest

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts/adhoc"
PIN = "a" * 40


def load_helper(name, monkeypatch):
    monkeypatch.syspath_prepend(str(SCRIPTS))
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def snapshot(folder):
    return {
        str(path.relative_to(folder)): (path.read_bytes(), path.stat().st_mtime_ns)
        for path in folder.rglob("*")
        if path.is_file()
    }


def invoke(module, monkeypatch, *arguments):
    monkeypatch.setattr("sys.argv", [module.__name__, *arguments])
    return module.main()


@pytest.fixture
def sync_repo(tmp_path, monkeypatch):
    module = load_helper("sync_m5_final_revision_20261114", monkeypatch)
    root = tmp_path / "repo"
    root.mkdir()
    state = root / ".temp/m5-completion-20261114"
    state.mkdir(parents=True)
    monkeypatch.setattr(module, "ROOT", root)
    monkeypatch.setattr(module, "STATE", state)

    def git(*args):
        return subprocess.check_output(["git", *args], cwd=root, text=True).strip()

    git("init", "-b", "main")
    git("config", "user.name", "Test")
    git("config", "user.email", "test@example.invalid")
    git("remote", "add", "origin", "https://github.com/CultureBotAI/CommunityMech.git")
    (root / ".gitignore").write_text(".temp/\n")
    (root / "tests").mkdir()
    test = root / "tests/test_no_new_bracketed_snippets.py"
    test.write_text("baseline\n")
    git("add", ".")
    git("commit", "-qm", "baseline")
    base = git("rev-parse", "HEAD")
    test.write_text("target version\n")
    (root / "notes.txt").write_text("target notes\n")
    git("add", ".")
    git("commit", "-qm", "target")
    target = git("rev-parse", "HEAD")
    git("checkout", "--detach", base)
    test.write_text("retained local test\n")
    (root / "notes.txt").write_text("retained local notes\n")
    return module, root, state, git, base, target


@pytest.mark.parametrize("attempt", [None, "c2"])
def test_sync_plan_apply_preserves_earlier_receipts_and_refuses_reuse(
    sync_repo, attempt, monkeypatch
):
    module, root, state, git, base, target = sync_repo
    arguments = ["--current", base, "--target", target]
    prefix = "final"
    if attempt:
        arguments.extend(["--attempt", attempt])
        prefix += "-" + attempt
        (state / "final-sync-plan.json").write_text("original plan\n")
        (state / "final-sync-receipt.json").write_text("original receipt\n")
    legacy = snapshot(state)
    invoke(module, monkeypatch, *arguments)
    plan = state / f"{prefix}-sync-plan.json"
    planned = (plan.read_bytes(), plan.stat().st_mtime_ns)
    assert git("rev-parse", "HEAD") == base
    invoke(module, monkeypatch, *arguments, "--apply")
    assert git("rev-parse", "HEAD") == target
    assert (plan.read_bytes(), plan.stat().st_mtime_ns) == planned
    result = json.loads((state / f"{prefix}-sync-receipt.json").read_text())
    backup = root / result["backup"]
    assert (backup / "notes.txt").read_text() == "retained local notes\n"
    assert (
        backup / "tests/test_no_new_bracketed_snippets.py"
    ).read_text() == "retained local test\n"
    assert (root / "notes.txt").read_text() == "target notes\n"
    for path, original in legacy.items():
        assert snapshot(state)[path] == original
    before = snapshot(state)
    with pytest.raises(ValueError, match="retained sync attempt"):
        invoke(module, monkeypatch, *arguments, "--apply")
    assert snapshot(state) == before


def test_duplicate_plan_refuses_before_any_output_change(sync_repo, monkeypatch):
    module, _, state, _, base, target = sync_repo
    arguments = ["--current", base, "--target", target, "--attempt", "c2"]
    invoke(module, monkeypatch, *arguments)
    before = snapshot(state)
    guard = Mock(side_effect=AssertionError("duplicate must fail before Git inspection"))
    monkeypatch.setattr(module, "git", guard)
    with pytest.raises(ValueError, match="retained sync attempt"):
        invoke(module, monkeypatch, *arguments)
    guard.assert_not_called()
    assert snapshot(state) == before


@pytest.fixture
def launcher(tmp_path, monkeypatch):
    module = load_helper("run_m5_final_checks_20261114", monkeypatch)
    root = tmp_path
    state = root / ".temp/m5-completion-20261114"
    state.mkdir(parents=True)
    monkeypatch.setattr(module, "ROOT", root)
    monkeypatch.setattr(module, "STATE", state)
    monkeypatch.setattr(module.importlib.metadata, "version", lambda _: "0.2.1")

    def git(*args):
        if args == ("rev-parse", "HEAD"):
            return PIN
        if args[0] == "hash-object":
            return "b" * 40
        return ""

    monkeypatch.setattr(module, "git", git)
    for stem in module.RECORDS.values():
        path = root / "kb/communities" / (stem + ".yaml")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("id: fixture\n")
    calls = []

    def run_check(name, recipe, **kwargs):
        calls.append(name)
        log = state / (name + ".log")
        log.write_text("mock native result\n")
        result = {
            "head": kwargs["expected_revision"],
            "exit_code": 0,
            "log": str(log.relative_to(root)),
            "log_sha256": hashlib.sha256(log.read_bytes()).hexdigest(),
            "stages": [
                {"recipe": "test", "status": "PASSED"},
                {"recipe": "validate-references-all", "status": "PASSED"},
            ],
        }
        (state / (name + ".json")).write_text(json.dumps(result))
        (state / (name + ".exit")).write_text("0\n")
        if "--out" in recipe:
            (root / recipe[recipe.index("--out") + 1]).write_text("header\n")
        return 0

    monkeypatch.setattr(module, "run_check", run_check)
    return module, state, calls


@pytest.mark.parametrize("attempt", [None, "c2"])
def test_fresh_launcher_attempt_runs_each_stage_and_preserves_legacy(
    launcher, attempt, monkeypatch
):
    module, state, calls = launcher
    arguments = ["--expected-revision", PIN]
    prefix = "final"
    if attempt:
        arguments.extend(["--attempt", attempt])
        prefix += "-" + attempt
        (state / "final-orchestration-inputs.json").write_text("old input receipt\n")
        (state / "final-checks-progress.json").write_text("old progress\n")
    old = snapshot(state)
    for stage in ("plan", "canary", "completion"):
        assert invoke(module, monkeypatch, stage, *arguments) == 0
    assert all(name.startswith(prefix + "-") for name in calls)
    assert f"{prefix}-qc-references" in calls
    assert (state / f"{prefix}-000025-strict.tsv").is_file()
    assert (state / f"{prefix}-000025-strict-artifact.json").is_file()
    assert (state / f"{prefix}-checks-progress.json").is_file()
    for path, original in old.items():
        assert snapshot(state)[path] == original
    before, call_count = snapshot(state), len(calls)
    with pytest.raises(ValueError, match="retained stage outputs"):
        invoke(module, monkeypatch, "completion", *arguments)
    assert snapshot(state) == before
    assert len(calls) == call_count


@pytest.mark.parametrize(
    "stage,artifact",
    [
        ("plan", "plan-qc-references.exit"),
        ("canary", "environment-canary.log"),
        ("completion", "checks-progress.json"),
        ("completion", "000025-strict.tsv"),
        ("completion", "000516-inputs.json.writing"),
    ],
)
def test_partial_launcher_attempt_refuses_before_startup_write(
    launcher, stage, artifact, monkeypatch
):
    module, state, calls = launcher
    (state / ("final-c2-" + artifact)).write_text("preserved partial evidence\n")
    before = snapshot(state)
    with pytest.raises(ValueError, match="retained stage outputs"):
        invoke(module, monkeypatch, stage, "--expected-revision", PIN, "--attempt", "c2")
    assert snapshot(state) == before
    assert not calls
    assert not (state / "final-c2-orchestration-inputs.json").exists()


@pytest.mark.parametrize("attempt", ["", "../prior", "Upper"])
@pytest.mark.parametrize(
    "helper", ["sync_m5_final_revision_20261114", "run_m5_final_checks_20261114"]
)
def test_invalid_attempt_is_rejected_without_files(helper, attempt, tmp_path, monkeypatch):
    module = load_helper(helper, monkeypatch)
    monkeypatch.setattr(module, "STATE", tmp_path)
    arguments = (
        ["--current", PIN, "--target", "b" * 40]
        if helper.startswith("sync_")
        else ["plan", "--expected-revision", PIN]
    )
    with pytest.raises(SystemExit):
        invoke(module, monkeypatch, *arguments, "--attempt", attempt)
    assert not list(tmp_path.iterdir())
