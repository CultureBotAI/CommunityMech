#!/usr/bin/env python3
"""Environment-grounding quality report for CommunityMech communities (issue #30 follow-up).

Every community grounds a single `environment_term` (an ENVO CURIE). This report
ranks those terms by how many communities share each, and flags two grounding
smells for curator review — it never edits records:

* **generic** — the term is a study/lab setting (`GENERIC_ENVIRONMENT_TERMS`, e.g.
  ENVO:01001405 "laboratory environment") rather than a natural/source habitat. As
  a *primary* environment it carries little signal; where the community models a
  knowable habitat (rumen, gut, groundwater, …) it should be re-grounded.
* **over-applied** — the term grounds an outsized share of communities
  (>= `--threshold`, default 15), which usually means a catch-all is standing in
  for more specific habitats.

(ENVO `is_a` depth was evaluated as a genericness signal and rejected: "laboratory
environment" is *deeper* than "soil", so depth doesn't separate the two. Hence the
curated set + count heuristic.)

Usage:
    PYTHONPATH=src uv run python scripts/env_grounding_quality.py
    PYTHONPATH=src uv run python scripts/env_grounding_quality.py --list --threshold 20
    PYTHONPATH=src uv run python scripts/env_grounding_quality.py --strict   # exit 1 if any generic groundings
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from communitymech.cross_repo_environment import (  # noqa: E402
    GENERIC_ENVIRONMENT_TERMS,
    build_coverage,
)

REPO_ROOT = Path(__file__).parent.parent
COMMUNITY_DIR = REPO_ROOT / "kb" / "communities"


def flags_for(envo_id: str, count: int, threshold: int) -> list[str]:
    """Grounding-quality flags for one term: 'GENERIC' and/or 'over-applied'."""
    flags = []
    if envo_id in GENERIC_ENVIRONMENT_TERMS:
        flags.append("GENERIC")
    if count >= threshold:
        flags.append("over-applied")
    return flags


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--threshold",
        type=int,
        default=15,
        help="Flag a term as over-applied at or above this many communities (default 15)",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List the community records grounded to each flagged term",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit 1 if any community is grounded to a generic environment term",
    )
    args = parser.parse_args()

    coverage = build_coverage(COMMUNITY_DIR, sibling_repos={})
    community_records = coverage.community_records

    rows = sorted(
        ((envo, coverage.label(envo), len(names)) for envo, names in community_records.items()),
        key=lambda r: -r[2],
    )
    total = sum(r[2] for r in rows)

    print(f"\nEnvironment-grounding quality — {len(rows)} distinct ENVO terms over {total} communities\n")
    header = f"{'ENVO term':16} {'label':30} {'count':>5}  flags"
    print(header)
    print("-" * len(header))
    generic_hits = 0
    flagged = []
    for envo_id, label, count in rows:
        flags = flags_for(envo_id, count, args.threshold)
        if "GENERIC" in flags:
            generic_hits += count
        if flags:
            flagged.append((envo_id, label, count))
        print(f"{envo_id:16} {label[:30]:30} {count:5}  {', '.join(flags)}")

    print(
        f"\nSummary: {len(flagged)} flagged term(s); "
        f"{generic_hits} community(ies) grounded to a generic environment.\n"
    )

    if args.list and flagged:
        print("Flagged terms — affected community records:")
        for envo_id, label, _ in flagged:
            print(f"\n  {envo_id} ({label}):")
            for name in sorted(community_records[envo_id]):
                print(f"    - {name}")
        print()

    if args.strict and generic_hits:
        print(f"[strict] {generic_hits} community(ies) grounded to a generic environment.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
