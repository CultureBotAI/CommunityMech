"""Emit whole-record residual planning groups after the verified000434 canary.

#2848, 2026-11-15. Reads immutable historical partition and current selected
bytes plus exact published completion proof. JSON stdout only; no writes,
network, automatic approval, science claim or partial-record completion.
"""

import argparse
import hashlib
import json
import subprocess
from collections import Counter, defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
PARTITION = ROOT / ".temp/gtdb-code006-20261115/partition-corpus-001.json"
PARTITION_SHA = "261f9193a9d1ad5ceefc05178b512f3b52d1fa6a23c325e5312905d06a32cf15"
SUMMARY = ROOT / "reports/gtdb-code006-20261115/canary-000434-003/summary.json"
SUMMARY_SHA = "2c7943d15a2e067a849b22ed5f387c4b86b7c8c90412189b58cb8ddb818832ee"


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--record", help="one whole-record read-only canary")
    args = parser.parse_args()
    inputs = {}

    def read(path, expected=None):
        raw = path.read_bytes()
        actual = digest(raw)
        if expected is not None and actual != expected:
            raise ValueError("retained input differs")
        inputs[str(path.relative_to(ROOT))] = actual
        return raw

    read(Path(__file__))
    original = json.loads(read(PARTITION, PARTITION_SHA))
    proof = json.loads(read(SUMMARY, SUMMARY_SHA))
    completed = proof["record"]
    before, after = proof["applications"]
    if before["after_sha256"] != after["before_sha256"]:
        raise ValueError("completed application chain differs")
    if before["before_sha256"] != original["inputs"][completed]:
        raise ValueError("completed preimage differs from historical partition")
    if after["after_sha256"] != proof["final_record_sha256"]:
        raise ValueError("completed final hash differs")
    for application in proof["applications"]:
        actual = json.loads(read(SUMMARY.parent / application["file"], application["sha256"]))
        if (
            actual["applied"] is not True
            or actual["before_sha256"] != application["before_sha256"]
            or actual["after_sha256"] != application["after_sha256"]
        ):
            raise ValueError("actual completed receipt differs")
    current = read(ROOT / completed, proof["final_record_sha256"])
    review_row = proof["saved_assessments"][1]
    review_path = ROOT / "reviews/structured" / review_row["review_id"] / "review.yaml"
    review = yaml.safe_load(read(review_path, review_row["review_sha256"]))
    if (
        review["scientific_review"] is not False
        or review["verdict"] != "pass_with_limitations"
        or not all(check["status"] == "passed" for check in review["checks"] if check["required"])
    ):
        raise ValueError("completed technical canary did not pass required checks")
    bound = [row for row in review["source"]["inputs"] if row["path"] == completed]
    if len(bound) != 1 or bound[0]["sha256"] != digest(current):
        raise ValueError("completed saved review does not bind current record")
    rows_by_record = defaultdict(list)
    for row in original["rows"]:
        rows_by_record[row["record"]].append(row)
    if len(rows_by_record[completed]) != 1:
        raise ValueError("do not treat a partly corrected record as complete")
    del rows_by_record[completed]
    if args.record:
        matches = {
            name: rows
            for name, rows in rows_by_record.items()
            if rows[0]["record_id"] == args.record
        }
        if len(matches) != 1:
            raise ValueError("one actual residual record required")
        rows_by_record = matches
    groups = defaultdict(list)
    for name, rows in sorted(rows_by_record.items()):
        read(ROOT / name, original["inputs"][name])
        categories = set()
        for row in rows:
            result = row["native_result"] or {}
            if row["existing_native_curated"] or row["existing_native_withheld"]:
                categories.add("manual_hold")
            elif row["partition"].startswith("status_"):
                categories.add(
                    "ambiguous"
                    if row["partition"].endswith("ambiguous")
                    else "unsupported_or_scope_status"
                )
            elif result.get("is_reclassified"):
                categories.add("renamed_mapping")
            elif row["partition"] == "species_or_strain_reference_correspondence":
                categories.add("same_name_species_or_strain")
            else:
                categories.add("same_name_higher_rank")
        key = "+".join(sorted(categories))
        guards = sorted(
            {
                test
                for row in rows
                for binding in row["historical_byte_bindings"]
                for test in binding["tests_referencing_ledger"]
            }
        )
        for guard in guards:
            read(ROOT / guard)
        groups[key].append(
            {
                "record": name,
                "record_id": rows[0]["record_id"],
                "baseline_sha256": original["inputs"][name],
                "occurrences": [
                    {
                        "selector": row["selector"],
                        "id": row["id"],
                        "label": row["label"],
                        "partition": row["partition"],
                        "native_result": row["native_result"],
                    }
                    for row in rows
                ],
                "historical_ledgers": sorted(
                    {
                        binding["ledger"]
                        for row in rows
                        for binding in row["historical_byte_bindings"]
                    }
                ),
                "candidate_historical_guard_files": guards,
                "guard_review": "Confirmed exact batch147 full-hash guards for000552/000553; other ledger-referencing files remain candidates requiring per-record scope inspection before application.",
                "approval": "NOT_APPROVED; assign whole record to one agent, inspect source and all occurrences, preserve science and obtain successor proof before apply",
            }
        )
    if inputs != {name: digest((ROOT / name).read_bytes()) for name in inputs}:
        raise ValueError("input changed during residual planning")
    print(
        json.dumps(
            {
                "historical_source_revision": original["source_revision"],
                "execution_revision": subprocess.check_output(
                    ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
                ).strip(),
                "historical_occurrences": original["measured_taxonomy_occurrences"],
                "historical_records": original["measured_record_files"],
                "excluded_complete_records": [
                    {
                        "record": completed,
                        "proof": str(SUMMARY.relative_to(ROOT)),
                        "sha256": SUMMARY_SHA,
                    }
                ],
                "selected_residual_records": len(rows_by_record),
                "selected_residual_occurrences": sum(map(len, rows_by_record.values())),
                "group_record_counts": dict(
                    Counter({key: len(rows) for key, rows in groups.items()})
                ),
                "groups": dict(groups),
                "inputs": inputs,
                "inputs_unchanged": True,
                "limits": "Whole-record planning from the historical native partition plus exact one-record completion proof; no fresh corpus classifier run or scientific approval. Other concurrent branch repairs are not silently excluded. No record may be split across agents.",
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
