"""Guard actual historical 393 note transitions and source changes (#2869)."""

import copy
import importlib.util
import json
import subprocess
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
HELPER = "scripts/adhoc/curate_gtdb_source_notes_20261115.py"
PLAN = "reports/gtdb-source-holds-20261115/paenibacillus-note-plan-001.json"
BASE = "68699871415fda3c9eebf20382a315f9f3c7b17a"
REVISION = "b5b4ad3cddc247ae52dd21086ca6ddceebadf01a"


@pytest.fixture
def case(tmp_path, monkeypatch):
    spec = importlib.util.spec_from_file_location("note_guard", ROOT / HELPER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    config = json.loads((ROOT / PLAN).read_bytes())
    original = subprocess.check_output(["git", "show", f"{BASE}:{config['target']}"], cwd=ROOT)
    assert module.sha(original) == config["before_sha256"]
    for name in (*config["inputs"], *module.REQUIRED, HELPER, PLAN):
        destination = tmp_path / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(
            original if name == config["target"] else (ROOT / name).read_bytes()
        )
    monkeypatch.setattr(module, "ROOT", tmp_path)
    monkeypatch.setattr(module, "__file__", str(tmp_path / HELPER))
    monkeypatch.setattr(module, "head", lambda: REVISION)

    def serialize(doc, output):
        output.write_text(yaml.safe_dump(doc, sort_keys=False))

    monkeypatch.setattr(module, "write_validated_community", serialize)
    return module, config, original, serialize


def stage(case, name=".temp/stage"):
    module, _, _, _ = case
    result = module.stage(PLAN, module.sha((module.ROOT / PLAN).read_bytes()), name, REVISION)
    return result, module.sha((module.ROOT / name / "receipt.json").read_bytes())


def test_real_historical_note_roundtrip_and_current_difference(case):
    module, config, original, _ = case
    receipt, receipt_sha = stage(case)
    candidate_path = module.ROOT / ".temp/stage" / Path(config["target"]).name
    candidate = candidate_path.read_bytes()
    expected, event = module.verify_candidate(original, candidate, config)
    before = yaml.safe_load(original)
    assert (
        expected["taxonomy"][2]["taxon_term"]["gtdb_candidates"]
        == before["taxonomy"][2]["taxon_term"]["gtdb_candidates"]
    )
    assert expected["curation_history"][:-1] == before["curation_history"]
    assert event["llm_assisted"] is True
    assert "ncbi_name" in expected["taxonomy"][2]["taxon_term"]["notes"]
    applied = module.apply(
        ".temp/stage", receipt["candidate_sha256"], receipt_sha, ".temp/apply", REVISION
    )
    assert applied["applied"] is True
    assert (module.ROOT / config["target"]).read_bytes() == candidate
    with pytest.raises(ValueError, match="input differs"):
        module.stage(PLAN, module.sha((module.ROOT / PLAN).read_bytes()), ".temp/repeat", REVISION)
    # Fixture keeps immutable baseline, rather than silently treating current bytes as historical.
    assert module.sha(original) == config["before_sha256"] != module.sha(candidate)


@pytest.mark.parametrize("mutation", ["note", "stock", "biology", "history", "options", "event"])
def test_undeclared_candidate_change_rejected_then_restored(case, mutation):
    module, config, original, _ = case
    receipt, receipt_sha = stage(case)
    target = module.ROOT / ".temp/stage" / Path(config["target"]).name
    good = target.read_bytes()
    changed = yaml.safe_load(good)
    if mutation == "note":
        changed["taxonomy"][2]["taxon_term"]["notes"] += " Stock identity is known."
    elif mutation == "stock":
        changed["taxonomy"][2]["strain_designation"]["notes"] = "invented assembly"
    elif mutation == "biology":
        changed["description"] += " Invented universal protection."
    elif mutation == "history":
        changed["curation_history"][0]["changes"] = "rewritten"
    elif mutation == "options":
        changed["taxonomy"][2]["taxon_term"]["gtdb_candidates"].pop()
    else:
        changed["curation_history"][-1]["llm_assisted"] = False
    with pytest.raises(ValueError, match="undeclared content|native history"):
        module.verify_candidate(original, yaml.safe_dump(changed).encode(), config)
    assert module.verify_candidate(original, good, config)[0] == yaml.safe_load(good)
    assert (module.ROOT / config["target"]).read_bytes() == original
    assert receipt_sha and receipt["source_inputs_unchanged"]


@pytest.mark.parametrize("which", ["paper", "population", "helper", "record"])
def test_source_change_during_native_validation_prevents_application(case, monkeypatch, which):
    module, config, original, serialize = case
    receipt, receipt_sha = stage(case)
    names = {
        "paper": "references_cache/PMID_41387930.txt",
        "population": (
            "reports/gtdb-ambiguity-20261115/r226-paenibacillus-ncbi-correspondence-001.json"
        ),
        "helper": HELPER,
        "record": config["target"],
    }
    altered = module.ROOT / names[which]
    raw = altered.read_bytes()

    def race(doc, output):
        serialize(doc, output)
        altered.write_bytes(raw + b"\n# changed during validation\n")

    monkeypatch.setattr(module, "write_validated_community", race)
    with pytest.raises(ValueError, match="captured input"):
        module.apply(
            ".temp/stage", receipt["candidate_sha256"], receipt_sha, ".temp/refused", REVISION
        )
    assert not (module.ROOT / ".temp/refused/receipt.json").exists()
    assert (module.ROOT / config["target"]).read_bytes() == (
        raw + b"\n# changed during validation\n" if which == "record" else original
    )
    altered.write_bytes(raw)
    monkeypatch.setattr(module, "write_validated_community", serialize)
    result = module.apply(
        ".temp/stage", receipt["candidate_sha256"], receipt_sha, ".temp/restored", REVISION
    )
    assert result["applied"] is True


def test_old_descriptor_stock_and_notes_must_match(case):
    module, config, original, _ = case
    for key in ("before", "existing_descriptor", "existing_stock"):
        changed = copy.deepcopy(config)
        changed["notes"][0][key] = "wrong"
        with pytest.raises(ValueError, match="existing note, descriptor and stock"):
            module.expected_document(original, changed, "2026-11-15T08:00:00Z")
    assert module.expected_document(original, config, "2026-11-15T08:00:00Z")[1]


def test_duplicate_output_preserves_all_existing_bytes(case):
    module, _, _, _ = case
    stage(case)
    before = {
        p: (p.read_bytes(), p.stat().st_mtime_ns) for p in (module.ROOT / ".temp/stage").iterdir()
    }
    with pytest.raises(ValueError, match="exclusive"):
        stage(case)
    assert before == {p: (p.read_bytes(), p.stat().st_mtime_ns) for p in before}


def test_wrong_execution_and_plan_hash_refuse_before_output(case):
    module, _, _, _ = case
    with pytest.raises(ValueError, match="exact current revision"):
        module.stage(PLAN, module.sha((module.ROOT / PLAN).read_bytes()), ".temp/bad", "a" * 40)
    with pytest.raises(ValueError, match="input differs"):
        module.stage(PLAN, "a" * 64, ".temp/bad", REVISION)
    assert not (module.ROOT / ".temp/bad").exists()
