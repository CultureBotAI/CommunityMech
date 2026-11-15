"""Retain unique command receipts for Phase 2 schema work, 2026-11-15.

Inputs: a run name and explicit command; current Git revision and lockfile.
Outputs: immutable log/JSON/exit triplets in .temp/phase2-schema-20261115.
Serves #2700–2704, #2429 and the treatment-arm schema follow-up.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp" / "phase2-schema-20261115"


def now():
    return datetime.now(timezone.utc).isoformat()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("name")
    parser.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", args.name) or not args.command:
        parser.error("use a simple unique name followed by a command")
    command = args.command[1:] if args.command[0] == "--" else args.command
    paths = [STATE / f"{args.name}.{suffix}" for suffix in ("log", "json", "exit")]
    if any(path.exists() or path.is_symlink() for path in paths):
        parser.error("refusing to overwrite an existing or partial run")
    STATE.mkdir(parents=True, exist_ok=True)
    receipt = {
        "name": args.name,
        "command": command,
        "started_at": now(),
        "head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "initial_git_status": subprocess.check_output(
            ["git", "status", "--short"], cwd=ROOT, text=True
        ),
        "uv_lock_sha256": hashlib.sha256((ROOT / "uv.lock").read_bytes()).hexdigest(),
    }
    env = os.environ.copy()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["JUST_NO_DOTENV"] = "1"
    with paths[0].open("xb") as handle:
        result = subprocess.run(command, cwd=ROOT, env=env, stdout=handle, stderr=subprocess.STDOUT)
    data = paths[0].read_bytes()
    receipt.update(
        finished_at=now(),
        exit_code=result.returncode,
        status="PASSED" if result.returncode == 0 else "FAILED",
        log_sha256=hashlib.sha256(data).hexdigest(),
        log_bytes=len(data),
    )
    with paths[1].open("x") as handle:
        handle.write(json.dumps(receipt, indent=2) + "\n")
    with paths[2].open("x") as handle:
        handle.write(str(result.returncode) + "\n")
    print(json.dumps(receipt, indent=2))
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
