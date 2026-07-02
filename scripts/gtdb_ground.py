#!/usr/bin/env python3
"""Ground CommunityMech taxa in GTDB using the local kg-microbe NCBI<->GTDB mapping.

For a taxon already grounded in NCBITaxon, look up its GTDB (Genome Taxonomy
Database) classification — canonical GTDB CURIE, taxon name, full lineage, and
the mapping confidence — from kg-microbe's ``data/raw/NCBI2GTDB.tsv.gz``. GTDB
frequently renames/reclassifies relative to NCBI (e.g. NCBITaxon "Agrobacterium
deltae" -> GTDB "Agrobacterium leguminum"), so this surfaces a genome-based
second opinion and emits a ready-to-paste ``gtdb_classification`` YAML block for
the CommunityMech schema.

Data source (local kg-microbe checkout; no network):
  <kg-microbe>/data/raw/NCBI2GTDB.tsv.gz
Resolution order for <kg-microbe>: --kg-microbe-dir, $KG_MICROBE_DIR,
then ../../kg-microbe relative to this repo.

GTDB CURIE scheme (matches kg-microbe / Bioregistry): the species name with
spaces replaced by underscores, e.g. "s__Bacillus velezensis" ->
"GTDB:s__Bacillus_velezensis"; resolvable at
https://gtdb.ecogenomic.org/tree?r={id}.

Usage:
    uv run python scripts/gtdb_ground.py --ncbi-id NCBITaxon:492670 --emit-yaml
    uv run python scripts/gtdb_ground.py --name "Bacillus velezensis"
    uv run python scripts/gtdb_ground.py --community kb/communities/Foo.yaml --emit-yaml
"""

from __future__ import annotations

import argparse
import gzip
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
MAPPING_REL = Path("data/raw/NCBI2GTDB.tsv.gz")

# NCBI2GTDB.tsv column indices (0-based); see header row.
COL_NCBI_ID = 0
COL_GTDB_ID = 1  # kg-microbe-internal numeric id (not the CURIE) — not used
COL_MAJORITY = 3
COL_NCBI_SPECIES = 10
# GTDB lineage columns: domain..species = 12..18 ; strain = 19
COL_GTDB_DOMAIN = 12
COL_GTDB_SPECIES = 18
RANK_PREFIXES = ["d__", "p__", "c__", "o__", "f__", "g__", "s__"]


def resolve_kg_microbe_dir(explicit: str | None) -> Path:
    candidates = []
    if explicit:
        candidates.append(Path(explicit))
    if os.environ.get("KG_MICROBE_DIR"):
        candidates.append(Path(os.environ["KG_MICROBE_DIR"]))
    # kg-microbe is a sibling of the outer KG-Microbe project dir; walk up a few
    # levels to tolerate the nested CommunityMech/CommunityMech layout.
    for up in (REPO_ROOT.parent, REPO_ROOT.parent.parent, REPO_ROOT.parent.parent.parent):
        candidates.append(up / "kg-microbe")
    for c in candidates:
        if (c / MAPPING_REL).exists():
            return c
    tried = "\n  ".join(str(c / MAPPING_REL) for c in candidates)
    sys.exit(f"[gtdb] NCBI2GTDB mapping not found. Tried:\n  {tried}\n"
             f"Pass --kg-microbe-dir or set KG_MICROBE_DIR.")


def _gtdb_curie(species_name: str) -> str:
    return "GTDB:s__" + species_name.replace(" ", "_")


def _lineage(cells: list[str]) -> str:
    ranks = cells[COL_GTDB_DOMAIN:COL_GTDB_SPECIES + 1]
    return ";".join(f"{p}{r}" for p, r in zip(RANK_PREFIXES, ranks) if r)


def stream_rows(mapping_path: Path, want_ids: set[str] | None, want_names: set[str] | None):
    """Yield matching rows from the gzipped TSV. Matches by NCBI id or NCBI species name."""
    want_names_lc = {n.lower() for n in want_names} if want_names else None
    with gzip.open(mapping_path, "rt") as fh:
        next(fh)  # header
        for line in fh:
            cells = line.rstrip("\n").split("\t")
            if len(cells) <= COL_GTDB_SPECIES:
                continue
            ncbi_id = cells[COL_NCBI_ID].strip()
            if want_ids and ncbi_id in want_ids:
                yield ncbi_id, cells
            elif want_names_lc and cells[COL_NCBI_SPECIES].strip().lower() in want_names_lc:
                yield ncbi_id, cells


def best_per_id(matches: list[tuple[str, list[str]]]) -> dict[str, dict]:
    """Collapse multiple GTDB rows per NCBI id to the highest-majority one; flag splits."""
    by_id: dict[str, list[list[str]]] = {}
    for ncbi_id, cells in matches:
        by_id.setdefault(ncbi_id, []).append(cells)
    out: dict[str, dict] = {}
    for ncbi_id, rows in by_id.items():
        def maj(c):
            try:
                return float(c[COL_MAJORITY])
            except ValueError:
                return 0.0
        rows.sort(key=maj, reverse=True)
        top = rows[0]
        gtdb_species = top[COL_GTDB_SPECIES].strip()
        ncbi_species = top[COL_NCBI_SPECIES].strip()
        out[ncbi_id] = {
            "ncbi_source_id": f"NCBITaxon:{ncbi_id}",
            "ncbi_species": ncbi_species,
            "gtdb_id": _gtdb_curie(gtdb_species) if gtdb_species else None,
            "gtdb_taxon": gtdb_species or None,
            "gtdb_lineage": _lineage(top),
            "majority_fraction": maj(top),
            "is_reclassified": bool(gtdb_species and ncbi_species and gtdb_species != ncbi_species),
            "n_gtdb_mappings": len(rows),
        }
    return out


def emit_block(g: dict, mapping_source: str) -> str:
    d = {
        "gtdb_classification": {
            "gtdb_id": g["gtdb_id"],
            "gtdb_taxon": g["gtdb_taxon"],
            "gtdb_lineage": g["gtdb_lineage"],
            "ncbi_source_id": g["ncbi_source_id"],
            "majority_fraction": g["majority_fraction"],
            "is_reclassified": g["is_reclassified"],
            "mapping_source": mapping_source,
        }
    }
    return yaml.dump(d, default_flow_style=False, sort_keys=False, allow_unicode=True, width=100)


def community_ncbi_ids(path: Path) -> list[tuple[str, str]]:
    """Return (ncbi_id, preferred_term) for each taxonomy[].taxon_term in a community YAML."""
    doc = yaml.safe_load(path.read_text())
    out = []
    for tc in doc.get("taxonomy", []) or []:
        tt = (tc or {}).get("taxon_term", {}) or {}
        term = tt.get("term", {}) or {}
        tid = term.get("id", "")
        if tid.startswith("NCBITaxon:"):
            out.append((tid.split(":", 1)[1], tt.get("preferred_term", term.get("label", ""))))
    return out


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument("--ncbi-id", action="append", help="NCBITaxon:NNN (repeatable).")
    src.add_argument("--name", action="append", help="NCBI species name (repeatable).")
    src.add_argument("--community", type=Path, help="Community YAML — ground all its taxa.")
    p.add_argument("--kg-microbe-dir", help="Path to kg-microbe checkout (else $KG_MICROBE_DIR or ../../kg-microbe).")
    p.add_argument("--emit-yaml", action="store_true", help="Print ready-to-paste gtdb_classification blocks.")
    args = p.parse_args(argv)

    kg_dir = resolve_kg_microbe_dir(args.kg_microbe_dir)
    mapping_path = kg_dir / MAPPING_REL
    built = datetime.fromtimestamp(mapping_path.stat().st_mtime, tz=timezone.utc).date().isoformat()
    mapping_source = f"kg-microbe NCBI2GTDB.tsv.gz; GTDB release latest (built {built})"
    print(f"[gtdb] mapping: {mapping_path}  ({mapping_source})", file=sys.stderr)

    want_ids: set[str] = set()
    want_names: set[str] = set()
    labels: dict[str, str] = {}
    if args.community:
        for nid, term in community_ncbi_ids(args.community):
            want_ids.add(nid)
            labels[nid] = term
        print(f"[gtdb] {args.community.name}: {len(want_ids)} NCBITaxon taxa", file=sys.stderr)
    if args.ncbi_id:
        for x in args.ncbi_id:
            want_ids.add(x.split(":", 1)[1] if ":" in x else x)
    if args.name:
        want_names.update(args.name)

    matches = list(stream_rows(mapping_path, want_ids or None, want_names or None))
    grounded = best_per_id(matches)

    if not grounded:
        print("[gtdb] no GTDB mapping found (taxon may be above species rank or absent from GTDB).",
              file=sys.stderr)
        return 1

    for nid, g in sorted(grounded.items()):
        flag = "  ⚠ RECLASSIFIED" if g["is_reclassified"] else ""
        split = f"  (⚠ {g['n_gtdb_mappings']} GTDB mappings — showing highest majority)" if g["n_gtdb_mappings"] > 1 else ""
        lab = labels.get(nid, g["ncbi_species"])
        print(f"\nNCBITaxon:{nid}  {lab}")
        print(f"  NCBI species : {g['ncbi_species']}")
        print(f"  GTDB taxon   : {g['gtdb_taxon']}{flag}")
        print(f"  GTDB CURIE   : {g['gtdb_id']}")
        print(f"  GTDB lineage : {g['gtdb_lineage']}")
        print(f"  majority     : {g['majority_fraction']}{split}")
        if args.emit_yaml:
            print("  --- gtdb_classification block ---")
            for line in emit_block(g, mapping_source).splitlines():
                print(f"  {line}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
