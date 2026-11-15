"""Assign disjoint whole-record repair lanes for #2848, 2026-11-15.

Inputs: frozen historical residual plan and exact current record bytes.
Outputs: new JSON/Markdown planning ledger. No curation, source acquisition,
scientific approval, current-classifier claim or completion assertion.
"""

import argparse
import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / ".temp/gtdb-code006-20261115/residual-groups-001.json"
SOURCE_SHA = "eaf78e16c342e36a0aa82c52c45888e8efb667fc2b70aa8d77ead956024f5f7c"
LANES = {
    "same_name_higher_rank": "genus",
    "same_name_species_or_strain": "species",
    "renamed_mapping": "species",
    "ambiguous": "ambiguity",
    "unsupported_or_scope_status": "ambiguity",
    "ambiguous+same_name_species_or_strain": "ambiguity",
    "ambiguous+renamed_mapping": "ambiguity",
    "renamed_mapping+same_name_species_or_strain": "species",
    "ambiguous+renamed_mapping+same_name_species_or_strain": "species",
    "same_name_higher_rank+same_name_species_or_strain": "genus",
    "ambiguous+same_name_higher_rank": "genus",
    "ambiguous+renamed_mapping+same_name_higher_rank": "genus",
    "renamed_mapping+same_name_higher_rank": "genus",
    "ambiguous+same_name_higher_rank+unsupported_or_scope_status": "genus",
    "ambiguous+renamed_mapping+same_name_higher_rank+same_name_species_or_strain": "genus",
    "renamed_mapping+same_name_higher_rank+same_name_species_or_strain": "genus",
}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", help="one real planning canary, e.g. CommunityMech:000552")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    if not output.is_relative_to(ROOT) or output.exists():
        raise ValueError("new output inside this repository required")
    source_raw = SOURCE.read_bytes()
    if sha(source_raw) != SOURCE_SHA:
        raise ValueError("exact historical residual plan required")
    source = json.loads(source_raw)
    if set(source["groups"]) != set(LANES):
        raise ValueError("planning categories changed; inspect before assignment")
    captured = {SOURCE: source_raw, Path(__file__): Path(__file__).read_bytes()}
    records, seen = [], set()
    for group, members in sorted(source["groups"].items()):
        for row in members:
            if args.record and row["record_id"] != args.record:
                continue
            relative = Path(row["record"])
            path = ROOT / relative
            if relative.is_absolute() or not path.resolve().is_relative_to(ROOT):
                raise ValueError("record path escapes checkout")
            raw = path.read_bytes()
            if sha(raw) != row["baseline_sha256"] or row["record_id"] in seen:
                raise ValueError("record changed or received overlapping assignments")
            seen.add(row["record_id"])
            captured[path] = raw
            records.append({**row, "group": group, "lane": LANES[group]})
    expected = 1 if args.record else 126
    if len(records) != expected:
        raise ValueError("unexpected whole-record population")
    counts = dict(sorted(Counter(row["lane"] for row in records).items()))
    occurrences = sum(len(row["occurrences"]) for row in records)
    if not args.record and (
        counts != {"ambiguity": 30, "genus": 40, "species": 56} or occurrences != 418
    ):
        raise ValueError("whole-record lane counts differ from reviewed partition")
    result = {
        "kind": "PLANNING ONLY",
        "execution_revision": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip(),
        "source_sha256": SOURCE_SHA,
        "historical_source_revision": source["historical_source_revision"],
        "selected_records": len(records),
        "selected_occurrences": occurrences,
        "lane_record_counts": counts,
        "records": records,
        "input_sha256": {str(path.relative_to(ROOT)): sha(raw) for path, raw in captured.items()},
        "limits": "Assignment only, from the retained historical classifier partition. No record is split across lanes. Other branches' ongoing repairs are not silently counted complete. Each record requires current source inspection, guarded application, native checks and immutable saved successor assessment. A new route requires one verified real canary before a batch. Full scientific review remains distinct.",
    }
    lines = [
        "# Whole-record GTDB repair assignments",
        "",
        result["limits"],
        "",
        f"Source plan SHA-256: `{SOURCE_SHA}`.",
        f"Current-record byte check at `{result['execution_revision']}`.",
        f"Selected: {len(records)} records / {occurrences} affected taxonomy occurrences.",
        "",
        "| Lane | Whole records |",
        "|---|---:|",
        *(f"| {lane} | {count} |" for lane, count in counts.items()),
        "",
        "Start with each lane's already selected canary. Complete pure groups before",
        "mixed groups; inspect all affected occurrences together. The genus lane owns",
        "every mixed record containing a higher-rank occurrence. The species lane",
        "owns the two mixed groups containing both renamed and same-name species.",
        "The ambiguity lane owns the other mixed groups and the pure unsupported case.",
        "",
        "| Record | Lane | Affected occurrences | Source group |",
        "|---|---|---:|---|",
        *(
            f"| {row['record_id']} · `{row['record']}` | {row['lane']} | {len(row['occurrences'])} | {row['group']} |"
            for row in sorted(records, key=lambda item: (item["lane"], item["record_id"]))
        ),
        "",
    ]
    if any(path.read_bytes() != raw for path, raw in captured.items()):
        raise ValueError("input changed during assignment")
    output.mkdir()
    (output / "assignments.json").write_text(json.dumps(result, indent=2) + "\n")
    (output / "README.md").write_text("\n".join(lines))
    print(json.dumps({"records": len(records), "occurrences": occurrences, "lanes": counts}))


if __name__ == "__main__":
    main()
