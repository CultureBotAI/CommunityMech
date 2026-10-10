"""Exercise the actual advisory shell step with immutable event base commits."""

import os
import subprocess
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]


def _step():
    workflow = yaml.safe_load((ROOT / ".github/workflows/curation-history.yaml").read_text())
    return next(
        step
        for step in workflow["jobs"]["history"]["steps"]
        if step.get("name") == "Check for missing history records (advisory)"
    )


def _git(cwd, *args):
    return subprocess.run(
        ["git", *args], cwd=cwd, check=True, capture_output=True, text=True
    ).stdout.strip()


def _identity(path):
    _git(path, "config", "user.name", "Workflow test")
    _git(path, "config", "user.email", "workflow@example.invalid")


def _commit(path, files):
    for name, content in files.items():
        target = path / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content)
    _git(path, "add", "--", *files)
    _git(path, "commit", "-qm", "Fixture")
    return _git(path, "rev-parse", "HEAD")


@pytest.fixture
def repository(tmp_path):
    remote = tmp_path / "remote"
    remote.mkdir()
    _git(remote, "init", "-q", "-b", "main")
    _identity(remote)
    base = _commit(remote, {"kb/communities/example.yaml": "version: base\n"})
    _git(remote, "branch", "parent")
    checkout = tmp_path / "checkout"
    _git(tmp_path, "clone", "-q", str(remote), str(checkout))
    _identity(checkout)
    return remote, checkout, base


def _run(checkout, base):
    summary = checkout.parent / "summary.md"
    result = subprocess.run(
        ["bash", "-c", _step()["run"]],
        cwd=checkout,
        env={**os.environ, "BASE_SHA": base, "GITHUB_STEP_SUMMARY": str(summary)},
        capture_output=True,
        text=True,
    )
    return result, summary.read_text() if summary.exists() else ""


def test_workflow_uses_event_base_without_interpolating_branch_names():
    step = _step()
    assert step["if"] == "github.event_name == 'pull_request'"
    assert step["env"] == {"BASE_SHA": "${{ github.event.pull_request.base.sha }}"}
    assert "${{" not in step["run"]
    assert "github.base_ref" not in step["run"]


def test_deleted_parent_uses_local_commit_without_network(repository):
    remote, checkout, base = repository
    _commit(
        checkout,
        {
            "kb/communities/example.yaml": "version: changed\n",
            "history/records/example/event.yaml": "event: EDIT\n",
        },
    )
    _git(remote, "branch", "-D", "parent")
    _git(checkout, "update-ref", "-d", "refs/remotes/origin/parent")
    remote.rename(remote.with_name("offline"))
    result, summary = _run(checkout, base)
    assert result.returncode == 0, result.stderr
    assert "community records changed: **1**" in summary
    assert "history records added: **1**" in summary
    assert "Provenance recorded" in summary


def test_previous_branch_fetch_reproduces_deleted_parent_failure(repository):
    remote, checkout, _ = repository
    _git(remote, "branch", "-D", "parent")
    result = subprocess.run(
        ["git", "fetch", "--no-tags", "origin", "parent"],
        cwd=checkout,
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0
    assert "couldn't find remote ref parent" in result.stderr


def test_advanced_branch_cannot_change_event_comparison(repository):
    remote, checkout, base = repository
    _commit(remote, {"kb/communities/example.yaml": "version: later\n"})
    _git(remote, "branch", "-f", "parent", "HEAD")
    _git(checkout, "fetch", "-q", "origin")
    _git(checkout, "merge", "--ff-only", "origin/main")
    result, summary = _run(checkout, base)
    assert result.returncode == 0, result.stderr
    assert "community records changed: **1**" in summary
    assert "history records added: **0**" in summary
    assert "Advisory only; this does not block the build." in summary


def test_missing_local_base_fetches_exact_commit(repository):
    remote, checkout, _ = repository
    base = _commit(remote, {"kb/communities/example.yaml": "version: new base\n"})
    _git(remote, "branch", "-D", "parent")
    missing = subprocess.run(
        ["git", "cat-file", "-e", f"{base}^{{commit}}"], cwd=checkout, capture_output=True
    )
    assert missing.returncode != 0
    result, summary = _run(checkout, base)
    assert result.returncode == 0, result.stderr
    assert _git(checkout, "rev-parse", "FETCH_HEAD") == base
    assert "community records changed: **0**" in summary
    assert "No community records changed" in summary


def test_unavailable_base_fails_instead_of_reporting_false_green(repository):
    _, checkout, _ = repository
    result, summary = _run(checkout, "0" * 40)
    assert result.returncode != 0
    assert not summary
