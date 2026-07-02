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
    sys.exit(
        f"[gtdb] NCBI2GTDB mapping not found. Tried:\n  {tried}\n"
        f"Pass --kg-microbe-dir or set KG_MICROBE_DIR."
    )


def _gtdb_curie(species_name: str) -> str:
    return "GTDB:s__" + species_name.replace(" ", "_")


def _lineage(cells: list[str]) -> str:
    ranks = cells[COL_GTDB_DOMAIN : COL_GTDB_SPECIES + 1]
    return ";".join(f"{p}{r}" for p, r in zip(RANK_PREFIXES, ranks, strict=False) if r)


def _maj(c: list[str]) -> float:
    try:
        return float(c[COL_MAJORITY])
    except (ValueError, IndexError):
        return 0.0


def collect_rows(mapping_path: Path, want_ids: set[str], want_names_lc: set[str]):
    """One pass over the gzipped TSV; index matching rows by NCBI id and by NCBI species name."""
    by_id: dict[str, list[list[str]]] = {}
    by_name: dict[str, list[list[str]]] = {}
    with gzip.open(mapping_path, "rt") as fh:
        next(fh)  # header
        for line in fh:
            cells = line.rstrip("\n").split("\t")
            if len(cells) <= COL_GTDB_SPECIES:
                continue
            nid = cells[COL_NCBI_ID].strip()
            if nid in want_ids:
                by_id.setdefault(nid, []).append(cells)
            nlc = cells[COL_NCBI_SPECIES].strip().lower()
            if nlc and nlc in want_names_lc:
                by_name.setdefault(nlc, []).append(cells)
    return by_id, by_name


def _ground(rows: list[list[str]], source_id: str | None, our_label: str | None, via: str) -> dict:
    """Build a grounding dict from rows that all share one GTDB species (highest majority wins)."""
    rows = sorted(rows, key=_maj, reverse=True)
    top = rows[0]
    gtdb_species = top[COL_GTDB_SPECIES].strip()
    ref_name = our_label or top[COL_NCBI_SPECIES].strip()
    return {
        "ncbi_source_id": source_id,
        "ncbi_species": ref_name,
        "gtdb_id": _gtdb_curie(gtdb_species) if gtdb_species else None,
        "gtdb_taxon": gtdb_species or None,
        "gtdb_lineage": _lineage(top),
        "majority_fraction": _maj(top),
        "is_reclassified": bool(gtdb_species and ref_name and gtdb_species != ref_name),
        "via": via,
        "n_rows": len(rows),
    }


def resolve_target(
    ncbi_id: str | None, label: str | None, by_id: dict, by_name: dict
) -> dict | None:
    """Resolve one taxon: exact NCBI id first, then NCBI species-name fallback (ambiguity-aware)."""
    source_id = f"NCBITaxon:{ncbi_id}" if ncbi_id else None
    # Genus-rank (or higher) inputs have single-word labels; the mapping is
    # species-keyed, so grounding a genus term to one species would be spurious.
    if label and len(label.strip().split()) < 2:
        return None
    if ncbi_id and ncbi_id in by_id:
        return _ground(by_id[ncbi_id], source_id, label, "ncbi_id")
    nlc = (label or "").strip().lower()
    if nlc and nlc in by_name:
        # Group name-matched rows by GTDB species; GTDB may split one NCBI species.
        species: dict[str, list[list[str]]] = {}
        for c in by_name[nlc]:
            sp = c[COL_GTDB_SPECIES].strip()
            if sp:
                species.setdefault(sp, []).append(c)
        if len(species) == 1:
            rows = next(iter(species.values()))
            return _ground(rows, source_id, label, "ncbi_name")
        if len(species) > 1:
            return {
                "ambiguous": True,
                "via": "ncbi_name",
                "ncbi_source_id": source_id,
                "ncbi_species": label,
                "gtdb_options": sorted(species),
            }
    return None


def emit_block(g: dict, mapping_source: str) -> str:
    src = mapping_source
    if g.get("via") == "ncbi_name":
        src += " [mapped via NCBI species name — no species-level NCBI id in table]"
    d = {
        "gtdb_classification": {
            "gtdb_id": g["gtdb_id"],
            "gtdb_taxon": g["gtdb_taxon"],
            "gtdb_lineage": g["gtdb_lineage"],
            "ncbi_source_id": g["ncbi_source_id"],
            "majority_fraction": g["majority_fraction"],
            "is_reclassified": g["is_reclassified"],
            "mapping_source": src,
        }
    }
    return yaml.dump(d, default_flow_style=False, sort_keys=False, allow_unicode=True, width=100)


def community_taxa(path: Path) -> list[tuple[str, str]]:
    """Return (ncbi_id, canonical_label) for each taxonomy[].taxon_term in a community YAML."""
    doc = yaml.safe_load(path.read_text())
    out = []
    for tc in doc.get("taxonomy", []) or []:
        tt = (tc or {}).get("taxon_term", {}) or {}
        term = tt.get("term", {}) or {}
        tid = term.get("id", "")
        if tid.startswith("NCBITaxon:"):
            out.append((tid.split(":", 1)[1], term.get("label", tt.get("preferred_term", ""))))
    return out


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument("--ncbi-id", action="append", help="NCBITaxon:NNN (repeatable).")
    src.add_argument("--name", action="append", help="NCBI species name (repeatable).")
    src.add_argument("--community", type=Path, help="Community YAML — ground all its taxa.")
    p.add_argument(
        "--kg-microbe-dir",
        help="Path to kg-microbe checkout (else $KG_MICROBE_DIR or ../../kg-microbe).",
    )
    p.add_argument(
        "--emit-yaml", action="store_true", help="Print ready-to-paste gtdb_classification blocks."
    )
    args = p.parse_args(argv)

    kg_dir = resolve_kg_microbe_dir(args.kg_microbe_dir)
    mapping_path = kg_dir / MAPPING_REL
    built = datetime.fromtimestamp(mapping_path.stat().st_mtime, tz=timezone.utc).date().isoformat()
    mapping_source = f"kg-microbe NCBI2GTDB.tsv.gz; GTDB release latest (built {built})"
    print(f"[gtdb] mapping: {mapping_path}  ({mapping_source})", file=sys.stderr)

    # Build targets: (ncbi_id | None, label | None). Community mode carries both
    # id and canonical label so we can fall back from id to species-name matching.
    targets: list[tuple[str | None, str | None]] = []
    if args.community:
        targets = [(nid, lab) for nid, lab in community_taxa(args.community)]
        print(f"[gtdb] {args.community.name}: {len(targets)} NCBITaxon taxa", file=sys.stderr)
    if args.ncbi_id:
        targets += [(x.split(":", 1)[1] if ":" in x else x, None) for x in args.ncbi_id]
    if args.name:
        targets += [(None, n) for n in args.name]

    want_ids = {nid for nid, _ in targets if nid}
    want_names_lc = {lab.lower() for _, lab in targets if lab}
    by_id, by_name = collect_rows(mapping_path, want_ids, want_names_lc)

    n_ok = 0
    for ncbi_id, label in targets:
        g = resolve_target(ncbi_id, label, by_id, by_name)
        head = f"\nNCBITaxon:{ncbi_id}" if ncbi_id else f"\n{label}"
        if label and ncbi_id:
            head += f"  {label}"
        if g is None:
            print(head)
            print("  no GTDB mapping (above species rank, fungal/eukaryote, or absent from GTDB).")
            continue
        if g.get("ambiguous"):
            opts = ", ".join(g["gtdb_options"])
            print(head)
            print(f"  ⚠ AMBIGUOUS — GTDB splits this species into: {opts}")
            print("  (no single grounding emitted; a curator should pick or leave ungrounded.)")
            continue
        n_ok += 1
        flag = "  ⚠ RECLASSIFIED" if g["is_reclassified"] else ""
        via = "" if g["via"] == "ncbi_id" else "  (via NCBI species name / strain rows)"
        print(f"{head}")
        print(f"  GTDB taxon   : {g['gtdb_taxon']}{flag}")
        print(f"  GTDB CURIE   : {g['gtdb_id']}")
        print(f"  GTDB lineage : {g['gtdb_lineage']}")
        print(f"  majority     : {g['majority_fraction']}{via}")
        if args.emit_yaml:
            print("  --- gtdb_classification block ---")
            for line in emit_block(g, mapping_source).splitlines():
                print(f"  {line}")
    print(f"\n[gtdb] grounded {n_ok}/{len(targets)} taxa", file=sys.stderr)
    return 0 if n_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
