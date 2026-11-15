"""Summarize the retained native code006 GTDB trace, 2026-11-15.

Input: completed two-tests-001 native log and receipt, for #2848/#2849 diagnostic
ownership. Output: JSON to stdout only. No classifier rerun, network, record
writes or claim that stored statuses should be automatically replaced.
"""

import ast
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/gtdb-code006-20261115"


def main():
    raw = (STATE / "two-tests-001.log").read_bytes()
    receipt = json.loads((STATE / "two-tests-001.json").read_bytes())
    digest = hashlib.sha256(raw).hexdigest()
    if receipt["exit_code"] != 1 or receipt["log_sha256"] != digest:
        raise ValueError("completed failed native log binding required")
    text = raw.decode()
    expected = re.search(r"AssertionError: (\d+) statuses do not reproduce:", text)
    full = re.findall(r"^E\s+assert not (\[.*\])$", text, re.MULTILINE)
    if expected is None or len(full) != 1:
        raise ValueError("one complete status failure list required")
    rows = ast.literal_eval(full[0])
    if (
        not isinstance(rows, list)
        or len(rows) != int(expected[1])
        or not all(isinstance(r, str) for r in rows)
    ):
        raise ValueError("native status count does not reconcile")
    parsed = []
    for value in rows:
        record, message = value.split(": ", 1)
        match = re.fullmatch(r"(.+) stored (\w+), classifier says (\w+)", message)
        if match:
            parsed.append(
                {
                    "record": record,
                    "taxon_label": match[1],
                    "kind": "status",
                    "stored": match[2],
                    "computed": match[3],
                }
            )
        elif message.endswith(" candidate list does not reproduce"):
            parsed.append(
                {
                    "record": record,
                    "taxon_label": message.removesuffix(" candidate list does not reproduce"),
                    "kind": "candidates",
                }
            )
        else:
            raise ValueError("unrecognized native failure row")
    # Anchor the actual per-record diagnostic, excluding pytest's repeated
    # assertion repr and its "Left contains" summary (#2848 diagnostic follow-up).
    mapping_lines = re.findall(
        r"^E\s+([A-Za-z0-9_]+\.yaml: '[^']+' stores GTDB:[^,]+, tool says [^\n]+)$",
        text,
        re.MULTILINE,
    )
    if len(mapping_lines) != 3 or len(set(mapping_lines)) != 3:
        raise ValueError("three distinct native mapping diagnostics required")
    transitions = Counter(
        f"{row['stored']} -> {row['computed']}" for row in parsed if row["kind"] == "status"
    )
    phase2_source = (
        ROOT / "reports/phase2-reference-blockers-20261115/reference-blockers-20185647.json"
    )
    phase2_bytes = phase2_source.read_bytes()
    phase2_records = [
        row["record"] for row in json.loads(phase2_bytes)["rows"] if row["phase2_scope"]
    ]
    if len(phase2_records) != 6:
        raise ValueError("exact six-record Phase2 scope required")
    affected = {row["record"] for row in parsed} | {row.split(": ", 1)[0] for row in mapping_lines}
    result = {
        "source_revision": receipt["head"],
        "native_log_sha256": digest,
        "native_exit": receipt["exit_code"],
        "parser_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "status_or_candidate_rows": len(parsed),
        "unique_record_files_with_status_or_candidate_rows": len({row["record"] for row in parsed}),
        "distinct_record_and_label_pairs": len(
            {(row["record"], row["taxon_label"]) for row in parsed}
        ),
        "row_kinds": dict(Counter(row["kind"] for row in parsed)),
        "status_transitions": dict(sorted(transitions.items())),
        "native_status_or_candidate_rows": parsed,
        "native_uncurated_mismatches": mapping_lines,
        "phase2_scope_source": str(phase2_source.relative_to(ROOT)),
        "phase2_scope_source_sha256": hashlib.sha256(phase2_bytes).hexdigest(),
        "phase2_records": phase2_records,
        "phase2_records_in_either_failure": [
            path for path in phase2_records if Path(path).name in affected
        ],
        "limitation": "Mismatch rows can repeat one taxon in multiple record occurrences. Distinct record/label pairs are not distinct organisms or taxonomy occurrences, because one record can repeat a label. These are native reproducibility findings, not approved scientific changes or new issue ownership.",
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
