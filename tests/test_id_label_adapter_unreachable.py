"""An outage is not a verdict about the KB -- but a typo must not look like one.

While `s3.amazonaws.com/bbop-sqlite` answered 403 for every ontology build,
`validate-products` emitted 6250+ `ADAPTER_ERROR` rows with `canonical=''` on
every term of every record, and `main` was red for two days on a condition no PR
caused and none could fix (#708). Reporting that as an ERROR conflates "the check
could not run" with "the check found something".

The fix downgrades it to `SKIPPED_UNREACHABLE_ADAPTER`. **The danger in that fix
is the whole subject of this module.** A typo'd ontology name raises the exact
same `DownloadError` as a real outage -- `sqlite:obo:not_a_real_ontology_xyz`
fails identically to `sqlite:obo:go`, and S3 answers 403 for a nonexistent key
just as it does for a forbidden one, so neither the exception type nor the HTTP
status separates them. Downgrading on the error alone would let one typo in
`conf/id_label_targets.yaml` turn a whole ontology's checking off while the gate
reported clean: #686's failure mode, reintroduced by the fix for #708.

So the downgrade needs two independent conditions, and the tests below hold both:
the exception type narrows the candidates, and `PINNED_ONTOLOGY_NAMES` decides.
That ordering is CLAUDE.md's "a guard may narrow, never excuse" (#700).
"""

from __future__ import annotations

import importlib.util
import pathlib

import pytest

REPO = pathlib.Path(__file__).parent.parent
SCRIPT = REPO / "scripts" / "validate_id_label_correspondence.py"


def _module():
    """Load the validator from source.

    `scripts/` is not a package, and a `.pyc` validated on (mtime, size) can
    serve a module that is not the file under test (#693).
    """
    spec = importlib.util.spec_from_file_location("_id_label_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class _FakeDownloadError(Exception):
    """Stands in for pystow's DownloadError without needing a network."""


@pytest.fixture
def patched(monkeypatch):
    """The validator with pystow's DownloadError swapped for a local class.

    The production check is `isinstance` against pystow's real type, so the test
    has to control that type rather than raise something merely named alike --
    which is also the property being asserted.
    """
    import pystow.utils

    monkeypatch.setattr(pystow.utils, "DownloadError", _FakeDownloadError)
    return _module()


def _pool_result(module, monkeypatch, selector: str, exc: BaseException):
    """What `AdapterPool.get` caches when `get_adapter` raises `exc`."""
    import oaklib

    monkeypatch.setattr(oaklib, "get_adapter", lambda _sel: (_ for _ in ()).throw(exc))
    pool = module.AdapterPool({"GO": selector})
    return pool.get("GO")


def test_the_config_asks_only_for_pinned_ontologies():
    """Every configured selector must be one the downgrade is allowed to cover.

    This is the structural half. It runs offline and deterministically, so a
    typo fails here -- loudly, on every machine -- instead of silently becoming
    a skipped ontology at runtime.
    """
    import yaml

    config = yaml.safe_load((REPO / "conf" / "id_label_targets.yaml").read_text(encoding="utf-8"))
    module = _module()

    selectors: dict[str, str] = {}

    def walk(node):
        if isinstance(node, dict):
            for key, value in node.items():
                if key == "adapters" and isinstance(value, dict):
                    selectors.update(value)
                else:
                    walk(value)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(config)
    assert selectors, "no adapters found in the config; this test would prove nothing"

    unpinned = sorted(
        f"{prefix} -> {selector}"
        for prefix, selector in selectors.items()
        if not module._is_pinned_obo_selector(selector)
    )
    assert unpinned == [], (
        "these configured adapters are not in PINNED_ONTOLOGY_NAMES, so a "
        "DownloadError on them would be a fatal ADAPTER_ERROR rather than a "
        "skip. Either the name is a typo, or the pin needs the new ontology "
        "added deliberately (#708):\n  " + "\n  ".join(unpinned)
    )


def test_an_unreachable_pinned_ontology_is_skipped_not_failed(patched, monkeypatch):
    """The case the fix exists for."""
    result = _pool_result(
        patched, monkeypatch, "sqlite:obo:go", _FakeDownloadError("403 from bbop-sqlite")
    )
    assert result is patched.UNREACHABLE_ADAPTER


def test_a_typoed_ontology_name_is_still_a_fatal_error(patched, monkeypatch):
    """The danger the pin exists for.

    Same exception, unpinned name. If this ever returns UNREACHABLE_ADAPTER, one
    typo in the config silently stops an ontology being checked at all.
    """
    result = _pool_result(
        patched,
        monkeypatch,
        "sqlite:obo:not_a_real_ontology_xyz",
        _FakeDownloadError("403 from bbop-sqlite"),
    )
    assert result is patched.LOAD_FAILED


def test_a_non_download_failure_on_a_pinned_name_is_still_fatal(patched, monkeypatch):
    """A broken local path or a corrupt db is a real error, outage or not."""
    result = _pool_result(
        patched, monkeypatch, "sqlite:obo:go", FileNotFoundError("File does not exist")
    )
    assert result is patched.LOAD_FAILED


def test_the_skip_never_fails_an_enforce_run_and_the_error_still_does():
    """Both halves, because asserting only the first would pass if the verdict
    were simply unknown to the module."""
    module = _module()
    assert "SKIPPED_UNREACHABLE_ADAPTER" not in module._ERROR_VERDICTS
    assert "SKIPPED_UNREACHABLE_ADAPTER" in module._SKIP_VERDICTS
    assert "ADAPTER_ERROR" in module._ERROR_VERDICTS


def test_the_check_can_actually_fail(monkeypatch):
    """Remove the pin's authority and the typo test must go red.

    Control arm first (CLAUDE.md, "Proving a gate can fail", rule 5): the
    UNMUTATED module must give the two results the tests above assert, so a red
    from the mutated one belongs to the mutation and not to the harness.
    """
    import pystow.utils

    monkeypatch.setattr(pystow.utils, "DownloadError", _FakeDownloadError)

    control = _module()
    assert (
        _pool_result(control, monkeypatch, "sqlite:obo:go", _FakeDownloadError("x"))
        is control.UNREACHABLE_ADAPTER
    ), "control arm is wrong; nothing below can be attributed to the mutation"
    assert (
        _pool_result(control, monkeypatch, "sqlite:obo:typo", _FakeDownloadError("x"))
        is control.LOAD_FAILED
    ), "control arm is wrong; nothing below can be attributed to the mutation"

    # Mutation: let the exception type alone authorise the downgrade.
    mutated = _module()
    monkeypatch.setattr(mutated, "_is_pinned_obo_selector", lambda _selector: True)
    assert mutated._is_pinned_obo_selector("sqlite:obo:typo") is True, "mutation not applied"

    assert (
        _pool_result(mutated, monkeypatch, "sqlite:obo:typo", _FakeDownloadError("x"))
        is mutated.UNREACHABLE_ADAPTER
    ), (
        "with the pin neutered, a typo'd ontology name should have been "
        "downgraded to a skip -- it was not, so "
        "test_a_typoed_ontology_name_is_still_a_fatal_error would pass with or "
        "without the pin it exists to defend"
    )


# --------------------------------------------------------------------------
# The preflight, and the risk it carries.
#
# Making Engine A decline when it cannot look anything up is only safe if it
# still RUNS when it can. A preflight stuck at "unreachable" would turn the gate
# off permanently and silently -- which is the failure this whole area keeps
# producing (#686, #689, #700). Both directions are asserted below.
# --------------------------------------------------------------------------

RECIPES_WITH_PREFLIGHT = ("validate-terms-all", "validate-terms-taxa")


def _recipe_body(name: str) -> str:
    import subprocess

    dump = subprocess.run(
        ["just", "--unstable", "--dump", "--dump-format", "just"],
        capture_output=True,
        text=True,
        cwd=REPO,
        timeout=120,
    )
    text = dump.stdout if dump.returncode == 0 else (REPO / "justfile").read_text(encoding="utf-8")
    lines = text.splitlines()
    body, capturing = [], False
    for line in lines:
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

    Written after the first version of the test below could not fail. It asked
    whether the body CONTAINED "linkml-term-validator" -- and the preflight
    comment this change adds says that word, so a recipe that stopped invoking
    the validator entirely still passed. A name is not a call: exactly the
    substring-as-proof shape CLAUDE.md's "a guard may narrow, never excuse"
    describes (#700), committed inside the change that cites it.
    """
    lines = []
    for line in body.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        lines.append(stripped)
    return lines


@pytest.mark.parametrize("recipe", RECIPES_WITH_PREFLIGHT)
def test_engine_a_recipes_ask_before_running(recipe):
    """The preflight is wired in, and the check it guards is still INVOKED.

    The second assertion is the one that matters: a preflight that replaced the
    validator loop instead of guarding it would satisfy the first and check
    nothing forever. It looks for an actual invocation among the executable
    lines, not for the tool's name anywhere in the text.
    """
    commands = _command_lines(_recipe_body(recipe))
    assert any(
        "--check-adapters" in line for line in commands
    ), f"{recipe} lost its ontology preflight (#708)"
    assert any(line.startswith("uv run linkml-term-validator") for line in commands), (
        f"{recipe} no longer INVOKES the validator -- the preflight is supposed "
        f"to guard the check, not replace it"
    )


def test_a_reachable_ontology_does_not_trigger_the_preflight(tmp_path, monkeypatch):
    """All adapters reachable -> nothing is reported unreachable.

    Hermetic: `get_adapter` is patched to succeed, so this holds on a machine
    with no ontology cache and during an outage. Without it, every assertion in
    this module is about the failure direction only, and a preflight wired to
    return "unreachable" unconditionally would pass all of them.
    """
    import oaklib
    import yaml as _yaml

    class _Adapter:
        def entities(self):
            return iter(["GO:0000001"])

    monkeypatch.setattr(oaklib, "get_adapter", lambda _sel: _Adapter())

    config = tmp_path / "targets.yaml"
    config.write_text(
        _yaml.safe_dump({"targets": [{"adapters": {"GO": "sqlite:obo:go"}}]}),
        encoding="utf-8",
    )
    assert _module().unreachable_ontologies(config) == []


def test_an_unreachable_ontology_is_named_by_the_preflight(tmp_path, monkeypatch, patched):
    """...and the other direction, so the test above cannot pass vacuously."""
    import oaklib
    import yaml as _yaml

    monkeypatch.setattr(
        oaklib, "get_adapter", lambda _sel: (_ for _ in ()).throw(_FakeDownloadError("403"))
    )
    config = tmp_path / "targets.yaml"
    config.write_text(
        _yaml.safe_dump({"targets": [{"adapters": {"GO": "sqlite:obo:go"}}]}),
        encoding="utf-8",
    )
    assert patched.unreachable_ontologies(config) == ["GO"]
