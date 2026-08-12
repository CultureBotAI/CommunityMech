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
_ACCEPTED: dict[tuple[str, str], str] = {}

# At or below this share of members named in the source, the pairing is suspect.
# `<=`, not `<`: the case that motivated this is a two-member coculture whose
# source names exactly one of them, which is 50% — a strict `<` let the guilty
# record through while flagging five innocent ones.
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

    Deliberately loose. Matching a full `preferred_term` would miss
    "C. kluyveri", and matching any word would hit "sp." and "strain".
    """
    words = []
    for entry in document.get("taxonomy") or []:
        term = entry.get("taxon_term") or {}
        name = term.get("preferred_term") or (term.get("term") or {}).get("label") or ""
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
        if share <= _THRESHOLD and (record, reference) not in _ACCEPTED
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
    assert named / len(members) <= _THRESHOLD, (
        "PMID:33841379 now names most of that record's members. If the record "
        "or the cache changed, re-check whether the paper studies the coculture "
        "— the whole point of #529 is that it does not"
    )
