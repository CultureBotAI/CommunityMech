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
  ``f__``/``o__``/...): aggregate the GTDB rank column over the genomes under the
  NCBI taxon; ground to the GTDB taxon holding a majority (>=50%) of them, else
  report AMBIGUOUS (e.g. NCBI genus Bacillus shatters into ~100 GTDB genera).

  Since #372 that aggregation counts only rows naming an actual binomial —
  ``exclude_unnamed`` defaults to True, so ``sp.``/``uncultured``/informal rows
  are excluded (#375). It is a real change of denominator, not a tidy-up: it
  moved 219 of the KB's 647 stored fractions. A tie is broken by name, which
  makes it reproducible but still a tie (#382), and the block does not record how
  many genomes the fraction was computed from (#383).

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
COL_NCBI_STRAIN = 11
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
                # Index under *every* wanted rank this row matches, not just the
                # first. With a `break` here, a row carrying two wanted names —
                # say genus Methanosarcina inside phylum Methanobacteriota —
                # counted only toward whichever rank HIGHER_RANKS reached first,
                # so a taxon's row set depended on which *other* taxa shared the
                # run. Grounding the same id per-record and whole-KB could then
                # disagree (#366).
                seen = set()
                for ncbi_col, _, _ in HIGHER_RANKS:
                    v = cells[ncbi_col].strip().lower()
                    # `seen` guards the other direction: one row carrying the same
                    # name in two rank columns would otherwise be appended twice
                    # and double-weighted. No row does today, but that is a
                    # property of the data, not of the code.
                    if v and v in want_higher_lc and v not in seen:
                        seen.add(v)
                        by_higher.setdefault(v, []).append(cells)
    return by_id, by_name, by_higher


def _genomes(row) -> int:
    """The row's genome count, or 0 if the cell is missing or unparseable."""
    try:
        return int(float(row[COL_TOTAL_GENOMES]))
    except (ValueError, IndexError, TypeError):
        return 0


def _ground_species(rows, source_id, label, via):
    # Deterministic order. A plain `sorted(key=_maj)` is stable, so among rows
    # tied on majority the winner was whichever the crosswalk listed first —
    # reversing the file moved *Anaerobutyricum hallii* from 156 genomes to 1,
    # with the same gtdb_id and the same 1.0. That is the tie-break bug fixed for
    # the higher-rank path in #382, reappearing here (#385 review). Prefer the
    # best-supported row, then break by name.
    rows = sorted(rows, key=lambda r: (-_maj(r), -_genomes(r), r[COL_GTDB_SPECIES].strip()))
    top = rows[0]
    sp = top[COL_GTDB_SPECIES].strip()
    ref = _clean_label(label) or top[COL_NCBI_SPECIES].strip()
    # Column 2 is the chosen row's *total* genomes; `majority_fraction` is the
    # share of them reaching this GTDB taxon. So this path can state the
    # denominator exactly, and cannot state the numerator at all.
    #
    # Two wrong answers were tried before this one. Storing the column straight
    # into `support_genomes` labelled the denominator as the numerator and
    # overstated 74 of 335 species blocks — *P. aeruginosa* read 17191 against a
    # true ~17019 — hidden by a worked example where `majority_fraction: 1.0`
    # makes the two identical (#385 review). Deriving it as `round(total * maj)`
    # is no better: the crosswalk's majority column carries **two decimal
    # places**, so at 17191 genomes and 0.99 the true numerator spans ~170
    # genomes, and a 5-digit `support_genomes` would assert a precision the
    # source does not have.
    #
    # So species blocks carry `total_genomes` only. That is what #383 asked for —
    # what the fraction is a fraction *of* — and `support_genomes` keeps one
    # meaning everywhere: an exact count this script computed itself.
    #
    # Aggregate across *every* row reaching the same GTDB species, not just the
    # chosen one (#386). A species name usually spans several crosswalk rows —
    # different NCBI strain taxonIDs under one name — and reading a single row
    # threw the rest away: *Bifidobacterium breve* reported 3 genomes where 25
    # rows totalling 1593 all map to `s__Bifidobacterium_breve`.
    #
    # The fraction is then the genome-weighted mean over those rows, because
    # each carries its own. Keeping the chosen row's fraction beside a summed
    # denominator would be incoherent — B. breve's rows are 1544 genomes at 0.99
    # and 49 at 1.0, so "1.0 of 1593" is a claim no row makes.
    #
    # This cannot change a grounding, and the reason is structural rather than a
    # property of today's KB: `sp` is read off `top` *before* `agreeing` is
    # built, so the filter can only ever narrow the rows behind an already-chosen
    # species. `resolve_target` also reports AMBIGUOUS whenever a name group
    # holds more than one GTDB species, so the mixed case does not arise from the
    # public entry point at all — the filter is defensive, and the synthetic
    # split in the tests is the only thing that exercises it.
    #
    # It moves 39 denominators (36 alone, 3 alongside a fraction) and 3 fractions.
    #
    # Only the **name** path aggregates. An NCBI id maps to exactly one crosswalk
    # row, so an id-path grounding still reports that row alone — which leaves
    # the understatement #386 was filed about in place on more blocks than this
    # fixes. Extending it means summing across NCBI depths, where a species-rank
    # row and its strain rows would double-count: 96 of the KB's species mix the
    # two. That is #371's question, and it is tracked separately (#389).
    agreeing = [r for r in rows if r[COL_GTDB_SPECIES].strip() == sp] if sp else []
    total = sum(_genomes(r) for r in agreeing)
    if total:
        fraction = round(sum(_genomes(r) * _maj(r) for r in agreeing) / total, 3)
    else:
        # No GTDB species cell, or every agreeing row carries no genome count.
        # An earlier comment here claimed this "degrades to its pre-#386
        # behaviour rather than to zero" — wrong on both counts: `top` is itself
        # in `agreeing`, so an empty total means `_genomes(top)` is 0 too, and
        # emitting `total_genomes: 0` would then fail the `minimum_value: 1` this
        # PR adds (#388 review). Publish no count rather than a meaningless one.
        total, fraction = _genomes(top) or None, _maj(top)
    return {
        "ncbi_source_id": source_id,
        "gtdb_id": _curie(sp, "s") if sp else None,
        "gtdb_taxon": sp or None,
        "gtdb_lineage": _lineage(top, COL_GTDB_SPECIES),
        "majority_fraction": fraction,
        "total_genomes": total,
        "is_reclassified": bool(sp and ref and sp != ref),
        "via": via,
    }


# NCBI species strings that name no species: metagenome bins, informal lineages
# and explicit placeholders. `Candidatus` is deliberately absent — a Candidatus
# name is a provisional *species* name for an uncultivated organism, not a
# placeholder, and excluding it would discard legitimate taxonomy.
# Measured over all 92711 crosswalk rows. Three of the original alternations
# under-matched because `\b` anchors the *start* of a compound word:
#   `\bsymbiont\b`  missed `endosymbiont`      -> 331 rows survived as binomials
#   `\bsp\.`         missed `genomosp.`         -> 72 rows
#   `\bbacterium\b` missed `proteobacterium`   -> 94 rows
# Allowing a preceding word-part fixes all three. `metagenome` and `unclassified`
# match nothing in this table today; both are kept as cheap forward guards.
UNNAMED_SPECIES = re.compile(
    # `\b` anchors the start of a compound word, so the original alternations
    # under-matched: `symbiont` missed `endosymbiont` (331 rows survived as if
    # binomial), `bacterium` missed `proteobacterium` (94), `sp.` missed
    # `genomosp.` (72). Measured over all 92711 crosswalk rows.
    #
    # The compound forms must stay **case-sensitive and lowercase-only**, hence
    # the scoped `(?-i:)`. An informal descriptor is lowercase (`gamma
    # proteobacterium`, `Wolbachia endosymbiont of ...`); a genus that merely
    # ends in the same letters is capitalised, and dropping those would discard
    # 1700+ real binomials — *Acetobacterium woodii*, *Acidipropionibacterium
    # jensenii*. `genomosp.` is listed explicitly rather than as `\w*sp\.`,
    # which would also swallow the legitimate `subsp.`.
    r"\bsp\.|\bgenomosp\."
    r"|(?-i:\b[a-z]*(?:bacterium|archaeon|symbiont|metagenome)\b)"
    r"|^(?:uncultured|unclassified|unidentified)\b",
    re.IGNORECASE,
)


def named_species_only(matched: list) -> list:
    """Drop rows whose NCBI species is not an actual binomial.

    Half the crosswalk is unbinomialed — 33.7% `sp.`, 10.9% informal
    (`Firmicutes bacterium CAG:176`), 5.2% placeholder-prefixed. Those rows carry
    genome counts like any other, so a heavily-binned MAG lineage can outvote the
    cultivated species that share the NCBI taxon.

    `Acetobacter` is the worked case: `g__CAG-267` draws its entire 338-genome
    support from two `sp.` rows, and wins under the `deepest` denominator. With
    this filter, all 257 binomial Acetobacter genomes map to `g__Acetobacter` and
    both denominators agree (#375).

    **On by default** as of #372, but not uniformly better: it turns `Serratia`
    from a type-anchored answer into AMBIGUOUS, and it does not make the two
    denominators agree in general. It also shrinks the evidence behind a
    grounding without recording that it did — `majority_fraction` reads the same
    at 4 genomes as at 4000, which is #383. See reports/gtdb_denominators.tsv for
    the current scenario counts rather than a number quoted here, which rots.
    """
    return [r for r in matched if r[COL_NCBI_SPECIES].strip()
            and not UNNAMED_SPECIES.search(r[COL_NCBI_SPECIES].strip())]


def deepest_only(matched: list) -> list:
    """Keep one depth per lineage: strain rows where a lineage has any, else its species row.

    `NCBI2GTDB.tsv.gz` is an upstream crosswalk (Bork group / metatraits) in which
    every row is an independent NCBI->GTDB assignment carrying its own genome
    support. Summing across depths therefore aggregates evidence rather than
    double-counting a ledger — a genome legitimately supports its strain's
    assignment and its species' — but it weights deeply sequenced lineages more
    heavily. Over all 92711 rows the supports total 1.84M against ~600k genomes
    in a release.

    This is the alternative denominator: one row per lineage, at the deepest
    depth available. It mirrors the rule kg-microbe-paper settled on for the same
    shape of problem ("deepest available level, one level only, per parent").

    The leaf case is handled first and deliberately: a row that is itself a
    strain with no species is kept as its own lineage. In the prior art, the
    equivalent branch looked up a leaf as if it were a parent, found nothing, and
    silently dropped the taxon.

    Note this is *not* provably the correct denominator. Containment does not
    hold in this table: of the 2827 species carrying both a species row and
    strain rows, 1363 have strain supports exceeding the species row — e.g.
    Agathobacter rectalis, 418 genomes at the species node against 13850 at its
    type strain. See #371.
    """
    lineages: dict[str, dict[str, list]] = {}
    for row in matched:
        species = row[COL_NCBI_SPECIES].strip().lower()
        strain = row[COL_NCBI_STRAIN].strip()
        # A strain row with no species names its own lineage; without this it
        # would pool under "" with every other speciesless strain and lose to
        # whichever the sort happened to favour. Rows with neither share one
        # lineage, which is harmless: with no strain bucket to prefer, every one
        # of them is kept regardless.
        key = species or strain.lower()
        lineages.setdefault(key, {"strain": [], "species": []})
        lineages[key]["strain" if strain else "species"].append(row)

    kept = []
    for group in lineages.values():
        kept.extend(group["strain"] or group["species"])
    return kept


def resolve_higher(clean_lc, source_id, label, by_higher, denominator="aggregate",
                   exclude_unnamed=True):
    """Ground a genus/family/... input to the majority GTDB taxon at that rank.

    `denominator` selects how genome support is summed: "aggregate" (the default)
    sums every matched row; "deepest" keeps one row per lineage. See `deepest_only`
    and #371 — that choice is published in reports/gtdb_denominators.tsv rather
    than argued here.

    `exclude_unnamed` is the orthogonal axis and defaults to **True** (#375): rows
    whose NCBI species is not a binomial are dropped before the count. Pass False
    for the pre-#372 behaviour. Note the two interact — with the filter on, every
    blank-species row is gone before `deepest_only` ever sees it.
    """
    # Validate before any early return. This used to sit inside the rank loop, so
    # a typo'd denominator returned None instead of raising whenever the taxon had
    # no rows or no rank matched (#372 review).
    if denominator not in ("aggregate", "deepest"):
        raise ValueError(f"unknown denominator {denominator!r}; expected 'aggregate' or 'deepest'")
    rows = by_higher.get(clean_lc)
    if not rows:
        return None
    for ncbi_col, gtdb_col, prefix in HIGHER_RANKS:
        matched = [r for r in rows if r[ncbi_col].strip().lower() == clean_lc]
        if not matched:
            continue
        if exclude_unnamed:
            filtered = named_species_only(matched)
            # Never let the filter empty a taxon out entirely: a genus known only
            # from MAG bins would otherwise go from a grounding to nothing.
            if filtered:
                matched = filtered
        if denominator == "deepest":
            matched = deepest_only(matched)
        weights: dict[str, float] = defaultdict(float)
        rep: dict[str, list] = {}
        for r in matched:
            gv = r[gtdb_col].strip()
            if not gv:
                continue
            try:
                w = float(r[COL_TOTAL_GENOMES])
            except (ValueError, IndexError, TypeError):
                # TypeError guards a None cell. Rows come from splitting a TSV so
                # every cell is a string today, but this fell over in testing and
                # a crash mid-sweep is a worse failure than a weight of 1.
                w = 1.0
            weights[gv] += w
            rep.setdefault(gv, r)
        if not weights:
            return None
        total = sum(weights.values())
        # Break ties by name, not by row order. `max` returns the first maximum,
        # which for an exact tie is whichever row the mapping happened to list
        # first — reversing the input flipped Ensifer/Sinorhizobium (both at 0.5).
        # Whether a 50/50 split should ground *at all* is a separate question
        # (#382); this only makes the answer reproducible.
        top, tw = sorted(weights.items(), key=lambda kv: (-kv[1], kv[0]))[0]
        frac = tw / total
        if frac >= 0.5:
            return {
                "ncbi_source_id": source_id,
                "gtdb_id": _curie(top, prefix),
                "gtdb_taxon": top,
                "gtdb_lineage": _lineage(rep[top], gtdb_col),
                "majority_fraction": round(frac, 3),
                # The numerator and denominator the fraction came from (#383).
                # `frac` is rounded to 3 places, so these cannot be recovered
                # from it — 4/7 and 4000/7000 both store as 0.571.
                "support_genomes": int(tw),
                "total_genomes": int(total),
                "is_reclassified": top != _clean_label(label),
                "via": f"ncbi_rank_{prefix}",
                "n_alt": len(weights),
            }
        # Same tie-break as `top` above: ties here were still row-ordered, so the
        # AMBIGUOUS option list a curator reads was not reproducible (#382 review).
        ranked = [k for k, _ in sorted(weights.items(), key=lambda kv: (-kv[1], kv[0]))]
        return {
            "ambiguous": True,
            "via": f"ncbi_rank_{prefix}",
            "ncbi_source_id": source_id,
            "ncbi_species": label,
            "gtdb_options": ranked[:8],
            "n_alt": len(weights),
        }
    return None


def resolve_target(ncbi_id, label, by_id, by_name, by_higher, denominator="aggregate",
                   exclude_unnamed=True):
    """Species: id then name (split-aware). Genus/higher: majority GTDB rank taxon.

    `denominator` is forwarded to `resolve_higher`; the species and id paths
    resolve a single row and are identical under either choice (#371).
    """
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
    return resolve_higher(clean.lower(), source_id, label, by_higher, denominator, exclude_unnamed)


# Groundings a curator chose against the majority vote, keyed by
# (record filename, NCBITaxon id). `--refresh` recomputes an existing block, so
# without this the tool silently replaces a right answer with a confidently wrong
# one and only `tests/test_gtdb_withheld_groundings.py::CURATED` notices, after
# the fact. Mirrors WITHHELD, which keeps taxa *ungrounded* (#292/#293).
#
# This is the narrow half of #384 — a hard-coded list, not the `curated:` flag on
# the block that the issue asks for. It exists so the record stays tool-
# maintainable: excluding the whole *file* instead stranded its other taxon.
CURATED_GROUNDINGS = {
    ("Dehalococcoides_Pelobacter_Acetylene_TCE_Coculture.yaml", "NCBITaxon:18"): (
        "GTDB:g__Syntrophotalea — SFB93 is an acetylene fermenter and the entry's "
        "notes tie it to Syntrophotalea acetylenivorans, but every Pelobacter row "
        "naming Syntrophotalea is an `sp.` row, so the named-species filter hands "
        "the vote to g__Seleniibacterium at 0.571 (#384)."
    ),
}


def _block(g: dict, mapping_source: str) -> dict:
    src = mapping_source
    if (g.get("via") or "").startswith("ncbi_rank"):
        rank = g["via"].split("_")[-1]
        src += f" [grounded at {rank}__ rank; {g.get('n_alt', 1)} GTDB taxa under the NCBI taxon]"
    elif g.get("via") == "ncbi_name":
        src += " [mapped via NCBI species name — no species-level NCBI id in table]"
    block = {
        "gtdb_id": g["gtdb_id"],
        "gtdb_taxon": g["gtdb_taxon"],
        "gtdb_lineage": g["gtdb_lineage"],
        "ncbi_source_id": g["ncbi_source_id"],
        "majority_fraction": g["majority_fraction"],
        "support_genomes": g.get("support_genomes"),
        "total_genomes": g.get("total_genomes"),
        "is_reclassified": g["is_reclassified"],
        "mapping_source": src,
    }
    # Omit the counts when absent rather than writing `total_genomes: null`. The
    # species path computes no denominator, so a null would appear on 335 blocks
    # as pure noise — and it hides from a naive diff, since `.get()` returns None
    # for both an absent key and a null one. Only these two are dropped: the
    # older fields have always been written even when empty, and silently
    # changing that would be a second, unrelated migration.
    for key in ("support_genomes", "total_genomes"):
        if block[key] is None:
            del block[key]
    return block


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


def _block_span(lines: list[str], anchor: int, end: int) -> tuple[int, int] | None:
    """Line span of the gtdb_classification block belonging to one taxonomy entry.

    Starts at the entry's `id:` anchor and stops at the next line indented no
    deeper than the block key, so a sibling (`notes`, `functional_role`) or the
    next entry ends the search. Returns None when the entry has no block.
    """
    key = re.compile(r"^\s{4}gtdb_classification:\s*$")
    i = anchor + 1
    while i < end:
        if key.match(lines[i]):
            j = i + 1
            # Indent >= 6, not exactly 6. PyYAML wraps long scalars onto
            # continuation lines indented deeper, so an exact match stopped one
            # line short and left orphans that became duplicate keys in 13
            # records (#378 review).
            while j < end and re.match(r"^\s{6,}\S", lines[j]):
                j += 1
            return (i, j)
        # Any line at the taxon_term level or shallower ends this entry.
        if re.match(r"^\s{0,4}\S", lines[i]) and not re.match(r"^\s{4}\S", lines[i]):
            return None
        if re.match(r"^- ", lines[i]):
            return None
        i += 1
    return None


STATUS_KEYS = ("gtdb_grounding_status", "gtdb_candidates")


def classify_status(
    record_name, tid, label, has_block, by_id, by_name, by_higher, preferred=None, **kwargs
):
    """Why this taxon does or does not carry a grounding (#294).

    Returns (status, candidates). The tool already distinguished all of these
    internally — it prints a block, `AMBIGUOUS`, or `no GTDB mapping` — so this
    persists a decision rather than making a new one.

    Order matters. WITHHELD is checked before anything is computed, because the
    point of a withhold is that the tool *can* produce a grounding and must not:
    classifying it by outcome would label it GROUNDED-able and invite exactly the
    re-run #293 exists to prevent.
    """
    if (record_name, tid) in CURATED_GROUNDINGS:
        # A curated block is a grounding, just not one the tool would compute.
        return ("GROUNDED" if has_block else "WITHHELD"), []
    # Keyed by preferred_term, NOT by NCBITaxon id. Both withheld records use
    # the offending id *correctly* elsewhere — BioModels uses 821 for its real
    # Bacteroides vulgatus entry, KBase uses 1236 for two Steroidobacteraceae —
    # so an id key marked three sound groundings WITHHELD. Same collision that
    # `apply_to_community` carries a comment about; caught here by the
    # status-vs-block coherence check.
    if (record_name, preferred) in WITHHELD_GROUNDINGS:
        return "WITHHELD", []
    if has_block:
        return "GROUNDED", []
    if not tid.startswith("NCBITaxon:"):
        return "NO_GTDB_EQUIVALENT", []
    result = resolve_target(tid.split(":", 1)[1], label, by_id, by_name, by_higher, **kwargs)
    if result and result.get("ambiguous"):
        return "AMBIGUOUS", list(result.get("gtdb_options") or [])
    if result is None or not result.get("gtdb_id"):
        return "NO_GTDB_EQUIVALENT", []
    # The tool would ground this and the KB does not. That is the only value
    # here that represents outstanding work.
    return "NOT_ATTEMPTED", []


# Taxa kept ungrounded on purpose because the NCBITaxon id names a different
# organism, so a derived block would describe the wrong species convincingly.
# Mirrors CURATED_GROUNDINGS, which protects a grounding that *is* right.
# Kept in step with WITHHELD in tests/test_gtdb_withheld_groundings.py (#292).
WITHHELD_GROUNDINGS = {
    ("BioModels_MODEL2405300001_Infant_Gut_HMO_SynCom.yaml", "Bacteroides ovatus"): (
        "NCBITaxon:821 is Phocaeicola vulgatus; B. ovatus is NCBITaxon:28116."
    ),
    ("KBase_ORT_Workflow_Community_Model.yaml", "Nitrospiraceae bacterium"): (
        "NCBITaxon:1236 is class Gammaproteobacteria, not a Nitrospiraceae bacterium."
    ),
}


def _status_spans(lines: list[str], anchor: int, end: int) -> list[tuple[int, int]]:
    """Line spans of any existing status keys for one taxonomy entry.

    Same shape as `_block_span`, and deliberately the same indent rule: `>= 6`
    rather than exactly 6, because `gtdb_candidates` is a list whose items sit
    deeper and an exact match would orphan them into duplicate keys (#378).
    """
    keys = re.compile(r"^\s{4}(?:" + "|".join(STATUS_KEYS) + r"):")
    # A block sequence is written at the *same* indent as its key, so
    # `gtdb_candidates:` is followed by `    - Anabaena`, not by a deeper line.
    # Matching only `\s{6,}` left those items outside the span: the key was
    # replaced and the items survived, so a second `--apply-status` run appended
    # a duplicate list under one key. Caught by the canary before any batch, but
    # this is the same class of bug as #378's wrapped continuations.
    item = re.compile(r"^\s{4}- ")
    spans, i = [], anchor + 1
    while i < end:
        if keys.match(lines[i]):
            j = i + 1
            while j < end and (re.match(r"^\s{6,}\S", lines[j]) or item.match(lines[j])):
                j += 1
            spans.append((i, j))
            i = j
            continue
        if re.match(r"^\s{0,4}\S", lines[i]) and not re.match(r"^\s{4}\S", lines[i]):
            break
        if re.match(r"^- ", lines[i]):
            break
        i += 1
    return spans


def apply_to_community(
    path: Path,
    by_id,
    by_name,
    by_higher,
    mapping_source,
    refresh: bool = False,
    denominator: str = "aggregate",
    exclude_unnamed: bool = True,
) -> int:
    """Insert or refresh gtdb_classification in taxonomy taxon_terms, line-level.

    Adds lines only (no YAML round-trip) so unrelated content — including plain
    scalar line-wrapping — is left byte-for-byte unchanged. Scoped to the
    top-level ``taxonomy:`` block so interaction source/target taxa are untouched.

    `refresh` recomputes blocks that already exist and **creates none**. That
    asymmetry is the point: an ungrounded taxon may be ungrounded deliberately —
    the entries withheld under #292 are — so a refresh that also grounded them
    would silently overturn a curation decision (#378).
    """
    doc = yaml.safe_load(path.read_text())
    entries = doc.get("taxonomy", []) or []

    # Positional, NOT keyed by NCBITaxon id. A record may legitimately list the
    # same id many times — GLBRC_Populus_Variovorax_SynCom28 has 28 isolates all
    # grounded to NCBITaxon:34072 (genus Variovorax). Keying by id inserted the
    # block at the *first* line bearing that id, which is a different taxonomy
    # entry than the one that needed it: the already-grounded entry got a
    # duplicate `gtdb_classification` key while the ungrounded ones stayed
    # ungrounded. PyYAML keeps the last of two duplicate keys silently, so
    # linkml-validate did not catch it either.
    wanted: list[dict | None] = []
    for tc in entries:
        tt = (tc or {}).get("taxon_term", {}) or {}
        term = tt.get("term", {}) or {}
        tid = str(term.get("id", ""))
        grounded = "gtdb_classification" in tt
        if (path.name, tid) in CURATED_GROUNDINGS:
            print(
                f"[gtdb] skipping curated {tid} in {path.name}: "
                f"{CURATED_GROUNDINGS[(path.name, tid)]}",
                file=sys.stderr,
            )
            wanted.append(None)
            continue
        if not tid.startswith("NCBITaxon:") or (grounded != refresh):
            # normal: act on ungrounded only. refresh: act on grounded only.
            wanted.append(None)
            continue
        g = resolve_target(
            tid.split(":", 1)[1],
            term.get("label", ""),
            by_id,
            by_name,
            by_higher,
            denominator=denominator,
            exclude_unnamed=exclude_unnamed,
        )
        # A result with no gtdb_id is not a grounding: `_ground_species` returns
        # one when the GTDB species cell is empty. Writing it replaced a curated
        # `g__Chlorobium` with nulls on refresh, so treat it as ungroundable and
        # leave whatever is there alone (#378 review).
        usable = g and not g.get("ambiguous") and g.get("gtdb_id")
        wanted.append(_block(g, mapping_source) if usable else None)
    if not any(w is not None for w in wanted):
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

    # One `id: NCBITaxon:… / label: …` pair per taxonomy entry, in document
    # order. If that correspondence does not hold the file is shaped in a way
    # this text-level editor cannot reason about, so refuse rather than guess —
    # a wrong insertion point is silent data corruption.
    anchors = [
        i
        for i in range(start + 1, end)
        if re.match(r"^\s+id: NCBITaxon:\d+\s*$", lines[i])
        and i + 1 < end
        and re.match(r"^\s+label:", lines[i + 1])
    ]
    if len(anchors) != len(entries):
        raise SystemExit(
            f"{path.name}: found {len(anchors)} taxon term-id lines for "
            f"{len(entries)} taxonomy entries — refusing to edit."
        )
    for pos, tc in zip(anchors, entries, strict=True):
        expected = str((((tc or {}).get("taxon_term") or {}).get("term") or {}).get("id", ""))
        if lines[pos].split("id:", 1)[1].strip() != expected:
            raise SystemExit(
                f"{path.name}: taxonomy entry order does not match the file — refusing to edit."
            )

    insert_at = {pos: block for pos, block in zip(anchors, wanted, strict=True) if block}
    # Where each refreshed entry's existing block lives, so it is removed rather
    # than duplicated. PyYAML keeps the last of two identical keys silently, so a
    # duplicate would survive linkml-validate unnoticed (#289).
    spans = {pos: _block_span(lines, pos, end) for pos in insert_at} if refresh else {}

    out = lines[: start + 1]
    i, added = start + 1, 0
    while i < end:
        out.append(lines[i])
        block = insert_at.get(i)
        if block is not None:
            out.append(lines[i + 1])  # keep the label line
            span = spans.get(i)
            if span:
                out += lines[i + 2 : span[0]]  # siblings written before the block
            indent = re.match(r"^(\s+)", lines[i]).group(1)
            child = " " * (len(indent) - 2)  # taxon_term child indent (sibling of `term`)
            out.append(f"{child}gtdb_classification:")
            dumped = yaml.dump(block, sort_keys=False, allow_unicode=True, width=4096)
            out += [f"{child}  {bl}" for bl in dumped.splitlines()]
            added += 1
            nxt = span[1] if span else i + 2
            if nxt <= i:
                raise SystemExit(f"{path.name}: computed a non-advancing block span.")
            i = nxt
            continue
        i += 1
    out += lines[end:]
    new_text = "\n".join(out) + "\n"

    # Refuse to write anything that changed more than the grounding blocks. Four
    # hand-rolled attempts at this edit corrupted records — deleting a sibling
    # `evidence` list, joining two lines, emitting duplicate keys — and every one
    # was caught only by looking afterwards. Checking before the write turns that
    # class of mistake into a refusal (#378).
    _assert_only_grounding_changed(path, doc, new_text, refresh=refresh)

    path.write_text(new_text)
    return added


def apply_status_to_community(path: Path, by_id, by_name, by_higher, **kwargs) -> int:
    """Write `gtdb_grounding_status` (and `gtdb_candidates`) on every taxon (#294).

    Same line-level, add-only approach as `apply_to_community`, and deliberately
    the same refusals: the entry count must match the anchors and the ids must
    line up, or this raises rather than guessing an insertion point.

    Status is written for **every** taxonomy entry, including grounded ones, even
    though GROUNDED is derivable from the block's presence. Deriving state from
    whether a field exists is the defect #294 is about; a consumer should read a
    value.
    """
    doc = yaml.safe_load(path.read_text())
    entries = doc.get("taxonomy", []) or []

    wanted: list[tuple[str, list[str]] | None] = []
    for tc in entries:
        tt = (tc or {}).get("taxon_term", {}) or {}
        term = tt.get("term", {}) or {}
        tid = str(term.get("id", ""))
        status, candidates = classify_status(
            path.name,
            tid,
            term.get("label", ""),
            "gtdb_classification" in tt,
            by_id,
            by_name,
            by_higher,
            preferred=tt.get("preferred_term"),
            **kwargs,
        )
        wanted.append((status, candidates))

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

    anchors = [
        i
        for i in range(start + 1, end)
        if re.match(r"^\s+id: NCBITaxon:\d+\s*$", lines[i])
        and i + 1 < end
        and re.match(r"^\s+label:", lines[i + 1])
    ]
    # Entries whose term id is not an NCBITaxon CURIE have no anchor line, so a
    # mismatch here is expected rather than corruption — but it means this
    # editor cannot place their status, and writing the others would silently
    # leave gaps. Refuse the file instead.
    if len(anchors) != len(entries):
        raise SystemExit(
            f"{path.name}: found {len(anchors)} taxon term-id lines for "
            f"{len(entries)} taxonomy entries — refusing to edit."
        )
    for pos, tc in zip(anchors, entries, strict=True):
        expected = str((((tc or {}).get("taxon_term") or {}).get("term") or {}).get("id", ""))
        if lines[pos].split("id:", 1)[1].strip() != expected:
            raise SystemExit(
                f"{path.name}: taxonomy entry order does not match the file — refusing to edit."
            )

    spans = {pos: _status_spans(lines, pos, end) for pos in anchors}
    by_anchor = dict(zip(anchors, wanted, strict=True))

    out = lines[: start + 1]
    i, written = start + 1, 0
    while i < end:
        out.append(lines[i])
        if i in by_anchor:
            status, candidates = by_anchor[i]
            out.append(lines[i + 1])  # the label line
            drop = {n for span in spans[i] for n in range(*span)}
            indent = re.match(r"^(\s+)", lines[i]).group(1)
            child = " " * (len(indent) - 2)
            out.append(f"{child}gtdb_grounding_status: {status}")
            if candidates:
                out.append(f"{child}gtdb_candidates:")
                out += [f"{child}- {c}" for c in candidates]
            written += 1
            j = i + 2
            while j < end and j in drop:
                j += 1
            # Siblings written after the label but before the next entry keep
            # their order; only the old status keys are dropped.
            k = j
            while k < end and k not in drop and not re.match(r"^\s+id: NCBITaxon:\d+\s*$", lines[k]):
                k += 1
            out += [ln for n, ln in enumerate(lines[j:k], start=j) if n not in drop]
            i = k
            continue
        i += 1
    out += lines[end:]
    new_text = "\n".join(out) + "\n"

    _assert_only_status_changed(path, doc, new_text)
    path.write_text(new_text)
    return written


def _assert_only_status_changed(path: Path, before: dict, new_text: str) -> None:
    """Fail loudly unless the edit touched the status slots and nothing else."""
    try:
        after = yaml.safe_load(new_text)
    except yaml.YAMLError as exc:
        raise SystemExit(
            f"{path.name}: edit produced unparseable YAML — refusing to write: {exc}"
        ) from exc

    class _DupDetector(yaml.SafeLoader):
        pass

    def _no_dups(loader, node, deep=False):
        seen, mapping = set(), {}
        for key_node, value_node in node.value:
            key = loader.construct_object(key_node, deep=deep)
            if key in seen:
                raise SystemExit(f"{path.name}: edit produced a duplicate `{key}` key.")
            seen.add(key)
            mapping[key] = loader.construct_object(value_node, deep=deep)
        return mapping

    _DupDetector.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_dups)
    yaml.load(new_text, Loader=_DupDetector)  # noqa: S506 — subclass of SafeLoader

    def _stripped(doc):
        copy = yaml.safe_load(yaml.dump(doc, sort_keys=False, allow_unicode=True))
        for entry in (copy or {}).get("taxonomy") or []:
            tt = (entry or {}).get("taxon_term")
            if isinstance(tt, dict):
                for key in STATUS_KEYS:
                    tt.pop(key, None)
        return copy

    if _stripped(before) != _stripped(after):
        raise SystemExit(
            f"{path.name}: the status edit changed something other than "
            f"{'/'.join(STATUS_KEYS)} — refusing to write."
        )

    missing = [
        i
        for i, e in enumerate((after or {}).get("taxonomy") or [])
        if "gtdb_grounding_status" not in ((e or {}).get("taxon_term") or {})
    ]
    if missing:
        raise SystemExit(
            f"{path.name}: {len(missing)} taxonomy entries have no status after the edit."
        )


def _assert_only_grounding_changed(
    path: Path, before: dict, new_text: str, refresh: bool = False
) -> None:
    """Fail loudly unless the edit touched gtdb_classification and nothing else."""
    try:
        after = yaml.safe_load(new_text)
    except yaml.YAMLError as exc:
        raise SystemExit(
            f"{path.name}: edit produced unparseable YAML — refusing to write: {exc}"
        ) from exc

    # Duplicate keys anywhere, detected by parsing rather than by counting a
    # substring. PyYAML keeps the last of two identical keys silently, so the
    # corruption survives both a diff skim and linkml-validate (#289). A
    # substring count also missed duplicates *inside* a block.
    class _DupDetector(yaml.SafeLoader):
        pass

    def _no_dups(loader, node, deep=False):
        seen, mapping = set(), {}
        for key_node, value_node in node.value:
            key = loader.construct_object(key_node, deep=deep)
            if key in seen:
                raise SystemExit(f"{path.name}: edit produced a duplicate `{key}` key.")
            seen.add(key)
            mapping[key] = loader.construct_object(value_node, deep=deep)
        return mapping

    _DupDetector.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_dups)
    yaml.load(new_text, Loader=_DupDetector)  # noqa: S506 — subclass of SafeLoader

    # The grounded set must be identical: refresh never creates and never drops.
    def _grounded(doc):
        return [
            i
            for i, e in enumerate(doc.get("taxonomy") or [])
            if ((e or {}).get("taxon_term") or {}).get("gtdb_classification")
        ]

    was, now = _grounded(before), _grounded(after)
    if refresh:
        # Refresh replaces in place: the set must be identical, or a block was
        # created (overturning a deliberate withholding) or swallowed by a bad span.
        if was != now:
            raise SystemExit(
                f"{path.name}: the set of grounded taxa changed — refresh must not "
                f"create or drop a gtdb_classification."
            )
    elif not set(was) <= set(now):
        # Plain apply may add groundings; it must never remove one.
        raise SystemExit(f"{path.name}: an existing gtdb_classification was dropped.")

    b_tax, a_tax = before.get("taxonomy") or [], after.get("taxonomy") or []
    if len(b_tax) != len(a_tax):
        raise SystemExit(f"{path.name}: taxonomy went from {len(b_tax)} to {len(a_tax)} entries.")
    if {k: v for k, v in before.items() if k != "taxonomy"} != {
        k: v for k, v in after.items() if k != "taxonomy"
    }:
        raise SystemExit(f"{path.name}: content outside taxonomy changed.")

    for b, a in zip(b_tax, a_tax, strict=True):
        bt = dict((b or {}).get("taxon_term") or {})
        at = dict((a or {}).get("taxon_term") or {})
        bt.pop("gtdb_classification", None)
        at.pop("gtdb_classification", None)
        if bt != at:
            raise SystemExit(f"{path.name}: a taxon_term changed outside its grounding block.")
        if {k: v for k, v in (b or {}).items() if k != "taxon_term"} != {
            k: v for k, v in (a or {}).items() if k != "taxon_term"
        }:
            raise SystemExit(f"{path.name}: a taxonomy entry changed outside taxon_term.")


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
    p.add_argument(
        "--refresh",
        action="store_true",
        help="With --apply: recompute blocks that already exist. Creates none.",
    )
    p.add_argument(
        "--apply-status",
        action="store_true",
        help="With --community: write gtdb_grounding_status on every taxon (#294). "
        "Independent of --apply; writes no gtdb_classification.",
    )
    p.add_argument(
        "--denominator",
        choices=("aggregate", "deepest"),
        default="aggregate",
        help="How genome support is summed (#371). aggregate: every matched row. "
        "deepest: one row per lineage, at the deepest rank present.",
    )
    p.add_argument(
        "--include-unnamed",
        action="store_true",
        help="Count rows whose NCBI species is not a binomial (sp./uncultured/informal). "
        "Off by default since #375; this restores the pre-#372 denominator.",
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

    if args.community and args.apply_status:
        n = apply_status_to_community(
            args.community,
            by_id,
            by_name,
            by_higher,
            denominator=args.denominator,
            exclude_unnamed=not args.include_unnamed,
        )
        print(f"[gtdb] wrote status on {n} taxa in {args.community.name}", file=sys.stderr)
        return 0

    if args.community and args.apply:
        n = apply_to_community(
            args.community,
            by_id,
            by_name,
            by_higher,
            mapping_source,
            refresh=args.refresh,
            denominator=args.denominator,
            exclude_unnamed=not args.include_unnamed,
        )
        print(f"[gtdb] applied {n} block(s) to {args.community.name}", file=sys.stderr)
        return 0

    n_ok = 0
    for ncbi_id, label in targets:
        g = resolve_target(
            ncbi_id,
            label,
            by_id,
            by_name,
            by_higher,
            denominator=args.denominator,
            exclude_unnamed=not args.include_unnamed,
        )
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
        support, total = g.get("support_genomes"), g.get("total_genomes")
        # Say what the fraction is a fraction *of*. A bare 0.571 reads the same
        # at 4 genomes as at 4000 (#383).
        if total and support is not None:
            of = f"  [{support}/{total} genomes]"
        elif total:
            of = f"  [{total} genomes under the NCBI taxon]"
        else:
            of = ""
        thin = "  ⚠ THIN" if total and total < 10 else ""
        print(f"  majority     : {g['majority_fraction']}{via}{of}{thin}")
        if args.emit_yaml:
            print("  --- gtdb_classification block ---")
            for line in emit_block(g, mapping_source).splitlines():
                print(f"  {line}")
    print(f"\n[gtdb] grounded {n_ok}/{len(targets)} taxa", file=sys.stderr)
    return 0 if n_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
