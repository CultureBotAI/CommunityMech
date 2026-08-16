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
    # Four nomenclature modernisations, all surfaced at once when a fresh
    # retrieval round gave these references full text for the first time. In each
    # the KB uses the current name and the paper uses the one current when it was
    # written, so the ratio measures the renaming rather than the relevance.
    ("Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml", "PMID:37973815"): (
        "Mediterraneibacter gnavus is the 2021 renaming of Ruminococcus gnavus, "
        "which is what the paper writes."
    ),
    ("BioModels_MODEL2204300001_Kefir_Community_Model.yaml", "PMID:33398099"): (
        "Maudiozyma is the recent renaming of Kazachstania, which is what the " "paper writes."
    ),
    ("Cellulose_Methane_Quad_Culture_SynCom.yaml", "PMID:36847519"): (
        "Nitratidesulfovibrio vulgaris is the renaming of Desulfovibrio vulgaris, "
        "which is what the paper writes."
    ),
    ("MSC1_Dominant_Core.yaml", "PMID:32983014"): (
        "Bacteroidota is the renaming of Bacteroidetes, which is what the paper " "writes."
    ),
    ("SIHUMIx_Human_Intestinal_Model_Community.yaml", "PMID:33622394"): (
        "Lactiplantibacillus plantarum is the 2020 renaming of Lactobacillus "
        "plantarum, which is what the paper writes."
    ),
    ("Synthetic_Periphyton_Freshwater_Biofilm.yaml", "PMID:35869094"): (
        "Cyanobacteriota is the renaming of Cyanobacteria, which is what the " "paper writes."
    ),
    ("Thiocyanate_Afipia_Thiobacillus_Bioreactor_Community.yaml", "PMID:33897653"): (
        "Hyphomicrobiales is the renaming of Rhizobiales, which is what the " "paper writes."
    ),
    # NOT a renaming, and NOT accepted as correct. Recorded here only so the gate
    # stays meaningful for everything else while the defect is tracked: the record
    # claims Thiobacillus thioparus and neither of its two references mentions
    # Thiobacillus or thioparus at all. Both snippets are verbatim quotes and both
    # validate, which is exactly why nothing else catches it. See #605 — the same
    # shape as Synechococcus_Yarrowia_SPC. Remove this entry when the membership
    # is either re-cited or withdrawn.
    ("PGM_Spent_Catalyst_Bioleaching.yaml", "PMID:38138568"): (
        "KNOWN DEFECT, tracked in #605: Thiobacillus thioparus appears in no "
        "cited source. Not a nomenclature difference — the record separately "
        "lists the two Acidithiobacillus species the paper does name."
    ),
    ("Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml", "PMID:33531396"): (
        "Same nomenclature drift as Rifle, and surfaced by the same fix. The "
        "source IS this community — 'Acetylene-Fueled Trichloroethene Reductive "
        "Dechlorination in a Groundwater Enrichment Culture' — and it names the "
        "member eight times as the phylum 'Actinobacteria'. The KB grounds it to "
        "'Actinomycetota', the 2021 renaming, which appears in the paper zero "
        "times. The record previously passed only because its second member is "
        "the domain 'Bacteria', which matched vacuously; dropping uninformative "
        "labels removed that false pass and left the real drift visible."
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
# NOTE ON THIS LIST'S SHAPE. Eight of its entries are now nomenclature
# modernisation — the KB uses the current name, the paper uses the one current
# when it was written, and the ratio measures the renaming rather than the
# relevance. They arrive in batches, because each fresh retrieval round gives
# several references full text for the first time and they all fail at once.
#
# Adding entries one at a time is not the fix. The check should ask whether the
# current name OR ANY SYNONYM appears, resolved through NCBITaxon, at which point
# every one of those eight disappears and what remains is the interesting
# residue: members that appear under no name at all (#605). Recorded here rather
# than built because it needs an ontology lookup this module deliberately does
# not have — it is pure arithmetic so it can run in the blocking gate.
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
    words = []
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
            named = sum(
                1 for word in members if re.search(rf"\b{re.escape(word)}", text, re.IGNORECASE)
            )
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
    named = sum(1 for word in members if re.search(rf"\b{re.escape(word)}", text, re.IGNORECASE))
    assert named / len(members) < _THRESHOLD, (
        "PMID:33841379 now names most of that record's members. If the record "
        "or the cache changed, re-check whether the paper studies the coculture "
        "— the whole point of #529 is that it does not"
    )
