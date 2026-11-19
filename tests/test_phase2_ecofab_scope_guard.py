"""Actual apply-path controls for the source-reviewed EcoFAB correction."""

import copy
import importlib
import json
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
FIXTURE_REVISION = "17616c9cad16a1b62cd6e9b39d82af4276e5188a"
sys.path.insert(0, str(ROOT / "scripts/adhoc"))
driver = importlib.import_module("curate_phase2_ecofab_scope_20261115")


@pytest.fixture
def prepared(tmp_path, monkeypatch):
    """Test real dispatch/guards with a bounded fixture, not fabricated science."""
    state = tmp_path / ".temp/phase2-science-20261115"
    state.mkdir(parents=True)
    for path in [driver.TARGET, *driver.PEERS]:
        destination = tmp_path / path
        destination.parent.mkdir(parents=True, exist_ok=True)
        # #2823: the guarded writer deliberately accepts the reviewed predecessor,
        # not whichever successor is current when the test suite runs. This public
        # review base is retained by the repository's native historical-input fetch.
        destination.write_bytes(
            subprocess.check_output(["git", "show", FIXTURE_REVISION + ":" + path], cwd=ROOT)
        )
    source = state / "source.xml"
    source.write_text("<fixture>guard binding only</fixture>\n")
    monkeypatch.setattr(driver, "ROOT", tmp_path)
    monkeypatch.setattr(driver, "STATE", state)
    monkeypatch.setattr(driver, "SOURCES", {"source.xml": driver.digest(source.read_bytes())})
    monkeypatch.setattr(driver, "read_sources", lambda: ("fixture source", {"fixture": "row"}))

    def bounded_build(original, _text, _rows, timestamp=None):
        before = driver.load_document(original)
        after = copy.deepcopy(before)
        after["description"] += " Guard fixture only."
        event = driver.record_curation_event(
            after,
            curator="codex",
            action="EDIT",
            changes="Guard fixture only.",
            llm_assisted=True,
            **({"timestamp": timestamp} if timestamp else {}),
        )
        text = yaml.safe_dump(after, sort_keys=False, allow_unicode=True)
        return before, after, text, event

    monkeypatch.setattr(driver, "build", bounded_build)
    plan = state / "plan"
    driver.plan(plan)
    originals = {path: (tmp_path / path).read_bytes() for path in [driver.TARGET, *driver.PEERS]}
    return tmp_path, state, plan, originals


def test_native_apply_control_only_changes_authorized_target(prepared):
    root, _, plan, originals = prepared
    driver.apply(plan)
    assert (root / driver.TARGET).read_bytes() == (plan / "candidate.yaml").read_bytes()
    assert all((root / peer).read_bytes() == originals[peer] for peer in driver.PEERS)
    record = driver.load_document((root / driver.TARGET).read_bytes())
    assert record["curation_history"][-1]["llm_assisted"] is True
    receipt = json.loads((plan / "apply/receipt.json").read_text())
    assert receipt["history_sidecar_required"] is True


def test_changed_source_rejects_before_write(prepared):
    root, state, plan, originals = prepared
    (state / "source.xml").write_text("changed source")
    with pytest.raises(ValueError, match="primary source changed"):
        driver.apply(plan)
    assert (root / driver.TARGET).read_bytes() == originals[driver.TARGET]


def test_changed_peer_rejects_before_write(prepared):
    root, _, plan, originals = prepared
    peer = next(iter(driver.PEERS))
    (root / peer).write_bytes(originals[peer] + b"\n")
    with pytest.raises(ValueError, match="related scientific input changed"):
        driver.apply(plan)
    assert (root / driver.TARGET).read_bytes() == originals[driver.TARGET]


def test_candidate_and_receipt_forgery_cannot_expand_scope(prepared):
    root, _, plan, originals = prepared
    path = plan / "candidate.yaml"
    path.write_bytes(path.read_bytes() + b"# injected change\n")
    receipt_path = plan / "receipt.json"
    receipt = json.loads(receipt_path.read_text())
    receipt["after_sha256"] = driver.digest(path.read_bytes())
    receipt_path.write_text(json.dumps(receipt))
    with pytest.raises(ValueError, match="bounded source reconstruction"):
        driver.apply(plan)
    assert (root / driver.TARGET).read_bytes() == originals[driver.TARGET]


def test_concurrent_target_change_during_native_validation_rejects(prepared, monkeypatch):
    root, _, plan, originals = prepared
    native = driver.write_validated_community
    target = root / driver.TARGET

    def competing_writer(record, path):
        native(record, path)
        target.write_bytes(originals[driver.TARGET] + b"# competing change\n")

    monkeypatch.setattr(driver, "write_validated_community", competing_writer)
    with pytest.raises(ValueError, match="canonical changed before replacement"):
        driver.apply(plan)
    assert target.read_bytes() == originals[driver.TARGET] + b"# competing change\n"
    assert not (plan / "apply/receipt.json").exists()
