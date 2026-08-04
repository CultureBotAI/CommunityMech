#!/usr/bin/env python3
"""Compare the two GTDB majority denominators over every taxon in the KB (#371).

`NCBI2GTDB.tsv.gz` is an upstream crosswalk (Bork group / metatraits) in which
each row is an independent NCBI->GTDB assignment carrying its own genome support.
`gtdb_ground.py` sums that support over every matched row. Because a genome
supports the assignment of its strain *and* its species *and* its genus, the
supports total 1.84M across the table against ~600k genomes in a GTDB release.

That is a weighting choice, not an arithmetic error, and the alternative — one
row per lineage at the deepest depth available — is equally defensible. It is
also the rule `kg-microbe-paper` settled on for the same shape of problem.

Neither is provably right, so this script does not pick. It emits the comparison
so the choice can be made from the table rather than in the abstract, which is
the process that prior art used: write every scenario out, and be explicit that
the preferred one was not chosen for producing the nicer answer.

    uv run python scripts/gtdb_denominator_compare.py [--out reports/gtdb_denominators.tsv]

Columns: the taxon, both grounded ids, both majority fractions, and whether the
outcome flips — and in which direction.
"""

from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).parent.parent
COMMUNITIES = REPO / "kb/communities"


def _load_grounder():
    spec = importlib.util.spec_from_file_location("gtdb_ground", REPO / "scripts/gtdb_ground.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _kb_taxa() -> list:
    """Every distinct (ncbi_id, label) in the KB, deduplicated on the id."""
    seen: dict[str, str] = {}
    for path in sorted(COMMUNITIES.glob("*.yaml")):
        data = yaml.safe_load(path.read_text()) or {}
        for taxon in data.get("taxonomy") or []:
            if not isinstance(taxon, dict):
                continue
            term = (taxon.get("taxon_term") or {}).get("term") or {}
            tid = str(term.get("id") or "")
            if tid.startswith("NCBITaxon:"):
                seen.setdefault(tid, term.get("label") or "")
    return sorted(seen.items())


def _outcome(result) -> tuple:
    """(gtdb_id, majority_fraction) for a resolve_target result; AMBIGUOUS if split."""
    if not result:
        return ("NONE", "")
    if result.get("ambiguous"):
        return ("AMBIGUOUS", "")
    return (result.get("gtdb_id") or "NONE", result.get("majority_fraction", ""))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=REPO / "reports/gtdb_denominators.tsv")
    parser.add_argument("--kg-microbe-dir", default=None)
    args = parser.parse_args()

    grounder = _load_grounder()
    try:
        mapping = grounder.resolve_kg_microbe_dir(args.kg_microbe_dir) / "data/raw/NCBI2GTDB.tsv.gz"
    except SystemExit as exc:
        print(str(exc), file=sys.stderr)
        return 2

    taxa = _kb_taxa()
    ids = {tid.split(":")[1] for tid, _ in taxa}
    cleaned = [grounder._clean_label(label) for _, label in taxa]
    species = {c.lower() for c in cleaned if " " in c}
    higher = {c.lower() for c in cleaned if " " not in c}
    by_id, by_name, by_higher = grounder.collect_rows(mapping, ids, species, higher)

    SCENARIOS = [
        ("aggregate", "aggregate", False),
        ("aggregate+named", "aggregate", True),
        ("deepest", "deepest", False),
        ("deepest+named", "deepest", True),
    ]

    rows, differ_from_default = [], 0
    for tid, label in taxa:
        core = tid.split(":")[1]
        # Only the higher-rank path has these choices; the species and id paths
        # resolve a single row and are identical under all four.
        answers = {
            name: _outcome(
                grounder.resolve_target(
                    core, label, by_id, by_name, by_higher,
                    denominator=den, exclude_unnamed=filt,
                )
            )
            for name, den, filt in SCENARIOS
        }
        default = answers["aggregate"][0]
        varies = sorted({a[0] for a in answers.values()})
        if len(varies) > 1:
            differ_from_default += 1
        rows.append((tid, label, *[x for a in answers.values() for x in a],
                     "VARIES" if len(varies) > 1 else "", len(varies)))

    args.out.parent.mkdir(parents=True, exist_ok=True)
    stat = mapping.stat()
    with open(args.out, "w") as fh:
        # Provenance: the upstream crosswalk churns (the KB already carries two
        # build vintages), so a bare table would go stale silently.
        fh.write(f"# mapping: {mapping.name}\tbytes={stat.st_size}\tmtime={int(stat.st_mtime)}\n")
        fh.write(f"# taxa={len(rows)}\tvarying={differ_from_default}\n")
        fh.write(
            "ncbi_id\tlabel\t"
            "aggregate_id\taggregate_frac\t"
            "aggregate_named_id\taggregate_named_frac\t"
            "deepest_id\tdeepest_frac\t"
            "deepest_named_id\tdeepest_named_frac\t"
            "varies\tdistinct_answers\n"
        )
        for row in rows:
            fh.write("\t".join(str(c) for c in row) + "\n")

    print(f"taxa compared: {len(rows)}")
    print(f"taxa where the four scenarios disagree: {differ_from_default}")
    for row in rows:
        if row[10]:
            print(f"  {row[0]:<18s} {row[1][:24]:<26s} "
                  f"agg={row[2]:<26s} agg+named={row[4]:<26s} "
                  f"deep={row[6]:<26s} deep+named={row[8]}")
    print(f"\nwritten to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
