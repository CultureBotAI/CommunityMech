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

**On deleting files from a fixture.** `__pycache__/` is gitignored derived data
whose only purpose is to be a cache, and the alternative is silently executing
code that is not in the repository. The cost of being wrong is one recompile.
"""

from __future__ import annotations

import os
import pathlib
import shutil
import sys

REPO = pathlib.Path(__file__).parent.parent

# Directories whose modules tests load by file path rather than by import, so a
# stale entry is executed instead of the file under test.
LOADED_BY_PATH = ("scripts",)


def _pycache_dirs() -> list[pathlib.Path]:
    return [REPO / name / "__pycache__" for name in LOADED_BY_PATH]


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
