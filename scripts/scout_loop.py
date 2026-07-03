#!/usr/bin/env python3
"""Loop the community scout across many query angles until it stops finding new communities.

Runs ``scout_communities`` repeatedly over a battery of query angles, keeping a
global seen-set (seeded from every PMID/DOI already cited in ``kb/communities/``
and grown with each candidate surfaced this run) so the same community never
counts twice across angles. Loop-until-dry: stops once ``--dry-streak``
consecutive angles yield zero new communities (or the battery is exhausted).

Writes one consolidated report + queue of the de-duplicated NEW candidates.

Usage:
    uv run python scripts/scout_loop.py --since 2023 --limit 50
    uv run python scripts/scout_loop.py --since 2024 --dry-streak 4 --emit-stubs
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import scout_communities as sc

# Query battery: presets first, then niche angles spanning the community space.
# Order matters only for the dry-streak early stop; every angle is deduped
# globally so overlap between angles is harmless.
ANGLES: list[tuple[str, str]] = [
    ("preset:general", sc.PRESETS["general"]),
    ("preset:syntrophy", sc.PRESETS["syntrophy"]),
    ("preset:syncom", sc.PRESETS["syncom"]),
    ("preset:coculture", sc.PRESETS["coculture"]),
    ("preset:engineered", sc.PRESETS["engineered"]),
    ("gut", '(gut OR intestinal) AND (consortium OR "defined community" OR "cross-feeding")'),
    ("rhizosphere", '(rhizosphere OR root OR phyllosphere) AND (SynCom OR "synthetic community")'),
    ("marine", '(marine OR ocean OR seep OR sediment) AND (consortium OR syntrophic OR co-culture)'),
    ("methane", '(methanogen OR methanotroph OR "anaerobic oxidation of methane") AND (consortium OR syntrophic)'),
    ("anaerobic_digestion", '"anaerobic digestion" AND (syntrophic OR "interspecies electron transfer" OR consortium)'),
    ("wastewater", '(wastewater OR "activated sludge" OR EBPR OR anammox) AND (community OR consortium)'),
    ("nitrogen", '(nitrification OR denitrification OR "nitrogen fixation" OR anammox) AND (consortium OR co-culture)'),
    ("photosynthetic", '(cyanobacteria OR microalgae OR phototroph) AND (consortium OR co-culture OR "synthetic community")'),
    ("bioelectrochemical", '(electroactive OR "microbial fuel cell" OR electrofermentation) AND (consortium OR co-culture)'),
    ("acid_mine", '("acid mine drainage" OR acidophile OR bioleaching) AND (community OR consortium)'),
    ("fermented_food", '(kefir OR kombucha OR cheese OR sourdough OR fermented) AND (community OR consortium OR co-culture)'),
    ("degradation", '(degradation OR dechlorination OR bioremediation OR "plastic") AND (consortium OR "defined community")'),
    ("division_of_labor", '"division of labor" AND (microbial OR consortium OR "synthetic community")'),
]


def norm_title(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", title.lower()).strip()


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--since", type=int, default=2023, help="Earliest first-publication year (default 2023).")
    p.add_argument("--limit", type=int, default=50, help="Max hits fetched per angle (default 50).")
    p.add_argument("--min-score", type=int, default=1, help="Drop hits below this community-signal score.")
    p.add_argument("--dry-streak", type=int, default=3,
                   help="Stop after this many consecutive angles with zero new communities (default 3).")
    p.add_argument("--emit-stubs", action="store_true", help="Write review-only draft stub YAMLs for NEW hits.")
    p.add_argument("--out-dir", type=Path, default=sc.DEFAULT_OUT_DIR)
    args = p.parse_args(argv)

    index = sc.build_dedup_index(sc.COMMUNITIES_DIR)
    seen_refs: set[str] = set()
    seen_titles: set[str] = set()
    for pmid in index["cited_pmids"]:
        seen_refs.add(f"PMID:{pmid}")
    for doi in index["cited_dois"]:
        seen_refs.add(f"doi:{doi}")
    print(
        f"[loop] seeded seen-set: {len(seen_refs)} refs from "
        f"{len(index['name_token_sets'])} existing records",
        file=sys.stderr,
    )

    new_candidates: list[dict] = []
    per_angle: list[tuple[str, int]] = []
    dry_streak = 0

    for label, query in ANGLES:
        try:
            hits = sc.query_epmc(query, args.since, args.limit)
        except Exception as e:  # network / API — log and treat angle as empty
            print(f"[loop] {label}: query failed ({e})", file=sys.stderr)
            hits = []

        round_new = 0
        for hit in hits:
            score, signals = sc.score_hit(hit)
            if score < args.min_score:
                continue
            status, detail = sc.dedup_status(hit, index)
            if status == "ALREADY_CITED":
                continue
            ref = f"PMID:{hit['pmid']}" if hit["pmid"] else (f"doi:{hit['doi']}" if hit["doi"] else "")
            nt = norm_title(hit["title"])
            if (ref and ref in seen_refs) or (nt and nt in seen_titles):
                continue  # cross-angle / preprint-vs-published dedup
            if ref:
                seen_refs.add(ref)
            if nt:
                seen_titles.add(nt)
            hit.update({
                "score": score, "signals": signals,
                "dedup": status, "dedup_detail": detail,
                "angle": label,
            })
            new_candidates.append(hit)
            round_new += 1

        per_angle.append((label, round_new))
        total = len(new_candidates)
        print(f"[loop] {label}: +{round_new} new (total {total})", file=sys.stderr)

        dry_streak = dry_streak + 1 if round_new == 0 else 0
        if dry_streak >= args.dry_streak:
            print(
                f"[loop] {dry_streak} consecutive dry angles — stopping "
                f"(loop-until-dry).",
                file=sys.stderr,
            )
            break

    # Rank: NEW before TITLE_OVERLAP, then score, then recency.
    new_candidates.sort(key=lambda h: (h["dedup"] != "NEW", -h["score"], -int(h.get("year") or 0)))

    args.out_dir.mkdir(parents=True, exist_ok=True)
    report_path = args.out_dir / "scout-loop.md"
    queue_path = args.out_dir / "scout-loop-queue.json"

    n_new = sum(1 for h in new_candidates if h["dedup"] == "NEW")
    n_overlap = sum(1 for h in new_candidates if h["dedup"] == "TITLE_OVERLAP")
    angles_run = len(per_angle)

    lines = [
        "# Community scouting — loop-until-dry sweep",
        "",
        f"- Angles run: {angles_run}/{len(ANGLES)} · since {args.since} · {args.limit}/angle",
        f"- Stopped after {args.dry_streak} consecutive dry angles"
        if dry_streak >= args.dry_streak else "- Battery exhausted (no early stop)",
        f"- Distinct candidates: **{len(new_candidates)}** "
        f"({n_new} NEW, {n_overlap} possible-existing) after dedup vs "
        f"{len(index['name_token_sets'])} records + cross-angle",
        "",
        "Per-angle new counts: " + ", ".join(f"{lbl} {n}" for lbl, n in per_angle),
        "",
        "Status: **NEW** = not cited & low name overlap · **TITLE_OVERLAP** = "
        "may match an existing record (verify before adding).",
        "",
    ]
    for i, h in enumerate(new_candidates, 1):
        ref = f"PMID:{h['pmid']}" if h["pmid"] else (f"doi:{h['doi']}" if h["doi"] else "no-id")
        oa = " · OA" if h["is_open"] else ""
        lines += [
            f"## {i}. {h['title']}  ",
            f"**{h['dedup']}** (score {h['score']}, via {h['angle']}) · {h['year']} · "
            f"{h['journal']}{oa} · `{ref}`  ",
            (f"_{h['dedup_detail']}_  " if h["dedup_detail"] else ""),
            f"Signals: {', '.join(h['signals']) or '—'}  ",
            "",
            (h["abstract"][:500] + ("…" if len(h["abstract"]) > 500 else "")) if h["abstract"] else "_(no abstract)_",
            "",
        ]
    report_path.write_text("\n".join(lines))

    queue = [
        {
            "reference": f"PMID:{h['pmid']}" if h["pmid"] else (f"doi:{h['doi']}" if h["doi"] else ""),
            "title": h["title"], "year": h["year"], "journal": h["journal"],
            "score": h["score"], "dedup": h["dedup"], "angle": h["angle"],
        }
        for h in new_candidates
    ]
    queue_path.write_text(json.dumps(queue, indent=2, ensure_ascii=False))

    if args.emit_stubs:
        for h in (c for c in new_candidates if c["dedup"] == "NEW"):
            sc.emit_stub(h, args.out_dir)

    print(
        f"[loop] done: {len(new_candidates)} candidates ({n_new} NEW) across "
        f"{angles_run} angles. Report: {report_path}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
