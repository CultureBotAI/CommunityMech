"""One adapter, so "is NCBITaxon available?" has one answer (#704).

`ncbi_domain` and `shared_taxon_ids` each built their own OAK adapter from the
same selector, with the same `except Exception: return None`. Nothing was wrong
with the code. What was wrong is what the duplication did to a *measurement*.

When `bbop-sqlite` began answering 403, I gated the tests that fail when
`ncbi_domain._adapter()` returns None -- measured, not guessed -- and shipped.
CI then failed on twelve more, because a probe pointed at one copy is blind to
every caller of the other. The two copies always agreed in practice, so the
error was invisible in behaviour and only showed up as a wrong count.

So the tests here are about identity rather than reuse, and the sharp one is
`test_the_two_validators_ask_the_same_object`. `is` is the assertion that
matters: two functions that merely behave alike would let the same mistake
happen again.
"""

from __future__ import annotations

import os
import pathlib
import subprocess
import sys

import pytest

from communitymech import ontology_adapters
from communitymech.validators import ncbi_domain, shared_taxon_ids

REPO = pathlib.Path(__file__).parent.parent
SRC = REPO / "src" / "communitymech"

# Test modules whose tests are gated on the taxonomy database being reachable.
#
# Pinned rather than discovered by scanning for `requires_ncbi_adapter`, and the
# direction of the failure is the reason. A scan would take its coverage FROM
# the thing it is checking: delete the last fixture use in a module -- a rename,
# a refactor, `ruff --fix` on an import -- and that module silently leaves the
# set, the guard goes green, and nothing was checked. That is #700's shape, one
# level up. A pinned list can only go stale in the safe direction, and
# `test_every_gated_module_is_covered_here` closes that direction too.
GATED_MODULES = (
    "tests/test_gtdb_coherence_validator.py",
    "tests/test_ncbi_domain_scope.py",
    "tests/test_prokaryotic_lineage.py",
    "tests/test_shared_taxon_ids.py",
)


def test_the_two_validators_ask_the_same_object():
    """Both validators resolve `_adapter` to the one shared accessor.

    Identity, not equivalence. Two separately-defined functions that happen to
    behave the same way are exactly the state this repository was already in,
    and it read as correct right up until a count came out wrong.
    """
    assert ncbi_domain._adapter is ontology_adapters.ncbitaxon_adapter
    assert shared_taxon_ids._adapter is ontology_adapters.ncbitaxon_adapter


def test_the_selector_appears_once_in_the_package():
    """`sqlite:obo:ncbitaxon` is written down in exactly one place.

    No exemption list, deliberately. The guard names the NCBITaxon selector
    literal, so the ENVO and ChEBI adapters in `cross_repo_environment.py` are
    outside it by what they *are* -- a different selector, built from a local
    path -- rather than by being excused for containing some token (#700).
    """
    hits = sorted(
        path.relative_to(REPO)
        for path in SRC.rglob("*.py")
        if ontology_adapters.NCBITAXON_SELECTOR in path.read_text(encoding="utf-8")
    )
    assert hits == [pathlib.Path("src/communitymech/ontology_adapters.py")], hits


def test_every_gated_module_is_covered_here():
    """A module that gates on the adapter must be in `GATED_MODULES`.

    The other half of pinning the list. Pinning stops coverage from evaporating
    when a fixture use disappears; this stops the list from going stale when a
    new module starts depending on the database.
    """
    using = sorted(
        str(path.relative_to(REPO))
        for path in sorted((REPO / "tests").glob("test_*.py"))
        if "requires_ncbi_adapter" in path.read_text(encoding="utf-8")
        and path.name != pathlib.Path(__file__).name
    )
    assert using == sorted(GATED_MODULES), using


def _outage_env(tmp_path: pathlib.Path) -> dict[str, str]:
    """An environment in which NCBITaxon cannot be reached, without a network.

    Two independent things, because either alone is unreliable. `PYSTOW_HOME`
    moves OAK's download cache to an empty directory, so an already-downloaded
    `ncbitaxon.db` cannot satisfy the request -- this machine has one, CI
    increasingly does too. The unroutable proxy then makes the re-download fail
    in milliseconds instead of pulling 13 GB the day the upstream 403 is fixed.
    """
    env = dict(os.environ)
    env["PYSTOW_HOME"] = str(tmp_path / "pystow")
    env["HTTP_PROXY"] = env["HTTPS_PROXY"] = "http://127.0.0.1:1"
    env.pop("NO_PROXY", None)
    env.pop("no_proxy", None)
    return env


def test_the_gated_modules_survive_an_unavailable_ontology(tmp_path):
    """With NCBITaxon unreachable, the gated modules skip -- they do not fail.

    This is the regression the whole change exists for: an ungated test added
    to either module reds the suite for a reason unrelated to the change under
    test, which is how a real failure gets waved through as "the flaky one".

    It is checked in a subprocess because `requires_ncbi_adapter` consults the
    process-wide cached adapter, and because two of the gated tests shell out to
    `validate_strict` -- an in-process monkeypatch would not reach those.
    """
    env = _outage_env(tmp_path)

    # Prove the simulation took before trusting anything it produces. If OAK
    # still finds a database here, every assertion below would pass for the
    # ordinary reason and certify nothing -- a false green of exactly the kind
    # CLAUDE.md's first mutation rule is about.
    armed = subprocess.run(
        [
            sys.executable,
            "-c",
            "from communitymech.ontology_adapters import ncbitaxon_available;"
            "print(ncbitaxon_available())",
        ],
        cwd=REPO,
        env=env,
        capture_output=True,
        text=True,
    )
    if armed.stdout.strip() != "False":
        pytest.skip(
            "could not make NCBITaxon unreachable in a subprocess "
            f"(availability reported {armed.stdout.strip()!r}), so this proves "
            "nothing about the outage path"
        )

    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", "-p", "no:randomly", *GATED_MODULES],
        cwd=REPO,
        env=env,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout[-4000:] + result.stderr[-2000:]

    # ...and that they skipped rather than all quietly passing, which would mean
    # the gating was never exercised.
    assert " skipped" in result.stdout, result.stdout[-2000:]


def _run_copy_of(module: str, tmp_path: pathlib.Path, mutate=None) -> subprocess.CompletedProcess:
    """Run a copy of a gated test module with NCBITaxon unreachable.

    `tests/conftest.py` is copied next to it, and that detail is the whole
    reason this helper exists. pytest loads a conftest from the test file's own
    directory; a copy dropped in `tmp_path` alone gets none, so every test
    requesting `requires_ncbi_adapter` errors with "fixture not found" -- and a
    mutation check built on that reds whether or not the mutation did anything.
    The first version of the test below did exactly that and passed, which is
    the #696 failure mode reproduced inside the file documenting it.
    """
    workspace = tmp_path / module
    workspace.mkdir(parents=True)
    (workspace / "conftest.py").write_text(
        (REPO / "tests" / "conftest.py").read_text(encoding="utf-8"), encoding="utf-8"
    )
    source = (REPO / "tests" / module).read_text(encoding="utf-8")
    if mutate is not None:
        source = mutate(source)
    copied = workspace / module
    copied.write_text(source, encoding="utf-8")

    env = _outage_env(workspace)
    env["PYTHONPATH"] = str(REPO / "src")
    return subprocess.run(
        [sys.executable, "-m", "pytest", "-q", "-p", "no:randomly", str(copied)],
        cwd=REPO,
        env=env,
        capture_output=True,
        text=True,
    )


def test_the_check_can_actually_fail(tmp_path):
    """Removing one test's gate reds the outage run -- and nothing else does.

    Two arms, because one proves nothing. The control runs an UNMUTATED copy
    through the identical harness: if that is red, the harness is the cause and
    a red from the mutated arm means nothing. Only with the control green does
    the mutated arm's red belong to the mutation.
    """
    module = "test_prokaryotic_lineage.py"
    target = "def test_the_committed_kb_is_clean(requires_ncbi_adapter):"
    assert (REPO / "tests" / module).read_text(encoding="utf-8").count(
        target
    ) == 1, "the mutation target moved; re-point it rather than deleting this test"

    control = _run_copy_of(module, tmp_path / "control")
    if "skipped" not in control.stdout:
        pytest.skip(
            "the control run skipped nothing, so nothing below would mean "
            "anything. Either the ontology was still reachable or the harness "
            "itself is broken -- the tail says which, and a fixture-not-found "
            f"error means the conftest copy above stopped working:\n"
            f"{control.stdout[-1200:]}"
        )
    assert control.returncode == 0, (
        "the control arm is red, so this test cannot attribute anything to the "
        f"mutation:\n{control.stdout[-3000:]}"
    )

    mutated = _run_copy_of(
        module,
        tmp_path / "mutated",
        mutate=lambda text: text.replace(target, "def test_the_committed_kb_is_clean():"),
    )
    assert mutated.returncode != 0, (
        "an ungated test survived an unavailable ontology, so the outage guard "
        f"above cannot detect one:\n{mutated.stdout[-3000:]}"
    )
    assert "test_the_committed_kb_is_clean" in mutated.stdout, mutated.stdout[-3000:]
