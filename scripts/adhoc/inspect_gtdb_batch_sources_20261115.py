"""Inspect bounded GTDB correspondence source configurations, #2848, 2026-11-15.

Inputs: a hash-pinned max-ten-record config, current records/primary caches,
existing local NCBI SQLite and pinned crosswalk/native resolver. JSON stdout;
no acquisition, canonical writes, or full scientific-review claim. Contexts
belong in private caller-owned output, not public source-body exports.
"""

import argparse
import gzip
import hashlib
import importlib.util
import json
import sqlite3
import subprocess
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
NATIVE = "scripts/gtdb_ground.py"
NATIVE_SHA = "0fc1ba926a56e5be85cdf064db0cf56452aeeee93f15b0ced98e8f11b5296175"
TABLE_SHA = "761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd"


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def local_path(name):
    path = Path(name)
    resolved = (ROOT / path).resolve()
    if path.is_absolute() or ".." in path.parts or not resolved.is_relative_to(ROOT):
        raise ValueError("repository-relative input required")
    if (ROOT / path).is_symlink():
        raise ValueError("input symlink not permitted")
    return ROOT / path


def native_module():
    spec = importlib.util.spec_from_file_location("bounded_species_native", ROOT / NATIVE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def query_identity(connection, identifier):
    return [
        dict(row)
        for row in connection.execute(
            "SELECT subject,predicate,value,object FROM statements WHERE subject=? "
            "AND (predicate='rdfs:label' OR predicate LIKE '%Synonym%' "
            "OR predicate LIKE '%rank%' OR predicate='rdfs:subClassOf') "
            "ORDER BY predicate,value,object",
            (identifier,),
        )
    ]


def inspect(config_path, expected_config_sha, expected_revision):
    captured = {}

    def read(name, expected=None):
        path = local_path(name)
        if path not in captured:
            captured[path] = path.read_bytes()
        raw = captured[path]
        if expected is not None and sha(raw) != expected:
            raise ValueError("pinned source changed: " + name)
        return raw

    head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    if head != expected_revision:
        raise ValueError("exact source revision required")
    config = json.loads(read(config_path, expected_config_sha))
    selected = config["records"]
    if not 1 <= len(selected) <= 10 or len({row["record"] for row in selected}) != len(selected):
        raise ValueError("one to ten unique whole records required")
    read(str(Path(__file__).relative_to(ROOT)))
    read(NATIVE, NATIVE_SHA)
    table = local_path(config["crosswalk"])
    table_raw = read(config["crosswalk"], TABLE_SHA)
    for name, expected in config["additional_inputs"].items():
        read(name, expected)
    native = native_module()
    ids = {
        occurrence["term"]["id"].split(":", 1)[1]
        for row in selected
        for occurrence in row["occurrences"]
    }
    names = {
        name
        for row in selected
        for occurrence in row["occurrences"]
        for name in native.lookup_keys(occurrence["term"]["label"])
    }
    rows = native.collect_rows(table, ids, names, set())
    lines = gzip.decompress(table_raw).decode().splitlines()
    header = lines[0].split("\t")
    mapping_rows = [
        {"line": number, "cells": dict(zip(header, line.split("\t"), strict=True))}
        for number, line in enumerate(lines[1:], 2)
        if line.split("\t")[native.COL_NCBI_ID] in ids
        or line.split("\t")[native.COL_NCBI_SPECIES].strip().lower() in names
    ]
    database = Path.home() / ".data/oaklib/ncbitaxon.db"
    before_stat = database.stat()
    result = []
    with sqlite3.connect(database.as_uri() + "?mode=ro", uri=True) as connection:
        connection.row_factory = sqlite3.Row
        for selected_record in selected:
            record_path = selected_record["record"]
            raw = read(record_path, selected_record["before_sha256"])
            record = yaml.safe_load(raw)
            if record["id"] != selected_record["record_id"]:
                raise ValueError("record identity differs")
            if len({item["taxonomy_index"] for item in selected_record["occurrences"]}) != len(
                selected_record["occurrences"]
            ):
                raise ValueError("duplicate occurrence")
            contexts = []
            for source in selected_record["primary_sources"]:
                text = read(source["path"], source["sha256"]).decode()
                if any(token not in text for token in source["identity_tokens"]):
                    raise ValueError("cached primary identity differs")
                for anchor in source["anchors"]:
                    start = text.find(anchor)
                    if start < 0:
                        raise ValueError("source anchor absent")
                    contexts.append(
                        {
                            "reference": source["reference"],
                            "path": source["path"],
                            "anchor": anchor,
                            "character_offset": start,
                            "line": text.count("\n", 0, start) + 1,
                            "context": text[max(0, start - 100) : start + len(anchor) + 600],
                        }
                    )
            occurrences = []
            for occurrence in selected_record["occurrences"]:
                index = occurrence["taxonomy_index"]
                member = record["taxonomy"][index]
                descriptor = member["taxon_term"]
                if (
                    descriptor["term"] != occurrence["term"]
                    or member.get("strain_designation", {}).get("strain_name")
                    != occurrence["strain_name"]
                ):
                    raise ValueError("source stock descriptor differs")
                identifier = occurrence["term"]["id"]
                identity = query_identity(connection, identifier)
                labels = {row["value"] for row in identity if row["predicate"] == "rdfs:label"}
                ranks = {row["object"] for row in identity if row["predicate"].endswith("rank")}
                if labels != {occurrence["term"]["label"]} or ranks != {
                    occurrence["expected_ncbi_rank"]
                }:
                    raise ValueError("local authority label/rank differs")
                resolved = native.resolve_target(
                    identifier.split(":", 1)[1], occurrence["term"]["label"], *rows
                )
                if resolved != occurrence["expected_native_result"]:
                    raise ValueError(
                        "fresh native correspondence differs from reviewed expectation"
                    )
                exact = [
                    row
                    for row in mapping_rows
                    if row["cells"]["taxonID NCBI"] == identifier.split(":", 1)[1]
                ]
                if resolved["via"] == "ncbi_id" and not exact:
                    raise ValueError("exact ID route lacks source rows")
                occurrences.append(
                    {
                        **occurrence,
                        "native_result": resolved,
                        "ncbi_identity_rows": identity,
                        "crosswalk_exact_rows": exact,
                        "existing_descriptor": descriptor,
                    }
                )
            result.append(
                {
                    "record": record_path,
                    "record_id": record["id"],
                    "before_sha256": sha(raw),
                    "occurrences": occurrences,
                    "primary_contexts": contexts,
                    "preserved_discussions": record.get("discussions", []),
                    "historical_guard_assessment": selected_record["historical_guard_assessment"],
                }
            )
    after_stat = database.stat()
    if (before_stat.st_size, before_stat.st_mtime_ns) != (
        after_stat.st_size,
        after_stat.st_mtime_ns,
    ):
        raise ValueError("local authority database changed")
    if any(path.read_bytes() != raw for path, raw in captured.items()):
        raise ValueError("source input changed during inspection")
    if subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip() != head:
        raise ValueError("source revision changed")
    return {
        "revision": head,
        "records": result,
        "inputs": {str(path.relative_to(ROOT)): sha(raw) for path, raw in captured.items()},
        "crosswalk_candidate_rows": mapping_rows,
        "database_observation": {
            "size": before_stat.st_size,
            "mtime_ns": before_stat.st_mtime_ns,
            "unchanged": True,
            "limitation": "Readonly local authority query; whole database hash/release not certified.",
        },
        "inputs_unchanged": True,
        "canonical_writes": False,
        "scientific_review": False,
        "scope": "Source identity and native reference correspondence only; stock membership in the crosswalk and biological mechanisms are not inferred.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True)
    parser.add_argument("--expected-config-sha256", required=True)
    parser.add_argument("--expected-revision", required=True)
    args = parser.parse_args()
    print(
        json.dumps(
            inspect(args.config, args.expected_config_sha256, args.expected_revision), indent=2
        )
    )
