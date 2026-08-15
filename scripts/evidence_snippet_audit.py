#!/usr/bin/env python3
"""Audit evidence snippets against their cited reference's cached abstract.

For every EvidenceItem (any dict with both `reference` and `snippet`) in
kb/communities/*.yaml, locate the reference's cache file, strip the circular
"Quoted snippets used in curated records" list (so we match only against real
abstract text), normalize whitespace, and classify:

  MATCH      - snippet is a literal (whitespace-normalized) substring of the text
  RENDERING  - matches only after punctuation/whitespace/Greek normalization
               (e.g. record "10% CO 2" vs cached "10% CO2"): a faithful quote of
               the paper whose cache carries a PDF/XML extraction artefact. This
               is the class `just validate-references` reports as an error
  ASSEMBLED  - every comma/semicolon-separated part is in the source but the
               whole is not: cells joined from a table, or a quote welded from
               two places. Supported content, but not a verbatim quote (#596)
  MISMATCH   - real abstract content exists but the snippet is absent (suspect)
  NOCONTENT  - cache missing or stub-only (no abstract body to verify against)

Nearly all MISMATCH hits are a *retrieval* gap, not a curation one: 290 of 296
in the #596 survey sat on an abstract-only cache while quoting Methods. Run
`scripts/cache_fulltext.py` for the reference before reading a MISMATCH as a
bad snippet.

Usage: uv run python scripts/evidence_snippet_audit.py [--list-mismatch]
       [--list-nocontent] [--list-rendering] [--list-assembled]
"""

import difflib
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

COMM = Path("kb/communities")
# Repo-anchored (#407). Tests override this attribute; a relative default also
# resolved against the cwd, so importing the module from elsewhere read nothing.
CACHE = Path(__file__).resolve().parent.parent / "references_cache"
LIST_MM = "--list-mismatch" in sys.argv
LIST_NC = "--list-nocontent" in sys.argv
LIST_RD = "--list-rendering" in sys.argv
LIST_AS = "--list-assembled" in sys.argv

# Sections that contain curated/paraphrased snippets, not the real abstract.
# Stripping them prevents circular self-matching.
# Markers that introduce the REAL source text in a .md cache: the NCBI BioC PMC
# re-fetch header, and the marker appended by scripts/cache_fulltext.py. These
# must (a) terminate a curated-snippet section and (b) count as a real-content
# signal — without them a genuine full text that merely lacks YAML frontmatter
# was discarded, and the audit fell back to a short abstract .txt and reported
# every full-text snippet as a MISMATCH.
FULLTEXT_MARKER = re.compile(
    r"^(Full text \(re-fetched|=====\s*OPEN-ACCESS FULL TEXT)", re.MULTILINE
)
SNIPPET_SECTION = re.compile(
    r"(Quoted snippets used in curated records:|Key evidence used:|"
    r"Key snippets used in curated records:|Cached source notes:|"
    r"Snippets used in curated records:).*?"
    r"(?=\nURL:|\nDOI:|\n## |\nFull text \(re-fetched|\n=====\s*OPEN-ACCESS FULL TEXT|\Z)",
    re.DOTALL | re.IGNORECASE,
)
FRONTMATTER = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)
HEADER_LINES = re.compile(r"^(#+\s|Title:|Source:|URL:|DOI:|\*\*|reference_id:).*$", re.MULTILINE)
UNAVAILABLE = re.compile(r"content_type:\s*unavailable", re.IGNORECASE)
# A .md cache is treated as a REAL abstract only with an explicit signal:
REAL_CT = re.compile(r"content_type:\s*(abstract_only|abstract|full|fulltext)", re.IGNORECASE)
CONTENT_HEADING = re.compile(r"^##\s+(Content|Abstract)\b", re.MULTILINE | re.IGNORECASE)


def norm(s: str) -> str:
    return " ".join(s.split()).lower()


GREEK = {
    "α": "alpha",
    "β": "beta",
    "γ": "gamma",
    "δ": "delta",
    "ε": "epsilon",
    "ζ": "zeta",
    "η": "eta",
    "θ": "theta",
    "ι": "iota",
    "κ": "kappa",
    "λ": "lambda",
    "μ": "mu",
    "ν": "nu",
    "ξ": "xi",
    "ο": "omicron",
    "π": "pi",
    "ρ": "rho",
    "σ": "sigma",
    "ς": "sigma",
    "τ": "tau",
    "υ": "upsilon",
    "φ": "phi",
    "χ": "chi",
    "ψ": "psi",
    "ω": "omega",
}


# Typographic symbols a curator spells out when reading a rendered page, and
# the letters they spell them with. Needed because `alnum` strips punctuation
# but NOT letters: the cache's "(ATCC® 47054)" reduces to "atcc47054" while a
# record's "(ATCC(R) 47054)" keeps the R and reduces to "atccr47054", so a
# faithful quote lands in MISMATCH instead of RENDERING (#596). Mapping the
# symbol to the same letters makes the two agree.
SYMBOLS = {
    "®": "r",
    "™": "tm",
    "©": "c",
}


def alnum(s: str) -> str:
    """Lowercase, transliterate Greek and typographic symbols, keep only [a-z0-9].

    Robust to punctuation/whitespace spacing and Greek-letter vs spelled-out
    differences (e.g. abstract "β-5" vs snippet "beta-5")."""
    s = s.lower()
    for g, name in GREEK.items():
        s = s.replace(g, name)
    for symbol, spelled in SYMBOLS.items():
        s = s.replace(symbol, spelled)
    return re.sub(r"[^a-z0-9]", "", s)


# A snippet is "assembled" when every comma/semicolon-separated part of it is in
# the source but the whole is not. Two real shapes produce this:
#
#   * cells joined from a table — OMM12 quotes "Lactobacillus reuteri I49,
#     Enterococcus faecalis KB1, Blautia coccoides YL58", three non-adjacent rows
#     of a strain table, each present verbatim;
#   * a quote welded from two places — PET's "R. jostii was added to reduce the
#     inhibition caused by terephthalic acid" takes the opening of one sentence
#     and the tail of another 35KB away.
#
# Reported as its own bucket rather than folded into MATCH. The content is
# supported and it is not a fabrication, but it is *not a verbatim quote*, and
# a matcher loose enough to call it one would be loose enough to hide a real
# mismatch — which is the failure this whole audit exists to prevent.
_ASSEMBLED_MIN_PART = 12


def assembled_parts(snippet: str, content: str) -> list[str] | None:
    """The parts a non-matching snippet was assembled from, or None.

    None when the snippet has no multi-part structure, or when any substantial
    part is absent from the source — the latter stays a MISMATCH, since a
    snippet with an unsupported clause is not merely reformatted.
    """
    parts = [p.strip() for p in re.split(r"[;,]", snippet) if len(p.strip()) >= _ASSEMBLED_MIN_PART]
    if len(parts) < 2:
        return None
    haystack = alnum(content)
    if not all(alnum(p) in haystack for p in parts):
        return None
    return parts


def cache_text(reference: str) -> tuple[str, bool]:
    """Return (real_abstract_text, has_real_content) for a reference."""
    ref = reference.strip()
    if ref.lower().startswith("pmid:"):
        core = ref.split(":", 1)[1].strip()
    elif ref.lower().startswith("doi:"):
        core = ref.split(":", 1)[1].strip().replace("/", "_")
    else:
        core = ref.replace(":", "_").replace("/", "_")
    # find all cache files mentioning this id
    hits = [p for p in CACHE.iterdir() if core.lower() in p.name.lower()]
    if not hits:
        return "", False
    # Order by extension, then by name. The name is the tiebreak that matters:
    # a reference can have two files of the *same* suffix — 14 PMIDs have both
    # `PMID_<id>.txt` and `pmc_full_pmid_<id>.txt` — and since sort is stable,
    # without it their concatenation order was raw `iterdir` order, i.e. it
    # varied by filesystem (#306).
    hits.sort(key=lambda p: ({".txt": 0, ".md": 1, ".json": 2}.get(p.suffix, 3), p.name))
    real_bodies = []
    for p in hits:
        try:
            t = p.read_text(errors="ignore")
        except OSError:
            # An unreadable cache entry is not evidence of anything; skip it.
            continue
        if p.suffix == ".txt":
            # PubMed full dump — always real content
            real_bodies.append(t)
            continue
        if UNAVAILABLE.search(t):
            continue  # explicitly no abstract body
        # Only trust a .md as a real abstract with an explicit signal. A cached
        # full text counts: several were fetched without YAML frontmatter or a
        # `## Content` heading and were being discarded as stubs.
        if not (REAL_CT.search(t) or CONTENT_HEADING.search(t) or FULLTEXT_MARKER.search(t)):
            continue  # stub (notes + curated snippets only)
        fm = FRONTMATTER.sub("", t)  # drop YAML frontmatter
        stripped = SNIPPET_SECTION.sub("", fm)  # drop curated-snippet sections
        body = HEADER_LINES.sub("", stripped)  # drop title/source/url headers
        if len(norm(body)) >= 200:  # substantial prose remains => real abstract
            real_bodies.append(body)
    full = "\n".join(real_bodies)
    return full, bool(real_bodies)


def coverage(snip: str, content: str) -> float:
    s, c = alnum(snip), alnum(content)
    if not s:
        return 1.0
    if s in c:
        return 1.0
    m = difflib.SequenceMatcher(None, s, c).find_longest_match(0, len(s), 0, len(c))
    return m.size / len(s)


def walk(node, path, out):
    if isinstance(node, dict):
        if "reference" in node and "snippet" in node and isinstance(node.get("snippet"), str):
            out.append((path, str(node["reference"]), node["snippet"]))
        for k, v in node.items():
            walk(v, f"{path}.{k}", out)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            walk(v, f"{path}[{i}]", out)


def main() -> None:
    """Run the audit over the whole KB and print the report.

    Wrapped in a function so the resolution helpers above can be imported
    and tested without the module printing a full audit as a side effect
    of import (#306).
    """
    stats = defaultdict(int)
    file_mismatch = defaultdict(list)
    file_nocontent = defaultdict(int)
    file_rendering = defaultdict(int)
    file_assembled = defaultdict(list)
    cache_cache = {}

    for f in sorted(COMM.glob("*.yaml")):
        try:
            data = yaml.safe_load(f.read_text())
        except Exception as e:
            print(f"YAML ERROR {f.name}: {e}")
            continue
        items = []
        walk(data, f.name, items)
        for path, ref, snip in items:
            if ref not in cache_cache:
                cache_cache[ref] = cache_text(ref)
            content, has = cache_cache[ref]
            if not has:
                stats["NOCONTENT"] += 1
                file_nocontent[f.name] += 1
                continue
            cov = coverage(snip, content)
            # snippets that stitch non-contiguous excerpts with ".." / "…" are legit
            # if every fragment is itself present in the abstract
            if cov < 0.9 and re.search(r"\.\.+|…", snip):
                frags = [f for f in re.split(r"\.\.+|…", snip) if alnum(f)]
                if frags and all(coverage(f, content) >= 0.9 for f in frags):
                    cov = 1.0
            if cov >= 0.9:
                # Split literal quotes from ones that only match after punctuation /
                # whitespace / Greek normalisation (e.g. record "10% CO 2" vs cached
                # "10% CO2", "beta-5" vs "β-5"). Both are faithful quotes of the
                # PAPER — the spacing is a PDF/XML extraction artefact in the CACHE —
                # but `just validate-references` does strict substring matching and
                # reports exactly this class as an error. Counting it separately is
                # what reconciles the two gates (issue #257); do NOT "fix" these by
                # rewriting snippets to match the cache, which would propagate
                # artefacts like "mg/ L" into the records.
                if norm(snip) in norm(content):
                    stats["MATCH"] += 1
                else:
                    stats["RENDERING"] += 1
                    file_rendering[f.name] += 1
            elif assembled_parts(snip, content) is not None:
                # Every part is in the source; the join is not. Supported content,
                # but not a verbatim quote — kept out of both MATCH and MISMATCH
                # so it is neither blessed nor called a fabrication (#596).
                stats["ASSEMBLED"] += 1
                file_assembled[f.name].append((path, ref, snip[:70]))
            elif cov >= 0.6:
                stats["WEAK"] += 1
                file_mismatch[f.name].append((path, ref, round(cov, 2), snip[:70], "WEAK"))
            else:
                stats["MISMATCH"] += 1
                file_mismatch[f.name].append((path, ref, round(cov, 2), snip[:70], "MISMATCH"))

    total = sum(stats.values())
    print(f"# {total} evidence snippets scanned across {len(list(COMM.glob('*.yaml')))} files")
    for k in ("MATCH", "RENDERING", "ASSEMBLED", "WEAK", "MISMATCH", "NOCONTENT"):
        print(f"  {k:<10} {stats[k]}")

    print(
        "\n# Files with MISMATCH/WEAK (content present but snippet absent)"
        " — fabrication suspects"
    )
    ranked = sorted(file_mismatch.items(), key=lambda x: -len(x[1]))
    for fn, rows in ranked:
        hard = sum(1 for r in rows if r[4] == "MISMATCH")
        print(f"  {len(rows):>2} ({hard} hard)  {fn}")

    if LIST_MM:
        print("\n# MISMATCH/WEAK detail")
        for fn, rows in ranked:
            for path, ref, cov, snip, kind in rows:
                print(f"  [{kind} cov={cov}] {fn} {ref}\n      {snip}...")

    if LIST_RD:
        print("\n# Files by RENDERING (faithful quote; differs from cache only by")
        print("# punctuation/whitespace/Greek — this is what validate-references flags)")
        for fn, n in sorted(file_rendering.items(), key=lambda x: -x[1])[:30]:
            print(f"  {n:>2}  {fn}")

    if LIST_NC:
        print("\n# Top files by NOCONTENT (unverifiable; cache stub/missing)")
        for fn, n in sorted(file_nocontent.items(), key=lambda x: -x[1])[:30]:
            print(f"  {n:>2}  {fn}")

    if LIST_AS:
        print("\n# ASSEMBLED (every part is in the source; the join is not —")
        print("# a table flattened into prose, or a quote welded from two places)")
        for fn, rows in sorted(file_assembled.items(), key=lambda x: -len(x[1])):
            for _path, ref, snip in rows:
                print(f"  {fn} {ref}\n      {snip}...")


if __name__ == "__main__":
    main()
