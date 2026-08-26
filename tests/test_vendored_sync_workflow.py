"""Offline contract tests for the claw-authoritative vendored-sync workflow."""

from __future__ import annotations

import os
import subprocess
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "vendored-sync.yaml"
OPERATIONAL_AUTHORITY_SURFACES = (WORKFLOW, ROOT / "justfile")


def _checker_run_block() -> str:
    workflow = yaml.safe_load(WORKFLOW.read_text(encoding="utf-8"))
    steps = workflow["jobs"]["vendored-sync"]["steps"]
    return next(step["run"] for step in steps if "check_vendored_sync.sh" in step.get("run", ""))


def _run_with_statuses(
    tmp_path: Path, statuses: list[int]
) -> tuple[subprocess.CompletedProcess[str], int]:
    scripts = tmp_path / "scripts"
    scripts.mkdir()
    counter = tmp_path / "checker-calls"
    counter.write_text("0\n", encoding="utf-8")
    cases = "\n".join(
        f"  {attempt}) exit {status} ;;" for attempt, status in enumerate(statuses, start=1)
    )
    checker = scripts / "check_vendored_sync.sh"
    checker.write_text(
        f"""#!/usr/bin/env bash
set -u
count=$(cat "$CHECKER_COUNTER")
count=$((count + 1))
printf '%s\\n' "$count" > "$CHECKER_COUNTER"
case "$count" in
{cases}
  *) exit 99 ;;
esac
""",
        encoding="utf-8",
    )

    env = os.environ.copy()
    env["CHECKER_COUNTER"] = str(counter)
    # Override only the workflow's backoff delay; the checker invocation and
    # exit-code control flow execute exactly as checked into the workflow.
    shell_program = "sleep() { :; }\n" + _checker_run_block()
    result = subprocess.run(
        ["bash", "-c", shell_program],
        cwd=tmp_path,
        env=env,
        capture_output=True,
        text=True,
        timeout=10,
        check=False,
    )
    return result, int(counter.read_text(encoding="utf-8").strip())


def test_workflow_declares_claw_as_authority() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    workflow = yaml.safe_load(text)
    triggers = workflow.get("on", workflow.get(True))
    concurrency = workflow["concurrency"]

    assert "CultureBotAI/culturebotai-claw" in text
    assert "pinned claw manifest" in text
    assert "canonical hub" not in text
    assert "CultureBotAI/CultureMech) at the commit pinned" not in text
    assert all("paths" not in (config or {}) for config in triggers.values())
    assert workflow["jobs"]["vendored-sync"]["timeout-minutes"] == 5
    assert "github.run_id" in concurrency["group"]
    assert concurrency["cancel-in-progress"] == "${{ github.event_name == 'pull_request' }}"


def test_operational_surfaces_do_not_restore_mech_authority() -> None:
    text = "\n".join(path.read_text(encoding="utf-8") for path in OPERATIONAL_AUTHORITY_SURFACES)

    assert "CultureBotAI/culturebotai-claw" in text
    assert "CultureBotAI/CultureMech@<scripts/.vendored_canon_ref>" not in text
    assert "against the canonical hub" not in text


def test_success_is_not_retried(tmp_path: Path) -> None:
    result, calls = _run_with_statuses(tmp_path, [0])

    assert result.returncode == 0, result.stderr
    assert calls == 1


def test_exit_one_is_retried_and_can_recover(tmp_path: Path) -> None:
    result, calls = _run_with_statuses(tmp_path, [1, 1, 0])

    assert result.returncode == 0, result.stderr
    assert calls == 3
    assert result.stderr.count("retrying in 5s") == 2


def test_exit_one_exhausts_three_attempts(tmp_path: Path) -> None:
    result, calls = _run_with_statuses(tmp_path, [1, 1, 1])

    assert result.returncode == 1
    assert calls == 3
    assert "after 3 attempts" in result.stderr


def test_exit_two_is_an_immediate_local_failure(tmp_path: Path) -> None:
    result, calls = _run_with_statuses(tmp_path, [2])

    assert result.returncode == 2
    assert calls == 1
    assert "local precondition failure" in result.stderr
    assert "retrying in 5s" not in result.stderr


def test_unexpected_exit_fails_closed_without_retry(tmp_path: Path) -> None:
    result, calls = _run_with_statuses(tmp_path, [99])

    assert result.returncode == 99
    assert calls == 1
    assert "unexpected exit 99" in result.stderr
    assert "retrying in 5s" not in result.stderr
