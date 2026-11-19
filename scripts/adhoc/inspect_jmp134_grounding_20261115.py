"""Retain exact JMP134 source/lookup evidence for #2848, 2026-11-15.

Inputs: fixed canonical record, cached primary article, local NCBI identity
query, exact761 crosswalk and native resolver. JSON stdout only; no provider
calls, canonical writes, or full scientific-review claim.
"""

import gzip
import hashlib
import importlib.util
import json
import subprocess
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/gtdb-species-status-20261115"
TARGET = "data/isolates/Cupriavidus_Necator_JMP134_24DBP_Hydroxylase_Isolate_Baseline.yaml"
BASELINE = "429964cbf945c41b2e89b57a072718158cf674e03786ef34b1ef96fe9247995e"
TABLE = STATE / "kg-microbe/data/raw/NCBI2GTDB.tsv.gz"
TABLE_SHA = "761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd"
NATIVE = ROOT / "scripts/gtdb_ground.py"
NATIVE_SHA = "0fc1ba926a56e5be85cdf064db0cf56452aeeee93f15b0ced98e8f11b5296175"
CACHE = ROOT / "references_cache/PMID_42364169.txt"
CACHE_SHA = "76ae187fe615a75d522443b9deb085bc8499efb54df080407563f901c514a4d4"
QUERY = STATE / "jmp134-ncbi-001.json"


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def main():
    paths = [ROOT / TARGET, TABLE, NATIVE, CACHE, QUERY, Path(__file__)]
    paths.append(ROOT / "scripts/adhoc/query_jmp134_ncbi_identity_20261115.sql")
    captured = {path: path.read_bytes() for path in paths}
    for path, expected in (
        (ROOT / TARGET, BASELINE),
        (TABLE, TABLE_SHA),
        (NATIVE, NATIVE_SHA),
        (CACHE, CACHE_SHA),
    ):
        if digest(captured[path]) != expected:
            raise ValueError("pinned source changed: " + str(path.relative_to(ROOT)))
    record = yaml.safe_load(captured[ROOT / TARGET])
    descriptor = record["taxonomy"][0]["taxon_term"]
    identity = json.loads(captured[QUERY])
    if record["id"] != "CommunityMech:000555" or descriptor["term"] != {
        "id": "NCBITaxon:264198",
        "label": "Cupriavidus pinatubonensis JMP134",
    }:
        raise ValueError("exact stock identity required")
    labels = {row["value"] for row in identity if row["predicate"] == "rdfs:label"}
    synonyms = {row["value"] for row in identity if row["predicate"] == "oio:hasRelatedSynonym"}
    if (
        labels != {"Cupriavidus pinatubonensis JMP134"}
        or ("Cupriavidus necator JMP134" not in synonyms)
        or any(row["subject"] != "NCBITaxon:264198" for row in identity)
    ):
        raise ValueError("retained NCBI query does not establish the name connection")
    spec = importlib.util.spec_from_file_location("jmp134_native", NATIVE)
    native = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(native)
    rows = native.collect_rows(TABLE, {"264198"}, set(), set())
    result = native.resolve_target("264198", descriptor["term"]["label"], *rows)
    if result != {
        "ncbi_source_id": "NCBITaxon:264198",
        "gtdb_id": "GTDB:s__Cupriavidus_pinatubonensis",
        "gtdb_taxon": "Cupriavidus pinatubonensis",
        "gtdb_lineage": "d__Bacteria;p__Pseudomonadota;c__Gammaproteobacteria;o__Burkholderiales;f__Burkholderiaceae;g__Cupriavidus;s__Cupriavidus pinatubonensis",
        "majority_fraction": 1.0,
        "total_genomes": 1,
        "is_reclassified": False,
        "via": "ncbi_id",
    }:
        raise ValueError("fresh exact-ID native correspondence differs")
    lines = gzip.decompress(captured[TABLE]).decode().splitlines()
    header = lines[0].split("\t")
    exact_rows = []
    for number, line in enumerate(lines[1:], 2):
        cells = line.split("\t")
        if cells[native.COL_NCBI_ID] == "264198":
            exact_rows.append({"line": number, "cells": dict(zip(header, cells, strict=True))})
    if len(exact_rows) != 1:
        raise ValueError("exact one-row population required")
    text = captured[CACHE].decode()
    for identity_token in ("PMID: 42364169", "PMC13440307", "10.1093/ismejo/wrag163"):
        if identity_token not in text:
            raise ValueError("primary cache identity differs")
    # Keep the public quote narrow. Offset/context is retained privately by the
    # caller; this observation is not a renewed review of enzyme/flux claims.
    phrases = [
        "C. necator JMP134 is a well-characterized bacterial strain",
        "R. wittichii YL-JM2C and C. necator JMP134 were grown separately in R2A",
    ]
    contexts = []
    for phrase in phrases:
        start = text.find(phrase)
        if start < 0:
            raise ValueError("expected source identity passage is absent")
        contexts.append(
            {
                "anchor": phrase,
                "character_offset": start,
                "line": text.count("\n", 0, start) + 1,
                "context": text[max(0, start - 100) : start + 600],
            }
        )
    if any(path.read_bytes() != raw for path, raw in captured.items()):
        raise ValueError("source changed during inspection")
    print(
        json.dumps(
            {
                "revision": subprocess.check_output(
                    ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
                ).strip(),
                "record": TARGET,
                "record_id": record["id"],
                "selector": "taxonomy[0].taxon_term",
                "inputs": {
                    str(path.relative_to(ROOT)): digest(raw) for path, raw in captured.items()
                },
                "primary_reference": "PMID:42364169",
                "primary_contexts": contexts,
                "ncbi_identity_rows": identity,
                "ncbi_query_limitation": "Readonly local adapter query retained; the whole SQLite database and its release were not hash-certified by this source inspection.",
                "crosswalk_exact_rows": exact_rows,
                "native_result": result,
                "population_scope": "One genome under exact NCBITaxon264198 in pinned crosswalk. No additional genomes or species-wide population inferred.",
                "name_scope": "The paper name is a retained NCBI synonym of the exact JMP134 strain. Native is_reclassified:false compares the cleaned canonical binomial with GTDB; it does not assert a formal nomenclatural event or equate every C.necator stock with C.pinatubonensis.",
                "preserved_scientific_limit": record["discussions"][0]["rationale"],
                "inputs_unchanged": True,
                "canonical_writes": False,
                "scientific_review": False,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
