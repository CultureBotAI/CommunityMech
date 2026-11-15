"""Exercise actual shared-engine proofs and rehashed tampering (#2848).

SCOPED_GTDB_PROOF_ROOT optionally selects its published sibling checkout during
pre-integration development; CI/default uses this repository. Tests copy only
public artifacts into isolated fixtures and never edit the actual evidence.
SCOPED_GTDB_PROOF_CASES selects explicit comma-separated cases during isolated
development. All four integrated actual proofs run by default.
"""

import copy
import json
import os
import subprocess
from pathlib import Path

import pytest
import scoped_gtdb_successor as successor
import yaml

ROOT = Path(__file__).resolve().parents[1]
PROOF_ROOT = Path(os.environ.get("SCOPED_GTDB_PROOF_ROOT", ROOT)).resolve()
BASE = "68699871415fda3c9eebf20382a315f9f3c7b17a"
CASES = {
    "554": (
        "reports/gtdb-species-status-20261115/yljm2c-001-successor.json",
        "606093a26fbbcbbfb03e1992f971507f2bc06a591cf9747eca1476234afe4a11",
        True,
    ),
    "340": (
        "reports/gtdb-code006-20261115/pes-001-successor.json",
        "b44e7040e1bdeacedc63cdb8f45ab4546c30327e357e8c58a0758acfa790c47f",
        True,
    ),
    "401": (
        "reports/gtdb-ambiguity-20261115/status401-001-successor.json",
        "053aecc46719cab2cc0afe6925a3e93729a51f7febb0eeade57cccf6e3632f2a",
        False,
    ),
    "388": (
        "reports/gtdb-species-status-20261115/next-ten-388-001-successor.json",
        "b810a33b29abba9f4c5e511ec7d946f5b9e0ce1679253373377925cafb726454",
        True,
    ),
}
SELECTED = os.environ.get("SCOPED_GTDB_PROOF_CASES", "554,340,401,388").split(",")
assert (
    SELECTED and len(set(SELECTED)) == len(SELECTED) and all(case in CASES for case in SELECTED)
), "explicit known proof cases required"


@pytest.fixture(params=SELECTED, ids=SELECTED)
def actual(tmp_path, monkeypatch, request):
    manifest, manifest_sha, historical_llm = CASES[request.param]
    raw_manifest = (PROOF_ROOT / manifest).read_bytes()
    assert successor.digest(raw_manifest) == manifest_sha
    proof = json.loads(raw_manifest)
    names = {manifest, proof["target"]}
    names.update(
        proof[key]["path"]
        for key in (
            "diagnostic_review",
            "review_markdown",
            "application_receipt",
            "native_recomputation",
            "history_sidecar",
        )
    )
    for gate in proof["check_evidence"].values():
        names.update(gate[key]["path"] for key in ("receipt", "log", "exit"))
    retained = {name: (PROOF_ROOT / name).read_bytes() for name in names}
    for name, raw in retained.items():
        destination = tmp_path / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(raw)
    git = subprocess.check_output

    def historical(command, *, cwd, **kwargs):
        assert command == ["git", "show", f"{BASE}:{proof['target']}"]
        assert Path(cwd) == tmp_path
        return git(command, cwd=PROOF_ROOT, **kwargs)

    monkeypatch.setattr(successor.subprocess, "check_output", historical)
    allowance = {
        proof["target"]: {
            "baseline_revision": BASE,
            "manifest": {"path": manifest, "sha256": manifest_sha},
        }
    }
    return tmp_path, proof, allowance, retained, historical_llm


def check(actual):
    root, proof, allowed, _retained, _historical_llm = actual
    return successor.admit(root, proof["target"], proof["before_sha256"], allowed)


def write(root, item, payload):
    raw = (json.dumps(payload, indent=2) + "\n").encode()
    (root / item["path"]).write_bytes(raw)
    item["sha256"] = successor.digest(raw)
    return item["sha256"]


def reseal_review(root, proof, review):
    raw = yaml.safe_dump(review, sort_keys=False).encode()
    (root / proof["diagnostic_review"]["path"]).write_bytes(raw)
    proof["diagnostic_review"]["sha256"] = successor.digest(raw)
    markdown = successor.render_markdown(review).encode()
    (root / proof["review_markdown"]["path"]).write_bytes(markdown)
    proof["review_markdown"]["sha256"] = successor.digest(markdown)


def replace_review_hash(review, path, value):
    matches = [row for row in review["source"]["inputs"] if row["path"] == path]
    assert len(matches) == 1
    matches[0]["sha256"] = value


def test_actual_shared_engine_successor_admits_and_retains_old_history(actual):
    root, proof, allowed, _retained, historical_llm = actual
    result = check(actual)
    assert result.changed and result.current_sha256 == proof["after_sha256"]
    assert successor.digest(result.historical_bytes) == proof["before_sha256"]
    historical = successor.historical_document(
        root, proof["target"], proof["before_sha256"], allowed
    )
    if historical_llm:
        assert historical["curation_history"][-1]["llm_assisted"] is True
    assert (
        yaml.safe_load((root / proof["target"]).read_bytes())["curation_history"][-1]["curator"]
        == "gtdb_ground.py"
    )


@pytest.mark.parametrize(
    "mutation",
    [
        "manifest_pin",
        "receipt",
        "source_result",
        "source_reference",
        "missing_gate",
        "gate_plan",
        "gate_target",
        "gate_log",
        "gate_raw_mapping",
        "scientific",
        "unbound_helper",
        "markdown",
        "biology",
        "history_receipt_path",
        "history_receipt_hash",
    ],
)
def test_actual_rehashed_tampering_refuses_and_restores(actual, mutation):
    root, proof, allowed, retained, _historical_llm = actual
    manifest = allowed[proof["target"]]["manifest"]["path"]
    manifest_sha = allowed[proof["target"]]["manifest"]["sha256"]
    assert check(actual).changed
    original = copy.deepcopy(proof)
    review = yaml.safe_load((root / proof["diagnostic_review"]["path"]).read_bytes())
    if mutation in {"receipt", "source_result", "source_reference"}:
        key = "application_receipt" if mutation == "receipt" else "native_recomputation"
        item = proof[key]
        payload = json.loads((root / item["path"]).read_bytes())
        if mutation == "receipt":
            payload["before_sha256"] = "0" * 64
        elif mutation == "source_result":
            result = payload["occurrences"][0]["native_result"]
            if result.get("ambiguous"):
                assert len(result["gtdb_options"]) > 1
                result["gtdb_options"].pop()
            else:
                result["total_genomes"] += 1
        else:
            payload["occurrences"][0]["native_result"]["ncbi_source_id"] = "NCBITaxon:2"
        new_hash = write(root, item, payload)
        item["raw_sha256"] = new_hash
        replace_review_hash(review, item["raw_path"], new_hash)
        if key == "native_recomputation":
            proof["grounding_evidence"]["sha256"] = new_hash
        reseal_review(root, proof, review)
    elif mutation.startswith("history_receipt_"):
        item = proof["history_sidecar"]
        history = yaml.safe_load((root / item["path"]).read_bytes())
        details = history["events"][0]["details"]
        old = proof["application_receipt"][
            "raw_path" if mutation.endswith("path") else "raw_sha256"
        ]
        replacement = ".temp/unreviewed/receipt.json" if mutation.endswith("path") else "0" * 64
        assert details.count(old) == 1
        history["events"][0]["details"] = details.replace(old, replacement)
        raw = yaml.safe_dump(history, sort_keys=False).encode()
        (root / item["path"]).write_bytes(raw)
        item["sha256"] = successor.digest(raw)
        replace_review_hash(review, item["path"], item["sha256"])
        reseal_review(root, proof, review)
    elif mutation == "missing_gate":
        del proof["check_evidence"]["terms"]
    elif mutation.startswith("gate_"):
        gate = proof["check_evidence"]["schema"]
        receipt = json.loads((root / gate["receipt"]["path"]).read_bytes())
        if mutation == "gate_plan":
            receipt["plan"] = True
        elif mutation == "gate_target":
            names = [name for name in receipt["inputs"] if name.endswith("/" + proof["target"])]
            assert len(names) == 1
            receipt["inputs"][names[0]] = "0" * 64
        elif mutation == "gate_raw_mapping":
            gate["log"]["raw_sha256"] = "0" * 64
        else:
            path = root / gate["log"]["path"]
            path.write_bytes(path.read_bytes() + b"Unreviewed output\n")
            gate["log"]["sha256"] = successor.digest(path.read_bytes())
        write(root, gate["receipt"], receipt)
    elif mutation in {"scientific", "unbound_helper"}:
        if mutation == "scientific":
            review["scientific_review"] = True
        else:
            review["source"]["inputs"] = [
                row for row in review["source"]["inputs"] if row["path"] != successor.ENGINE
            ]
        reseal_review(root, proof, review)
    elif mutation == "markdown":
        item = proof["review_markdown"]
        raw = (root / item["path"]).read_bytes() + b"\nInvented approval\n"
        (root / item["path"]).write_bytes(raw)
        item["sha256"] = successor.digest(raw)
    elif mutation == "biology":
        path = root / proof["target"]
        document = yaml.safe_load(path.read_bytes())
        document["description"] += " Invented mechanism."
        raw = yaml.safe_dump(document).encode()
        path.write_bytes(raw)
        proof["after_sha256"] = successor.digest(raw)
    else:
        proof["scope"] += " Unreviewed approval."
    assert proof != original or any(
        (root / name).read_bytes() != raw for name, raw in retained.items()
    )
    new_manifest = (json.dumps(proof, indent=2) + "\n").encode()
    (root / manifest).write_bytes(new_manifest)
    if mutation != "manifest_pin":
        allowed[proof["target"]]["manifest"]["sha256"] = successor.digest(new_manifest)
    expected_message = "history receipt link" if mutation.startswith("history_receipt_") else None
    with pytest.raises((AssertionError, ValueError), match=expected_message):
        check(actual)
    for name, raw in retained.items():
        (root / name).write_bytes(raw)
    proof.clear()
    proof.update(original)
    allowed[proof["target"]]["manifest"]["sha256"] = manifest_sha
    assert check(actual).changed
