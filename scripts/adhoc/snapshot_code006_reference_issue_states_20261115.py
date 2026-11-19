"""Read current owner issue states for the code006 reference ledger, 2026-11-15.

Inputs: exact reconciled ledger and read-only GitHub issue metadata. Outputs:
exclusive private snapshots and a metadata-only JSON/Markdown report for PR2804.
One real issue canary is required before the remaining issue reads. No issue,
source, reference-validation result or scientific disposition is changed.
"""

import argparse
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LEDGER = "reports/phase2-completion-20261115/code006-reference-owners.json"
LEDGER_SHA = "4c14f2bbad1e4bad4290438a888c52d08d60c4fe6b250316afda4e14fa1e8278"
REPO = "CultureBotAI/CommunityMech"
FIELDS = "number,title,state,url,updatedAt,closedAt"


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def now():
    return datetime.now(timezone.utc).isoformat()


def check_issue(issue, number):
    if (
        issue["number"] != number
        or issue["url"] != f"https://github.com/{REPO}/issues/{number}"
        or issue["state"] not in {"OPEN", "CLOSED"}
    ):
        raise ValueError("issue metadata does not identify the expected owner")


def snapshot(number, output):
    started = now()
    raw = subprocess.check_output(
        ["gh", "issue", "view", str(number), "--repo", REPO, "--json", FIELDS], cwd=ROOT
    )
    issue = json.loads(raw)
    check_issue(issue, number)
    result = {"started_at": started, "finished_at": now(), "issue": issue}
    target = output / f"issue-{number}.json"
    with target.open("x") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    if json.loads(target.read_bytes()) != result:
        raise ValueError("issue snapshot did not persist correctly")
    return target


def capture_snapshots(paths):
    """Bind parsed metadata and digest to the same read for every issue (#2859)."""
    captured = {number: path.read_bytes() for number, path in paths.items()}
    observations = {str(number): json.loads(raw) for number, raw in captured.items()}
    for number in paths:
        check_issue(observations[str(number)]["issue"], number)
    hashes = {str(number): digest(raw) for number, raw in captured.items()}
    return observations, hashes, captured


def verify_snapshots(paths, captured):
    if set(paths) != set(captured) or any(
        path.read_bytes() != captured[number] for number, path in paths.items()
    ):
        raise ValueError("captured issue snapshot changed before publication")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--issue", type=int, help="one real canary issue")
    parser.add_argument("--canary", type=Path, help="verified prior one-issue snapshot")
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    raw = (ROOT / LEDGER).read_bytes()
    if digest(raw) != LEDGER_SHA:
        raise ValueError("exact reconciled reference ledger required")
    ledger = json.loads(raw)
    affected = [row for row in ledger["rows"] if row["native_issues"]]
    numbers = sorted({number for row in affected for number in row["ownership"]["issues"]})
    if args.plan:
        print(json.dumps({"ledger_sha256": LEDGER_SHA, "issues": numbers}))
        return
    output = args.output.resolve()
    if not output.is_relative_to(ROOT / ".temp") or output.exists():
        raise ValueError("new exclusive repository-private output required")
    if args.issue is not None:
        if args.canary or args.issue not in numbers:
            raise ValueError("canary must be one of the exact existing owners")
        output.mkdir(parents=True)
        path = snapshot(args.issue, output)
        print(json.dumps({"path": str(path), "sha256": digest(path.read_bytes())}))
        return
    if not args.canary:
        raise ValueError("a persisted one-issue canary is required before the remaining reads")
    canary = args.canary.resolve()
    if not canary.is_relative_to(ROOT / ".temp"):
        raise ValueError("retained repository-private canary required")
    canary_raw = canary.read_bytes()
    first = json.loads(canary_raw)
    first_number = first["issue"]["number"]
    if first_number not in numbers:
        raise ValueError("canary is not an owner in this ledger")
    check_issue(first["issue"], first_number)
    output.mkdir(parents=True)
    paths = {first_number: canary}
    for number in numbers:
        if number != first_number:
            paths[number] = snapshot(number, output)
    observations, snapshot_hashes, captured = capture_snapshots(paths)
    rows = []
    for row in affected:
        owners = row["ownership"]["issues"]
        rows.append(
            {
                "record": row["record"],
                "id": row["id"],
                "native_issues": row["native_issues"],
                "owners": owners,
                "open_owners": [
                    n for n in owners if observations[str(n)]["issue"]["state"] == "OPEN"
                ],
                "disposition": "Retained reference blocker; no source correction or scientific resolution inferred from issue state.",
            }
        )
    result = {
        "observed_at": now(),
        "ledger": LEDGER,
        "ledger_sha256": LEDGER_SHA,
        "helper_sha256": digest(Path(__file__).read_bytes()),
        "issues": observations,
        "snapshot_sha256": snapshot_hashes,
        "rows": rows,
        "all_affected_records_have_open_owner": all(row["open_owners"] for row in rows),
        "limits": "Issue metadata snapshot only. No scientific assessment, source acquisition, reference rerun or issue mutation.",
    }
    if (ROOT / LEDGER).read_bytes() != raw or canary.read_bytes() != canary_raw:
        raise ValueError("fixed inputs changed during observation")
    verify_snapshots(paths, captured)
    with (output / "report.json").open("x") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    lines = [
        "# Reference blocker issue-state snapshot",
        "",
        f"Observed {result['observed_at']}. The exact code006 ownership ledger remains unchanged.",
        "Issue state does not establish source accuracy or resolve any of the retained reference failures.",
        "",
        "| Owner | State | Title |",
        "|---|---|---|",
    ]
    for number in numbers:
        issue = observations[str(number)]["issue"]
        title = issue["title"].replace("|", "\\|").replace("\n", " ")
        lines.append(f"| [#{number}]({issue['url']}) | {issue['state']} | {title} |")
    lines.extend(["", result["limits"], ""])
    with (output / "report.md").open("x") as stream:
        stream.write("\n".join(lines))
    print(
        json.dumps(
            {
                "report": str(output / "report.json"),
                "all_records_have_open_owner": result["all_affected_records_have_open_owner"],
            }
        )
    )


if __name__ == "__main__":
    main()
