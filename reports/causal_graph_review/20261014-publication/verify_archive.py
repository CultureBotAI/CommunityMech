"""Verify the batch129 archive in a separately fetched Git object database."""

import argparse
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import yaml

TAG = "refs/tags/review-provenance/20261014-batch129"
SNAPSHOT = "bbf94e02b72dfc254f55e4fd08ee9e524c12ce35"
SOURCE = "a7eaa4c339569107d60c25c409ba3599ce27a599"
REVIEW = "reviews/structured/20261014T200439Z-spring-parent-rank/review.yaml"


def verify(clone):
    def git(*args):
        return subprocess.check_output(["git", "-C", str(clone), *args])

    assert git("remote", "get-url", "origin").decode().strip() == (
        "https://github.com/CultureBotAI/CommunityMech.git"
    )
    common = Path(git("rev-parse", "--git-common-dir").decode().strip())
    if not common.is_absolute():
        common = clone / common
    assert common.resolve() == (clone / ".git").resolve()
    assert not (common / "objects/info/alternates").exists()
    assert git("cat-file", "-t", TAG).strip() == b"tag"
    assert git("rev-parse", f"{TAG}^{{commit}}").decode().strip() == SNAPSHOT
    subprocess.run(
        ["git", "-C", str(clone), "merge-base", "--is-ancestor", SOURCE, TAG], check=True
    )
    review_bytes = git("show", f"{SNAPSHOT}:{REVIEW}")
    review = yaml.safe_load(review_bytes)
    assert review["source"]["git_revision"] == SOURCE
    items = []
    for item in review["source"]["inputs"]:
        path = item["path"]
        actual = hashlib.sha256(git("show", f"{SNAPSHOT}:{path}")).hexdigest()
        assert actual == item["sha256"], path
        base = subprocess.run(
            ["git", "-C", str(clone), "show", f"{SOURCE}:{path}"], capture_output=True
        )
        base_hash = hashlib.sha256(base.stdout).hexdigest() if base.returncode == 0 else None
        items.append({"path": path, "sha256": actual, "matches_source_base": base_hash == actual})
    return {
        "verified_at": datetime.now(timezone.utc).isoformat(),
        "issue": "https://github.com/CultureBotAI/CommunityMech/issues/2003",
        "pull_request": "https://github.com/CultureBotAI/CommunityMech/pull/2002",
        "clone_path": str(clone),
        "clone_command": [
            "git",
            "clone",
            "--no-checkout",
            "--single-branch",
            "--branch",
            TAG.removeprefix("refs/tags/"),
            "https://github.com/CultureBotAI/CommunityMech.git",
            str(clone),
        ],
        "shared_objects": False,
        "tag": TAG,
        "tag_object": git("rev-parse", TAG).decode().strip(),
        "tag_type": "tag",
        "retained_snapshot": SNAPSHOT,
        "retained_source_base": SOURCE,
        "source_base_is_ancestor": True,
        "review": REVIEW,
        "review_sha256": hashlib.sha256(review_bytes).hexdigest(),
        "input_count": len(items),
        "inputs": items,
        "interpretation": (
            "The annotated remote archive retains the review source base and every attested input "
            "at the reviewed snapshot. Source-base matches are reported separately: a working-tree "
            "attestation is not a claim that all inputs were committed at its base revision."
        ),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("clone", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = verify(args.clone.resolve())
    with args.output.open("x") as handle:
        json.dump(result, handle, indent=2)
        handle.write("\n")
    print(json.dumps({key: value for key, value in result.items() if key != "inputs"}, indent=2))
