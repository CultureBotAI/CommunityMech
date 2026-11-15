"""Bind one database-only successor to the unchanged batch53 science (#2849).

Only the Sulfobacillus mapping and append-only inline history may differ from
the already-fetched686 baseline. An actual reviewed M5 apply, native diagnostic
and history sidecar are required; this does not replace old graph assertions.
"""

import copy
import hashlib
import subprocess
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.record_review import render_markdown, validate_review  # noqa: E402

BASELINE = "68699871415fda3c9eebf20382a315f9f3c7b17a"
TARGET = "kb/communities/Industrial_Bioreactor_Consortium.yaml"
IDENTITY = "CommunityMech:000035"
SELECTOR = "taxonomy[6].taxon_term.gtdb_classification"
MANIFEST = "reports/gtdb-source-routes-2849-20261115/sulfobacillus-successor-001.json"


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def artifact(root, item):
    path = Path(item["path"])
    assert not path.is_absolute() and ".." not in path.parts
    resolved = (root / path).resolve()
    assert resolved.is_relative_to(root.resolve())
    raw = resolved.read_bytes()
    assert digest(raw) == item["sha256"], str(path)
    return raw


def reviewed_input(review, path, expected):
    matches = [item for item in review["source"]["inputs"] if item["path"] == path]
    assert len(matches) == 1 and matches[0]["sha256"] == expected, path


def unchanged_science(before, after):
    assert before["id"] == after["id"] == IDENTITY
    previous = before["curation_history"]
    assert after["curation_history"][: len(previous)] == previous
    assert len(after["curation_history"]) == len(previous) + 1
    assert after["curation_history"][-1]["llm_assisted"] is True
    old, new = copy.deepcopy(before), copy.deepcopy(after)
    for doc in (old, new):
        doc.pop("curation_history")
        doc["taxonomy"][6]["taxon_term"].pop("gtdb_classification")
    assert (
        old == new
    ), "all source/scientific/graph content outside the one mapping must remain unchanged"
    assert after["taxonomy"][6]["taxon_term"]["term"] == {
        "id": "NCBITaxon:53633",
        "label": "Sulfobacillus acidophilus",
    }


def current_record_sha256(root, path, predecessor_hash, *, manifest=None, current=None):
    current = (root / path).read_bytes() if current is None else current
    if path != TARGET:
        assert digest(current) == predecessor_hash
        return predecessor_hash
    manifest = yaml.safe_load((root / MANIFEST).read_bytes()) if manifest is None else manifest
    assert manifest["source_baseline"] == BASELINE
    assert manifest["target"] == TARGET and manifest["target_id"] == IDENTITY
    assert manifest["scientific_review"] is False
    before_raw = subprocess.check_output(["git", "show", f"{BASELINE}:{TARGET}"], cwd=root)
    assert digest(before_raw) == predecessor_hash == manifest["before_sha256"]
    assert digest(current) == manifest["after_sha256"]
    unchanged_science(yaml.safe_load(before_raw), yaml.safe_load(current))
    review = yaml.safe_load(artifact(root, manifest["diagnostic_review"]))
    validate_review(review)
    assert review["repository"] == "CultureBotAI/CommunityMech"
    assert review["completion"] == "completed" and review["scientific_review"] is False
    assert review["verdict"] == "pass_with_limitations" and review["scope"]["coverage"] == "partial"
    assert review["scope"]["reviewed_target_ids"] == [IDENTITY]
    assert len(review["targets"]) == 1
    target = review["targets"][0]
    assert (target["path"], target["target_id"], target["selector"]) == (TARGET, IDENTITY, SELECTOR)
    reviewed_input(review, TARGET, manifest["after_sha256"])
    evidence = {row["evidence_id"]: row for row in review["evidence"]}
    assert any(
        row["area"] == "grounding"
        and row["outcome"] == "supported"
        and row["target_ids"] == [IDENTITY]
        and any(evidence[key]["kind"] == "database" for key in row["evidence_ids"])
        for row in review["assessments"]
    ), "a positive database-grounding assessment is required"
    assert {row["check_id"] for row in review["checks"] if row["required"]} == {
        "schema",
        "strict",
        "gtdb",
        "domain",
        "scalars",
        "history",
        "new-history",
    }
    assert all(
        row["status"] == "passed" and row["exit_code"] == 0
        for row in review["checks"]
        if row["required"]
    )
    proof = manifest["application_receipt"]
    assert proof["sha256"] == proof["raw_sha256"]
    reviewed_input(review, proof["raw_path"], proof["raw_sha256"])
    receipt = yaml.safe_load(artifact(root, proof))
    assert receipt["target"] == TARGET and receipt["applied"] is True
    assert receipt["before_sha256"] == predecessor_hash
    assert receipt["after_sha256"] == manifest["after_sha256"]
    assert receipt["execution_revision"] == review["source"]["git_revision"]
    for name, expected in receipt["inputs"].items():
        reviewed_input(review, name, expected)
    sidecar = manifest["history_sidecar"]
    reviewed_input(review, sidecar["path"], sidecar["sha256"])
    history = yaml.safe_load(artifact(root, sidecar))
    assert history["target"]["path"] == TARGET and history["target"]["kind"] == "record"
    assert history["events"]
    route = manifest["native_recomputation"]
    reviewed_input(review, route["raw_path"], route["sha256"])
    result = yaml.safe_load(artifact(root, route))
    assert result["target"] == TARGET and result["record_sha256"] == manifest["after_sha256"]
    assert result["revision"] == receipt["execution_revision"]
    assert result["matches_corrected_block"] is True
    block = yaml.safe_load(current)["taxonomy"][6]["taxon_term"]["gtdb_classification"]
    assert not block.get("curated")
    assert {key: block[key] for key in result["result"] if key != "via"} == {
        key: value for key, value in result["result"].items() if key != "via"
    }
    reviewed_input(review, "scripts/gtdb_ground.py", result["classifier_sha256"])
    reviewed_input(
        review,
        ".temp/gtdb-source-routes-2849-20261115/kg-microbe/data/raw/NCBI2GTDB.tsv.gz",
        result["crosswalk_sha256"],
    )
    assert artifact(root, manifest["review_markdown"]).decode() == render_markdown(review)
    return manifest["after_sha256"]
