"""Report historical review source commits missing from the local object store."""

import argparse
import json
import re
import subprocess
from pathlib import Path

import yaml

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument(
    "--fetch", action="store_true", help="Fetch missing exact objects without updating branch refs"
)
args = parser.parse_args()

revisions = {}
for path in sorted(Path("reviews/structured").glob("*/review.yaml")):
    document = yaml.safe_load(path.read_text())
    revision = document["source"]["git_revision"]
    assert re.fullmatch(r"[0-9a-f]{40}", revision), "Expected a frozen full commit SHA"
    revisions.setdefault(revision, []).append(str(path))

missing = {}
for revision, paths in revisions.items():
    result = subprocess.run(
        ["git", "cat-file", "-e", f"{revision}^{{commit}}"], capture_output=True, check=False
    )
    if result.returncode:
        missing[revision] = paths

print(json.dumps({"source_commit_count": len(revisions), "missing": missing}, indent=2))
if args.fetch and missing:
    subprocess.run(["git", "fetch", "--no-write-fetch-head", "origin", *missing], check=True)
