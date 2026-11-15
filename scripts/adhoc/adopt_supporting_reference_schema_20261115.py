"""Governed single-consumer adoption for Claw #1219 / CommunityMech #476.

2026-11-15. Inputs: published immutable Claw checkout and this exact clean
CommunityMech worktree. Outputs: native plan/application plus exclusive private
before/after evidence. Defaults to planning; apply uses RepositorySettings,
LockManager and the maintained transactional synchronizer. No other consumer,
record, cache, live configuration or merge is changed by this helper.
"""

import argparse
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PIN = "85b4d693002387b855ece75282fad7a324b761cc"
EXPECTED = {
    "prompts/backlog-loop-goal.md",
    "src/communitymech/schema/mech_shared.yaml",
    "scripts/auto_merge_ready_prs.py",
    "docs/record-reviews.md",
    "scripts/.vendored_canon_ref",
}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args], text=True).strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--claw-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    source = args.claw_root.resolve()
    output = args.output.resolve()
    if not output.is_relative_to(ROOT / ".temp") or output.exists():
        parser.error("output must be a new exclusive repository .temp directory")
    if git(source, "rev-parse", "HEAD") != PIN or git(source, "status", "--porcelain"):
        parser.error("Claw source must be clean at the reviewed published revision")
    if git(ROOT, "status", "--porcelain"):
        parser.error("target must be clean before planning or applying")
    sys.path[:0] = [str(source), str(source / "src")]
    from kg_microbe_governance import plan_sync, sync_repository
    from plugins.lock_manager import LockManager
    from plugins.repository_settings import RepositorySettings

    settings = RepositorySettings.from_environment(environ={"COMMUNITYMECH_ROOT": str(ROOT)})
    target = settings.get_target("communitymech")
    if Path(target.open().working_tree_dir).resolve() != ROOT:
        parser.error("configured repository differs from this worktree")
    changes = plan_sync("communitymech", ROOT, PIN)
    if {change.path for change in changes} != EXPECTED:
        parser.error("native plan differs from the five reviewed adoption paths")
    before = {name: (ROOT / name).read_bytes() for name in sorted(EXPECTED)}
    receipt = {
        "started_at": datetime.now(timezone.utc).isoformat(),
        "claw_revision": PIN,
        "communitymech_revision": git(ROOT, "rev-parse", "HEAD"),
        "helper_sha256": sha(Path(__file__).read_bytes()),
        "apply": args.apply,
        "plan": [
            {"artifact": change.artifact_id, "path": change.path, "reason": change.reason}
            for change in changes
        ],
        "before_sha256": {name: sha(raw) for name, raw in before.items()},
    }
    output.mkdir(parents=True)
    for name, raw in before.items():
        backup = output / "before" / name
        backup.parent.mkdir(parents=True, exist_ok=True)
        backup.write_bytes(raw)
    (output / "started.json").write_text(json.dumps(receipt, indent=2) + "\n")
    if args.apply:
        with LockManager().lock("communitymech", "adopt-reviewed-supporting-reference-schema"):
            settings.get_target("communitymech")
            if any((ROOT / name).read_bytes() != raw for name, raw in before.items()):
                raise ValueError("reviewed target bytes changed before synchronization")
            applied = sync_repository("communitymech", ROOT, PIN, apply=True)
            if {change.path for change in applied} != EXPECTED:
                raise ValueError("applied native plan differs from the reviewed plan")
        if plan_sync("communitymech", ROOT, PIN):
            raise ValueError("native post-write governance check found drift")
    elif any((ROOT / name).read_bytes() != raw for name, raw in before.items()):
        raise ValueError("planning changed target bytes")
    receipt["after_sha256"] = {name: sha((ROOT / name).read_bytes()) for name in sorted(EXPECTED)}
    receipt["finished_at"] = datetime.now(timezone.utc).isoformat()
    receipt["status"] = "APPLIED AND VERIFIED" if args.apply else "PLAN VERIFIED"
    (output / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
