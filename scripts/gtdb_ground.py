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
  NCBI taxon; ground to the GTDB taxon holding a strict majority (>50%) of them,
  else
  report AMBIGUOUS (e.g. NCBI genus Bacillus shatters into ~100 GTDB genera).

  Since #372 that aggregation counts only rows naming an actual binomial —
  ``exclude_unnamed`` defaults to True, so ``sp.``/``uncultured``/informal rows
  are excluded (#375). It is a real change of denominator, not a tidy-up: it
  moved 219 of the KB's stored fractions. An exact 50/50 tie no longer grounds at
  all — the name tie-break now only orders the AMBIGUOUS option list (#382) — and
  the block records how many genomes the fraction came from (#383).

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

# `scripts/` is on sys.path when this runs as `python scripts/gtdb_ground.py`,
# so reach the package the same way the other scripts do.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from communitymech.validators.ncbi_domain import outside_gtdb_scope  # noqa: E402

# NCBI2GTDB.tsv column indices (0-based); see header row.
COL_NCBI_ID = 0
COL_TOTAL_GENOMES = 2
COL_MAJORITY = 3
COL_NCBI_SPECIES = 10
COL_NCBI_STRAIN = 11
COL_GTDB_SPECIES = 18
# (NCBI column, GTDB column, CURIE prefix), deepest first — `resolve_higher`
# takes the first rank whose NCBI column carries the requested name.
#
# Domain was absent until #393, so *Bacteria* and *Archaea* never resolved and
# 72 KB entries recorded "the tool produced no grounding" for the two taxa that
# are the roots of GTDB.
#
# Domain is last on principle rather than necessity: `resolve_higher` re-filters
# by each rank's own NCBI column, and no name occupies two rank columns in this
# crosswalk, so moving it first changes nothing today — I checked all 1032 KB
# taxa. Ordering is what would keep it correct if that ever stopped holding
# (#402 review).
# A grounding this close to the 0.5 line is a coin flip that landed right (#396).
#
# 0.55 is a judgement call and is meant to be: there is no natural cut point in
# the distribution, which is why #396 rejected *raising* the threshold. It sits
# where it does because the population either side is stable — 5 blocks below
# 0.55, then a gap to 0.57 — so the marker points at the genuinely marginal ones
# instead of crying wolf across the 35 blocks between 0.7 and 0.9.
#
# Deliberately advisory. It changes no stored value and withholds no grounding;
# it only makes the tool say so where a curator will see it.
NEAR_TIE_BELOW = 0.55


def _is_near_tie(fraction) -> bool:
    """Is this grounding close enough to 0.5 to be a coin flip?

    False for a missing fraction: "unknown" is not "marginal".

    A pure function of the number, deliberately — it does not consult `curated`.
    The KB's one sub-threshold block (`g__Syntrophotalea` at exactly 0.5) really
    is a coin flip; that a curator chose it anyway (#384) is a separate fact the
    block records for itself.

    No `isinstance(fraction, bool)` guard. Booleans are ints in Python, so one
    looked prudent — but `True` is 1, above the bound, and `False` is 0, which
    fails `0 < fraction`. It was dead code: removing it failed no test.
    """
    return isinstance(fraction, (int, float)) and 0 < fraction < NEAR_TIE_BELOW


HIGHER_RANKS = [
    (9, 17, "g"),
    (8, 16, "f"),
    (7, 15, "o"),
    (6, 14, "c"),
    (5, 13, "p"),
    (4, 12, "d"),
]
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


def lookup_keys(label: str | None) -> list[str]:
    """Mapping-table keys for a label, most specific first.

    `_clean_label` strips a leading "Candidatus" so the binomial heuristic and
    the CURIE builder see a bare name. The NCBI2GTDB species and genus columns
    **keep** it, so looking up only the stripped form missed every *Candidatus*
    taxon and they went silently ungrounded — no error, just
    `no GTDB mapping`. `Candidatus Accumulibacter` is the case that surfaced it
    (#419): the genus has 45 genomes under `GTDB:g__Accumulibacter`, and the
    KB had fallen back to grounding it at *class* rank instead.

    Both spellings are returned because both occur: the table is not
    self-consistent about the prefix, and a taxon may be renamed out of
    *Candidatus* status once cultured. Exact-as-NCBI-spells-it comes first, so
    a genuine un-prefixed homonym cannot capture a Candidatus lookup.
    """
    raw = (label or "").strip()
    keys = []
    for key in (raw.lower(), _clean_label(raw).lower()):
        if key and key not in keys:
            keys.append(key)
    return keys


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


def _species_denominator(rows) -> tuple[int, float]:
    """(genomes, genome-weighted majority) for one GTDB species, without double-counting.

    A crosswalk row is an NCBI taxonID's assignment, so a species-rank row and
    its strain rows describe overlapping genome sets. Summing them inflates:
    *Escherichia coli* has 2 species-rank rows totalling 166398 and 2608 strain
    rows totalling 17969, and adding them gives 184367 for a population no
    larger than the species.

    `deepest_only`'s rule — drop the species rows, keep the strains — is not
    right for a denominator either: it would report 17969 for that same taxon,
    discarding the largest measurement.

    Note this is currently a **no-op on the KB**: no grounded name group mixes
    the two depths today. It is here so that the first one to do so cannot
    double-count silently, and the tests state the rule rather than a sample.

    So take the larger of the two depths and never their sum. Containment does
    not hold in this table (1363 of 2827 species have strain support exceeding
    their species row, #371), so the larger depth is the best supported lower
    bound rather than a derived total.
    """
    species_rows = [r for r in rows if not r[COL_NCBI_STRAIN].strip()]
    strain_rows = [r for r in rows if r[COL_NCBI_STRAIN].strip()]
    chosen = max((species_rows, strain_rows), key=lambda group: sum(_genomes(r) for r in group))
    total = sum(_genomes(r) for r in chosen)
    if not total:
        return 0, 0.0
    return total, round(sum(_genomes(r) * _maj(r) for r in chosen) / total, 3)


def _ground_species(rows, source_id, label, via, exclude_unnamed=True):
    # The named-species filter, which `resolve_target` accepted and forwarded
    # only to `resolve_higher` — so `exclude_unnamed=False` was honoured at genus
    # rank and silently dropped here (#405).
    #
    # It runs *before* `top`, so it selects the GTDB species and not merely the
    # denominator. That placement is what the tests pin; moving it below passes
    # every other fixture, since they all put both rows on one species.
    #
    # **It cannot fire through `resolve_target` on this crosswalk**, and the PR
    # that added it was wrong to call that "free today, real later". Every NCBI
    # id maps to exactly one row (0 of 92711 have more), so the id path filters a
    # singleton; and `by_name` is keyed on the NCBI species string, so a group
    # shares one string and the filter is all-or-nothing — 0 of 64660 groups
    # mix. The non-empty fallback then restores an all-unnamed group intact.
    # What the change buys is that the flag now means the same thing on both
    # paths, not a latent guard (#408 review).
    #
    # Same "never empty a taxon" fallback as the higher-rank path.
    if exclude_unnamed:
        filtered = named_species_only(rows)
        if filtered:
            rows = filtered

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
    # This second filter cannot change a grounding — `sp` is read off `top`
    # *before* `agreeing` is built, so it can only narrow the rows behind an
    # already-chosen species. (The named-species filter above runs earlier and
    # does select the species; do not read this paragraph as covering both.) `resolve_target` also reports AMBIGUOUS whenever a
    # name group holds more than one GTDB species, so the mixed case does not
    # arise from the public entry point — the filter is defensive, and the
    # synthetic split in the tests is what exercises it.
    #
    # It moves 39 denominators (36 alone, 3 alongside a fraction) and 3 fractions.
    #
    # Only the **name** path aggregates. An NCBI id maps to exactly one crosswalk
    # row, so an id-path grounding reports that row alone — which leaves the
    # understatement #386 was filed about in place on more blocks than this
    # fixes. #389 tried to widen it and had to be reverted: the only wider set
    # available is keyed on `term.label`, so a synonym moved the answer 9.5x.
    # Widening needs a key as stable as the id, which this crosswalk does not
    # offer — #389 stays open with the measurement.
    # Scoped to the rows this grounding was resolved from — the taxon's own rows
    # on the id path, the name group on the name path. #389 widened the id path
    # to include the name group and that was worse: the name group is keyed on
    # `term.label`, which is curator prose, so `NCBITaxon:33038` reported 2945
    # under "Mediterraneibacter gnavus" and 311 under its NCBI synonym
    # "Ruminococcus gnavus". An id is stable; a label is not (#404 review).
    agreeing = [r for r in rows if r[COL_GTDB_SPECIES].strip() == sp] if sp else []
    total, fraction = _species_denominator(agreeing)
    if not total:
        # No GTDB species cell, or every agreeing row carries no genome count.
        # `top` is itself in `agreeing`, so an empty total means `_genomes(top)`
        # is 0 too — publish no count rather than a meaningless one, since
        # `total_genomes: 0` would fail the schema's `minimum_value: 1`.
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
    return [
        r
        for r in matched
        if r[COL_NCBI_SPECIES].strip() and not UNNAMED_SPECIES.search(r[COL_NCBI_SPECIES].strip())
    ]


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


def resolve_higher(
    clean_lc, source_id, label, by_higher, denominator="aggregate", exclude_unnamed=True
):
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
        # Since #382 a tie no longer grounds, so this orders the AMBIGUOUS option
        # list rather than deciding an answer; the reproducibility is still the
        # point, because that list is what a curator reads.
        top, tw = sorted(weights.items(), key=lambda kv: (-kv[1], kv[0]))[0]
        frac = tw / total
        # Strictly greater. An exact 50/50 split is not a majority, and grounding
        # it meant the answer came from the tie-break rather than the evidence:
        # two live KB blocks sat on `19/38`, decided alphabetically between
        # `g__Ensifer` and `g__Sinorhizobium` (#382). The tie-break stays — it is
        # what makes the AMBIGUOUS option list reproducible — but it no longer
        # decides a grounding.
        if frac > 0.5:
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
            # Full list, not `ranked[:8]`. The stored `gtdb_candidates` exists so
            # a curator can choose without re-running the tool, and truncating it
            # silently defeated exactly that: six KB taxa recorded 8 of 46 and 8
            # of 33 contenders with no marker that any were dropped (#392 review).
            # The CLI still prints only the first 8, with an "and N more" tail.
            #
            # CURIEs, not bare names, and via the same `_curie` the grounding uses
            # so a candidate is spelled exactly as it would be once chosen (#415).
            # A bare `RDYJ01` is an alphanumeric GTDB placeholder that means
            # nothing without its rank; `GTDB:g__RDYJ01` resolves and can be
            # filtered by rank the way `gtdb_id` can.
            "gtdb_options": [_curie(name, prefix) for name in ranked],
            "n_alt": len(weights),
        }
    return None


def resolve_target(
    ncbi_id, label, by_id, by_name, by_higher, denominator="aggregate", exclude_unnamed=True
):
    """Species: id then name (split-aware). Genus/higher: majority GTDB rank taxon.

    `denominator` reaches `resolve_higher` only — the species paths resolve
    within one GTDB species, so the aggregate/deepest choice does not arise.
    `exclude_unnamed` reaches both since #405; it used to be accepted here and
    silently dropped on the species path.
    """
    source_id = f"NCBITaxon:{ncbi_id}" if ncbi_id else None
    clean = _clean_label(label)
    if _is_species(clean):
        if ncbi_id and ncbi_id in by_id:
            return _ground_species(
                by_id[ncbi_id], source_id, label, "ncbi_id", exclude_unnamed=exclude_unnamed
            )
        # Both spellings, exact first — see `lookup_keys` (#419).
        for nlc in lookup_keys(label):
            if nlc not in by_name:
                continue
            species: dict[str, list] = {}
            for c in by_name[nlc]:
                sp = c[COL_GTDB_SPECIES].strip()
                if sp:
                    species.setdefault(sp, []).append(c)
            if len(species) == 1:
                return _ground_species(
                    next(iter(species.values())),
                    source_id,
                    label,
                    "ncbi_name",
                    exclude_unnamed=exclude_unnamed,
                )
            if len(species) > 1:
                return {
                    "ambiguous": True,
                    "via": "ncbi_name",
                    "ncbi_source_id": source_id,
                    "ncbi_species": label,
                    # Species rank, so `s__` — see the CURIE note in
                    # `resolve_higher` (#415).
                    "gtdb_options": [_curie(name, "s") for name in sorted(species)],
                    "n_alt": len(species),
                }
        return None
    for key in lookup_keys(label):
        found = resolve_higher(key, source_id, label, by_higher, denominator, exclude_unnamed)
        if found is not None:
            return found
    return None


# Groundings a curator chose against the majority vote, keyed by
# (record filename, NCBITaxon id). `--refresh` recomputes an existing block, so
# without this the tool silently replaces a right answer with a confidently wrong
# one and only `tests/test_gtdb_withheld_groundings.py::CURATED` notices, after
# the fact. Mirrors WITHHELD, which keeps taxa *ungrounded* (#292/#293).
#
# A fallback for records not yet marked. The `curated: true` flag on the block is
# the primary mechanism (#384) — prefer it, because a list protects only what
# someone remembered to add, which is how *Chlorobium* went unprotected.
CURATED_GROUNDINGS = {
    ("Dehalococcoides_Pelobacter_Acetylene_TCE_Coculture.yaml", "NCBITaxon:18"): (
        "GTDB:g__Syntrophotalea — SFB93 is an acetylene fermenter and the entry's "
        "notes tie it to Syntrophotalea acetylenivorans, but every Pelobacter row "
        "naming Syntrophotalea is an `sp.` row, so the named-species filter hands "
        "the vote to g__Seleniibacterium at 0.571 (#384)."
    ),
}


def _is_curated(term_block: dict) -> bool:
    """Is this taxon's grounding pinned by a curator?

    Reads the flag off the block, so the decision travels with the data.
    `CURATED_GROUNDINGS` remains as a fallback for records not yet marked, but a
    list only protects what someone remembered to add — which is exactly how
    *Chlorobium* went unprotected (#384).
    """
    block = (term_block or {}).get("gtdb_classification")
    if not isinstance(block, dict):
        return False
    # Keyed on the *value*, and only on `curated`. Reading the key's presence
    # would freeze a block written `curated: false` — a curator recording "I
    # checked, the tool is right" — and reading `curation_note` would let a note
    # protect a block nothing flagged (#397 review).
    return block.get("curated") is True


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
    # Indent derived from the anchor, not hardcoded. `data/isolates` uses the
    # indented-sequence style (`  - taxon_term:`), putting taxon_term children at
    # 6 spaces, so a literal 4 never matched there and withdrawal could not find
    # the block to remove. Same defect `_status_spans` carried until #392; this
    # function kept the assumption (#394 review).
    child = len(re.match(r"^(\s*)", lines[anchor]).group(1)) - 2
    key = re.compile(r"^\s{" + str(child) + r"}gtdb_classification:\s*$")
    deeper = re.compile(r"^\s{" + str(child + 2) + r",}\S")
    i = anchor + 1
    while i < end:
        if key.match(lines[i]):
            j = i + 1
            # Deeper, not exactly one level deeper. PyYAML wraps long scalars onto
            # continuation lines indented further, so an exact match stopped one
            # line short and left orphans that became duplicate keys in 13
            # records (#378 review).
            while j < end and deeper.match(lines[j]):
                j += 1
            return (i, j)
        # Any line at the taxon_term level or shallower ends this entry.
        if re.match(r"^\s{0," + str(child) + r"}\S", lines[i]) and not re.match(
            r"^\s{" + str(child) + r"}\S", lines[i]
        ):
            return None
        if re.match(r"^\s*- \S", lines[i]) and not re.match(
            r"^\s{" + str(child) + r"}- ", lines[i]
        ):
            return None
        i += 1
    return None


STATUS_KEYS = ("gtdb_grounding_status", "gtdb_candidates")


# Why a resolve failed, from what the tool already holds at that moment (#393).
#
# #294 wanted UNRESOLVED told apart from NO_GTDB_EQUIVALENT ("GTDB has no
# counterpart and never will"). #392 made the tool emit only the weak state,
# because inferring the strong one from "the resolve failed" was wrong for at
# least 82 of 293 entries.
#
# This does not restore the strong claim — that needs an NCBI lineage source
# this script does not have, since GTDB is bacteria/archaea only (#393 option 1).
# It records the *reason*, which the tool knew and discarded, and which splits
# the population into two genuinely different piles:
#
#   ROWS_FILTERED    the crosswalk has rows under this taxon and the
#                    named-species filter (#375) removed all of them —
#                    `Pseudomonas sp.`, `Streptomyces sp.`. A curator could
#                    recover these by relaxing the filter; nothing is missing.
#   NOT_IN_CROSSWALK the id and name appear nowhere in the mapping. Two very
#                    different things live here and this deliberately does not
#                    guess between them: a eukaryote or virus, which really is
#                    final (GTDB will never classify Saccharomyces), and a clade
#                    the crosswalk spells differently (NCBI *Sulcia* is
#                    `Candidatus Karelsulcia`), which is a lookup failure.
#
# So NOT_IN_CROSSWALK is the population #393 option 1 would resolve, and naming
# it is what makes that work schedulable instead of a re-derivation.
UNRESOLVED_REASONS = ("ROWS_FILTERED", "NOT_IN_CROSSWALK")


def unresolved_reason(tid: str, label: str, by_id, by_name, by_higher) -> str:
    """Which of the two failure modes applied.

    Read off the indexes rather than re-deriving: `collect_rows` only indexes
    taxa that were asked for, so a non-empty entry means the crosswalk really
    does carry rows for this taxon and the filter is what emptied them.
    """
    number = tid.split(":", 1)[1] if ":" in tid else tid
    name = (label or "").strip().lower()
    if by_id.get(number) or by_name.get(name) or by_higher.get(name):
        return "ROWS_FILTERED"
    return "NOT_IN_CROSSWALK"


def classify_status(
    record_name,
    tid,
    label,
    has_block,
    by_id,
    by_name,
    by_higher,
    preferred=None,
    **kwargs,
):
    """Why this taxon does or does not carry a grounding (#294).

    Returns (status, candidates). The tool already distinguished all of these
    internally — it prints a block, `AMBIGUOUS`, or `no GTDB mapping` — so this
    persists a decision rather than making a new one.

    Order matters. WITHHELD is checked before anything is computed, because the
    point of a withhold is that the tool *can* produce a grounding and must not:
    classifying it by outcome would label it GROUNDED-able and invite exactly the
    re-run #293 exists to prevent.

    There is deliberately no `curated` parameter. `curated: true` lives *inside*
    `gtdb_classification`, so a flagged taxon always has a block and the
    `has_block` branch already answers GROUNDED. A `curated=` argument was added
    in #384 and was unreachable from the writer — deleting its wiring left the
    whole suite green — while quietly reordering this function so a taxon both
    flagged and in WITHHELD_GROUNDINGS returned GROUNDED, contradicting the
    paragraph above (#397 review).
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
        # UNRESOLVED, never NO_GTDB_EQUIVALENT. This script cannot tell the two
        # apart, and an earlier version asserted the strong one anyway: 57 KB
        # entries read "GTDB has no counterpart and never will" for *Bacteria*,
        # which is the root of GTDB. That was a gap in `HIGHER_RANKS`, closed in
        # #393 by adding domain rank. What remains fails for other reasons — the
        # crosswalk spelling the clade differently (NCBI *Sulcia* is `Candidatus
        # Karelsulcia`), or the named-species filter removing its rows.
        #
        # Matching NCBI names against the table was tried and does not settle it
        # either — a rename defeats it. Establishing "GTDB will never classify
        # this" needs an NCBI lineage source, since GTDB is bacteria/archaea
        # only. That source is now wired in (#393): `outside_gtdb_scope` asks the
        # NCBITaxon ontology for the taxon's domain, and a eukaryote or virus is
        # final rather than merely unresolved.
        #
        # Of the KB's 220 UNRESOLVED taxa, 92 are Eukaryota and 6 Viruses — so
        # 98 were never outstanding work, and the backlog overstated itself by
        # about 45%. The other 106 are genuinely bacteria and archaea the tool
        # failed to match, and stay UNRESOLVED.
        #
        # One-directional on purpose. `outside_gtdb_scope` returns False when it
        # cannot tell — no adapter, a lookup failure, a taxon above every domain
        # like `cellular organisms` — so an unavailable NCBITaxon database
        # degrades to the weaker status and never to a false claim of finality.
        # That is what keeps this script runnable without a large download.
        if outside_gtdb_scope(tid):
            return "NO_GTDB_EQUIVALENT", []
        return "UNRESOLVED", []
    # The tool would ground this and the KB does not. That is the only value
    # here that represents outstanding work.
    return "NOT_ATTEMPTED", []


# Taxa kept ungrounded on purpose because the block this tool would derive is
# wrong, so writing it would state the error convincingly in a second field.
# Two reasons qualify and they need different fixes: a wrong NCBITaxon id (#292,
# fixed by correcting the id) and a GTDB majority that contradicts the record's
# own physiology (#416, fixed only by a curator choosing the grounding).
# Mirrors CURATED_GROUNDINGS, which protects a grounding that *is* right.
# Kept in step with WITHHELD in tests/test_gtdb_withheld_groundings.py (#292).
WITHHELD_GROUNDINGS = {
    ("KBase_ORT_Workflow_Community_Model.yaml", "Nitrospiraceae bacterium"): (
        "GTDB's majority for NCBI Nitrospiraceae is f__Leptospirillaceae at 0.534 "
        "(31/58 genomes), and Leptospirillum is an iron oxidizer while this genome "
        "is the record's nitrite oxidizer — so the majority vote would assign the "
        "wrong physiology. A near-tie of this kind is #396's class. Withheld until "
        "a curator picks. (Was withheld because the id was NCBITaxon:1236, class "
        "Gammaproteobacteria; that is fixed — it is now NCBITaxon:189779 — but the "
        "grounding is still not safe to take automatically, #416.)"
    ),
}


def _status_spans(lines: list[str], anchor: int, end: int) -> list[tuple[int, int]]:
    """Line spans of any existing status keys for one taxonomy entry.

    The indent is derived from the anchor rather than hardcoded. `data/isolates`
    uses the indented-sequence style (`  - taxon_term:`), putting taxon_term
    children at 6 spaces, so a literal 4-space match never worked there: the key
    was neither found nor dropped, and a second `--apply-status` produced a
    duplicate. The canary that "proved" idempotency only ever ran on
    kb/communities, which is uniformly 4-space (#392 review).

    A block sequence sits at the *same* indent as its key, so `gtdb_candidates:`
    is followed by `- Anabaena` at that indent, not by a deeper line.
    """
    child = len(re.match(r"^(\s*)", lines[anchor]).group(1)) - 2
    keys = re.compile(r"^\s{" + str(child) + r"}(?:" + "|".join(STATUS_KEYS) + r"):")
    item = re.compile(r"^\s{" + str(child) + r"}- ")
    deeper = re.compile(r"^\s{" + str(child + 2) + r",}\S")
    sibling = re.compile(r"^\s{0," + str(child) + r"}\S")
    spans, i = [], anchor + 1
    while i < end:
        if keys.match(lines[i]):
            j = i + 1
            while j < end and (deeper.match(lines[j]) or item.match(lines[j])):
                j += 1
            spans.append((i, j))
            i = j
            continue
        if sibling.match(lines[i]) and not re.match(r"^\s{" + str(child) + r"}\S", lines[i]):
            break
        if re.match(r"^\s*- ", lines[i]) and not item.match(lines[i]):
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
        # A withheld taxon must not be re-grounded. #293 closed this with a CI
        # pin rather than a guard, so the write still happened and was only
        # caught afterwards — running the documented `--apply` over the KB
        # reinstated `NCBITaxon:1236` as c__Gammaproteobacteria, derived from an
        # id that names a different organism (#402 review). Keyed by
        # preferred_term, not by id: a withheld record may use the same id
        # correctly for one of its other entries (#294).
        if (path.name, tt.get("preferred_term")) in WITHHELD_GROUNDINGS:
            print(
                f"[gtdb] skipping withheld {tt.get('preferred_term')!r} in {path.name}: "
                f"{WITHHELD_GROUNDINGS[(path.name, tt.get('preferred_term'))]}",
                file=sys.stderr,
            )
            wanted.append(None)
            continue
        if _is_curated(tt) or (path.name, tid) in CURATED_GROUNDINGS:
            # The reason can come from either source, and indexing the list
            # unconditionally raised KeyError whenever the block's own `curated`
            # flag was what protected it — i.e. exactly the case the flag exists
            # for. Caught by the canary before any sweep (#384).
            reason = CURATED_GROUNDINGS.get((path.name, tid)) or (
                (tt.get("gtdb_classification") or {}).get("curation_note")
                or "marked `curated: true` with no curation_note"
            )
            print(f"[gtdb] skipping curated {tid} in {path.name}: {reason}", file=sys.stderr)
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


def withdraw_ambiguous(path: Path, by_id, by_name, by_higher, **kwargs) -> int:
    """Remove groundings the tool now calls AMBIGUOUS (#382, #376).

    `--refresh` is deliberately unable to drop a block: an ungrounded taxon may
    be ungrounded on purpose, so a refresh that could remove would be able to
    overturn a curation decision silently (#378). Withdrawal is therefore its
    own mode, and a narrow one — it removes only where the recompute is
    *explicitly* ambiguous, never where it merely fails, so a taxon whose rows
    have gone missing keeps its stored answer rather than losing it to a bad
    mapping build.

    Curated pins are skipped, as everywhere else.
    """
    doc = yaml.safe_load(path.read_text())
    entries = doc.get("taxonomy", []) or []

    drop_entry: list[bool] = []
    for tc in entries:
        tt = (tc or {}).get("taxon_term", {}) or {}
        term = tt.get("term", {}) or {}
        tid = str(term.get("id", ""))
        if (
            _is_curated(tt)
            or (path.name, tid) in CURATED_GROUNDINGS
            or "gtdb_classification" not in tt
        ):
            drop_entry.append(False)
            continue
        if not tid.startswith("NCBITaxon:"):
            drop_entry.append(False)
            continue
        result = resolve_target(
            tid.split(":", 1)[1], term.get("label", ""), by_id, by_name, by_higher, **kwargs
        )
        drop_entry.append(bool(result and result.get("ambiguous")))
    if not any(drop_entry):
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

    drop: set[int] = set()
    removed = 0
    for pos, wanted in zip(anchors, drop_entry, strict=True):
        if not wanted:
            continue
        span = _block_span(lines, pos, end)
        if span is None:
            raise SystemExit(f"{path.name}: could not locate the block to withdraw at line {pos}.")
        drop.update(range(*span))
        removed += 1

    new_text = "\n".join(ln for i, ln in enumerate(lines) if i not in drop) + "\n"
    _assert_only_grounding_changed(path, doc, new_text, withdraw=True)
    path.write_text(new_text)
    return removed


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
    # The label line is emitted by hand beside its anchor, so it must not also
    # be emitted by the main loop.
    label_lines = {pos + 1 for pos in anchors}

    # Emit every line except the old status keys, inserting the new ones right
    # after each entry's label.
    #
    # This replaces a walk that advanced two cursors and then re-emitted
    # `lines[i]` unconditionally, so a dropped line reappeared whenever the old
    # status keys were not exactly two lines below the anchor — which is what
    # `--apply` produces, since it inserts `gtdb_classification` between the
    # label and them. The result was a duplicate key that this function then
    # refused to write, leaving records only hand-editable, and in one ordering
    # a silently stale `gtdb_candidates` beside a fresh status (#392 review).
    # A drop-set cannot express either failure.
    drop = {n for pos in by_anchor for span in spans[pos] for n in range(*span)}
    out, written = lines[: start + 1], 0
    for i in range(start + 1, end):
        if i in drop or i in label_lines:
            continue
        out.append(lines[i])
        if i in by_anchor:
            status, candidates = by_anchor[i]
            # The label line is the anchor's partner and never a status key, so
            # emitting it here keeps the pair together; `drop` skips it below.
            out.append(lines[i + 1])
            child = " " * (len(re.match(r"^(\s*)", lines[i]).group(1)) - 2)
            out.append(f"{child}gtdb_grounding_status: {status}")
            if candidates:
                out.append(f"{child}gtdb_candidates:")
                out += [f"{child}- {c}" for c in candidates]
            written += 1
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
    path: Path, before: dict, new_text: str, refresh: bool = False, withdraw: bool = False
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
    if withdraw:
        # Withdrawal removes and never adds. The inverse of plain apply.
        if not set(now) <= set(was):
            raise SystemExit(f"{path.name}: withdrawal created a gtdb_classification.")
        if was == now:
            raise SystemExit(f"{path.name}: withdrawal removed nothing.")
    elif refresh:
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

    # Losing `curated`/`curation_note` is the exact regression this flag prevents,
    # and popping gtdb_classification wholesale below makes it invisible. `_block`
    # never emits them, so any path that fails to detect the flag would rewrite
    # the block and delete the evidence it was ever curated (#397 review).
    def _pins(doc):
        return {
            i: ((e or {}).get("taxon_term") or {})
            .get("gtdb_classification", {})
            .get("curation_note")
            for i, e in enumerate(doc.get("taxonomy") or [])
            if isinstance(((e or {}).get("taxon_term") or {}).get("gtdb_classification"), dict)
            and ((e or {}).get("taxon_term") or {}).get("gtdb_classification", {}).get("curated")
        }

    lost = {i: note for i, note in _pins(before).items() if i not in _pins(after)}
    if lost:
        raise SystemExit(
            f"{path.name}: the edit dropped `curated` from {len(lost)} block(s) — "
            f"refusing to write. A curated grounding must survive every mode."
        )

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
        "--withdraw-ambiguous",
        action="store_true",
        help="With --community: remove groundings the tool now calls AMBIGUOUS (#382). "
        "Removes only; --refresh cannot, by design.",
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
        # Index both spellings, or the lookup in `resolve_target` has nothing to
        # find under the exact one (#419).
        if _is_species(clean):
            if ncbi_id:
                want_ids.add(ncbi_id)
            want_species.update(lookup_keys(label))
        elif clean:
            want_higher.update(lookup_keys(label))
    by_id, by_name, by_higher = collect_rows(mapping_path, want_ids, want_species, want_higher)

    if args.community and args.withdraw_ambiguous:
        n = withdraw_ambiguous(
            args.community,
            by_id,
            by_name,
            by_higher,
            denominator=args.denominator,
            exclude_unnamed=not args.include_unnamed,
        )
        print(f"[gtdb] withdrew {n} block(s) from {args.community.name}", file=sys.stderr)
        # Withdrawing leaves the status saying GROUNDED with no block. Returning
        # here made `--withdraw-ambiguous --apply-status` exit 0 having ignored
        # the second flag and left exactly that incoherence, with nothing on
        # stderr (#394 review). Fall through so the modes compose; if the caller
        # did not ask for a status pass, say what still needs doing.
        if n and not args.apply_status:
            print(
                f"[gtdb] {args.community.name}: {n} taxon(s) are now ungrounded — "
                f"re-run with --apply-status to record why.",
                file=sys.stderr,
            )
        if not args.apply_status:
            return 0

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
            shown = g["gtdb_options"][:8]
            opts = ", ".join(shown)
            extra = g.get("n_alt", 0) - len(shown)
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
        # A grounding just over the line is a coin flip that happened to land
        # right. #394 moved the threshold from >=0.5 to >0.5 so a tie-break could
        # no longer decide a grounding, but it did not make the survivors
        # well-supported: four blocks sit at 0.50098 — 226306 against 225423,
        # a margin of 883 genomes in 451729 (#396).
        #
        # Marked rather than withheld, because there is no natural cut point and
        # raising the threshold is a curation policy call. What a curator needs
        # is to be told at the moment of decision. #416 is the case in point: a
        # 0.534 majority put an *iron* oxidizer (f__Leptospirillaceae) on the
        # record's *nitrite* oxidizer. The number alone did not say "look here".
        near = "  ⚠ NEAR-TIE" if _is_near_tie(g.get("majority_fraction")) else ""
        print(f"  majority     : {g['majority_fraction']}{via}{of}{thin}{near}")
        if args.emit_yaml:
            print("  --- gtdb_classification block ---")
            for line in emit_block(g, mapping_source).splitlines():
                print(f"  {line}")
    print(f"\n[gtdb] grounded {n_ok}/{len(targets)} taxa", file=sys.stderr)
    return 0 if n_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
