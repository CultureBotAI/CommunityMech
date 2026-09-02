"""Engine B is pointed at builds it already has, without drifting a vendored file (#716).

`conf/id_label_targets.yaml` names adapters as `sqlite:obo:<name>`. That
selector does not ask whether the database is usable — it asks pystow to ensure
the **`.db.gz`** is present and re-downloads when it is not. CI restores 20.29 GB
of `.db` files with no `.gz` at all, so Engine B reported 6300 ADAPTER_ERROR rows
and checked nothing (#707). Pointed at those same files, it checks **6288 pairs
and exits 0**.

`scripts/validate_id_label_correspondence.py` is a governed vendored artifact and
must stay byte-identical, so nothing about it changes: the config it already
accepts via `-c` is resolved at run time instead.

Resolution has to happen at run time because OAK expands neither `~` nor
`$HOME` — only an absolute path resolves — and an absolute path cannot be
committed.

**Engine A keeps asking about the ORIGINAL config on purpose.**
`linkml-term-validator` has no config to point anywhere, so it still cannot
survive an unreachable ontology. Giving it the resolved config's answer would
tell it to run and then let it die on a `DownloadError` — a preflight that
lies about the thing it guards.
"""

from __future__ import annotations

import importlib.util
import pathlib
import subprocess

import pytest

REPO = pathlib.Path(__file__).parent.parent
SCRIPT = REPO / "scripts" / "resolve_ontology_config.py"
CONFIG = REPO / "conf" / "id_label_targets.yaml"


def _module():
    spec = importlib.util.spec_from_file_location("_resolve_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_a_present_build_is_named_directly(tmp_path):
    """The case the whole change exists for."""
    directory = tmp_path / "oaklib"
    directory.mkdir()
    (directory / "go.db").write_bytes(b"present")

    text, rewritten = _module().resolve("  GO: sqlite:obo:go\n", directory)

    assert rewritten == ["go"]
    assert f"sqlite:{directory / 'go.db'}" in text
    assert "sqlite:obo:go" not in text


def test_a_missing_build_keeps_the_download_selector(tmp_path):
    """The other direction, so the test above cannot pass vacuously.

    If this ever stops holding, an ontology that is genuinely absent would stop
    being fetched at all — masking an outage rather than surviving one.
    """
    directory = tmp_path / "oaklib"
    directory.mkdir()

    text, rewritten = _module().resolve("  GO: sqlite:obo:go\n", directory)

    assert rewritten == []
    assert text == "  GO: sqlite:obo:go\n"


def test_an_empty_build_is_not_trusted(tmp_path):
    """A zero-byte file is a failed download, not a database."""
    directory = tmp_path / "oaklib"
    directory.mkdir()
    (directory / "go.db").write_bytes(b"")

    _, rewritten = _module().resolve("  GO: sqlite:obo:go\n", directory)

    assert rewritten == []


def test_nothing_but_the_selectors_changes(tmp_path):
    """Everything else in the config is copied through.

    The config carries the targets, the policies and the curator-accepted
    exceptions. A rewrite that touched any of those would change what is
    enforced while appearing to be about adapters.
    """
    directory = tmp_path / "oaklib"
    directory.mkdir()
    for name in ("chebi", "cl", "envo", "go", "ncbitaxon", "uberon"):
        (directory / f"{name}.db").write_bytes(b"present")

    original = CONFIG.read_text(encoding="utf-8")
    resolved, _ = _module().resolve(original, directory)

    before = [line for line in original.splitlines() if "sqlite:obo:" not in line]
    after = [line for line in resolved.splitlines() if "sqlite:" not in line]
    assert before == after
    assert len(original.splitlines()) == len(resolved.splitlines())


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


def _commands(body: str) -> list[str]:
    """Executable lines only. A name in a comment is not a call (#700)."""
    return [
        line.strip()
        for line in body.splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]


@pytest.mark.parametrize("recipe", ["validate-products", "report-label-drift"])
def test_engine_b_recipes_use_the_resolved_config(recipe: str):
    """They resolve first, and hand the validator the resolved file."""
    commands = _commands(_recipe_body(recipe))
    assert any("resolve_ontology_config.py" in line for line in commands), (
        f"{recipe} no longer resolves the config, so Engine B is back to "
        f"sqlite:obo: selectors that re-download (#716)"
    )
    validator = [
        line for line in commands if line.startswith("uv run") and "validate_id_label" in line
    ]
    assert validator, f"{recipe} no longer invokes the validator at all"
    assert all("id_label_targets.resolved.yaml" in line for line in validator), (
        f"{recipe} resolves a config and then hands the validator a different "
        f"one:\n  " + "\n  ".join(validator)
    )


@pytest.mark.parametrize("recipe", ["validate-terms-all", "validate-terms-taxa"])
def test_engine_a_recipes_do_not_use_the_resolved_config(recipe: str):
    """Engine A has no config to point, so it must keep asking about the real one.

    Handing it the resolved answer would say "go ahead" and then let
    `linkml-term-validator` die on a DownloadError — a preflight lying about the
    thing it guards.
    """
    commands = _commands(_recipe_body(recipe))
    assert any(
        "ontology_preflight.py" in line for line in commands
    ), f"{recipe} lost its preflight (#708)"
    assert not any("resolved.yaml" in line for line in commands), (
        f"{recipe} asks the preflight about the resolved config, but "
        f"linkml-term-validator cannot use it"
    )
