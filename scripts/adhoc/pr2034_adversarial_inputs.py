"""Read-only provenance checks and bounded review views for the PR 2034 audit."""

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
    parser.add_argument("--target", help="Print the scientific sections for this target ID suffix")
    parser.add_argument("--review", type=Path, help="Read a specific review, including a successor")
    parser.add_argument("--audit-only", action="store_true")
    parser.add_argument("--compare-review", type=Path)
    parser.add_argument("--science-only", action="store_true")
    parser.add_argument(
        "--section",
        choices=["assessments", "findings", "evidence", "actions", "limitations", "checks"],
    )
    parser.add_argument("--output", type=Path)
    parser.add_argument("--source", type=Path)
    parser.add_argument("--needle")
    parser.add_argument("--radius", type=int, default=1600)
    parser.add_argument("--html", action="store_true")
    args = parser.parse_args()
    if args.compare_review:
        before = yaml.safe_load(args.compare_review.read_text())
        after = yaml.safe_load(args.review.read_text())
        differences = {}
        for field in ("checks", "targets", "completion", "verdict", "scientific_review"):
            differences[field] = before[field] == after[field]
        old_assessments = {item["assessment_id"]: item for item in before["assessments"]}
        new_assessments = {item["assessment_id"]: item for item in after["assessments"]}
        differences["changed_prior_assessments"] = [
            key for key, value in old_assessments.items() if new_assessments.get(key) != value
        ]
        differences["new_assessment_ids"] = sorted(new_assessments.keys() - old_assessments.keys())
        old_findings = {
            item["finding_id"]: {
                key: value for key, value in item.items() if key != "previous_occurrences"
            }
            for item in before["findings"]
        }
        new_findings = {
            item["finding_id"]: {
                key: value for key, value in item.items() if key != "previous_occurrences"
            }
            for item in after["findings"]
        }
        differences["findings_equal_except_lineage"] = old_findings == new_findings
        differences["actions_equal"] = before["actions"] == after["actions"]
        print(json.dumps(differences, indent=2))
        return
    if args.source:
        text = args.source.read_text()
        if args.html:
            from bs4 import BeautifulSoup

            text = BeautifulSoup(text, "html.parser").get_text(" ", strip=True)
        start = text.index(args.needle)
        low = max(0, start - args.radius)
        high = min(len(text), start + len(args.needle) + args.radius)
        print(f"SOURCE {args.source}; characters {low}:{high} of {len(text)}")
        print(text[low:high])
        return
    old_head = "4d8f5120972fc99b3cb41c279d497eddde71eb8b"
    paths = git("diff", "--name-only", old_head + "^", old_head).decode().splitlines()
    if args.review:
        paths = [str(args.review)]
    rows = []
    for path in paths:
        if not args.review and not path.endswith("/review.yaml"):
            continue
        raw = Path(path).read_bytes()
        review = yaml.safe_load(raw)
        target = review["targets"][0]
        if not args.audit_only and (
            args.review or (args.target and target["target_id"].endswith(args.target))
        ):
            view = {
                key: value for key, value in review.items() if key not in ("checks", "evidence")
            }
            view["checks"] = [
                {key: value for key, value in check.items() if key != "summary"}
                for check in review["checks"]
            ]
            view["evidence"] = [item for item in review["evidence"] if item["kind"] != "validation"]
            if args.science_only:
                view.pop("checks")
                view["source"] = {
                    "git_revision": review["source"]["git_revision"],
                    "state": review["source"]["state"],
                    "source_paths": [
                        item["path"]
                        for item in review["source"]["inputs"]
                        if item["path"].startswith("references_cache/")
                    ],
                }
            print(
                yaml.safe_dump(
                    view[args.section] if args.section else view, sort_keys=False, width=100
                )
            )
        mismatches = []
        current_mismatches = []
        for item in review["source"]["inputs"]:
            revision = review["source"]["git_revision"]
            result = subprocess.run(
                ["git", "show", f"{revision}:{item['path']}"], capture_output=True, check=False
            )
            digest = hashlib.sha256(result.stdout).hexdigest() if result.returncode == 0 else None
            if digest != item["sha256"]:
                mismatches.append({"path": item["path"], "frozen": item["sha256"], "git": digest})
            current_path = Path(item["path"])
            current_digest = (
                hashlib.sha256(current_path.read_bytes()).hexdigest()
                if current_path.is_file()
                else None
            )
            if current_digest != item["sha256"]:
                current_mismatches.append(
                    {"path": item["path"], "frozen": item["sha256"], "current": current_digest}
                )
        old_blob = subprocess.run(
            ["git", "show", f"{old_head}:{path}"], capture_output=True, check=False
        )
        rows.append(
            {
                "path": path,
                "review_id": review["review_id"],
                "target_id": target["target_id"],
                "state": review["source"]["state"],
                "input_count": len(review["source"]["inputs"]),
                "historical_tree_mismatches": mismatches,
                "current_file_mismatches": current_mismatches,
                "original_bundle_unchanged": (
                    raw == old_blob.stdout if old_blob.returncode == 0 else None
                ),
                "required_unavailable": [
                    item["check_id"]
                    for item in review["checks"]
                    if item.get("required") and item["status"] in ("unavailable", "skipped")
                ],
            }
        )
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(rows, indent=2) + "\n")
        if args.audit_only:
            print(
                json.dumps(
                    [
                        {
                            "review_id": row["review_id"],
                            "input_count": row["input_count"],
                            "historical_mismatch_count": len(row["historical_tree_mismatches"]),
                            "current_file_mismatches": row["current_file_mismatches"],
                            "original_bundle_unchanged": row["original_bundle_unchanged"],
                            "required_unavailable": row["required_unavailable"],
                        }
                        for row in rows
                    ],
                    indent=2,
                )
            )
        else:
            print(json.dumps(rows, indent=2))


if __name__ == "__main__":
    main()
