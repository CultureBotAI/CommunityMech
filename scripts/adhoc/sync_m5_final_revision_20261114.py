"""Preserve owned M5 working copies before final fast-forward (2026-11-14).

Inputs: isolated checkout, explicit current/target revisions already fetched.
Outputs: per-file SHA-256 plan, byte-for-byte backups, and final sync receipt in
.temp/m5-completion-20261114. No original Documents checkout is touched.
Use --attempt c2 for a later sync; the matching plan may advance once to --apply.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/m5-completion-20261114"


def git(*args, binary=False):
    result = subprocess.check_output(["git", *args], cwd=ROOT)
    return result if binary else result.decode().strip()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--current", required=True)
    parser.add_argument("--target", required=True)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--attempt", help="new attempt ID; omitted preserves first-run names")
    args = parser.parse_args()
    if args.attempt is not None and not re.fullmatch(r"[a-z0-9][a-z0-9_-]{0,31}", args.attempt):
        parser.error("--attempt requires 1–32 lowercase letters, digits, underscores or hyphens")
    prefix = "final" + ("-" + args.attempt if args.attempt else "")
    plan_path = STATE / f"{prefix}-sync-plan.json"
    receipt_path = STATE / f"{prefix}-sync-receipt.json"
    backup = STATE / (f"pre-{prefix}-sync-" + args.target[:12])
    # A saved plan may advance once to apply, but no completed/partial attempt is reused.
    occupied = [path for path in (receipt_path, backup) if path.exists() or path.is_symlink()]
    if (plan_path.exists() or plan_path.is_symlink()) and not args.apply:
        occupied.append(plan_path)
    if occupied:
        raise ValueError("retained sync attempt already exists; use a new --attempt")
    if git("rev-parse", "HEAD") != args.current:
        raise ValueError("unexpected initial revision")
    if git("remote", "get-url", "origin") != "https://github.com/CultureBotAI/CommunityMech.git":
        raise ValueError("unexpected repository")
    if git("rev-parse", args.target + "^{commit}") != args.target:
        raise ValueError("target must be an available full immutable commit")
    subprocess.run(
        ["git", "merge-base", "--is-ancestor", args.current, args.target], cwd=ROOT, check=True
    )
    tracked = set(git("ls-tree", "-r", "--name-only", "HEAD").splitlines())
    target_paths = set(git("ls-tree", "-r", "--name-only", args.target).splitlines())
    dirty = set(git("diff", "--name-only", "HEAD", "--").splitlines())
    if dirty - {"tests/test_no_new_bracketed_snippets.py"}:
        raise ValueError("unexpected tracked modifications; preserve and investigate before sync")
    # Inspect target paths directly, including ignored files, for checkout collisions.
    conflicts = {path for path in target_paths - tracked if (ROOT / path).exists()}
    paths = sorted(dirty | conflicts)
    rows = []
    for name in paths:
        path = ROOT / name
        if not path.is_file() or path.is_symlink():
            raise ValueError(f"unsupported collision: {name}")
        source = path.read_bytes()
        target = git("show", args.target + ":" + name, binary=True)
        rows.append(
            {
                "path": name,
                "original_sha256": sha(source),
                "target_sha256": sha(target),
                "same_bytes": source == target,
                "tracked_change": name in dirty,
            }
        )
    receipt = {"current": args.current, "target": args.target, "files": rows, "applied": False}
    if args.attempt:
        receipt["attempt"] = args.attempt
    if plan_path.exists() or plan_path.is_symlink():
        if plan_path.is_symlink() or json.loads(plan_path.read_text()) != receipt:
            raise ValueError("retained plan differs from current inputs; use a new --attempt")
    else:
        STATE.mkdir(parents=True, exist_ok=True)
        with plan_path.open("x") as handle:
            handle.write(json.dumps(receipt, indent=2) + "\n")
    if not args.apply:
        print(
            json.dumps(
                {
                    "planned_files": len(rows),
                    "different_bytes": sum(not row["same_bytes"] for row in rows),
                }
            )
        )
        return
    backup.mkdir(exist_ok=False)
    # Back up everything and verify all copies before removing any checkout collision.
    for row in rows:
        source = ROOT / row["path"]
        destination = backup / row["path"]
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        if sha(destination.read_bytes()) != row["original_sha256"]:
            raise ValueError("backup verification failed")
    for row in rows:
        path = ROOT / row["path"]
        if sha(path.read_bytes()) != row["original_sha256"]:
            raise ValueError("a working copy changed during preservation")
        if row["tracked_change"]:
            subprocess.run(
                ["git", "restore", "--source=HEAD", "--staged", "--worktree", "--", row["path"]],
                cwd=ROOT,
                check=True,
            )
        else:
            path.unlink()
    subprocess.run(
        ["git", "merge", "--ff-only", args.target], cwd=ROOT, check=True, stdout=subprocess.DEVNULL
    )
    if git("rev-parse", "HEAD") != args.target:
        raise ValueError("final revision mismatch")
    for row in rows:
        if sha((ROOT / row["path"]).read_bytes()) != row["target_sha256"]:
            raise ValueError("final checkout bytes mismatch")
    receipt.update(
        applied=True, backup=str(backup.relative_to(ROOT)), final_status=git("status", "--short")
    )
    with receipt_path.open("x") as handle:
        handle.write(json.dumps(receipt, indent=2) + "\n")
    print(
        json.dumps(
            {
                "preserved_files": len(rows),
                "head": args.target,
                "backup": str(backup.relative_to(ROOT)),
            }
        )
    )


if __name__ == "__main__":
    main()
