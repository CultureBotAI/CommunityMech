"""Finalize the reviewed Claw #1283 schema pin; CommunityMech #1996, 2026-11-15.

Inputs: reviewed immutable Claw checkout and this exact clean
CommunityMech worktree. Outputs: native plan/application plus exclusive private
before/after evidence. Defaults to planning; apply uses RepositorySettings,
LockManager and the maintained transactional synchronizer. No other consumer,
record, cache, live configuration or merge is changed by this helper.
The initial three-file adoption used this helper as committed at 09254e5d;
its schema-apply-001 receipt remains immutable. This follow-up advances only
the governance pin after Claw's native template baseline correction.
"""

import argparse
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PIN = "846c4635c305ff1d837fcb4aa7e261a01c4258e3"
EXPECTED_BEFORE = {
    "scripts/.vendored_canon_ref": "fd0d27c3ef06c3880e429242131ee858335988d0229393800a3a12288445e1bf",
}
EXPECTED = set(EXPECTED_BEFORE)
EXPECTED_ROOT = Path("/Users/marcin/agent-work/CommunityMech/supplement-adoption-1996-20261115")
EXPECTED_BRANCH = "fix/supplement-adoption-1996-20261115"


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
    if ROOT != EXPECTED_ROOT or git(ROOT, "branch", "--show-current") != EXPECTED_BRANCH:
        parser.error("this preparation is restricted to its isolated feature worktree")
    source = args.claw_root.resolve()
    output = args.output.resolve()
    if not output.is_relative_to(ROOT / ".temp") or output.exists():
        parser.error("output must be a new exclusive repository .temp directory")
    if git(source, "rev-parse", "HEAD") != PIN or git(source, "status", "--porcelain"):
        parser.error("Claw source must be clean at the reviewed published revision")
    if (source / ".env").exists() or (source / ".env").is_symlink():
        parser.error("isolated source must not contain a dotenv file")
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
        parser.error("native plan differs from the reviewed pin-only follow-up")
    before = {name: (ROOT / name).read_bytes() for name in sorted(EXPECTED)}
    if {name: sha(raw) for name, raw in before.items()} != EXPECTED_BEFORE:
        parser.error("target bytes differ from the reviewed adoption predecessor")
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
    config = output / "repository-config.json"
    config.write_text(json.dumps({"repositories": {"communitymech": str(ROOT)}}) + "\n")
    config_command = [
        sys.executable,
        "-m",
        "cli.main",
        "config",
        "validate",
        "--config-file",
        str(config),
    ]
    cli_environment = os.environ.copy()
    cli_environment["PYTHONPATH"] = str(source) + os.pathsep + str(source / "src")
    with (output / "config-validation.log").open("xb") as handle:
        validation = subprocess.run(
            config_command, cwd=source, env=cli_environment, stdout=handle, stderr=subprocess.STDOUT
        )
    receipt["config_validation"] = {
        "command": config_command,
        "exit_code": validation.returncode,
        "config_sha256": sha(config.read_bytes()),
        "log_sha256": sha((output / "config-validation.log").read_bytes()),
    }
    if validation.returncode:
        raise ValueError("native configuration validation failed before synchronization")
    for name, raw in before.items():
        backup = output / "before" / name
        backup.parent.mkdir(parents=True, exist_ok=True)
        backup.write_bytes(raw)
    (output / "started.json").write_text(json.dumps(receipt, indent=2) + "\n")
    if args.apply:
        with LockManager().lock("communitymech", "prepare-supplement-schema-pin"):
            settings.get_target("communitymech")
            if (
                git(ROOT, "rev-parse", "HEAD") != receipt["communitymech_revision"]
                or git(ROOT, "status", "--porcelain")
                or git(source, "rev-parse", "HEAD") != PIN
                or git(source, "status", "--porcelain")
            ):
                raise ValueError("source or target checkout changed before lock acquisition")
            locked_plan = plan_sync("communitymech", ROOT, PIN)
            if {change.path for change in locked_plan} != EXPECTED:
                raise ValueError("native plan changed before lock acquisition")
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
