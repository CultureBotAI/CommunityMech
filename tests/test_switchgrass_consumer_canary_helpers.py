"""Consumer helper guards for #1996; real bytes, refusal and restoration.

Only scratch files are changed. These controls do not claim the installed
CommunityMech runtime canary has run. 2026-11-15.
"""

import importlib.util
from pathlib import Path

import pytest
from ruamel.yaml import YAML

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    path = ROOT / "scripts/adhoc" / name
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


PREPARE = load("prepare_switchgrass_consumer_canary_20261115.py")
RUNNER = load("run_switchgrass_consumer_canary_20261115.py")


def schemas():
    return (
        b"# exact original formatting\nclasses:\n  EvidenceItem:\n    attributes:\n"
        b"      source_locator: {range: SourceLocator, inlined: true}\n",
        b"# separate shared bytes\nclasses:\n  SourceLocator: {}\n"
        b"  SupportingReference:\n    attributes:\n"
        b"      source_locator: {range: SourceLocator, inlined: true}\n",
    )


@pytest.mark.parametrize("owner", [0, 1])
@pytest.mark.parametrize("change", ["missing", "required", "range", "inlined"])
def test_native_schema_is_not_augmented_or_reserialized(owner, change):
    original = schemas()
    expected = dict(
        zip(("schema/communitymech.yaml", "schema/mech_shared.yaml"), original, strict=True)
    )
    assert PREPARE.native_schema_artifacts(*original) == expected
    changed = list(original)
    if change == "missing":
        changed[owner] = changed[owner].replace(
            b"source_locator: {range: SourceLocator, inlined: true}", b"other: {range: string}"
        )
    elif change == "required":
        changed[owner] = changed[owner].replace(b"inlined: true", b"inlined: true, required: true")
    elif change == "range":
        changed[owner] = changed[owner].replace(b"range: SourceLocator", b"range: string")
    else:
        changed[owner] = changed[owner].replace(b"inlined: true", b"inlined: false")
    assert changed[owner] != original[owner]
    with pytest.raises(ValueError, match="reviewed optional inlined locator"):
        PREPARE.native_schema_artifacts(*changed)
    assert PREPARE.native_schema_artifacts(*original) == expected
    # The original input is still exactly parseable and contains its old comments.
    assert YAML(typ="safe").load(original[owner])["classes"]


def package_pair(tmp_path):
    source_root = tmp_path / "reviewed"
    source = source_root / "src/linkml_reference_validator"
    installed = tmp_path / "installed/linkml_reference_validator"
    for directory in (source, installed):
        directory.mkdir(parents=True)
        (directory / "__init__.py").write_bytes(b'"""Real synthetic package bytes."""\n')
        (directory / "module.py").write_bytes(b"VALUE = 1\n")
    return source_root, source, installed


@pytest.mark.parametrize("change", ["extra", "changed"])
def test_complete_installed_identity_refuses_then_restores(tmp_path, change):
    root, source, installed = package_pair(tmp_path)
    assert len(RUNNER.capture_runtime_members(root, installed, {})[1]) == 2
    target = installed / ("stale.py" if change == "extra" else "module.py")
    old = target.read_bytes() if target.exists() else None
    target.write_bytes(b"VALUE = 2\n")
    assert target.read_bytes() != old
    expected_error = (
        "Installed Python membership differs from reviewed source"
        if change == "extra"
        else "Installed runtime bytes differ from reviewed source"
    )
    try:
        with pytest.raises(ValueError, match="^" + expected_error + "$"):
            RUNNER.capture_runtime_members(root, installed, {})
    finally:
        if old is None:
            target.unlink()
        else:
            target.write_bytes(old)
    captured = {}
    package, relative = RUNNER.capture_runtime_members(root, installed, captured)
    RUNNER.verify_runtime_membership(package, installed, relative)
    assert package == source and len(relative) == 2 and len(captured) == 4


@pytest.mark.parametrize("which", ["source", "installed"])
@pytest.mark.parametrize("change", ["add", "remove"])
def test_membership_change_after_capture_refuses_then_restores(tmp_path, which, change):
    root, source, installed = package_pair(tmp_path)
    package, relative = RUNNER.capture_runtime_members(root, installed, {})
    RUNNER.verify_runtime_membership(package, installed, relative)
    directory = source if which == "source" else installed
    target = directory / ("new.py" if change == "add" else "module.py")
    old = target.read_bytes() if target.exists() else None
    if change == "add":
        target.write_bytes(b"NEW = True\n")
    else:
        target.unlink()
    try:
        with pytest.raises(ValueError, match="membership changed"):
            RUNNER.verify_runtime_membership(package, installed, relative)
    finally:
        if old is None:
            target.unlink()
        else:
            target.write_bytes(old)
    RUNNER.verify_runtime_membership(package, installed, relative)
    assert len(RUNNER.capture_runtime_members(root, installed, {})[1]) == 2
