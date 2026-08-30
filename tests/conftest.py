"""Session-wide setup for the test suite.

Its one job today is bytecode: making it impossible for a test to run a version
of a `scripts/` module that is not the one on disk (#693).

**The problem.** `scripts/` is not a package, so tests reach into it with
`importlib.util.spec_from_file_location(...)` + `exec_module` — 14 modules do,
13 of them against `scripts/gtdb_ground.py`. Each such load writes a
`scripts/__pycache__/*.pyc`, and Python validates that cache on **(mtime,
size)**. A source edit changing neither — a same-length substitution inside the
same second — is invisible to the loader, which serves the stale module.

**Why that is worse than a flaky run.** It was found producing a false RED:
`doi_` → `DOI_` in `scripts/cache_fulltext.py` is the same length, so a mutation
and its restore were indistinguishable and the test kept failing against correct
source. The same mechanism runs the other way. Mutate, see red (correctly),
restore, and see green *from the stale mutated module* — a mutation check
certifying a test that cannot fail. This repository's gate tests are written and
defended by exactly that ritual, so the two are not independent risks: the
mechanism can forge the evidence for the discipline that is supposed to catch it.

**The fix is two conditions, and it needs both.** Not writing new bytecode does
nothing about a `.pyc` left by an earlier session; removing the directory does
nothing if this session immediately writes a fresh one. So:

1. `sys.dont_write_bytecode` — no `.pyc` is created during the session, so
   nothing can go stale *within* it;
2. the `scripts/__pycache__` sweep — anything left by an earlier session, or by
   someone running a script by hand, cannot be read.

Both are asserted by `tests/test_no_stale_bytecode.py` rather than trusted.

**Scope.** `spec_from_file_location` is how this was found, not the boundary of
it. A regular import's bytecode is validated by the same (mtime, size) check, so
`src/communitymech/` is exposed identically — and it is mutated by gate work
more often than `scripts/` is.

**On deleting files from a fixture.** `__pycache__/` is gitignored derived data
whose only purpose is to be a cache, and the alternative is silently executing
code that is not in the repository. The cost of being wrong is one recompile.
"""

from __future__ import annotations

import os
import pathlib
import shutil
import sys

import pytest

REPO = pathlib.Path(__file__).parent.parent

# Directories whose modules tests load by file path rather than by import, so a
# stale entry is executed instead of the file under test.
LOADED_BY_PATH = ("scripts",)

# ...and the package the suite imports normally. `spec_from_file_location` is
# how this was FOUND, not the boundary of it: CPython validates a regular
# import's bytecode with the same (mtime, size) check, so a same-length edit to
# `src/communitymech/paths.py` between two runs is exactly as invisible. The
# gate work in this repository mutates that package as routinely as it mutates
# `scripts/`, so scoping the guard to the symptom would have left the more
# frequently mutated tree uncovered.
IMPORTED_NORMALLY = ("src/communitymech",)


def guarded_roots() -> list[pathlib.Path]:
    """The source trees whose bytecode must never shadow the file on disk."""
    return [REPO / name for name in (*LOADED_BY_PATH, *IMPORTED_NORMALLY)]


def _pycache_dirs() -> list[pathlib.Path]:
    """Every bytecode cache currently under a guarded root.

    Re-derived on each call, never cached. `rglob` because subpackages carry
    their own `__pycache__` -- a list of top-level directories would miss
    `export/`, `network/`, `validation/` and any added later.
    """
    return [d for root in guarded_roots() for d in sorted(root.rglob("__pycache__"))]


# Set at conftest import, which pytest does before collecting any test module —
# earlier than the first `exec_module` call, which is what matters.
sys.dont_write_bytecode = True

# ...and again for child processes, which `sys.dont_write_bytecode` does not
# reach. 26 test modules use subprocess and at least five invoke a `scripts/`
# module directly (audit_writers, gtdb_ground, validate_strict,
# validate_shared_taxon_ids, drop_obsolete_go_bp). Each child is a fresh
# interpreter that writes bytecode by default, so the in-process flag alone
# leaves scripts/__pycache__ repopulated by the very suite that swept it —
# which is the same hole, arrived at from outside.
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

for _directory in _pycache_dirs():
    if _directory.is_dir():
        shutil.rmtree(_directory, ignore_errors=True)


def _ncbi_adapter_available() -> bool:
    """Is the NCBITaxon SQLite database actually reachable right now?

    Asks `communitymech.ontology_adapters`, which is the single place the
    adapter is built. That matters more than the deduplication: while
    `ncbi_domain` and `shared_taxon_ids` each built their own, this predicate
    could only ever be about one of them, and the first version of this fixture
    was -- so it gated the 12 tests that fail when `ncbi_domain` has no adapter
    and left the nine that fail when `shared_taxon_ids` has none, which CI then
    found (#704).

    Why it can be unavailable at all: OAK downloads `ncbitaxon.db.gz` from
    `s3.amazonaws.com/bbop-sqlite`, and that URL has been answering **403** --
    verified from a developer machine, so it is upstream, not a runner. A cache
    step cannot repair it, since a cache only warms from a download that
    succeeds; it only preserves an already-warm one.
    """
    from communitymech.ontology_adapters import ncbitaxon_available

    return ncbitaxon_available()


@pytest.fixture
def requires_ncbi_adapter():
    """Skip a test that cannot mean anything without the taxonomy database.

    Deliberately NOT applied to the tests that assert the ABSENT case --
    `test_an_unavailable_adapter_degrades_rather_than_guesses` and
    `test_an_unavailable_ontology_is_reported_not_silently_passed` are the ones
    that must still run when the adapter is gone, since that is their subject.

    Nor to the one-directional half of `outside_gtdb_scope`: `False` must hold
    with or without a lookup, and that is the property the callers rely on.
    Skipping it because the database is missing would drop the safety check
    exactly when the risk is highest.
    """
    # Function-scoped on purpose. `ncbitaxon_adapter` is already lru_cached, so
    # re-asking costs nothing, and a session-scoped fixture would freeze the
    # answer at whatever the first test saw -- including a monkeypatched one.
    if not _ncbi_adapter_available():
        pytest.skip(
            "the NCBITaxon adapter is unavailable, so a taxonomy lookup cannot "
            "be made: this check was SKIPPED, NOT PASSED (#704). It is the "
            "wording `shared_taxon_ids` already prints to stderr for the same "
            "situation, and it is the whole safety of skipping -- a green run "
            "that had no ontology must never read as a clean KB."
        )
