"""Mutation controls for source-bound batch144 mapping successors (#2849)."""

import copy
import json
import subprocess
from pathlib import Path

import batch144_mapping_successor as successor
import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
BEFORE = "81c8fd983bc57050595d7a4d51b64acdf2617ce9fea0f03f7ec9db4fa617c05e"


@pytest.fixture
def evidence(tmp_path):
    manifest = json.loads(
        (
            ROOT / "reports/gtdb-source-routes-2849-20261115/terrabacter-successor-001.json"
        ).read_bytes()
    )
    entry = manifest["records"][0]
    git_dir = subprocess.check_output(
        ["git", "rev-parse", "--absolute-git-dir"], cwd=ROOT, text=True
    ).strip()
    (tmp_path / ".git").write_text("gitdir: " + git_dir + "\n")
    for name in [
        entry["target"],
        *(
            entry[key]["path"]
            for key in (
                "diagnostic_review",
                "review_markdown",
                "application_receipt",
                "history_sidecar",
                "grounding_proof",
            )
        ),
    ]:
        path = tmp_path / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes((ROOT / name).read_bytes())
    return tmp_path, manifest, entry


def verify(evidence):
    root, manifest, _entry = evidence
    return successor.current_record_sha256(root, successor.TERRABACTER, BEFORE, manifest=manifest)


def rewrite(root, artifact, document):
    path = root / artifact["path"]
    path.write_text(yaml.safe_dump(document, sort_keys=False))
    artifact["sha256"] = successor.digest(path.read_bytes())


def test_actual_mapping_chain_and_exact_markdown(evidence):
    root, _manifest, entry = evidence
    assert verify(evidence) == entry["after_sha256"]
    markdown = root / entry["review_markdown"]["path"]
    original = markdown.read_bytes()
    markdown.write_bytes(original + b"\nInvented scientific approval\n")
    entry["review_markdown"]["sha256"] = successor.digest(markdown.read_bytes())
    with pytest.raises(AssertionError):
        verify(evidence)
    markdown.write_bytes(original)
    entry["review_markdown"]["sha256"] = successor.digest(original)
    assert verify(evidence) == entry["after_sha256"]


@pytest.mark.parametrize("field", ["graph", "identity", "history", "description"])
def test_rehashed_biological_or_historical_change_fails(evidence, field):
    root, _manifest, entry = evidence
    assert verify(evidence) == entry["after_sha256"]
    path = root / successor.TERRABACTER
    original = path.read_bytes()
    doc = yaml.safe_load(original)
    if field == "graph":
        doc["ecological_interactions"][0]["description"] = "Invented mechanism"
    elif field == "identity":
        doc["taxonomy"][0]["taxon_term"]["term"]["id"] = "NCBITaxon:2"
    elif field == "history":
        doc["curation_history"][0]["changes"] = "Rewritten old event"
    else:
        doc["description"] += " Invented stock genome identity."
    path.write_text(yaml.safe_dump(doc, sort_keys=False))
    entry["after_sha256"] = successor.digest(path.read_bytes())
    with pytest.raises(AssertionError):
        verify(evidence)
    path.write_bytes(original)
    entry["after_sha256"] = successor.digest(original)
    assert verify(evidence) == entry["after_sha256"]


@pytest.mark.parametrize("key", ["application_receipt", "history_sidecar", "grounding_proof"])
def test_rehashed_proof_still_needs_saved_review_binding(evidence, key):
    root, _manifest, entry = evidence
    assert verify(evidence) == entry["after_sha256"]
    binding = entry[key]
    original = (root / binding["path"]).read_bytes()
    doc = yaml.safe_load(original)
    if key == "application_receipt":
        doc["created_at"] = "2000-01-01T00:00:00Z"
    elif key == "history_sidecar":
        doc["events"][0]["summary"] = "Invented sidecar"
    else:
        doc["result"]["total_genomes"] = 999
    rewrite(root, binding, doc)
    if key == "application_receipt":
        binding["raw_sha256"] = binding["sha256"]
    with pytest.raises(AssertionError):
        verify(evidence)
    (root / binding["path"]).write_bytes(original)
    binding["sha256"] = successor.digest(original)
    if key == "application_receipt":
        binding["raw_sha256"] = binding["sha256"]
    assert verify(evidence) == entry["after_sha256"]


def test_missing_target_proof_and_wrong_scope_refused(evidence):
    root, manifest, entry = evidence
    assert verify(evidence) == entry["after_sha256"]
    omitted = copy.deepcopy(manifest)
    omitted["records"] = []
    with pytest.raises(AssertionError):
        successor.current_record_sha256(root, successor.TERRABACTER, BEFORE, manifest=omitted)
    review = yaml.safe_load((root / entry["diagnostic_review"]["path"]).read_bytes())
    review["scientific_review"] = True
    rewrite(root, entry["diagnostic_review"], review)
    with pytest.raises(AssertionError):
        verify(evidence)


def test_br1_scope_admits_only_the_exact_description_token():
    before = yaml.safe_load(
        subprocess.check_output(["git", "show", f"{successor.BASELINE}:{successor.BR1}"], cwd=ROOT)
    )
    after = copy.deepcopy(before)
    after["description"] = after["description"].replace(
        "GTDB:s__Microbacterium_lacus", "GTDB:s__Microbacterium_sp002812725", 1
    )
    after["curation_history"].append({"action": "EDIT", "llm_assisted": True})
    successor.unchanged_science(successor.BR1, before, after)
    restored = copy.deepcopy(after)
    after["description"] += " Universal cross-feeder."
    with pytest.raises(AssertionError):
        successor.unchanged_science(successor.BR1, before, after)
    successor.unchanged_science(successor.BR1, before, restored)


def test_other_records_receive_no_hash_exception(tmp_path):
    path = "data/isolates/unrelated.yaml"
    target = tmp_path / path
    target.parent.mkdir(parents=True)
    target.write_bytes(b"unchanged")
    expected = successor.digest(target.read_bytes())
    assert successor.current_record_sha256(tmp_path, path, expected) == expected
    target.write_bytes(b"changed")
    with pytest.raises(AssertionError):
        successor.current_record_sha256(tmp_path, path, expected)


@pytest.fixture
def br1_evidence(tmp_path):
    manifest = json.loads((ROOT / successor.MANIFEST).read_bytes())
    entry = next(row for row in manifest["records"] if row["target"] == successor.BR1)
    git_dir = subprocess.check_output(
        ["git", "rev-parse", "--absolute-git-dir"], cwd=ROOT, text=True
    ).strip()
    (tmp_path / ".git").write_text("gitdir: " + git_dir + "\n")
    names = [entry["target"]] + [
        value["path"]
        for value in entry.values()
        if isinstance(value, dict) and "path" in value and "sha256" in value
    ]
    for name in names:
        path = tmp_path / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes((ROOT / name).read_bytes())
    return tmp_path, manifest, entry


@pytest.mark.parametrize("mutation", ["source_proof", "native_route", "receipt", "description"])
def test_actual_br1_chain_mutation_and_restoration(br1_evidence, mutation):
    root, manifest, entry = br1_evidence

    def check():
        return successor.current_record_sha256(
            root, successor.BR1, entry["before_sha256"], manifest=manifest
        )

    assert check() == entry["after_sha256"]
    if mutation == "description":
        path = root / entry["target"]
        original = path.read_bytes()
        document = yaml.safe_load(original)
        document["description"] += " Unreported universal interaction."
        path.write_text(yaml.safe_dump(document, sort_keys=False))
        entry["after_sha256"] = successor.digest(path.read_bytes())
        with pytest.raises(AssertionError):
            check()
        path.write_bytes(original)
        entry["after_sha256"] = successor.digest(original)
    else:
        key = {
            "source_proof": "grounding_proof",
            "native_route": "native_recomputation",
            "receipt": "application_receipt",
        }[mutation]
        binding = entry[key]
        path = root / binding["path"]
        original = path.read_bytes()
        document = yaml.safe_load(original)
        if mutation == "source_proof":
            document["assembly"]["strain"] = "Different stock"
        elif mutation == "native_route":
            document["native_result"] = {"total_genomes": 3}
        else:
            document["created_at"] = "2000-01-01T00:00:00Z"
        rewrite(root, binding, document)
        if "raw_sha256" in binding:
            binding["raw_sha256"] = binding["sha256"]
        with pytest.raises(AssertionError):
            check()
        path.write_bytes(original)
        binding["sha256"] = successor.digest(original)
        if "raw_sha256" in binding:
            binding["raw_sha256"] = binding["sha256"]
    assert check() == entry["after_sha256"]


def test_historical_batch144_ledger_is_byte_identical():
    ledger = "reports/causal_graph_review/decisions/20261108-stage2-five-records-batch144.yaml"
    original = subprocess.check_output(["git", "show", f"{successor.BASELINE}:{ledger}"], cwd=ROOT)
    assert (ROOT / ledger).read_bytes() == original
