"""The real saved review is a positive control; incomplete or wrong scope must fail (#2816)."""

import subprocess
from copy import deepcopy
from pathlib import Path

import phase2_review_successor as successor
import pytest
import yaml
from phase2_review_successor import validate_assessment

ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "reviews/structured/20261115T021628Z-phase2-lbnl-canary/review.yaml"
TARGET = "kb/communities/LBNL_Switchgrass_Soil_SynCom16.yaml"
RECORD_HASH = "aa146b5e21d2480725ed8a017372fd1dd9dc8b1e89778e7ca1f83477566845c4"


def test_actual_saved_canary_assesses_its_exact_historical_record():
    validate_assessment(yaml.safe_load(REVIEW.read_bytes()), TARGET, RECORD_HASH)


@pytest.mark.parametrize(
    "mutation",
    ["wrong_bytes", "partial", "diagnostic_only", "field_only", "unassessed", "no_primary"],
)
def test_incomplete_or_unrelated_assessment_is_not_current_acceptance(mutation):
    review = deepcopy(yaml.safe_load(REVIEW.read_bytes()))
    record_hash = RECORD_HASH
    if mutation == "wrong_bytes":
        record_hash = "0" * 64
    elif mutation == "partial":
        review["completion"] = "partial"
    elif mutation == "diagnostic_only":
        review["scientific_review"] = False
    elif mutation == "field_only":
        review["targets"][0]["selector"] = "taxonomy"
    elif mutation == "unassessed":
        review["assessments"] = []
    else:
        for row in review["evidence"]:
            if row["kind"] == "primary_source":
                row["kind"] = "diagnostic"
    with pytest.raises(AssertionError):
        validate_assessment(review, TARGET, record_hash)


@pytest.fixture
def lineage(tmp_path, monkeypatch):
    """Real canary bytes and native bundle; fixture Git identity is supplied explicitly."""
    before = successor.historical_bytes(ROOT, TARGET)
    after = subprocess.check_output(
        ["git", "show", f"6db62bda10f9ff88df9561475112f47d08d332c3:{TARGET}"], cwd=ROOT
    )
    canonical = tmp_path / TARGET
    canonical.parent.mkdir(parents=True)
    canonical.write_bytes(after)
    # Exact public copies of the two actual writes assessed by the saved canary.
    receipt_artifacts = []
    for name, raw_directory in (
        ("lbnl-source-scope", "curation-applied-001"),
        ("lbnl-mapping-note", "mapping-note-applied-001"),
    ):
        relative = f"reports/phase2-science-20261115/applied-chain-9356098c/{name}.json"
        content = (ROOT / relative).read_bytes()
        destination = tmp_path / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(content)
        receipt_artifacts.append(
            {
                "path": relative,
                "sha256": successor.digest(content),
                "raw_path": f".temp/phase2-science-20261115/{raw_directory}/receipt.json",
                "raw_sha256": successor.digest(content),
            }
        )
    artifacts = []
    for source in [
        REVIEW,
        REVIEW.with_name("review.md"),
        ROOT
        / "history/records/LBNL_Switchgrass_Soil_SynCom16/2026-11-15T021229Z-codex-948486.yaml",
    ]:
        destination = tmp_path / source.relative_to(ROOT)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(source.read_bytes())
        artifacts.append(
            {"path": str(source.relative_to(ROOT)), "sha256": successor.digest(source.read_bytes())}
        )
    manifest = {
        "source_baseline": successor.BASELINE,
        "independent_approval": False,
        "records": [
            {
                "id": "CommunityMech:000087",
                "path": TARGET,
                "before_sha256": successor.digest(before),
                "after_sha256": successor.digest(after),
                "scientific_review": artifacts[0],
                "review_markdown": artifacts[1],
                "history_sidecars": [artifacts[2]],
                "curation_receipts": receipt_artifacts,
            }
        ],
    }
    monkeypatch.setattr(successor, "TARGETS", {TARGET: "CommunityMech:000087"})
    monkeypatch.setattr(successor, "historical_bytes", lambda root, path: before)
    return tmp_path, manifest


def test_real_canary_record_review_markdown_and_history_form_a_bound_successor(lineage):
    root, manifest = lineage
    row = manifest["records"][0]
    assert (
        successor.current_record_sha256(root, TARGET, row["before_sha256"], manifest=manifest)
        == RECORD_HASH
    )


@pytest.mark.parametrize(
    "mutation",
    [
        "record",
        "review",
        "markdown",
        "history",
        "baseline",
        "rehash_record",
        "receipt",
        "rehash_history",
        "rehash_receipt",
        "unreviewed_receipt_path",
        "synthetic_receipt",
    ],
)
def test_broken_successor_evidence_cannot_be_promoted(lineage, mutation):
    root, manifest = lineage
    row = manifest["records"][0]
    if mutation == "baseline":
        row["before_sha256"] = "0" * 64
    elif mutation in {"record", "rehash_record"}:
        path = root / TARGET
        path.write_bytes(path.read_bytes() + b"\n# unreviewed mutation\n")
        if mutation == "rehash_record":
            row["after_sha256"] = successor.digest(path.read_bytes())
    elif mutation == "unreviewed_receipt_path":
        row["curation_receipts"][0]["raw_path"] = ".temp/unreviewed/receipt.json"
    elif mutation == "synthetic_receipt":
        artifact = row["curation_receipts"][0]
        path = root / artifact["path"]
        path.write_text(
            yaml.safe_dump(
                {
                    "target": TARGET,
                    "before_sha256": row["before_sha256"],
                    "after_sha256": row["after_sha256"],
                    "applied": True,
                }
            )
        )
        artifact["sha256"] = artifact["raw_sha256"] = successor.digest(path.read_bytes())
        row["curation_receipts"] = [artifact]
    else:
        artifact = {
            "review": row["scientific_review"],
            "markdown": row["review_markdown"],
            "history": row["history_sidecars"][0],
            "receipt": row["curation_receipts"][0],
            "rehash_history": row["history_sidecars"][0],
            "rehash_receipt": row["curation_receipts"][0],
        }[mutation]
        path = root / artifact["path"]
        path.write_bytes(path.read_bytes() + b"\n# changed saved artifact\n")
        if mutation.startswith("rehash_"):
            artifact["sha256"] = successor.digest(path.read_bytes())
            if mutation == "rehash_receipt":
                artifact["raw_sha256"] = artifact["sha256"]
    with pytest.raises(AssertionError):
        successor.current_record_sha256(root, TARGET, row["before_sha256"], manifest=manifest)
