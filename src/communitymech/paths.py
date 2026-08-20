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
DATA_ISOLATES = REPO_ROOT / "data" / "isolates"
KB_TAXA = REPO_ROOT / "kb" / "taxa"


def default_record_roots() -> list[Path]:
    """Every directory holding `MicrobialCommunity` records, in one place.

    The validators, the term checks and the network audit each need this list,
    and each used to carry its own copy. They drifted: `data/isolates/**` was
    added to `validate_strict`, `validate-all`, `validate-terms-all` and
    `validate-references-all`, but the network auditor kept its own
    `Path("kb/communities")` default and never saw an isolate's interactions
    (#350).

    Defining it once does not by itself keep a *new* directory in step — that is
    what `tests/test_record_roots_are_shared.py` is for — but it removes the
    copies that made the drift invisible.
    """
    return [KB_COMMUNITIES, DATA_ISOLATES]


def taxon_descriptor_roots() -> list[Path]:
    """Every directory whose records can carry a `TaxonDescriptor` (#656).

    A superset of `default_record_roots()`, and a different question. That list
    answers "where do `MicrobialCommunity` records live"; this one answers "where
    can a `gtdb_classification` be", which the schema decides:

        MicrobialCommunity.taxonomy[].taxon_term -> TaxonDescriptor
        CommonTaxon.taxon_term                   -> TaxonDescriptor

    and `TaxonDescriptor` carries `gtdb_grounding_status`, `gtdb_candidates` and
    `gtdb_classification`. `CommonTaxon` records live in `kb/taxa`, so a GTDB
    gate that sweeps only the community roots cannot see a grounding there.

    Three such gates did exactly that, each with its own
    `RECORD_DIRS = ("kb/communities", "data/isolates")`. It was harmless only by
    accident: `kb/taxa` holds 2 records with 0 `gtdb_classification` blocks
    today, so there was nothing to miss. The first taxon record to gain one would
    have been skipped by all three, silently and with a clean report.

    Kept separate from `default_record_roots()` rather than widening it: callers
    that mean "community records" — the network auditor, `validate_strict` — must
    not start sweeping a different root class by side effect.
    """
    return [KB_COMMUNITIES, DATA_ISOLATES, KB_TAXA]


def looks_like_a_checkout() -> bool:
    """Is `REPO_ROOT` really the repo, or did a wheel install fool `__file__`?"""
    return (REPO_ROOT / "pyproject.toml").is_file() and (REPO_ROOT / "kb").is_dir()
