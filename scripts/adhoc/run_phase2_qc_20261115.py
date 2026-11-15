"""Retain serial Phase 2 native QC evidence on M5 (2026-11-15, PR #2102 follow-up).

Inputs: explicit Git revision, frozen uv environment and native just recipes.
Outputs: exclusive logs/exits/receipts in the existing completion-runner state.
Reuses its tested fail-fast stage accounting: later QC gates stay NOT RUN.
This driver does not acquire references, edit records or declare scientific approval.
"""

import argparse
import hashlib
import json
import shutil
import subprocess
import sys

from m5_completion_checks import ROOT, STATE, environment, git, now, run_check

RECORD = "kb/communities/LBNL_Switchgrass_Soil_SynCom16.yaml"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=["install", "plan", "canary", "qc", "products", "docs"])
    parser.add_argument("--expected-revision", required=True)
    parser.add_argument("--attempt", required=True)
    args = parser.parse_args()
    if not args.attempt.replace("-", "").isalnum() or not args.attempt.isascii():
        parser.error("attempt must use ASCII letters, digits and hyphens")
    if git("rev-parse", "HEAD") != args.expected_revision:
        parser.error("HEAD differs from expected revision")
    if git("diff", "--name-only", "HEAD", "--"):
        parser.error("tracked checkout must be clean before native checks")
    prefix = f"phase2-{args.attempt}"
    STATE.mkdir(parents=True, exist_ok=True)
    if args.stage == "install":
        paths = [
            STATE / name
            for name in ("install.exit", f"{prefix}-install.json", f"{prefix}-install.log")
        ]
        if any(p.exists() for p in paths):
            parser.error("installation proof already exists; preserve it and use a fresh checkout")
        command = [
            shutil.which("uv", path=environment()["PATH"]),
            "sync",
            "--offline",
            "--frozen",
            "--extra",
            "dev",
            "--python",
            sys.executable,
        ]
        started = now()
        with paths[2].open("x") as handle:
            process = subprocess.run(
                command, cwd=ROOT, env=environment(), stdout=handle, stderr=subprocess.STDOUT
            )
        receipt = {
            "started_at": started,
            "finished_at": now(),
            "revision": args.expected_revision,
            "command": command,
            "exit_code": process.returncode,
            "log_sha256": hashlib.sha256(paths[2].read_bytes()).hexdigest(),
            "log_bytes": paths[2].stat().st_size,
        }
        with paths[1].open("x") as handle:
            json.dump(receipt, handle, indent=2)
            handle.write("\n")
        with paths[0].open("x") as handle:
            handle.write(str(process.returncode) + "\n")
        return process.returncode
    if args.stage == "plan":
        return run_check(
            f"{prefix}-plan", ["qc"], dry_run=True, expected_revision=args.expected_revision
        )
    if args.stage == "canary":
        return run_check(
            f"{prefix}-canary",
            ["validate-strict", RECORD],
            expected_revision=args.expected_revision,
        )
    canary = json.loads((STATE / f"{prefix}-canary.json").read_text())
    log = STATE / f"{prefix}-canary.log"
    exit_artifact = STATE / f"{prefix}-canary.exit"
    expected_command = [
        shutil.which("just", path=environment()["PATH"]),
        "--verbose",
        "--no-dotenv",
        "--color",
        "never",
        "validate-strict",
        RECORD,
    ]
    if (
        canary.get("name") != f"{prefix}-canary"
        or canary.get("head") != args.expected_revision
        or canary.get("exit_code") != 0
        or canary.get("status") != "PASSED"
        or canary.get("dry_run") is not False
        or canary.get("diagnostic_no_deps") is not False
        or not canary.get("finished_at")
        or canary.get("command") != expected_command
        or canary.get("stages") != [{"recipe": "validate-strict", "status": "PASSED"}]
        or canary.get("log") != str(log.relative_to(ROOT))
        or not exit_artifact.is_file()
        or exit_artifact.read_text().strip() != "0"
        or not log.is_file()
        or not log.stat().st_size
        or hashlib.sha256(log.read_bytes()).hexdigest() != canary["log_sha256"]
    ):
        parser.error("a persisted passing canary on this exact revision is required")
    recipe = {"qc": "qc", "products": "validate-products", "docs": "check-docs-current"}[args.stage]
    return run_check(f"{prefix}-{args.stage}", [recipe], expected_revision=args.expected_revision)


if __name__ == "__main__":
    raise SystemExit(main())
