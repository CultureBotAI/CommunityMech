#!/usr/bin/env python3
"""Ground CommunityMech taxa in GTDB using the local kg-microbe NCBI<->GTDB mapping.

For a taxon grounded in NCBITaxon, look up its GTDB (Genome Taxonomy Database)
classification — GTDB CURIE, taxon name, lineage, and mapping confidence — from
kg-microbe's ``data/raw/NCBI2GTDB.tsv.gz`` (no network). Works at the rank of the
input:

* species (binomial label) -> ``GTDB:s__...`` via exact NCBI id, else NCBI
  species-name fallback (the mapping is strain/genome-keyed, so species ids often
  miss on id alone). When GTDB splits one NCBI species into several, report
  AMBIGUOUS rather than guessing.
* genus / family / order / ... (single-name label) -> ``GTDB:g__...`` (or
  ``f__``/``o__``/...): aggregate the GTDB rank column over all genomes under the
  NCBI taxon; ground to the GTDB taxon holding a majority (>=50%) of genomes, else
  report AMBIGUOUS (e.g. NCBI genus Bacillus shatters into ~100 GTDB genera).

GTDB frequently reclassifies relative to NCBI (e.g. NCBITaxon "Agrobacterium
deltae" -> GTDB "Agrobacterium leguminum"); ``is_reclassified`` flags it.

Data source (local kg-microbe checkout): ``<kg-microbe>/data/raw/NCBI2GTDB.tsv.gz``.
Resolution order for <kg-microbe>: --kg-microbe-dir, $KG_MICROBE_DIR, then
../../kg-microbe relative to this repo.

GTDB CURIE scheme (kg-microbe / Bioregistry): rank prefix + name with spaces as
underscores, e.g. "s__Bacillus velezensis" -> "GTDB:s__Bacillus_velezensis";
resolvable at https://gtdb.ecogenomic.org/tree?r={id}.

Usage:
    uv run python scripts/gtdb_ground.py --ncbi-id NCBITaxon:492670 --emit-yaml
    uv run python scripts/gtdb_ground.py --name "Bacillus velezensis"
    uv run python scripts/gtdb_ground.py --community kb/communities/Foo.yaml --emit-yaml
    uv run python scripts/gtdb_ground.py --community kb/communities/Foo.yaml --apply
"""

from __future__ import annotations

import argparse
import gzip
import os
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
MAPPING_REL = Path("data/raw/NCBI2GTDB.tsv.gz")

# NCBI2GTDB.tsv column indices (0-based); see header row.
COL_NCBI_ID = 0
COL_TOTAL_GENOMES = 2
COL_MAJORITY = 3
COL_NCBI_SPECIES = 10
COL_GTDB_SPECIES = 18
# (ncbi_col, gtdb_col, rank_prefix) for higher ranks, finest -> coarsest.
HIGHER_RANKS = [(9, 17, "g"), (8, 16, "f"), (7, 15, "o"), (6, 14, "c"), (5, 13, "p")]
# GTDB lineage columns (col, prefix), domain..species.
GTDB_RANK_COLS = [(12, "d"), (13, "p"), (14, "c"), (15, "o"), (16, "f"), (17, "g"), (18, "s")]


def resolve_kg_microbe_dir(explicit: str | None) -> Path:
    candidates = []
    if explicit:
        candidates.append(Path(explicit))
    if os.environ.get("KG_MICROBE_DIR"):
        candidates.append(Path(os.environ["KG_MICROBE_DIR"]))
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


def _curie(name: str, prefix: str) -> str:
    return f"GTDB:{prefix}__" + name.replace(" ", "_")


def _lineage(cells: list[str], last_gtdb_col: int) -> str:
    parts = []
    for col, pfx in GTDB_RANK_COLS:
        if col > last_gtdb_col:
            break
        v = cells[col].strip()
        if v:
            parts.append(f"{pfx}__{v}")
    return ";".join(parts)


def _maj(c: list[str]) -> float:
    try:
        return float(c[COL_MAJORITY])
    except (ValueError, IndexError):
        return 0.0


def _clean_label(label: str | None) -> str:
    """Strip NCBITaxon disambiguators (<...>) and a leading 'Candidatus'."""
    s = re.sub(r"<[^>]*>", "", label or "").strip()
    s = re.sub(r"^Candidatus\s+", "", s).strip()
    return s


def _is_species(clean: str) -> bool:
    """Binomial heuristic: >=2 tokens with a lowercase second token (species epithet)."""
    toks = clean.split()
    return len(toks) >= 2 and toks[1][:1].islower()


def collect_rows(mapping_path: Path, want_ids, want_species_lc, want_higher_lc):
    """One pass; index rows by NCBI id, NCBI species name, and higher-rank NCBI name."""
    by_id: dict[str, list] = {}
    by_name: dict[str, list] = {}
    by_higher: dict[str, list] = {}
    with gzip.open(mapping_path, "rt") as fh:
        next(fh)
        for line in fh:
            cells = line.rstrip("\n").split("\t")
            if len(cells) <= COL_GTDB_SPECIES:
                continue
            nid = cells[COL_NCBI_ID].strip()
            if nid in want_ids:
                by_id.setdefault(nid, []).append(cells)
            sp = cells[COL_NCBI_SPECIES].strip().lower()
            if sp and sp in want_species_lc:
                by_name.setdefault(sp, []).append(cells)
            if want_higher_lc:
                for ncbi_col, _, _ in HIGHER_RANKS:
                    v = cells[ncbi_col].strip().lower()
                    if v and v in want_higher_lc:
                        by_higher.setdefault(v, []).append(cells)
                        break
    return by_id, by_name, by_higher


def _ground_species(rows, source_id, label, via):
    rows = sorted(rows, key=_maj, reverse=True)
    top = rows[0]
    sp = top[COL_GTDB_SPECIES].strip()
    ref = _clean_label(label) or top[COL_NCBI_SPECIES].strip()
    return {
        "ncbi_source_id": source_id,
        "gtdb_id": _curie(sp, "s") if sp else None,
        "gtdb_taxon": sp or None,
        "gtdb_lineage": _lineage(top, COL_GTDB_SPECIES),
        "majority_fraction": _maj(top),
        "is_reclassified": bool(sp and ref and sp != ref),
        "via": via,
    }


def resolve_higher(clean_lc, source_id, label, by_higher):
    """Ground a genus/family/... input to the majority GTDB taxon at that rank."""
    rows = by_higher.get(clean_lc)
    if not rows:
        return None
    for ncbi_col, gtdb_col, prefix in HIGHER_RANKS:
        matched = [r for r in rows if r[ncbi_col].strip().lower() == clean_lc]
        if not matched:
            continue
        weights: dict[str, float] = defaultdict(float)
        rep: dict[str, list] = {}
        for r in matched:
            gv = r[gtdb_col].strip()
            if not gv:
                continue
            try:
                w = float(r[COL_TOTAL_GENOMES])
            except (ValueError, IndexError):
                w = 1.0
            weights[gv] += w
            rep.setdefault(gv, r)
        if not weights:
            return None
        total = sum(weights.values())
        top, tw = max(weights.items(), key=lambda kv: kv[1])
        frac = tw / total
        if frac >= 0.5:
            return {
                "ncbi_source_id": source_id,
                "gtdb_id": _curie(top, prefix),
                "gtdb_taxon": top,
                "gtdb_lineage": _lineage(rep[top], gtdb_col),
                "majority_fraction": round(frac, 3),
                "is_reclassified": top != _clean_label(label),
                "via": f"ncbi_rank_{prefix}",
                "n_alt": len(weights),
            }
        ranked = [k for k, _ in sorted(weights.items(), key=lambda kv: -kv[1])]
        return {
            "ambiguous": True,
            "via": f"ncbi_rank_{prefix}",
            "ncbi_source_id": source_id,
            "ncbi_species": label,
            "gtdb_options": ranked[:8],
            "n_alt": len(weights),
        }
    return None


def resolve_target(ncbi_id, label, by_id, by_name, by_higher):
    """Species: id then name (split-aware). Genus/higher: majority GTDB rank taxon."""
    source_id = f"NCBITaxon:{ncbi_id}" if ncbi_id else None
    clean = _clean_label(label)
    if _is_species(clean):
        if ncbi_id and ncbi_id in by_id:
            return _ground_species(by_id[ncbi_id], source_id, label, "ncbi_id")
        nlc = clean.lower()
        if nlc in by_name:
            species: dict[str, list] = {}
            for c in by_name[nlc]:
                sp = c[COL_GTDB_SPECIES].strip()
                if sp:
                    species.setdefault(sp, []).append(c)
            if len(species) == 1:
                return _ground_species(next(iter(species.values())), source_id, label, "ncbi_name")
            if len(species) > 1:
                return {
                    "ambiguous": True,
                    "via": "ncbi_name",
                    "ncbi_source_id": source_id,
                    "ncbi_species": label,
                    "gtdb_options": sorted(species),
                    "n_alt": len(species),
                }
        return None
    return resolve_higher(clean.lower(), source_id, label, by_higher)


def _block(g: dict, mapping_source: str) -> dict:
    src = mapping_source
    if (g.get("via") or "").startswith("ncbi_rank"):
        rank = g["via"].split("_")[-1]
        src += f" [grounded at {rank}__ rank; {g.get('n_alt', 1)} GTDB taxa under the NCBI taxon]"
    elif g.get("via") == "ncbi_name":
        src += " [mapped via NCBI species name — no species-level NCBI id in table]"
    return {
        "gtdb_id": g["gtdb_id"],
        "gtdb_taxon": g["gtdb_taxon"],
        "gtdb_lineage": g["gtdb_lineage"],
        "ncbi_source_id": g["ncbi_source_id"],
        "majority_fraction": g["majority_fraction"],
        "is_reclassified": g["is_reclassified"],
        "mapping_source": src,
    }


def emit_block(g: dict, mapping_source: str) -> str:
    d = {"gtdb_classification": _block(g, mapping_source)}
    return yaml.dump(d, default_flow_style=False, sort_keys=False, allow_unicode=True, width=100)


def community_taxa(path: Path):
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


def apply_to_community(path: Path, by_id, by_name, by_higher, mapping_source) -> int:
    """Insert gtdb_classification into taxonomy taxon_terms via line-level text edits.

    Adds lines only (no YAML round-trip) so unrelated content — including plain
    scalar line-wrapping — is left byte-for-byte unchanged. Scoped to the
    top-level ``taxonomy:`` block so interaction source/target taxa are untouched.
    """
    doc = yaml.safe_load(path.read_text())
    blocks: dict[str, dict] = {}
    for tc in doc.get("taxonomy", []) or []:
        tt = (tc or {}).get("taxon_term", {}) or {}
        if "gtdb_classification" in tt:
            continue
        term = tt.get("term", {}) or {}
        tid = str(term.get("id", ""))
        if not tid.startswith("NCBITaxon:"):
            continue
        g = resolve_target(tid.split(":", 1)[1], term.get("label", ""), by_id, by_name, by_higher)
        if g and not g.get("ambiguous"):
            blocks[tid.split(":", 1)[1]] = _block(g, mapping_source)
    if not blocks:
        return 0

    lines = path.read_text().splitlines()
    start = end = None
    for idx, line in enumerate(lines):
        if re.match(r"^taxonomy:\s*$", line):
            start = idx
        elif start is not None and idx > start and re.match(r"^[A-Za-z_]", line):
            end = idx
            break
    if start is None:
        return 0
    end = end if end is not None else len(lines)

    out = lines[: start + 1]
    i, added = start + 1, 0
    while i < end:
        out.append(lines[i])
        m = re.match(r"^(\s+)id: (NCBITaxon:\d+)\s*$", lines[i])
        nid = m.group(2).split(":", 1)[1] if m else None
        if nid in blocks and i + 1 < end and re.match(r"^\s+label:", lines[i + 1]):
            out.append(lines[i + 1])  # keep the label line
            child = " " * (len(m.group(1)) - 2)  # taxon_term child indent (sibling of `term`)
            out.append(f"{child}gtdb_classification:")
            dumped = yaml.dump(blocks.pop(nid), sort_keys=False, allow_unicode=True, width=4096)
            out += [f"{child}  {bl}" for bl in dumped.splitlines()]
            added += 1
            i += 2
            continue
        i += 1
    out += lines[end:]
    path.write_text("\n".join(out) + "\n")
    return added


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument("--ncbi-id", action="append", help="NCBITaxon:NNN (repeatable).")
    src.add_argument("--name", action="append", help="NCBI taxon name (repeatable).")
    src.add_argument("--community", type=Path, help="Community YAML — ground all its taxa.")
    p.add_argument(
        "--kg-microbe-dir", help="kg-microbe checkout (else $KG_MICROBE_DIR / ../../kg-microbe)."
    )
    p.add_argument(
        "--emit-yaml", action="store_true", help="Print paste-ready gtdb_classification blocks."
    )
    p.add_argument(
        "--apply", action="store_true", help="With --community: write blocks into the file."
    )
    args = p.parse_args(argv)

    kg_dir = resolve_kg_microbe_dir(args.kg_microbe_dir)
    mapping_path = kg_dir / MAPPING_REL
    built = datetime.fromtimestamp(mapping_path.stat().st_mtime, tz=timezone.utc).date().isoformat()
    mapping_source = f"kg-microbe NCBI2GTDB.tsv.gz; GTDB release latest (built {built})"
    print(f"[gtdb] mapping: {mapping_path}  ({mapping_source})", file=sys.stderr)

    targets = []
    if args.community:
        targets = list(community_taxa(args.community))
        print(f"[gtdb] {args.community.name}: {len(targets)} NCBITaxon taxa", file=sys.stderr)
    if args.ncbi_id:
        targets += [(x.split(":", 1)[1] if ":" in x else x, None) for x in args.ncbi_id]
    if args.name:
        targets += [(None, n) for n in args.name]

    want_ids, want_species, want_higher = set(), set(), set()
    for ncbi_id, label in targets:
        clean = _clean_label(label)
        if _is_species(clean):
            if ncbi_id:
                want_ids.add(ncbi_id)
            want_species.add(clean.lower())
        elif clean:
            want_higher.add(clean.lower())
    by_id, by_name, by_higher = collect_rows(mapping_path, want_ids, want_species, want_higher)

    if args.community and args.apply:
        n = apply_to_community(args.community, by_id, by_name, by_higher, mapping_source)
        print(f"[gtdb] applied {n} block(s) to {args.community.name}", file=sys.stderr)
        return 0

    n_ok = 0
    for ncbi_id, label in targets:
        g = resolve_target(ncbi_id, label, by_id, by_name, by_higher)
        head = f"\nNCBITaxon:{ncbi_id}" if ncbi_id else f"\n{label}"
        if label and ncbi_id:
            head += f"  {label}"
        if g is None:
            print(head)
            print("  no GTDB mapping (rank absent from the NCBI2GTDB table, or eukaryote).")
            continue
        if g.get("ambiguous"):
            opts = ", ".join(g["gtdb_options"])
            extra = g.get("n_alt", 0) - len(g["gtdb_options"])
            if extra > 0:
                opts += f" (+{extra} more)"
            print(head)
            print(f"  ⚠ AMBIGUOUS — GTDB splits this taxon into: {opts}")
            print("  (no single grounding emitted; a curator should pick or leave ungrounded.)")
            continue
        n_ok += 1
        flag = "  ⚠ RECLASSIFIED" if g["is_reclassified"] else ""
        rank = g["via"].split("_")[-1]
        via = {"ncbi_id": "", "ncbi_name": "  (via species name)"}.get(
            g["via"], f"  (at {rank}__ rank)"
        )
        print(head)
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
