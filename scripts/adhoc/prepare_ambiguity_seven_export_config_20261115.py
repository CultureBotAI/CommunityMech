"""Assemble seven-record public proof configuration, #2848/PR2881, 2026-11-15.

Inputs: exact accepted review config, saved YAML and bound native stage receipts.
Output: one exclusive JSON config for the unchanged scoped evidence exporter.
No canonical, saved review, raw receipt or checkpoint content is modified.
"""

import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
PUBLIC = "reports/gtdb-ambiguity-eight-20261115"
CONFIG = f"{PUBLIC}/seven-review-config-001.json"
CONFIG_SHA = "b5dc409b5154d67b712755987e4ee5cc37355262c788e1868b933be8b4f5034c"
REVIEW = (
    "reviews/structured/20261115T095024Z-seven-record-reference-alternatives-diagnostic/review.yaml"
)
REVIEW_SHA = "0969d25b44b17c6956baf5838e9ac4ae405a569f0ae4d21e24a7b5295b4722bd"
REVISION = "ee9930cb145805101cc87b0a9ba188616cbf7ab8"
INDICES = {
    "400": [3],
    "499": [0, 1],
    "500": [2],
    "506": [0, 1, 2],
    "507": [0, 1, 2],
    "508": [0, 1, 2],
    "509": [0, 1, 2, 3, 4],
}


def captured(path, expected):
    raw = (ROOT / path).read_bytes()
    if hashlib.sha256(raw).hexdigest() != expected:
        raise ValueError("accepted input differs: " + path)
    return raw


def main():
    config = json.loads(captured(CONFIG, CONFIG_SHA))
    review = yaml.safe_load(captured(REVIEW, REVIEW_SHA))
    inputs = {item["path"]: item["sha256"] for item in review["source"]["inputs"]}
    if review["source"]["git_revision"] != REVISION or review["scientific_review"] is not False:
        raise ValueError("saved partial diagnostic execution differs")
    records = []
    for item in config["records"]:
        short = str(int(item["target_id"].split(":")[1]))
        stage_path = item["stage_directory"] + "/receipt.json"
        stage = json.loads(captured(stage_path, inputs[stage_path]))
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
        raise ValueError("exact seven-record order required")
    result = {
        "review": REVIEW,
        "review_sha256": REVIEW_SHA,
        "execution_revision": REVISION,
        "output_directory": PUBLIC,
        "records": records,
    }
    path = ROOT / PUBLIC / "seven-export-config-001.json"
    raw = (json.dumps(result, indent=2) + "\n").encode()
    with path.open("xb") as handle:
        handle.write(raw)
    print(
        json.dumps({"path": str(path.relative_to(ROOT)), "sha256": hashlib.sha256(raw).hexdigest()})
    )


if __name__ == "__main__":
    main()
