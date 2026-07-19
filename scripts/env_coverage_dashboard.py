#!/usr/bin/env python3
"""Environmental coverage dashboard across CommunityMech + CultureMech + MIM (issue #30).

For every ENVO environment term used by a CommunityMech community, report how many
communities, CultureMech media (``source_environment``), and MediaIngredientMech
ingredients (``environmental_context``) share it — surfacing where a community's
environment has good media/ingredient support and where it is a gap.

Sibling repos are read from local paths (no network), configured via the
``COMMUNITYMECH_SIBLING_REPOS`` env var (``Name=path,Name=path``) or the
``--culturemech`` / ``--mediaingredientmech`` flags. Point them at each sibling
repo root (or any subtree holding its records).

Usage:
    PYTHONPATH=src uv run python scripts/env_coverage_dashboard.py
    COMMUNITYMECH_SIBLING_REPOS="CultureMech=../CultureMech,MediaIngredientMech=../MediaIngredientMech" \\
        PYTHONPATH=src uv run python scripts/env_coverage_dashboard.py --tsv reports/env_coverage.tsv
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from communitymech.cross_repo_environment import build_coverage, sibling_repos_from_env

REPO_ROOT = Path(__file__).parent.parent
COMMUNITY_DIR = REPO_ROOT / "kb" / "communities"


def _rows(coverage):
    """Sorted rows: (envo_id, label, n_comm, n_media, n_ingred), community terms only."""
    rows = []
    for envo_id in sorted(coverage.community_records):
        rows.append(
            (
                envo_id,
                coverage.label(envo_id),
                len(coverage.community_records[envo_id]),
                len(coverage.media_records.get(envo_id, [])),
                len(coverage.ingredient_records.get(envo_id, [])),
            )
        )
    # Gaps first: least sibling support, then most communities affected.
    rows.sort(key=lambda r: (r[3] + r[4], -r[2]))
    return rows


def _print_table(rows, have_siblings) -> None:
    print(f"\nEnvironmental coverage — {len(rows)} community ENVO terms\n")
    header = f"{'ENVO term':16} {'label':28} {'comm':>5} {'media':>6} {'ingred':>7}  status"
    print(header)
    print("-" * len(header))
    for envo_id, label, n_comm, n_media, n_ingred in rows:
        if not have_siblings:
            status = "siblings not configured"
        elif n_media == 0 and n_ingred == 0:
            status = "GAP: no media or ingredients"
        elif n_media == 0:
            status = "gap: no media"
        elif n_ingred == 0:
            status = "gap: no ingredients"
        else:
            status = "covered"
        print(f"{envo_id:16} {label[:28]:28} {n_comm:5} {n_media:6} {n_ingred:7}  {status}")


def _summary(rows, have_siblings) -> None:
    total = len(rows)
    if not have_siblings:
        print(f"\n{total} community ENVO terms. Configure sibling repos for coverage.\n")
        return
    both = sum(1 for r in rows if r[3] and r[4])
    no_media = sum(1 for r in rows if r[3] == 0)
    no_ingred = sum(1 for r in rows if r[4] == 0)
    full_gap = sum(1 for r in rows if r[3] == 0 and r[4] == 0)
    print(
        f"\nSummary: {total} community ENVO terms | "
        f"{both} with both media+ingredients | {no_media} lack media | "
        f"{no_ingred} lack ingredients | {full_gap} have neither\n"
    )


def _write_tsv(path: Path, rows) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["envo_id\tlabel\tcommunities\tmedia\tingredients"]
    lines += ["\t".join(map(str, r)) for r in rows]
    path.write_text("\n".join(lines) + "\n")
    print(f"Wrote {path} ({len(rows)} rows)")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--culturemech", type=Path, help="Path to CultureMech repo/records")
    parser.add_argument("--mediaingredientmech", type=Path, help="Path to MIM repo/records")
    parser.add_argument("--tsv", type=Path, help="Also write the table to this TSV path")
    args = parser.parse_args()

    sibling_repos = sibling_repos_from_env()
    if args.culturemech is not None:
        sibling_repos["CultureMech"] = args.culturemech
    if args.mediaingredientmech is not None:
        sibling_repos["MediaIngredientMech"] = args.mediaingredientmech

    coverage = build_coverage(COMMUNITY_DIR, sibling_repos=sibling_repos)
    rows = _rows(coverage)
    have_siblings = bool(sibling_repos)

    _print_table(rows, have_siblings)
    _summary(rows, have_siblings)
    if args.tsv is not None:
        _write_tsv(args.tsv, rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
