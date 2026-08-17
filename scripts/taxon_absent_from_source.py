#!/usr/bin/env python3
"""Find taxa that appear in NO cited source, under any name (#605).

A membership claim can be backed by verbatim, validating snippets and still be
unsupported. `Synechococcus_Yarrowia_SPC` asserts *Yarrowia lipolytica* on a
paper whose three heterotrophs are *B. subtilis*, *E. coli* and *S. cerevisiae*;
`PGM_Spent_Catalyst_Bioleaching` asserts *Thiobacillus thioparus* on two papers
that never mention it. Every snippet in both records is a real quote. That is the
failure mode snippet validation structurally cannot see, because it checks
whether the quote is real, not whether the quote supports the claim.

The obvious detector — "is this taxon's genus in the paper?" — does not work on
its own. Run naively it returns ~79 hits, and most are **nomenclature
modernisation**: the KB uses `Mediterraneibacter gnavus` and the paper, being
older, writes `Ruminococcus gnavus`. Flagging those would be worse than not
checking, because they are correct curation.

So the question has to be asked properly: does the current name **or any of its
NCBITaxon synonyms** appear? Only what survives that is a candidate defect.

Usage:
    uv run python scripts/taxon_absent_from_source.py            # summary
    uv run python scripts/taxon_absent_from_source.py --list     # every hit
    uv run python scripts/taxon_absent_from_source.py --drift    # renamings only

Needs the NCBITaxon OAK adapter, so it is a script rather than a test: the
blocking gate is deliberately pure arithmetic with no ontology download.
"""

from __future__ import annotations

import pathlib
import re
import subprocess
import sys

import yaml

REPO = pathlib.Path(__file__).resolve().parent.parent
COMMUNITIES = REPO / "kb/communities"
CACHE = REPO / "references_cache"

FULL_TEXT_MARKERS = ("===== OPEN-ACCESS FULL TEXT", "Full text (re-fetched")

# Ranks and prefixes that cannot discriminate: a paper about anything microbial
# contains "Bacteria", and "Candidatus" is a status marker rather than a name.
# "Bacterium" belongs here for a reason worth stating: it is a real obsolete
# genus that survives in NCBITaxon synonyms — Thiobacillus thioparus carries
# "Bacterium thioparum" — and it appears in essentially every microbiology
# paper, so it rescued a known-bad claim as if it were a renaming.
UNINFORMATIVE = {
    "bacteria",
    "bacterium",
    "archaea",
    "fungi",
    "eukaryota",
    "viruses",
    "cellular",
}
STATUS_PREFIXES = {"candidatus", "ca."}

# Rank suffixes. A paper naming the genus Thermotoga supports a claim about the
# phylum Thermotogota, and one writing "Ignavibacteria" supports
# "Ignavibacteriota" — whole-word matching called both absent. Truncating to the
# stem and matching as a PREFIX fixes it, while the leading \b keeps the match
# honest: "\bThiobacill" still does not match "Acidithiobacillus", which is a
# different genus the PGM paper does name and which must not rescue that claim.
_RANK_SUFFIXES = ("ota", "ales", "aceae", "ineae", "mycetes", "phyceae", "ia", "a")
_MIN_STEM = 6


def stem_of(word: str) -> str:
    """`word` reduced to a stem long enough to stay specific."""
    for suffix in _RANK_SUFFIXES:
        if word.lower().endswith(suffix) and len(word) - len(suffix) >= _MIN_STEM:
            return word[: -len(suffix)]
    return word


def cached_text(reference: str) -> str:
    """Every cached word for a reference — abstract included.

    **Abstracts count here, and that is the opposite of the rule in the
    cultivation check.** There, an abstract-only cache is excluded because
    growth conditions live in Methods, so matching against an abstract measures
    cache depth rather than support (#577). Membership is different: a paper
    almost always names its organisms in the abstract, so an abstract that names
    a taxon is real evidence for it.

    Importing the cultivation rule here produced a false positive worth naming.
    `Ferroplasma_Leptospirillum_Syntrophy` was reported as claiming
    *Leptospirillum ferriphilum* unsupported, while one of its two references —
    a 2.8 KB abstract with no full-text marker — names "ferriphilum" six times.
    The check had skipped the file that answered the question.
    """
    stem = str(reference).replace(":", "_").replace("/", "_")
    parts = []
    for suffix in (".md", ".txt"):
        path = CACHE / f"{stem}{suffix}"
        if path.is_file():
            parts.append(path.read_text(errors="replace"))
    return " ".join(" ".join(parts).split())


def has_full_text(reference: str) -> bool:
    """Whether a reference has retrieved full text, not just an abstract.

    Used to decide whether ABSENCE is worth reporting, which is a different
    question from what to MATCH against. Matching uses every cached word,
    including abstracts, because a paper names its organisms there. But absence
    from an abstract alone means little — an abstract will not list every minor
    member — so reporting it would bury the real cases: allowing abstract-only
    references to be reported took this list from 17 entries to 78.
    """
    stem = str(reference).replace(":", "_").replace("/", "_")
    for suffix in (".md", ".txt"):
        path = CACHE / f"{stem}{suffix}"
        if path.is_file() and any(m in path.read_text(errors="replace") for m in FULL_TEXT_MARKERS):
            return True
    return False


def aliases(curie: str) -> set[str]:
    """Every label and synonym NCBITaxon carries for this id."""
    result = subprocess.run(
        ["uv", "run", "runoak", "-i", "sqlite:obo:ncbitaxon", "aliases", curie],
        capture_output=True,
        text=True,
        cwd=REPO,
    )
    names = set()
    for line in result.stdout.splitlines()[1:]:
        parts = line.split("\t")
        if len(parts) >= 3 and parts[2].strip():
            names.add(parts[2].strip())
    return names


# NCBITaxon synonyms are not clean names. They arrive quoted and carrying
# authorship, e.g. '"""Candidatus Eisenbacteria"" Anantharaman et al. 2016"' and
# 'Mediterraneibacter gnavus (Moore et al. 1976) Togo et al. 2023'. Left as-is,
# the first of those yielded the search key '"""Candidatus' and reported
# Mercury_SFA_EFPC_Sediment_Community as making an unsupported claim — while its
# source names "Eisenbacteria" three times.
_AUTHORSHIP = re.compile(
    r"\s*\(?[A-Z][A-Za-z-]+(?:\s+(?:and|&)\s+[A-Z][A-Za-z-]+)?"
    r"(?:\s+et\s+al\.?)?,?\s*\d{4}\)?\s*$"
)


def clean_name(name: str) -> str:
    """A synonym reduced to the name itself, without quotes or authorship."""
    name = name.replace('"', " ").replace("'", " ")
    previous = None
    while previous != name:  # authorship can be stacked: "(Moore 1976) Togo 2023"
        previous = name
        name = _AUTHORSHIP.sub("", name).strip()
    return " ".join(name.split())


def search_keys(name: str, *, require_capital: bool = True) -> list[str]:
    """The distinctive word(s) to look for in a source, from one name.

    The genus alone, because a source may write "R. gnavus" or give the species
    only in a table. Names whose head word cannot discriminate are dropped
    rather than counted either way.

    `require_capital` is False for synonyms. NCBITaxon stores many of them
    lower-cased — `Bacillota` carries "firmicutes", `Cyanobacteriota` carries
    "cyanobacteria" — and requiring a capital threw every one of those away, so
    twenty phylum renamings were being reported as unsupported claims. Matching
    is case-insensitive anyway; the capital was only ever a proxy for "looks
    like a proper name", and it is the wrong proxy here.
    """
    words = clean_name(name).split()
    if words and words[0].lower() in STATUS_PREFIXES:
        words = words[1:]
    if not words:
        return []
    head = words[0]
    if len(head) < 5 or head.lower() in UNINFORMATIVE:
        return []
    if require_capital and not head[0].isupper():
        return []
    return [head]


def mentions(name: str, text: str) -> bool:
    """Does `text` name this taxon, allowing a rank change but not a substring?

    The one place the matching rule lives. It was inline in `main()`, and the
    test file re-implemented it — so removing the leading word boundary here
    changed nothing that any test could see, and the safety property the whole
    loosening depends on was unpinned. A test that rebuilds the logic it is
    checking is not checking it.

    The leading `\b` is that property: `Thiobacillus` must not match inside
    `Acidithiobacillus`.
    """
    return bool(re.search(rf"\b{re.escape(stem_of(name))}", text, re.IGNORECASE))


def taxa(document: object):
    """(label, curie, [references]) for every taxonomy entry with evidence."""
    for entry in (document or {}).get("taxonomy", []) or []:
        term = (entry.get("taxon_term") or {}).get("term") or {}
        label, curie = term.get("label"), term.get("id")
        refs = [e.get("reference") for e in (entry.get("evidence") or []) if e.get("reference")]
        if label and curie and refs:
            yield label, curie, refs


def main() -> int:
    list_all = "--list" in sys.argv
    drift_only = "--drift" in sys.argv

    absent, drift, checked = [], [], 0
    for path in sorted(COMMUNITIES.glob("*.yaml")):
        document = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        for label, curie, refs in taxa(document):
            texts = [t for t in (cached_text(r) for r in refs) if t]
            if not texts:
                continue  # nothing cached; not this script's business
            # Match against everything, but only report absence where at least
            # one reference has real full text behind it.
            if not any(has_full_text(r) for r in refs):
                continue
            keys = search_keys(label)
            if not keys:
                continue
            checked += 1
            if any(re.search(rf"\b{re.escape(stem_of(k))}", t, re.I) for k in keys for t in texts):
                continue

            # Current name is absent. Before calling it unsupported, ask whether
            # the source uses an older name for the same NCBITaxon id.
            hit = None
            for name in aliases(curie):
                if name == label:
                    continue
                keys_for = search_keys(name, require_capital=False)
                if not keys_for:
                    continue
                # A synonym must match MORE strictly than the primary name.
                # Genus alone is right for the primary check, since a paper may
                # write "R. gnavus" — but for a synonym it is a licence to
                # forgive: "Candida lipolytica" is a synonym of Yarrowia
                # lipolytica, and matching only "Candida" cleared a claim on a
                # paper that discusses an unrelated Candida. Require the species
                # epithet too, so the rescue is about THIS organism.
                # From the CLEANED, prefix-stripped name. Using the raw string
                # here looked for 'Eisenbacteria""' and never matched, so the
                # quote fix above did nothing on its own.
                parts_of = clean_name(name).split()
                if parts_of and parts_of[0].lower() in STATUS_PREFIXES:
                    parts_of = parts_of[1:]
                epithet = parts_of[1] if len(parts_of) > 1 else None
                needed = keys_for + ([epithet] if epithet and len(epithet) > 3 else [])
                if all(any(mentions(k, t) for t in texts) for k in needed):
                    hit = " ".join(needed)
                    break
            if hit:
                drift.append((path.name, label, hit))
            else:
                absent.append((path.name, label, curie, refs))

    print(f"# {checked} taxon claims checked against a full-text source")
    print(f"  nomenclature drift (source uses an older name): {len(drift)}")
    print(f"  ABSENT under every known name:                  {len(absent)}")

    if drift_only or list_all:
        print("\n# Drift — correct curation, source is simply older")
        for name, label, hit in drift:
            print(f"  {name[:52]:52} {label} <- source says {hit}")

    if list_all or not drift_only:
        print("\n# Absent under every NCBITaxon synonym — candidate #605 defects")
        for name, label, curie, refs in absent:
            print(f"  {name[:52]:52} {label} ({curie})  refs={refs}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
