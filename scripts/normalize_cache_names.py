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

# The name a rename passes through, so that `DOI_x.md` -> `doi_x.md` is two
# real renames rather than one no-op on a filesystem that ignores case.
TEMPORARY_SUFFIX = ".casetmp"


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
    temporary = current.with_name(current.name + TEMPORARY_SUFFIX)
    if temporary.exists():
        # `Path.rename` would clobber it without a word, and a leftover
        # temporary IS a cache file -- an earlier run died holding it. Refuse
        # and let `recover` deal with it (#705).
        return (
            f"[conflict] {current.name}: {temporary.name} is left over from an "
            f"interrupted run; it holds a fetch nothing else can reach"
        )
    current.rename(temporary)
    temporary.rename(wanted)
    return f"[renamed] {current.name} -> {wanted.name}"


def orphans(cache_dir: Path) -> list[Path]:
    """Temporaries left behind by a run that died between the two renames."""
    return [
        path
        for path in sorted(cache_dir.iterdir())
        if path.is_file() and path.name.endswith(TEMPORARY_SUFFIX)
    ]


def recover(path: Path) -> str:
    """Finish an interrupted rename, rather than leaving the fetch unreachable.

    A `.casetmp` file is invisible twice over: no reader resolves the name, and
    `canonical_cache_name` returns None for it, so a later run of this script
    passes straight over it. The reference then reads as a cache MISS, and a
    miss sends the fetcher back to the network -- the loop #697 closes, reached
    from the other side (#705).
    """
    stem = path.name[: -len(TEMPORARY_SUFFIX)]
    wanted = path.with_name(canonical_cache_name(stem) or stem)
    if wanted.exists() and not _same_file(path, wanted):
        return f"[conflict] {path.name}: {wanted.name} already exists and differs"
    path.rename(wanted)
    return f"[recovered] {path.name} -> {wanted.name}"


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

    conflicts = 0

    # Before anything else: an interrupted earlier run leaves a `.casetmp`
    # holding a real fetch that nothing can reach, and it also blocks the rename
    # that would have produced it (#705).
    for path in orphans(args.cache_dir):
        if args.check:
            print(f"[would recover] {path.name}")
            conflicts += 1
            continue
        message = recover(path)
        print(message)
        conflicts += message.startswith("[conflict]")

    pairs = plan(args.cache_dir)
    for current, wanted in pairs:
        if args.check:
            print(f"[would rename] {current.name} -> {wanted.name}")
            continue
        message = rename(current, wanted)
        print(message)
        conflicts += message.startswith("[conflict]")

    if args.check:
        return 1 if (pairs or conflicts) else 0
    # A conflict is left for a human: both casings exist as distinct files, and
    # choosing between two fetches of the same reference is not this script's
    # call.
    return 1 if conflicts else 0


if __name__ == "__main__":
    raise SystemExit(main())
