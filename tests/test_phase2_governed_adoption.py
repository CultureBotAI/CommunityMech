"""A changed preflight cannot expand the wrapper's apply scope (#2810)."""

import importlib
import sys
from pathlib import Path
from types import ModuleType, SimpleNamespace

import pytest


@pytest.mark.parametrize("mutation", [None, "target_head", "source_head", "extra_plan"])
def test_locked_scope_is_rebound_before_native_apply(tmp_path, monkeypatch, mutation):
    monkeypatch.syspath_prepend(str(Path(__file__).parents[1] / "scripts/adhoc"))
    driver = importlib.import_module("adopt_supporting_reference_schema_20261115")
    root, source = tmp_path / "consumer", tmp_path / "claw"
    root.mkdir()
    source.mkdir()
    monkeypatch.setattr(driver, "ROOT", root)
    heads = {root: "a" * 40, source: driver.PIN}
    monkeypatch.setattr(
        driver, "git", lambda repo, *args: heads[repo] if args[0] == "rev-parse" else ""
    )
    for name in driver.EXPECTED:
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("original\n")
    state = {"locked": False, "applied": False}
    calls = []

    def plan(*args, **kwargs):
        if state["applied"]:
            return []
        paths = set(driver.EXPECTED)
        if state["locked"] and mutation == "extra_plan":
            paths.add("scripts/unreviewed.py")
        return [SimpleNamespace(path=p, artifact_id=p, reason="content drift") for p in paths]

    def apply(*args, **kwargs):
        calls.append((args, kwargs))
        changes = plan()
        (root / "scripts/.vendored_canon_ref").write_text(driver.PIN + "\n")
        state["applied"] = True
        return changes

    class Lock:
        def __enter__(self):
            state["locked"] = True
            if mutation == "target_head":
                heads[root] = "b" * 40
            elif mutation == "source_head":
                heads[source] = "c" * 40

        def __exit__(self, *args):
            state["locked"] = False

    native = ModuleType("kg_microbe_governance")
    native.plan_sync, native.sync_repository = plan, apply
    locks = ModuleType("plugins.lock_manager")
    locks.LockManager = lambda: SimpleNamespace(lock=lambda *args: Lock())
    settings = ModuleType("plugins.repository_settings")
    target = SimpleNamespace(open=lambda: SimpleNamespace(working_tree_dir=str(root)))
    settings.RepositorySettings = SimpleNamespace(
        from_environment=lambda **kwargs: SimpleNamespace(get_target=lambda name: target)
    )
    monkeypatch.setitem(sys.modules, "kg_microbe_governance", native)
    monkeypatch.setitem(sys.modules, "plugins.lock_manager", locks)
    monkeypatch.setitem(sys.modules, "plugins.repository_settings", settings)
    monkeypatch.setattr(
        sys,
        "argv",
        ["adopt", "--claw-root", str(source), "--output", str(root / ".temp/run"), "--apply"],
    )
    if mutation:
        with pytest.raises(ValueError):
            driver.main()
        assert calls == [], "scope changed before lock, but native apply was already dispatched"
        assert (root / "scripts/.vendored_canon_ref").read_text() == "original\n"
    else:
        driver.main()
        assert len(calls) == 1 and calls[0][1] == {"apply": True}
        assert (root / ".temp/run/receipt.json").stat().st_size > 0
