"""Publish only the reviewed Switchgrass successor and failed-attempt provenance.

Inputs: exact manifest002, saved full87 pair, four actual writes and history.
Output: exclusive manifest003 plus the retained attempt001 triplet. #1996/#2944,
2026-11-16. The unchanged strict core verifies all five rows; no record changes.
"""

import argparse
import json
import sys
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path

import scoped_gtdb_evidence_20261115 as captured
import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tests"))
import phase2_review_successor as strict  # noqa: E402

PRIOR = "reports/phase2-completion-20261115/scientific-successor-provenance-002.yaml"
PRIOR_SHA = "4e5077a181fd11be174c5a5ba411b7d7efd73bd27bd2203bf5b15509a333f20a"
OUTPUT = "reports/phase2-completion-20261115/scientific-successor-provenance-003.yaml"
TARGET = "kb/communities/LBNL_Switchgrass_Soil_SynCom16.yaml"
REVIEW = "reviews/structured/20261116T011931Z-switchgrass-full-source-successor/review.yaml"
REVIEW_SHA = "83d4aa59145ddd04383bb61c29f19dc73c778a6d54967bedbb3db7b97ebfba0d"
APPLY = "reports/phase2-science-20261115/applied-chain-switchgrass-locators-003/switchgrass-locators-apply-001.json"
RAW_APPLY = (
    ".temp/supplement-adoption-1996-20261115/switchgrass-locator-applied-m5-001/receipt.json"
)
APPLY_SHA = "54eead0a6475128efde3a1afb2250b7ba75ff369b1c2253a53650caeed7f2983"
SIDECAR = "history/records/LBNL_Switchgrass_Soil_SynCom16/2026-11-16T003751Z-codex-245811.yaml"
FAILED = ".temp/phase2-schema-20261115/switchgrass-full-review-build-001"
FAILED_PINS = {
    "json": "3900f45cc6349efd0625b89e6e820cff5af93a82c070c246f095d737c1d4e88a",
    "log": "935c5f7224f8089abf71c4e7605c917b9808f1eb938f2912ce9aa0fe5ec086f6",
    "exit": "4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865",
}


def prepare():
    review, inputs = captured.validate_pair(ROOT / REVIEW, REVIEW_SHA)

    def read(name, expected=None):
        path = ROOT / name
        raw = path.read_bytes()
        if expected is not None and captured.digest(raw) != expected:
            raise ValueError("pinned input differs: " + name)
        if path in inputs and inputs[path] != raw:
            raise ValueError("captured input changed: " + name)
        inputs[path] = raw
        return raw

    def artifact(name, expected=None):
        return {"path": name, "sha256": captured.digest(read(name, expected))}

    prior = yaml.safe_load(read(PRIOR, PRIOR_SHA))
    result = deepcopy(prior)
    result["created_at"] = datetime.now(timezone.utc).isoformat()
    result["recorded_revision"] = review["source"]["git_revision"]
    result["prior_manifest"] = artifact(PRIOR, PRIOR_SHA)
    result["generator"] = artifact(str(Path(__file__).relative_to(ROOT)))
    result["failed_build_attempt"] = {
        "issue": 2944,
        "executed_helper": artifact(
            "scripts/adhoc/build_switchgrass_full_review_attempt001_20261116.py",
            "c1cedb4a2aae0830edc5ad2fc9880ea853234d43642aca7172bfd9ca9221199e",
        ),
        "config": artifact(
            "reports/switchgrass-full-review-20261116/review-config-003.yaml",
            "bd331e7de26ebdf4cc055b5e6f4ab0675ec97197312210421d60ee72769e53a4",
        ),
        "raw_triplet": {
            suffix: {
                "path": f"reports/switchgrass-full-review-20261116/attempt001.{suffix}",
                "sha256": digest,
            }
            for suffix, digest in FAILED_PINS.items()
        },
        "scope": "Refused before source inspection or draft output; not an authoritative review.",
    }
    rows = [row for row in result["records"] if row["path"] == TARGET]
    if len(rows) != 1:
        raise ValueError("exactly one original Switchgrass row required")
    row = rows[0]
    row["after_sha256"] = captured.digest(read(TARGET))
    row["scientific_review"] = artifact(REVIEW, REVIEW_SHA)
    row["review_markdown"] = artifact(str(Path(REVIEW).with_name("review.md")))
    row["history_sidecars"].append(artifact(SIDECAR))
    row["curation_receipts"].append(
        {**artifact(APPLY, APPLY_SHA), "raw_path": RAW_APPLY, "raw_sha256": APPLY_SHA}
    )
    if read(APPLY, APPLY_SHA) != read(RAW_APPLY, APPLY_SHA):
        raise ValueError("public apply is not exact retained raw bytes")
    if [r for r in prior["records"] if r["path"] != TARGET] != [
        r for r in result["records"] if r["path"] != TARGET
    ]:
        raise ValueError("another scientific successor changed")
    # Retain every artifact actually used by the unchanged five-record verifier.
    for item in result["records"]:
        read(item["path"], item["after_sha256"])
        for ref in [
            item["scientific_review"],
            item["review_markdown"],
            *item["history_sidecars"],
            *item["curation_receipts"],
        ]:
            read(ref["path"], ref["sha256"])
        strict.current_record_sha256(ROOT, item["path"], item["before_sha256"], manifest=result)
    pending = {ROOT / OUTPUT: yaml.safe_dump(result, sort_keys=False).encode()}
    failure = json.loads(read(FAILED + ".json", FAILED_PINS["json"]))
    if failure["status"] != "FAILED" or failure["exit_code"] != 1:
        raise ValueError("failed attempt disposition changed")
    for suffix, expected in FAILED_PINS.items():
        name = f"reports/switchgrass-full-review-20261116/attempt001.{suffix}"
        pending[ROOT / name] = read(FAILED + "." + suffix, expected)
    captured.verify_captured(inputs)
    return inputs, pending


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    inputs, pending = prepare()
    if not args.plan:
        captured.publish(inputs, pending)
    print(
        json.dumps(
            {str(p.relative_to(ROOT)): captured.digest(raw) for p, raw in pending.items()}, indent=2
        )
    )


if __name__ == "__main__":
    main()
