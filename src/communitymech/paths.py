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

Anchoring on ``__file__`` assumes the package is imported from a source checkout,
which is how this repo is installed (editable) and how `scripts/` already
resolves its own paths. A wheel installed into site-packages would compute a
nonsense root — acceptable here because nothing ships that way, and stated so the
assumption is visible rather than discovered.
"""

from __future__ import annotations

from pathlib import Path

# src/communitymech/paths.py -> src/communitymech -> src -> <repo>
REPO_ROOT = Path(__file__).resolve().parents[2]

REFERENCES_CACHE = REPO_ROOT / "references_cache"
REPORTS = REPO_ROOT / "reports"
DOCS = REPO_ROOT / "docs"
KB_COMMUNITIES = REPO_ROOT / "kb" / "communities"
