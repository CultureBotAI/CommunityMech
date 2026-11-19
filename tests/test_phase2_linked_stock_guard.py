"""Exercise real guarded application on private fixture copies, #2806."""

import importlib
import json
import shutil
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts/adhoc"))
driver = importlib.import_module("curate_phase2_linked_stocks_20261115")


@pytest.fixture
def prepared(tmp_path, monkeypatch):
    state = tmp_path / ".temp/phase2-science-20261115"
    state.mkdir(parents=True)
    targets, inputs = {}, {}
    for key, (relative, _, identifier) in driver.TARGETS.items():
        target = tmp_path / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / relative, target)
        raw = target.read_bytes()
        targets[key] = (relative, driver.digest(raw), identifier)
        if key == "lbnl":
            continue
        doc = driver.load_document(raw)
        # Controlled diagnostic fixtures exercise write safety, not source truth.
        # They deliberately require no ignored evidence or ontology installation.
        rows = []
        for item in doc["taxonomy"]:
            strain = item["strain_designation"]["strain_name"]
            rows.append(
                {
                    "strain": strain,
                    "stored_numeric_core_reproduced": True,
                    "stored_candidates_reproduced": True,
                    "verified_genus_term": {"id": "NCBITaxon:1663", "label": "Arthrobacter"},
                    "native_current_label_grounding": {
                        "ambiguous": True,
                        "gtdb_options": ["GTDB:g__Arthrobacter", "GTDB:g__Arthrobacter_B"],
                    },
                }
            )
        proof = {
            "record": {"sha256": driver.digest(raw)},
            "crosswalk": {"sha256": driver.MAPPING_HASH},
            "rows": rows,
        }
        name = f"linked-{key}-grounding-001.json"
        (state / name).write_text(json.dumps(proof))
        inputs[name] = driver.digest((state / name).read_bytes())
    primary = state / "lbnl-retained/ecofab-relations/PMC9765266.xml"
    primary.parent.mkdir(parents=True)
    primary.write_text("<test-fixture>source binding only</test-fixture>\n")
    inputs[str(primary.relative_to(state))] = driver.digest(primary.read_bytes())
    monkeypatch.setattr(driver, "ROOT", tmp_path)
    monkeypatch.setattr(driver, "STATE", state)
    monkeypatch.setattr(driver, "TARGETS", targets)
    monkeypatch.setattr(driver, "INPUTS", inputs)
    plan = state / "plan"
    driver.plan(plan)
    originals = {name: (tmp_path / row[0]).read_bytes() for name, row in driver.TARGETS.items()}
    return tmp_path, state, plan, originals


def assert_unchanged(root, originals):
    assert all(
        (root / driver.TARGETS[name][0]).read_bytes() == raw for name, raw in originals.items()
    )


def test_real_single_target_control_preserves_other_members(prepared):
    root, _, plan, originals = prepared
    driver.apply(plan, "ecofab")
    assert (root / driver.TARGETS["ecofab"][0]).read_bytes() == (
        plan / "ecofab/candidate.yaml"
    ).read_bytes()
    assert all(
        (root / driver.TARGETS[name][0]).read_bytes() == originals[name]
        for name in ("dopamine", "lbnl")
    )
    receipt = json.loads((plan / "ecofab/apply/receipt.json").read_text())
    assert receipt["history_sidecar_required"] is True
    after = driver.load_document((root / driver.TARGETS["ecofab"][0]).read_bytes())
    assert after["curation_history"][-1]["llm_assisted"] is True


def test_changed_peer_refuses_before_target_write(prepared):
    root, _, plan, originals = prepared
    peer = root / driver.TARGETS["lbnl"][0]
    peer.write_bytes(originals["lbnl"] + b"\n")
    originals["lbnl"] = peer.read_bytes()
    with pytest.raises(ValueError, match="concurrent cohort change"):
        driver.apply(plan, "ecofab")
    assert_unchanged(root, originals)


def test_changed_primary_refuses_before_target_write(prepared):
    root, state, plan, originals = prepared
    primary = state / "lbnl-retained/ecofab-relations/PMC9765266.xml"
    primary.write_bytes(primary.read_bytes() + b"\n")
    with pytest.raises(ValueError, match="source input changed"):
        driver.apply(plan, "ecofab")
    assert_unchanged(root, originals)


def test_candidate_and_matching_manifest_hash_cannot_expand_scope(prepared):
    root, _, plan, originals = prepared
    candidate = plan / "ecofab/candidate.yaml"
    raw = candidate.read_bytes().replace(b"name: EcoFAB 2.0", b"name: Unreviewed EcoFAB 2.0", 1)
    assert raw != candidate.read_bytes()
    candidate.write_bytes(raw)
    receipt_path = plan / "receipt.json"
    receipt = json.loads(receipt_path.read_text())
    receipt["targets"]["ecofab"]["after_sha256"] = driver.digest(raw)
    receipt_path.write_text(json.dumps(receipt))
    with pytest.raises(ValueError, match="bounded source-backed reconstruction"):
        driver.apply(plan, "ecofab")
    assert_unchanged(root, originals)


def test_peer_change_during_native_validation_is_detected(prepared, monkeypatch):
    root, _, plan, originals = prepared
    native = driver.write_validated_community
    peer = root / driver.TARGETS["dopamine"][0]

    def changed(doc, path):
        native(doc, path)
        peer.write_bytes(originals["dopamine"] + b"\n")

    monkeypatch.setattr(driver, "write_validated_community", changed)
    with pytest.raises(ValueError, match="cohort changed during native revalidation"):
        driver.apply(plan, "ecofab")
    assert (root / driver.TARGETS["ecofab"][0]).read_bytes() == originals["ecofab"]
    assert (root / driver.TARGETS["lbnl"][0]).read_bytes() == originals["lbnl"]
