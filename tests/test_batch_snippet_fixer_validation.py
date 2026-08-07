"""A validation step reported "no issues" because it never ran (#410).

`batch_snippet_fixer.validate_file` shelled out to
`poetry run python scripts/curate_evidence_with_pdfs.py`. Three things were
wrong at once, and together they were silent:

* that script imports `communitymech.literature_enhanced`, which has never
  existed in any commit, so it cannot start;
* `poetry` is not this repo's runner — it uses `uv`;
* `cwd` was `yaml_path.parent.parent`, i.e. `kb/`, not the repo root.

`returncode` was never checked. Reproduced before the fix: the subprocess
exited **2**, stdout and stderr carried no `ERROR: N` for the regex to match,
and the function returned `{"total": 0, "errors": 0, "warnings": 0}` — which
its caller reads as *validated, clean*.

That is the defect class this repo keeps finding: not a crash, but a check that
reports success because it did nothing. The distinction these tests defend is
between **"clean"** and **"could not tell"**, which the old code could not
express — `0` meant both.

It now calls `linkml-reference-validator`, the tool behind
`just validate-references`, which does check snippets against
`references_cache/` (#466 established that it genuinely validates, despite its
"Total checks" line counting issues rather than checks).
"""

from __future__ import annotations

import ast
import importlib.util
import pathlib
import subprocess
import sys

import pytest
import yaml

REPO = pathlib.Path(__file__).parent.parent
CLEAN_RECORD = (
    REPO / "kb/communities/Geobacter_Clostridium_Interspecies_Electron_Transfer_Coculture.yaml"
)


@pytest.fixture(scope="module")
def fixer():
    spec = importlib.util.spec_from_file_location(
        "batch_snippet_fixer", REPO / "scripts/batch_snippet_fixer.py"
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules["batch_snippet_fixer"] = module
    spec.loader.exec_module(module)
    return module


def test_a_file_that_cannot_be_validated_is_not_reported_as_clean(fixer, tmp_path):
    """The whole point. `0` must mean clean, never "the validator never ran".

    A missing path is the cheapest way to make validation impossible without
    depending on the network or the cache.
    """
    result = fixer.validate_file(tmp_path / "does_not_exist.yaml")
    assert result["total"] == -1, (
        f"a file that could not be validated was reported as {result}, which a "
        f"caller reads as clean (#410)"
    )


def test_the_validator_it_calls_can_actually_start(fixer):
    """Guard against the original failure recurring in a new form.

    The old target could not be imported at all, so `--help` failed. If the
    replacement ever becomes unrunnable, this fails immediately rather than at
    the next batch run.
    """
    result = subprocess.run(
        ["uv", "run", "linkml-reference-validator", "validate", "data", "--help"],
        capture_output=True,
        text=True,
        cwd=REPO,
        timeout=600,
    )
    assert result.returncode == 0, result.stderr[-400:]


def _known_broken() -> set[str]:
    """The five scripts `tests/test_scripts_import.py` records as unrunnable."""
    source = (REPO / "tests/test_scripts_import.py").read_text()
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == "_KNOWN_BROKEN" for target in node.targets
        ):
            return {
                element.value
                for element in ast.walk(node.value)
                if isinstance(element, ast.Constant) and isinstance(element.value, str)
            }
    raise AssertionError("_KNOWN_BROKEN is gone from tests/test_scripts_import.py")


def _strings_in(node: ast.AST) -> list[str]:
    """Every string literal reachable inside a call, f-strings included."""
    found = []
    for child in ast.walk(node):
        if isinstance(child, ast.Constant) and isinstance(child.value, str):
            found.append(child.value)
    return found


def test_no_working_script_points_at_a_script_that_cannot_run():
    """Four working tools told the user to run the broken one.

    `batch_snippet_fixer` actually invoked it; three others printed it as the
    next step. A dead pointer in a working tool is how a curator discovers the
    breakage, which is the worst place to discover it.
    """
    # Read from the same list `test_scripts_import` maintains, rather than a
    # second copy: two hand-kept lists drift, and the first version of this test
    # named three of the five, so a pointer at `test_pdf_fetching` or
    # `extract_evidence_snippets` sailed through (#487 review).
    dead = {name.removesuffix(".py") for name in _known_broken()}
    assert len(dead) >= 5, f"the known-broken list has shrunk unexpectedly: {sorted(dead)}"
    offenders = []
    for path in sorted((REPO / "scripts").glob("*.py")):
        if path.stem in dead:
            continue  # the dead scripts may of course name themselves
        tree = ast.parse(path.read_text())
        # Strings that are *executed* — printed, or passed to subprocess — not
        # every string in the file. A raw-text scan flagged this module's own
        # docstring, which exists to explain the historical bug: it cannot tell
        # a live instruction from prose documenting its removal, the same trap
        # as grepping a curation note for the id it retired.
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            func = node.func
            name = getattr(func, "id", None) or getattr(func, "attr", None)
            # `system` and `write` too: os.system and sys.stdout.write are the
            # shapes the first version missed.
            if name not in (
                "print",
                "run",
                "Popen",
                "check_output",
                "call",
                "system",
                "write",
                "info",
                "warning",
                "error",
            ):
                continue
            for text in _strings_in(node):
                if any(script in text for script in dead):
                    offenders.append(f"{path.name}: {text.strip()[:90]}")
    assert offenders == [], (
        "these working scripts still tell the user to run a script that cannot "
        "start (#410):\n" + "\n".join(offenders)
    )


@pytest.mark.e2e
def test_a_clean_record_is_reported_clean_and_a_broken_one_is_not(fixer, tmp_path):
    """The check must discriminate, or `-1` everywhere would pass the tests above.

    Marked `e2e`, which `pyproject.toml`'s `addopts = "-m 'not e2e'"` deselects
    by default. Two reasons, both from the #487 review: `slow` is not a
    registered marker here, so it only produced a warning and deselected
    nothing; and this runs `linkml-reference-validator`, which #417 deliberately
    keeps out of `just qc`. It resolves against the committed cache today, but
    that is a property of which references this record happens to use, not a
    guarantee — an uncached one would reach NCBI from inside the test suite.

    Run it deliberately: `uv run pytest -m e2e tests/test_batch_snippet_fixer_validation.py`.
    """
    assert fixer.validate_file(CLEAN_RECORD)["total"] == 0

    document = yaml.safe_load(CLEAN_RECORD.read_text())
    document["taxonomy"][0]["evidence"][0][
        "snippet"
    ] = "ZZQQ this sentence appears in no publication whatsoever XKCD"
    broken = tmp_path / "broken.yaml"
    broken.write_text(yaml.safe_dump(document, sort_keys=False, allow_unicode=True, width=4096))

    assert (
        fixer.validate_file(broken)["total"] >= 1
    ), "a snippet that appears in no publication was reported as clean"
