"""Read one saved GTDB route against the pinned crosswalk, 2026-11-15, #2849.

Inputs: one canonical record/term label, native classifier, preserved SHA-pinned
NCBI2GTDB table. Output: JSON stdout only for #2849. No acquisition,
ontology initialization, record/cache changes, or inferred scientific approval.
"""

import argparse
import gzip
import hashlib
import importlib.util
import json
import subprocess
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
PIN = "6e3912d326ea59959f8987947a2f19eedf7cdcdb"
TABLE = ROOT / ".temp/gtdb-source-routes-2849-20261115/kg-microbe/data/raw/NCBI2GTDB.tsv.gz"
TABLE_SHA = "761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--record", required=True)
    parser.add_argument("--label", required=True)
    args = parser.parse_args()
    record = (ROOT / args.record).resolve()
    record.relative_to(ROOT)
    if git("rev-parse", "HEAD") != PIN or sha(TABLE) != TABLE_SHA:
        raise ValueError("exact frozen code/table required")
    source = ROOT / "scripts/gtdb_ground.py"
    inputs = {p: sha(p) for p in (record, source, Path(__file__), TABLE)}
    spec = importlib.util.spec_from_file_location("gtdb_ground", source)
    gtdb = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gtdb)
    doc = yaml.safe_load(record.read_bytes())
    found = [
        (i, entry["taxon_term"])
        for i, entry in enumerate(doc["taxonomy"])
        if entry.get("taxon_term", {}).get("term", {}).get("label") == args.label
    ]
    if len(found) != 1:
        raise ValueError("one exact taxon occurrence required")
    index, term = found[0]
    tid = term["term"]["id"]
    ncbi_id = tid.removeprefix("NCBITaxon:")
    keys = gtdb.lookup_keys(args.label)
    genus = gtdb._clean_label(args.label).split()[0]
    rows = gtdb.collect_rows(TABLE, {ncbi_id}, set(keys), {*keys, genus.lower()})
    native = gtdb.resolve_target(ncbi_id, args.label, *rows)
    genus_only = gtdb.resolve_target(None, genus, *rows)
    with gzip.open(TABLE, "rt") as handle:
        header = handle.readline().rstrip("\n").split("\t")

    def full_rows(values):
        return [dict(zip(header, row, strict=True)) for row in values]

    result = {
        "code_revision": PIN,
        "record": record.relative_to(ROOT).as_posix(),
        "record_id": doc["id"],
        "selector": f"taxonomy[{index}].taxon_term",
        "inputs": {str(p.relative_to(ROOT)): h for p, h in inputs.items()},
        "stored_taxon_descriptor": term,
        "native_lookup": {
            "ncbi_id": ncbi_id,
            "label": args.label,
            "species_heuristic": gtdb._is_species(gtdb._clean_label(args.label)),
            "name_keys": keys,
            "exact_id_rows": full_rows(rows[0].get(ncbi_id, [])),
            "exact_species_name_rows": {key: full_rows(rows[1].get(key, [])) for key in keys},
            "exact_higher_name_row_counts": {key: len(rows[2].get(key, [])) for key in keys},
            "result": native,
        },
        "separate_genus_diagnostic_not_native_strain_fallback": {
            "label": genus,
            "row_count": len(rows[2].get(genus.lower(), [])),
            "gtdb_genus_row_counts": dict(
                sorted(Counter(row[17] for row in rows[2].get(genus.lower(), [])).items())
            ),
            "result": genus_only,
        },
        "record_history_commits": git("log", "--format=%H %cs %s", "--", args.record).splitlines(),
        "limitation": "Crosswalk rows and native route are measured. Genus-only diagnostic is not a strain-level identity or an authorized fallback. No scientific status/block replacement is proposed by this output.",
    }
    if inputs != {p: sha(p) for p in inputs} or git("rev-parse", "HEAD") != PIN:
        raise ValueError("inputs changed during read-only probe")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
