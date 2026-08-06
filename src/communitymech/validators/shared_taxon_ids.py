"""One specific NCBITaxon id standing in for two different organisms (#292).

Two KB records asserted facts about the wrong species. *Bacteroides ovatus*
carried `NCBITaxon:821`, which is *Phocaeicola vulgatus*; a `Nitrospiraceae
bacterium` carried `NCBITaxon:1236`, class Gammaproteobacteria — a different
phylum. Both then acquired a GTDB block derived from the wrong id, which restates
an error in a second field and makes it look better sourced.

**No existing gate can see this.** `linkml-term-validator` checks that `term.id`
and `term.label` correspond, and they do: `NCBITaxon:821` really is labelled
"Phocaeicola vulgatus". The disagreement is between `preferred_term` and the
grounded term, and comparing *those* is not viable — `preferred_term` differs
from `term.label` right across the KB on purpose, preserving the source paper's
name across NCBI renames (*Eubacterium rectale* -> *Agathobacter rectalis*, and
~50 more). Flagging that would bury the signal.

The usable signal is narrower: **one id reused for two genuinely different named
organisms inside a single record.** Both defects had that shape, because both
were copy-paste from a neighbouring entry.

Sharpening it with rank is what makes it a gate rather than a report. A *broad*
id shared across entries is normal and correct — environmental records
deliberately put several functional guilds under `NCBITaxon:2` (Bacteria) or
`NCBITaxon:131567` (cellular organisms). A *species* id shared by two different
organisms is a contradiction: a species is one organism, so two names under it
cannot both be right. NCBITaxon carries the rank, so this is a lookup rather than
a guess, and the legitimate cases need no waiver list.

Genus is included as specific. A genus id shared by two entries is a real
pattern in MAG-based records ("Methylobacter MAG 1" / "MAG 2"), so those are
allowed through when the names differ only by such a suffix — see
`_looks_like_the_same_organism`.
"""

from __future__ import annotations

import functools
import re

# NCBI ranks at or below which one id denotes one organism. Anything broader is
# a clade that may legitimately host several distinct entries.
SPECIFIC_RANKS = frozenset(
    {
        "species",
        "subspecies",
        "strain",
        "isolate",
        "serotype",
        "serogroup",
        "biotype",
        "genotype",
        "species_subgroup",
        "forma_specialis",
        "genus",
        "subgenus",
    }
)

# A binomial core: genus plus specific epithet, with everything that
# distinguishes an *isolate* stripped. `Bacillus velezensis OB3` and `... NA3`
# share a core; `Bacteroides ovatus` and `Bacteroides vulgatus` do not.
_CORE = re.compile(r"^([A-Za-z][A-Za-z0-9_\-]*)\s+([a-z][a-z0-9_\-]*)")
# GTDB-style placeholder epithets: `sp.`, `sp900119625`, `sp002874965`. All mean
# "unnamed species", so two of them under one genus are not a contradiction.
_PLACEHOLDER = re.compile(r"^sp\d*$")


def _core(name: str) -> tuple[str, str] | None:
    """(genus, epithet) for a Latin binomial, or None if the name is not one.

    Parentheticals and trailing strain codes are dropped before matching, so
    `Olsenella_B sp. (MAG ATO3)` reduces to `("olsenella_b", "sp")`.
    """
    cleaned = re.sub(r"\(.*?\)", " ", name or "").replace(".", " ")
    match = _CORE.match(cleaned.strip())
    if not match:
        return None
    genus, epithet = match.group(1).lower(), match.group(2).lower()
    if _PLACEHOLDER.match(epithet):
        epithet = "sp"
    return genus, epithet


@functools.lru_cache(maxsize=1)
def _adapter():
    try:
        from oaklib import get_adapter  # type: ignore[import-untyped]

        return get_adapter("sqlite:obo:ncbitaxon")
    except Exception:
        return None


@functools.lru_cache(maxsize=4096)
def rank_of(curie: str) -> str | None:
    """The NCBI rank (`species`, `genus`, `class`, ...), or None if undetermined.

    None whenever the adapter is missing or the term carries no rank, which
    callers must treat as "cannot judge" — never as "specific". A gate that
    fired when it could not look anything up would be noise on any machine
    without the NCBITaxon database.
    """
    adapter = _adapter()
    if adapter is None or not curie.startswith("NCBITaxon:"):
        return None
    try:
        metadata = adapter.entity_metadata_map(curie)
    except Exception:
        return None
    for key, values in (metadata or {}).items():
        if "rank" not in key.lower():
            continue
        for value in values:
            if isinstance(value, str) and value.startswith("NCBITaxon:"):
                return value.split(":", 1)[1].replace("_", " ").strip().replace(" ", "_")
    return None


def is_specific(curie: str) -> bool:
    """Does this id denote a single organism? False when undetermined."""
    return (rank_of(curie) or "") in SPECIFIC_RANKS


def _names_disagree(first: str, second: str, rank: str | None) -> bool:
    """Do two `preferred_term`s under one id name genuinely different taxa?

    The rank decides what counts as a disagreement, and this is the whole design:

    * a **genus** id legitimately hosts many species and many unnamed isolates —
      `Variovorax sp. BK119` through `BK752`, or a named species beside an
      `sp.` — so only a differing *genus* is a contradiction there;
    * a **species**-or-finer id denotes one organism, so a differing *epithet* is
      a contradiction: `Bacteroides ovatus` and `Bacteroides vulgatus` cannot
      both be `NCBITaxon:821`.

    Names that are not binomials at all fall back to "no disagreement". A guild
    label like `rhizosphere Actinobacteria` says nothing this check can use, and
    guessing from it is how a gate becomes noise.
    """
    left, right = _core(first), _core(second)
    if left is None or right is None:
        return False
    if left[0] != right[0]:
        return True
    return rank != "genus" and rank != "subgenus" and left[1] != right[1]


def check_record(taxonomy: list) -> list[str]:
    """Messages for each specific id shared by genuinely different organisms."""
    by_id: dict[str, list[str]] = {}
    for entry in taxonomy or []:
        term_block = entry.get("taxon_term") or {}
        term = term_block.get("term")
        if not isinstance(term, dict):
            continue
        curie = term.get("id") or ""
        name = term_block.get("preferred_term") or term.get("label") or ""
        if curie and name and name not in by_id.get(curie, []):
            by_id.setdefault(curie, []).append(name)

    problems = []
    for curie, names in sorted(by_id.items()):
        # Cheap test first. Asking NCBITaxon for a rank opens a large SQLite
        # database, and only a handful of ids in a record are shared at all —
        # ordering this the other way meant ~1000 lookups per KB sweep instead
        # of ~15, and the scan took minutes rather than seconds.
        if len(names) < 2:
            continue
        rank = rank_of(curie)
        if (rank or "") not in SPECIFIC_RANKS:
            continue
        clashing = sorted(
            {
                names[i]
                for i in range(len(names))
                for j in range(i)
                if _names_disagree(names[i], names[j], rank)
            }
            | {
                names[j]
                for i in range(len(names))
                for j in range(i)
                if _names_disagree(names[i], names[j], rank)
            }
        )
        if len(clashing) < 2:
            continue
        problems.append(
            f"{curie} ({rank}) is used for taxa that cannot all be it: "
            + ", ".join(repr(n) for n in clashing)
        )
    return problems
