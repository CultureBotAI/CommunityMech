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
import importlib.util
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

# All import `communitymech.literature_enhanced`, which has never existed in any
# commit on any branch — verified over all 498 commits. They were added in
# `7c658e6` (the 7th commit, 2026-02-18; the repo's first is `79f5196`).
#
# Not a curation call in general: #88 already ported the same import in two other
# scripts, and `fix_invalid_snippets.py` followed that recipe here because it
# passed `download_pdf=False` throughout, so nothing was lost. These five pass a
# *variable* for PDF fetching, or call `fetch_pdf_url`, and `LiteratureFetcher`
# has no PDF surface at all — porting them means deciding whether to drop a
# capability their CLI flags advertise. That decision is #410, which stays open.
_KNOWN_BROKEN = {
    "curate_evidence_with_pdfs.py",
    "extract_evidence_snippets.py",
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


def _declared_packages() -> frozenset[str]:
    """Distribution names mentioned anywhere in the dependency files.

    Coarse on purpose — this only has to tell "a real package nobody installed"
    from "a name that exists nowhere".
    """
    text = (REPO / "pyproject.toml").read_text()
    lock = REPO / "uv.lock"
    if lock.exists():
        text += lock.read_text()
    return frozenset(re.findall(r"[A-Za-z0-9_.-]+", text))


_DECLARED_PACKAGES = _declared_packages()


def _is_installed(module: str) -> bool:
    return importlib.util.find_spec(module) is not None


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


def test_the_sweep_actually_tests_most_scripts():
    """Counting files is not enough — the *tested* set must not collapse.

    pytest turns an empty parametrize list into a skip, not a failure, so
    growing an exclusion list to cover everything would leave this file green
    with nothing checked (#413 review).
    """
    assert len(_scripts()) > 50, f"expected the scripts tree, found {len(_scripts())}"
    assert len(_importable()) >= 55, (
        f"only {len(_importable())} of {len(_scripts())} scripts are import-tested; "
        f"an exclusion list has grown"
    )


@pytest.mark.parametrize("name", sorted(_EXECUTES_ON_IMPORT))
def test_an_excluded_script_really_executes_on_import(name):
    """The other allowlist, which had no hygiene test at all.

    A name lands here by claiming it does work at module scope. If that stops
    being true it should rejoin the import check rather than stay exempt.
    """
    tree = ast.parse((SCRIPTS / name).read_text())
    work = [
        node
        for node in tree.body
        if not isinstance(
            node,
            (ast.Import, ast.ImportFrom, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef),
        )
        and not (isinstance(node, ast.Assign | ast.AnnAssign | ast.Expr))
    ]
    calls = [
        node
        for node in tree.body
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call)
    ]
    assert work or calls, (
        f"{name} has no module-level work; drop it from _EXECUTES_ON_IMPORT so it "
        f"is import-tested like everything else"
    )


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
    if missing:
        module = missing.group(1)
        if _is_first_party(module):
            pytest.fail(f"{script.name} imports a module this repo does not provide: {module}")
        if module not in _DECLARED_PACKAGES:
            # A name that appears in no dependency file can never be installed,
            # so it is a typo or a rename, not an environment difference —
            # `import reqeusts` used to skip forever (#413 review).
            pytest.fail(f"{script.name} imports {module!r}, which is in no dependency file")
        pytest.skip(f"{script.name} needs {module}, which is not installed here")

    # Some scripts catch the ImportError themselves and exit with an install
    # hint, so there is no "No module named" to match. Key off the package they
    # name and verify it really is absent — matching the phrase alone was too
    # loose (`compare_ncbi_gtdb_taxonomy.py` prints it as a *non-fatal* warning,
    # which would have relabelled a later first-party failure as an install gap)
    # and requiring the script to mention the package was too strict
    # (`gtdb_demo.py` inherits it from a sibling import) — #413 review.
    hint = re.search(r"([A-Za-z0-9_]+) not available\. Install with", output)
    if hint and not _is_first_party(hint.group(1)) and not _is_installed(hint.group(1)):
        pytest.skip(f"{script.name} exits deliberately without {hint.group(1)}")

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


def test_every_known_broken_script_says_so_in_its_docstring():
    """A reader opening the file should not have to run it to find out.

    `_KNOWN_BROKEN` records the breakage for the *suite*; it is invisible to
    someone who opens `curate_evidence_with_pdfs.py` and sees 586 lines of
    plausible code. Each carries a docstring warning naming the phantom module,
    why porting is not an import swap, and what to use instead (#410).

    Asserted against `_KNOWN_BROKEN` rather than a fixed list, so a script
    joining it later cannot arrive undocumented.
    """
    undocumented = []
    for name in sorted(_KNOWN_BROKEN):
        path = SCRIPTS / name
        if not path.exists():
            continue
        docstring = ast.get_docstring(ast.parse(path.read_text())) or ""
        if "has never run" not in docstring or "literature_enhanced" not in docstring:
            undocumented.append(name)
    assert not undocumented, (
        "these are in _KNOWN_BROKEN but their docstrings do not say so — a "
        f"reader would take them for working tools (#410): {undocumented}"
    )


def test_the_replacement_named_in_those_docstrings_exists():
    """The pointer has to stay true, or it is worse than no pointer."""
    # Not `validators/reference_validator.py` — that was deleted in 4dd299a
    # when the custom validators were replaced by the official LinkML ones.
    # Writing this test is what caught the docstrings, and CLAUDE.md, still
    # naming it.
    assert (REPO / "conf/reference_validator.yaml").exists()
    assert (REPO / "src/communitymech/literature.py").exists()

    justfile = (REPO / "justfile").read_text()
    assert "validate-references FILE:" in justfile
    assert "validate-references-all:" in justfile
    assert "linkml-reference-validator" in justfile

    fetcher = (REPO / "src/communitymech/literature.py").read_text()
    assert "def fetch_paper(" in fetcher, (
        "the docstrings contrast the phantom fetch_paper with this one; if it is "
        "gone or renamed, they now describe nothing"
    )
