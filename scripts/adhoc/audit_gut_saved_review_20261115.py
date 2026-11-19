"""Verify the saved 000122 review and every retained input, 2026-11-15.

Input: one native saved review. Output: caller-exclusive JSON audit in repository.
Read-only hashes and native Markdown derivation; no source/validator/network runs.
Serves #1548/#2816 persistence, not a scientific support verdict. Reuses the
verified Phase2 000087 native saved-review canary audit without changing its checks.
"""

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
from record_review import load_document, render_markdown  # noqa: E402


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("review", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    path = args.review.resolve()
    output = args.output.resolve()
    if (
        not path.is_relative_to(ROOT / "reviews/structured")
        or not output.is_relative_to(ROOT)
        or output.exists()
    ):
        raise ValueError("invalid review or nonexclusive repository output")
    raw = path.read_bytes()
    review = load_document(raw)
    rows = []
    for item in review["source"]["inputs"]:
        source = (ROOT / item["path"]).resolve()
        if not source.is_relative_to(ROOT):
            raise ValueError("input escapes repository")
        content = source.read_bytes() if source.is_file() else None
        actual = sha(content) if content is not None else None
        rows.append(
            {
                "path": item["path"],
                "expected_sha256": item["sha256"],
                "actual_sha256": actual,
                "bytes": len(content) if content is not None else None,
                "matched": actual == item["sha256"],
            }
        )
    markdown = path.with_suffix(".md").read_text()
    result = {
        "audit_helper_sha256": sha(Path(__file__).read_bytes()),
        "checked_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "review_id": review["review_id"],
        "review_sha256": sha(raw),
        "review_bytes": len(raw),
        "markdown_sha256": sha(markdown.encode()),
        "markdown_bytes": len(markdown.encode()),
        "markdown_matches_native_render": markdown == render_markdown(review),
        "input_count": len(rows),
        "all_inputs_match": all(row["matched"] for row in rows),
        "scope": "Persistence and hash verification only; scientific and full-QC status remain those of the saved assessment.",
        "inputs": rows,
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("x") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print(json.dumps({key: value for key, value in result.items() if key != "inputs"}))
    return int(not result["all_inputs_match"] or not result["markdown_matches_native_render"])


if __name__ == "__main__":
    raise SystemExit(main())
