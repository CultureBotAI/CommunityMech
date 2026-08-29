"""Rename cache files the fetcher wrote with a prefix casing nothing resolves to.

`linkml-reference-validator` normalises a reference id to `DOI:` and builds its
cache path from that, so every cache miss it fills writes `DOI_*.md`
(``etl/reference_fetcher.py:204-225``). Every reader in this repository builds
`doi_...` from the `doi:` citation, so those files are unreachable on a
case-sensitive filesystem — and per ``src/communitymech/paths.py`` an unreachable
cache is not a skip, it sends the fetcher back to the network. 133 of them
accumulated that way before #690, and #697 is the loop that refills the set.

This runs after the validator rather than instead of it. The dependency is not
ours to change; what is ours is that its output leaves the tree in a state the
next run can use.

**Renaming on a case-insensitive filesystem.** ``Path.rename`` from `DOI_x.md` to
`doi_x.md` is a no-op on macOS — same file — so each rename goes via a temporary
name. On Linux both forms can exist at once, which is a genuine conflict rather
than a rename: those are reported and left alone, because picking a winner would
silently discard one fetch.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from communitymech.paths import REFERENCES_CACHE, canonical_cache_name


def plan(cache_dir: Path) -> list[tuple[Path, Path]]:
    """(current, wanted) for every file whose prefix casing is wrong."""
    pairs = []
    for path in sorted(cache_dir.iterdir()):
        if not path.is_file():
            continue
        wanted = canonical_cache_name(path.name)
        if wanted is not None:
            pairs.append((path, path.with_name(wanted)))
    return pairs


def rename(current: Path, wanted: Path) -> str:
    """Rename via a temporary name, so it works where case is ignored."""
    if wanted.exists() and not _same_file(current, wanted):
        return f"[conflict] {current.name}: {wanted.name} already exists and differs"
    temporary = current.with_name(current.name + ".casetmp")
    current.rename(temporary)
    temporary.rename(wanted)
    return f"[renamed] {current.name} -> {wanted.name}"


def _same_file(a: Path, b: Path) -> bool:
    """True when the filesystem ignores case and both names are one file."""
    try:
        return a.stat().st_ino == b.stat().st_ino
    except OSError:
        return False


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache-dir", type=Path, default=REFERENCES_CACHE)
    parser.add_argument(
        "--check",
        action="store_true",
        help="report without renaming, and exit 1 if anything needs it",
    )
    args = parser.parse_args(argv)

    if not args.cache_dir.is_dir():
        print(f"no cache directory at {args.cache_dir}", file=sys.stderr)
        return 0  # nothing to normalise is not an error

    pairs = plan(args.cache_dir)
    if not pairs:
        return 0

    conflicts = 0
    for current, wanted in pairs:
        if args.check:
            print(f"[would rename] {current.name} -> {wanted.name}")
            continue
        message = rename(current, wanted)
        print(message)
        conflicts += message.startswith("[conflict]")

    if args.check:
        return 1
    # A conflict is left for a human: both casings exist as distinct files, and
    # choosing between two fetches of the same reference is not this script's
    # call.
    return 1 if conflicts else 0


if __name__ == "__main__":
    raise SystemExit(main())
