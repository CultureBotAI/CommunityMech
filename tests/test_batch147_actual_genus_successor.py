"""The actual saved000552 successor passes; forged proof/biology does not (#2848)."""

import copy
import json
from pathlib import Path

import batch147_genus_successor as successor
import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(params=["CommunityMech:000552", "CommunityMech:000553"])
def actual(tmp_path, monkeypatch, request):
    path = next(path for path, values in successor.TARGETS.items() if values[0] == request.param)
    manifest = json.loads((ROOT / successor.MANIFESTS[path]).read_bytes())
    proof = next(row for row in manifest["records"] if row["target_id"] == request.param)
    original = successor.historical_bytes(ROOT, proof["target"])
    assert successor.digest(original) == proof["before_sha256"]
    monkeypatch.setattr(successor, "historical_bytes", lambda root, path: original)
    names = {proof["target"]}
    names.update(
        proof[key]["path"]
        for key in (
            "diagnostic_review",
            "review_markdown",
            "application_receipt",
            "history_sidecar",
            "native_recomputation",
        )
    )
    retained = {}
    for name in names:
        raw = (ROOT / name).read_bytes()
        path = tmp_path / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
        retained[name] = raw
    return tmp_path, copy.deepcopy(manifest), proof, retained


def check(root, manifest, proof):
    return successor.current_record_sha256(
        root, proof["target"], proof["before_sha256"], manifest=manifest
    )


def test_actual_saved_native_chain_passes(actual):
    root, manifest, proof, _raw = actual
    assert check(root, manifest, proof) == proof["after_sha256"]


def reseal_review(root, proof, review):
    raw = yaml.safe_dump(review, sort_keys=False).encode()
    (root / proof["diagnostic_review"]["path"]).write_bytes(raw)
    proof["diagnostic_review"]["sha256"] = successor.digest(raw)
    markdown = successor.render_markdown(review).encode()
    (root / proof["review_markdown"]["path"]).write_bytes(markdown)
    proof["review_markdown"]["sha256"] = successor.digest(markdown)


@pytest.mark.parametrize(
    "mutation",
    ["receipt", "sidecar", "route", "source", "scientific", "terms", "markdown", "biology"],
)
def test_rehashed_actual_proof_mutation_is_rejected_then_restores(actual, mutation):
    root, manifest, _initial, retained = actual
    proof = next(row for row in manifest["records"] if row["target_id"] == _initial["target_id"])
    before = copy.deepcopy(manifest)
    assert check(root, manifest, proof) == proof["after_sha256"]
    review = yaml.safe_load((root / proof["diagnostic_review"]["path"]).read_bytes())
    if mutation in {"receipt", "sidecar", "route", "source"}:
        key = {
            "receipt": "application_receipt",
            "sidecar": "history_sidecar",
            "route": "native_recomputation",
            "source": "native_recomputation",
        }[mutation]
        item = proof[key]
        payload = yaml.safe_load((root / item["path"]).read_bytes())
        if mutation == "receipt":
            payload["before_sha256"] = "0" * 64
        elif mutation == "sidecar":
            payload["target"]["path"] = "data/isolates/unreviewed.yaml"
        elif mutation == "route":
            payload["record_sha256"] = "0" * 64
        else:
            payload["crosswalk_sha256"] = "1" * 64
        raw = yaml.safe_dump(payload, sort_keys=False).encode()
        (root / item["path"]).write_bytes(raw)
        item["sha256"] = successor.digest(raw)
        if "raw_sha256" in item:
            item["raw_sha256"] = item["sha256"]
        raw_path = item.get("raw_path", item["path"])
        for row in review["source"]["inputs"]:
            if row["path"] == raw_path:
                row["sha256"] = item["sha256"]
        reseal_review(root, proof, review)
    elif mutation == "scientific":
        review["scientific_review"] = True
        reseal_review(root, proof, review)
    elif mutation == "terms":
        review["checks"] = [row for row in review["checks"] if row["check_id"] != "terms"]
        reseal_review(root, proof, review)
    elif mutation == "markdown":
        raw = (root / proof["review_markdown"]["path"]).read_bytes() + b"\nInvented outcome\n"
        (root / proof["review_markdown"]["path"]).write_bytes(raw)
        proof["review_markdown"]["sha256"] = successor.digest(raw)
    else:
        current = yaml.safe_load((root / proof["target"]).read_bytes())
        current["description"] += " Invented organism mechanism."
        raw = yaml.safe_dump(current).encode()
        (root / proof["target"]).write_bytes(raw)
        proof["after_sha256"] = successor.digest(raw)
    assert manifest != before or any(
        (root / name).read_bytes() != raw for name, raw in retained.items()
    )
    with pytest.raises((AssertionError, ValueError)):
        check(root, manifest, proof)
    for name, raw in retained.items():
        (root / name).write_bytes(raw)
    restored = next(row for row in before["records"] if row["target_id"] == _initial["target_id"])
    assert check(root, before, restored) == restored["after_sha256"]
