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

from communitymech.paths import default_record_roots

REPO = pathlib.Path(__file__).parent.parent
CACHE = REPO / "references_cache"


def _record_paths() -> list[pathlib.Path]:
    """Every `MicrobialCommunity` record, from the shared root list (#529).

    This module globbed `kb/communities` alone. `data/isolates` holds records of
    the same root class, which may carry `cultivation_setup` and cite the same
    literature, and it was outside the sweep -- the defect `default_record_roots()`
    exists to prevent, and the one that produced #310 and #471 elsewhere.

    Harmless the day it was found: 4 isolate records, 0 with a `cultivation_setup`,
    so there was nothing to miss. The first isolate to gain one would have been
    skipped silently, with a clean report -- which is how the two issues above
    also began. `tests/test_record_roots_are_shared.py` did not catch this because
    its hard-coded-root scan reads `src/communitymech/**`, not `tests/`.
    """
    return [path for root in default_record_roots() for path in sorted(root.glob("*.yaml"))]


def _record_path(name: str) -> pathlib.Path | None:
    """Resolve a record filename against every root, not just the first."""
    for root in default_record_roots():
        candidate = root / name
        if candidate.is_file():
            return candidate
    return None


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
# scores 50% -- at the threshold, not below. Of its FOUR members, two are named
# and two (Sulfobacillus, Thiobacillus) appear zero times in the source; an
# earlier version of this comment said "three other members ARE named", which was
# simply wrong. Once the genus renamings above are resolved (#639) the other five
# records that sat at 0.50 rise to 75-100% and PGM is the only one left at the
# boundary -- so the ratio discriminates again instead of scoring it the same as
# five healthy records. A limit of this heuristic, not a clearance. Tracked in
# #605; dropping the waiver does not close it.

# Records that carry a `cultivation_setup` but that this discriminator cannot
# see at all -- it scores them zero times, in either direction (#529).
#
# The issue's own sentence is "the point is that the ratio is looked at once, by
# someone, rather than never." For these it is never, and until this list existed
# that fact was invisible: `_pairs()` drops them with a `continue` and the corpus
# assertion passes on what remains. Measured when this list was written: **30 of
# the 93 records carrying a `cultivation_setup` are blind, 32%.** A gate that
# silently omits a third of its subject is the "green by blindness" shape that
# produced #471 and #686 elsewhere in this repo.
#
# Four reasons, which fail differently:
#
# * `every member is domain-rank` -- the taxonomy is "Bacteria" / "Archaea" /
#   "cellular organisms". `_member_words` drops those deliberately (matching
#   "Bacteria" would pass any microbiology paper), so the record has no search
#   key left. This is a real limit of the heuristic, not a fixable extraction
#   bug: there is nothing in the record specific enough to look for. TEN of the
#   eleven carry a #183 commit touching them -- verified per record with
#   `git log origin/main --perl-regexp --grep '#183\b' -- <path>`, only
#   NCycle_Bioflocculation_Model_Consortium does not. So this is not a
#   correlation with the growth-conditions sweep, it is very nearly a
#   description of it: #183 selected records LACKING conditions, and those are
#   disproportionately environmental or metagenomic communities whose taxonomy
#   sits at domain rank. The sweep that added the conditions and the check that
#   would vet their sources have almost disjoint reach.
# * `no taxonomy members at all` -- one record, and a curation gap rather than a
#   heuristic limit: a named SynCom whose membership is unrecorded.
# * `no cited source has cached full text` -- the reference resolves only to an
#   abstract (< _FULL_TEXT_BYTES). The ratio would measure the cache rather than
#   the paper. Caching the full text moves the record into coverage, which is
#   why this list must be re-derived rather than trusted. Three entries arrived
#   with new records rather than from neglect: the sources for Methane_MFC,
#   Sedimenting_Arabinose and Waste_Sludge are not open access.
#   `just cache-fulltext` was run on PMID:42551599, PMID:41793807,
#   PMID:30010916 and PMID:42461012 and refused all four -- "not open-access in
#   Europe PMC (pmcid=None, oa=False)". Listing them is the honest outcome, not
#   a shortcut past caching.
# * `the cultivation_setup cites no reference at all` -- no record is in this
#   state, so the entry exists to keep the branch honest rather than to excuse
#   anything (see `_classify`).
#
# An exact-set assertion, not a bound: a record that BECOMES checkable has to
# leave, or the list rots into a permanent excuse the way `_ACCEPTED`'s ten
# entries did (#637).
# Named once. The reason strings are compared in three places -- the list, the
# classifier, and the known-reasons check -- and three copies of a literal is how
# they drift apart.
_DOMAIN_RANK = "every member is domain-rank"
_NO_MEMBERS = "no taxonomy members at all"
_NO_FULL_TEXT = "no cited source has cached full text"
_NO_REFERENCES = "the cultivation_setup cites no reference at all"
_BLIND_REASONS = frozenset({_DOMAIN_RANK, _NO_MEMBERS, _NO_FULL_TEXT, _NO_REFERENCES})

_BLIND_BY_REASON: dict[str, tuple[str, ...]] = {
    _DOMAIN_RANK: (
        "California_Grassland_Precipitation_Legacy_Soil_Community.yaml",
        "Coastal_Forested_Wetland_Seawater_Ion_Microcosm_Community.yaml",
        "LBNL_Brachypodium_Drought_SynCom15.yaml",
        "LBNL_Human_Gut_Interaction_SynCom.yaml",
        "Maize_Benzoxazinoid_Metabolizing_SynComs.yaml",
        "NCycle_Bioflocculation_Model_Consortium.yaml",
        "PSY_Transgenic_Rice_Rhizosphere_Methane_Community.yaml",
        "SkinCom_Synthetic_Skin_Community.yaml",
        "South_Bay_Salt_Pond_Methane_Restoration_Community.yaml",
        "Wetland_Oxygen_Sulfate_GHG_Microcosm_Community.yaml",
        "hCom2_Complex_Gut_Microbiome.yaml",
    ),
    _NO_MEMBERS: ("Multi_stage_Anaerobic_Digestion_SynCom_YSJ_and_SynCom_J.yaml",),
    _NO_FULL_TEXT: (
        "Methane_MFC_Electrogenesis_Nitrogen_Fixation_Consortium.yaml",
        "Sedimenting_Arabinose_Glucose_Saccharomyces_Coculture.yaml",
        "Waste_Sludge_Electrofermentation_Biofilm_Suspension_Community.yaml",
        "Aalborg_East_Full_Scale_EBPR_Community.yaml",
        "Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml",
        "Caldicellulosiruptor_TwoSpecies_Hydrogen_Coculture.yaml",
        "Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml",
        "Clostridium_Thermocellum_Saccharoperbutylacetonicum_Cellulosic_Butanol_Coculture.yaml",
        "Defined_Multispecies_Enamel_Caries_Model.yaml",
        "Electrostimulated_Mixotrophic_VFA_Producing_Enrichment_Consortium.yaml",
        "Industrial_Bioreactor_Consortium.yaml",
        "Lunar_Martian_Simulant_PGPB_Lettuce_SynCom.yaml",
        "Ostreococcus_Dinoroseobacter_BVitamin_Mutualism.yaml",
        "Pseudomonas_stutzeri_Rhodococcus_Naphthalene_Biochar_Engineered_Consortium.yaml",
        "Rammelsberg_Cobalt_Nickel_Tailings.yaml",
        "Shewanella_Geobacter_Exoelectrogenic_Biofilm_Community.yaml",
        "Trichoderma_Lactate_Platform.yaml",
        "Urine_Nitrification_SynCom.yaml",
    ),
}

_BLIND: dict[str, str] = {
    name: reason for reason, group in _BLIND_BY_REASON.items() for name in group
}

# The checked population when `_BLIND` was measured. A floor, not a target: the
# previous guard asserted `>= 1`, which would have passed if coverage collapsed
# from 67 pairs to one.
_CHECKED_PAIRS_FLOOR = 60


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
    # NCBITaxon's root-adjacent label, and the least discriminating string here.
    # It was already being dropped, but only incidentally: `head` is "cellular",
    # which fails the `head[0].isupper()` test. Capitalise the label and
    # "Cellular" survives the filter and gets searched for. Two records
    # (Wetland_Oxygen_Sulfate_GHG_Microcosm, Coastal_Forested_Wetland_Seawater_Ion)
    # carry it today, so the skip is load-bearing and should not rest on casing.
    "cellular",
    "cellular organisms",
    "bacteria",
    "archaea",
    "fungi",
    "eukaryota",
    "viruses",
    "microorganisms",
    "prokaryotes",
}


# The cache filenames as they exist on disk, keyed by lowercase name. Built once.
#
# `references_cache/` uses two conventions for the same prefix -- 133 files named
# `DOI_*` and 79 named `doi_*` -- while every reference in the corpus writes
# `doi:` in lowercase. The stem convention (`reference.replace(":", "_")`) yields
# `doi_...`, so the `DOI_*` half is found only by a filesystem that ignores case.
#
# macOS ignores case and Linux does not, which is the whole failure: this module
# scored six records locally and reported them BLIND on CI, and the first
# diagnosis here blamed uncommitted files in the working tree -- wrong, and only
# disproved by hiding them and watching the result invert. 117 of the corpus's
# 514 distinct references (23%) resolve this way. Tracked in #690, which also
# covers the seven scripts and the upstream validator that share the convention;
# fixing the filenames is that issue's job, and this lookup stops the platform
# deciding what this check can see in the meantime.
_CACHE_BY_LOWER_NAME = {path.name.lower(): path for path in CACHE.glob("*") if path.is_file()}


def _cache_path(reference: str) -> pathlib.Path | None:
    stem = reference.replace(":", "_").replace("/", "_")
    for suffix in (".md", ".txt"):
        candidate = _CACHE_BY_LOWER_NAME.get(f"{stem}{suffix}".lower())
        if candidate is not None:
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


# Taxon names renamed since the sources were written, current -> prior.
# A record grounded to a CURRENT NCBITaxon phylum whose source predates the rename
# names none of its members by this check's reckoning, which reads as "the paper
# did not study this community" when the paper IS the record's own source. Nine of
# the ten waivers this module used to carry were only this. The note by _ACCEPTED
# predicted it: "adding entries one at a time is not the fix".
_PRIOR_NAME = {
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
    # --- genus rank (#639) ---
    # Where the corpus actually sits. Six of 65 pairs scored exactly 0.50 and
    # passed only because the comparison is strict; five were a renamed genus and
    # nothing else. Each verified against the cached source: the current name
    # appears ZERO times and the prior name repeatedly, so these are drift rather
    # than a source that is about something else.
    "Mediterraneibacter": "Ruminococcus",  # Ruminococcus 7x
    "Methanothrix": "Methanosaeta",  # Methanosaeta 9x
    "Nitratidesulfovibrio": "Desulfovibrio",  # Desulfovibrio 13x
    "Lachnoclostridium": "Clostridium",  # Clostridium 12x
    "Acetivibrio": "Clostridium",  # Clostridium 10x
    "Desmonostoc": "Nostoc",  # Nostoc 17x
    "Limnospira": "Arthrospira",  # Arthrospira 9x
}

# Prior names with MORE THAN ONE successor here. A split is weaker evidence than
# a rename: a paper saying "Clostridium" is not thereby about *Acetivibrio*,
# because the genus was carved up and most of it stayed elsewhere. `Euryarchaeota`
# was dropped from the table for exactly this reason (#640) -- Methanobacteriota,
# Halobacteriota and Thermoplasmatota all descend from parts of it, so matching on
# it would be a false pass in the one direction that matters.
#
# `Clostridium` is kept, and listed here rather than left looking like a rename,
# because both entries were checked against their own sources: each paper calls
# the organism by its full prior binomial (Clostridium thermocellum,
# C. clariflavum), so within these records the genus match is sound. The test
# below fails on any split NOT acknowledged here, so the next one cannot arrive
# silently.
_KNOWN_SPLIT_PRIORS = {"Clostridium"}


def _names_member(word: str, text: str) -> bool:
    """Does the source name this taxon, under its current or its prior name?"""
    for candidate in (word, _PRIOR_NAME.get(word)):
        if candidate and re.search(rf"\b{re.escape(candidate)}", text, re.IGNORECASE):
            return True
    return False


def _classify(path: pathlib.Path) -> tuple[list[tuple[str, str, float, int]], str | None]:
    """One record's scored pairs, and the reason it was blind (or None).

    Single-sourced deliberately. `_pairs()` and `_blind()` each used to decide
    "is this pair checkable" on their own, which is two implementations of one
    rule and the drift that #350 and #656 are both about -- and a blind list
    computed by a second copy of the rule can disagree with the check it
    documents while both look right.
    """
    document = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    setups = document.get("cultivation_setup") or []
    if not setups:
        return [], None  # out of scope entirely, not blind

    members = _member_words(document)
    if not members:
        return [], _NO_MEMBERS if not (document.get("taxonomy") or []) else _DOMAIN_RANK

    references = sorted(
        {
            evidence.get("reference")
            for setup in setups
            for evidence in (setup.get("evidence") or [])
            if isinstance(evidence, dict) and evidence.get("reference")
        }
    )
    if not references:
        # Distinct from "the cache is thin": there is nothing cited to look at.
        # No record is in this state today, so the branch is written from the
        # schema rather than from a case -- but labelling it "no cached full
        # text" would send someone to fetch a paper that was never named.
        return [], _NO_REFERENCES

    scored = []
    for reference in references:
        cached = _cache_path(reference)
        if cached is None:
            continue  # nothing to check against; not this test's business
        text = cached.read_text(errors="replace")
        if len(text) < _FULL_TEXT_BYTES:
            continue  # abstract-only: the ratio would measure the cache
        named = sum(1 for word in members if _names_member(word, text))
        scored.append((path.name, reference, named / len(members), len(members)))
    return scored, None if scored else _NO_FULL_TEXT


def _pairs() -> list[tuple[str, str, float, int]]:
    """(record, reference, share_of_members_named, member_count) for cached sources."""
    return [pair for path in _record_paths() for pair in _classify(path)[0]]


def _blind() -> dict[str, str]:
    """Records with a `cultivation_setup` that the discriminator never scores.

    Derived, never read from `_BLIND` -- a list that describes itself cannot
    notice that the corpus moved underneath it.
    """
    out: dict[str, str] = {}
    for path in _record_paths():
        reason = _classify(path)[1]
        if reason is not None:
            out[path.name] = reason
    return out


@pytest.fixture(scope="module")
def pairs() -> list[tuple[str, str, float, int]]:
    return _pairs()


@pytest.fixture(scope="module")
def blind() -> dict[str, str]:
    return _blind()


def test_there_are_pairs_to_check(pairs):
    """Guard: with nothing cached the check below passes on an empty list.

    The bound is the measured population rather than `>= 1`, which was the
    original and could not tell full coverage from near-total collapse.
    """
    assert len(pairs) >= _CHECKED_PAIRS_FLOOR, (
        f"only {len(pairs)} cultivation_setup/reference pairs are being checked, "
        f"below the floor of {_CHECKED_PAIRS_FLOOR} (67 when measured). Coverage "
        f"has collapsed -- check whether the reference cache or the member "
        f"extraction broke before lowering this number."
    )


def test_the_records_this_check_cannot_see_are_itemised(blind):
    """29% of the subject is invisible to the discriminator; say which 29% (#529).

    Both directions. A NEW blind record must be acknowledged rather than
    silently dropped, and a record that BECOMES checkable -- typically because
    its source got cached -- must leave the list, or `_BLIND` decays into a
    permanent excuse the way `_ACCEPTED` did before #637.
    """
    derived = _blind()
    appeared = sorted(set(derived) - set(_BLIND))
    disappeared = sorted(set(_BLIND) - set(derived))
    assert appeared == [], (
        "these records carry a `cultivation_setup` that this check cannot score, "
        "and are not acknowledged in `_BLIND` (#529):\n"
        + "\n".join(f"  {name}: {derived[name]}" for name in appeared)
        + "\n\nPrefer removing the blindness to recording it: cache the cited "
        "source's full text, or ground the members below domain rank. Add to "
        "`_BLIND` only when neither is possible."
    )
    assert disappeared == [], (
        "these are listed in `_BLIND` but are now scored normally -- take them "
        "out, an excuse that no longer applies is how the list stops meaning "
        "anything:\n" + "\n".join(f"  {name}" for name in disappeared)
    )
    changed = sorted(
        f"  {name}: listed as {_BLIND[name]!r}, now {derived[name]!r}"
        for name in set(derived) & set(_BLIND)
        if derived[name] != _BLIND[name]
    )
    assert changed == [], "the reason a record is blind has changed:\n" + "\n".join(changed)


def test_a_setup_citing_nothing_is_not_reported_as_a_thin_cache(tmp_path):
    """The one blindness reason no shipped record exercises.

    Zero records have a `cultivation_setup` with no evidence reference today, so
    without this the branch is unreachable and could say anything. Before it
    existed the record fell through to `no cited source has cached full text`,
    which would send a curator to fetch full text for a paper that was never
    cited in the first place.
    """
    path = tmp_path / "Nothing_Cited.yaml"
    path.write_text(
        yaml.safe_dump(
            {
                "taxonomy": [{"taxon_term": {"term": {"label": "Geobacter sulfurreducens"}}}],
                "cultivation_setup": [{"temperature": "30 C"}],
            }
        ),
        encoding="utf-8",
    )
    scored, reason = _classify(path)
    assert scored == []
    assert reason == _NO_REFERENCES, reason
    assert reason in _BLIND_REASONS


def test_the_blind_reasons_are_the_known_ones(blind):
    """A new reason string means the classifier changed and the notes did not."""
    unknown = sorted({reason for reason in blind.values() if reason not in _BLIND_REASONS})
    assert unknown == [], f"unrecognised blindness reasons: {unknown}"


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


def test_the_prior_name_is_what_makes_a_renamed_member_match():
    """The synonym table must be load-bearing, not decorative.

    Both ranks, because they fail differently. Removing the PHYLUM entries makes
    records fail outright. Removing the GENUS entries does not — those records
    fall back to exactly 0.50, which the strict `<` still passes, so the corpus
    assertion stays green while the table silently stops working. That is the
    "check that reports clean because it never ran" shape, and it is why each
    renamed genus is asserted here by name rather than left to the corpus.
    """
    phyla = "Dominant phyla were Actinobacteria, Firmicutes and Planctomycetes."
    for current in ("Actinomycetota", "Bacillota", "Planctomycetota"):
        assert _names_member(current, phyla), f"{current} does not match its prior name"
    assert not _names_member("Thermotogota", phyla), "matches a phylum the text never names"

    # One line per genus in the table, each phrased as its own source writes it.
    genera = [
        ("Mediterraneibacter", "cross-feeding with Ruminococcus gnavus"),
        ("Methanothrix", "acetoclastic Methanosaeta concilii dominated"),
        ("Nitratidesulfovibrio", "Desulfovibrio vulgaris Hildenborough"),
        ("Lachnoclostridium", "co-culture with Clostridium clariflavum"),
        ("Acetivibrio", "Clostridium thermocellum was grown"),
        ("Desmonostoc", "Nostoc muscorum UTAD_N213"),
        ("Limnospira", "Arthrospira platensis UTEX LB 2340"),
    ]
    for current, sentence in genera:
        assert _names_member(current, sentence), f"{current} does not match its prior name"
        assert not _names_member(
            current, "an unrelated study of Escherichia coli"
        ), f"{current} matches text naming neither it nor its prior name"


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
        path = _record_path(record)
        assert path is not None, f"{record} in _ACCEPTED no longer exists"
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


def test_no_unacknowledged_split_in_the_synonym_table():
    """Two current names sharing a prior name means a split, not a rename.

    A rename is 1:1 and the match is sound. A split is 1:many, and matching the
    ancestor is weak evidence that can pass a source which is about a different
    descendant — a false pass in the direction this whole module exists to catch.
    Mechanically detectable even though "is this really a rename?" is not.
    """
    successors: dict[str, list[str]] = {}
    for current, prior in _PRIOR_NAME.items():
        successors.setdefault(prior, []).append(current)

    splits = {
        prior: sorted(names)
        for prior, names in successors.items()
        if len(names) > 1 and prior not in _KNOWN_SPLIT_PRIORS
    }
    assert not splits, (
        "these prior names have several successors in _PRIOR_NAME, so matching "
        "them is a split rather than a rename and can pass a source about a "
        f"different descendant. Acknowledge in _KNOWN_SPLIT_PRIORS with a reason, "
        f"or drop the entry: {splits}"
    )

    unused = _KNOWN_SPLIT_PRIORS - {p for p, n in successors.items() if len(n) > 1}
    assert not unused, f"_KNOWN_SPLIT_PRIORS names priors that are not split: {unused}"
