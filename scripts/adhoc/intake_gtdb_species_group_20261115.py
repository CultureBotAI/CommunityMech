"""Capture the 29-record species/strain source and guard intake, #2848, 2026-11-15.

Inputs: fixed residual/historical manifests, current records, cached sources,
historical reviews and guard code. JSON stdout only; no native batch, writes or
scientific approval. --record selects one complete record for the intake canary.
"""

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/gtdb-species-status-20261115"
RESIDUAL = STATE / "residual-groups-001.json"
PARTITION = STATE / "partition-corpus-001.json"
PINS = {
    RESIDUAL: "eaf78e16c342e36a0aa82c52c45888e8efb667fc2b70aa8d77ead956024f5f7c",
    PARTITION: "261f9193a9d1ad5ceefc05178b512f3b52d1fa6a23c325e5312905d06a32cf15",
    ROOT
    / "scripts/gtdb_ground.py": "0fc1ba926a56e5be85cdf064db0cf56452aeeee93f15b0ced98e8f11b5296175",
}
GROUP = "same_name_species_or_strain"


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def walk_refs(value):
    if isinstance(value, dict):
        for key, child in value.items():
            if key in {"reference", "reference_id", "resource_id"} and isinstance(child, str):
                if re.match(r"(?i)^(PMID:|doi:|PMC)", child):
                    yield child
            yield from walk_refs(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_refs(child)


def selected_node(document, selector):
    node = document
    for name, index in re.findall(r"([A-Za-z_]+)(?:\[([0-9]+)\])?", selector):
        node = node[name]
        if index:
            node = node[int(index)]
    return node


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--record", help="One exact CommunityMech ID, otherwise the fixed 29-record group"
    )
    args = parser.parse_args()
    captured = {}

    def read(path, expected=None):
        path = path.resolve()
        if not path.is_relative_to(ROOT):
            raise ValueError("input outside this isolated repository")
        if path not in captured:
            captured[path] = path.read_bytes()
        raw = captured[path]
        if expected is not None and sha(raw) != expected:
            raise ValueError("pinned input changed: " + str(path.relative_to(ROOT)))
        return raw

    for path, digest in PINS.items():
        read(path, digest)
    read(Path(__file__))
    groups = json.loads(captured[RESIDUAL])
    historical = json.loads(captured[PARTITION])
    selected = groups["groups"][GROUP]
    if len(selected) != 29 or len({row["record"] for row in selected}) != 29:
        raise ValueError("exact whole-record planning group required")
    if args.record:
        selected = [row for row in selected if row["record_id"] == args.record]
        if len(selected) != 1:
            raise ValueError("one exact selected whole record required")
    # rglob includes ignored files: these are bounded cache-directory candidates,
    # not a claim about whether any paper exists globally.
    cache_paths = [path for path in (ROOT / "references_cache").rglob("*") if path.is_file()]
    results = []
    for row in selected:
        record = row["record"]
        raw = read(ROOT / record, row["baseline_sha256"])
        document = yaml.safe_load(raw)
        if document["id"] != row["record_id"]:
            raise ValueError("record identity differs")
        prior_rows = [item for item in historical["rows"] if item["record"] == record]
        if {item["selector"] for item in prior_rows} != {
            item["selector"] for item in row["occurrences"]
        }:
            raise ValueError("selected group splits a record's historical occurrences")
        occurrences = []
        reviews = {}
        for occurrence in row["occurrences"]:
            prior = next(item for item in prior_rows if item["selector"] == occurrence["selector"])
            descriptor = selected_node(document, occurrence["selector"])
            if (
                descriptor != prior["taxon_descriptor"]
                or occurrence["native_result"] != prior["native_result"]
            ):
                raise ValueError("descriptor or historical native result changed")
            taxonomy_match = re.fullmatch(
                r"taxonomy\[([0-9]+)\]\.taxon_term", occurrence["selector"]
            )
            member = document["taxonomy"][int(taxonomy_match[1])] if taxonomy_match else {}
            occurrences.append(
                {
                    **occurrence,
                    "current_descriptor": descriptor,
                    "strain_designation": member.get("strain_designation"),
                    "existing_taxonomy_evidence": member.get("evidence", []),
                    "historical_stored_status": prior["stored_status"],
                    "historical_computed_status": prior["status"],
                    "existing_native_curated": prior["existing_native_curated"],
                    "existing_native_withheld": prior["existing_native_withheld"],
                    "native_result_is_historical_not_rerun": True,
                }
            )
            for binding in prior["saved_review_inputs"]:
                name = binding["review"]
                saved = yaml.safe_load(read(ROOT / name))
                target_inputs = [
                    item for item in saved["source"]["inputs"] if item["path"] == record
                ]
                reviews[name] = {
                    "review_id": saved["review_id"],
                    "scientific_review": saved["scientific_review"],
                    "completion": saved["completion"],
                    "verdict": saved["verdict"],
                    "record_input_bindings": target_inputs,
                    "findings_for_target": [
                        finding
                        for finding in saved.get("findings", [])
                        if row["record_id"] in finding.get("target_ids", [])
                    ],
                    "limitations": saved.get("limitations", []),
                }
        ledgers = {}
        for name in row["historical_ledgers"]:
            ledger = yaml.safe_load(read(ROOT / name))
            ledgers[name] = [
                entry
                for entry in ledger.get("records", [])
                if entry.get("id") == row["record_id"] or entry.get("path") == record
            ]
        guards = {}
        for name in row["candidate_historical_guard_files"]:
            code = read(ROOT / name).decode()
            guards[name] = {
                "sha256": sha(captured[ROOT / name]),
                "source_lines_to_inspect": [
                    {"line": number, "text": line.strip()}
                    for number, line in enumerate(code.splitlines(), 1)
                    if any(
                        token in line
                        for token in (
                            "digest",
                            "record_sha256",
                            "historical_bytes",
                            "current_record_sha256",
                            row["record_id"],
                            Path(record).name,
                        )
                    )
                ],
                "actual_guard_semantics": "MANUAL_INSPECTION_REQUIRED; text matches do not establish guard scope",
            }
        refs = sorted(set(walk_refs(document)))
        caches = {}
        for reference in refs:
            stem = re.sub(r"[^A-Za-z0-9._-]", "_", reference).casefold()
            matches = [path for path in cache_paths if path.name.casefold().startswith(stem + ".")]
            caches[reference] = [
                {
                    "path": str(path.relative_to(ROOT)),
                    "sha256": sha(read(path)),
                    "bytes": len(captured[path]),
                    "scope": "Cached bytes available for source inspection; identity/completeness not certified by this intake.",
                }
                for path in sorted(matches)
            ]
        results.append(
            {
                "record": record,
                "record_id": row["record_id"],
                "record_sha256": sha(raw),
                "name": document.get("name"),
                "description": document.get("description"),
                "occurrences": occurrences,
                "references": caches,
                "historical_ledgers": ledgers,
                "saved_reviews": reviews,
                "candidate_guards": guards,
                "current_discussions": document.get("discussions", []),
                "manual_source_and_guard_triage": "PENDING; this is an input inventory, not an assessment or application approval",
            }
        )
    if any(path.read_bytes() != raw for path, raw in captured.items()):
        raise ValueError("intake input changed")
    print(
        json.dumps(
            {
                "revision": subprocess.check_output(
                    ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
                ).strip(),
                "group": GROUP,
                "group_population": 29,
                "selected_records": len(results),
                "selected_occurrences": sum(len(row["occurrences"]) for row in results),
                "native_execution": False,
                "canonical_writes": False,
                "scientific_review": False,
                "inputs": {
                    str(path.relative_to(ROOT)): sha(raw) for path, raw in sorted(captured.items())
                },
                "records": results,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
