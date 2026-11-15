"""Exercise the fixed Wetland471 identity write and refusal boundaries; #2898."""

import copy
import importlib.util
import json
import subprocess
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
HELPER = "scripts/adhoc/curate_wetland_identity_20261115.py"
PREP = "scripts/adhoc/prepare_wetland_identity_plan_20261115.py"
PLAN = "reports/gtdb-wetland-identity-20261115/471-identity-plan-001.json"
BASE = "68699871415fda3c9eebf20382a315f9f3c7b17a"
REVISION = "0126f074d97eb795e68bbe27bc15f21468c31634"


def load(name, file):
    spec = importlib.util.spec_from_file_location(name, ROOT / file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def case(tmp_path, monkeypatch):
    module, prep = load("wetland_guard", HELPER), load("wetland_plan", PREP)
    original = subprocess.check_output(["git", "show", f"{BASE}:{module.TARGET}"], cwd=ROOT)
    assert module.sha(original) == module.BEFORE
    names = {
        HELPER,
        PREP,
        module.BASE_HELPER,
        module.TARGET,
        module.SOURCE,
        "tests/test_causal_review_batch133.py",
        "reports/causal_graph_review/decisions/20261020-stage2-fifteen-records-batch133.yaml",
        *module.capture_core.REQUIRED,
    }
    for name in names:
        output = tmp_path / name
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_bytes(original if name == module.TARGET else (ROOT / name).read_bytes())
    monkeypatch.setattr(prep, "ROOT", tmp_path)
    monkeypatch.setattr(prep, "__file__", str(tmp_path / PREP))
    config = prep.build()
    destination = tmp_path / PLAN
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(config, indent=2) + "\n")
    monkeypatch.setattr(module, "ROOT", tmp_path)
    monkeypatch.setattr(module, "__file__", str(tmp_path / HELPER))
    monkeypatch.setattr(module.capture_core, "ROOT", tmp_path)
    monkeypatch.setattr(module.capture_core, "head", lambda: REVISION)

    def serialize(document, output):
        output.write_text(yaml.safe_dump(document, sort_keys=False))

    native = module.write_validated_community
    monkeypatch.setattr(module, "write_validated_community", serialize)
    return module, config, original, serialize, native


def staged(case):
    module, _, _, _, _ = case
    receipt = module.stage(
        PLAN, module.sha((module.ROOT / PLAN).read_bytes()), ".temp/stage", REVISION
    )
    return receipt, module.sha((module.ROOT / ".temp/stage/receipt.json").read_bytes())


def test_native_positive_persistence_preserves_all_unselected_semantics(case, monkeypatch):
    module, config, original, _, native = case
    monkeypatch.setattr(module, "write_validated_community", native)
    receipt, receipt_sha = staged(case)
    candidate = (module.ROOT / ".temp/stage" / Path(module.TARGET).name).read_bytes()
    before, after = yaml.safe_load(original), yaml.safe_load(candidate)
    assert before["ecological_interactions"] == after["ecological_interactions"]
    for old, new in zip(before["taxonomy"], after["taxonomy"], strict=True):
        assert old["taxon_term"]["term"] == new["taxon_term"]["term"]
        assert (
            old["taxon_term"]["gtdb_grounding_status"] == new["taxon_term"]["gtdb_grounding_status"]
        )
        assert [e["snippet"] for e in old["evidence"]] == [e["snippet"] for e in new["evidence"]]
    assert after["curation_history"][:-1] == before["curation_history"]
    assert len(after["discussions"]) == 1
    applied = module.apply(
        ".temp/stage", receipt["candidate_sha256"], receipt_sha, ".temp/applied", REVISION
    )
    assert applied["applied"] is True
    assert (module.ROOT / module.TARGET).read_bytes() == candidate
    assert (module.ROOT / ".temp/applied/before.yaml").read_bytes() == original
    assert (module.ROOT / ".temp/applied/receipt.json").stat().st_size > 0
    assert applied["helper_sha256"] == module.sha((module.ROOT / HELPER).read_bytes())
    assert config["discussion"] == after["discussions"][0]


@pytest.mark.parametrize(
    "change", ["graph", "term", "snippet", "mapping", "history", "event", "note"]
)
def test_rehashed_undeclared_candidate_refused_then_restored(case, change):
    module, _, original, _, _ = case
    receipt, receipt_sha = staged(case)
    candidate_path = module.ROOT / ".temp/stage" / Path(module.TARGET).name
    receipt_path = module.ROOT / ".temp/stage/receipt.json"
    good, good_receipt = candidate_path.read_bytes(), receipt_path.read_bytes()
    changed = yaml.safe_load(good)
    if change == "graph":
        changed["ecological_interactions"][0]["downstream"] = []
    elif change == "term":
        changed["taxonomy"][0]["taxon_term"]["term"]["id"] = "NCBITaxon:2"
    elif change == "snippet":
        changed["taxonomy"][0]["evidence"][0]["snippet"] += " invented"
    elif change == "mapping":
        changed["taxonomy"][0]["taxon_term"]["gtdb_grounding_status"] = "GROUNDED"
    elif change == "history":
        changed["curation_history"][0]["changes"] = "rewritten"
    elif change == "event":
        changed["curation_history"][-1]["llm_assisted"] = False
    else:
        changed["taxonomy"][3]["taxon_term"]["notes"] = "new unsupported stock"
    candidate_path.write_text(yaml.safe_dump(changed, sort_keys=False))
    receipt["candidate_sha256"] = module.sha(candidate_path.read_bytes())
    receipt_path.write_text(json.dumps(receipt))
    with pytest.raises(ValueError, match="candidate differs"):
        module.apply(
            ".temp/stage",
            receipt["candidate_sha256"],
            module.sha(receipt_path.read_bytes()),
            ".temp/refused",
            REVISION,
        )
    assert (module.ROOT / module.TARGET).read_bytes() == original
    assert not (module.ROOT / ".temp/refused").exists()
    candidate_path.write_bytes(good)
    receipt_path.write_bytes(good_receipt)
    result = module.apply(".temp/stage", module.sha(good), receipt_sha, ".temp/restored", REVISION)
    assert result["applied"] is True


@pytest.mark.parametrize("which", ["source", "record", "helper", "base_helper", "plan"])
def test_changed_captured_input_during_validation_refuses_then_restores(case, monkeypatch, which):
    module, _, original, serialize, _ = case
    receipt, receipt_sha = staged(case)
    names = {
        "source": module.SOURCE,
        "record": module.TARGET,
        "helper": HELPER,
        "base_helper": module.BASE_HELPER,
        "plan": PLAN,
    }
    target = module.ROOT / names[which]
    old = target.read_bytes()

    def change(document, output):
        serialize(document, output)
        target.write_bytes(old + b"\n# changed during native validation\n")

    monkeypatch.setattr(module, "write_validated_community", change)
    with pytest.raises(ValueError, match="captured input"):
        module.apply(
            ".temp/stage", receipt["candidate_sha256"], receipt_sha, ".temp/refused", REVISION
        )
    assert not (module.ROOT / ".temp/refused/receipt.json").exists()
    if which != "record":
        assert (module.ROOT / module.TARGET).read_bytes() == original
    target.write_bytes(old)
    monkeypatch.setattr(module, "write_validated_community", serialize)
    assert module.apply(
        ".temp/stage", receipt["candidate_sha256"], receipt_sha, ".temp/restored", REVISION
    )["applied"]


@pytest.mark.parametrize(
    "which", ["duplicate_field", "extra_field", "wrong_before", "missing_evidence", "wrong_source"]
)
def test_plan_scope_and_assertion_evidence_fail_before_output(case, which):
    module, config, original, _, _ = case
    changed = copy.deepcopy(config)
    if which == "duplicate_field":
        changed["changes"][1] = changed["changes"][0]
    elif which == "extra_field":
        changed["changes"][0]["path"] = ["name"]
    elif which == "wrong_before":
        changed["changes"][0]["before"] = "wrong"
    elif which == "missing_evidence":
        changed["changes"][0]["source_anchor_indices"] = []
    else:
        changed["discussion"]["evidence"][0]["snippet"] = "invented primary quotation"
    location = module.ROOT / PLAN
    good = location.read_bytes()
    location.write_text(json.dumps(changed))
    with pytest.raises(ValueError):
        module.stage(PLAN, module.sha(location.read_bytes()), ".temp/refused", REVISION)
    assert not (module.ROOT / ".temp/refused").exists()
    assert (module.ROOT / module.TARGET).read_bytes() == original
    location.write_bytes(good)
    assert staged(case)[0]["canonical_apply"] is False


def test_plan_has_no_side_effect_and_existing_outputs_are_preserved(case):
    module, _, original, _, _ = case
    plan_sha = module.sha((module.ROOT / PLAN).read_bytes())
    assert module.stage(PLAN, plan_sha, ".temp/plan", REVISION, plan_only=True)["planned"]
    assert not (module.ROOT / ".temp/plan").exists()
    staged(case)
    preserved = {p: p.read_bytes() for p in (module.ROOT / ".temp/stage").iterdir()}
    with pytest.raises(ValueError, match="exclusive"):
        staged(case)
    assert all(p.read_bytes() == raw for p, raw in preserved.items())
    with pytest.raises(ValueError, match="revision"):
        module.stage(PLAN, plan_sha, ".temp/wrong", "a" * 40)
    assert (module.ROOT / module.TARGET).read_bytes() == original
