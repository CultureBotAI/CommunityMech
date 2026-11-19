"""Assemble four-record public evidence configuration, PR2896, 2026-11-15.

Inputs: accepted review config, externally pinned saved YAML and native receipts.
Output: exclusive configuration for the unchanged scoped exporter. No curation.
"""

import argparse
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
PUBLIC = "reports/gtdb-ambiguity-five-20261115"
CONFIG = f"{PUBLIC}/four-review-config-001.json"
CONFIG_SHA = "e8c9989407d959ae3ce3277f919049a867f94d612957b4aa2b95a37c14ed9b71"
REVIEW = (
    "reviews/structured/20261115T120728Z-four-record-complete-reference-alternatives-diagnostic/"
    "review.yaml"
)
REVISION = "b195783da416b4be119edbb442d5b19dabe32ed4"
INDICES = {"425": [2], "460": [1], "446": [1], "412": [0]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--review-sha256", required=True)
    args = parser.parse_args()
    captured = {}

    def read(name, expected):
        path = ROOT / name
        if path.is_symlink() or not path.resolve().is_relative_to(ROOT):
            raise ValueError("unsafe captured path")
        raw = path.read_bytes()
        if hashlib.sha256(raw).hexdigest() != expected:
            raise ValueError("accepted input differs: " + name)
        if path in captured and captured[path] != raw:
            raise ValueError("input changed between reads: " + name)
        captured[path] = raw
        return raw

    config = json.loads(read(CONFIG, CONFIG_SHA))
    review = yaml.safe_load(read(REVIEW, args.review_sha256))
    inputs = {item["path"]: item["sha256"] for item in review["source"]["inputs"]}
    if (
        review["source"]["git_revision"] != REVISION
        or review["scientific_review"] is not False
        or review["scope"]["coverage"] != "partial"
        or review["completion"] != "completed"
        or review["verdict"] != "pass_with_limitations"
    ):
        raise ValueError("saved partial diagnostic differs")
    records = []
    for item in config["records"]:
        short = str(int(item["target_id"].split(":")[1]))
        stage_path = item["stage_directory"] + "/receipt.json"
        stage = json.loads(read(stage_path, inputs[stage_path]))
        if (
            stage["target"] != item["target"]
            or stage["target_id"] != item["target_id"]
            or stage["candidate_sha256"] != item["after_sha256"]
            or stage["before_sha256"] != item["before_sha256"]
            or stage["code_revision"] != REVISION
        ):
            raise ValueError("accepted native stage differs: " + short)
        records.append(
            {
                "prefix": short + "-001",
                "target": item["target"],
                "target_id": item["target_id"],
                "before_sha256": item["before_sha256"],
                "after_sha256": item["after_sha256"],
                "application_receipt": item["application_receipt"],
                "source_proof": item["source_metadata_output"],
                "history_sidecar": item["history_sidecar"],
                "history_directory": str(Path(item["history_sidecar"]).parent),
                "mutable_taxonomy_indices": INDICES[short],
                "appended_inline_events": stage["appended_native_inline_history"],
                "gates": {
                    gate: {
                        "directory": directory,
                        "check_id": item["target_id"].split(":")[1] + "-" + gate,
                    }
                    for gate, directory in item["gates"].items()
                },
            }
        )
    if [str(int(row["target_id"].split(":")[1])) for row in records] != list(INDICES):
        raise ValueError("exact four-record order required")
    result = {
        "review": REVIEW,
        "review_sha256": args.review_sha256,
        "execution_revision": REVISION,
        "output_directory": PUBLIC,
        "records": records,
    }
    for path, raw in captured.items():
        if path.is_symlink() or path.read_bytes() != raw:
            raise ValueError("captured input changed before output")
    path = ROOT / PUBLIC / "four-export-config-001.json"
    raw = (json.dumps(result, indent=2) + "\n").encode()
    with path.open("xb") as handle:
        handle.write(raw)
    if path.read_bytes() != raw:
        raise ValueError("output did not persist exact bytes")
    print(
        json.dumps({"path": str(path.relative_to(ROOT)), "sha256": hashlib.sha256(raw).hexdigest()})
    )


if __name__ == "__main__":
    main()
