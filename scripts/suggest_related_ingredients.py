#!/usr/bin/env python3
"""Suggest environment-matched MIM ingredients for communities (issue #30, Use Case 1).

The ingredient analog of ``suggest_related_media.py``. For each community, match its
ENVO environment(s) — ``environment_term`` plus every ``modeled_environment`` — against
MediaIngredientMech (MIM) ingredients that declare the same ``environmental_context``,
and emit ready-to-review ``related_ingredients`` blocks (``chebi_term`` +
``shared_environment_term``) for a curator to paste. Suggestion-only — never edits records.

**CHEBI route, per MediaIngredientMech#119.** MIM confirmed:
* ``MediaIngredientMech:NNNNNN`` is vestigial — this tool never emits it.
* The equivalence-safe join is the ingredient's CHEBI term taken from MIM's SSSOM
  ``skos:exactMatch`` rows (NOT the record ``identifier`` field, and NOT
  close/narrowMatch). ``cross_repo_environment.mim_ingredients_by_environment`` does
  that join; ingredients with no exactMatch CHEBI (environment materials grounded to
  ENVO/MICRO, protein digests ChEBI can't represent, …) are skipped.

``chebi_term.label`` is resolved to the **canonical** ChEBI label (from the local
ChEBI sqlite), not MIM's free-text name, so the id↔label gate stays green; records
whose CHEBI label can't be resolved locally are skipped (reported).

Sibling repo path comes from ``COMMUNITYMECH_SIBLING_REPOS`` (``Name=path``) or
``--mediaingredientmech``; point it at the MIM repo root (needs both
``data/ingredients/`` and ``mappings/``). Add ``--subsumption`` to also match ENVO
subtype environments.
"""

import argparse
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from communitymech.cross_repo_environment import (  # noqa: E402
    GENERIC_ENVIRONMENT_TERMS as GENERIC_ENVIRONMENTS,
)
from communitymech.cross_repo_environment import (
    envo_subtypes,
    get_chebi_adapter,
    get_envo_adapter,
    mim_ingredients_by_environment,
    sibling_repos_from_env,
)

REPO_ROOT = Path(__file__).parent.parent
COMMUNITY_DIR = REPO_ROOT / "kb" / "communities"


def _env_from_descriptor(desc):
    term = desc.get("term") if isinstance(desc, dict) else None
    if not isinstance(term, dict):
        return None
    envo_id = term.get("id")
    if isinstance(envo_id, str) and envo_id.startswith("ENVO:"):
        return envo_id, term.get("label") or ""
    return None


def _community_envs(data: dict):
    """All ENVO (id, label) keys: environment_term + every modeled_environment."""
    envs, seen = [], set()
    et = _env_from_descriptor(data.get("environment_term"))
    if et:
        envs.append(et)
        seen.add(et[0])
    for desc in data.get("modeled_environment") or []:
        me = _env_from_descriptor(desc)
        if me and me[0] not in seen:
            envs.append(me)
            seen.add(me[0])
    return envs


def _linked_chebi_ids(data: dict) -> set[str]:
    linked = set()
    for entry in data.get("related_ingredients") or []:
        if isinstance(entry, dict):
            ct = entry.get("chebi_term")
            if isinstance(ct, dict) and ct.get("id"):
                linked.add(ct["id"])
    return linked


def _matches_for(envo_id, ing_by_env, envo_adapter, exclude_subtype_envs=frozenset()):
    """[(IngredientHit, relation)] with a CHEBI id, exact + optional subtypes."""
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


def _block(hit, relation, envo_id, env_label, canonical):
    if relation == "exact":
        note = (
            f"MIM ingredient shares environment '{env_label}' ({envo_id}) with this "
            "community; CHEBI route (skos:exactMatch) per MediaIngredientMech#119."
        )
    else:
        note = (
            f"MIM ingredient environment '{hit.env_label}' ({hit.env_id}) is a subtype of "
            f"this community's '{env_label}' ({envo_id}); ENVO-subsumption CHEBI route."
        )
    return {
        "preferred_term": hit.name,
        "chebi_term": {"id": hit.chebi_id, "label": canonical},
        "shared_environment_term": {"id": envo_id, "label": env_label},
        "relevance": note,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("yaml_paths", nargs="*", type=Path)
    parser.add_argument("--mediaingredientmech", type=Path, help="Path to MIM repo root")
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

    chebi_adapter = get_chebi_adapter()
    if chebi_adapter is None:
        print(
            "ChEBI sqlite not cached; cannot resolve canonical labels — no output.", file=sys.stderr
        )
        return 0
    ing_by_env = mim_ingredients_by_environment(mim_path)
    envo_adapter = get_envo_adapter() if args.subsumption else None
    exclude_subtypes = frozenset() if args.include_generic else GENERIC_ENVIRONMENTS

    paths = args.yaml_paths or sorted(COMMUNITY_DIR.glob("*.yaml"))
    total, n_comm, unresolved = 0, 0, []
    for path in paths:
        try:
            data = yaml.safe_load(path.read_bytes()) or {}
        except (OSError, yaml.YAMLError):
            continue
        envs = _community_envs(data)
        active = [
            (e, lbl) for e, lbl in envs if args.include_generic or e not in GENERIC_ENVIRONMENTS
        ]
        if not active:
            continue
        already = _linked_chebi_ids(data)
        seen_chebi = set(already)
        groups = []
        for eid, lbl in active:
            matches = _matches_for(eid, ing_by_env, envo_adapter, exclude_subtypes)
            blocks = []
            for hit, rel in sorted(matches, key=lambda m: m[0].chebi_id):
                if hit.chebi_id in seen_chebi:
                    continue
                canonical = chebi_adapter.label(hit.chebi_id)
                if not canonical:
                    unresolved.append(hit.chebi_id)
                    continue
                seen_chebi.add(hit.chebi_id)
                blocks.append(_block(hit, rel, eid, lbl, canonical))
            if blocks:
                groups.append((eid, lbl, blocks))
        if not groups:
            continue
        n_comm += 1
        total += sum(len(g[2]) for g in groups)
        print(f"\n# {path.name}")
        for eid, lbl, blocks in groups:
            print(f"#   {eid} ({lbl}) — {len(blocks)} related_ingredients")
            print(yaml.safe_dump(blocks, sort_keys=False, allow_unicode=True).rstrip())

    extra = f" {len(set(unresolved))} skipped (unresolved CHEBI label)." if unresolved else ""
    print(f"\n# ---\n# {total} ingredient suggestion(s) across {n_comm} community(ies).{extra}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
