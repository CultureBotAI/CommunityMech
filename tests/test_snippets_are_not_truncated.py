"""A snippet cut off mid-word, which no gate could see (#295).

`snippet` is meant to be a verbatim quote from the cited paper — the whole
evidence model rests on it. Four had been cut mid-word:

    "...to acetate or acetate and propionate usi"
    "...electron transfer and energy generation were upregu"
    "...branching at the base of the Thermo"
    "...couple the electron balance with o"

Nothing detected them. `validate-scalars` (#398) looks for a *different* defect
— a plain scalar swallowed by a `#` comment — and reports 0 here, correctly,
because these are well-formed scalars that merely stop early. And
`just validate-references` performs **zero** checks on these records (#466), so
the verbatim guarantee was never tested at all.

The check is the reviewer's: resolve each snippet against its cached source and
flag any that matches verbatim but is followed *in the source* by an
alphanumeric character. Cutting at a word boundary is legitimate — quoting half
a sentence is normal — so only a mid-word cut is evidence of damage.

Skips any reference with no cache entry, which is most of the DOI ones (#259).
That is a real limit: it can only check what has been fetched.
"""

from __future__ import annotations

import glob
import pathlib
import re

import pytest
import yaml

REPO = pathlib.Path(__file__).parent.parent
CACHE = REPO / "references_cache"
RECORD_DIRS = ("kb/communities", "kb/taxa", "data/isolates")

# (record, snippet's last word, what follows in the source) where the *cache* is
# at fault, not the snippet: the fetched markdown lost a space, so a complete
# word abuts the next one. `parvus` is the full species epithet and
# `cocultivated` a whole word — nothing is missing from the quote.
_CACHE_RUN_TOGETHER = {
    (
        "Methylocystis_Rhodococcus_Methane_VFA_PHBV_Coculture.yaml",
        "parvus",
        "cocultivated",
    ),
    # The abstract's italic taxon names lost their surrounding spaces when the
    # markdown was fetched, so "...related to Leptospirillum spp., Acidithiobacillus
    # ferrooxidans..." is cached as "...related toLeptospirillumspp.,Acidithiobacillus
    # ferrooxidans...". The snippet ends at "related to", which IS a word boundary in
    # the article; only the cache disagrees.
    #
    # This became visible when the DOI caches were renamed to the lowercase form the
    # stem convention produces (#690). Before that, `_cached` could not find
    # DOI_10.1128_aem.69.8.4853-4865.2003.md on Linux -- its fallback upper-cases the
    # WHOLE stem, so "doi_10.1128_aem..." became "DOI_10.1128_AEM...", which matches
    # nothing -- and the record was skipped on CI while failing on macOS, where the
    # filesystem ignores case.
    (
        "Tinto_River_Iron_Cycling_Community.yaml",
        "to",
        "Leptospirillumspp",
    ),
}


def _cached(reference: str) -> str:
    """The cached text for a PMID/DOI, or "" if it was never fetched."""
    key = reference.replace(":", "_").replace("/", "_")
    # `key.upper()` was a second pattern here, meant to catch the uppercase-prefix
    # caches. It never could: it upper-cases the WHOLE stem, so
    # "doi_10.1128_aem..." becomes "DOI_10.1128_AEM..." and matches no real
    # filename. The prefixes are canonically lowercase since #690, so the
    # fallback is dropped rather than fixed -- a pattern that cannot match is
    # worse than none, because it looks like coverage.
    for pattern in (f"{key}*",):
        for path in sorted(glob.glob(str(CACHE / pattern))):
            try:
                return " ".join(pathlib.Path(path).read_text().split())
            except OSError:
                continue
    return ""


def _snippets():
    """(record, reference, snippet) for every evidence item carrying one."""
    for directory in RECORD_DIRS:
        for path in sorted((REPO / directory).glob("*.yaml")):
            document = yaml.safe_load(path.read_text()) or {}
            stack = [document]
            while stack:
                node = stack.pop()
                if isinstance(node, dict):
                    ref, snip = node.get("reference"), node.get("snippet")
                    if isinstance(ref, str) and isinstance(snip, str) and snip.strip():
                        yield path.name, ref, snip
                    stack.extend(node.values())
                elif isinstance(node, list):
                    stack.extend(node)


def test_the_sweep_can_actually_check_things():
    """Guard: if nothing resolves against the cache, the next test is vacuous."""
    checkable = sum(
        1 for _, ref, snip in _snippets() if _cached(ref) and " ".join(snip.split()) in _cached(ref)
    )
    assert checkable > 500, (
        f"only {checkable} snippets resolved against references_cache/; the "
        f"truncation check below cannot mean much"
    )


def test_no_snippet_stops_mid_word():
    """A quote may end anywhere except inside a word.

    Ending at a word boundary is ordinary quoting. Ending inside one means the
    text was cut by something other than a curator — which is what happened to
    all four cases in #295, three of them in records where the *same* snippet
    appeared complete elsewhere.
    """
    truncated = []
    for record, reference, snippet in _snippets():
        source = _cached(reference)
        if not source:
            continue
        flat = " ".join(snippet.split())
        index = source.find(flat)
        if index < 0:
            continue  # a paraphrase rather than a quote — that is #347, not this
        after = source[index + len(flat) :]
        # A digit here is a citation marker the cached markdown ran together
        # with the preceding word ("...glutamate4"), not a cut word.
        if not after or not after[0].isalpha():
            continue
        tail = re.match(r"[A-Za-z]+", after).group(0)
        last = flat.split()[-1]
        if (record, last, tail) in _CACHE_RUN_TOGETHER:
            continue
        truncated.append(f"{record}: ...{last!r} is cut before {tail!r} ({reference})")

    assert truncated == [], (
        "these snippets stop mid-word, so they are not the quotes they claim to "
        "be — complete them from references_cache/ (#295):\n" + "\n".join(truncated)
    )


@pytest.mark.parametrize(
    ("record", "fragment"),
    [
        ("Geobacter_Clostridium_Interspecies_Electron_Transfer_Coculture.yaml", "with o"),
        ("Syntrophomonas_Methanospirillum_Syntrophy.yaml", "propionate usi"),
        ("Desulfovibrio_Methanococcus_Syntrophy.yaml", "were upregu"),
        ("Naica_Deep_Subsurface_Thermophilic.yaml", "the base of the Thermo"),
    ],
)
def test_the_four_known_truncations_stay_fixed(record: str, fragment: str):
    """Pinned by their tails, since three had a complete twin in the same file.

    That is what made them survive: a reader grepping the snippet found the
    intact copy and moved on.
    """
    for directory in RECORD_DIRS:
        path = REPO / directory / record
        if path.exists():
            assert (
                f"{fragment}\n" not in path.read_text()
            ), f"{record} carries the truncated form again: ...{fragment!r}"
            return
    raise AssertionError(f"{record} is gone; update this test")
