"""Reproduce one record's mapping votes without mutation, 2026-11-14.

Inputs: one canonical record and an explicit local NCBI2GTDB crosswalk.
Outputs: a hash-bound JSON comparison in ignored completion working evidence.
Serves #2674/#2709/#2774; numerical coherence does not prove ecological function
or GTDB release/build provenance. Uses the native aggregate/named-row method.
"""

import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import gtdb_ground as native  # noqa: E402


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", type=Path, required=True)
    parser.add_argument("--mapping", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise ValueError("refusing to replace a mapping receipt")
    record = yaml.safe_load(args.record.read_text())
    targets = list(native.community_taxa(args.record))
    ids, species, higher = set(), set(), set()
    for nid, label in targets:
        if native._is_species(native._clean_label(label)):
            if nid:
                ids.add(nid)
            species.update(native.lookup_keys(label))
        else:
            higher.update(native.lookup_keys(label))
    indexed = native.collect_rows(args.mapping, ids, species, higher)
    rows = []
    for index, (nid, label) in enumerate(targets):
        grounding = native.resolve_target(
            nid, label, *indexed, denominator="aggregate", exclude_unnamed=True
        )
        stored = record["taxonomy"][index]["taxon_term"].get("gtdb_classification")
        row = {
            "selector": f"taxonomy[{index}].taxon_term",
            "ncbi_id": nid,
            "label": label,
            "native_grounding": grounding,
            "stored_grounding": stored,
        }
        fields = (
            "gtdb_id",
            "gtdb_lineage",
            "support_genomes",
            "total_genomes",
            "majority_fraction",
        )
        row["numeric_core_matches_native"] = bool(
            stored and grounding and all(stored.get(key) == grounding.get(key) for key in fields)
        )
        if nid == "651137":
            selected = native.named_species_only(indexed[2]["nitrososphaerota"])
            counts = Counter()
            members = Counter()
            for item in selected:
                counts[item[14]] += native._genomes(item)
                members[item[14]] += 1
            row["curated_class_votes"] = dict(counts)
            row["curated_class_row_counts"] = dict(members)
            row["curated_core_reproduced"] = (
                counts["Nitrososphaeria"] == stored["support_genomes"]
                and sum(counts.values()) == stored["total_genomes"]
                and round(counts["Nitrososphaeria"] / sum(counts.values()), 3)
                == stored["majority_fraction"]
            )
        rows.append(row)
    result = {
        "record_id": record["id"],
        "record_sha256": hashlib.sha256(args.record.read_bytes()).hexdigest(),
        "mapping_filename": args.mapping.name,
        "mapping_sha256": hashlib.sha256(args.mapping.read_bytes()).hexdigest(),
        "native_script_sha256": hashlib.sha256(
            (ROOT / "scripts/gtdb_ground.py").read_bytes()
        ).hexdigest(),
        "method": "native aggregate denominator; exclude unnamed rows; no ecological function inference and no release assertion",
        "rows": rows,
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(args.output)


if __name__ == "__main__":
    main()
