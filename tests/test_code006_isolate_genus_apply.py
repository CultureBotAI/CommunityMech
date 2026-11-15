"""External approval, bounded semantics and post-validation race guards (#2848)."""

import importlib.util
import json
from pathlib import Path

import pytest
import yaml
from test_code006_isolate_genus_candidate import candidate  # noqa: F401

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def harness(candidate, tmp_path, monkeypatch):  # noqa: F811
    _stage, _native, before, after, block, _row = candidate
    source = ROOT / "scripts/adhoc/apply_code006_isolate_genus_20261115.py"
    spec = importlib.util.spec_from_file_location("isolate_applier", source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    root = tmp_path / "repo"
    state = root / ".temp/gtdb-code006-20261115"
    stage = state / "stage"
    stage.mkdir(parents=True)
    target = next(name for name, row in module.TARGETS.items() if row[0] == before["id"])
    path = root / target
    path.parent.mkdir(parents=True)
    path.write_text(yaml.safe_dump(before, sort_keys=False))
    originals = dict(module.TARGETS)
    originals[target] = (*originals[target][:-1], module.sha(path))
    monkeypatch.setattr(module, "TARGETS", originals)
    for name in (
        str(source.relative_to(ROOT)),
        module.STAGER,
        "scripts/gtdb_ground.py",
        "src/communitymech/curate/curation_event.py",
        "src/communitymech/validation/write_validated.py",
    ):
        destination = root / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes((ROOT / name).read_bytes())
    for name in (module.PLAN, module.TABLE, "references_cache/PMID_42666409.txt"):
        destination = root / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text("unchanged toy input\n")
    monkeypatch.setattr(module, "ROOT", root)
    monkeypatch.setattr(module, "STATE", state)
    monkeypatch.setattr(module, "__file__", str(root / source.relative_to(ROOT)))
    monkeypatch.setattr(module, "head", lambda: "toy-execution")
    monkeypatch.setattr(module, "PLAN_SHA", module.sha(root / module.PLAN))
    monkeypatch.setattr(module, "TABLE_SHA", module.sha(root / module.TABLE))
    names = [
        target,
        module.STAGER,
        module.PLAN,
        module.TABLE,
        "scripts/gtdb_ground.py",
        "src/communitymech/curate/curation_event.py",
        "references_cache/PMID_42666409.txt",
    ]
    candidate_path = stage / path.name
    candidate_path.write_text(yaml.safe_dump(after, sort_keys=False))
    receipt = {
        "target": target,
        "record_id": before["id"],
        "code_revision": module.STAGING_REVISION,
        "canonical_apply": False,
        "exit_codes": [0, 0],
        "source_inputs_unchanged": True,
        "candidate_sha256": module.sha(candidate_path),
        "native_block": block,
        "inputs": {name: module.sha(root / name) for name in names},
        "scope": "Fixture same-genus technical correspondence only.",
    }
    (stage / "receipt.json").write_text(json.dumps(receipt))
    return module, stage, state / "applied", path


def run(harness, **kwargs):
    module, stage, output, target = harness
    return module.apply(
        stage,
        output,
        module.sha(stage / target.name),
        module.sha(stage / "receipt.json"),
        "toy-execution",
        **kwargs,
    )


def test_plan_then_actual_native_persistence_and_duplicate_refusal(harness):
    module, stage, output, target = harness
    assert run(harness)["planned"] is True
    assert not output.exists()
    result = run(harness, do_apply=True)
    assert result["applied"] is True
    assert target.read_bytes() == (stage / target.name).read_bytes()
    assert json.loads((output / "receipt.json").read_bytes()) == result
    assert (output / "before.yaml").stat().st_size > 0
    with pytest.raises(ValueError):
        run(harness, do_apply=True)


def test_external_review_hashes_are_required(harness):
    module, stage, output, target = harness
    original = target.read_bytes()
    with pytest.raises(ValueError, match="reviewed receipt"):
        module.apply(
            stage, output, module.sha(stage / target.name), "0" * 64, "toy-execution", do_apply=True
        )
    assert target.read_bytes() == original and not output.exists()


def test_forged_candidate_and_receipt_cannot_expand_scope(harness):
    module, stage, output, target = harness
    original = target.read_bytes()
    path = stage / target.name
    document = yaml.safe_load(path.read_bytes())
    document["ecological_interactions"][0]["description"] += " Invented source claim."
    path.write_text(yaml.safe_dump(document, sort_keys=False))
    receipt_path = stage / "receipt.json"
    receipt = json.loads(receipt_path.read_bytes())
    receipt["candidate_sha256"] = module.sha(path)
    receipt_path.write_text(json.dumps(receipt))
    with pytest.raises(ValueError, match="exceeds exact"):
        run(harness, do_apply=True)
    assert target.read_bytes() == original and not output.exists()


@pytest.mark.parametrize("when", ["before", "during", "implementation"])
def test_source_and_implementation_change_refused(harness, monkeypatch, when):
    module, _stage, output, target = harness
    original = target.read_bytes()
    source = module.ROOT / "references_cache/PMID_42666409.txt"
    if when == "before":
        source.write_text("different source\n")
    else:
        native = module.write_validated_community

        def raced(document, path):
            native(document, path)
            changed = source if when == "during" else Path(module.__file__)
            changed.write_bytes(changed.read_bytes() + b"\nchanged during native validation\n")

        monkeypatch.setattr(module, "write_validated_community", raced)
    with pytest.raises(ValueError, match="changed"):
        run(harness, do_apply=True)
    assert target.read_bytes() == original
    assert not (output / "receipt.json").exists()
