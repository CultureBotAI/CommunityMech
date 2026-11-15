"""Ground the Methods-defined 12 stocks for CommunityMech000122/#1548, 2026-11-15.

Inputs: retained primary XML, explicit read-only NCBI/ENVO SQLite databases and
the retained NCBI2GTDB crosswalk. Output: JSON to stdout; no writes or network.
Species-level mappings do not assert a genome identity for a study stock.
"""

import argparse
import hashlib
import json
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import gtdb_ground as native  # noqa: E402

ROSTER = [
    ("BH", "Blautia hydrogenotrophica", "DSM", "10507", 41),
    ("FP", "Faecalibacterium prausnitzii", "DSM", "17677", 41),
    ("CA", "Collinsella aerofaciens", "DSM", "3979", 41),
    ("PC", "Prevotella copri", "DSM", "18205", 41),
    ("ER", "Eubacterium rectale", "ATCC", "33656", 41),
    ("DP", "Desulfovibrio piger", "ATCC", "29098", 41),
    ("BU", "Bacteroides uniformis", "DSM", "6597", 16),
    ("BV", "Bacteroides vulgatus", "ATCC", "8482", 16),
    ("BT", "Bacteroides thetaiotaomicron", "ATCC", "29148", 16),
    ("BO", "Bacteroides ovatus", "ATCC", "8483", 16),
    ("CH", "Clostridium hiranonis", "DSM", "13275", 16),
    ("EL", "Eggerthella lenta", "DSM", "2243", 16),
]
REVIEWED_NAMES = {
    "FP": "Faecalibacterium duncaniae",
    "PC": "Prevotella copri Hayashi et al. 2007",
    "ER": "Eubacterium rectale (Hauduroy et al. 1937) Prevot 1938 (Approved Lists 1980)",
    "BV": "Bacteroides vulgatus Eggerth and Gagnon 1933 (Approved Lists 1980)",
}


def sha(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def connect(path):
    conn = sqlite3.connect(path.resolve().as_uri() + "?mode=ro", uri=True)
    conn.execute("PRAGMA query_only=ON")
    conn.execute("BEGIN")
    return conn


def describe(conn, identifier):
    rows = conn.execute(
        "SELECT predicate,value,object FROM statements WHERE subject=? AND "
        "(predicate='rdfs:label' OR predicate LIKE '%Synonym%' OR predicate LIKE '%rank%') "
        "ORDER BY predicate,value,object",
        (identifier,),
    ).fetchall()
    labels = [value for predicate, value, obj in rows if predicate == "rdfs:label"]
    if len(labels) != 1:
        raise ValueError(f"missing/ambiguous label: {identifier}")
    return {
        "term": {"id": identifier, "label": labels[0]},
        "assertions": [{"predicate": p, "value": v, "object": o} for p, v, o in rows],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ncbi", type=Path, required=True)
    parser.add_argument("--envo", type=Path, required=True)
    parser.add_argument("--mapping", type=Path, required=True)
    parser.add_argument("--only", choices=[row[0] for row in ROSTER])
    parser.add_argument("--environment-only", action="store_true")
    parser.add_argument(
        "--discover",
        action="store_true",
        help="Inspect candidate labels/synonyms; no identity verdict",
    )
    args = parser.parse_args()
    if args.environment_only:
        before = args.envo.stat()
        with connect(args.envo) as conn:
            environment = [
                describe(conn, identifier) for identifier in ("ENVO:01001405", "ENVO:2100002")
            ]
        fingerprint = sha(args.envo)
        if (before.st_size, before.st_mtime_ns) != (
            args.envo.stat().st_size,
            args.envo.stat().st_mtime_ns,
        ):
            raise ValueError("environment authority changed during query")
        print(
            json.dumps(
                {"database": args.envo.name, "sha256": fingerprint, "terms": environment}, indent=2
            )
        )
        return
    paths = [args.ncbi, args.envo, args.mapping]
    before = [(p.stat().st_size, p.stat().st_mtime_ns) for p in paths]
    source = ROOT / ".temp/phase2-gut-20261115/primary-001/article.xml"
    if sha(source) != "9148ad1c34d3e0527d86bbd7d70c83792306c502deadde5c353c525ece318e08":
        raise ValueError("primary source changed")
    selected = [row for row in ROSTER if args.only is None or row[0] == args.only]
    rows = []
    with connect(args.ncbi) as conn:
        for abbreviation, name, collection, accession, starter_h in selected:
            query_name = name if args.discover else REVIEWED_NAMES.get(abbreviation, name)
            if abbreviation == "FP" and not args.discover:
                catalogue = ROOT / ".temp/phase2-gut-20261115/dsm17677-catalog-001/catalog.txt"
                if (
                    "Since May 2022 assigned to the species Faecalibacterium duncaniae"
                    not in " ".join(catalogue.read_text().split())
                ):
                    raise ValueError("stock-specific reclassification source missing")
            found = conn.execute(
                "SELECT DISTINCT subject FROM statements WHERE value=? AND "
                "(predicate='rdfs:label' OR predicate LIKE '%Synonym%')",
                (query_name,),
            ).fetchall()
            candidates = [describe(conn, item[0]) for item in found]
            if args.discover:
                matches = conn.execute(
                    "SELECT DISTINCT subject,predicate,value FROM statements WHERE value LIKE ? "
                    "AND (predicate='rdfs:label' OR predicate LIKE '%Synonym%') ORDER BY subject",
                    (name + "%",),
                ).fetchall()
                rows.append(
                    {
                        "source_name": name,
                        "matches": [
                            {"matched_predicate": p, "matched_value": v, **describe(conn, s)}
                            for s, p, v in matches
                        ],
                    }
                )
                continue
            species = [
                candidate
                for candidate in candidates
                if any(item["object"] == "NCBITaxon:species" for item in candidate["assertions"])
            ]
            if len(species) != 1:
                raise ValueError(f"source name has {len(species)} species-level identities: {name}")
            rows.append(
                {
                    "member_id": abbreviation,
                    "source_name": name,
                    "verified_name_query": query_name,
                    "collection": collection,
                    "accession": accession,
                    "starter_incubation_hours": starter_h,
                    **species[0],
                }
            )
    if args.discover:
        print(json.dumps({"mode": "candidate discovery only", "rows": rows}, indent=2))
        return
    with connect(args.envo) as conn:
        envo = describe(conn, "ENVO:01001405")
    ids = {row["term"]["id"].split(":", 1)[1] for row in rows}
    names = {key for row in rows for key in native.lookup_keys(row["term"]["label"])}
    indexed = native.collect_rows(args.mapping, ids, names, set())
    for row in rows:
        row["native_grounding"] = native.resolve_target(
            row["term"]["id"].split(":", 1)[1],
            row["term"]["label"],
            *indexed,
            denominator="aggregate",
            exclude_unnamed=True,
        )
    hashes = {p.name: sha(p) for p in paths}
    if (
        hashes[args.mapping.name]
        != "761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd"
    ):
        raise ValueError("unreviewed crosswalk")
    if before != [(p.stat().st_size, p.stat().st_mtime_ns) for p in paths]:
        raise ValueError("read-only input changed during query")
    print(
        json.dumps(
            {
                "source_sha256": sha(source),
                "input_hashes": hashes,
                "native_script_sha256": sha(ROOT / "scripts/gtdb_ground.py"),
                "mode": "one-stock canary" if args.only else "12-stock roster",
                "environment": envo,
                "rows": rows,
                "scope": "Species identity and crosswalk only; no stock-specific genome, type-strain status or functional-role inference.",
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
