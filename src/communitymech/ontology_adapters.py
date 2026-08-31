"""One construction site for the NCBITaxon adapter (#704).

Two runtime modules needed the same OAK adapter and each built its own:
`validators/ncbi_domain.py` for `domain_of`, `validators/shared_taxon_ids.py`
for `rank_of` and `known_cores`. Same selector, same `try/except Exception:
return None`, same `lru_cache(maxsize=1)` — one fact written down twice.

**The cost was not duplication, it was measurement.** When
`https://s3.amazonaws.com/bbop-sqlite/ncbitaxon.db.gz` began returning 403, the
suite went red in a way that had nothing to do with the change under test. I
gated the tests that fail when *one* of those two copies returns None, checked
the count, and called it done. CI then failed on the other copy's dependants,
because a probe pointed at `ncbi_domain._adapter` cannot see anything that asks
`shared_taxon_ids._adapter`. Two copies meant a question about availability had
two answers and no way to notice they had diverged.

So the point of this module is less that the code is shared than that
`ncbitaxon_available()` is a *single* question with a *single* answer, which
`tests/conftest.py` and the guard test can both ask.

**Not included here on purpose:** the ENVO and ChEBI adapters in
`cross_repo_environment.py`. Those read a locally-cached sqlite by path and
return None when the file is absent, which is a different contract — nothing is
downloaded, so nothing can 403 — and folding them in would blur the one thing
this module is for.
"""

from __future__ import annotations

import functools
import os
from pathlib import Path
from typing import Any

# OAK's selector for the NCBITaxon SQLite build. Written once here so that a
# grep for it has exactly one hit under `src/`, which is what
# `tests/test_ncbitaxon_adapter_is_shared.py` asserts.
NCBITAXON_SELECTOR = "sqlite:obo:ncbitaxon"


def _local_build(name: str) -> Any | None:
    """The already-downloaded SQLite build for `name`, or None.

    **Why this is tried first.** `sqlite:obo:<name>` does not ask whether the
    database is usable; it asks pystow to ensure the **`.db.gz`** is present and
    re-downloads when it is not. So a machine holding a perfectly good
    `ncbitaxon.db` and no `.gz` re-downloads anyway — and while
    `s3.amazonaws.com/bbop-sqlite` answers 403, that turns a working ontology
    into "unavailable".

    That is not hypothetical. Verified on a developer machine: `go.db` (1.7 GB)
    and `cl.db` (0.5 GB) are present without their `.gz`, `sqlite:obo:go` fails,
    and `sqlite:<path>/go.db` answers `label("GO:0015979") == "photosynthesis"`.
    CI is the same shape — the `oaklib-Linux-v1` cache restores 6.7 GB
    successfully and every ontology was still reported unreachable (#707).

    Opening a path never touches the network, so this cannot mask an outage: if
    the file is absent we fall through to the selector exactly as before.
    """
    home = os.environ.get("PYSTOW_HOME")
    root = Path(home) if home else Path.home() / ".data"
    database = root / "oaklib" / f"{name}.db"
    if not database.is_file() or database.stat().st_size == 0:
        return None
    try:
        from oaklib import get_adapter  # type: ignore[import-untyped]

        return get_adapter(f"sqlite:{database}")
    except Exception:
        return None


@functools.lru_cache(maxsize=1)
def ncbitaxon_adapter() -> Any | None:
    """The NCBITaxon adapter, or None when it cannot be built.

    Cached because building it opens a large SQLite database and a grounding run
    asks about a few hundred taxa. Shared, so the two validators that need it
    open that database once between them rather than once each.

    None covers every reason the adapter is unavailable — oaklib not installed,
    the download failing, a corrupt cache — because callers act on all of them
    identically: they decline to judge. Distinguishing them here would invite a
    caller to treat one of them as "fine".
    """
    local = _local_build("ncbitaxon")
    if local is not None:
        return local
    try:
        # oaklib ships no py.typed marker; same ignore as the call sites this
        # replaced.
        from oaklib import get_adapter  # type: ignore[import-untyped]

        return get_adapter(NCBITAXON_SELECTOR)
    except Exception:
        return None


def ncbitaxon_available() -> bool:
    """Can a taxonomy lookup actually be made right now?

    The one question `tests/conftest.py` asks before skipping a test whose
    subject is the *result* of a lookup. Cheap to re-ask: the adapter behind it
    is cached, so this is a dictionary hit after the first call.
    """
    return ncbitaxon_adapter() is not None
