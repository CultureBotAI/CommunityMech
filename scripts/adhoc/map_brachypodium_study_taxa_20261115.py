"""Map verified study sequence-record taxon IDs using native GTDB, 2026-11-15.

Inputs: source/Sample identity receipt, unchanged authority receipt, exact local
crosswalk. Output: stdout JSON; no record/source writes or provider requests.
Native unresolved/ambiguous results survive; a sequence taxon is not a named
biological species and current assembly versions need not be those used in 2025.
"""

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import gtdb_ground as native  # noqa: E402


def sha(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--identities", type=Path, required=True)
    parser.add_argument("--authority-receipt", type=Path, required=True)
    parser.add_argument("--mapping", type=Path, required=True)
    parser.add_argument("--only-strain")
    args = parser.parse_args()
    identity = json.loads(args.identities.read_bytes())
    authority = json.loads(args.authority_receipt.read_bytes())
    path = Path(authority["ontology"]["path"])
    before = path.stat()
    if (
        before.st_size != authority["ontology"]["bytes"]
        or before.st_mtime_ns != authority["ontology"]["mtime_ns"]
    ):
        raise ValueError("authority changed since fingerprinted inspection")
    if sha(args.mapping) != "761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd":
        raise ValueError("unexpected crosswalk")
    rows = [
        row
        for row in identity["roster"]
        if args.only_strain is None or row["paper_stock"] == args.only_strain
    ]
    if not rows:
        raise ValueError("stock is absent from source-bound roster")
    wanted_ids = {row["taxon_id"].split(":", 1)[1] for row in rows}
    names = {key for row in rows for key in native.lookup_keys(row["taxon_name"])}
    indexed = native.collect_rows(args.mapping, wanted_ids, names, set())
    for row in rows:
        row["native_sequence_taxon_mapping"] = native.resolve_target(
            row["taxon_id"].split(":", 1)[1],
            row["taxon_name"],
            *indexed,
            denominator="aggregate",
            exclude_unnamed=True,
        )
    after = path.stat()
    if (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns):
        raise ValueError("authority changed during mapping")
    print(
        json.dumps(
            {
                "identity_receipt_sha256": sha(args.identities),
                "authority_receipt_sha256": sha(args.authority_receipt),
                "native_script_sha256": sha(ROOT / "scripts/gtdb_ground.py"),
                "mapping_sha256": sha(args.mapping),
                "ontology_hash_from_unchanged_stat_receipt": authority["ontology"],
                "mode": (
                    "one-stock canary"
                    if args.only_strain
                    else "all15 verified sequence-record taxa"
                ),
                "roster": rows,
                "excluded_project_entries": identity["excluded_project_entries"],
                "limitations": [
                    identity["limitation"],
                    "Named species filter and native unresolved/ambiguous behavior are unchanged; no fallback or taxonomy waiver.",
                    "Native database fingerprint is inherited from the explicitly unchanged size/mtime snapshot, not recomputed here.",
                ],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
