"""Compare PR 2034's frozen review inputs with a fetched main revision."""

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

import yaml


def git(*args):
    return subprocess.check_output(["git", *args])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", default="origin/main")
    parser.add_argument("--head", default="4d8f5120972fc99b3cb41c279d497eddde71eb8b")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    base = git("rev-parse", args.base).decode().strip()
    head = git("rev-parse", args.head).decode().strip()
    files = git("diff", "--name-only", f"{head}^", head).decode().splitlines()
    rows = []
    for filename in files:
        if not filename.startswith("reviews/structured/") or not filename.endswith("/review.yaml"):
            continue
        review = yaml.safe_load(git("show", f"{head}:{filename}"))
        assert len(review["targets"]) == 1, filename
        target = review["targets"][0]
        inputs = {item["path"]: item for item in review["source"]["inputs"]}
        frozen = inputs[target["path"]]["sha256"]
        current = hashlib.sha256(git("show", f"{base}:{target['path']}")).hexdigest()
        changed_inputs = []
        for path, item in inputs.items():
            result = subprocess.run(
                ["git", "show", f"{base}:{path}"], capture_output=True, check=False
            )
            digest = hashlib.sha256(result.stdout).hexdigest() if result.returncode == 0 else None
            if digest != item["sha256"]:
                changed_inputs.append({"path": path, "frozen": item["sha256"], "current": digest})
        rows.append(
            {
                "review": filename,
                "review_id": review["review_id"],
                "target_id": target["target_id"],
                "target_path": target["path"],
                "frozen_sha256": frozen,
                "current_sha256": current,
                "stale": frozen != current,
                "changed_inputs": changed_inputs,
                "finding_count": len(review.get("findings", [])),
            }
        )
    assert len(rows) == 10, len(rows)
    result = {"base": base, "original_pr_head": head, "records": rows}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    for row in rows:
        print(
            f"{row['target_id']}\t{'STALE' if row['stale'] else 'unchanged'}\t{row['target_path']}"
        )


if __name__ == "__main__":
    main()
