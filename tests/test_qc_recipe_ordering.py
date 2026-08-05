"""`just qc` must reach `lint` and `test` (#417).

`just` stops at the first failing dependency. `qc` listed
`validate-references-all` eighth of ten, and that recipe **cannot pass**: it
needs the network, and it reports ~320 errors on a clean `main` for reasons
already tracked (#259, no DOI full-text cache path; #347, snippets that
paraphrase rather than quote).

So the command named "check everything" stopped there every time and never ran
`lint` or `test` — the only two checks CI actually enforces. It failed loudly
enough to look like it had done its job, which is the worst way for a check to
be broken.

These tests read the recipe text rather than running it. Running `qc` takes
~15 minutes and needs the kg-microbe checkout; the property worth guarding is a
statement about the dependency list, and that is cheap to read.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

REPO = Path(__file__).parent.parent
JUSTFILE = REPO / "justfile"

# Recipes that cannot pass offline or do not pass on `main` today. Keeping one
# of these ahead of a gate hides the gate.
_CANNOT_PASS = ("validate-references-all",)

# What CI enforces. These must be reachable in a local `qc`.
_CI_GATES = ("lint", "test")


def _recipe_dependencies(name: str) -> list[str]:
    """The dependency list of `name`, in order.

    A just recipe header is `name: dep1 dep2` (or `name param="x": deps`), so
    the dependencies are whatever follows the first unquoted colon on the line
    that starts the recipe.
    """
    for line in JUSTFILE.read_text().splitlines():
        match = re.match(rf"^{re.escape(name)}(?:\s+[^:]*)?:(?P<deps>.*)$", line)
        if match:
            return match.group("deps").split()
    raise AssertionError(f"no `{name}` recipe in the justfile")


def test_the_helper_finds_a_real_recipe():
    """Guards every assertion below: a helper that found nothing would pass them."""
    dependencies = _recipe_dependencies("qc")

    assert len(dependencies) > 5, f"`qc` parsed as {dependencies}, which is not its dependency list"
    assert "validate-all" in dependencies

    with pytest.raises(AssertionError):
        _recipe_dependencies("no-such-recipe-anywhere")


@pytest.mark.parametrize("gate", _CI_GATES)
def test_qc_runs_the_checks_ci_enforces(gate):
    assert gate in _recipe_dependencies("qc"), (
        f"`just qc` no longer runs `{gate}` — the gate CI enforces. A local QC "
        f"command that skips it reports green on a build that will fail (#417)."
    )


@pytest.mark.parametrize("recipe", _CANNOT_PASS)
def test_qc_does_not_depend_on_a_recipe_that_cannot_pass(recipe):
    """The actual regression: one of these back in `qc` re-breaks it."""
    assert recipe not in _recipe_dependencies("qc"), (
        f"`{recipe}` is back in `qc`. It fails on a clean `main` (#259, #347) and "
        f"needs the network, so `just` stops there and never reaches lint or test "
        f"(#417). Put it in `qc-references` instead."
    )


@pytest.mark.parametrize("gate", _CI_GATES)
def test_the_ci_gates_come_before_the_slow_validators(gate):
    """Ordering, not just membership.

    Being in the list is not enough — `lint` and `test` last would still mean a
    seven-minute validator decides whether they run at all. They are also the
    fastest things in the chain (~40s, ~2min against 5-7min), so failing early
    is free.
    """
    dependencies = _recipe_dependencies("qc")
    slow = [d for d in dependencies if d.startswith("validate-")]
    assert slow, "no validators in `qc`; this test is stale"

    assert dependencies.index(gate) < min(dependencies.index(s) for s in slow), (
        f"`{gate}` runs after {slow[0]} in `qc`; a failure there would stop the "
        f"run before the gate CI enforces (#417)"
    )


def test_the_reference_sweep_is_still_reachable():
    """Removed from `qc`, not from the repo.

    Dropping the check entirely would trade one silent gap for another — the
    point is that it runs deliberately, not that it stops running.
    """
    dependencies = _recipe_dependencies("qc-references")

    assert "validate-references-all" in dependencies
    assert "qc" in dependencies, "`qc-references` should be a superset of `qc`"


def test_the_docs_do_not_promise_qc_checks_references():
    """CLAUDE.md is what a contributor reads before running anything."""
    text = (REPO / "CLAUDE.md").read_text()

    assert "just qc-references" in text, "CLAUDE.md does not mention the reference sweep"
    assert "#417" in text, "CLAUDE.md does not explain why references are out of `qc`"
