"""Prepare/canary/copy a verified private Phase2 checkpoint to M5, 2026-11-15.

Inputs: an exact local snapshot, explicit fresh attempt, reviewed standalone
verifier. Outputs: exclusive local staging/plan/logs/receipt and one fresh M5
.temp namespace. No delete, overwrite, publication or source-checkout edits.
Prepare is local only; transfer is an explicit separate invocation after review.
"""

import argparse
import json
import re
import shlex
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from checkpoint_phase2_review_inputs_20261115 import (
    REMOTE_CHECKOUT,
    REMOTE_HOST,
    ROOT,
    digest,
    private_output,
    verify,
)

VERIFIER = ROOT / "scripts/adhoc/verify_phase2_review_checkpoint_20261115.py"
REMOTE_PARENT = REMOTE_CHECKOUT + "/.temp/phase2-review-input-checkpoints-20261115"


def prepare(snapshot, output, attempt):
    output = private_output(output)
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,79}", attempt):
        raise ValueError("simple explicit attempt label required")
    checked = verify(snapshot)
    manifest = json.loads((snapshot / "manifest.json").read_bytes())
    output.mkdir(parents=True)
    payload = output / "payload"
    payload.mkdir()
    shutil.copytree(snapshot, payload / "snapshot")
    verifier_raw = VERIFIER.read_bytes()
    with (payload / "verify_checkpoint.py").open("xb") as stream:
        stream.write(verifier_raw)
    copied = verify(payload / "snapshot")
    if any(
        copied[key] != checked[key]
        for key in ("manifest_sha256", "files_verified", "bytes_verified")
    ):
        raise ValueError("local transfer staging differs")
    files = ["snapshot/manifest.json", "verify_checkpoint.py"] + [
        "snapshot/" + row["path"] for row in manifest["files"]
    ]
    canary = next(row for row in manifest["files"] if row["role"] == "review_yaml" and row["bytes"])
    canary_path = "snapshot/" + canary["path"]
    for filename, names in (
        ("canary.files", [canary_path]),
        ("remaining.files", [name for name in files if name != canary_path]),
    ):
        with (output / filename).open("xb") as stream:
            stream.write("\0".join(names).encode() + b"\0")
    result = {
        "created_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "attempt": attempt,
        "remote_host": REMOTE_HOST,
        "remote_destination": REMOTE_PARENT + "/" + attempt,
        "snapshot": checked,
        "standalone_verifier_sha256": digest(verifier_raw),
        "transfer_helper_sha256": digest(Path(__file__).read_bytes()),
        "canary": {"path": canary_path, "sha256": canary["sha256"], "bytes": canary["bytes"]},
        "filelist_sha256": {
            name: digest((output / name).read_bytes())
            for name in ("canary.files", "remaining.files")
        },
        "network_actions_performed": False,
    }
    with (output / "plan.json").open("x") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    return result


def transfer(plan_path, run=subprocess.run):
    directory = plan_path.resolve().parent
    if not directory.is_relative_to(ROOT / ".temp"):
        raise ValueError("transfer plan must remain in this checkout's private .temp")
    plan_raw = plan_path.read_bytes()
    plan = json.loads(plan_raw)
    marker = directory / "transfer-started.json"
    if marker.exists() or marker.is_symlink() or (directory / "transfer-receipt.json").exists():
        raise ValueError("this transfer was already attempted; preserve its outputs")
    if (
        plan["remote_host"] != REMOTE_HOST
        or not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,79}", plan["attempt"])
        or plan["remote_destination"] != REMOTE_PARENT + "/" + plan["attempt"]
        or plan["transfer_helper_sha256"] != digest(Path(__file__).read_bytes())
    ):
        raise ValueError("reviewed transfer destination/helper differs")
    payload = directory / "payload"
    checked = verify(payload / "snapshot")
    manifest = json.loads((payload / "snapshot/manifest.json").read_bytes())
    for key in ("manifest_sha256", "files_verified", "bytes_verified"):
        if checked[key] != plan["snapshot"][key]:
            raise ValueError("reviewed snapshot differs")
    if (
        digest((payload / "verify_checkpoint.py").read_bytes())
        != plan["standalone_verifier_sha256"]
    ):
        raise ValueError("standalone verifier differs")
    for name, expected in plan["filelist_sha256"].items():
        if (
            name not in {"canary.files", "remaining.files"}
            or digest((directory / name).read_bytes()) != expected
        ):
            raise ValueError("reviewed file list differs")
    canary_matches = [
        row
        for row in manifest["files"]
        if "snapshot/" + row["path"] == plan["canary"]["path"]
        and row["role"] == "review_yaml"
        and row["bytes"] > 0
        and row["sha256"] == plan["canary"]["sha256"]
        and row["bytes"] == plan["canary"]["bytes"]
    ]
    if len(canary_matches) != 1:
        raise ValueError("canary is not one complete reviewed YAML artifact")
    expected_files = ["snapshot/manifest.json", "verify_checkpoint.py"] + [
        "snapshot/" + row["path"] for row in manifest["files"]
    ]
    expected_lists = {
        "canary.files": [plan["canary"]["path"]],
        "remaining.files": [name for name in expected_files if name != plan["canary"]["path"]],
    }
    for name, expected in expected_lists.items():
        if (directory / name).read_bytes() != "\0".join(expected).encode() + b"\0":
            raise ValueError("file list contains undeclared or missing payload members")
    started = datetime.now(timezone.utc).isoformat(timespec="seconds")
    with marker.open("x") as stream:
        json.dump({"started_at": started, "plan_sha256": digest(plan_raw)}, stream)
        stream.write("\n")
    steps = []

    def command(name, argv):
        completed = run(argv, capture_output=True, check=False)
        for suffix, raw in (("stdout", completed.stdout), ("stderr", completed.stderr)):
            with (directory / f"{name}.{suffix}.log").open("xb") as stream:
                stream.write(raw)
        steps.append({"name": name, "argv": argv, "exit_code": completed.returncode})
        if completed.returncode:
            raise RuntimeError("native transfer command failed: " + name)
        return completed.stdout.decode()

    def ssh(name, text):
        return command(name, ["ssh", REMOTE_HOST, text])

    def rsync(name, filelist):
        return command(
            name,
            [
                "rsync",
                "-a",
                "--ignore-existing",
                "--from0",
                "--files-from=" + str(directory / filelist),
                "--",
                str(payload) + "/",
                REMOTE_HOST + ":" + plan["remote_destination"] + "/",
            ],
        )

    receipt = {"started_at": started, "plan_sha256": digest(plan_raw), "steps": steps}
    try:
        q = shlex.quote
        destination = plan["remote_destination"]
        actual_root = ssh("remote-checkout", "cd " + q(REMOTE_CHECKOUT) + " && pwd -P").strip()
        if actual_root != REMOTE_CHECKOUT:
            raise ValueError("M5 checkout resolves to a different location")
        preflight = " && ".join(
            [
                "test -d " + q(REMOTE_CHECKOUT),
                "test ! -L " + q(REMOTE_CHECKOUT + "/.temp"),
                "test ! -L " + q(REMOTE_PARENT),
                "test ! -e " + q(destination),
                "test ! -L " + q(destination),
                "mkdir -p " + q(REMOTE_PARENT),
                "mkdir " + q(destination),
            ]
        )
        ssh("remote-fresh-directory", preflight)
        rsync("canary", "canary.files")
        remote_canary = destination + "/" + plan["canary"]["path"]
        canary_sha = ssh("canary-sha", shlex.join(["shasum", "-a", "256", remote_canary])).split()[
            0
        ]
        canary_bytes = int(
            ssh("canary-size", shlex.join(["stat", "-f", "%z", remote_canary])).strip()
        )
        if canary_sha != plan["canary"]["sha256"] or canary_bytes != plan["canary"]["bytes"]:
            raise ValueError("canary did not persist exact reviewed bytes")
        receipt["canary_verified"] = {"sha256": canary_sha, "bytes": canary_bytes}
        rsync("remaining", "remaining.files")
        verifier_sha = ssh(
            "verifier-sha",
            shlex.join(["shasum", "-a", "256", destination + "/verify_checkpoint.py"]),
        ).split()[0]
        if verifier_sha != plan["standalone_verifier_sha256"]:
            raise ValueError("remote verifier bytes differ")
        remote_result = json.loads(
            ssh(
                "remote-verification",
                shlex.join(
                    [
                        "/usr/bin/python3",
                        destination + "/verify_checkpoint.py",
                        destination + "/snapshot",
                        "--expected-manifest-sha256",
                        checked["manifest_sha256"],
                    ]
                ),
            )
        )
        if remote_result["status"] != "verified" or any(
            remote_result[key] != checked[key]
            for key in ("manifest_sha256", "files_verified", "bytes_verified")
        ):
            raise ValueError("remote complete snapshot verification differs")
        receipt.update(
            status="verified", remote_verification=remote_result, remote_destination=destination
        )
    except Exception as error:
        receipt.update(status="failed", error=str(error))
        raise
    finally:
        receipt["finished_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
        with (directory / "transfer-receipt.json").open("x") as stream:
            json.dump(receipt, stream, indent=2)
            stream.write("\n")
    return receipt


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("prepare")
    p.add_argument("--snapshot", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--attempt", required=True)
    t = sub.add_parser("transfer")
    t.add_argument("--plan", type=Path, required=True)
    args = parser.parse_args()
    if args.command == "prepare":
        result = prepare(args.snapshot, args.output, args.attempt)
    else:
        result = transfer(args.plan)
    print(json.dumps(result))


if __name__ == "__main__":
    main()
