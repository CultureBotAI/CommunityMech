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

Genus is included as specific, but a genus id shared by two entries is a real
pattern in MAG-based records (`Variovorax sp. BK119` .. `BK752`), so under a
genus id only a differing *genus* counts — see `_names_disagree`.

Three ways the KB spells one organism two ways are exempt, because each would
otherwise be a false positive, and a gate that fires on a legitimate record is
one a curator learns to ignore:

* an **NCBI rename** — one species id carrying both `Eubacterium rectale` and
  `Agathobacter rectalis`, which is the very thing `preferred_term` exists to
  preserve. Both are names NCBITaxon lists for the id (`known_cores`).
* a **GTDB genus split** — `Olsenella` beside `Olsenella_B`.
* an **abbreviated genus** — `B. subtilis` beside `Bacillus subtilis`.

The last two are `_same_genus`. All three are lookups or unambiguous string
facts rather than guesses, so none of them needs a waiver list.
"""

from __future__ import annotations

import functools
import re
import sys

# NCBI ranks at or below which one id denotes one organism. Anything broader is
# a clade that may legitimately host several distinct entries.
#
# `species_group`/`species_subgroup` are deliberately absent: each spans several
# species, so two names under one are not a contradiction. They would be
# unreachable here anyway — NCBITaxon models those two ranks as
# `obo:NCBITaxon#_species_group` rather than a `NCBITaxon:` CURIE, so `rank_of`
# returns None for them.
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
# GTDB splits one NCBI genus into `Olsenella`, `Olsenella_A`, `Olsenella_B`. NCBI
# genus names never contain an underscore, so stripping this suffix is
# unambiguous, and two GTDB splits of one genus are not two different genera.
_GTDB_GENUS_SUFFIX = re.compile(r"_[a-z]$")


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


_warned_no_adapter = False


def _warn_once_if_unavailable() -> None:
    """Say so when the whole check is being skipped for want of NCBITaxon.

    Without this a green `validate-strict` on a machine with no NCBITaxon
    database reads as "no id is reused for two organisms", when in fact nothing
    was looked at (#426). Stderr, not a failure: refusing to run is the right
    behaviour on a bare checkout, but it should be visible.
    """
    global _warned_no_adapter
    if not _warned_no_adapter and _adapter() is None:
        _warned_no_adapter = True
        print(
            "[taxon-ids] NCBITaxon is unavailable, so the shared-id check (#292) "
            "was skipped, not passed.",
            file=sys.stderr,
        )


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
                return value.split(":", 1)[1].strip()
    return None


def is_specific(curie: str) -> bool:
    """Does this id denote a single organism? False when undetermined."""
    return (rank_of(curie) or "") in SPECIFIC_RANKS


@functools.lru_cache(maxsize=4096)
def known_cores(curie: str) -> frozenset:
    """Binomial cores of every name NCBITaxon itself recognises for this id.

    This is what keeps NCBI renames out of the gate. `preferred_term` preserves
    the source paper's name, so one species id legitimately carries both
    `Eubacterium rectale` and `Agathobacter rectalis` — different genus *and*
    different epithet, which is otherwise the strongest possible clash signal.
    Both are names NCBITaxon lists for `NCBITaxon:39491`, so both are the same
    organism and neither is evidence of a wrong id.

    Empty when the adapter is missing, which simply leaves the rank filter to
    decide as before.
    """
    adapter = _adapter()
    if adapter is None or not curie.startswith("NCBITaxon:"):
        return frozenset()
    names = []
    try:
        label = adapter.label(curie)
        if label:
            names.append(label)
        names.extend(adapter.entity_aliases(curie) or [])
    except Exception:
        return frozenset()
    return frozenset(core for core in (_core(n) for n in names) if core)


def _same_genus(first: str, second: str) -> bool:
    """Two genus tokens naming one genus.

    Beyond equality this absorbs the two ways the KB spells a genus without
    meaning a different one: a GTDB split suffix (`Olsenella_B`), and the
    abbreviation a paper uses after first mention (`B. subtilis` beside
    `Bacillus subtilis`).
    """
    first = _GTDB_GENUS_SUFFIX.sub("", first)
    second = _GTDB_GENUS_SUFFIX.sub("", second)
    if first == second:
        return True
    if len(first) == 1:
        return second.startswith(first)
    if len(second) == 1:
        return first.startswith(second)
    return False


def _names_disagree(first: str, second: str, rank: str | None, known: frozenset) -> bool:
    """Do two `preferred_term`s under one id name genuinely different taxa?

    The rank decides what counts as a disagreement, and this is the whole design:

    * a **genus** id legitimately hosts many species and many unnamed isolates —
      `Variovorax sp. BK119` through `BK752`, or a named species beside an
      `sp.` — so only a differing *genus* is a contradiction there;
    * a **species**-or-finer id denotes one organism, so a differing *epithet* is
      a contradiction: `Bacteroides ovatus` and `Bacteroides vulgatus` cannot
      both be `NCBITaxon:821`.

    Two names that NCBITaxon *both* lists for the id are exempt whatever the
    rank: that is a rename, not a clash — see `known_cores`.

    Names that are not binomials at all fall back to "no disagreement". A guild
    label like `rhizosphere Actinobacteria` says nothing this check can use, and
    guessing from it is how a gate becomes noise.
    """
    left, right = _core(first), _core(second)
    if left is None or right is None:
        return False
    if left in known and right in known:
        return False
    if not _same_genus(left[0], right[0]):
        return True
    return rank not in ("genus", "subgenus") and left[1] != right[1]


def check_record(taxonomy: list) -> list[str]:
    """Messages for each specific id shared by genuinely different organisms.

    Malformed input is skipped rather than raised on. This runs inside
    `validate_strict`, whose whole job is to report bad records — a record so
    malformed that `taxonomy` holds a non-mapping is exactly what the schema
    validator in that same pass diagnoses properly, and an exception here would
    abort the run and discard every other file's findings (#429).
    """
    if not isinstance(taxonomy, list):
        return []
    by_id: dict[str, list[str]] = {}
    for entry in taxonomy:
        if not isinstance(entry, dict):
            continue
        term_block = entry.get("taxon_term")
        if not isinstance(term_block, dict):
            continue
        term = term_block.get("term")
        if not isinstance(term, dict):
            continue
        curie = term.get("id") or ""
        name = term_block.get("preferred_term") or term.get("label") or ""
        if not isinstance(curie, str) or not isinstance(name, str):
            continue
        if curie and name and name not in by_id.get(curie, []):
            by_id.setdefault(curie, []).append(name)

    _warn_once_if_unavailable()
    problems = []
    for curie, names in sorted(by_id.items()):
        # Cheap test first. Asking NCBITaxon for a rank opens a large SQLite
        # database, and only a handful of ids in a record are shared at all —
        # ordering this the other way meant ~1000 lookups per KB sweep instead
        # of ~15, and the scan took minutes rather than seconds.
        if len(names) < 2:
            continue
        if not is_specific(curie):
            continue
        rank = rank_of(curie)
        known = known_cores(curie)
        clashing: set[str] = set()
        for i in range(len(names)):
            for j in range(i):
                if _names_disagree(names[i], names[j], rank, known):
                    clashing.update((names[i], names[j]))
        if not clashing:
            continue
        problems.append(
            f"{curie} ({rank}) is used for taxa that cannot all be it: "
            + ", ".join(repr(n) for n in sorted(clashing))
        )
    return problems
