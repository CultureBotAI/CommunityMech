"""Verify retained inputs of one immutable M5 review (2026-11-14).

Inputs: one saved native review and its ignored captured-source/check receipts.
Output: a new hash audit; refuses replacement. Serves completion evidence and
#2780 without fetching sources, rewriting reviews, or interpreting claims.
"""

import argparse
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("review", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    review_path = (ROOT / args.review).resolve()
    output = (ROOT / args.output).resolve()
    review_path.relative_to(ROOT / "reviews/structured")
    output.relative_to(ROOT)
    if output.exists():
        raise ValueError("refusing to replace a retained input audit")
    review = yaml.safe_load(review_path.read_text())
    rows = []
    for item in review["source"]["inputs"]:
        if not item["path"].startswith(".temp/m5-completion-20261114/"):
            continue
        source = (ROOT / item["path"]).resolve()
        source.relative_to(ROOT / ".temp/m5-completion-20261114")
        data = source.read_bytes() if source.is_file() else None
        actual = hashlib.sha256(data).hexdigest() if data is not None else None
        rows.append(
            {
                "path": item["path"],
                "expected_sha256": item["sha256"],
                "actual_sha256": actual,
                "bytes": len(data) if data is not None else None,
                "matched": actual == item["sha256"],
            }
        )
    if not rows:
        raise ValueError("review has no retained working inputs to verify")
    result = {
        "review_id": review["review_id"],
        "review_sha256": hashlib.sha256(review_path.read_bytes()).hexdigest(),
        "scope": "Only captured .temp inputs; not a fresh scientific review or a current canonical-record check.",
        "all_matched": all(row["matched"] for row in rows),
        "inputs": rows,
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("x") as handle:
        json.dump(result, handle, indent=2)
        handle.write("\n")
    print(
        json.dumps(
            {
                "review_id": review["review_id"],
                "inputs": len(rows),
                "all_matched": result["all_matched"],
            }
        )
    )
    return int(not result["all_matched"])


if __name__ == "__main__":
    raise SystemExit(main())
