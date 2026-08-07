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

"Named" is doing work there. An entry that gives only a strain code or an `sp.`
says nothing about *which* species it is, so it cannot contradict a named one —
`Marinobacter CS1` may well be the species it sits beside. Only two differing
*named* epithets are a contradiction.

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
# `Candidatus` is a status, not a name, and the epithet follows it. Stripping it
# is what `gtdb_ground._clean_label` already does for the same reason (#431).
_CANDIDATUS = re.compile(r"^candidatus\s+", re.IGNORECASE)
# `Genus STRAINCODE` — `Marinobacter CS1`, `Parabacteroides ASF519`. A strain
# code is not an epithet, so these name a genus and leave the species unsaid.
#
# The genus group is strict on purpose: a Latin genus is one capitalised word,
# lowercase after the first letter, optionally with a GTDB `_A` split suffix. A
# looser `[A-Za-z]...` read `soil DPANN archaea` as a genus named "soil" and
# `BGC-encoding CPR bacterium` as one named "bgc-encoding" — 11 KB guild labels
# in all, every one a fabricated genus that a differing neighbour would clash
# with (#448).
_STRAIN = re.compile(r"^([A-Z][a-z]+(?:_[A-Z])?)\s+([A-Z][A-Za-z0-9\-]*)(?:\s+(\S+))?")


def _looks_like_a_strain_code(token: str, following: str | None = None) -> bool:
    """A token that designates an isolate rather than a word of prose.

    Isolate codes carry a number. Either the token has a digit itself — `CS1`,
    `ASF519`, `PHNZY-24-6`, `Crocei1` — or it is a bare collection abbreviation
    whose number is the next token, as in `PCC 7002`. Requiring the
    abbreviation to be all-caps is what separates that case from prose: it
    rejects `Candidate Division OP3`, where `Division` is an ordinary word and
    the digits belong to a clade label, not a strain.

    Earlier versions were looser in two ways, both caught in review: accepting
    any all-caps token admitted `CPR`, `DPANN`, `DNA` and roman numerals, and
    accepting a digit anywhere downstream admitted `Candidate Division OP3`
    (#448).
    """
    if any(c.isdigit() for c in token):
        return True
    return token.isupper() and any(c.isdigit() for c in (following or ""))


def _core(name: str) -> tuple[str, str] | None:
    """(genus, epithet) for a Latin binomial, or None if the name is not one.

    Parentheticals and trailing strain codes are dropped before matching, so
    `Olsenella_B sp. (MAG ATO3)` reduces to `("olsenella_b", "sp")`.

    Two conventions the KB uses routinely are read as binomials (#431):

    * `Candidatus Genus epithet` — the prefix is a nomenclatural status, so
      `Candidatus Nitrosotalea devanaterra` is `("nitrosotalea", "devanaterra")`;
    * `Genus STRAINCODE` — `Marinobacter CS1` names a genus and *no* species, so
      it reduces to `("marinobacter", "sp")`, exactly as `Marinobacter sp. CS1`
      would. Two unnamed species under one genus id are then not a
      contradiction, while two different genera still are.

    Everything else that is not a binomial stays None, which is most of what
    this sees: 189 of the KB's distinct names still parse to None, nearly all
    guild labels like `13C-labeled rhizosphere bacteria` or `soil DPANN
    archaea`. They say nothing this check can use, and reading a genus out of
    one is how a gate starts firing on correct records — 12 names became
    parseable here, and every one is an organism.
    """
    cleaned = re.sub(r"\(.*?\)", " ", name or "").replace(".", " ")
    cleaned = _CANDIDATUS.sub("", cleaned.strip()).strip()
    # A provisional genus is bracketed in NCBI: `[Clostridium] scindens`.
    cleaned = cleaned.replace("[", "").replace("]", "")
    match = _CORE.match(cleaned)
    if not match:
        strain = _STRAIN.match(cleaned)
        if strain and _looks_like_a_strain_code(strain.group(2), strain.group(3)):
            return strain.group(1).lower(), "sp"
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
    if rank in ("genus", "subgenus"):
        return False
    # An unnamed species asserts nothing about *which* species, so it cannot
    # contradict a named one: `Marinobacter CS1` may well be the very species it
    # sits beside. Only two *named* epithets are a contradiction (#431). This
    # also covers the `sp.` spelling, which had the same latent false positive
    # before strain codes started reducing to `sp` as well.
    if "sp" in (left[1], right[1]):
        return False
    return left[1] != right[1]


def _says_unnamed_species(name: str) -> bool:
    """Does this name *literally* decline to name a species — `Genus sp.`?

    Distinct from `_core(...)[1] == "sp"`, which is also what a bare strain code
    reduces to. That difference is the whole of #449. `Marinobacter CS1` names a
    strain and may well *be* the species it sits beside, so sharing a species id
    with it is ordinary; `Marinobacter sp.` asserts the species is unnamed,
    which a named species id contradicts. Treating the two alike is what #447
    did, and it is right at genus rank and wrong at species rank.
    """
    core = _core(name)
    if core is None or core[1] != "sp":
        return False
    cleaned = re.sub(r"\(.*?\)", " ", name or "").replace(".", " ")
    cleaned = _CANDIDATUS.sub("", cleaned.strip()).strip()
    cleaned = cleaned.replace("[", "").replace("]", "")
    match = _CORE.match(cleaned)
    # Only the placeholder path counts. When `_CORE` does not match at all, the
    # `sp` came from the strain-code fallback.
    return bool(match and _PLACEHOLDER.match(match.group(2).lower()))


def _over_grounded(first: str, second: str, rank: str | None, known: frozenset) -> bool:
    """Is one of these an `sp.` sitting on an id that names a species (#449)?

    A different claim from `_names_disagree`, and reported separately. Neither
    name is wrong about the organism — nobody has said two incompatible things
    — but a species id asserts one named species, so an entry that declines to
    name one is grounded finer than it knows. That is the #292 shape with the
    `sp.` entry as the victim rather than the culprit.

    Genus rank is exempt, because a genus id legitimately hosts unnamed
    isolates; that is #447's point and it stands.
    """
    if rank in ("genus", "subgenus"):
        return False
    left, right = _core(first), _core(second)
    if left is None or right is None:
        return False
    if left in known and right in known:
        return False
    if not _same_genus(left[0], right[0]):
        return False  # a genuine clash, already reported by _names_disagree
    # Reuse the cores parsed above rather than re-deriving them: calling
    # _core again returns Optional, which is not indexable, and the guard that
    # makes it safe is several lines away.
    pairs = ((first, left), (second, right))
    unnamed = [n for n, _ in pairs if _says_unnamed_species(n)]
    named = [n for n, core in pairs if core[1] != "sp"]
    return len(unnamed) == 1 and len(named) == 1


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
        over: set[str] = set()
        for i in range(len(names)):
            for j in range(i):
                if _names_disagree(names[i], names[j], rank, known):
                    clashing.update((names[i], names[j]))
                elif _over_grounded(names[i], names[j], rank, known):
                    over.update((names[i], names[j]))
        if clashing:
            problems.append(
                f"{curie} ({rank}) is used for taxa that cannot all be it: "
                + ", ".join(repr(n) for n in sorted(clashing))
            )
        # Reported separately, and only where there is no clash to report: the
        # two are different claims. A clash says somebody is wrong about the
        # organism; this says nobody is wrong, but an entry that declines to
        # name a species is sitting on an id that names one (#449).
        if over and not clashing:
            problems.append(
                f"{curie} ({rank}) names a species, but is also used for an entry "
                f"that does not name one: " + ", ".join(repr(n) for n in sorted(over))
            )
    return problems
