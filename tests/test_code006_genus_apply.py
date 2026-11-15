"""One-genus externally reviewed application and concurrency controls, #2848."""

import copy
import importlib.util
import json
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def harness(tmp_path, monkeypatch):
    directory = ROOT / "scripts/adhoc"
    monkeypatch.syspath_prepend(str(directory))
    source = directory / "apply_code006_genus_grounding_20261115.py"
    spec = importlib.util.spec_from_file_location("genus_apply_test", source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    root = tmp_path / "repo"
    state = root / ".temp/gtdb-code006-20261115"
    stage = state / "stage"
    stage.mkdir(parents=True)
    for path in (
        source,
        Path(module.guarded.__file__),
        Path(module.staging.__file__),
        ROOT / "scripts/gtdb_ground.py",
    ):
        target = root / path.relative_to(ROOT)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(path.read_bytes())
    monkeypatch.setattr(module, "__file__", str(root / source.relative_to(ROOT)))
    monkeypatch.setattr(
        module.guarded,
        "__file__",
        str(root / "scripts/adhoc/apply_code006_gtdb_status_20261115.py"),
    )
    monkeypatch.setattr(
        module.staging,
        "__file__",
        str(root / "scripts/adhoc/stage_code006_genus_grounding_20261115.py"),
    )
    monkeypatch.setattr(module, "ROOT", root)
    monkeypatch.setattr(module, "STATE", state)
    monkeypatch.setattr(module.guarded, "ROOT", root)
    monkeypatch.setattr(module.guarded, "current_head", lambda: module.staging.REVISION)
    target = root / module.TARGET
    target.parent.mkdir(parents=True)
    before = yaml.safe_load((ROOT / module.TARGET).read_bytes())
    before["taxonomy"][1]["taxon_term"].pop("gtdb_classification", None)
    before["taxonomy"][1]["taxon_term"]["gtdb_grounding_status"] = "NOT_ATTEMPTED"
    original = yaml.safe_dump(before, sort_keys=False).encode()
    target.write_bytes(original)
    monkeypatch.setattr(module, "BASELINE", module.guarded.digest(original))
    after = copy.deepcopy(before)
    block = {
        "gtdb_id": "GTDB:g__Mycobacterium",
        "gtdb_taxon": "Mycobacterium",
        "ncbi_source_id": "NCBITaxon:1763",
        "majority_fraction": 1.0,
        "support_genomes": 18589,
        "total_genomes": 18589,
        "is_reclassified": False,
    }
    after["taxonomy"][1]["taxon_term"]["gtdb_classification"] = block.copy()
    after["taxonomy"][1]["taxon_term"]["gtdb_grounding_status"] = "GROUNDED"
    for action, changes in (
        ("GTDB_GROUND", "Added 1 gtdb_classification block(s) from NCBI2GTDB.tsv.gz (#395)."),
        ("GTDB_SET_STATUS", "Wrote gtdb_grounding_status on 1 taxonomy entries (#294, #395)."),
    ):
        module.guarded.record_curation_event(
            after,
            curator="gtdb_ground.py",
            action=action,
            changes=changes,
            timestamp="2026-11-15T00:00:00Z",
        )
    candidate = stage / target.name
    candidate.write_text(yaml.safe_dump(after, sort_keys=False))
    predecessor = state / "applied-001/receipt.json"
    predecessor.parent.mkdir()
    predecessor.write_text('{"fixture": "prior actual receipt"}\n')
    paths = (target, root / "scripts/gtdb_ground.py", Path(module.staging.__file__), predecessor)
    receipt = {
        "code_revision": module.staging.REVISION,
        "canonical_apply": False,
        "exit_codes": [0, 0],
        "candidate_sha256": module.staging.sha(candidate),
        "source_inputs_unchanged": True,
        "native_block": block,
        "inputs": {str(path.relative_to(root)): module.staging.sha(path) for path in paths},
    }
    receipt_path = stage / "receipt.json"
    receipt_path.write_text(json.dumps(receipt))
    return (
        module,
        stage,
        target,
        predecessor,
        module.staging.sha(candidate),
        module.staging.sha(receipt_path),
    )


def run(harness, **kwargs):
    module, stage, _target, _predecessor, candidate_sha, receipt_sha = harness
    return module.apply(
        stage,
        stage.parent / "applied",
        candidate_sha,
        receipt_sha,
        module.staging.REVISION,
        **kwargs,
    )


def test_actual_native_write_persists_reviewed_bytes(harness):
    module, stage, target, *_ = harness
    assert run(harness)["applied"] is True
    assert target.read_bytes() == (stage / target.name).read_bytes()
    assert (stage.parent / "applied/receipt.json").stat().st_size > 0


def test_plan_changes_nothing(harness):
    _module, stage, target, *_ = harness
    before = target.read_bytes()
    assert run(harness, plan=True)["planned"] is True
    assert target.read_bytes() == before
    assert not (stage.parent / "applied").exists()


def test_forged_candidate_and_adjacent_receipt_do_not_change_external_approval(harness):
    module, stage, target, *_ = harness
    original = target.read_bytes()
    candidate = stage / target.name
    changed = yaml.safe_load(candidate.read_bytes())
    changed["description"] += " Invented biology."
    candidate.write_text(yaml.safe_dump(changed))
    receipt = json.loads((stage / "receipt.json").read_bytes())
    receipt["candidate_sha256"] = module.staging.sha(candidate)
    (stage / "receipt.json").write_text(json.dumps(receipt))
    with pytest.raises(ValueError, match="external reviewed"):
        run(harness)
    assert target.read_bytes() == original


def test_stale_source_is_rejected(harness):
    _module, _stage, target, predecessor, *_ = harness
    original = target.read_bytes()
    predecessor.write_text("changed source")
    with pytest.raises(ValueError, match="reviewed input changed"):
        run(harness)
    assert target.read_bytes() == original


@pytest.mark.parametrize("changed", ["source", "implementation"])
def test_concurrent_change_after_native_validation_is_rejected(harness, monkeypatch, changed):
    module, _stage, target, predecessor, *_ = harness
    original = target.read_bytes()
    native_write = module.guarded.write_validated_community

    def mutate(doc, output):
        native_write(doc, output)
        path = predecessor if changed == "source" else Path(module.__file__)
        path.write_bytes(path.read_bytes() + b"\n# changed\n")

    monkeypatch.setattr(module.guarded, "write_validated_community", mutate)
    with pytest.raises(ValueError, match="changed"):
        run(harness)
    assert target.read_bytes() == original
