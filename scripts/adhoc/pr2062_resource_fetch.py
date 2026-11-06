"""Freeze explicitly selected public archive metadata for the PR 2062 review.

The JSON plan supplies labels and HTTPS URLs; it is data, never executable code.
Responses, headers and retrieval receipts go only to a new PR scratch directory.
This helper does not curate records, download raw sequencing reads, or contact
people. Reviewers must inspect response contents and qualify unavailable results.
"""

import argparse
import datetime
import hashlib
import json
import re
import subprocess
import time
from pathlib import Path
from urllib.parse import urlsplit

HOSTS = {"www.ncbi.nlm.nih.gov", "eutils.ncbi.nlm.nih.gov", "api.ncbi.nlm.nih.gov", "www.ebi.ac.uk"}
SCRATCH = Path(".temp/pr2062/root-resources")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not args.output.resolve().is_relative_to(SCRATCH.resolve()):
        raise ValueError("Output must stay within this PR's resource scratch directory")
    if args.output.exists():
        raise ValueError(f"Refusing to overwrite frozen source bytes: {args.output}")
    plan = json.loads(args.plan.read_text())
    labels = [row["label"] for row in plan]
    if len(labels) != len(set(labels)):
        raise ValueError("Duplicate request labels")
    for row in plan:
        url = urlsplit(row["url"])
        if url.scheme != "https" or url.hostname not in HOSTS or url.username or url.password:
            raise ValueError("Only explicitly allowed public HTTPS archive endpoints are accepted")
        if not re.fullmatch(r"[A-Za-z0-9_.-]+", row["label"]):
            raise ValueError("Unsafe output label")
    args.output.mkdir(parents=True)
    receipts = []
    for row in plan:
        body = args.output / (row["label"] + ".body")
        headers = args.output / (row["label"] + ".headers")
        command = [
            "curl",
            "--location",
            "--silent",
            "--show-error",
            "--connect-timeout",
            "15",
            "--max-time",
            "60",
            "--retry",
            "2",
            "--retry-delay",
            "1",
            "--dump-header",
            str(headers),
            "--output",
            str(body),
            "--write-out",
            "%{http_code}",
            row["url"],
        ]
        started = datetime.datetime.now(datetime.timezone.utc).isoformat()
        result = subprocess.run(command, capture_output=True, text=True)
        stderr = args.output / (row["label"] + ".stderr")
        stderr.write_text(result.stderr)
        receipt = {
            **row,
            "started_at": started,
            "finished_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "command": command,
            "exit_code": result.returncode,
            "http_status": result.stdout,
            "body_path": str(body),
            "body_sha256": hashlib.sha256(body.read_bytes()).hexdigest() if body.exists() else None,
            "headers_path": str(headers),
            "stderr_path": str(stderr),
        }
        receipts.append(receipt)
        (args.output / "retrievals.json").write_text(json.dumps(receipts, indent=2) + "\n")
        print(
            json.dumps({k: receipt[k] for k in ["label", "exit_code", "http_status"]}), flush=True
        )
        time.sleep(0.4)


if __name__ == "__main__":
    main()
