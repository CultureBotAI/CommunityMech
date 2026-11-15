"""Guard identity-specific native gate receipts and exact history sections; #2898."""

import importlib.util
import json
import subprocess
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
HELPER = "scripts/adhoc/check_wetland_identity_unit_20261115.py"
REVISION = "f" * 40


@pytest.fixture
def harness(tmp_path, monkeypatch):
    spec = importlib.util.spec_from_file_location("identity_check_test", ROOT / HELPER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    root = tmp_path / "repo"
    state = root / ".temp/fixture"
    state.mkdir(parents=True)
    target = root / module.TARGET
    target.parent.mkdir(parents=True)
    target.write_bytes(b"accepted current identity fixture")
    source = root / "references_cache/fixture.txt"
    source.parent.mkdir()
    source.write_bytes(b"fixed primary source fixture")
    applied = state / "applied/receipt.json"
    applied.parent.mkdir()
    applied.with_name("before.yaml").write_bytes(b"original identity fixture")
    receipt = {
        "applied": True,
        "target": module.TARGET,
        "target_id": "CommunityMech:000471",
        "scope": module.SCOPE,
        "scientific_review": False,
        "execution_revision": REVISION,
        "before_sha256": module.checks.digest(applied.with_name("before.yaml").read_bytes()),
        "after_sha256": module.checks.digest(target.read_bytes()),
        "inputs": {"references_cache/fixture.txt": module.checks.digest(source.read_bytes())},
    }
    receipt["inputs"][module.TARGET] = receipt["before_sha256"]
    applied.write_text(json.dumps(receipt))
    config = state / "check.json"
    config.write_text(
        json.dumps(
            {
                "target": module.TARGET,
                "scope": module.SCOPE,
                "before_sha256": receipt["before_sha256"],
                "after_sha256": receipt["after_sha256"],
                "application_receipt": str(applied.relative_to(root)),
                "application_receipt_sha256": module.checks.digest(applied.read_bytes()),
                "history_scaffolder_revision": REVISION,
                "history_summary": "Fixed fixture summary",
                "history_details": "Identity-only fixture, not a real M5 application.",
            }
        )
    )
    for name in (
        HELPER,
        module.SHARED,
        "uv.lock",
        "justfile",
        "src/communitymech/schema/communitymech.yaml",
        "src/communitymech/schema/history.yaml",
    ):
        p = root / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes((ROOT / name).read_bytes())
    claw = tmp_path / "claw"
    for name in (
        "src/kg_microbe_history/fixture.py",
        "src/kg_microbe_governance/artifacts/schema/history.yaml",
    ):
        p = claw / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("fixed native source fixture\n")
    monkeypatch.setattr(module, "ROOT", root)
    monkeypatch.setattr(module, "__file__", str(root / HELPER))
    monkeypatch.setattr(module.checks, "ROOT", root)
    monkeypatch.setattr(module.checks, "head", lambda _root=None: REVISION)
    calls = []
    sidecar = root / "history/records" / Path(module.TARGET).stem / "fixture.yaml"

    def native(command, **kwargs):
        calls.append(command)
        kwargs["stdout"].write(b"fixture native output persisted\n")
        if "new-history" in command and "--dry-run" not in command:
            sidecar.parent.mkdir(parents=True, exist_ok=True)
            sidecar.write_text(
                yaml.safe_dump(
                    {
                        "target": {"path": module.TARGET},
                        "events": [
                            {
                                "type": "EDIT",
                                "outcome": "changed",
                                "sections": command[command.index("--sections") + 1].split(","),
                                "details": command[command.index("--details") + 1],
                            }
                        ],
                    }
                )
            )
        return subprocess.CompletedProcess(command, 0)

    monkeypatch.setattr(module.subprocess, "run", native)
    return module, root, target, source, config, claw, sidecar, calls


def invoke(harness, gate="schema", suffix="001", plan=False):
    module, root, _, _, config, claw, *_ = harness
    return module.run(
        str(config.relative_to(root)),
        module.checks.digest(config.read_bytes()),
        gate,
        ".temp/fixture/check-" + suffix,
        REVISION,
        plan=plan,
        claw=claw,
    )


def test_fixed_target_receipt_and_no_crosswalk_requirement(harness):
    module, root, target, _, _, _, _, calls = harness
    result = invoke(harness)
    assert result["inputs"][str(target)] == module.checks.digest(target.read_bytes())
    assert result["execution_inputs_unchanged"] and len(calls) == 1
    assert (root / ".temp/fixture/check-001/native.exit").read_bytes() == b"0\n"
    assert json.loads((root / ".temp/fixture/check-001/receipt.json").read_bytes()) == result


def test_history_exact_four_sections_and_actual_receipt_bound(harness):
    module, _, _, _, config, _, sidecar, _ = harness
    result = invoke(harness, "new-history")
    assert result["new_history_sidecars"]
    event = yaml.safe_load(sidecar.read_bytes())["events"][0]
    assert event["sections"] == module.SECTIONS.split(",")
    assert json.loads(config.read_bytes())["application_receipt_sha256"] in event["details"]


@pytest.mark.parametrize("field", ["target", "sections", "receipt", "type", "missing"])
def test_bad_or_missing_sidecar_refuses_publication_then_restores(harness, monkeypatch, field):
    module, root, _, _, _, _, sidecar, _ = harness
    actual = module.subprocess.run

    def mutate(command, **kwargs):
        result = actual(command, **kwargs)
        doc = yaml.safe_load(sidecar.read_bytes())
        if field == "missing":
            sidecar.unlink()
            return result
        if field == "target":
            doc["target"]["path"] = "kb/communities/Other.yaml"
        elif field == "sections":
            doc["events"][0]["sections"] = ["taxonomy", "curation_history"]
        elif field == "type":
            doc["events"][0]["type"] = "REVIEW"
        else:
            doc["events"][0]["details"] = "unbound"
        sidecar.write_text(yaml.safe_dump(doc))
        return result

    monkeypatch.setattr(module.subprocess, "run", mutate)
    with pytest.raises(ValueError, match="sidecar"):
        invoke(harness, "new-history")
    assert not (root / ".temp/fixture/check-001/receipt.json").exists()
    if sidecar.exists():
        sidecar.unlink()
    monkeypatch.setattr(module.subprocess, "run", actual)
    assert invoke(harness, "new-history", "restored")["exit_code"] == 0


@pytest.mark.parametrize("field", ["target", "source", "helper"])
def test_input_mutation_refuses_success_then_restores(harness, monkeypatch, field):
    module, root, target, source, *_ = harness
    location = {"target": target, "source": source, "helper": root / HELPER}[field]
    original = location.read_bytes()
    actual = module.subprocess.run

    def mutate(command, **kwargs):
        result = actual(command, **kwargs)
        location.write_bytes(original + b" changed")
        return result

    monkeypatch.setattr(module.subprocess, "run", mutate)
    with pytest.raises(ValueError, match="captured execution inputs"):
        invoke(harness)
    assert not (root / ".temp/fixture/check-001/receipt.json").exists()
    location.write_bytes(original)
    monkeypatch.setattr(module.subprocess, "run", actual)
    assert invoke(harness, suffix="restored")["exit_code"] == 0


def test_dry_run_is_explicit_and_cannot_claim_history(harness):
    result = invoke(harness, "new-history", plan=True)
    assert result["plan"] is True and not result["new_history_sidecars"]
    assert "--dry-run" in result["command"]
