"""Verify source roster ranks against native NCBI ontology for #1548, 2026-11-15.

Inputs: exact publisher Table S1, read-only NCBI database and optional crosswalk.
Output: JSON on stdout. Genus/family identity never establishes a study-stock
species or genome accession. Optional one-stock mode is the same-path canary.
"""

import argparse
import hashlib
import json
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import gtdb_ground as native  # noqa: E402


def sha(path):
    result = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(4 * 1024 * 1024), b""):
            result.update(chunk)
    return result.hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--table", type=Path, required=True)
    parser.add_argument("--ncbi", type=Path, required=True)
    parser.add_argument("--only-strain")
    parser.add_argument("--fingerprint", action="store_true")
    parser.add_argument("--mapping", type=Path)
    args = parser.parse_args()
    before = args.ncbi.stat()
    workbook = openpyxl.load_workbook(args.table, data_only=True, read_only=True)
    source_rows = list(workbook["Table S1"].iter_rows(min_row=3, max_row=17, values_only=True))
    if len(source_rows) != 15 or len({row[0] for row in source_rows}) != 15:
        raise ValueError("unexpected Table S1 roster")
    roster = []
    with sqlite3.connect(args.ncbi.resolve().as_uri() + "?mode=ro", uri=True) as connection:
        connection.execute("PRAGMA query_only=ON")
        for row_index, row in enumerate(source_rows, 3):
            source_name = row[0]
            genus, stock = source_name.split(" sp. ")
            if args.only_strain and stock != args.only_strain:
                continue
            # NCBI disambiguates the bacterial Bacillus from the insect genus.
            label = {
                "MA-N2": "Micrococcaceae",
                "Bacillus": "Bacillus <firmicutes>",
                "Bosea": "Allobosea",
            }.get(genus, genus)
            expected_rank = "family" if genus == "MA-N2" else "genus"
            if genus == "MA-N2" and "Micrococcaceae" not in row[8]:
                raise ValueError("family grounding is not supported by source SILVA cell")
            labels = connection.execute(
                "SELECT DISTINCT subject FROM statements WHERE predicate='rdfs:label' AND value=?",
                (label,),
            ).fetchall()
            candidates = []
            for (identifier,) in labels:
                ranks = connection.execute(
                    "SELECT object FROM statements WHERE subject=? AND predicate LIKE '%has_rank'",
                    (identifier,),
                ).fetchall()
                if ("NCBITaxon:" + expected_rank,) in ranks:
                    candidates.append(identifier)
            if len(candidates) != 1:
                raise ValueError(f"expected one verified {expected_rank} for {label}: {candidates}")
            identifier = candidates[0]
            taxonomy = connection.execute(
                "SELECT predicate, value, object FROM statements WHERE subject=? "
                "AND (predicate='rdfs:label' OR predicate LIKE '%Synonym%' OR predicate LIKE '%has_rank' OR predicate='rdfs:subClassOf') "
                "ORDER BY predicate,value,object",
                (identifier,),
            ).fetchall()
            domain_ancestors = connection.execute(
                "WITH RECURSIVE parents(id) AS (SELECT ? UNION "
                "SELECT object FROM statements JOIN parents ON subject=parents.id "
                "WHERE predicate='rdfs:subClassOf') SELECT id FROM parents "
                "WHERE id IN ('NCBITaxon:2','NCBITaxon:2157','NCBITaxon:2759') ORDER BY id",
                (identifier,),
            ).fetchall()
            if domain_ancestors != [("NCBITaxon:2",)]:
                raise ValueError(f"source bacterial stock resolved outside Bacteria: {identifier}")
            if (
                genus == "Bosea"
                and ("oio:hasRelatedSynonym", "Bosea Das et al. 1996", None) not in taxonomy
            ):
                raise ValueError("bacterial Bosea rename lacks the verified authority synonym")
            roster.append(
                {
                    "source_name": source_name,
                    "strain": stock,
                    "source_cell": f"Table S1!A{row_index}:J{row_index}",
                    "silva_classification": row[8],
                    "source_gtdb_tk_classification": row[9],
                    "term": {"id": identifier, "label": label},
                    "rank": expected_rank,
                    "native_authority_rows": taxonomy,
                    "verified_domain_ancestors": domain_ancestors,
                    "limitation": "Species and stock genome identity not inferred from genus/family grounding.",
                }
            )
        host = connection.execute(
            "SELECT subject FROM statements WHERE predicate='rdfs:label' AND value='Brachypodium distachyon'"
        ).fetchall()
    if not roster:
        raise ValueError("requested stock absent from exact source roster")
    mapping = None
    if args.mapping:
        mapping_sha = sha(args.mapping)
        if mapping_sha != "761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd":
            raise ValueError("unexpected crosswalk input")
        keys = {key for row in roster for key in native.lookup_keys(row["term"]["label"])}
        indexed = native.collect_rows(args.mapping, set(), set(), keys)
        for row in roster:
            row["native_rank_mapping"] = native.resolve_target(
                row["term"]["id"].split(":", 1)[1],
                row["term"]["label"],
                *indexed,
                denominator="aggregate",
                exclude_unnamed=True,
            )
        mapping = {
            "path": str(args.mapping),
            "sha256": mapping_sha,
            "native_script_sha256": sha(ROOT / "scripts/gtdb_ground.py"),
            "method": "native aggregate denominator excluding unnamed species; genus/family correspondence, not study-stock identity",
            "release_limitation": "Crosswalk hash does not establish GTDB release or build date.",
        }
    fingerprint = sha(args.ncbi) if args.fingerprint else None
    after = args.ncbi.stat()
    if (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns):
        raise ValueError("ontology input changed during inspection")
    print(
        json.dumps(
            {
                "accessed_at": datetime.now(timezone.utc).isoformat(),
                "table_sha256": sha(args.table),
                "ontology": {
                    "path": str(args.ncbi),
                    "bytes": before.st_size,
                    "mtime_ns": before.st_mtime_ns,
                    "sha256": fingerprint,
                },
                "mode": "one-stock canary" if args.only_strain else "source roster",
                "mapping": mapping,
                "roster": roster,
                "host_exact_label_candidates": host,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
