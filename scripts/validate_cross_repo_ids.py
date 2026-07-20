#!/usr/bin/env python3
"""CLI: validate cross-repo CultureMech IDs (related_media) in one or more community YAMLs.

Pattern checks always run. Existence checks run only when a CultureMech sibling-repo
path is supplied via flag or via the COMMUNITYMECH_SIBLING_REPOS environment
variable (comma-separated `Name=path` pairs). `related_ingredients` is no longer
checked — the MediaIngredientMech:NNNNNN scheme is vestigial (MediaIngredientMech#119).

Usage:
    PYTHONPATH=src uv run python scripts/validate_cross_repo_ids.py kb/communities/X.yaml
    PYTHONPATH=src uv run python scripts/validate_cross_repo_ids.py kb/communities/X.yaml \\
        --culturemech ../CultureMech/kb/media
    PYTHONPATH=src uv run python scripts/validate_cross_repo_ids.py kb/communities/*.yaml
"""

import argparse
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from communitymech.validators.cross_repo_ids import validate_cross_repo_ids


def _sibling_repos_from_env() -> dict[str, Path]:
    raw = os.environ.get("COMMUNITYMECH_SIBLING_REPOS", "").strip()
    if not raw:
        return {}
    out: dict[str, Path] = {}
    for pair in raw.split(","):
        if "=" not in pair:
            continue
        name, path = pair.split("=", 1)
        out[name.strip()] = Path(path.strip())
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("yaml_paths", nargs="+", type=Path)
    parser.add_argument("--culturemech", type=Path, help="Path to CultureMech kb/ dir")
    args = parser.parse_args()

    sibling_repos = _sibling_repos_from_env()
    if args.culturemech is not None:
        sibling_repos["CultureMech"] = args.culturemech

    total_errors = 0
    for yaml_path in args.yaml_paths:
        if not yaml_path.exists():
            print(f"[skipped] {yaml_path}: file not found")
            continue
        issues = validate_cross_repo_ids(yaml_path, sibling_repos=sibling_repos)
        errors = [i for i in issues if i.severity == "error"]
        if not issues:
            print(f"[ok] {yaml_path}")
            continue
        print(f"[{len(errors)} error(s)] {yaml_path}")
        for issue in issues:
            print(f"  {issue}")
        total_errors += len(errors)

    return 1 if total_errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
