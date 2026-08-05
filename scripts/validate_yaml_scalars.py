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

DEFAULT_DIRS = ("kb/communities", "data/isolates", "kb/taxa")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", type=Path, help="YAML file(s); default: all records")
    args = parser.parse_args(argv)

    paths = args.files or [
        path for directory in DEFAULT_DIRS for path in sorted((REPO_ROOT / directory).glob("*.yaml"))
    ]
    if not paths:
        print("[scalars] no files to check", file=sys.stderr)
        return 2

    issues = []
    for path in paths:
        if not path.exists():
            print(f"[scalars] no such file: {path}", file=sys.stderr)
            return 2
        issues.extend(find_truncated_scalars(path))

    for issue in issues:
        print(issue)

    print(f"\nfiles checked: {len(paths)}", file=sys.stderr)
    print(f"truncated scalars: {len(issues)}", file=sys.stderr)
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
