"""Exercise shared actual-persistence and refusal guards, #2848, 2026-11-15."""

import copy
import importlib.util
import json
import subprocess
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
BASE = "68699871415fda3c9eebf20382a315f9f3c7b17a"
TARGET = "data/isolates/Rhizorhabdus_Wittichii_YL_JM2C_BDE47_Dioxygenase_Isolate_Baseline.yaml"


@pytest.fixture
def harness(tmp_path, monkeypatch):
    source = ROOT / "scripts/adhoc/gtdb_batch_curation_20261115.py"
    spec = importlib.util.spec_from_file_location("shared_gtdb_guard", source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    native = module.native_module()
    root = tmp_path / "repo"
    state = root / ".temp/batch"
    stage = state / "staged"
    stage.mkdir(parents=True)
    target = root / TARGET
    target.parent.mkdir(parents=True)
    before = subprocess.check_output(["git", "show", f"{BASE}:{TARGET}"], cwd=ROOT)
    target.write_bytes(before)
    document = yaml.safe_load(before)
    for name in (*module.REQUIRED_INPUTS, str(source.relative_to(ROOT))):
        location = root / name
        location.parent.mkdir(parents=True, exist_ok=True)
        location.write_bytes((ROOT / name).read_bytes())
    table = state / "kg-microbe/data/raw/NCBI2GTDB.tsv.gz"
    table.parent.mkdir(parents=True)
    table.write_bytes(b"synthetic guard fixture, not a native correspondence measurement")
    result = {
        "ncbi_source_id": "NCBITaxon:160791",
        "gtdb_id": "GTDB:s__Rhizorhabdus_wittichii",
        "gtdb_taxon": "Rhizorhabdus wittichii",
        "gtdb_lineage": (
            "d__Bacteria;p__Pseudomonadota;c__Alphaproteobacteria;o__Sphingomonadales;"
            "f__Sphingomonadaceae;g__Rhizorhabdus;s__Rhizorhabdus wittichii"
        ),
        "majority_fraction": 0.86,
        "total_genomes": 7,
        "is_reclassified": False,
        "via": "ncbi_id",
    }
    row = {
        "record": TARGET,
        "record_id": document["id"],
        "before_sha256": module.sha(before),
        "occurrences": [
            {
                "taxonomy_index": 0,
                "term": document["taxonomy"][0]["taxon_term"]["term"],
                "strain_name": "YL-JM2C",
                "existing_descriptor": document["taxonomy"][0]["taxon_term"],
                "native_result": result,
            }
        ],
    }
    proof = state / "source.json"
    proof.write_text(
        json.dumps(
            {
                "records": [row],
                "inputs": {
                    TARGET: module.sha(before),
                    str(table.relative_to(root)): module.sha(table.read_bytes()),
                },
                "inputs_unchanged": True,
                "canonical_writes": False,
            }
        )
    )
    monkeypatch.setattr(module, "ROOT", root)
    monkeypatch.setattr(module, "STATE", root / ".temp")
    monkeypatch.setattr(module, "__file__", str(root / source.relative_to(ROOT)))
    monkeypatch.setattr(module, "head", lambda: "f" * 40)
    monkeypatch.setattr(module, "TABLE_SHA", module.sha(table.read_bytes()))
    mapping = "synthetic fixture source; native source proof is independently required"
    after, actions = module.expected_science(document, row, native, mapping)
    for action, changes in actions:
        native.record_curation_event(
            after,
            curator="gtdb_ground.py",
            action=action,
            changes=changes,
            timestamp="2026-11-15T00:00:00Z",
        )
    candidate = stage / target.name
    candidate.write_text(yaml.safe_dump(after, sort_keys=False))
    proof_name = str(proof.relative_to(root))
    _, _, _, inputs, _ = module.prepare(
        proof_name, module.sha(proof.read_bytes()), row["record_id"], "f" * 40
    )
    receipt = stage / "receipt.json"
    receipt.write_text(
        json.dumps(
            {
                "canonical_apply": False,
                "source_inputs_unchanged": True,
                "exit_codes": [0, 0],
                "native_operations": ["--apply", "--apply-status"],
                "candidate_sha256": module.sha(candidate.read_bytes()),
                "source_proof": {"path": proof_name, "sha256": module.sha(proof.read_bytes())},
                "target": TARGET,
                "target_id": row["record_id"],
                "before_sha256": module.sha(before),
                "inputs": {str(p.relative_to(root)): module.sha(raw) for p, raw in inputs.items()},
                "mapping_source": mapping,
                "appended_native_inline_history": after["curation_history"][-len(actions) :],
                "scope": "synthetic control of bounded actual publication",
            }
        )
    )
    return module, root, target, candidate, receipt, proof, table, row


def invoke(harness, *, plan=False):
    module, root, _, candidate, receipt, *_ = harness
    return module.apply(
        str(candidate.parent.relative_to(root)),
        ".temp/batch/applied",
        module.sha(candidate.read_bytes()),
        module.sha(receipt.read_bytes()),
        "f" * 40,
        plan=plan,
    )


def test_actual_native_writer_and_persisted_receipt(harness):
    module, root, target, candidate, *_ = harness
    before = target.read_bytes()
    assert invoke(harness)["applied"]
    assert target.read_bytes() == candidate.read_bytes()
    saved = root / ".temp/batch/applied"
    assert (saved / "before.yaml").read_bytes() == before
    assert json.loads((saved / "receipt.json").read_bytes())["after_sha256"] == module.sha(
        candidate.read_bytes()
    )


def test_plan_preserves_record_and_output_namespace(harness):
    _, root, target, *_ = harness
    before = target.read_bytes()
    assert invoke(harness, plan=True)["planned"]
    assert target.read_bytes() == before and not (root / ".temp/batch/applied").exists()


@pytest.mark.parametrize(
    "mutation", ["stock", "evidence", "discussion", "count", "history", "extra"]
)
def test_scientific_or_unapproved_change_refuses_then_restores(harness, mutation):
    module, _, target, candidate, receipt, *_ = harness
    baseline = target.read_bytes()
    old_candidate, old_receipt = candidate.read_bytes(), receipt.read_bytes()
    doc = yaml.safe_load(old_candidate)
    descriptor = doc["taxonomy"][0]["taxon_term"]
    if mutation == "stock":
        doc["taxonomy"][0]["strain_designation"]["strain_name"] = "RW1"
    elif mutation == "evidence":
        doc["taxonomy"][0]["evidence"][0]["snippet"] += " invented"
    elif mutation == "discussion":
        doc["discussions"][0]["status"] = "RESOLVED"
    elif mutation == "count":
        descriptor["gtdb_classification"]["total_genomes"] = 8
    elif mutation == "history":
        doc["curation_history"][0]["changes"] += " rewritten"
    else:
        descriptor["gtdb_classification"]["curated"] = True
    candidate.write_text(yaml.safe_dump(doc, sort_keys=False))
    value = json.loads(old_receipt)
    value["candidate_sha256"] = module.sha(candidate.read_bytes())
    receipt.write_text(json.dumps(value))
    with pytest.raises(ValueError):
        invoke(harness)
    assert target.read_bytes() == baseline
    candidate.write_bytes(old_candidate)
    receipt.write_bytes(old_receipt)
    assert invoke(harness)["applied"]


@pytest.mark.parametrize(
    "change", ["target", "table", "helper", "proof", "candidate", "receipt", "head"]
)
def test_concurrent_change_prevents_actual_canonical_replace(harness, monkeypatch, change):
    module, root, target, candidate, receipt, proof, table, _ = harness
    baseline = target.read_bytes()
    native_writer = module.write_validated_community

    def altered(doc, output):
        native_writer(doc, output)
        if change == "head":
            monkeypatch.setattr(module, "head", lambda: "0" * 40)
        else:
            location = {
                "target": target,
                "table": table,
                "helper": Path(module.__file__),
                "proof": proof,
                "candidate": candidate,
                "receipt": receipt,
            }[change]
            location.write_bytes(location.read_bytes() + b"\n# changed\n")

    monkeypatch.setattr(module, "write_validated_community", altered)
    with pytest.raises(ValueError, match="changed"):
        invoke(harness)
    assert target.read_bytes() == baseline + (b"\n# changed\n" if change == "target" else b"")
    assert not (root / ".temp/batch/applied/receipt.json").exists()


def test_duplicate_or_unscoped_batch_input_lists_refuse(harness):
    module, _, _, _, _, proof, _, row = harness
    value = json.loads(proof.read_bytes())
    other = {**copy.deepcopy(row), "record": "kb/communities/other.yaml", "record_id": "other"}
    value["records"].append(other)
    with pytest.raises(ValueError, match="explicit per-record"):
        module.source_unit(value, row["record_id"])
    value["records"][0]["input_paths"] = [TARGET, TARGET]
    with pytest.raises(ValueError, match="unique complete"):
        module.source_unit(value, row["record_id"])
    value["records"][0]["input_paths"] = [TARGET]
    assert module.source_unit(value, row["record_id"])[1] == {TARGET: row["before_sha256"]}


def test_complete_ambiguity_options_are_preserved(harness):
    module, _, target, _, _, _, _, row = harness
    before = yaml.safe_load(target.read_bytes())
    row = copy.deepcopy(row)
    row["occurrences"][0]["native_result"] = {
        "ambiguous": True,
        "via": "ncbi_name",
        "ncbi_source_id": "NCBITaxon:160791",
        "gtdb_options": ["GTDB:s__Rhizorhabdus_wittichii", "GTDB:s__Rhizorhabdus_wittichii_A"],
    }
    native = module.native_module()
    after, actions = module.expected_science(before, row, native, "fixture")
    assert len(actions) == 1 and actions[0][0] == "GTDB_SET_STATUS"
    term = after["taxonomy"][0]["taxon_term"]
    assert term["gtdb_grounding_status"] == "AMBIGUOUS" and "gtdb_classification" not in term
    assert term["gtdb_candidates"] == row["occurrences"][0]["native_result"]["gtdb_options"]
    for action, changes in actions:
        native.record_curation_event(
            after, curator="gtdb_ground.py", action=action, changes=changes
        )
    saved = yaml.safe_dump(after).encode()
    module.verify_candidate(target.read_bytes(), saved, row, native, "fixture")
    term["gtdb_candidates"].pop()
    with pytest.raises(ValueError, match="undeclared"):
        module.verify_candidate(
            target.read_bytes(), yaml.safe_dump(after).encode(), row, native, "fixture"
        )
    module.verify_candidate(target.read_bytes(), saved, row, native, "fixture")


def test_status_only_receipt_cannot_add_a_grounded_block(harness):
    _, _, target, _, receipt, *_ = harness
    before = target.read_bytes()
    saved = receipt.read_bytes()
    data = json.loads(saved)
    data["native_operations"] = ["--apply-status"]
    data["exit_codes"] = [0]
    receipt.write_text(json.dumps(data))
    with pytest.raises(ValueError, match="status-only"):
        invoke(harness)
    assert target.read_bytes() == before
    receipt.write_bytes(saved)
    assert invoke(harness)["applied"]
