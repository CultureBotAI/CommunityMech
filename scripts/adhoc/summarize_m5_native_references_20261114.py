"""Summarize native M5 reference evidence for #622/#2790/#2791/#2792 (2026-11-14).

Input: one retained native qc-references log, optionally one exact record path,
an exact-revision Git path inventory and the completed native command receipt.
Output: JSON on stdout only; the caller retains it under a unique evidence name.
No writes, fetching, validators, or explanatory annotation heuristics are used.
Native 'Total checks' counts retained findings, not examined evidence excerpts.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from collections import Counter
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
RECORD = re.compile(r"^(?:\\n)?Validating references in (.+?)\.\.\.$")
ISSUE = re.compile(r"^\s+\[(ERROR|WARNING|INFO)\]\s+(.*)$")
TOTAL = re.compile(r"^\s+Total checks: (\d+)$")
EXPECTED_RECORD = re.compile(r"^(?:kb/communities|data/isolates)/[^/]+\.yaml$")


def git_inventory(revision):
    """Read the exact local commit tree; never fetch or change repository state (#2791)."""
    try:
        resolved = subprocess.check_output(
            ["git", "rev-parse", "--verify", revision + "^{commit}"],
            cwd=REPO,
            text=True,
            stderr=subprocess.PIPE,
        ).strip()
        if resolved != revision:
            raise ValueError("expected revision must identify an exact local commit")
        listing = subprocess.check_output(
            [
                "git",
                "ls-tree",
                "-r",
                "--name-only",
                revision,
                "--",
                "kb/communities",
                "data/isolates",
            ],
            cwd=REPO,
            text=True,
            stderr=subprocess.PIPE,
        )
    except subprocess.CalledProcessError as error:
        raise ValueError("expected commit is unavailable in the local Git repository") from error
    return {name for name in listing.splitlines() if EXPECTED_RECORD.fullmatch(name)}


def category(message):
    if message.startswith("No content available for reference:"):
        return "source_content_unavailable"
    if message.startswith("Text part not found as substring:"):
        return "excerpt_substring_mismatch"
    return "other_native_finding"


def parse(log):
    """Keep native record boundaries, findings and acquisition diagnostics distinct."""
    rows = []
    current = None
    last_issue = None
    for line in log.splitlines():
        marker = RECORD.fullmatch(line)
        if marker:
            current = {
                "record": marker[1],
                "status": "INCOMPLETE",
                "native_retained_findings": None,
                "findings": [],
                "acquisition_messages": [],
                "native_lines": [],
            }
            rows.append(current)
            last_issue = None
            continue
        if line.startswith("===> running recipe"):
            current = None
            last_issue = None
        if current is None:
            continue
        current["native_lines"].append(line)
        match = ISSUE.fullmatch(line)
        if match:
            last_issue = {
                "severity": match[1],
                "message": match[2],
                "category": category(match[2]),
                "location": None,
                "reference": None,
            }
            current["findings"].append(last_issue)
        elif last_issue is not None and line.strip().startswith("Location: "):
            last_issue["location"] = line.strip().removeprefix("Location: ")
        elif last_issue is not None and line.strip().startswith("Reference: "):
            last_issue["reference"] = line.strip().removeprefix("Reference: ")
        if line.startswith("Download failed for ") or (
            line.startswith("Provider '") and " failed for " in line
        ):
            current["acquisition_messages"].append(line)
        total = TOTAL.fullmatch(line)
        if total:
            current["native_retained_findings"] = int(total[1])
        if line.strip() == "All validations passed!":
            current["status"] = "NATIVE_PASSED"
        elif re.fullmatch(r"\s+Issues found in \d+ file\(s\) \(\d+ validation issue\(s\)\)", line):
            current["status"] = "NATIVE_FINDINGS"
    for row in rows:
        if row["status"] != "INCOMPLETE":
            if row["native_retained_findings"] != len(row["findings"]):
                raise ValueError(f"native finding count does not reconcile: {row['record']}")
            if (row["status"] == "NATIVE_PASSED") != (not row["findings"]):
                raise ValueError(f"native status contradicts findings: {row['record']}")
    return rows


def summarize(data, record=None, *, expected_data=None, revision=None, receipt=None):
    rows = parse(data.decode("utf-8"))
    if record is not None:
        rows = [row for row in rows if row["record"] == record]
        if len(rows) != 1:
            raise ValueError("the requested record must appear exactly once")
    if not rows:
        raise ValueError("no native reference record boundaries found")
    names = [row["record"] for row in rows]
    name_counts = Counter(names)
    duplicates = sorted(name for name, count in name_counts.items() if count > 1)
    statuses = Counter(row["status"] for row in rows)
    findings = [finding for row in rows for finding in row["findings"]]
    result = {
        "native_log_sha256": hashlib.sha256(data).hexdigest(),
        "native_log_bytes": len(data),
        "record_filter": record,
        "interpretation": (
            "Native Total checks counts retained findings, not examined excerpts. "
            "Acquisition failures are separate from validation findings. "
            "Substring mismatches identify matcher outcomes, not scientific verdicts."
        ),
        "records_started": len(rows),
        "unique_records_started": len(name_counts),
        "duplicate_records": duplicates,
        "records_completed": len(rows) - statuses["INCOMPLETE"],
        "records_native_passed": statuses["NATIVE_PASSED"],
        "records_with_native_findings": statuses["NATIVE_FINDINGS"],
        "records_incomplete": statuses["INCOMPLETE"],
        "native_findings_by_severity": dict(
            sorted(Counter(x["severity"] for x in findings).items())
        ),
        "native_findings_by_category": dict(
            sorted(Counter(x["category"] for x in findings).items())
        ),
        "records": rows,
    }
    if (expected_data is None) != (revision is None):
        raise ValueError("expected inventory and revision must be supplied together")
    if expected_data is not None:
        if record is not None:
            raise ValueError("full-sweep inventory cannot be combined with a record filter")
        if not re.fullmatch(r"[0-9a-f]{40}", revision):
            raise ValueError("expected revision must be a full lowercase Git commit SHA")
        expected = expected_data.decode("utf-8").splitlines()
        if not expected or any(not EXPECTED_RECORD.fullmatch(name) for name in expected):
            raise ValueError("inventory must contain exact top-level native sweep paths")
        if len(set(expected)) != len(expected):
            raise ValueError("expected inventory contains duplicate paths")
        actual = git_inventory(revision)
        if set(expected) != actual:
            raise ValueError("saved inventory does not match the exact local Git tree")
        missing = sorted(set(expected) - set(names))
        unexpected = sorted(set(names) - set(expected))
        incomplete = sorted(row["record"] for row in rows if row["status"] == "INCOMPLETE")
        result["coverage"] = {
            "expected_revision": revision,
            "expected_inventory_sha256": hashlib.sha256(expected_data).hexdigest(),
            "expected_records": len(expected),
            "git_inventory_verified": True,
            "missing_records": missing,
            "unexpected_records": unexpected,
            "duplicate_records": duplicates,
            "incomplete_records": incomplete,
            "complete": not (missing or unexpected or duplicates or incomplete),
        }
    if receipt is not None:
        if expected_data is None:
            raise ValueError("final receipt binding requires the expected inventory and revision")
        if (
            receipt.get("head") != revision
            or receipt.get("log_sha256") != result["native_log_sha256"]
            or receipt.get("log_bytes") != len(data)
        ):
            raise ValueError("native receipt revision or log bytes/hash do not match")
        command = receipt.get("command", [])
        if (
            not isinstance(command, list)
            or not command
            or not isinstance(command[0], str)
            or not Path(command[0]).is_absolute()
            or Path(command[0]).name != "just"
            or command[1:] != ["--verbose", "--no-dotenv", "--color", "never", "qc-references"]
        ):
            raise ValueError("receipt must match the exact native runner command contract")
        if receipt.get("dry_run") is not False or receipt.get("diagnostic_no_deps") is not False:
            raise ValueError("receipt must explicitly identify a real full-dependency execution")
        try:
            started = datetime.fromisoformat(receipt["started_at"])
            finished = datetime.fromisoformat(receipt["finished_at"])
        except (KeyError, TypeError, ValueError) as error:
            raise ValueError("receipt must contain completed native timestamps") from error
        if started.utcoffset() is None or finished.utcoffset() is None or finished < started:
            raise ValueError("native timestamps must be timezone-aware and chronological")
        code = receipt.get("exit_code")
        status = receipt.get("status")
        if type(code) is not int or status != ("PASSED" if code == 0 else "FAILED"):
            raise ValueError("native receipt lacks a consistent completed command outcome")
        stages = {row["recipe"]: row["status"] for row in receipt.get("stages", [])}
        if stages.get("validate-references-all") not in {"PASSED", "FAILED", "FAILED WITH SKIPS"}:
            raise ValueError("native receipt does not show a completed reference stage")
        result["native_command"] = {
            "name": receipt.get("name"),
            "command": command,
            "exit_code": code,
            "status": status,
            "reference_stage_status": stages["validate-references-all"],
            "started_at": receipt.get("started_at"),
            "finished_at": receipt.get("finished_at"),
            "initial_git_status": receipt.get("initial_git_status"),
            "final_git_status": receipt.get("final_git_status"),
        }
    return result


def public_derivative(result):
    """Omit raw diagnostic lines and apply the existing evidence privacy scrubber."""
    from export_m5_technical_evidence_20261114 import sanitize

    result = json.loads(json.dumps(result))
    for row in result["records"]:
        row.pop("native_lines")
        row["acquisition_message_count"] = len(row.pop("acquisition_messages"))
    counts = Counter()
    result = json.loads(sanitize(json.dumps(result), counts))
    result["public_derivative"] = {
        "raw_lines_omitted": True,
        "redactions": {key: value for key, value in sorted(counts.items()) if value},
        "note": "Exact raw diagnostics remain in the private snapshot identified by native_log_sha256.",
    }
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("log", type=Path)
    parser.add_argument("--record", help="one exact native record path for the real canary")
    parser.add_argument(
        "--expected-records", type=Path, help="saved exact-revision Git path inventory"
    )
    parser.add_argument("--expected-revision", help="full Git SHA that produced the path inventory")
    parser.add_argument("--command-receipt", type=Path, help="completed native qc-references JSON")
    parser.add_argument(
        "--public", action="store_true", help="omit raw lines and redact private text"
    )
    args = parser.parse_args()
    result = summarize(
        args.log.read_bytes(),
        args.record,
        expected_data=args.expected_records.read_bytes() if args.expected_records else None,
        revision=args.expected_revision,
        receipt=json.loads(args.command_receipt.read_text()) if args.command_receipt else None,
    )
    print(json.dumps(public_derivative(result) if args.public else result, indent=2))


if __name__ == "__main__":
    main()
