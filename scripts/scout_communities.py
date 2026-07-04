#!/usr/bin/env python3
"""Scout recent literature for newly published microbial communities.

Discovery counterpart to ``deep-research-community``: instead of enriching a
community you already curate, this queries Europe PMC for recently published
papers describing defined/structured microbial communities, dedups the hits
against the records already in ``kb/communities/`` (both by cited PMID/DOI and
by community-name token overlap), scores each hit by how strongly it reads as a
*community* paper, and writes a curator-facing report plus a machine-readable
queue.

It does NOT mutate ``kb/communities/`` — minting IDs and writing records stays
a human decision (hand promising hits to ``manage-identifiers`` +
``deep-research-community``). With ``--emit-stubs`` it writes minimal draft
records under the scouting output dir for review only.

Free + reproducible: Europe PMC REST search needs no API key. Re-running the
same query on the same day is deterministic apart from newly indexed papers.

Usage:
    uv run python scripts/scout_communities.py \
        --query "microbial consortium cross-feeding" --since 2024 --limit 40
    uv run python scripts/scout_communities.py --preset syntrophy --emit-stubs
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path

import requests
import yaml

EPMC_SEARCH = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"

REPO_ROOT = Path(__file__).resolve().parent.parent
COMMUNITIES_DIR = REPO_ROOT / "kb" / "communities"
DEFAULT_OUT_DIR = REPO_ROOT / "research" / "scouting"

# Words that signal a paper is about a *defined/structured community*, not a
# single-organism study. Presence in title/abstract raises the score.
COMMUNITY_SIGNALS = [
    "consortium",
    "consortia",
    "co-culture",
    "coculture",
    "co-cultivation",
    "syncom",
    "synthetic community",
    "synthetic microbial community",
    "defined community",
    "microbial community",
    "cross-feed",
    "cross feeding",
    "crossfeeding",
    "syntrophy",
    "syntrophic",
    "mutualis",
    "metabolic exchange",
    "metabolic handoff",
    "interspecies",
    "enrichment culture",
    "tri-culture",
    "two-species",
    "three-species",
    "multispecies",
    "multi-species",
    "member community",
    "minimal microbiome",
]

# Presets: ready-made Europe PMC query fragments for common scouting angles.
PRESETS = {
    "general": "microbial community OR microbial consortium OR synthetic community",
    "syntrophy": "syntrophic OR syntrophy OR interspecies electron transfer OR cross-feeding",
    "syncom": '"synthetic community" OR SynCom OR "defined community" OR "synthetic microbial community"',
    "coculture": '"co-culture" OR coculture OR "two-species" OR "tri-culture"',
    "engineered": '"engineered consortium" OR "designed microbial community" OR "division of labor"',
}

STOPWORDS = {
    "the",
    "a",
    "an",
    "of",
    "and",
    "in",
    "on",
    "for",
    "with",
    "to",
    "from",
    "community",
    "communities",
    "consortium",
    "consortia",
    "coculture",
    "co",
    "culture",
    "microbial",
    "synthetic",
    "syncom",
    "defined",
    "system",
    "model",
    "based",
    "using",
    "study",
    "novel",
    "new",
}


def _tokens(text: str) -> set[str]:
    """Lowercase alphanumeric tokens minus stopwords, length >= 4."""
    return {t for t in re.findall(r"[a-z0-9]+", text.lower()) if len(t) >= 4 and t not in STOPWORDS}


def build_dedup_index(communities_dir: Path) -> dict:
    """Index existing records: cited PMIDs/DOIs and per-record name token sets."""
    cited_pmids: set[str] = set()
    cited_dois: set[str] = set()
    name_token_sets: list[tuple[str, set[str]]] = []

    pmid_re = re.compile(r"reference:\s*PMID:(\d+)", re.IGNORECASE)
    doi_re = re.compile(r"reference:\s*doi:(\S+)", re.IGNORECASE)
    name_re = re.compile(r"^name:\s*(.+)$", re.MULTILINE)

    for path in sorted(communities_dir.glob("*.yaml")):
        text = path.read_text(errors="replace")
        cited_pmids.update(pmid_re.findall(text))
        cited_dois.update(d.lower().rstrip(".,;") for d in doi_re.findall(text))
        m = name_re.search(text)
        name = m.group(1).strip() if m else path.stem.replace("_", " ")
        name_token_sets.append((name, _tokens(name)))

    return {
        "cited_pmids": cited_pmids,
        "cited_dois": cited_dois,
        "name_token_sets": name_token_sets,
    }


def dedup_status(hit: dict, index: dict) -> tuple[str, str]:
    """Classify a hit vs. existing records: (status, detail)."""
    pmid = (hit.get("pmid") or "").strip()
    doi = (hit.get("doi") or "").strip().lower().rstrip(".,;")

    if pmid and pmid in index["cited_pmids"]:
        return "ALREADY_CITED", f"PMID:{pmid} already cited"
    if doi and doi in index["cited_dois"]:
        return "ALREADY_CITED", f"doi:{doi} already cited"

    title_tokens = _tokens(hit.get("title", ""))
    best_name, best_overlap = "", 0.0
    for name, name_tokens in index["name_token_sets"]:
        if not name_tokens:
            continue
        shared = title_tokens & name_tokens
        # Jaccard against the (smaller) record-name token set is more sensitive
        # to short community names than full-title Jaccard.
        overlap = len(shared) / max(1, len(name_tokens))
        if overlap > best_overlap:
            best_name, best_overlap = name, overlap
    if best_overlap >= 0.5:
        return "TITLE_OVERLAP", f"~{best_overlap:.0%} name overlap with '{best_name}'"
    return "NEW", ""


def score_hit(hit: dict) -> tuple[int, list[str]]:
    """Community-signal score: count distinct signal phrases in title+abstract."""
    blob = f"{hit.get('title', '')} {hit.get('abstract', '')}".lower()
    matched = [s for s in COMMUNITY_SIGNALS if s in blob]
    # Title matches weigh double.
    title = hit.get("title", "").lower()
    title_bonus = sum(1 for s in COMMUNITY_SIGNALS if s in title)
    return len(matched) + title_bonus, matched


def query_epmc(query: str, since: int, limit: int) -> list[dict]:
    """Query Europe PMC, return normalized hit dicts (title/abstract/pmid/doi/...)."""
    full_query = f"({query}) AND (FIRST_PDATE:[{since}-01-01 TO 3000-12-31]) AND HAS_ABSTRACT:Y"
    hits: list[dict] = []
    cursor = "*"
    session = requests.Session()
    session.headers.update({"User-Agent": "CommunityMech-scout/1.0"})
    while len(hits) < limit:
        page_size = min(100, limit - len(hits))
        # NB: no `sort` param — Europe PMC's relevance default keeps results
        # on-topic; passing `sort=P_PDATE_D desc` silently broadens the query
        # to thousands of off-topic hits. We re-rank by score+year in Python.
        params = {
            "query": full_query,
            "format": "json",
            "resultType": "core",
            "pageSize": str(page_size),
            "cursorMark": cursor,
        }
        resp = session.get(EPMC_SEARCH, params=params, timeout=60)
        resp.raise_for_status()
        data = resp.json()
        results = data.get("resultList", {}).get("result", [])
        if not results:
            break
        for r in results:
            hits.append(
                {
                    "pmid": r.get("pmid", ""),
                    "doi": r.get("doi", ""),
                    "title": re.sub(r"<[^>]+>", "", html.unescape(r.get("title") or "")).rstrip(
                        "."
                    ),
                    "abstract": re.sub(r"<[^>]+>", "", html.unescape(r.get("abstractText") or "")),
                    "year": r.get("pubYear", ""),
                    "journal": (r.get("journalInfo", {}) or {}).get("journal", {}).get("title", ""),
                    "authors": r.get("authorString", ""),
                    "is_open": r.get("isOpenAccess", "N") == "Y",
                }
            )
        next_cursor = data.get("nextCursorMark")
        if not next_cursor or next_cursor == cursor:
            break
        cursor = next_cursor
    return hits[:limit]


def crossref_doi_for_title(title: str, session: requests.Session) -> str:
    """Best-effort DOI for a title via CrossRef, so ref-less hits can dedup by DOI.

    Europe PMC AGR-source records often carry no PMID/DOI; without one a hit for an
    already-curated paper re-surfaces as NEW. Resolving the DOI lets dedup_status
    catch it against cited_dois. Requires a high title-token overlap to avoid
    grabbing an unrelated DOI.
    """
    if not title:
        return ""
    try:
        resp = session.get(
            "https://api.crossref.org/works",
            params={"query.bibliographic": title, "rows": "1"},
            timeout=30,
        )
        resp.raise_for_status()
        items = resp.json().get("message", {}).get("items", [])
    except (requests.exceptions.RequestException, ValueError):
        return ""
    if not items:
        return ""
    it = items[0]
    cand_title = (it.get("title") or [""])[0]
    # Require the CrossRef hit's title to substantially match the query title.
    q, c = _tokens(title), _tokens(cand_title)
    if q and len(q & c) / len(q) >= 0.7:
        return (it.get("DOI") or "").strip()
    return ""


def backfill_missing_dois(hits: list[dict], session: requests.Session) -> int:
    """Fill hit['doi'] from CrossRef for hits lacking both PMID and DOI. Returns count filled."""
    filled = 0
    for h in hits:
        if not (h.get("pmid") or "").strip() and not (h.get("doi") or "").strip():
            doi = crossref_doi_for_title(h.get("title", ""), session)
            if doi:
                h["doi"] = doi
                filled += 1
    return filled


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:40] or "scout"


def emit_stub(hit: dict, out_dir: Path) -> Path:
    """Write a minimal review-only draft record (placeholder id, NOT minted)."""
    stub_dir = out_dir / "stubs"
    stub_dir.mkdir(parents=True, exist_ok=True)
    ref = (
        f"PMID:{hit['pmid']}"
        if hit.get("pmid")
        else (f"doi:{hit['doi']}" if hit.get("doi") else "")
    )
    name = hit["title"][:120]
    stub = {
        "id": "CommunityMech:XXXXXX",  # placeholder — mint via manage-identifiers
        "name": name,
        "description": (hit.get("abstract", "")[:500] or "TODO: summarize from source"),
        "_scout": {
            "source_reference": ref,
            "year": hit.get("year", ""),
            "journal": hit.get("journal", ""),
            "status": "candidate — review, mint id, then deep-research-community",
        },
    }
    fname = f"{slugify(name)}.stub.yaml"
    path = stub_dir / fname
    path.write_text(
        yaml.dump(stub, default_flow_style=False, sort_keys=False, allow_unicode=True, width=100)
    )
    return path


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    grp = p.add_mutually_exclusive_group(required=True)
    grp.add_argument("--query", help="Free-text Europe PMC query.")
    grp.add_argument("--preset", choices=sorted(PRESETS), help="Ready-made query angle.")
    p.add_argument(
        "--since", type=int, default=2024, help="Earliest first-publication year (default 2024)."
    )
    p.add_argument(
        "--limit", type=int, default=40, help="Max Europe PMC hits to fetch (default 40)."
    )
    p.add_argument(
        "--min-score", type=int, default=1, help="Drop hits below this community-signal score."
    )
    p.add_argument(
        "--include-cited", action="store_true", help="Keep hits already cited by a record."
    )
    p.add_argument("--emit-stubs", action="store_true", help="Write review-only draft stub YAMLs.")
    p.add_argument("--out-dir", type=Path, default=DEFAULT_OUT_DIR)
    args = p.parse_args(argv)

    query = args.query or PRESETS[args.preset]
    label = args.query or f"preset:{args.preset}"

    print(f"[scout] query: {query}", file=sys.stderr)
    print(f"[scout] since {args.since}, limit {args.limit}", file=sys.stderr)

    try:
        hits = query_epmc(query, args.since, args.limit)
    except requests.exceptions.RequestException as e:
        print(f"[scout] Europe PMC request failed: {e}", file=sys.stderr)
        return 1
    print(f"[scout] fetched {len(hits)} hits", file=sys.stderr)

    # Ref-less hits (e.g. Europe PMC AGR source) can't dedup by PMID/DOI; try to
    # resolve a DOI via CrossRef so already-curated papers don't re-surface as NEW.
    n_filled = backfill_missing_dois(hits, requests.Session())
    if n_filled:
        print(f"[scout] backfilled DOIs for {n_filled} ref-less hits (CrossRef)", file=sys.stderr)

    index = build_dedup_index(COMMUNITIES_DIR)
    print(
        f"[scout] dedup index: {len(index['cited_pmids'])} PMIDs, "
        f"{len(index['cited_dois'])} DOIs, {len(index['name_token_sets'])} records",
        file=sys.stderr,
    )

    candidates = []
    for hit in hits:
        score, matched = score_hit(hit)
        status, detail = dedup_status(hit, index)
        hit.update({"score": score, "signals": matched, "dedup": status, "dedup_detail": detail})
        if score < args.min_score:
            continue
        if status == "ALREADY_CITED" and not args.include_cited:
            continue
        candidates.append(hit)

    candidates.sort(key=lambda h: (h["dedup"] != "NEW", -h["score"], -int(h.get("year") or 0)))

    args.out_dir.mkdir(parents=True, exist_ok=True)
    slug = slugify(label)
    report_path = args.out_dir / f"scout-{slug}.md"
    queue_path = args.out_dir / f"scout-{slug}-queue.json"

    lines = [
        f"# Community scouting: {label}",
        "",
        f"- Europe PMC query: `{query}`",
        f"- Since: {args.since} · fetched {len(hits)} · candidates after filter: {len(candidates)}",
        f"- Dedup index: {len(index['cited_pmids'])} cited PMIDs, {len(index['cited_dois'])} DOIs, "
        f"{len(index['name_token_sets'])} existing records",
        "",
        "Status legend: **NEW** = not cited & low name overlap · **TITLE_OVERLAP** = "
        "possible existing record · **ALREADY_CITED** = reference already in a record.",
        "",
    ]
    for i, h in enumerate(candidates, 1):
        ref = f"PMID:{h['pmid']}" if h["pmid"] else (f"doi:{h['doi']}" if h["doi"] else "no-id")
        oa = " · OA" if h["is_open"] else ""
        lines += [
            f"## {i}. {h['title']}  ",
            f"**{h['dedup']}** (score {h['score']}) · {h['year']} · {h['journal']}{oa} · `{ref}`  ",
            (f"_{h['dedup_detail']}_  " if h["dedup_detail"] else ""),
            f"Signals: {', '.join(h['signals']) or '—'}  ",
            "",
            (
                (h["abstract"][:600] + ("…" if len(h["abstract"]) > 600 else ""))
                if h["abstract"]
                else "_(no abstract)_"
            ),
            "",
        ]
    report_path.write_text("\n".join(lines))

    queue = [
        {
            "reference": (
                f"PMID:{h['pmid']}" if h["pmid"] else (f"doi:{h['doi']}" if h["doi"] else "")
            ),
            "title": h["title"],
            "year": h["year"],
            "journal": h["journal"],
            "score": h["score"],
            "dedup": h["dedup"],
            "dedup_detail": h["dedup_detail"],
        }
        for h in candidates
    ]
    queue_path.write_text(json.dumps(queue, indent=2, ensure_ascii=False))

    stub_note = ""
    if args.emit_stubs:
        new_hits = [h for h in candidates if h["dedup"] == "NEW"]
        for h in new_hits:
            emit_stub(h, args.out_dir)
        stub_note = f" · {len(new_hits)} stubs -> {args.out_dir / 'stubs'}"

    n_new = sum(1 for h in candidates if h["dedup"] == "NEW")
    print(
        f"[scout] {len(candidates)} candidates ({n_new} NEW). " f"Report: {report_path}{stub_note}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
