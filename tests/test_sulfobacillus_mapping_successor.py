"""Actual saved mapping provenance must not waive batch53 science (#2849)."""

import copy
import json
import subprocess
from pathlib import Path

import pytest
import sulfobacillus_mapping_successor as successor
import yaml

ROOT = Path(__file__).resolve().parents[1]
BEFORE = "71160959bae2c8e3f0caf63d57452a597e29967f70faea6bec59016752b9aad4"


@pytest.fixture
def evidence(tmp_path):
    manifest = json.loads((ROOT / successor.MANIFEST).read_bytes())
    # This fixture reads the real immutable Git objects; no Git commands here
    # change the repository, and only the toy evidence files are mutated.
    git_dir = subprocess.check_output(
        ["git", "rev-parse", "--absolute-git-dir"], cwd=ROOT, text=True
    ).strip()
    (tmp_path / ".git").write_text("gitdir: " + git_dir + "\n")
    names = [
        successor.TARGET,
        *(
            manifest[key]["path"]
            for key in (
                "diagnostic_review",
                "review_markdown",
                "application_receipt",
                "history_sidecar",
                "native_recomputation",
            )
        ),
    ]
    for name in names:
        path = tmp_path / name
        path.parent.mkdir(exist_ok=True, parents=True)
        path.write_bytes((ROOT / name).read_bytes())
    return tmp_path, manifest


def verify(root, manifest):
    return successor.current_record_sha256(root, successor.TARGET, BEFORE, manifest=manifest)


def rewrite(root, artifact, document):
    path = root / artifact["path"]
    path.write_text(yaml.safe_dump(document, sort_keys=False))
    artifact["sha256"] = successor.digest(path.read_bytes())


def test_real_current_successor_and_exact_markdown(evidence):
    root, manifest = evidence
    assert verify(root, manifest) == manifest["after_sha256"]
    markdown = root / manifest["review_markdown"]["path"]
    original = markdown.read_bytes()
    markdown.write_bytes(original + b"\nInvented scientific approval\n")
    manifest["review_markdown"]["sha256"] = successor.digest(markdown.read_bytes())
    with pytest.raises(AssertionError):
        verify(root, manifest)
    markdown.write_bytes(original)
    manifest["review_markdown"]["sha256"] = successor.digest(original)
    assert verify(root, manifest) == manifest["after_sha256"]


@pytest.mark.parametrize("field", ["graph", "identity", "history", "other_mapping"])
def test_rehashed_scientific_or_historical_change_fails(evidence, field):
    root, manifest = evidence
    assert verify(root, manifest) == manifest["after_sha256"]
    path = root / successor.TARGET
    doc = yaml.safe_load(path.read_bytes())
    if field == "graph":
        doc["ecological_interactions"][0]["description"] = "Invented causal mechanism"
    elif field == "identity":
        doc["taxonomy"][6]["taxon_term"]["term"]["id"] = "NCBITaxon:2"
    elif field == "history":
        doc["curation_history"][0]["changes"] = "Rewritten old event"
    else:
        doc["taxonomy"][0]["taxon_term"]["gtdb_classification"]["total_genomes"] += 1
    path.write_text(yaml.safe_dump(doc, sort_keys=False))
    manifest["after_sha256"] = successor.digest(path.read_bytes())
    with pytest.raises(AssertionError):
        verify(root, manifest)


@pytest.mark.parametrize("key", ["application_receipt", "history_sidecar", "native_recomputation"])
def test_rehashed_public_proof_must_still_be_review_bound(evidence, key):
    root, manifest = evidence
    assert verify(root, manifest) == manifest["after_sha256"]
    proof = manifest[key]
    document = yaml.safe_load((root / proof["path"]).read_bytes())
    if key == "application_receipt":
        document["created_at"] = "2000-01-01T00:00:00Z"
    elif key == "history_sidecar":
        document["events"][0]["summary"] = "Invented replacement sidecar"
    else:
        document["result"]["total_genomes"] = 999
    rewrite(root, proof, document)
    if key == "application_receipt":
        proof["raw_sha256"] = proof["sha256"]
    with pytest.raises(AssertionError):
        verify(root, manifest)


def test_synthetic_or_wrong_scope_diagnostic_is_not_admitted(evidence):
    root, manifest = evidence
    assert verify(root, manifest) == manifest["after_sha256"]
    original = yaml.safe_load((root / manifest["diagnostic_review"]["path"]).read_bytes())
    for mutation in (
        "full_science",
        "wrong_selector",
        "wrong_receipt_path",
        "no_grounding_assessment",
    ):
        review = copy.deepcopy(original)
        if mutation == "full_science":
            review["scientific_review"] = True
        elif mutation == "wrong_selector":
            review["targets"][0]["selector"] = "ecological_interactions"
        elif mutation == "wrong_receipt_path":
            item = next(
                row
                for row in review["source"]["inputs"]
                if row["path"] == manifest["application_receipt"]["raw_path"]
            )
            item["path"] = ".temp/fabricated-receipt.json"
        else:
            review["assessments"] = [
                item for item in review["assessments"] if item["area"] != "grounding"
            ]
        rewrite(root, manifest["diagnostic_review"], review)
        with pytest.raises(AssertionError):
            verify(root, manifest)
        rewrite(root, manifest["diagnostic_review"], original)
        assert verify(root, manifest) == manifest["after_sha256"]


def test_other_record_cannot_use_the_exception(evidence):
    root, manifest = evidence
    path = root / "kb/communities/other.yaml"
    path.write_text("changed\n")
    with pytest.raises(AssertionError):
        successor.current_record_sha256(
            root, "kb/communities/other.yaml", BEFORE, manifest=manifest
        )
