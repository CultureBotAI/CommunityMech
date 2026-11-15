"""Plan two source-supported genus correspondences, #2848, 2026-11-15.

Inputs: immutable native partition, unchanged selected records/table/primary
cache and historical reviews. Output: private metadata JSON on stdout only.
No network, canonical/candidate writes, automatic approval or scientific review.
"""

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/gtdb-code006-20261115"
PARTITION = STATE / "partition-corpus-001.json"
PARTITION_SHA = "261f9193a9d1ad5ceefc05178b512f3b52d1fa6a23c325e5312905d06a32cf15"
HISTORICAL_REVISION = "68699871"
SELECTED = {"CommunityMech:000552": 16, "CommunityMech:000553": 46}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--record", choices=sorted(SELECTED), action="append")
    args = parser.parse_args()
    requested = args.record or list(SELECTED)
    if len(set(requested)) != len(requested):
        raise ValueError("unique selected records required")
    partition_bytes = PARTITION.read_bytes()
    if digest(partition_bytes) != PARTITION_SHA:
        raise ValueError("exact historical native partition required")
    partition = json.loads(partition_bytes)
    inputs = {str(PARTITION.relative_to(ROOT)): PARTITION_SHA}

    def retained(path, expected=None):
        name = str(path.relative_to(ROOT))
        raw = path.read_bytes()
        actual = digest(raw)
        if expected is not None and actual != expected:
            raise ValueError(f"selected input changed: {name}")
        if name in inputs and inputs[name] != actual:
            raise ValueError(f"selected input changed during planning: {name}")
        inputs[name] = actual
        return raw

    retained(Path(__file__))
    source = ROOT / "references_cache/PMID_42666409.txt"
    source_bytes = retained(
        source, "3442799f20b033c3a010c14a4f32c4be15485fb0a501aed059921a5006cbe698"
    )
    source_text = re.sub(r"\s+", " ", source_bytes.decode()).strip()
    test = ROOT / "tests/test_causal_review_batch147.py"
    retained(test)
    for name in (
        "scripts/gtdb_ground.py",
        ".temp/gtdb-code006-20261115/kg-microbe/data/raw/NCBI2GTDB.tsv.gz",
    ):
        retained(ROOT / name, partition["inputs"][name])
    historical = subprocess.check_output(
        ["git", "rev-parse", HISTORICAL_REVISION], cwd=ROOT, text=True
    ).strip()
    rows = []
    for record_id in requested:
        matches = [row for row in partition["rows"] if row["record_id"] == record_id]
        if len(matches) != 1:
            raise ValueError("one exact taxonomy occurrence per selected isolate required")
        row = matches[0]
        path = ROOT / row["record"]
        raw = retained(path, partition["inputs"][row["record"]])
        original = subprocess.check_output(
            ["git", "show", f"{historical}:{row['record']}"], cwd=ROOT
        )
        if original != raw:
            raise ValueError("historical full-record bytes do not match current baseline")
        doc = yaml.safe_load(raw)
        taxon = doc["taxonomy"][0]
        if (
            doc["id"] != record_id
            or len(doc["taxonomy"]) != 1
            or taxon["taxon_term"] != row["taxon_descriptor"]
        ):
            raise ValueError("selected occurrence identity differs")
        result = row["native_result"]
        label = taxon["taxon_term"]["term"]["label"]
        if (
            row["existing_native_curated"]
            or row["existing_native_withheld"]
            or row["partition"] != "higher_rank_correspondence"
            or result["gtdb_id"] != "GTDB:g__" + label
            or result["is_reclassified"] is not False
            or result["majority_fraction"] != 1.0
            or result["total_genomes"] != SELECTED[record_id]
            or result["support_genomes"] != SELECTED[record_id]
            or taxon["taxon_term"]["gtdb_grounding_status"] != "UNRESOLVED"
            or "gtdb_classification" in taxon["taxon_term"]
        ):
            raise ValueError("exact unambiguous same-genus correspondence required")
        evidence = taxon["evidence"]
        if len(evidence) != 1 or evidence[0]["reference"] != "PMID:42666409":
            raise ValueError("exact primary genus evidence required")
        if re.sub(r"\s+", " ", evidence[0]["snippet"]).strip() not in source_text:
            raise ValueError("existing genus quote not present in retained primary cache")
        for binding in row["historical_byte_bindings"]:
            retained(ROOT / binding["ledger"], partition["inputs"][binding["ledger"]])
        for binding in row["saved_review_inputs"]:
            retained(ROOT / binding["review"], partition["inputs"][binding["review"]])
        rows.append(
            {
                "record_id": record_id,
                "record": row["record"],
                "selector": row["selector"],
                "baseline_sha256": digest(raw),
                "native_result": result,
                "primary_source": {
                    "path": str(source.relative_to(ROOT)),
                    "locator": "Section3.1 genus assignments; retained cache line57",
                    "existing_taxonomy_evidence_matches": True,
                },
                "historical_byte_bindings": row["historical_byte_bindings"],
                "saved_review_inputs": row["saved_review_inputs"],
                "actual_historical_guard": "tests/test_causal_review_batch147.py::test_batch147_ledger_matches_curated_records",
                "compatibility": "The older UNRESOLVED status describes the earlier database result. A same-genus reference correspondence does not assign this study strain to a GTDB species or genome. Existing strain/genome notes, biological claims, graphs, evidence and historical assessments must remain unchanged.",
                "required_before_application": [
                    "Reviewed original-basename native candidate and exact source block",
                    "Strict successor guard retaining historical full bytes and all biological fields, allowing only this mapping/status and native appended events",
                    "Exact external candidate and receipt hashes; source and canonical rechecks before and after native validation",
                    "One actual same-path canary with native sidecar, scoped gates, completion tests and saved technical assessment before second record",
                ],
            }
        )
    if inputs != {name: digest((ROOT / name).read_bytes()) for name in inputs}:
        raise ValueError("input changed during planning")
    print(
        json.dumps(
            {
                "source_revision": partition["source_revision"],
                "execution_revision": subprocess.check_output(
                    ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
                ).strip(),
                "historical_blob_revision": historical,
                "canonical_apply": False,
                "scientific_review": False,
                "approval": "PLAN_ONLY: parent candidate and successor guard review required before application",
                "selected_records": len(rows),
                "rows": rows,
                "inputs": inputs,
                "inputs_unchanged": True,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
