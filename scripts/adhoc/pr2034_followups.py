"""Inventory original PR 2034 findings and candidate existing issue matches."""

import argparse
import json
from pathlib import Path

import yaml


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory", type=Path, required=True)
    parser.add_argument("--issues", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    inventory = json.loads(args.inventory.read_text())
    issues = json.loads(args.issues.read_text())
    rows = []
    for record in inventory["records"]:
        review = yaml.safe_load(Path(record["review"]).read_text())
        needles = [record["target_id"], Path(record["target_path"]).stem]
        needles += [finding["issue_key"] for finding in review.get("findings", [])]
        candidates = []
        for issue in issues:
            text = issue["title"] + "\n" + (issue["body"] or "")
            matched = [needle for needle in needles if needle.casefold() in text.casefold()]
            if matched:
                candidates.append({**issue, "matched": matched})
        rows.append(
            {
                "target_id": record["target_id"],
                "target_path": record["target_path"],
                "review": record["review"],
                "stale": record["stale"],
                "findings": review.get("findings", []),
                "actions": review.get("action_plan", review.get("actions", [])),
                "issue_candidates": candidates,
            }
        )
    args.output.write_text(
        json.dumps({"issue_count": len(issues), "records": rows}, indent=2) + "\n"
    )
    for row in rows:
        print(row["target_id"], row["target_path"])
        for finding in row["findings"]:
            print(" ", finding["finding_id"], finding["severity"], finding.get("title", ""))
            print("   ", finding["description"])
        print(
            "  Candidate issues:",
            [(i["number"], i["state"], i["title"]) for i in row["issue_candidates"]],
        )


if __name__ == "__main__":
    main()
