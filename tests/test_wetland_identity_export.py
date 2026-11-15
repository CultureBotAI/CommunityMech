"""Fixed identity export scope and captured publication controls; #2898, 2026-11-15."""

import copy
import importlib.util
import json
from pathlib import Path

import pytest


@pytest.fixture
def exporter(monkeypatch):
    root = Path(__file__).resolve().parents[1]
    monkeypatch.syspath_prepend(str(root / "scripts/adhoc"))
    spec = importlib.util.spec_from_file_location(
        "wetland_export_test", root / "scripts/adhoc/export_wetland_identity_evidence_20261115.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    config = json.loads((root / module.CONFIG).read_bytes())
    assert module.audit.digest((root / module.CONFIG).read_bytes()) == module.CONFIG_SHA
    review = config["review"]
    review["source"] = {"git_revision": module.diagnostic.REVISION}
    review["checks"] = [
        {"check_id": "000471-" + gate, "status": "passed", "required": True, "exit_code": 0}
        for gate in (*module.shared.RECIPES, "references", "reference-measurement")
    ]
    return module, review


def test_exact_partial_identity_verdict_and_blockers(exporter):
    module, review = exporter
    module.verify_review(review)


@pytest.mark.parametrize(
    "mutation",
    [
        "scientific",
        "verdict",
        "completion",
        "scope",
        "population",
        "target",
        "findings",
        "checks",
        "exit",
        "revision",
    ],
)
def test_identity_export_scope_refuses_and_restores(exporter, mutation):
    module, review = exporter
    changed = copy.deepcopy(review)
    if mutation == "scientific":
        changed["scientific_review"] = True
    elif mutation == "verdict":
        changed["verdict"] = "pass_with_limitations"
    elif mutation == "completion":
        changed["completion"] = "partial"
    elif mutation == "scope":
        changed["scope"]["coverage"] = "full"
    elif mutation == "population":
        changed["scope"]["population_size"] = 2
    elif mutation == "target":
        changed["targets"][0]["target_id"] = "CommunityMech:000001"
    elif mutation == "findings":
        changed["findings"][0]["status"] = "resolved"
    elif mutation == "checks":
        changed["checks"][-1] = copy.deepcopy(changed["checks"][0])
    elif mutation == "exit":
        changed["checks"][-1]["exit_code"] = 1
    else:
        changed["source"]["git_revision"] = "0" * 40
    with pytest.raises(ValueError, match="exact partial identity review"):
        module.verify_review(changed)
    module.verify_review(review)


def test_captured_publication_refuses_changed_input_then_restores(exporter, tmp_path, monkeypatch):
    module, _ = exporter
    monkeypatch.setattr(module.audit, "ROOT", tmp_path)
    source = tmp_path / "raw-receipt.json"
    original = b'{"applied":true,"scope":"identity-only"}\n'
    source.write_bytes(original)
    captured = {source: original}
    destination = tmp_path / "reports/public-receipt.json"
    source.write_bytes(b'{"applied":false}\n')
    module.shared.capture_additional(captured, [source])
    assert captured[source] == original
    with pytest.raises(ValueError, match="captured input changed"):
        module.audit.publish(captured, {destination: captured[source]})
    assert not destination.exists()
    source.write_bytes(original)
    module.audit.publish(captured, {destination: captured[source]})
    assert destination.read_bytes() == original
    with pytest.raises(ValueError, match="exclusive"):
        module.audit.publish(captured, {destination: captured[source]})
