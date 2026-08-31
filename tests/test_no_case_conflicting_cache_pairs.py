"""Two cache files differing only by prefix case cannot both be reachable (#706).

`scripts/normalize_cache_names.py` renames `DOI_x.md` to `doi_x.md`, and when
BOTH already exist as distinct tracked files it reports a `[conflict]` and
refuses — choosing between two fetches of the same reference is not a script's
call. But the justfile recipes discard the normaliser's exit code (deliberately:
normalising must not turn a failing validation green), so that conflict is one
printed line and nothing else.

**Why the existing case-exactness test does not close this.**
`test_reference_cache_names_are_case_exact.py` reads
`os.listdir(REFERENCES_CACHE)` — the filesystem. macOS cannot hold `DOI_x.md`
and `doi_x.md` at once, so on a developer machine the pair is invisible and the
divergence only appears on Linux. That is #690's lesson stated as a test: a
green local run is not a green CI run.

Reading git's index instead makes the check case-exact on every machine, because
git records the name it was told regardless of what the filesystem will store.
"""

from __future__ import annotations

import collections
import pathlib
import subprocess

REPO = pathlib.Path(__file__).parent.parent


def _tracked_cache_names() -> list[str]:
    """Cache filenames as GIT records them, not as the filesystem reports them."""
    result = subprocess.run(
        ["git", "ls-files", "-z", "--", "references_cache/"],
        cwd=REPO,
        capture_output=True,
        text=True,
        timeout=120,
        check=True,
    )
    # -z, because a path containing a space or a newline would otherwise split
    # into several bogus entries -- the whitespace-splitting trap.
    return [entry.rsplit("/", 1)[-1] for entry in result.stdout.split("\0") if entry]


def test_there_are_tracked_cache_files_to_check():
    """A finder that found nothing would make the check below vacuous."""
    names = _tracked_cache_names()
    assert len(names) >= 400, f"only {len(names)} tracked cache files; the listing broke"


def test_no_two_tracked_caches_differ_only_by_case():
    """One reference must not have two files whose names differ only in case.

    On a case-sensitive filesystem both exist and only one is reachable, so the
    other is a fetch nothing can read -- and which one wins depends on which
    casing the citation happens to use.
    """
    by_folded = collections.defaultdict(list)
    for name in _tracked_cache_names():
        by_folded[name.casefold()].append(name)

    clashes = {folded: sorted(names) for folded, names in by_folded.items() if len(set(names)) > 1}
    assert clashes == {}, (
        "these cache files differ only by case, so on a case-sensitive "
        "filesystem both exist and at most one is reachable (#706). The "
        "normaliser reports this as a [conflict] and refuses to choose; a human "
        "has to decide which fetch to keep:\n  "
        + "\n  ".join(f"{folded}: {names}" for folded, names in sorted(clashes.items()))
    )
