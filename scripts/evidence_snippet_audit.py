#!/usr/bin/env python3
"""Audit evidence snippets against their cited reference's cached abstract.

For every EvidenceItem (any dict with both `reference` and `snippet`) in
kb/communities/*.yaml, locate the reference's cache file, strip the circular
"Quoted snippets used in curated records" list (so we match only against real
abstract text), normalize whitespace, and classify:

  MATCH      - snippet is a (near-)substring of the real cached text
  MISMATCH   - real abstract content exists but the snippet is absent (suspect)
  NOCONTENT  - cache missing or stub-only (no abstract body to verify against)

Usage: uv run python scripts/evidence_snippet_audit.py [--list-mismatch] [--list-nocontent]
"""
import re
import sys
import difflib
from pathlib import Path
from collections import defaultdict

import yaml

COMM = Path("kb/communities")
CACHE = Path("references_cache")
LIST_MM = "--list-mismatch" in sys.argv
LIST_NC = "--list-nocontent" in sys.argv

# Sections that contain curated/paraphrased snippets, not the real abstract.
# Stripping them prevents circular self-matching.
SNIPPET_SECTION = re.compile(
    r"(Quoted snippets used in curated records:|Key evidence used:|"
    r"Key snippets used in curated records:|Cached source notes:|"
    r"Snippets used in curated records:).*?(?=\nURL:|\nDOI:|\n## |\Z)",
    re.DOTALL | re.IGNORECASE,
)
FRONTMATTER = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)
HEADER_LINES = re.compile(r"^(#+\s|Title:|Source:|URL:|DOI:|\*\*|reference_id:).*$",
                          re.MULTILINE)
UNAVAILABLE = re.compile(r"content_type:\s*unavailable", re.IGNORECASE)
# A .md cache is treated as a REAL abstract only with an explicit signal:
REAL_CT = re.compile(r"content_type:\s*(abstract_only|abstract|full|fulltext)", re.IGNORECASE)
CONTENT_HEADING = re.compile(r"^##\s+(Content|Abstract)\b", re.MULTILINE | re.IGNORECASE)


def norm(s: str) -> str:
    return " ".join(s.split()).lower()


GREEK = {
    "α": "alpha", "β": "beta", "γ": "gamma", "δ": "delta", "ε": "epsilon",
    "ζ": "zeta", "η": "eta", "θ": "theta", "ι": "iota", "κ": "kappa",
    "λ": "lambda", "μ": "mu", "ν": "nu", "ξ": "xi", "ο": "omicron",
    "π": "pi", "ρ": "rho", "σ": "sigma", "ς": "sigma", "τ": "tau",
    "υ": "upsilon", "φ": "phi", "χ": "chi", "ψ": "psi", "ω": "omega",
}


def alnum(s: str) -> str:
    """Lowercase, transliterate Greek, keep only [a-z0-9].

    Robust to punctuation/whitespace spacing and Greek-letter vs spelled-out
    differences (e.g. abstract "β-5" vs snippet "beta-5")."""
    s = s.lower()
    for g, name in GREEK.items():
        s = s.replace(g, name)
    return re.sub(r"[^a-z0-9]", "", s)


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
    # prefer full-text .txt, then .md, then .json
    hits.sort(key=lambda p: {".txt": 0, ".md": 1, ".json": 2}.get(p.suffix, 3))
    real_bodies = []
    for p in hits:
        try:
            t = p.read_text(errors="ignore")
        except Exception:
            continue
        if p.suffix == ".txt":
            # PubMed full dump — always real content
            real_bodies.append(t)
            continue
        if UNAVAILABLE.search(t):
            continue                          # explicitly no abstract body
        # Only trust a .md as a real abstract with an explicit signal
        if not (REAL_CT.search(t) or CONTENT_HEADING.search(t)):
            continue                          # stub (notes + curated snippets only)
        fm = FRONTMATTER.sub("", t)           # drop YAML frontmatter
        stripped = SNIPPET_SECTION.sub("", fm)  # drop curated-snippet sections
        body = HEADER_LINES.sub("", stripped) # drop title/source/url headers
        if len(norm(body)) >= 200:            # substantial prose remains => real abstract
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


stats = defaultdict(int)
file_mismatch = defaultdict(list)
file_nocontent = defaultdict(int)
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
            stats["MATCH"] += 1
        elif cov >= 0.6:
            stats["WEAK"] += 1
            file_mismatch[f.name].append((path, ref, round(cov, 2), snip[:70], "WEAK"))
        else:
            stats["MISMATCH"] += 1
            file_mismatch[f.name].append((path, ref, round(cov, 2), snip[:70], "MISMATCH"))

total = sum(stats.values())
print(f"# {total} evidence snippets scanned across {len(list(COMM.glob('*.yaml')))} files")
for k in ("MATCH", "WEAK", "MISMATCH", "NOCONTENT"):
    print(f"  {k:<10} {stats[k]}")

print(f"\n# Files with MISMATCH/WEAK (content present but snippet absent) — fabrication suspects")
ranked = sorted(file_mismatch.items(), key=lambda x: -len(x[1]))
for fn, rows in ranked:
    hard = sum(1 for r in rows if r[4] == "MISMATCH")
    print(f"  {len(rows):>2} ({hard} hard)  {fn}")

if LIST_MM:
    print("\n# MISMATCH/WEAK detail")
    for fn, rows in ranked:
        for path, ref, cov, snip, kind in rows:
            print(f"  [{kind} cov={cov}] {fn} {ref}\n      {snip}...")

if LIST_NC:
    print(f"\n# Top files by NOCONTENT (unverifiable; cache stub/missing)")
    for fn, n in sorted(file_nocontent.items(), key=lambda x: -x[1])[:30]:
        print(f"  {n:>2}  {fn}")
