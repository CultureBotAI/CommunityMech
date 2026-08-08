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

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from communitymech.validators.yaml_scalars import find_truncated_scalars  # noqa: E402

# `kb/taxa` is deliberately included and is *not* covered by validate-strict,
# whose DEFAULT_ROOTS are the two record trees. It reaches CI through pytest
# instead (#399 review, #391).
DEFAULT_DIRS = ("kb/communities", "data/isolates", "kb/taxa")

# The non-record YAML trees, which had no scalar check at all (#400). `.github`
# rather than `.github/workflows`, so a future dependabot.yml or ISSUE_TEMPLATE
# is covered; `history` and `examples` carry prose and were missed by the first
# pass (review of #488).
IDIOMATIC_DIRS = (
    "conf",
    ".github",
    "vocab",
    "src/communitymech/schema",
    "history",
    "examples",
)

# The strict rule runs on these trees too. Only these three files use a
# deliberate trailing comment, and only they are relaxed to the gap rule.
#
# The first version relaxed all 21 files to buy the 3 — spending the strong
# guarantee on 18 that did not need it, including every file in `vocab/` and the
# schema, which have no trailing comments at all (review of #488). A per-file
# list does go stale, which is what #400 says about allowlists; the answer is
# that going stale here means a file gets *stricter* than it needs and reports a
# comment somebody wrote on purpose, which is visible and cheap. The failure
# mode of the alternative is silence.
RELAXED_FILES = frozenset(
    {
        "conf/id_label_targets.yaml",
        ".github/workflows/curation-history.yaml",
        ".github/workflows/kgx-release.yaml",
    }
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", type=Path, help="YAML file(s); default: all records")
    parser.add_argument(
        "--idiomatic",
        action="store_true",
        help=(
            f"Check the non-record trees ({', '.join(IDIOMATIC_DIRS)}) instead of "
            f"the records. Strict everywhere except the {len(RELAXED_FILES)} files "
            f"that use a deliberate trailing comment (#400)."
        ),
    )
    args = parser.parse_args(argv)

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
    unparseable = []
    for path in paths:
        if not path.exists():
            print(f"[scalars] no such file: {path}", file=sys.stderr)
            return 2
        # `find_truncated_scalars` returns [] for a file it cannot parse, which
        # is right for the record trees — `validate-strict` reports
        # yaml_parse_error separately there. The non-record trees have no such
        # backstop, so an unparseable file would pass this sweep at exit 0 and
        # take any real truncation in it down with it (review of #488).
        if args.idiomatic:
            try:
                yaml.safe_load(path.read_text())
            except yaml.YAMLError as exc:
                unparseable.append(f"{path}: {str(exc).splitlines()[0]}")
                continue
        # Per file, not per run: the record trees are never relaxed, and
        # neither are the 18 non-record files that do not need it.
        relative = path.resolve().relative_to(REPO_ROOT).as_posix()
        issues.extend(find_truncated_scalars(path, require_gap=relative in RELAXED_FILES))

    for issue in issues:
        print(issue)

    for problem in unparseable:
        print(f"[scalars] unparseable, so NOT checked: {problem}", file=sys.stderr)

    print(f"\nfiles checked: {len(paths) - len(unparseable)}", file=sys.stderr)
    print(f"truncated scalars: {len(issues)}", file=sys.stderr)
    if unparseable:
        print(f"unparseable files: {len(unparseable)}", file=sys.stderr)
    return 1 if issues or unparseable else 0


if __name__ == "__main__":
    raise SystemExit(main())
