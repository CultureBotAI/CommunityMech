"""Repo-anchored locations for the artifacts this package reads and writes (#407).

Several defaults were plain relative strings — ``Path("reports")``,
``"references_cache"``, ``"docs/communities"`` — resolved against the *working
directory*. Run from anywhere but the repo root they wrote stray trees, and the
targets are git-tracked, so a caller could also overwrite committed files.

The sharpest case was the literature cache. `LiteratureFetcher` defaulted to
``references_cache`` and `mkdir`-ed it, so running from another directory created
a second, empty cache and re-fetched from PubMed and CrossRef — a silent cache
miss and billed network traffic, not merely an untidy tree. The committed cache
exists for reproducibility; a miss defeats it quietly.

Anchoring on ``__file__`` assumes the package is imported from a source checkout.
That is how this repo installs today (editable) and how `scripts/` already
resolves its own paths — but `pyproject.toml` does declare a setuptools build and
a console script, so a wheel install is a supported build even if nobody uses it.
Under one, ``parents[2]`` lands in ``site-packages``' parent and every constant
here would point somewhere nobody looks, which for the literature cache means a
silent re-fetch into a directory destroyed on the next venv rebuild.

`looks_like_a_checkout()` makes that loud rather than silent; callers that care
can check it. It is deliberately not raised at import time, because importing a
path module should not be able to break an otherwise working install.
"""

from __future__ import annotations

from pathlib import Path

# src/communitymech/paths.py -> src/communitymech -> src -> <repo>
REPO_ROOT = Path(__file__).resolve().parents[2]

REFERENCES_CACHE = REPO_ROOT / "references_cache"
REPORTS = REPO_ROOT / "reports"
DOCS = REPO_ROOT / "docs"
KB_COMMUNITIES = REPO_ROOT / "kb" / "communities"


def looks_like_a_checkout() -> bool:
    """Is `REPO_ROOT` really the repo, or did a wheel install fool `__file__`?"""
    return (REPO_ROOT / "pyproject.toml").is_file() and (REPO_ROOT / "kb").is_dir()
