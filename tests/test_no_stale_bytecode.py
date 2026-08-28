"""The two conditions that make a stale `scripts/` module impossible (#693).

`tests/conftest.py` explains why this matters; this file is the part that fails
if either condition quietly stops holding. Both are needed: not writing new
bytecode does nothing about a `.pyc` from an earlier session, and sweeping the
directory does nothing if this session writes a fresh one a moment later.

A comment in conftest asserting "we set dont_write_bytecode" is not evidence.
`pyproject.toml` gaining a `-p no:cacheprovider`, someone flipping the flag back
inside a fixture, or a future conftest ordering change would all leave the
comment true and the guarantee gone.
"""

from __future__ import annotations

import importlib.util
import pathlib
import sys

from conftest import IMPORTED_NORMALLY, LOADED_BY_PATH, _pycache_dirs, guarded_roots

REPO = pathlib.Path(__file__).parent.parent


def test_the_session_does_not_write_bytecode():
    """Condition 1, read from the interpreter rather than from the source."""
    assert sys.dont_write_bytecode is True, (
        "sys.dont_write_bytecode is off, so loading a scripts/ module by path "
        "writes a .pyc validated on (mtime, size) — and a same-length edit in "
        "the same second is invisible to that check (#693)"
    )


def test_no_bytecode_cache_survives_under_a_guarded_root():
    """Condition 2, after a load has actually happened.

    Parametrising over the *existing* caches would be self-defeating: conftest
    sweeps them at session start, so the list would be empty at collection time
    and the check would pass by having nothing to look at. It asks the question
    of the guarded ROOTS instead, and triggers a real load first so the
    mechanism is under test even when this module runs before any other.
    """
    script = REPO / "scripts" / "cache_fulltext.py"
    assert script.is_file(), "the probe script is gone; pick another scripts/ module"
    spec = importlib.util.spec_from_file_location("_stale_probe", script)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # ...and an ordinary import of the package, which is the other exposure.
    import communitymech.paths  # noqa: F401

    surviving = sorted(str(d.relative_to(REPO)) for d in _pycache_dirs())
    assert surviving == [], (
        "these bytecode caches exist after loading and importing from a guarded "
        "root:\n"
        + "\n".join(f"  {d}" for d in surviving)
        + "\n\nA .pyc there can be served in place of the file under test when "
        "a source edit changes neither mtime nor size (#693)."
    )


def test_the_directories_being_guarded_are_the_ones_tests_load_from():
    """Guard: an empty or wrong LOADED_BY_PATH makes both checks vacuous."""
    assert LOADED_BY_PATH, "no directories are guarded; the checks above prove nothing"
    loaders = [
        path.name
        for path in sorted((REPO / "tests").glob("test_*.py"))
        if "spec_from_file_location" in path.read_text(encoding="utf-8")
    ]
    assert len(loaders) >= 20, f"only {len(loaders)} modules load by path; the scan broke"

    assert IMPORTED_NORMALLY, "the imported package is unguarded"
    for root in guarded_roots():
        assert root.is_dir(), f"{root} is guarded but does not exist"

    for name in LOADED_BY_PATH:
        assert not (REPO / name / "__init__.py").exists(), (
            f"{name}/ has become a package, so tests can import it normally "
            f"instead of by path. That removes the loader this guard was "
            f"written for -- though not the (mtime, size) staleness itself, "
            f"which is why the package tree is guarded too (#693)"
        )
