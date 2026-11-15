#!/usr/bin/env python3
"""Retain seven focused native checks for CommunityMech:000087 (2026-11-14).

Inputs: explicit M5 host/checkout, existing m5_completion_checks.py persisted
runner, canonical record/history. Outputs: unique lbnl-* remote and local ignored
receipts. Serves the authorized PR2102 completion review; no record/code edits.
"""

import argparse
import json
import shlex
import subprocess
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", required=True)
    parser.add_argument("--remote-repo", required=True)
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[2]
    evidence = ".temp/m5-completion-20261114"
    out = repo / evidence
    out.mkdir(parents=True, exist_ok=True)
    record = "kb/communities/LBNL_Switchgrass_Soil_SynCom16.yaml"
    checks = {
        "schema": ["validate", record],
        "strict": ["validate-strict", record, "--out", evidence + "/lbnl-strict.tsv"],
        "terms": ["validate-terms", record],
        "references": ["validate-references-explained", record],
        "gtdb": ["validate-gtdb", record],
        "domain": ["validate-gtdb-domain", record],
        "history": ["validate-history", "history/records/LBNL_Switchgrass_Soil_SynCom16"],
    }
    for label, native_args in checks.items():
        name = "lbnl-" + label
        command = [
            ".venv/bin/python",
            "scripts/adhoc/m5_completion_checks.py",
            "run",
            "--name",
            name,
            "--arguments",
            *native_args,
        ]
        remote = "cd " + shlex.quote(args.remote_repo) + " && " + shlex.join(command)
        result = subprocess.run(
            ["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=8", args.host, remote],
            capture_output=True,
            text=True,
        )
        (out / (name + ".launch.log")).write_text(result.stdout + result.stderr)
        for suffix in ["json", "log", "exit"]:
            source = args.remote_repo + "/" + evidence + "/" + name + "." + suffix
            receipt = subprocess.run(
                ["ssh", "-o", "BatchMode=yes", args.host, "cat " + shlex.quote(source)],
                capture_output=True,
            )
            if receipt.returncode == 0:
                (out / (name + "." + suffix)).write_bytes(receipt.stdout)
        print(json.dumps({"name": name, "launcher_exit": result.returncode}), flush=True)


if __name__ == "__main__":
    main()
