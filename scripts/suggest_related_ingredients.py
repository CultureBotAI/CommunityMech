#!/usr/bin/env python3
"""DRAFT: suggest environment-matched MIM ingredients for communities (issue #30, Use Case 1).

The ingredient analog of ``suggest_related_media.py``. For each community, match its
``environment_term`` ENVO id against MediaIngredientMech (MIM) ingredients that
declare the same ``environmental_context``, and emit ready-to-review
``related_ingredients`` blocks (``chebi_term`` + ``shared_environment_term``) for a
curator to paste. Suggestion-only — never edits records.

**Status: DRAFT, pending MediaIngredientMech#119.** It links via the ingredient's
**CHEBI** term (`RelatedIngredient.chebi_term`) — the "CHEBI route" — which needs
no `MediaIngredientMech:NNNNNN` id and works today for MIM records whose
`identifier` is a CHEBI CURIE. It does **not** emit `mediaingredientmech_id`,
because MIM's canonical id is `MIM:<name>` (not the schema's pattern); that
reconciliation is the open question in MIM#119. Do not merge for production use
until MIM confirms the CHEBI route is an acceptable link (#119 ask c).

`chebi_term.label` is set to the **canonical** ChEBI label (from the local ChEBI
sqlite), not MIM's free-text ingredient name, so the id↔label gate stays green.
Records whose CHEBI label can't be resolved locally are skipped (reported).

Sibling repo path comes from ``COMMUNITYMECH_SIBLING_REPOS`` (``Name=path``) or
``--mediaingredientmech``; point it at the MIM repo root. Add ``--subsumption`` to
also match ENVO subtype environments.

Usage:
    COMMUNITYMECH_SIBLING_REPOS="MediaIngredientMech=../MediaIngredientMech" \\
        PYTHONPATH=src uv run python scripts/suggest_related_ingredients.py
"""

import argparse
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from communitymech.cross_repo_environment import (  # noqa: E402
    GENERIC_ENVIRONMENT_TERMS as GENERIC_ENVIRONMENTS,
    envo_subtypes,
    get_chebi_adapter,
    get_envo_adapter,
    mim_ingredients_by_environment,
    sibling_repos_from_env,
)

REPO_ROOT = Path(__file__).parent.parent
COMMUNITY_DIR = REPO_ROOT / "kb" / "communities"


def _community_env(data: dict):
    et = data.get("environment_term")
    term = (et or {}).get("term") if isinstance(et, dict) else None
    if not isinstance(term, dict):
        return None
    envo_id = term.get("id")
    if isinstance(envo_id, str) and envo_id.startswith("ENVO:"):
        return envo_id, term.get("label") or ""
    return None


def _linked_chebi_ids(data: dict) -> set[str]:
    """CHEBI ids already referenced by the community's related_ingredients."""
    linked: set[str] = set()
    for entry in data.get("related_ingredients") or []:
        if isinstance(entry, dict):
            ct = entry.get("chebi_term")
            if isinstance(ct, dict) and ct.get("id"):
                linked.add(ct["id"])
    return linked


def _ingredient_matches(envo_id, ing_by_env, envo_adapter, exclude_subtype_envs=frozenset()):
    """[(IngredientHit, relation)] for a community ENVO term, exact + optional subtypes."""
    seen: dict[str, tuple] = {}
    for hit in ing_by_env.get(envo_id, []):
        if hit.chebi_id:
            seen[hit.chebi_id] = (hit, "exact")
    if envo_adapter is not None:
        for sub in envo_subtypes(envo_id, envo_adapter):
            if sub in exclude_subtype_envs:
                continue
            for hit in ing_by_env.get(sub, []):
                if hit.chebi_id:
                    seen.setdefault(hit.chebi_id, (hit, "subtype"))
    return list(seen.values())


def _blocks(matches, envo_id, env_label, chebi_adapter):
    """Render related_ingredients dicts; skip any whose canonical CHEBI label is unresolved."""
    blocks, unresolved = [], []
    for hit, relation in sorted(matches, key=lambda m: m[0].chebi_id):
        canonical = chebi_adapter.label(hit.chebi_id) if chebi_adapter is not None else None
        if not canonical:
            unresolved.append(hit.chebi_id)
            continue
        if relation == "exact":
            note = (
                f"MIM ingredient shares environment '{env_label}' ({envo_id}) with this "
                "community; surfaced by env-based cross-repo match (CHEBI route)."
            )
        else:
            note = (
                f"MIM ingredient environment '{hit.env_label}' ({hit.env_id}) is a subtype of "
                f"this community's '{env_label}' ({envo_id}); ENVO-subsumption match (CHEBI route)."
            )
        blocks.append(
            {
                "preferred_term": hit.name,
                "chebi_term": {"id": hit.chebi_id, "label": canonical},
                "shared_environment_term": {"id": envo_id, "label": env_label},
                "relevance": note,
            }
        )
    return blocks, unresolved


def main() -> int:
    parser = argparse.ArgumentParser(description="DRAFT ingredient suggester (issue #30)")
    parser.add_argument("yaml_paths", nargs="*", type=Path)
    parser.add_argument("--mediaingredientmech", type=Path, help="Path to MIM repo/records")
    parser.add_argument("--include-generic", action="store_true")
    parser.add_argument("--subsumption", action="store_true")
    args = parser.parse_args()

    sibling_repos = sibling_repos_from_env()
    if args.mediaingredientmech is not None:
        sibling_repos["MediaIngredientMech"] = args.mediaingredientmech
    mim_path = sibling_repos.get("MediaIngredientMech")
    if mim_path is None or not mim_path.exists():
        print(
            "No MediaIngredientMech sibling path configured (COMMUNITYMECH_SIBLING_REPOS "
            "or --mediaingredientmech).",
            file=sys.stderr,
        )
        return 2

    print(
        "# DRAFT — pending MediaIngredientMech#119 (CHEBI-route ingredient linking). "
        "Review before applying.",
    )
    ing_by_env = mim_ingredients_by_environment(mim_path)
    chebi_adapter = get_chebi_adapter()
    if chebi_adapter is None:
        print("# WARNING: ChEBI sqlite not cached; cannot resolve canonical labels — no output.")
        return 0
    envo_adapter = get_envo_adapter() if args.subsumption else None
    exclude_subtypes = frozenset() if args.include_generic else GENERIC_ENVIRONMENTS

    paths = args.yaml_paths or sorted(COMMUNITY_DIR.glob("*.yaml"))
    total, n_comm, all_unresolved = 0, 0, []
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
            continue
        matches = _ingredient_matches(envo_id, ing_by_env, envo_adapter, exclude_subtypes)
        already = _linked_chebi_ids(data)
        fresh = [(h, rel) for h, rel in matches if h.chebi_id not in already]
        if not fresh:
            continue
        blocks, unresolved = _blocks(fresh, envo_id, env_label, chebi_adapter)
        all_unresolved += unresolved
        if not blocks:
            continue
        n_comm += 1
        total += len(blocks)
        print(f"\n# {path.name}  —  environment {envo_id} ({env_label})")
        print(f"# {len(blocks)} suggested related_ingredients (paste under `related_ingredients:`)")
        print(yaml.safe_dump(blocks, sort_keys=False, allow_unicode=True).rstrip())

    extra = f" {len(set(all_unresolved))} skipped (unresolved CHEBI label)." if all_unresolved else ""
    print(f"\n# ---\n# {total} ingredient suggestion(s) across {n_comm} community(ies).{extra}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
