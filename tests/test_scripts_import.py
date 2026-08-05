"""Every script must at least import (#410).

`scripts/` has no test coverage at all. Six scripts have imported a module that
does not exist — `communitymech.literature_enhanced` — since the repo's first
commit, so they have never run, and nothing noticed for months. `just lint` did
not reach `scripts/` until #381, and lint would not have caught this anyway: the
import is syntactically fine.

Importing is a low bar deliberately. These are scripts with side effects and
network calls; running them is not something a test suite should do. But an
import failure means the file cannot execute at all, which is worth exactly one
cheap check.

Scripts that execute work at import time are excluded by name rather than by
pattern, because "does this module do something on import" is not decidable from
the outside and a wrong guess here writes into the repo.
"""

from __future__ import annotations

import ast
import re
import subprocess
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).parent.parent
SCRIPTS = REPO / "scripts"

# These run their work at import — no `if __name__ == "__main__"` guard — so
# importing them would rewrite KB files. They are checked for parse only.
_EXECUTES_ON_IMPORT = {
    "chebi_fix_apply.py",
    "chebi_label_audit.py",
    "term_fix_apply.py",
    "term_label_audit.py",
}

# Broken since the repo's first commit (7c658e6): all six import
# `communitymech.literature_enhanced`, which has never existed in any commit on
# any branch. Listed rather than skipped silently, so the count is visible and
# shrinks as #410 is resolved — deleting them or porting them to
# `LiteratureFetcher` is a curation decision, not a test's to make.
_KNOWN_BROKEN = {
    "curate_evidence_with_pdfs.py",
    "extract_evidence_snippets.py",
    "fix_invalid_snippets.py",
    "quick_literature_review.py",
    "review_literature.py",
    "test_pdf_fetching.py",
}


# `python scripts/foo.py` puts `scripts/` on sys.path, which is how the sibling
# imports between these files resolve (`from scout_communities import ...`).
# Loading the file without that made four scripts look broken when they are not —
# the probe has to match how the thing is actually invoked.
_PROBE = (
    "import sys, importlib.util; "
    "sys.path.insert(0, {scripts!r}); "
    "spec = importlib.util.spec_from_file_location('_probe', {path!r}); "
    "mod = importlib.util.module_from_spec(spec); "
    "spec.loader.exec_module(mod)"
)


def _is_first_party(module: str) -> bool:
    """Is this a module the repo is supposed to provide?

    `communitymech.*` and any sibling script name. Those can never be fixed by
    installing something, so their absence is a defect rather than an
    environment difference.
    """
    root = module.split(".")[0]
    return root == "communitymech" or (SCRIPTS / f"{root}.py").exists()


def _scripts() -> list[Path]:
    return sorted(SCRIPTS.glob("*.py"))


def _importable() -> list[Path]:
    return [
        path
        for path in _scripts()
        if path.name not in _EXECUTES_ON_IMPORT and path.name not in _KNOWN_BROKEN
    ]


def test_the_sweep_sees_the_scripts():
    """Guards everything below: an empty glob would pass vacuously."""
    assert len(_scripts()) > 50, f"expected the scripts tree, found {len(_scripts())}"


@pytest.mark.parametrize("script", _importable(), ids=lambda p: p.name)
def test_a_script_imports(script: Path):
    """A script that cannot import cannot run, whatever else is true of it."""
    result = subprocess.run(
        [
            sys.executable,
            "-c",
            _PROBE.format(path=str(script), scripts=str(SCRIPTS)),
        ],
        capture_output=True,
        text=True,
        cwd=REPO,
        timeout=120,
    )
    if result.returncode == 0:
        return

    # Both streams: three of these print their install hint to stdout and exit,
    # so a stderr-only check reported them as failing with an empty message.
    output = (result.stdout + result.stderr).strip()
    missing = re.search(r"No module named '([^']+)'", output)
    # A missing *third-party* package is an install gap, not a defect — five
    # scripts need `duckdb`, which is not in the default sync, and three of them
    # exit with an install hint on purpose. A missing *first-party* module is a
    # bug: it can never be installed, which is exactly #410.
    if missing and not _is_first_party(missing.group(1)):
        pytest.skip(f"{script.name} needs {missing.group(1)}, which is not installed")
    if "not available. Install with" in output:
        pytest.skip(f"{script.name} exits deliberately without duckdb")

    tail = output.splitlines()[-3:] or ["(no output)"]
    pytest.fail(f"{script.name} does not import:\n  " + "\n  ".join(tail))


@pytest.mark.parametrize("script", _scripts(), ids=lambda p: p.name)
def test_a_script_parses(script: Path):
    """Even the excluded ones must be syntactically valid."""
    ast.parse(script.read_text())


def test_the_known_broken_list_is_still_accurate():
    """A name that starts importing must leave the list, or the list rots.

    Without this, fixing one of the six would leave it permanently exempt from
    the check above — the failure mode of every allowlist.
    """
    fixed = []
    for name in sorted(_KNOWN_BROKEN):
        path = SCRIPTS / name
        if not path.exists():
            continue
        result = subprocess.run(
            [
                sys.executable,
                "-c",
                _PROBE.format(path=str(path), scripts=str(SCRIPTS)),
            ],
            capture_output=True,
            text=True,
            cwd=REPO,
            timeout=120,
        )
        if result.returncode == 0:
            fixed.append(name)
    assert not fixed, f"these now import and should be removed from _KNOWN_BROKEN: {fixed} (#410)"


def test_the_known_broken_all_share_one_cause():
    """The list is one bug, not a bucket.

    If a script joins it for a different reason, that reason wants its own issue
    rather than being absorbed into #410's count.
    """
    for name in sorted(_KNOWN_BROKEN):
        path = SCRIPTS / name
        if not path.exists():
            continue
        imports = {
            node.module
            for node in ast.walk(ast.parse(path.read_text()))
            if isinstance(node, ast.ImportFrom) and node.module
        }
        assert any(
            "literature_enhanced" in module for module in imports
        ), f"{name} is in _KNOWN_BROKEN but does not import literature_enhanced"
