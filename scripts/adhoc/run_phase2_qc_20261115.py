"""Retain serial Phase 2 native QC evidence on M5 (2026-11-15, PR #2102 follow-up).

Inputs: explicit Git revision, frozen uv environment and native just recipes.
Outputs: exclusive logs/exits/receipts in the existing completion-runner state.
Reuses its tested fail-fast stage accounting: later QC gates stay NOT RUN.
This driver does not acquire references, edit records or declare scientific approval.
"""

import argparse
import hashlib
import json
import re
import shlex
import shutil
import subprocess
import sys

from m5_completion_checks import ROOT, STATE, environment, git, now, run_check

RECORD = "kb/communities/LBNL_Switchgrass_Soil_SynCom16.yaml"


def historical_command():
    """Use the same immutable review-base prerequisite as native CI (#2813)."""
    workflow = (ROOT / ".github/workflows/validate-strict.yaml").read_text()
    block = workflow.split("      - name: Fetch historical cache review bases\n", 1)[1]
    block = block.split("\n      - ", 1)[0]
    command = shlex.split(block.split("run: |", 1)[1].replace("\\\n", " "))
    if (
        command[:4] != ["git", "fetch", "--no-tags", "origin"]
        or not command[4:]
        or not all(re.fullmatch(r"[0-9a-f]{40}", value) for value in command[4:])
    ):
        raise ValueError("unexpected native historical-base prerequisite")
    return command


def missing_history():
    return [
        revision
        for revision in historical_command()[4:]
        if subprocess.run(
            ["git", "cat-file", "-e", revision + "^{commit}"],
            cwd=ROOT,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        ).returncode
    ]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "stage", choices=["install", "plan", "history", "canary", "qc", "products", "docs"]
    )
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
    if args.stage == "history":
        proof = STATE / f"{prefix}-history-objects.json"
        if proof.exists():
            parser.error("historical object proof already exists; use a new attempt")
        before = missing_history()
        code = run_check(
            f"{prefix}-history",
            [],
            native_command=historical_command(),
            expected_revision=args.expected_revision,
        )
        if code:
            return code
        if missing_history() or git("rev-parse", "HEAD") != args.expected_revision:
            raise ValueError("historical acquisition did not preserve revision/object identities")
        objects = []
        for revision in historical_command()[4:]:
            if git("rev-parse", revision + "^{commit}") != revision:
                raise ValueError("historical commit identity mismatch")
            objects.append(
                {
                    "commit": revision,
                    "tree": git("rev-parse", revision + "^{tree}"),
                    "present_before_fetch": revision not in before,
                }
            )
        with proof.open("x") as handle:
            json.dump({"head": args.expected_revision, "objects": objects}, handle, indent=2)
            handle.write("\n")
        return 0
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
    if args.stage == "qc" and missing_history():
        parser.error("immutable review bases are missing; run this driver's history stage first")
    return run_check(f"{prefix}-{args.stage}", [recipe], expected_revision=args.expected_revision)


if __name__ == "__main__":
    raise SystemExit(main())
