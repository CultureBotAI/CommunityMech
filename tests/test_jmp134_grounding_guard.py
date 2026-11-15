"""Exercise actual bounded JMP134 application/refusal, #2848, 2026-11-15."""

import copy
import importlib.util
import json
import subprocess
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
HISTORICAL = "68699871415fda3c9eebf20382a315f9f3c7b17a"


@pytest.fixture
def harness(tmp_path, monkeypatch):
    monkeypatch.syspath_prepend(str(ROOT / "scripts/adhoc"))
    source = ROOT / "scripts/adhoc/apply_jmp134_grounding_20261115.py"
    spec = importlib.util.spec_from_file_location("jmp134_guard_test", source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    staging = module.staging
    root = tmp_path / "repo"
    state = root / ".temp/gtdb-species-status-20261115"
    stage = state / "candidate"
    stage.mkdir(parents=True)
    target = root / module.TARGET
    target.parent.mkdir(parents=True)
    original = subprocess.check_output(["git", "show", f"{HISTORICAL}:{module.TARGET}"], cwd=ROOT)
    assert module.digest(original) == module.BASELINE
    target.write_bytes(original)
    before = yaml.safe_load(original)
    native = staging.native_module()
    native_result = {
        "ncbi_source_id": "NCBITaxon:264198",
        "gtdb_id": "GTDB:s__Cupriavidus_pinatubonensis",
        "gtdb_taxon": "Cupriavidus pinatubonensis",
        "gtdb_lineage": (
            "d__Bacteria;p__Pseudomonadota;c__Gammaproteobacteria;o__Burkholderiales;"
            "f__Burkholderiaceae;g__Cupriavidus;s__Cupriavidus pinatubonensis"
        ),
        "majority_fraction": 1.0,
        "total_genomes": 1,
        "is_reclassified": False,
        "via": "ncbi_id",
    }
    block = native._block(native_result, "fixture crosswalk sha256:761d5537a7edb4b0")
    after = copy.deepcopy(before)
    after["taxonomy"][0]["taxon_term"]["gtdb_classification"] = block
    after["taxonomy"][0]["taxon_term"]["gtdb_grounding_status"] = "GROUNDED"
    for action, changes in (
        ("GTDB_GROUND", "Added 1 gtdb_classification block(s) from NCBI2GTDB.tsv.gz (#395)."),
        ("GTDB_SET_STATUS", "Wrote gtdb_grounding_status on 1 taxonomy entries (#294, #395)."),
    ):
        native.record_curation_event(
            after,
            curator="gtdb_ground.py",
            action=action,
            changes=changes,
            timestamp="2026-11-15T00:00:00Z",
        )
    candidate = stage / target.name
    candidate.write_text(yaml.safe_dump(after, sort_keys=False))
    names = (
        "scripts/gtdb_ground.py",
        "scripts/adhoc/stage_jmp134_grounding_20261115.py",
        "scripts/adhoc/inspect_jmp134_grounding_20261115.py",
        "src/communitymech/validation/write_validated.py",
        "src/communitymech/schema/communitymech.yaml",
        "src/communitymech/schema/mech_shared.yaml",
    )
    paths = [target]
    for name in names:
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes((ROOT / name).read_bytes())
        paths.append(path)
    source_copy = root / source.relative_to(ROOT)
    source_copy.write_bytes(source.read_bytes())
    table = state / "kg-microbe/data/raw/NCBI2GTDB.tsv.gz"
    table.parent.mkdir(parents=True)
    table.write_bytes(b"fixture only; no scientific correspondence asserted")
    paths.append(table)
    proof = state / "jmp134-source-001.json"
    proof.write_text(
        json.dumps(
            {
                "native_result": native_result,
                "inputs": {
                    str(path.relative_to(root)): module.digest(path.read_bytes()) for path in paths
                },
            }
        )
    )
    paths.append(proof)
    monkeypatch.setattr(staging, "PROOF_SHA", module.digest(proof.read_bytes()))
    receipt = {
        "code_revision": staging.REVISION,
        "canonical_apply": False,
        "source_inputs_unchanged": True,
        "exit_codes": [0, 0],
        "candidate_sha256": module.digest(candidate.read_bytes()),
        "inputs": {str(path.relative_to(root)): module.digest(path.read_bytes()) for path in paths},
        "native_block": block,
        "native_result": native_result,
        "appended_native_inline_history": after["curation_history"][-2:],
        "scope": "fixture exact block/status/two events",
    }
    receipt_path = stage / "receipt.json"
    receipt_path.write_text(json.dumps(receipt))
    monkeypatch.setattr(module, "ROOT", root)
    monkeypatch.setattr(module, "STATE", state)
    monkeypatch.setattr(module, "__file__", str(source_copy))
    monkeypatch.setattr(staging, "head", lambda: staging.REVISION)
    return module, stage, target, candidate, receipt_path, table


def invoke(harness, *, plan=False):
    module, stage, _target, candidate, receipt, _table = harness
    return module.apply(
        stage,
        stage.parent / "applied",
        module.digest(candidate.read_bytes()),
        module.digest(receipt.read_bytes()),
        module.staging.REVISION,
        plan=plan,
    )


def test_actual_native_validation_and_persistence(harness):
    module, stage, target, candidate, *_ = harness
    result = invoke(harness)
    assert result["applied"] and result["scientific_review"] is False
    assert target.read_bytes() == candidate.read_bytes()
    assert (stage.parent / "applied/receipt.json").stat().st_size > 0
    assert module.digest((stage.parent / "applied/before.yaml").read_bytes()) == module.BASELINE


def test_plan_is_read_only(harness):
    _module, stage, target, *_ = harness
    before = target.read_bytes()
    assert invoke(harness, plan=True)["planned"]
    assert target.read_bytes() == before and not (stage.parent / "applied").exists()


@pytest.mark.parametrize("mutation", ["stock", "quote", "discussion", "history", "count", "status"])
def test_unreviewed_semantic_changes_refused_and_restoration_passes(harness, mutation):
    module, _stage, target, candidate, receipt_path, _table = harness
    before = target.read_bytes()
    saved_candidate, saved_receipt = candidate.read_bytes(), receipt_path.read_bytes()
    doc = yaml.safe_load(saved_candidate)
    if mutation == "stock":
        doc["taxonomy"][0]["taxon_term"]["term"]["id"] = "NCBITaxon:106590"
    elif mutation == "quote":
        doc["taxonomy"][0]["evidence"][0]["snippet"] += " invented"
    elif mutation == "discussion":
        doc["discussions"][0]["status"] = "RESOLVED"
    elif mutation == "history":
        doc["curation_history"][0]["changes"] += " rewritten"
    elif mutation == "count":
        doc["taxonomy"][0]["taxon_term"]["gtdb_classification"]["total_genomes"] = 2
    else:
        doc["taxonomy"][0]["taxon_term"]["gtdb_grounding_status"] = "UNRESOLVED"
    candidate.write_text(yaml.safe_dump(doc, sort_keys=False))
    receipt = json.loads(saved_receipt)
    receipt["candidate_sha256"] = module.digest(candidate.read_bytes())
    receipt_path.write_text(json.dumps(receipt))
    with pytest.raises(ValueError):
        invoke(harness)
    assert target.read_bytes() == before
    candidate.write_bytes(saved_candidate)
    receipt_path.write_bytes(saved_receipt)
    assert invoke(harness)["applied"]


def test_external_receipt_hash_cannot_self_authorize_changes(harness):
    module, stage, target, candidate, receipt, _table = harness
    before = target.read_bytes()
    candidate_sha, receipt_sha = module.digest(candidate.read_bytes()), module.digest(
        receipt.read_bytes()
    )
    receipt.write_bytes(receipt.read_bytes() + b"\n")
    with pytest.raises(ValueError, match="external reviewed"):
        module.apply(
            stage, stage.parent / "applied", candidate_sha, receipt_sha, module.staging.REVISION
        )
    assert target.read_bytes() == before


@pytest.mark.parametrize(
    "changed", ["source", "candidate", "receipt", "implementation", "target", "head"]
)
def test_change_during_native_validation_refuses_actual_replace(harness, monkeypatch, changed):
    module, stage, target, candidate, receipt, table = harness
    before = target.read_bytes()
    original_write = module.write_validated_community

    def mutate(doc, output):
        original_write(doc, output)
        if changed == "head":
            monkeypatch.setattr(module.staging, "head", lambda: "0" * 40)
            return
        path = {
            "source": table,
            "candidate": candidate,
            "receipt": receipt,
            "implementation": Path(module.__file__),
            "target": target,
        }[changed]
        path.write_bytes(path.read_bytes() + b"\n# concurrent change\n")

    monkeypatch.setattr(module, "write_validated_community", mutate)
    with pytest.raises(ValueError, match="changed"):
        invoke(harness)
    if changed == "target":
        assert target.read_bytes() == before + b"\n# concurrent change\n"
    else:
        assert target.read_bytes() == before
    assert not (stage.parent / "applied/receipt.json").exists()
