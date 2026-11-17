"""Run and retain CommunityMech completion-check evidence (2026-11-14).

Inputs: pinned checkout, installed uv environment, native just recipes.
Outputs: .temp/m5-completion-20261114 logs/checkpoints and a technical report.
Serves the requested M5 completion review; no validators or baselines are edited.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shlex
import shutil
import signal
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/m5-completion-20261114"
REPORT = ROOT / "reports/m5-completion-20261114"
PIN = "76aa644cd6803ea2c9545d4c704276ede219d354"
QC = (
    "lint",
    "test",
    "validate-all",
    "validate-taxa",
    "validate-strict",
    "validate-gtdb-all",
    "validate-scalars",
    "validate-scalars-idiomatic",
    "validate-terms-all",
    "validate-terms-taxa",
)
CANARY = ["validate-scalars", "kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml"]
DIAGNOSTICS = (
    "validate-scalars",
    "validate-strict",
    "validate-gtdb-all",
    "validate-scalars-idiomatic",
    "validate-taxa",
    "validate-terms-taxa",
    "validate-terms-all",
    "validate-products",
    "check-docs-current",
    "validate-all",
    "validate-references-all",
)


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def write_json(path, value):
    temporary = path.with_suffix(path.suffix + ".writing")
    temporary.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def environment():
    env = dict(os.environ)
    env.update(
        PATH="/opt/homebrew/bin:/Users/marcin/.local/bin:/usr/bin:/bin:/usr/sbin:/sbin",
        UV_NO_SYNC="1",
        JUST_NO_DOTENV="true",
        GIT_TERMINAL_PROMPT="0",
        PYTHONDONTWRITEBYTECODE="1",
        PYTHONUNBUFFERED="1",
        NO_COLOR="1",
        TERM="dumb",
    )
    # Reference fetches must not disclose a personal email through polite pools.
    for name in ("EMAIL", "NCBI_EMAIL", "ENTREZ_EMAIL", "CROSSREF_MAILTO", "OPENALEX_MAILTO"):
        env.pop(name, None)
    return env


def stage_status(log, exit_code, recipes, dry_run=False):
    if dry_run:
        return [{"recipe": recipe, "status": "DRY RUN"} for recipe in recipes]
    started = re.findall(r"(?:===>|==>)\s*[Rr]unning recipe [`']?([^`'\s:]+)", log)
    # Use just's recipe-start markers, never infer execution from its dependency list.
    rows = []
    for recipe in recipes:
        if recipe not in started:
            status = "NOT RUN"
        else:
            begin = next(
                match.end()
                for match in re.finditer(
                    r"(?:===>|==>)\s*[Rr]unning recipe [`']?"
                    + re.escape(recipe)
                    + r"(?:[`'\s:]|$)",
                    log,
                )
            )
            following = re.search(r"(?:===>|==>)\s*[Rr]unning recipe", log[begin:])
            segment = log[begin : begin + following.start()] if following else log[begin:]
            if "SKIPPED, NOT PASSED" in segment:
                status = "SKIPPED" if exit_code == 0 or following else "FAILED WITH SKIPS"
            elif re.search(r"error: Recipe [`']" + re.escape(recipe) + r"[`'].*failed", segment):
                status = "FAILED"
            elif following or exit_code == 0:
                status = "PASSED"
            else:
                status = "FAILED"
        rows.append({"recipe": recipe, "status": status})
    return rows


def run_check(
    name, recipe, *, dry_run=False, no_deps=False, native_command=None, expected_revision=PIN
):
    STATE.mkdir(parents=True, exist_ok=True)
    result_path = STATE / f"{name}.json"
    if result_path.exists() or (STATE / f"{name}.log").exists():
        raise ValueError(f"refusing to overwrite retained run: {name}")
    if git("rev-parse", "HEAD") != expected_revision:
        raise ValueError("checkout HEAD differs from the pinned review baseline")
    if git("remote", "get-url", "origin") != "https://github.com/CultureBotAI/CommunityMech.git":
        raise ValueError("unexpected repository identity")
    if not dry_run:
        install = STATE / "install.exit"
        if not install.is_file() or install.read_text().strip() != "0":
            raise ValueError("environment installation has not completed successfully")
    env = environment()
    executable = shutil.which("just", path=env["PATH"])
    if executable is None:
        raise ValueError("just is unavailable")
    command = [executable, "--verbose", "--no-dotenv", "--color", "never"]
    if dry_run:
        command.append("--dry-run")
    if no_deps:
        command.append("--no-deps")
    command.extend(recipe)
    ordered = []
    if native_command is not None:
        command = native_command
    else:
        ordered = list(QC) if recipe[0] in {"qc", "qc-references"} and not no_deps else []
        if recipe[0] == "qc-references":
            ordered.append("qc")
            ordered.append("validate-references-all")
        ordered.append(recipe[0])
    result = {
        "name": name,
        "started_at": now(),
        "status": "RUNNING",
        "head": expected_revision,
        "branch": git("branch", "--show-current"),
        "cwd": str(ROOT),
        "python": sys.version,
        "command": command,
        "environment_overrides": {
            key: env[key]
            for key in (
                "UV_NO_SYNC",
                "JUST_NO_DOTENV",
                "GIT_TERMINAL_PROMPT",
                "PYTHONDONTWRITEBYTECODE",
                "NO_COLOR",
                "TERM",
            )
        },
        "runner_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "uv_lock_sha256": hashlib.sha256((ROOT / "uv.lock").read_bytes()).hexdigest(),
        "justfile_sha256": hashlib.sha256((ROOT / "justfile").read_bytes()).hexdigest(),
        "initial_git_status": git("status", "--short"),
        "dry_run": dry_run,
        "diagnostic_no_deps": no_deps,
        "log": str((STATE / f"{name}.log").relative_to(ROOT)),
    }
    write_json(result_path, result)
    with (STATE / f"{name}.log").open("w", encoding="utf-8") as handle:
        process = subprocess.run(
            command, cwd=ROOT, env=env, stdout=handle, stderr=subprocess.STDOUT
        )
    log = (STATE / f"{name}.log").read_text(encoding="utf-8", errors="replace")
    result.update(
        finished_at=now(),
        exit_code=process.returncode,
        status="PASSED" if process.returncode == 0 else "FAILED",
        stages=stage_status(log, process.returncode, ordered, dry_run),
        log_bytes=(STATE / f"{name}.log").stat().st_size,
        log_sha256=hashlib.sha256((STATE / f"{name}.log").read_bytes()).hexdigest(),
        skip_markers=[line for line in log.splitlines() if "SKIPPED, NOT PASSED" in line],
        final_git_status=git("status", "--short"),
    )
    if result["skip_markers"] and process.returncode == 0 and not dry_run:
        result["status"] = "COMPLETED WITH SKIPS"
    write_json(result_path, result)
    (STATE / f"{name}.exit").write_text(str(process.returncode) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {"name": name, "exit_code": process.returncode, "log_bytes": result["log_bytes"]}
        )
    )
    return process.returncode


def fetch_historical_bases():
    """Execute the existing CI prerequisite, preserving its exact commit identities."""
    workflow = (ROOT / ".github/workflows/validate-strict.yaml").read_text(encoding="utf-8")
    block = workflow.split("      - name: Fetch historical cache review bases\n", 1)[1]
    block = block.split("\n      - ", 1)[0]
    command = shlex.split(block.split("run: |", 1)[1].replace("\\\n", " "))
    if (
        command[:4] != ["git", "fetch", "--no-tags", "origin"]
        or not all(re.fullmatch(r"[0-9a-f]{40}", value) for value in command[4:])
        or not command[4:]
    ):
        raise ValueError("historical-base CI command does not have the expected immutable shape")
    before = {}
    for revision in command[4:]:
        before[revision] = (
            subprocess.run(
                ["git", "cat-file", "-e", revision + "^{commit}"],
                cwd=ROOT,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            ).returncode
            == 0
        )
    code = run_check("historical-bases-fetch", [], native_command=command)
    if code:
        return code
    objects = []
    for revision in command[4:]:
        observed = git("rev-parse", revision + "^{commit}")
        if observed != revision:
            raise ValueError("fetched historical commit identity mismatch")
        objects.append(
            {
                "commit": observed,
                "tree": git("rev-parse", revision + "^{tree}"),
                "present_before_fetch": before[revision],
            }
        )
    write_json(
        STATE / "historical-bases-verified.json",
        {
            "head_unchanged": git("rev-parse", "HEAD") == PIN,
            "source": ".github/workflows/validate-strict.yaml",
            "verified_at": now(),
            "objects": objects,
        },
    )
    return 0


def interrupt_invalid_environment_run(pid):
    """Interrupt only this checkout's pytest child after the known bad env value."""
    expected = f"{ROOT}/.venv/bin/python {ROOT}/.venv/bin/pytest tests/ -v"
    command = subprocess.check_output(["ps", "-p", str(pid), "-o", "command="], text=True).strip()
    if command != expected:
        raise ValueError(
            "refusing to interrupt any process except this checkout's exact pytest command"
        )
    ancestor = pid
    ancestry = []
    for _ in range(6):
        row = subprocess.check_output(
            ["ps", "-p", str(ancestor), "-o", "ppid=,command="], text=True
        ).strip()
        parent, text = row.split(None, 1)
        ancestry.append({"pid": ancestor, "ppid": int(parent), "command": text})
        if text == ".venv/bin/python scripts/adhoc/m5_completion_checks.py qc-references":
            break
        ancestor = int(parent)
    else:
        raise ValueError("pytest is not descended from this owned qc-references launcher")
    receipt = STATE / "invalid-launcher-interruption.json"
    if receipt.exists():
        raise ValueError("interruption receipt already exists")
    write_json(
        receipt,
        {
            "time": now(),
            "pid": pid,
            "signal": "SIGINT",
            "ancestry": ancestry,
            "reason": "JUST_NO_DOTENV=1 is invalid; just requires true/false. Preserve this attempt and rerun after a canary.",
            "git_status_before": git("status", "--short"),
        },
    )
    os.kill(pid, signal.SIGINT)


def diagnostic_batch(expected_revision):
    """Run downstream gates serially, retaining each native result independently."""
    results = []
    for recipe in DIAGNOSTICS:
        name = "diagnostic-" + recipe
        checkpoint = STATE / f"{name}.json"
        if checkpoint.exists():
            previous = json.loads(checkpoint.read_text())
            if (
                "exit_code" not in previous
                or previous["head"] != expected_revision
                or previous["environment_overrides"].get("JUST_NO_DOTENV") != "true"
            ):
                raise ValueError(f"cannot reuse incomplete or incompatible diagnostic: {name}")
            code = previous["exit_code"]
        else:
            code = run_check(name, [recipe], no_deps=True, expected_revision=expected_revision)
        results.append({"name": name, "exit_code": code})
        write_json(
            STATE / "diagnostic-batch-progress.json", {"checks": results, "updated_at": now()}
        )
    return int(any(result["exit_code"] != 0 for result in results))


def summarize():
    REPORT.mkdir(parents=True, exist_ok=True)
    results = [
        json.loads(path.read_text())
        for path in sorted(STATE.glob("*.json"))
        if path.name != "summary.json"
    ]
    results = [result for result in results if "command" in result]
    for result in results:
        if (
            result["name"] == "qc-references"
            and (STATE / "invalid-launcher-interruption.json").exists()
        ):
            result["attempt_disposition"] = "INVALID LAUNCHER; INTERRUPTED"
        log = (ROOT / result["log"]).read_text(encoding="utf-8", errors="replace")
        summaries = [
            line
            for line in log.splitlines()
            if re.match(r"^=+ .*\b(?:passed|failed|skipped)\b.*\bin [0-9.]+s", line)
        ]
        result["pytest_summaries"] = summaries
        result["pytest_counts"] = {
            key: int(value)
            for value, key in re.findall(
                r"\b(\d+) (passed|failed|skipped|deselected|xfailed|xpassed|errors?)\b",
                summaries[-1] if summaries else "",
            )
        }
        result["pytest_failures"] = [
            line for line in log.splitlines() if line.startswith(("FAILED tests/", "ERROR tests/"))
        ]
        result["pytest_skipped_cases"] = [
            line for line in log.splitlines() if line.startswith("tests/") and " SKIPPED " in line
        ]
        stage_counts = {}
        for stage in result.get("stages", []):
            status = stage["status"]
            stage_counts[status] = stage_counts.get(status, 0) + 1
        result["native_stage_counts"] = stage_counts
    write_json(
        REPORT / "technical-checks.json",
        {"baseline": PIN, "generated_at": now(), "checks": results},
    )
    lines = [
        "# M5 technical checks",
        "",
        f"Baseline: `{PIN}`",
        "",
        "Aggregate results retain native dependency stops. Separate diagnostics do not repair an aggregate failure.",
        "",
        "| Run | Status | Exit | Log bytes |",
        "|---|---|---:|---:|",
    ]
    for result in results:
        lines.append(
            f"| {result['name']} | {result.get('attempt_disposition', result['status'])} | {result.get('exit_code', 'pending')} | {result.get('log_bytes', 0)} |"
        )
    for result in results:
        lines.extend(["", "## " + result["name"], ""])
        lines.append("Command: `" + " ".join(result["command"]) + "`")
        lines.append("")
        lines.append(f"Log: `{result['log']}`")
        if result.get("attempt_disposition"):
            lines.append(
                "Invalid launcher environment; interrupted deliberately. This attempt is not a repository-failure conclusion."
            )
        lines.extend(["", *result["pytest_summaries"]])
        if result["pytest_counts"].get("skipped"):
            lines.append("Skipped tests are not passed checks; see the JSON for their exact names.")
        if result["pytest_failures"]:
            lines.extend(["", "```text", *result["pytest_failures"], "```"])
        if result.get("skip_markers"):
            lines.extend(["", "```text", *result["skip_markers"], "```"])
        if result.get("stages"):
            lines.extend(["", "| Native recipe | Status |", "|---|---|"])
            lines.extend(f"| {item['recipe']} | {item['status']} |" for item in result["stages"])
            lines.append("")
    (REPORT / "technical-checks.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(str(REPORT / "technical-checks.md"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "mode",
        choices=(
            "plan",
            "canary",
            "qc",
            "qc-references",
            "diagnostic",
            "diagnostic-batch",
            "run",
            "pytest",
            "history-fetch",
            "interrupt-invalid-run",
            "summary",
        ),
    )
    parser.add_argument(
        "--recipe",
        choices=(*QC, "validate-references-all", "validate-products", "check-docs-current"),
    )
    parser.add_argument("--name", help="unique evidence name for run mode")
    parser.add_argument(
        "--expected-revision",
        default=PIN,
        help="full expected HEAD SHA; defaults to the original baseline",
    )
    parser.add_argument(
        "--pid", type=int, help="exact owned pytest PID for invalid-run interruption"
    )
    parser.add_argument(
        "--arguments", nargs=argparse.REMAINDER, help="native just recipe and arguments"
    )
    args = parser.parse_args()
    if not re.fullmatch(r"[0-9a-f]{40}", args.expected_revision):
        parser.error("--expected-revision requires a complete 40-character commit SHA")
    if args.mode == "interrupt-invalid-run":
        if args.pid is None:
            parser.error("interrupt-invalid-run requires --pid")
        interrupt_invalid_environment_run(args.pid)
        return 0
    if args.mode == "history-fetch":
        if args.expected_revision != PIN:
            parser.error("history-fetch is recorded only against the original baseline")
        return fetch_historical_bases()
    if args.mode == "diagnostic-batch":
        return diagnostic_batch(args.expected_revision)
    if args.mode in {"run", "pytest"}:
        if not args.name or not re.fullmatch(r"[a-z0-9][a-z0-9_-]{0,80}", args.name):
            parser.error("run requires a simple unique --name")
        if not args.arguments or args.arguments[0].startswith("-"):
            parser.error("run requires --arguments RECIPE [ARGS...]")
        if args.mode == "pytest":
            return run_check(
                args.name,
                [],
                native_command=["uv", "run", "pytest", *args.arguments],
                expected_revision=args.expected_revision,
            )
        return run_check(args.name, args.arguments, expected_revision=args.expected_revision)
    if args.mode == "summary":
        summarize()
        return 0
    if args.mode == "plan":
        return run_check(
            "plan-qc", ["qc"], dry_run=True, expected_revision=args.expected_revision
        ) or run_check(
            "plan-qc-references",
            ["qc-references"],
            dry_run=True,
            expected_revision=args.expected_revision,
        )
    if args.mode == "canary":
        return run_check("canary", CANARY, expected_revision=args.expected_revision)
    if args.mode == "diagnostic":
        if args.recipe is None:
            parser.error("diagnostic requires --recipe")
        return run_check(
            "diagnostic-" + args.recipe,
            [args.recipe],
            no_deps=True,
            expected_revision=args.expected_revision,
        )
    return run_check(args.mode, [args.mode], expected_revision=args.expected_revision)


if __name__ == "__main__":
    raise SystemExit(main())
