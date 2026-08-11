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

# Empty, and kept rather than deleted: #410 was about five scripts that imported
# `communitymech.literature_enhanced`, a module that never existed in any of the
# repo's 498 commits. They were removed rather than ported, because porting meant
# deciding whether to keep a capability their CLI flags advertised and the code
# never had — a 6-tier PDF cascade with "fallback mirrors". Answering "no": the
# OA full-text need is served by `scripts/cache_fulltext.py`, which works and
# which the #183 sweep used to cache 64 of 125 references.
#
# The name stays so the tests below keep their shape if a script ever breaks
# this way again. `test_no_script_imports_a_module_that_does_not_exist` is the
# real guard now, and unlike this list it cannot go stale.
_KNOWN_BROKEN: set[str] = set()


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


def test_no_script_imports_a_module_that_does_not_exist():
    """The invariant #410 actually wanted, in place of a list of exceptions.

    The old guard was `_KNOWN_BROKEN`, five names plus three tests keeping the
    list honest. That records breakage; it does not prevent it, and a sixth
    script importing a sixth phantom module would simply have been added to it.

    This resolves every `from communitymech.X import ...` in `scripts/` against
    the installed package. It is deliberately narrow — only this package, not
    third-party imports, which fail for environment reasons a test should not
    adjudicate.
    """
    import importlib.util

    offenders = []
    for path in sorted(SCRIPTS.glob("*.py")):
        for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
            if not isinstance(node, ast.ImportFrom) or not node.module:
                continue
            if not node.module.startswith("communitymech"):
                continue
            try:
                found = importlib.util.find_spec(node.module)
            except (ImportError, ValueError):
                found = None
            if found is None:
                offenders.append(f"{path.name}:{node.lineno} imports {node.module}")
    assert offenders == [], (
        "these scripts import a `communitymech` module that cannot be "
        "resolved, so they fail before `--help` (#410):\n" + "\n".join(offenders)
    )


def test_that_guard_can_actually_fail(tmp_path):
    """Mutation check, in-tree: the sweep above must reject a phantom import.

    Written because the guard it replaces was a list — and a list-driven test
    passes cleanly once the list is empty, which is exactly the state this file
    is now in. Without this, `test_no_script_imports_a_module_that_does_not_exist`
    could resolve nothing at all and still report success.
    """
    import importlib.util

    assert importlib.util.find_spec("communitymech.literature") is not None
    try:
        missing = importlib.util.find_spec("communitymech.literature_enhanced")
    except (ImportError, ValueError):
        missing = None
    assert missing is None, (
        "`communitymech.literature_enhanced` now resolves. If it was genuinely "
        "implemented, #410 can be revisited; if something is shadowing the "
        "package, the guard above is not testing what it claims"
    )


def test_the_removed_scripts_are_gone_and_stay_gone():
    """They are superseded, and a reintroduction should be deliberate.

    Each had a working replacement by the time it was removed: OA full text via
    `cache_fulltext.py`, snippet checking via `just validate-references`. A file
    reappearing under one of these names is most likely a revert that did not
    mean to bring back a script that cannot start.
    """
    removed = {
        "curate_evidence_with_pdfs.py",
        "extract_evidence_snippets.py",
        "quick_literature_review.py",
        "review_literature.py",
        "test_pdf_fetching.py",
    }
    back = sorted(name for name in removed if (SCRIPTS / name).exists())
    assert back == [], (
        f"{back} were removed in #410 as unrunnable and superseded. If one is "
        "genuinely wanted again it needs a working literature backend first — "
        "see scripts/cache_fulltext.py."
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
