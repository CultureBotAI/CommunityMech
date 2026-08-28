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

import pytest
from conftest import LOADED_BY_PATH, _pycache_dirs

REPO = pathlib.Path(__file__).parent.parent


def test_the_session_does_not_write_bytecode():
    """Condition 1, read from the interpreter rather than from the source."""
    assert sys.dont_write_bytecode is True, (
        "sys.dont_write_bytecode is off, so loading a scripts/ module by path "
        "writes a .pyc validated on (mtime, size) — and a same-length edit in "
        "the same second is invisible to that check (#693)"
    )


@pytest.mark.parametrize("directory", _pycache_dirs(), ids=lambda p: p.parent.name)
def test_no_bytecode_cache_survives_for_a_path_loaded_directory(directory: pathlib.Path):
    """Condition 2, after the loads have happened.

    Ordering is not assumed: the assertion is re-derived here, and the load
    below puts the mechanism under test even when this module runs first.
    """
    script = REPO / directory.parent.name / "cache_fulltext.py"
    if script.is_file():
        spec = importlib.util.spec_from_file_location("_stale_probe", script)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

    assert not directory.exists(), (
        f"{directory.relative_to(REPO)} exists after loading a module from it. "
        f"A .pyc there can be served in place of the file under test when a "
        f"source edit changes neither mtime nor size (#693)."
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

    for name in LOADED_BY_PATH:
        assert (REPO / name).is_dir(), f"{name}/ is guarded but does not exist"
        assert not (REPO / name / "__init__.py").exists(), (
            f"{name}/ has become a package, so tests can import it normally and "
            f"this guard may be describing a problem that no longer exists (#693)"
        )
