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
# EMPTY as the result of a fix, not for never having been used.
#
# All ten entries became obsolete at once when `_member_words` stopped discarding
# all but the last member (#637) and `_names_member` learned the ICNP phylum
# renamings. Nine were pure nomenclature -- the KB writing Actinomycetota where a
# 2020 paper writes Actinobacteria -- exactly as the note below predicted. They
# now score 50-100% unaided.
#
# ONE was not a renaming, and must not be forgotten because the arithmetic stopped
# flagging it. `PGM_Spent_Catalyst_Bioleaching.yaml` / PMID:38138568 claims
# *Thiobacillus thioparus*, which appears in no cited source; both its snippets
# are verbatim and both validate, which is why nothing else catches it. It now
# scores 50% -- at the threshold, not below -- because the record's three other
# members ARE named, so the ratio cannot see one fabricated member among several
# real ones. A limit of this heuristic, not a clearance. Tracked in #605; dropping
# it from this list does not close it.

# Below this share of members named in the source, the pairing is suspect.
#
# Strict `<`. `<=` is actively wrong: a two-member coculture scores 50% whenever
# the source abbreviates the second genus after first use
# ("T. thermosaccharolyticum"), which is normal scientific prose rather than a
# warning sign -- it flagged four records each already verified by reading.
#
# The cost of that, stated rather than left implicit: at two members this ratio
# cannot tell "the source names one partner and not the other" from "half the
# community". The rejected Methylacidiphilum case is precisely that, scoring 1/2,
# so the threshold does NOT catch the case this module was written for. An earlier
# comment here claimed it scored 0% and was caught with room to spare; that was an
# artefact of `_member_words` returning one member instead of two (#637). The
# finding is now pinned as a fact below rather than resting on arithmetic that
# cannot see it.
_THRESHOLD = 0.5

# Only full-text caches are checked. An abstract names few members by nature, so
# on abstract-only entries this ratio measures **cache depth, not relevance**:
# the first version of this file flagged five records whose caches are 3 KB, and
# missed the 47 KB one it was written for. 12 KB is the same bar used to pick
# candidates worth reading in the first place.
_FULL_TEXT_BYTES = 12_000

# Taxon labels too broad to discriminate. A record whose only "member" is
# `Bacteria` cannot be checked by this test: the word appears in essentially
# every microbiology paper, so matching it would be a false pass and failing on
# it is a false alarm. `NCycle_Bioflocculation_Model_Consortium` is the live
# case — its member is NCBITaxon `Bacteria` with the preferred term "N-cycle
# bacterial consortium members", and its source is titled "Establishing a
# co-culture aggregate of N-cycle bacteria...", i.e. exactly the right paper.
# Skipped with a reason rather than added to `_ACCEPTED`, because nothing is
# being excused — there is simply no name here to look for.
_UNINFORMATIVE_LABELS = {
    "bacteria",
    "archaea",
    "fungi",
    "eukaryota",
    "viruses",
    "microorganisms",
    "prokaryotes",
}


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
    # Accumulated separately from the per-entry split. `words` used to be both,
    # so `words = name.split()` discarded every member examined so far and the
    # function returned only the LAST member -- plus a duplicate of its own head
    # word, which also inflated the denominator. A 4-member record reported
    # "0% of 2 members" (#637). The check claimed to ask whether a paper names
    # the community, and asked about one taxon.
    heads: list[str] = []
    for entry in document.get("taxonomy") or []:
        term = entry.get("taxon_term") or {}
        name = (term.get("term") or {}).get("label") or term.get("preferred_term") or ""
        words = name.split()
        # "Candidatus" is a nomenclatural status marker, not a genus, so the
        # first word of "Candidatus Methylacidiphilum" is useless as a search
        # key — and it matches any paper that discusses any Candidatus taxon.
        # 53 taxa in the KB carry the prefix; every one of them was contributing
        # the same worthless word until this line existed.
        if words and words[0].lower() in {"candidatus", "ca."}:
            words = words[1:]
        head = words[0] if words else ""
        # A domain-rank label carries no discriminating power (see
        # _UNINFORMATIVE_LABELS): matching it would pass any microbiology paper,
        # so it is dropped rather than counted either way.
        if len(head) > 3 and head[0].isupper() and head.lower() not in _UNINFORMATIVE_LABELS:
            heads.append(head)
    return heads


# Phylum names the ICNP renamed in 2021-22 (Oren & Garrity), current -> prior.
# A record grounded to a CURRENT NCBITaxon phylum whose source predates the rename
# names none of its members by this check's reckoning, which reads as "the paper
# did not study this community" when the paper IS the record's own source. Nine of
# the ten waivers this module used to carry were only this. The note by _ACCEPTED
# predicted it: "adding entries one at a time is not the fix".
_PRIOR_PHYLUM_NAME = {
    "Actinomycetota": "Actinobacteria",
    "Bacillota": "Firmicutes",
    "Bacteroidota": "Bacteroidetes",
    "Pseudomonadota": "Proteobacteria",
    "Planctomycetota": "Planctomycetes",
    "Acidobacteriota": "Acidobacteria",
    "Verrucomicrobiota": "Verrucomicrobia",
    "Chloroflexota": "Chloroflexi",
    "Cyanobacteriota": "Cyanobacteria",
    "Nitrospirota": "Nitrospirae",
    "Spirochaetota": "Spirochaetes",
    "Methanobacteriota": "Euryarchaeota",
    "Thermoproteota": "Crenarchaeota",
    "Nitrososphaerota": "Thaumarchaeota",
    "Deinococcota": "Deinococcus-Thermus",
    "Fusobacteriota": "Fusobacteria",
    "Chlamydiota": "Chlamydiae",
    "Mycoplasmatota": "Tenericutes",
    "Synergistota": "Synergistetes",
    "Gemmatimonadota": "Gemmatimonadetes",
    "Armatimonadota": "Armatimonadetes",
    "Aquificota": "Aquificae",
    "Thermotogota": "Thermotogae",
    "Chlorobiota": "Chlorobi",
    "Elusimicrobiota": "Elusimicrobia",
    "Ignavibacteriota": "Ignavibacteriae",
}


def _names_member(word: str, text: str) -> bool:
    """Does the source name this taxon, under its current or its prior name?"""
    for candidate in (word, _PRIOR_PHYLUM_NAME.get(word)):
        if candidate and re.search(rf"\b{re.escape(candidate)}", text, re.IGNORECASE):
            return True
    return False


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
            named = sum(1 for word in members if _names_member(word, text))
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

    The corpus assertion passes today because every shipped record is fine --
    which is also what it would do if `_member_words` returned nothing or the
    cache lookup missed every file. Synthetic input, because no shipped record
    can serve: a record scoring below the threshold would be a corpus bug, so the
    only honest failing case is a made-up one.

    This used to run the arithmetic on the real Methylacidiphilum example and
    require it to score below the threshold. It did -- but only because
    `_member_words` returned one member instead of two (#637). Corrected, it
    scores exactly 1/2, so it no longer demonstrates anything about the check.
    """
    document = {
        "taxonomy": [
            {"taxon_term": {"term": {"label": "Methanocaldococcus jannaschii"}}},
            {"taxon_term": {"term": {"label": "Pyrococcus furiosus"}}},
        ]
    }
    members = _member_words(document)
    assert members == ["Methanocaldococcus", "Pyrococcus"], members

    absent = "A study of Escherichia coli grown in a chemostat. Nothing else was cultured."
    assert sum(1 for w in members if _names_member(w, absent)) / len(members) < _THRESHOLD

    # ...and it must NOT fire when the source does name them, or it would flag
    # everything and be switched off.
    present = "We cocultured Methanocaldococcus jannaschii with Pyrococcus furiosus."
    assert sum(1 for w in members if _names_member(w, present)) / len(members) >= _THRESHOLD


def test_the_prior_phylum_name_is_what_makes_a_renamed_member_match():
    """The synonym table must be load-bearing, not decorative."""
    text = "Dominant phyla were Actinobacteria, Firmicutes and Planctomycetes."
    for current in ("Actinomycetota", "Bacillota", "Planctomycetota"):
        assert _names_member(current, text), f"{current} does not match its prior name"
    assert not _names_member("Thermotogota", text), "matches a phylum the text never names"


def test_the_rejected_coculture_source_still_never_names_the_alga():
    """The #529 finding itself, as a fact rather than as a ratio.

    `Methylacidiphilum_Galdieria_Thermoacidophilic_Coculture` has 47k characters
    of cached full text describing a LABFORS 3 bioreactor, and curating those
    numbers would have been wrong because the source is a *Methylacidiphilum*
    monoculture study. The evidence for that is not a percentage -- it is that
    *Galdieria* appears zero times. Pinned directly, so the finding survives
    further changes to the threshold or the extraction, both of which have now
    moved three times.
    """
    cached = _cache_path("PMID:33841379")
    assert cached is not None, "the rejected example's source is no longer cached"
    text = cached.read_text(errors="replace")

    assert not re.search(r"\bGaldieria", text, re.IGNORECASE), (
        "PMID:33841379 now mentions Galdieria -- re-check whether it studies the "
        "coculture after all, since #529 rests on it not doing so"
    )
    assert re.search(r"\bMethylacidiphilum", text, re.IGNORECASE), (
        "the source no longer names Methylacidiphilum either, so this is not the "
        "paper #529 was about and the pairing needs re-checking from scratch"
    )


def test_no_accepted_entry_is_dead():
    """A waiver that no longer fires is a decision nobody is making.

    All ten entries became obsolete at once when the member extraction was fixed
    (#637), and each would have gone on excusing a record that no longer needed
    excusing -- including one that was a real defect (#605) rather than a
    renaming, whose note would have sat in the list looking settled.

    Vacuous while the list is empty, deliberately: it becomes load-bearing the
    moment someone adds an entry, which is exactly when it is needed.
    """
    stale = []
    for (record, reference), reason in _ACCEPTED.items():
        path = COMMUNITIES / record
        assert path.is_file(), f"{record} in _ACCEPTED no longer exists"
        assert reason.strip(), f"{record}/{reference} is excused without a reason"
        document = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        members = _member_words(document)
        cached = _cache_path(reference)
        if not members or cached is None:
            continue
        text = cached.read_text(errors="replace")
        if len(text) < _FULL_TEXT_BYTES:
            continue
        named = sum(1 for word in members if _names_member(word, text))
        if named / len(members) >= _THRESHOLD:
            stale.append(f"  {record} / {reference}: now names {named}/{len(members)}")

    assert not stale, (
        "these _ACCEPTED entries no longer fire -- the check passes them on their "
        "own merits, so each waiver is dead and hides whatever it excused:\n" + "\n".join(stale)
    )
