"""Prepare and publish individually reviewed issues for an explicitly named batch PR."""

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

import yaml

REPOSITORY = "CultureBotAI/CommunityMech"


def prepare_staleness(args):
    inventory = json.loads(args.inventory.read_text())
    args.output.mkdir(parents=True, exist_ok=True)
    plan = []
    for record in inventory["records"]:
        if not record["stale"]:
            continue
        identifier = record["target_id"].split(":")[-1]
        key = f"pr{args.pr}-{identifier}-stale-review"
        title = f"PR #{args.pr}: refresh stale {record['target_id']} review against current main"
        body = (
            f"In-scope review-bundle finding from the PR #{args.pr} publication audit.\n\n"
            f"Stable finding key: `{key}`.\n\n"
            f"Target: `{record['target_path']}`.\n\n"
            f"Original review: `{record['review_id']}`. Its frozen target SHA-256 is "
            f"`{record['frozen_sha256']}`; the record at fetched main "
            f"`{inventory['base']}` is `{record['current_sha256']}`. "
            "The old observation is historical and does not assess the current record.\n\n"
            "Acceptance: inspect the changed record and actual primary sources, reassess all "
            "prior findings, run current native validators, and add a linked immutable successor "
            "review with current frozen inputs. Preserve the original YAML/Markdown pair. "
            "Run structured-review validation and contract tests, then an independent read-only "
            "re-review on the committed head. No canonical record edit belongs in this PR.\n"
        )
        path = args.output / f"{identifier}-staleness.md"
        path.write_text(body)
        plan.append(
            {
                "key": key,
                "finding_id": f"stale-{identifier}",
                "title": title,
                "body_file": str(path),
            }
        )
    path = args.output / "staleness-plan.json"
    path.write_text(json.dumps(plan, indent=2) + "\n")
    print(path)


def prepare(args):
    review = yaml.safe_load(args.review.read_text())
    target = review["targets"][0]
    assert len(review["targets"]) == 1
    evidence = {entry["evidence_id"]: entry for entry in review.get("evidence", [])}
    rows = []
    args.output.mkdir(parents=True, exist_ok=True)
    for finding in review["findings"]:
        if finding["status"] not in {"open", "deferred"}:
            continue
        key = finding["issue_key"]
        actions = [
            a for a in review.get("actions", []) if finding["finding_id"] in a["finding_ids"]
        ]
        title = f"{target['target_id']}: {finding['title']}"
        body = [
            f"Record/source-curation follow-up from PR #{args.pr}. This issue stays outside its review-bundle scope.",
            f"Stable finding key: `{key}`.",
            f"Target: `{target['target_id']}` — `{target['path']}`.",
            f"Review: `{review['review_id']}` / `{finding['finding_id']}`.",
            f"[Review bundle](https://github.com/{REPOSITORY}/blob/{args.revision}/{args.review.as_posix()}).",
            f"Severity: {finding['severity']} ({finding.get('native_severity', 'not specified')}).",
            finding["description"],
            "Affected fields:\n\n"
            + "\n".join(f"- `{field}`" for field in finding.get("field_paths", [])),
        ]
        refs = []
        for evidence_id in finding.get("evidence_ids", []):
            entry = evidence[evidence_id]
            locator = re.sub(
                r"; (?:exact response )?body retained at /private/tmp/.*$",
                "",
                entry.get("locator", ""),
            )
            refs.append(f"- `{evidence_id}`: {entry.get('reference', '')}; {locator}")
        body.append(
            "Inspected evidence (details and limitations remain in the linked bundle):\n\n"
            + "\n".join(refs)
        )
        for action in actions:
            body.append(action["description"])
            body.append(
                "Acceptance checks:\n\n"
                + "\n".join(f"- {check}" for check in action["acceptance_checks"])
            )
        body.append(
            "Issue search: the publication pass inspected the repository issue inventory and record/finding-specific candidates before filing. Record or source edits require a separate curation change."
        )
        content = "\n\n".join(body) + "\n"
        assert "@" not in content + title, "User/team mentions are prohibited"
        path = args.output / f"{target['target_id'].split(':')[-1]}-{finding['finding_id']}.md"
        path.write_text(content)
        rows.append(
            {
                "key": key,
                "finding_id": finding["finding_id"],
                "title": title,
                "body_file": str(path),
            }
        )
    plan = args.output / f"{target['target_id'].split(':')[-1]}-plan.json"
    plan.write_text(json.dumps(rows, indent=2) + "\n")
    print(plan)


def publish(args):
    rows = json.loads(args.plan.read_text())
    journal = json.loads(args.journal.read_text()) if args.journal.exists() else []
    by_key = {row["key"]: row for row in journal}
    for row in rows:
        if args.only and row["finding_id"] not in args.only:
            continue
        if row["key"] in by_key:
            print("Already recorded:", by_key[row["key"]]["url"], flush=True)
            continue
        search = subprocess.check_output(
            [
                "gh",
                "issue",
                "list",
                "--repo",
                REPOSITORY,
                "--state",
                "all",
                "--limit",
                "100",
                "--search",
                f'"{row["key"]}" in:body',
                "--json",
                "number,url,body",
            ],
            text=True,
        )
        matches = [issue for issue in json.loads(search) if row["key"] in (issue["body"] or "")]
        if matches:
            assert len(matches) == 1, "Multiple exact finding keys require manual reconciliation"
            url = matches[0]["url"]
            created = False
        else:
            content = Path(row["body_file"]).read_text()
            assert f"PR #{args.pr}" in content, "Issue must identify the explicitly selected PR"
            assert "@" not in content + row["title"]
            url = subprocess.check_output(
                [
                    "gh",
                    "issue",
                    "create",
                    "--repo",
                    REPOSITORY,
                    "--title",
                    row["title"],
                    "--body-file",
                    row["body_file"],
                ],
                text=True,
            ).strip()
            created = True
        entry = {**row, "url": url, "created": created}
        journal.append(entry)
        args.journal.write_text(json.dumps(journal, indent=2) + "\n")
        by_key[row["key"]] = entry
        print(url, flush=True)


def reuse(args):
    """Record an explicitly reviewed mapping to an existing open issue."""
    rows = json.loads(args.plan.read_text())
    matches = [row for row in rows if row["finding_id"] == args.finding]
    assert len(matches) == 1, "Select exactly one prepared finding"
    assert len(args.reason.strip()) >= 20 and "@" not in args.reason
    row = matches[0]
    issue = json.loads(
        subprocess.check_output(
            [
                "gh",
                "issue",
                "view",
                str(args.issue),
                "--repo",
                REPOSITORY,
                "--json",
                "number,title,state,url,body",
            ],
            text=True,
        )
    )
    assert issue["state"] == "OPEN", "Reuse requires a currently open issue"
    journal = json.loads(args.journal.read_text()) if args.journal.exists() else []
    previous = [item for item in journal if item["key"] == row["key"]]
    if previous:
        assert len(previous) == 1 and previous[0]["url"] == issue["url"]
        print("Already recorded:", issue["url"])
        return
    journal.append(
        {
            **row,
            "url": issue["url"],
            "created": False,
            "reuse_reason": args.reason,
            "existing_title": issue["title"],
            "existing_body_sha256": hashlib.sha256(issue["body"].encode()).hexdigest(),
        }
    )
    args.journal.write_text(json.dumps(journal, indent=2) + "\n")
    print(issue["url"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pr", type=int, required=True, help="Explicitly authorized PR number")
    sub = parser.add_subparsers(dest="command", required=True)
    prep = sub.add_parser("prepare")
    prep.add_argument("--review", type=Path, nargs="+", required=True)
    prep.add_argument("--revision", required=True, help="Exact inspected review commit")
    prep.add_argument("--output", type=Path, required=True)
    stale = sub.add_parser("prepare-staleness")
    stale.add_argument("--inventory", type=Path, required=True)
    stale.add_argument("--output", type=Path, required=True)
    pub = sub.add_parser("publish")
    pub.add_argument("--plan", type=Path, nargs="+", required=True)
    pub.add_argument("--journal", type=Path, required=True)
    pub.add_argument("--only", nargs="*")
    existing = sub.add_parser("reuse", help="Record a human-reviewed existing-issue match")
    existing.add_argument("--plan", type=Path, required=True)
    existing.add_argument("--finding", required=True)
    existing.add_argument("--issue", type=int, required=True)
    existing.add_argument("--reason", required=True)
    existing.add_argument("--journal", type=Path, required=True)
    args = parser.parse_args()
    if args.command == "prepare":
        reviews = args.review
        for args.review in reviews:
            prepare(args)
    elif args.command == "prepare-staleness":
        prepare_staleness(args)
    elif args.command == "reuse":
        reuse(args)
    else:
        plans = args.plan
        for args.plan in plans:
            publish(args)


if __name__ == "__main__":
    main()
