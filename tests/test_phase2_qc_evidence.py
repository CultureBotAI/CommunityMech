"""Retain native identities and outcomes without promotion (#2809/#2839/#2850)."""

import hashlib
import importlib
import json
from pathlib import Path

import pytest

STANDALONE_RECIPES = (
    "validate-all",
    "validate-taxa",
    "validate-strict",
    "validate-gtdb-all",
    "validate-scalars",
    "validate-scalars-idiomatic",
    "validate-terms-all",
    "validate-terms-taxa",
    "validate-references-all",
)


@pytest.fixture
def native_receipt(tmp_path, monkeypatch):
    monkeypatch.syspath_prepend(str(Path(__file__).parents[1] / "scripts/adhoc"))
    module = importlib.import_module("export_phase2_qc_evidence_20261115")
    state = tmp_path / ".temp/m5-completion-20261114"
    state.mkdir(parents=True)
    output = tmp_path / "reports/technical-evidence"
    monkeypatch.setattr(module, "ROOT", tmp_path)
    monkeypatch.setattr(module, "STATE", state)
    monkeypatch.setattr(module, "OUTPUT", output)

    def prepare(name, status="PASSED", exit_code=0):
        raw = (
            b"Native ontology preflight unavailable. SKIPPED, NOT PASSED\n"
            if status == "COMPLETED WITH SKIPS"
            else b"Native recipe finished.\n"
        )
        log = state / f"{name}.log"
        log.write_bytes(raw)
        (state / f"{name}.exit").write_text(f"{exit_code}\n")
        recipe = name.split("-standalone-", 1)[-1] if "-standalone-" in name else "qc"
        receipt = {
            "name": name,
            "head": "a" * 40,
            "finished_at": "2026-11-15T00:00:00Z",
            "status": status,
            "exit_code": exit_code,
            "stages": (
                [
                    {
                        "recipe": recipe,
                        "status": "SKIPPED" if status == "COMPLETED WITH SKIPS" else status,
                    }
                ]
                if "-standalone-" in name
                else [{"recipe": "validate-terms-all", "status": "NOT RUN"}]
            ),
            "skip_markers": [raw.decode().strip()] if status == "COMPLETED WITH SKIPS" else [],
            "command": [
                "/opt/homebrew/bin/just",
                "--verbose",
                "--no-dotenv",
                "--color",
                "never",
                recipe,
            ],
            "dry_run": False,
            "diagnostic_no_deps": False,
            "log": str(log.relative_to(tmp_path)),
            "log_bytes": len(raw),
            "log_sha256": hashlib.sha256(raw).hexdigest(),
        }
        (state / f"{name}.json").write_text(json.dumps(receipt))
        return module, state, output, raw, receipt

    return prepare


@pytest.mark.parametrize(
    "name",
    ["phase2-test-qc", "phase2-code005-qc-references"]
    + [f"phase2-code006-standalone-{recipe}" for recipe in STANDALONE_RECIPES],
)
@pytest.mark.parametrize(
    "status,exit_code,accepted",
    [
        ("PASSED", 0, True),
        ("FAILED", 1, True),
        ("COMPLETED WITH SKIPS", 0, True),
        ("COMPLETED WITH SKIPS", 1, False),
        ("PASSED", 1, False),
        ("FAILED", 0, False),
    ],
)
def test_native_receipt_disposition_is_preserved(native_receipt, name, status, exit_code, accepted):
    module, state, output, raw, receipt = native_receipt(name, status, exit_code)
    if not accepted:
        with pytest.raises(ValueError, match="incomplete or inconsistent"):
            module.export(name)
        assert not output.exists()
        return
    module.export(name)
    saved = json.loads((output / f"{name}.receipt.json").read_text())
    assert saved["name"] == name
    assert saved["status"] == status
    assert saved["exit_code"] == exit_code
    assert saved["stages"] == receipt["stages"]
    assert saved["skip_markers"] == receipt["skip_markers"]
    assert (output / f"{name}.log.txt").read_bytes() == raw
    for kind, suffix in (("receipt", "json"), ("log", "log"), ("exit", "exit")):
        assert (
            saved["public_evidence"][f"raw_{kind}_sha256"]
            == hashlib.sha256((state / f"{name}.{suffix}").read_bytes()).hexdigest()
        )


@pytest.mark.parametrize(
    "name",
    ["phase2-code006-standalone-unknown", "phase2-code006-standalone-unknown-qc"],
)
def test_unknown_standalone_name_is_refused_before_publication(native_receipt, name):
    module, _, output, _, _ = native_receipt(name)
    with pytest.raises(ValueError, match="standalone"):
        module.export(name)
    assert not output.exists()


@pytest.mark.parametrize(
    "change",
    [
        {
            "command": [
                "/opt/homebrew/bin/just",
                "--verbose",
                "--no-dotenv",
                "--color",
                "never",
                "validate-taxa",
            ]
        },
        {
            "command": [
                "/opt/homebrew/bin/just",
                "--verbose",
                "--no-dotenv",
                "--color",
                "never",
                "--no-deps",
                "validate-all",
            ]
        },
        {"dry_run": True},
        {"diagnostic_no_deps": True},
        {"stages": [{"recipe": "validate-taxa", "status": "PASSED"}]},
    ],
)
def test_standalone_scope_mismatch_is_refused(native_receipt, change):
    name = "phase2-code006-standalone-validate-all"
    module, state, output, _, receipt = native_receipt(name)
    receipt.update(change)
    (state / f"{name}.json").write_text(json.dumps(receipt))
    with pytest.raises(ValueError, match="standalone"):
        module.export(name)
    assert not output.exists()


@pytest.mark.parametrize("change", [{"log_bytes": 1}, {"log_sha256": "0" * 64}])
def test_standalone_corrupted_log_binding_is_refused(native_receipt, change):
    name = "phase2-code006-standalone-validate-all"
    module, state, output, _, receipt = native_receipt(name)
    receipt.update(change)
    (state / f"{name}.json").write_text(json.dumps(receipt))
    with pytest.raises(ValueError, match="incomplete or inconsistent"):
        module.export(name)
    assert not output.exists()
