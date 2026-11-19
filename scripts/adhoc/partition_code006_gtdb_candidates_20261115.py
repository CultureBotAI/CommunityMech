"""Partition exact native GTDB discrepancies for reviewed work, #2848/#2854.

2026-11-15. Inputs: retained549-record comparison, unchanged native/table and
canonical bytes, maintained public review ledgers/tests. JSON stdout only;
no acquisition, candidate writes, application, automatic hold or approval.
"""

import argparse
import hashlib
import importlib.util
import json
import re
import subprocess
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/gtdb-code006-20261115"
MEASUREMENT = STATE / "indexing-corpus-001.json"
MEASUREMENT_SHA = "aecdbf62b49967d0ddf138c2cc3d9d8c018446000715b031856a4599b17bca2e"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--record", help="one-record read-only canary")
    args = parser.parse_args()
    raw = MEASUREMENT.read_bytes()
    if hashlib.sha256(raw).hexdigest() != MEASUREMENT_SHA:
        raise ValueError("exact reviewed native comparison required")
    measured = json.loads(raw)
    baseline = measured["source_revision"]
    occurrences = measured["discrepancies"]["native_cli"]
    if len(occurrences) != 419 or len({r["record"] for r in occurrences}) != 127:
        raise ValueError("exact native discrepancy denominator differs")
    if args.record:
        occurrences = [row for row in occurrences if row["record"] == args.record]
        if not occurrences:
            raise ValueError("canary must be one actually discrepant record")
    native_path = ROOT / "scripts/gtdb_ground.py"
    table = STATE / "kg-microbe/data/raw/NCBI2GTDB.tsv.gz"
    inputs = {
        MEASUREMENT: sha(MEASUREMENT),
        native_path: sha(native_path),
        table: sha(table),
        Path(__file__): sha(Path(__file__)),
    }
    for path in (native_path, table):
        if inputs[path] != measured["inputs"][str(path.relative_to(ROOT))]:
            raise ValueError("measured native/table input changed")
    documents = {}
    for row in occurrences:
        path = ROOT / row["record"]
        if path in inputs:
            continue
        inputs[path] = sha(path)
        if inputs[path] != measured["inputs"][row["record"]]:
            raise ValueError("selected canonical baseline changed")
        documents[row["record"]] = yaml.safe_load(path.read_bytes())
    spec = importlib.util.spec_from_file_location("partition_native_gtdb", native_path)
    native = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(native)
    wanted = [set(), set(), set()]
    for row in occurrences:
        clean = native._clean_label(row["label"])
        if native._is_species(clean):
            wanted[0].add(row["id"].removeprefix("NCBITaxon:"))
            wanted[1].update(native.lookup_keys(row["label"]))
        elif clean:
            wanted[2].update(native.lookup_keys(row["label"]))
    indexes = native.collect_rows(table, *wanted)
    selected = set(documents)
    tests = {path: path.read_text() for path in (ROOT / "tests").glob("*.py")}
    historical, review_inputs = {name: [] for name in selected}, {name: [] for name in selected}
    # pathlib enumeration includes ignored files on these declared maintained
    # review surfaces. Private scratch drafts are deliberately not approval input.
    for ledger in (ROOT / "reports/causal_graph_review/decisions").rglob("*.yaml"):
        content = ledger.read_text()
        if not any(name in content for name in selected):
            continue
        doc = yaml.safe_load(content)
        for item in doc.get("records", []) if isinstance(doc, dict) else []:
            name = item.get("path")
            if name not in selected or not item.get("record_sha256"):
                continue
            inputs[ledger] = sha(ledger)
            referencing = [
                str(path.relative_to(ROOT)) for path, text in tests.items() if ledger.name in text
            ]
            historical[name].append(
                {
                    "ledger": str(ledger.relative_to(ROOT)),
                    "record_sha256": item["record_sha256"],
                    "status": item.get("status"),
                    "tests_referencing_ledger": referencing,
                    "disposition": "Historical byte binding requires a reviewed strict successor proof before this record is admitted.",
                }
            )
            for test_name in referencing:
                path = ROOT / test_name
                inputs[path] = sha(path)
    for review in (ROOT / "reviews/structured").rglob("review.yaml"):
        content = review.read_text()
        if not any(name in content for name in selected):
            continue
        doc = yaml.safe_load(content)
        for item in doc.get("source", {}).get("inputs", []):
            name = item.get("path")
            if name in selected:
                inputs[review] = sha(review)
                review_inputs[name].append(
                    {
                        "review": str(review.relative_to(ROOT)),
                        "review_id": doc["review_id"],
                        "record_sha256": item["sha256"],
                        "scientific_review": doc.get("scientific_review"),
                        "verdict": doc["verdict"],
                        "disposition": "Inspect the existing taxonomy/source uncertainty and preserve all unchanged biological conclusions; this is not automatic scientific approval.",
                    }
                )
    rows = []
    for item in occurrences:
        record = documents[item["record"]]
        match = re.fullmatch(r"taxonomy\[(\d+)\]\.taxon_term", item["selector"])
        if not match:
            raise ValueError("exact taxonomy occurrence selector required")
        entry = record["taxonomy"][int(match.group(1))]
        block = entry["taxon_term"]
        if block["term"] != {"id": item["id"], "label": item["label"]}:
            raise ValueError("measured term identity differs")
        result = native.resolve_target(
            item["id"].removeprefix("NCBITaxon:"), item["label"], *indexes
        )
        manual = (
            Path(item["record"]).name,
            block.get("preferred_term"),
        ) in native.WITHHELD_GROUNDINGS
        curated = (Path(item["record"]).name, item["id"]) in native.CURATED_GROUNDINGS or bool(
            (block.get("gtdb_classification") or {}).get("curated")
        )
        if item["status"] == "NOT_ATTEMPTED":
            if not result or result.get("ambiguous") or not result.get("gtdb_id"):
                raise ValueError("native computability no longer reproduced")
            partition = (
                "higher_rank_correspondence"
                if not native._is_species(native._clean_label(item["label"]))
                else "species_or_strain_reference_correspondence"
            )
        elif item["status"] == "AMBIGUOUS":
            if (
                not result
                or not result.get("ambiguous")
                or sorted(result.get("gtdb_options") or []) != item["candidates"]
            ):
                raise ValueError("native ambiguity no longer reproduced")
            partition = "status_candidates_only_ambiguous"
        else:
            partition = "status_only_" + item["status"].lower()
        blockers = []
        if manual or curated:
            blockers.append("existing_native_manual_or_curated_guard")
        if historical[item["record"]]:
            blockers.append("historical_byte_binding_successor_required")
        if result and (result.get("is_reclassified") or result.get("majority_fraction", 1) < 0.55):
            blockers.append("name_change_or_near_tie_requires_individual_source_review")
        if item["record_id"] == "CommunityMech:000434":
            blockers.append("already_handled_by_separate_M5_canary_chain")
        rows.append(
            {
                **item,
                "partition": partition,
                "native_result": result,
                "existing_native_withheld": manual,
                "existing_native_curated": curated,
                "taxon_descriptor": block,
                "taxonomy_evidence": entry.get("evidence", []),
                "historical_byte_bindings": historical[item["record"]],
                "saved_review_inputs": review_inputs[item["record"]],
                "pre_application_blockers": blockers,
                "approval": "NOT_APPROVED: database correspondence/source scope must be reviewed before any native original-basename candidate or application.",
            }
        )
    if inputs != {path: sha(path) for path in inputs}:
        raise ValueError("inputs changed during partition")
    print(
        json.dumps(
            {
                "source_revision": baseline,
                "execution_revision": subprocess.check_output(
                    ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
                ).strip(),
                "measured_taxonomy_occurrences": 419,
                "measured_record_files": 127,
                "selected_occurrences": len(rows),
                "selected_records": len(documents),
                "partitions": dict(Counter(row["partition"] for row in rows)),
                "historically_bound_record_files": sum(
                    bool(value) for value in historical.values()
                ),
                "record_files_with_saved_reviews": sum(
                    bool(value) for value in review_inputs.values()
                ),
                "inputs": {str(path.relative_to(ROOT)): value for path, value in inputs.items()},
                "rows": rows,
                "inputs_unchanged": True,
                "limits": [
                    "Planning inventory only; no source-backed organism identity or scientific approval inferred from native computability.",
                    "Historical ledger bindings and tests referencing those ledgers are enumerated; exact successor admissibility still needs guard review.",
                    "Ignore-independent enumeration covers maintained public decision ledgers and structured reviews, not every private scratch artifact.",
                    "Each future native candidate must preserve its original basename and all curated/withheld and biological-scope constraints.",
                ],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
