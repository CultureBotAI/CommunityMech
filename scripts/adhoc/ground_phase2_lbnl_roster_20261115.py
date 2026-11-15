"""Read-only genus grounding evidence for the #1548 final16 canary, 2026-11-15.

Inputs: source-roster receipt, explicit readonly NCBI/ENVO databases and GTDB crosswalk.
Output: JSON on stdout. No canonical/database writes or provider requests.
The genus mapping is not a genome assignment for an individual study stock.
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


def digest_file(path):
    result = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(4 * 1024 * 1024), b""):
            result.update(chunk)
    return result.hexdigest()


def query_terms(path, identifiers):
    before = path.stat()
    uri = path.resolve().as_uri() + "?mode=ro"
    rows = {}
    with sqlite3.connect(uri, uri=True) as connection:
        connection.execute("PRAGMA query_only=ON")
        connection.execute("BEGIN")
        for identifier in identifiers:
            selected = connection.execute(
                "SELECT predicate, value, object FROM statements WHERE subject=? "
                "AND (predicate='rdfs:label' OR predicate LIKE '%Synonym%' "
                "OR predicate LIKE '%rank%') ORDER BY predicate,value,object",
                (identifier,),
            ).fetchall()
            rows[identifier] = [
                {"predicate": predicate, "value": value, "object": obj}
                for predicate, value, obj in selected
            ]
            labels = [row["value"] for row in rows[identifier] if row["predicate"] == "rdfs:label"]
            if len(labels) != 1 or not labels[0]:
                raise ValueError(f"missing or ambiguous canonical label: {identifier}")
    sha256 = digest_file(path)
    after = path.stat()
    if (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns):
        raise ValueError("ontology database changed during readonly query/fingerprint")
    return {"filename": path.name, "bytes": before.st_size, "sha256": sha256, "rows": rows}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--roster", type=Path, required=True)
    parser.add_argument("--ncbi", type=Path, required=True)
    parser.add_argument("--envo", type=Path, required=True)
    parser.add_argument("--mapping", type=Path, required=True)
    parser.add_argument("--only-strain", help="Same-path one-stock canary before remaining roster")
    args = parser.parse_args()
    roster_bytes = args.roster.read_bytes()
    roster = json.loads(roster_bytes)
    selected = [
        row
        for row in roster["roster"]
        if args.only_strain is None or row["strain"] == args.only_strain
    ]
    if not selected:
        raise ValueError("requested strain is not in source final16 roster")
    identifiers = {}
    for row in selected:
        # The paper identifies an unknown species within Arthrobacter, not the
        # unrelated generic 'Arthrobacter sp.' species taxon used by the neighbor.
        identifier = (
            "NCBITaxon:1663" if row["strain"] == "OAP107" else row["candidate_neighbor_term"]["id"]
        )
        identifiers[row["strain"]] = identifier
    ncbi = query_terms(args.ncbi, identifiers.values())
    envo = query_terms(args.envo, ["ENVO:01001405", "ENVO:00001998"])
    labels = {
        identifier: next(row["value"] for row in rows if row["predicate"] == "rdfs:label")
        for identifier, rows in ncbi["rows"].items()
    }
    for identifier, rows in ncbi["rows"].items():
        if not any(row["object"] == "NCBITaxon:genus" for row in rows):
            raise ValueError(f"candidate is not a verified genus: {identifier}")
    mapping_sha256 = digest_file(args.mapping)
    if mapping_sha256 != "761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd":
        raise ValueError("crosswalk does not match the retained reviewed input")
    higher = {key for label in labels.values() for key in native.lookup_keys(label)}
    indexed = native.collect_rows(args.mapping, set(), set(), higher)
    rows = []
    for item in selected:
        identifier = identifiers[item["strain"]]
        label = labels[identifier]
        grounding = native.resolve_target(
            identifier.split(":", 1)[1],
            label,
            *indexed,
            denominator="aggregate",
            exclude_unnamed=True,
        )
        rows.append(
            {
                **item,
                "verified_genus_term": {"id": identifier, "label": label},
                "native_genus_grounding": grounding,
            }
        )
    print(
        json.dumps(
            {
                "roster_sha256": hashlib.sha256(roster_bytes).hexdigest(),
                "mode": "one-stock canary" if args.only_strain else "source final16",
                "ncbi": ncbi,
                "envo": envo,
                "mapping": {"filename": args.mapping.name, "sha256": mapping_sha256},
                "native_script_sha256": digest_file(ROOT / "scripts/gtdb_ground.py"),
                "method": "native aggregate denominator, unnamed species excluded; genus scope only",
                "rows": rows,
                "limitations": [
                    "Canonical genus identity does not identify an unknown study-stock species or genome.",
                    "Source names that differ from current genus labels require inspected synonym/reclassification support.",
                    "No GTDB release/build date is inferred from the crosswalk file timestamp.",
                ],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
