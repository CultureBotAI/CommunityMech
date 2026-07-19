#!/usr/bin/env python3
"""Suggest environment-matched CultureMech media for CommunityMech communities (issue #30, Use Case 1).

For each community, match its ``environment_term`` ENVO id against CultureMech
media that declare the same ``source_environment`` term, and emit ready-to-review
``related_media`` YAML blocks (with ``shared_environment_term``) for a curator to
paste. Media already linked from the community (via ``related_media.culturemech_id``
or ``growth_media.culturemech_id``) are skipped, so re-runs only surface new
matches.

This is suggestion-only: it prints blocks for review and never edits records —
mirroring `scripts/suggest_missing_interactions.py`.

Scope: **media only.** Environment-based *ingredient* suggestion is not emitted
because (a) `RelatedIngredient` has no `shared_environment_term` slot to carry the
link, and (b) MIM ingredient records don't carry `MediaIngredientMech:NNNNNN` ids
(the schema pattern) — both tracked in NEXT_TASKS.md §2b.

Sibling repo path comes from ``COMMUNITYMECH_SIBLING_REPOS`` (``Name=path``) or
``--culturemech``; point it at the CultureMech repo root.

Matching is exact-ENVO by default. `--subsumption` also matches media whose
environment is an ENVO *subtype* of the community's (e.g. a "marine sediment"
medium for a "sediment" community), when the ENVO sqlite is cached locally.

Usage:
    COMMUNITYMECH_SIBLING_REPOS="CultureMech=../CultureMech" \\
        PYTHONPATH=src uv run python scripts/suggest_related_media.py
    PYTHONPATH=src uv run python scripts/suggest_related_media.py --subsumption \\
        --culturemech ../CultureMech kb/communities/SPRUCE_Peatland_Methane_Cycling_Community.yaml
"""

import argparse
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from communitymech.cross_repo_environment import (  # noqa: E402
    culturemech_media_by_environment,
    envo_subtypes,
    get_envo_adapter,
    sibling_repos_from_env,
)

REPO_ROOT = Path(__file__).parent.parent
COMMUNITY_DIR = REPO_ROOT / "kb" / "communities"

# Over-generic environments where a shared tag does not imply a meaningful
# environment analog (e.g. every lab-grown community shares "laboratory
# environment", so matching on it just yields noise). Skipped by default;
# override with --include-generic. See NEXT_TASKS.md §2b (grounding-quality note).
GENERIC_ENVIRONMENTS = {
    "ENVO:01001405",  # laboratory environment (applied to ~110 communities)
}


def _linked_culturemech_ids(data: dict) -> set[str]:
    """CultureMech ids already referenced by the community (related + growth media)."""
    linked: set[str] = set()
    for slot in ("related_media", "growth_media"):
        for entry in data.get(slot) or []:
            if isinstance(entry, dict) and entry.get("culturemech_id"):
                linked.add(entry["culturemech_id"])
    return linked


def _community_env(data: dict) -> tuple[str, str] | None:
    """(ENVO id, label) from environment_term, or None."""
    et = data.get("environment_term")
    term = (et or {}).get("term") if isinstance(et, dict) else None
    if not isinstance(term, dict):
        return None
    envo_id = term.get("id")
    if isinstance(envo_id, str) and envo_id.startswith("ENVO:"):
        return envo_id, term.get("label") or ""
    return None


def _suggestion_block(matches, envo_id, env_label):
    """Render related_media dicts for (MediaHit, relation) matches.

    ``relation`` is "exact" or "subtype" (the medium's environment is a subtype of
    the community's). For subtype matches the shared_environment_term is the
    community's own (broader) ENVO term — the valid join key — and the medium's
    more-specific environment is recorded in the notes.
    """
    blocks = []
    for hit, relation in sorted(matches, key=lambda m: m[0].culturemech_id):
        if relation == "exact":
            note = (
                f"Shares environment '{env_label or hit.env_label}' ({envo_id}) with this "
                "community; surfaced by env-based cross-repo match against CultureMech "
                "source_environment."
            )
        else:
            note = (
                f"CultureMech source_environment '{hit.env_label}' ({hit.env_id}) is a subtype "
                f"of this community's environment '{env_label}' ({envo_id}); surfaced by "
                "ENVO-subsumption cross-repo match."
            )
        blocks.append(
            {
                "preferred_term": hit.name,
                "culturemech_id": hit.culturemech_id,
                "relationship_type": "ENVIRONMENT_ANALOG",
                "shared_environment_term": {"id": envo_id, "label": env_label or hit.env_label},
                "relevance_notes": note,
            }
        )
    return blocks


def _matches_for(envo_id, media_by_env, envo_adapter, exclude_subtype_envs=frozenset()):
    """Return [(MediaHit, relation)] for a community ENVO term.

    Always includes exact matches; when ``envo_adapter`` is provided, also includes
    media whose environment is an ENVO subtype of ``envo_id`` — except subtypes in
    ``exclude_subtype_envs`` (e.g. the over-generic "laboratory environment", which
    subsumption would otherwise pull in as a media env). Each medium appears once,
    preferring an exact match over a subtype match.
    """
    seen: dict[str, tuple] = {}
    for hit in media_by_env.get(envo_id, []):
        seen[hit.culturemech_id] = (hit, "exact")
    if envo_adapter is not None:
        for sub in envo_subtypes(envo_id, envo_adapter):
            if sub in exclude_subtype_envs:
                continue
            for hit in media_by_env.get(sub, []):
                seen.setdefault(hit.culturemech_id, (hit, "subtype"))
    return list(seen.values())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "yaml_paths",
        nargs="*",
        type=Path,
        help="Community YAMLs to process (default: all in kb/communities/)",
    )
    parser.add_argument("--culturemech", type=Path, help="Path to CultureMech repo/records")
    parser.add_argument(
        "--include-generic",
        action="store_true",
        help="Also match over-generic environments like 'laboratory environment'",
    )
    parser.add_argument(
        "--subsumption",
        action="store_true",
        help="Also match media whose environment is an ENVO subtype of the community's "
        "(needs the ENVO sqlite cached locally)",
    )
    args = parser.parse_args()

    sibling_repos = sibling_repos_from_env()
    if args.culturemech is not None:
        sibling_repos["CultureMech"] = args.culturemech
    cm_path = sibling_repos.get("CultureMech")
    if cm_path is None or not cm_path.exists():
        print(
            "No CultureMech sibling path configured (set COMMUNITYMECH_SIBLING_REPOS "
            "or --culturemech). Nothing to match against.",
            file=sys.stderr,
        )
        return 2

    media_by_env = culturemech_media_by_environment(cm_path)

    envo_adapter = None
    if args.subsumption:
        envo_adapter = get_envo_adapter()
        if envo_adapter is None:
            print(
                "--subsumption requested but ENVO sqlite not cached locally; "
                "falling back to exact matches only.",
                file=sys.stderr,
            )

    paths = args.yaml_paths or sorted(COMMUNITY_DIR.glob("*.yaml"))
    total_suggestions = 0
    communities_with_suggestions = 0
    skipped_generic = 0
    for path in paths:
        try:
            data = yaml.safe_load(path.read_bytes()) or {}
        except (OSError, yaml.YAMLError):
            continue
        env = _community_env(data)
        if env is None:
            continue
        envo_id, env_label = env
        if envo_id in GENERIC_ENVIRONMENTS and not args.include_generic:
            skipped_generic += 1
            continue
        exclude_subtypes = frozenset() if args.include_generic else GENERIC_ENVIRONMENTS
        matches = _matches_for(envo_id, media_by_env, envo_adapter, exclude_subtypes)
        already = _linked_culturemech_ids(data)
        fresh = [(h, rel) for h, rel in matches if h.culturemech_id not in already]
        if not fresh:
            continue
        communities_with_suggestions += 1
        total_suggestions += len(fresh)
        n_sub = sum(1 for _, rel in fresh if rel == "subtype")
        blocks = _suggestion_block(fresh, envo_id, env_label)
        sub_note = f" ({n_sub} via ENVO subtype)" if n_sub else ""
        print(f"\n# {path.name}  —  environment {envo_id} ({env_label})")
        print(f"# {len(fresh)} suggested related_media{sub_note} (paste under `related_media:`)")
        print(yaml.safe_dump(blocks, sort_keys=False, allow_unicode=True).rstrip())

    note = ""
    if skipped_generic and not args.include_generic:
        note = (
            f" Skipped {skipped_generic} community(ies) whose only environment is "
            "over-generic (e.g. laboratory environment); use --include-generic to include."
        )
    print(
        f"\n# ---\n# {total_suggestions} media suggestion(s) across "
        f"{communities_with_suggestions} community(ies).{note}",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
