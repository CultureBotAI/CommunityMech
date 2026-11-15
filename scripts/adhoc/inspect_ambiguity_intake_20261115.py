"""Inspect the assigned whole-record #2848 intake, 2026-11-15.

Inputs: frozen historical residual partition, current YAML, native manual holds,
and candidate historical guards. JSON stdout only; no writes, acquisition,
classifier recomputation, scientific assessment, or correction approval.
"""

import argparse
import hashlib
import importlib.util
import json
import re
import subprocess
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / ".temp/gtdb-ambiguity-20261115/residual-groups-001.json"
SOURCE_SHA = "eaf78e16c342e36a0aa82c52c45888e8efb667fc2b70aa8d77ead956024f5f7c"
GROUPS = {
    "ambiguous": 15,
    "unsupported_or_scope_status": 1,
    "ambiguous+same_name_species_or_strain": 7,
    "ambiguous+renamed_mapping": 7,
}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", help="optional exact CommunityMech identifier")
    args = parser.parse_args()
    captured = {SOURCE: SOURCE.read_bytes(), Path(__file__): Path(__file__).read_bytes()}
    if sha(captured[SOURCE]) != SOURCE_SHA:
        raise ValueError("exact historical assignment source required")
    inventory = json.loads(captured[SOURCE])
    native_path = ROOT / "scripts/gtdb_ground.py"
    captured[native_path] = native_path.read_bytes()
    spec = importlib.util.spec_from_file_location("native_intake_holds", native_path)
    native = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(native)
    records, seen = [], set()
    for group, count in GROUPS.items():
        if len(inventory["groups"][group]) != count:
            raise ValueError("assigned group changed")
        for row in inventory["groups"][group]:
            if args.record and row["record_id"] != args.record:
                continue
            path = ROOT / row["record"]
            path.resolve().relative_to(ROOT)
            captured[path] = path.read_bytes()
            if sha(captured[path]) != row["baseline_sha256"]:
                raise ValueError("record changed since frozen residual intake")
            doc = yaml.safe_load(captured[path])
            if doc["id"] != row["record_id"] or doc["id"] in seen:
                raise ValueError("identity collision")
            seen.add(doc["id"])
            occurrences = []
            for occurrence in row["occurrences"]:
                match = re.fullmatch(r"taxonomy\[(\d+)\]\.taxon_term", occurrence["selector"])
                if not match:
                    raise ValueError("unexpected selector")
                entry = doc["taxonomy"][int(match[1])]
                term = entry["taxon_term"]
                if term["term"] != {"id": occurrence["id"], "label": occurrence["label"]}:
                    raise ValueError("stored descriptor no longer matches intake")
                occurrences.append(
                    {
                        **occurrence,
                        "stored_taxon_term": term,
                        "strain_designation": entry.get("strain_designation"),
                        "evidence": entry.get("evidence", []),
                        "manual_withheld_reason": native.WITHHELD_GROUNDINGS.get(
                            (path.name, term.get("preferred_term"))
                        ),
                        "manual_curated_reason": native.CURATED_GROUNDINGS.get(
                            (path.name, term["term"]["id"])
                        ),
                        "curated_block": bool(term.get("gtdb_classification", {}).get("curated")),
                    }
                )
            guards = row["candidate_historical_guard_files"] + row["historical_ledgers"]
            for relative in guards:
                guard = ROOT / relative
                guard.resolve().relative_to(ROOT)
                captured[guard] = guard.read_bytes()
            records.append(
                {
                    "record_id": doc["id"],
                    "record": row["record"],
                    "sha256": sha(captured[path]),
                    "name": doc["name"],
                    "description": doc.get("description"),
                    "group": group,
                    "occurrences": occurrences,
                    "candidate_guard_paths": guards,
                    "graph_nodes": len(doc.get("ecological_interactions", [])),
                    "prior_discussions": doc.get("discussions", []),
                    "scope": "Metadata intake only. Native results are the retained historical partition, not newly recomputed. Guard behavior and primary scientific evidence require per-record inspection before application.",
                }
            )
    if len(records) != (1 if args.record else 30):
        raise ValueError("incomplete or unexpected assigned population")
    if any(path.read_bytes() != raw for path, raw in captured.items()):
        raise ValueError("intake inputs changed")
    print(
        json.dumps(
            {
                "kind": "READ_ONLY_INTAKE",
                "execution_revision": subprocess.check_output(
                    ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
                ).strip(),
                "scientific_review": False,
                "records": records,
                "input_sha256": {
                    str(path.relative_to(ROOT)): sha(raw) for path, raw in captured.items()
                },
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
