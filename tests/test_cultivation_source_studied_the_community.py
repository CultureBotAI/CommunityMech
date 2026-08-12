"""A cultivation_setup's source must be about *this* community (#529).

`Methylacidiphilum_Galdieria_Thermoacidophilic_Coculture` was the strongest
remaining #183 candidate by every mechanical measure: 47k characters of cached
full text and a methods section with a LABFORS 3 bioreactor, 2 L working volume,
45 °C, 450 rpm, fed-batch switched to chemostat. Its cited reference mentions
*Galdieria* **zero times** and "coculture" zero times — it is a
*Methylacidiphilum* monoculture study.

Curating those numbers would have been wrong in the way hardest to catch later:
every value individually correct, every snippet verbatim, `just validate` and
`just validate-references` both clean, and the record asserting that a two-member
coculture ran under conditions never applied to it.

`Soil_Corrinoid_B12_Reservoir_Community` is the same shape — scored 5/5 on
conditions belonging to an *E. coli* reporter strain, in a community that is
metagenomic and was never cultured. Only reading the record caught it.

What no existing gate can see: `validate-references` confirms a snippet is a
substring of the cited text. Nothing confirms the cited text is *about this
community*. This is the cheap discriminator — how many members the source names —
and it is deliberately a **heuristic with an escape hatch**, not a proof. A paper
can name every member and still report monoculture conditions, and a legitimate
apparatus paper may name none. The point is that the ratio is looked at once, by
someone, rather than never.
"""

from __future__ import annotations

import pathlib
import re

import pytest
import yaml

REPO = pathlib.Path(__file__).parent.parent
COMMUNITIES = REPO / "kb/communities"
CACHE = REPO / "references_cache"

# (record, reference) pairs where a low ratio is correct and understood. Each
# needs a reason: an empty allow-list entry is how the next Methylacidiphilum
# gets waved through.
_ACCEPTED: dict[tuple[str, str], str] = {
    ("Rifle_Aquifer_Bioanode_EET_Community.yaml", "PMID:32849356"): (
        "The paper studies this community — it is the metagenomic "
        "characterization of its anode-biofilm and planktonic fractions — but "
        "the KB records six of the seven members under current NCBI phylum "
        "names (Actinomycetota, Chloroflexota, Acidobacteriota, Bacillota, "
        "Pseudomonadota, Ignavibacteriota) that postdate the 2020 source, which "
        "writes Actinobacteria, Chloroflexi, and so on. Only Geobacter matches, "
        "so the ratio measures nomenclature drift rather than relevance."
    ),
}

# Below this share of members named in the source, the pairing is suspect.
#
# Strict `<`, and the boundary moved twice before settling. It was briefly `<=`,
# because under the old `preferred_term`-first extraction the rejected
# Methylacidiphilum case scored exactly 50% and a strict `<` let it through.
# Reading `term.label` first fixed the extraction and the case now scores **0%**
# — its members resolve to "Candidatus" and "Galdieria", neither in the source —
# so `<` catches it with room to spare.
#
# `<=` is actively wrong here: a two-member coculture scores 50% whenever the
# source abbreviates the second genus after first use ("T. thermosaccharolyticum"),
# which is normal scientific prose rather than a warning sign. It flagged four
# records that had each been verified by reading.
_THRESHOLD = 0.5

# Only full-text caches are checked. An abstract names few members by nature, so
# on abstract-only entries this ratio measures **cache depth, not relevance**:
# the first version of this file flagged five records whose caches are 3 KB, and
# missed the 47 KB one it was written for. 12 KB is the same bar used to pick
# candidates worth reading in the first place.
_FULL_TEXT_BYTES = 12_000


def _cache_path(reference: str) -> pathlib.Path | None:
    stem = reference.replace(":", "_").replace("/", "_")
    for suffix in (".md", ".txt"):
        candidate = CACHE / f"{stem}{suffix}"
        if candidate.is_file():
            return candidate
    return None


def _member_words(document: dict) -> list[str]:
    """One distinctive word per member — the genus, usually.

    Deliberately loose. Matching a full name would miss "C. kluyveri", and
    matching any word would hit "sp." and "strain".

    **`term.label` first, `preferred_term` second.** The original order was the
    other way round and produced nonsense on records whose members are described
    rather than named: `Rifle_Aquifer_Bioanode_EET_Community` has members like
    "EET-capable Rifle aquifer Actinobacteria", whose first word is "EET-capable"
    — extracted six times, matched never, and scored the record 0% of 6. The
    ontology label is an actual taxon name, which is what this check wants.
    """
    words = []
    for entry in document.get("taxonomy") or []:
        term = entry.get("taxon_term") or {}
        name = (term.get("term") or {}).get("label") or term.get("preferred_term") or ""
        head = name.split()[0] if name.split() else ""
        if len(head) > 3 and head[0].isupper():
            words.append(head)
    return words


def _pairs() -> list[tuple[str, str, float, int]]:
    """(record, reference, share_of_members_named, member_count) for cached sources."""
    found = []
    for path in sorted(COMMUNITIES.glob("*.yaml")):
        document = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        setups = document.get("cultivation_setup") or []
        if not setups:
            continue
        members = _member_words(document)
        if not members:
            continue
        references = {
            evidence.get("reference")
            for setup in setups
            for evidence in (setup.get("evidence") or [])
            if isinstance(evidence, dict) and evidence.get("reference")
        }
        for reference in sorted(references):
            cached = _cache_path(reference)
            if cached is None:
                continue  # nothing to check against; not this test's business
            text = cached.read_text(errors="replace")
            if len(text) < _FULL_TEXT_BYTES:
                continue  # abstract-only: the ratio would measure the cache
            named = sum(1 for word in members if re.search(rf"\b{re.escape(word)}", text))
            found.append((path.name, reference, named / len(members), len(members)))
    return found


@pytest.fixture(scope="module")
def pairs() -> list[tuple[str, str, float, int]]:
    return _pairs()


def test_there_are_pairs_to_check(pairs):
    """Guard: with nothing cached the check below passes on an empty list."""
    assert len(pairs) >= 1, (
        f"only {len(pairs)} cultivation_setup/reference pairs have a cached "
        f"source; this check is close to vacuous"
    )


def test_every_source_names_most_of_the_community(pairs):
    """The discriminator that would have caught the Methylacidiphilum case."""
    suspect = [
        f"  {record}: {reference} names {share:.0%} of {count} members"
        for record, reference, share, count in pairs
        if share < _THRESHOLD and (record, reference) not in _ACCEPTED
    ]
    assert suspect == [], (
        "these cultivation_setup blocks cite a source that barely mentions the "
        "community's members, which is how a monoculture's conditions get "
        "recorded as a coculture's (#529):\n"
        + "\n".join(suspect)
        + "\n\nCheck whether the paper actually studied this community. If it "
        "did and the names are simply written differently, add the pair to "
        "`_ACCEPTED` with the reason."
    )


def test_the_accepted_pairs_have_reasons_and_are_current(pairs):
    """An allow-list that outlives its entries stops meaning anything."""
    blank = sorted(key for key, why in _ACCEPTED.items() if not (why or "").strip())
    assert blank == [], f"accepted pairs need a reason: {blank}"
    known = {(record, reference) for record, reference, _, _ in pairs}
    stale = sorted(key for key in _ACCEPTED if key not in known)
    assert stale == [], f"these accepted pairs no longer exist: {stale}"


def test_the_check_can_actually_fail():
    """Mutation check, without touching the corpus.

    The assertion above passes today because every shipped record is fine —
    which is also what it would do if `_member_words` returned nothing, or the
    cache lookup silently missed every file. This runs the same arithmetic on
    the case that was rejected, and requires it to score below the threshold.
    """
    document = yaml.safe_load(
        (COMMUNITIES / "Methylacidiphilum_Galdieria_Thermoacidophilic_Coculture.yaml").read_text(
            encoding="utf-8"
        )
    )
    members = _member_words(document)
    assert len(members) >= 2, "the rejected example no longer has two named members"

    cached = _cache_path("PMID:33841379")
    assert cached is not None, "the rejected example's source is no longer cached"
    text = cached.read_text(errors="replace")
    named = sum(1 for word in members if re.search(rf"\b{re.escape(word)}", text))
    assert named / len(members) < _THRESHOLD, (
        "PMID:33841379 now names most of that record's members. If the record "
        "or the cache changed, re-check whether the paper studies the coculture "
        "— the whole point of #529 is that it does not"
    )
