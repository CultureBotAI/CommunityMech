"""Run the native term CLI against existing local databases, #2848, 2026-11-15.

Inputs: exact revision/record/hash and existing OAK SQLite adapters. Outputs:
exclusive private config, native log/exit and receipt. No acquisition, canonical
writes or matcher changes; adapter identity is a recorded stat, not a byte hash.
"""

import argparse
import contextlib
import hashlib
import json
import socket
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch

import yaml

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/gtdb-code006-20261115"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stat(path):
    value = path.stat()
    return {key: getattr(value, key) for key in ("st_dev", "st_ino", "st_size", "st_mtime_ns")}


def deny_network(*args, **kwargs):
    raise RuntimeError("network acquisition forbidden in local term check")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", required=True)
    parser.add_argument("--expected-sha256", required=True)
    parser.add_argument("--expected-revision", required=True)
    parser.add_argument("--name", required=True)
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    target = ROOT / args.target
    output = STATE / args.name
    if (
        not args.name.startswith("isolate-")
        or not args.name.replace("-", "").isalnum()
        or output.exists()
        or target.is_symlink()
        or not target.resolve().is_relative_to(ROOT / "data/isolates")
    ):
        raise ValueError("safe exact isolate and exclusive private namespace required")
    revision = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    if revision != args.expected_revision or sha(target) != args.expected_sha256:
        raise ValueError("execution revision or actual record differs")
    adapters = {
        key: Path("/Users/marcin/.data/oaklib") / (name + ".db")
        for key, name in (("NCBITaxon", "ncbitaxon"), ("ENVO", "envo"), ("CHEBI", "chebi"))
    }
    if any(not path.is_file() or not path.stat().st_size for path in adapters.values()):
        raise ValueError("existing local ontology databases required")
    database_stats = {str(path): stat(path) for path in adapters.values()}
    inputs = {
        name: sha(ROOT / name)
        for name in (
            args.target,
            str(Path(__file__).relative_to(ROOT)),
            "uv.lock",
            "src/communitymech/schema/communitymech.yaml",
            "src/communitymech/schema/mech_shared.yaml",
            "src/communitymech/schema/history.yaml",
        )
    }
    argv = [
        "validate-data",
        args.target,
        "-s",
        "src/communitymech/schema/communitymech.yaml",
        "--labels",
        "--config",
        str((output / "oak.yaml").relative_to(ROOT)),
        "--cache-dir",
        str((output / "labels").relative_to(ROOT)),
    ]
    if args.plan:
        print(json.dumps({"planned": True, "argv": argv, "inputs": inputs}, indent=2))
        return 0
    output.mkdir()
    config = output / "oak.yaml"
    config.write_text(
        yaml.safe_dump(
            {"ontology_adapters": {key: "sqlite:" + str(path) for key, path in adapters.items()}}
        )
    )
    started = datetime.now(timezone.utc).isoformat()
    code = 0
    with (output / "native.log").open("w") as log:
        with contextlib.redirect_stdout(log), contextlib.redirect_stderr(log):
            with (
                patch.object(socket.socket, "connect", deny_network),
                patch.object(socket, "create_connection", deny_network),
            ):
                from linkml_term_validator import cli

                cli_sha = sha(Path(cli.__file__))
                try:
                    result = cli.app(args=argv, standalone_mode=False)
                    if isinstance(result, int):
                        code = result
                except SystemExit as exc:
                    code = int(exc.code or 0)
                except Exception as exc:
                    print("Native term exception type:", type(exc).__name__)
                    code = 2
    (output / "native.exit").write_text(str(code) + "\n")
    unchanged = inputs == {name: sha(ROOT / name) for name in inputs}
    unchanged = unchanged and database_stats == {
        str(path): stat(path) for path in adapters.values()
    }
    unchanged = (
        unchanged
        and revision
        == subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    )
    if not unchanged or not (output / "native.log").stat().st_size:
        raise ValueError("native check input changed or log was empty")
    receipt = {
        "target": args.target,
        "revision": revision,
        "record_sha256": args.expected_sha256,
        "native_argv": ["linkml-term-validator", *argv],
        "native_cli_sha256": cli_sha,
        "python": sys.version,
        "started_at": started,
        "finished_at": datetime.now(timezone.utc).isoformat(),
        "exit_code": code,
        "inputs": inputs,
        "database_stats_unchanged": database_stats,
        "database_hashes_measured": False,
        "config_sha256": sha(config),
        "log_sha256": sha(output / "native.log"),
        "inputs_unchanged": True,
        "network_policy": "socket connections refused; existing explicit SQLite paths only",
        "scope": "Native binding/label validation only; not scientific evidence validation.",
    }
    (output / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(
        json.dumps({"receipt": str((output / "receipt.json").relative_to(ROOT)), "exit_code": code})
    )
    return code


if __name__ == "__main__":
    raise SystemExit(main())
