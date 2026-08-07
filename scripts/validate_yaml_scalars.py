#!/usr/bin/env python3
"""Report YAML scalars a mid-line `#` will silently truncate (#398).

In YAML a `#` preceded by whitespace opens a comment, even mid-value, so an
unquoted scalar loses its tail while the file stays valid and the value stays
non-empty. No schema check can see it; this reads the raw lines.

    just validate-scalars kb/communities/Foo.yaml
    just validate-scalars            # every record

Exits 1 if anything is found, so it can gate on its own. The same check runs
inside `just validate-strict`.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from communitymech.validators.yaml_scalars import find_truncated_scalars  # noqa: E402

# `kb/taxa` is deliberately included and is *not* covered by validate-strict,
# whose DEFAULT_ROOTS are the two record trees. It reaches CI through pytest
# instead (#399 review, #391).
DEFAULT_DIRS = ("kb/communities", "data/isolates", "kb/taxa")

# Trees where a trailing comment is an ordinary idiom, so the strict rule would
# report 13 deliberate comments as truncation. Checked under `--require-gap`
# instead: report only a `#` written tight against the value (#400). Also .yml,
# which the workflows use and the record trees do not.
IDIOMATIC_DIRS = ("conf", ".github/workflows", "vocab", "src/communitymech/schema")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", type=Path, help="YAML file(s); default: all records")
    parser.add_argument(
        "--require-gap",
        action="store_true",
        help=(
            "Report only comments written tight against the value (<2 spaces "
            "before the #). For trees where deliberate trailing comments are an "
            "idiom; a convention check rather than a proof (#400)."
        ),
    )
    parser.add_argument(
        "--idiomatic",
        action="store_true",
        help=(
            f"Check {', '.join(IDIOMATIC_DIRS)} instead of the record trees, "
            f"which implies --require-gap."
        ),
    )
    args = parser.parse_args(argv)
    require_gap = args.require_gap or args.idiomatic

    directories = IDIOMATIC_DIRS if args.idiomatic else DEFAULT_DIRS
    paths = args.files or [
        path
        for directory in directories
        for suffix in ("*.yaml", "*.yml")
        for path in sorted((REPO_ROOT / directory).rglob(suffix))
    ]
    # A directory argument is what `validate_strict.py` accepts, so accept it
    # here too rather than dying on IsADirectoryError. The two CLIs disagreeing
    # on their contract is a trap for whoever wires them together (#399 review).
    expanded: list[Path] = []
    for path in paths:
        if path.is_dir():
            expanded.extend(sorted(p for s in ("*.yaml", "*.yml") for p in path.rglob(s)))
        else:
            expanded.append(path)
    paths = expanded
    if not paths:
        print("[scalars] no files to check", file=sys.stderr)
        return 2

    issues = []
    for path in paths:
        if not path.exists():
            print(f"[scalars] no such file: {path}", file=sys.stderr)
            return 2
        issues.extend(find_truncated_scalars(path, require_gap=require_gap))

    for issue in issues:
        print(issue)

    print(f"\nfiles checked: {len(paths)}", file=sys.stderr)
    print(f"truncated scalars: {len(issues)}", file=sys.stderr)
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
