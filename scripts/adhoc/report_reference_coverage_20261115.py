"""Verify and summarize private reference coverage receipts (2026-11-15, #2798).

Inputs: finalized local mirrors of M5 receipt directories and unchanged inputs.
Output: sanitized JSON or Markdown on stdout only; no writes or network calls.
Raw quotes, references, native messages and absolute invocation paths are omitted.
"""

import argparse
import json
import re
from collections import Counter
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TRIAGE = ROOT / "reports/m5-completion-20261114/reference-failure-triage-20261114.md"


def sha(path):
    return sha256(path.read_bytes()).hexdigest()


def checked_summary(path, verify_inputs=True):
    receipt = json.loads(path.read_text())
    if not receipt.get("finished_at") or not isinstance(receipt.get("exit_code"), int):
        raise ValueError("Receipt is not final")
    if verify_inputs:
        for name, expected in receipt["input_sha256"].items():
            source = (ROOT / name).resolve()
            if not source.is_relative_to(ROOT) or sha(source) != expected:
                raise ValueError(f"Input mismatch: {name}")
    raw_paths = {path, path.parent / "started.json"}
    launch_dir = ROOT / ".temp/reference-coverage-launches"
    runtime_path = launch_dir / "m5-python-version.txt"
    runtime = runtime_path.read_text().strip()
    if not re.fullmatch(r"Python \d+\.\d+\.\d+", runtime):
        raise ValueError("Invalid retained Python runtime receipt")
    launch_log = launch_dir / f"{path.parent.name.removeprefix('reference-coverage-')}.log"
    raw_paths.update([runtime_path, launch_log])
    plans = [
        plan
        for plan in launch_dir.glob("m5-plan-*.json")
        if json.loads(plan.read_text())["revision"] == receipt["revision"]
    ]
    if (
        len(plans) != 1
        or json.loads(plans[0].read_text())["selected"] != receipt["declared_records"]
    ):
        raise ValueError("Missing or inconsistent Git-bound launch plan")
    raw_paths.add(plans[0])
    cases = []
    for case in receipt["cases"]:
        name = case["case"]
        case_path, log_path = path.parent / f"{name}.json", path.parent / f"{name}.log"
        if json.loads(case_path.read_text()) != case:
            raise ValueError("Case receipt differs from aggregate receipt")
        raw_paths.update([case_path, log_path])
        input_path = path.parent / f"{name}-input.json"
        if input_path.exists():
            raw_paths.add(input_path)
            expected = case["input_sha256"][str(input_path.relative_to(ROOT))]
            if sha(input_path) != expected:
                raise ValueError("Scratch input differs from the measured bytes")
        rows = case["records"]
        assertions = [item for row in rows for item in row["assertions"]]
        counts = {
            "records_selected": len(receipt["selected_records"]),
            "records_completed": sum(row["completed"] for row in rows),
            "snippet_surfaces": len(assertions),
            "snippet_occurrences_compared": sum(item["actually_compared"] for item in assertions),
            "excerpt_validator_invocations": sum("validator_calls" in item for item in assertions),
            "matcher_calls": sum(item.get("matcher_calls", 0) for item in assertions),
            "substring_calls": sum(item.get("substring_calls", 0) for item in assertions),
            "substring_parts_compared": sum(
                item.get("substring_parts_compared", 0) for item in assertions
            ),
            "title_only_invocations": sum(len(row["title_only"]) for row in rows),
            "native_issues": sum(row["native_issue_count"] for row in rows),
        }
        statuses = dict(sorted(Counter(item["status"] for item in assertions).items()))
        if counts != case["counts"] or statuses != case["assertion_status_counts"]:
            raise ValueError("Per-occurrence counters do not reconcile")
        if case["measurement_valid"]:
            if [row["record"] for row in rows] != receipt["selected_records"]:
                raise ValueError("Complete measurement does not cover the selected inventory")
            native_count = re.findall(
                r"^  Total checks: (\d+)$", log_path.read_text(), re.MULTILINE
            )
            if native_count != [str(counts["native_issues"])]:
                raise ValueError("Native issue counter does not reconcile")
        cases.append(
            {
                "case": name,
                "counts": counts,
                "status_counts": statuses,
                "measurement_valid": case["measurement_valid"],
                "record_processing_complete": case["record_processing_complete"],
                "assertion_coverage_complete": case["assertion_coverage_complete"],
                "native_validation_passed": case["native_validation_passed"],
                "validation_passed": case["validation_passed"],
                "native_exit_code": case["native_exit_code"],
                "error_count": len(case["errors"]),
                "omission_classes": dict(
                    sorted(
                        Counter(
                            item.get("native_class") or "outside_native_traversal"
                            for item in assertions
                            if not item["actually_compared"]
                        ).items()
                    )
                ),
                "records": [
                    {
                        "record": row["record"],
                        "completed": row["completed"],
                        "snippet_surfaces": len(row["assertions"]),
                        "compared": sum(item["actually_compared"] for item in row["assertions"]),
                        "native_issues": row["native_issue_count"],
                        "status_counts": dict(
                            sorted(Counter(item["status"] for item in row["assertions"]).items())
                        ),
                    }
                    for row in rows
                ],
            }
        )
    if any(not p.is_file() or not p.stat().st_size for p in raw_paths):
        raise ValueError("Required raw artifact is missing or empty")
    prior = {}
    for stem, count, description in re.findall(
        r"^\| `([^`]+)` \| (\d+) \| (.*) \|$", TRIAGE.read_text(), re.MULTILINE
    ):
        owners = re.findall(
            r"https://github.com/CultureBotAI/CommunityMech/issues/(\d+)", description
        )
        prior[stem] = (int(count), int(owners[0]) if owners else None)
    for case in cases:
        for row in case["records"]:
            if row["native_issues"]:
                previous = prior.get(Path(row["record"]).stem)
                row["prior_triage_primary_issue"] = (
                    previous[1] if previous and previous[0] == row["native_issues"] else None
                )
    return {
        "attempt": path.parent.name,
        "execution_host": "M5",
        "runtime_python": runtime,
        "code_and_declared_record_revision": receipt["revision"],
        "started_at": receipt["started_at"],
        "finished_at": receipt["finished_at"],
        "dependencies": receipt["dependencies"],
        "script_sha256": receipt["script_sha256"],
        "native_source_sha256": receipt["native_source_sha256"],
        "declared_record_count": len(receipt["declared_records"]),
        "selected_record_count": len(receipt["selected_records"]),
        "inputs_unchanged": receipt["inputs_unchanged"],
        "current_local_inputs_verified": verify_inputs,
        "exit_code": receipt["exit_code"],
        "canary_passed": receipt.get("canary_passed"),
        "cases": cases,
        "prior_triage": {"path": str(TRIAGE.relative_to(ROOT)), "sha256": sha(TRIAGE)},
        "raw_artifacts": {str(p.relative_to(ROOT)): sha(p) for p in sorted(raw_paths)},
    }


def markdown(reports):
    lines = [
        "# Measured native reference coverage on M5",
        "",
        "These are cache-only native CLI measurements. No acquisition, enrichment or input writes were allowed. "
        "Actual comparisons are distinct from retained issues, skipped prefixes and unannotated snippets. "
        "Lexical comparison does not establish scientific truth.",
        "",
        "| Attempt / case | Records completed / selected | Snippet surfaces | Occurrences compared | Native issues | Measurement valid | Native exit |",
        "| --- | ---: | ---: | ---: | ---: | --- | ---: |",
    ]
    for report in reports:
        for case in report["cases"]:
            c = case["counts"]
            lines.append(
                f"| {report['attempt']} / {case['case']} | {c['records_completed']}/{c['records_selected']} | "
                f"{c['snippet_surfaces']} | {c['snippet_occurrences_compared']} | {c['native_issues']} | "
                f"{case['measurement_valid']} | {case['native_exit_code']} |"
            )
    for report in reports:
        lines.extend(
            [
                "",
                f"## {report['attempt']}",
                "",
                f"Exact code and declared-record revision: `{report['code_and_declared_record_revision']}`. "
                f"Input hashes unchanged: **{report['inputs_unchanged']}**. Wrapper exit: **{report['exit_code']}**.",
                "",
            ]
        )
        for case in report["cases"]:
            lines.append(
                f"{case['case']}: assertion coverage complete = **{case['assertion_coverage_complete']}**; "
                f"native validation passed = **{case['native_validation_passed']}**."
            )
            lines.append("")
            if (
                case["record_processing_complete"]
                and report["selected_record_count"] == report["declared_record_count"]
            ):
                findings = sorted(
                    (row for row in case["records"] if row["native_issues"]),
                    key=lambda row: (-row["native_issues"], row["record"]),
                )
                lines.extend(
                    [
                        "| Record with native findings | Issues | Prior tracking owner |",
                        "| --- | ---: | --- |",
                    ]
                )
                for row in findings:
                    owner = row.get("prior_triage_primary_issue")
                    link = (
                        f"[#{owner}](https://github.com/CultureBotAI/CommunityMech/issues/{owner})"
                        if owner
                        else "Needs triage"
                    )
                    lines.append(
                        f"| {Path(row['record']).stem} | {row['native_issues']} | {link} |"
                    )
                lines.append("")
            lines.extend(["| Occurrence outcome | Count |", "| --- | ---: |"])
            lines.extend(
                f"| {status} | {count} |" for status, count in case["status_counts"].items()
            )
            lines.append("")
    lines.extend(
        [
            "## Boundaries and unresolved owners",
            "",
            "SupportingReference's unannotated snippets remain owned by [#476](https://github.com/CultureBotAI/CommunityMech/issues/476). "
            "BIOPROJECT skips are configured exclusions, not successful text comparisons. "
            "Missing content and substring mismatches remain native findings, not proof that a scientific claim is false. "
            "Supplement-specific routing remains owned by [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996). "
            "No supplement or alternative source was substituted.",
            "",
            "The first corpus attempt is retained as incomplete/invalid: YAML1.1 inventory loading disagreed with the "
            "native YAML1.2 parser ([#2799](https://github.com/CultureBotAI/CommunityMech/issues/2799)). "
            "Its partial counters must not be combined with a later full attempt. The native parser correction retained "
            "record/cache bytes and matching rules. Reference-identity binding is guarded by "
            "[#2795](https://github.com/CultureBotAI/CommunityMech/issues/2795).",
            "",
            "The adjacent JSON contains per-record status counts and SHA256 hashes of the private raw receipts/logs. "
            "Raw source excerpts, reference values and local invocation paths are deliberately omitted here.",
            "Tracking owners are carried from the retained earlier triage only where the record and finding count agree; "
            "this is routing metadata, not a new scientific disposition or a live issue-state claim.",
            "The JSON also hashes the retained Python-version receipt, exact Git-bound launch plan "
            "and same-path nohup/just output for each attempt.",
            "",
        ]
    )
    runtimes = ", ".join(sorted({report["runtime_python"] for report in reports}))
    lines.append(f"Verified runtime: {runtimes} on M5.")
    for report in reports:
        for case in report["cases"]:
            if (
                case["record_processing_complete"]
                and report["selected_record_count"] == report["declared_record_count"]
            ):
                lines.append(
                    f"Complete corpus native prefix skips: {case['status_counts'].get('skipped_prefix', 0)}; "
                    f"title-only validations: {case['counts']['title_only_invocations']}; "
                    f"uncompared SupportingReference surfaces: {case['omission_classes'].get('SupportingReference', 0)}."
                )
    lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipt", type=Path, action="append", required=True)
    parser.add_argument("--format", choices=["json", "markdown"], default="json")
    args = parser.parse_args()
    reports = [checked_summary(path.resolve()) for path in args.receipt]
    print(json.dumps(reports, indent=2) if args.format == "json" else markdown(reports))


if __name__ == "__main__":
    main()
