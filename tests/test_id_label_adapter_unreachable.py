"""An outage is not a verdict about the KB -- but a typo must not look like one.

While `s3.amazonaws.com/bbop-sqlite` answered 403 for every ontology build, the
checks that consult OAK reacted incompatibly: `linkml-term-validator` passed 328
files vacuously and died on the 329th with a raw `DownloadError` traceback, and
`validate_id_label_correspondence.py` emitted 6250+ `ADAPTER_ERROR` rows.
`label-correspondence` was red on `main` for two days on a condition no PR
caused and none could fix (#708).

`scripts/ontology_preflight.py` asks first, and the recipes decline out loud
rather than report a result they did not earn.

**The danger in that is the whole subject of this module.** A typo'd ontology
name raises the exact same `DownloadError` as a real outage --
`sqlite:obo:not_a_real_ontology_xyz` fails identically to `sqlite:obo:go`, and
S3 answers 403 for a nonexistent key just as it does for a forbidden one, so
neither the exception type nor the HTTP status separates them. Reporting
"unreachable" on the error alone would let one typo in
`conf/id_label_targets.yaml` skip an ontology's checks while the gate reported
clean: #686's failure mode, reintroduced by the fix for #708.

Two independent conditions, and the tests below hold both: the exception type
narrows the candidates, and `PINNED_ONTOLOGY_NAMES` decides. That ordering is
CLAUDE.md's "a guard may narrow, never excuse" (#700).
"""

from __future__ import annotations

import importlib.util
import pathlib
import subprocess

import pytest
import yaml

REPO = pathlib.Path(__file__).parent.parent
SCRIPT = REPO / "scripts" / "ontology_preflight.py"

# Recipes whose checker cannot survive an unreachable ontology, so each must ask
# the preflight first. Pinned rather than discovered: a scan for the preflight's
# name would take its coverage from the very thing it checks, so deleting the
# call would drop the recipe from the set and go green (#700, one level up).
GUARDED_RECIPES = ("validate-products", "validate-terms-all", "validate-terms-taxa")

# What each guarded recipe must still actually INVOKE. A preflight that replaced
# its checker instead of guarding it would otherwise satisfy every assertion
# here and check nothing forever.
RECIPE_CHECKER = {
    "validate-products": "scripts/validate_id_label_correspondence.py",
    "validate-terms-all": "linkml-term-validator",
    "validate-terms-taxa": "linkml-term-validator",
}


def _module():
    """Load the preflight from source.

    `scripts/` is not a package, and a `.pyc` validated on (mtime, size) can
    serve a module that is not the file under test (#693).
    """
    spec = importlib.util.spec_from_file_location("_ontology_preflight_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class _FakeDownloadError(Exception):
    """Stands in for pystow's DownloadError without needing a network."""


@pytest.fixture
def patched(monkeypatch):
    """The preflight with pystow's DownloadError swapped for a local class.

    The production check is `isinstance` against pystow's real type, so the test
    controls that type rather than raising something merely named alike -- which
    is also the property being asserted.
    """
    import pystow.utils

    monkeypatch.setattr(pystow.utils, "DownloadError", _FakeDownloadError)
    return _module()


def _config(tmp_path: pathlib.Path, adapters: dict[str, str]) -> pathlib.Path:
    path = tmp_path / "targets.yaml"
    path.write_text(yaml.safe_dump({"targets": [{"adapters": adapters}]}), encoding="utf-8")
    return path


def _raise(exc):
    def _boom(_selector):
        raise exc

    return _boom


# --------------------------------------------------------------------------
# The pin, which is what authorises anything to be called "unreachable".
# --------------------------------------------------------------------------


def test_the_config_asks_only_for_pinned_ontologies():
    """Every configured selector must be one the preflight may cover.

    The structural half. Runs offline and deterministically, so a typo fails
    here -- loudly, on every machine -- instead of silently becoming a skipped
    ontology at runtime.
    """
    module = _module()
    selectors = module.configured_adapters(REPO / "conf" / "id_label_targets.yaml")
    assert selectors, "no adapters found in the config; this test would prove nothing"

    unpinned = sorted(
        f"{prefix} -> {selector}"
        for prefix, selector in selectors.items()
        if not module.is_pinned_obo_selector(selector)
    )
    assert unpinned == [], (
        "these configured adapters are not in PINNED_ONTOLOGY_NAMES. Either the "
        "name is a typo, or a new ontology needs adding to the pin "
        "deliberately (#708):\n  " + "\n  ".join(unpinned)
    )


# --------------------------------------------------------------------------
# Both directions. Asserting only the failure direction would pass with a
# preflight wired to say "unreachable" forever, which would turn the gates off.
# --------------------------------------------------------------------------


def test_an_unreachable_pinned_ontology_is_reported(tmp_path, monkeypatch, patched):
    """The case the preflight exists for."""
    import oaklib

    monkeypatch.setattr(oaklib, "get_adapter", _raise(_FakeDownloadError("403")))
    assert patched.unreachable_ontologies(_config(tmp_path, {"GO": "sqlite:obo:go"})) == ["GO"]


def test_a_reachable_ontology_is_not_reported(tmp_path, monkeypatch):
    """...and the direction that stops the gates being disabled permanently.

    Hermetic: `get_adapter` is patched to succeed, so this holds on a machine
    with no ontology cache and during the outage itself.
    """
    import oaklib

    monkeypatch.setattr(oaklib, "get_adapter", lambda _sel: object())
    assert _module().unreachable_ontologies(_config(tmp_path, {"GO": "sqlite:obo:go"})) == []


def test_a_typoed_ontology_name_is_not_called_unreachable(tmp_path, monkeypatch, patched):
    """The danger the pin exists for.

    Same exception, unpinned name. If this is ever reported unreachable, one
    typo in the config silently stops an ontology being checked at all.
    """
    import oaklib

    monkeypatch.setattr(oaklib, "get_adapter", _raise(_FakeDownloadError("403")))
    config = _config(tmp_path, {"GO": "sqlite:obo:not_a_real_ontology_xyz"})
    assert patched.unreachable_ontologies(config) == []


def test_a_non_download_failure_is_not_called_unreachable(tmp_path, monkeypatch, patched):
    """A broken local path or corrupt db is a real error, outage or not."""
    import oaklib

    monkeypatch.setattr(oaklib, "get_adapter", _raise(FileNotFoundError("no such file")))
    config = _config(tmp_path, {"GO": "sqlite:obo:go"})
    assert patched.unreachable_ontologies(config) == []


def test_the_exit_code_distinguishes_the_two_outcomes(tmp_path, monkeypatch, patched):
    """3 means "cannot run"; 0 means "go ahead". The recipes branch on this."""
    import oaklib

    monkeypatch.setattr(oaklib, "get_adapter", _raise(_FakeDownloadError("403")))
    assert patched.main(["-c", str(_config(tmp_path, {"GO": "sqlite:obo:go"}))]) == 3

    monkeypatch.setattr(oaklib, "get_adapter", lambda _sel: object())
    assert patched.main(["-c", str(_config(tmp_path, {"GO": "sqlite:obo:go"}))]) == 0


# --------------------------------------------------------------------------
# The wiring.
# --------------------------------------------------------------------------


def _recipe_body(name: str) -> str:
    dump = subprocess.run(
        ["just", "--unstable", "--dump", "--dump-format", "just"],
        capture_output=True,
        text=True,
        cwd=REPO,
        timeout=120,
    )
    text = dump.stdout if dump.returncode == 0 else (REPO / "justfile").read_text(encoding="utf-8")
    body, capturing = [], False
    for line in text.splitlines():
        if line.startswith(f"{name}:"):
            capturing = True
            continue
        if capturing:
            if line and not line.startswith((" ", "\t")):
                break
            body.append(line)
    return "\n".join(body)


def _command_lines(body: str) -> list[str]:
    """The recipe's executable lines, with comments stripped.

    Written because the first version of this guard could not fail. It asked
    whether the body CONTAINED the checker's name -- and the preflight comment
    this change adds says that name, so a recipe that stopped invoking its
    checker entirely still passed. A name is not a call: the substring-as-proof
    shape CLAUDE.md describes (#700), committed inside the change citing it.
    """
    return [
        line.strip()
        for line in body.splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]


@pytest.mark.parametrize("recipe", GUARDED_RECIPES)
def test_a_guarded_recipe_asks_before_running(recipe):
    """The preflight is wired in, and the checker it guards is still invoked."""
    commands = _command_lines(_recipe_body(recipe))
    assert any(
        "ontology_preflight.py" in line for line in commands
    ), f"{recipe} lost its ontology preflight (#708)"
    checker = RECIPE_CHECKER[recipe]
    assert any(line.startswith("uv run") and checker in line for line in commands), (
        f"{recipe} no longer INVOKES {checker} -- the preflight is supposed to "
        f"guard the check, not replace it"
    )


def test_the_vendored_validator_was_not_edited():
    """The fix must not drift a governed artifact.

    `scripts/validate_id_label_correspondence.py` is vendored byte-identically
    across the Mech repos and pinned to a claw revision. The first version of
    this change taught it a `SKIPPED_UNREACHABLE_ADAPTER` verdict directly,
    which is the better fix and broke `vendored-sync` -- so it belongs upstream,
    and the preflight lives beside it instead.
    """
    text = (REPO / "scripts" / "validate_id_label_correspondence.py").read_text(encoding="utf-8")
    assert "SKIPPED_UNREACHABLE_ADAPTER" not in text, (
        "the vendored id/label validator has been edited locally; that change "
        "belongs in culturebotai-claw, not here"
    )
