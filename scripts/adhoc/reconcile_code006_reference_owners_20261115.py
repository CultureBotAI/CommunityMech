"""Reconcile current c9 reference failures with historical owners, 2026-11-15.

Inputs: pinned public/native measurement and immutable 20185647 owner ledger.
Output: metadata-only JSON on stdout; caller chooses an exclusive destination.
Serves PR2804/#476 accounting. No validator, acquisition, source or cache writes.
"""

import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REVISION = "c9e151eb9f22afb5c531dd5a8b3346ce1d58b12a"
SUMMARY = "reports/phase2-completion-20261115/code006-reference-measurement.json"
SUMMARY_SHA = "0ad5e6a4de4e2f8ee86e7fb6029dc99297c3d8f189e948a5e90b6b85de9cb7b8"
PREVIOUS = "reports/phase2-reference-blockers-20261115/reference-blockers-20185647.json"
PREVIOUS_SHA = "6b4f1ae65b0ad3c0b9c5c6fd98a0f51202ba64e8adabc18db4506fffa6730f63"
MEASUREMENT = ".temp/phase2-reference-code006-20261115/corpus-001/measurement.json"
PROCESS_EXIT = ".temp/phase2-schema-20261115/code006-reference-corpus-001.exit"
FIELDS = (
    "path",
    "reference",
    "native_class",
    "status",
    "actually_compared",
    "cache_path",
    "cache_sha256",
    "content_type",
)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def failure(item):
    cache = item.get("cache", {})
    return {
        **{key: item[key] for key in FIELDS[:5]},
        "cache_path": cache.get("requested_path"),
        "cache_sha256": cache.get("sha256"),
        "content_type": cache.get("content_type"),
    }


def unique_rows(rows):
    result = {row["record"]: row for row in rows}
    require(len(result) == len(rows), "duplicate record rows")
    return result


def reconcile(summary, measured, previous, source_bytes):
    require(measured["measurement_valid"] is True, "invalid native measurement")
    require(summary["counts"] == measured["counts"], "aggregate counters differ")
    require(summary["status_counts"] == measured["assertion_status_counts"], "statuses differ")
    require(summary["record_processing_complete"] is True, "incomplete record traversal")
    current = unique_rows(measured["records"])
    published = unique_rows(summary["records"])
    old = unique_rows(previous["rows"])
    require(set(current) == set(published), "published and measured inventory differ")
    require(len(current) == summary["counts"]["records_completed"], "record count differs")
    totals, compared, output = Counter(), 0, []
    old_failures = {path for path, row in old.items() if row["native_issues"]}
    new_failures = set()
    for path, observed in current.items():
        pub = published[path]
        items = observed["assertions"]
        statuses = Counter(item["status"] for item in items)
        require(dict(statuses) == pub["status_counts"], "per-record statuses differ")
        require(len(items) == pub["surfaces"], "per-record surface count differs")
        require(
            all(type(item["actually_compared"]) is bool for item in items),
            "invalid comparison flag",
        )
        record_compared = sum(item["actually_compared"] for item in items)
        require(record_compared == pub["compared"], "per-record comparison count differs")
        totals.update(statuses)
        compared += record_compared
        bad = [failure(item) for item in items if item["status"] != "matched"]
        require(
            len(bad) == pub["native_issues"] == observed["native_issue_count"],
            "issue count differs",
        )
        if bad:
            new_failures.add(path)
            require(path in old_failures, "new failure record requires fresh ownership")
            before = old[path]
            require(
                digest(source_bytes(path)) == before["record_sha256"],
                "affected record bytes changed",
            )
            require(
                Counter(tuple(row[key] for key in FIELDS) for row in bad)
                == Counter(tuple(row[key] for key in FIELDS) for row in before["failures"]),
                "failure occurrence or source binding differs; ownership requires review",
            )
        if bad or old.get(path, {}).get("phase2_scope"):
            require(path in old, "new scoped record requires explicit inventory")
            raw = source_bytes(path)
            require(
                digest(raw) == measured["input_sha256"][path], "measured record differs from Git"
            )
            output.append(
                {
                    "record": path,
                    "id": old[path]["id"],
                    "record_sha256": digest(raw),
                    "phase2_scope": old[path]["phase2_scope"],
                    "surfaces": len(items),
                    "compared": record_compared,
                    "native_issues": len(bad),
                    "status_counts": dict(statuses),
                    "native_classes": pub["native_classes"],
                    "failures": bad,
                    "ownership": (
                        old[path]["ownership"]
                        if bad
                        else {
                            "issues": [],
                            "note": "No native issue in this current run; no scientific verdict inferred.",
                        }
                    ),
                }
            )
    require(new_failures == old_failures, "historical/current affected inventories differ")
    require(dict(totals) == summary["status_counts"], "aggregate status census differs")
    require(sum(totals.values()) == summary["counts"]["snippet_surfaces"], "surface census differs")
    require(
        compared == summary["counts"]["snippet_occurrences_compared"], "comparison census differs"
    )
    require(
        sum(row["native_issues"] for row in output) == summary["counts"]["native_issues"],
        "failure census differs",
    )
    scoped = [row for row in output if row["phase2_scope"]]
    require(
        {row["record"] for row in scoped} == {p for p, row in old.items() if row["phase2_scope"]},
        "scoped inventory differs",
    )
    classes = Counter(item["native_class"] for row in output for item in row["failures"])
    return {
        "measurement_revision": summary["measurement_revision"],
        "previous_measurement_revision": previous["measurement_revision"],
        "counts": summary["counts"],
        "status_counts": summary["status_counts"],
        "record_processing_complete": summary["record_processing_complete"],
        "assertion_coverage_complete": summary["assertion_coverage_complete"],
        "native_exit_code": summary["native_exit_code"],
        "exact_failure_tuple_reconciliation": True,
        "affected_records": len(new_failures),
        "failure_classes": dict(classes),
        "phase2": {
            "records": len(scoped),
            "surfaces": sum(row["surfaces"] for row in scoped),
            "compared": sum(row["compared"] for row in scoped),
            "matched": sum(row["status_counts"].get("matched", 0) for row in scoped),
            "native_issues": sum(row["native_issues"] for row in scoped),
        },
        "rows": output,
        "ownership_observation": "Existing owners are reused only after exact occurrence, record-byte and cache-byte equality. Issue state snapshots remain historical; no fresh GitHub status read or source review is claimed.",
        "limits": "Current lexical matching is not scientific proof or aggregate QC success. No new scientific scope, source acquisition, validator rerun or issue closure.",
    }


def main():
    summary_raw, previous_raw = (ROOT / SUMMARY).read_bytes(), (ROOT / PREVIOUS).read_bytes()
    require(digest(summary_raw) == SUMMARY_SHA, "public measurement digest differs")
    require(digest(previous_raw) == PREVIOUS_SHA, "historical owner ledger digest differs")
    summary, previous = json.loads(summary_raw), json.loads(previous_raw)
    raw = (ROOT / MEASUREMENT).read_bytes()
    require(
        digest(raw) == summary["raw_artifact_sha256"]["measurement.json"],
        "native measurement digest differs",
    )
    require(summary["measurement_revision"] == REVISION, "unexpected current revision")
    exit_raw = (ROOT / PROCESS_EXIT).read_bytes()
    require(
        digest(exit_raw) == summary["raw_artifact_sha256"]["process.exit"],
        "independent exit digest differs",
    )
    require(exit_raw == b"1\n", "expected actual native failed exit")
    result = reconcile(
        summary,
        json.loads(raw),
        previous,
        lambda path: subprocess.check_output(
            ["git", "show", f"{REVISION}:{path}"],
            cwd=ROOT,
        ),
    )
    result["provenance"] = {
        "public_summary": {"path": SUMMARY, "sha256": SUMMARY_SHA},
        "historical_ledger": {"path": PREVIOUS, "sha256": PREVIOUS_SHA},
        "raw_measurement": {"path": MEASUREMENT, "sha256": digest(raw)},
        "independent_process_exit": {"path": PROCESS_EXIT, "sha256": digest(exit_raw)},
        "helper_sha256": digest(Path(__file__).read_bytes()),
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
