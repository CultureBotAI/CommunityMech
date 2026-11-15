"""Add exact correction-provenance inputs to a new native diagnostic, 2026-11-15.

#2892: read a pinned config and retained issue/review bytes, invoke the unchanged
builder, then reinspect its complete capture plus those additional inputs.
Write only a fresh private draft and the builder's fresh source metadata. Never
edit saved reviews, canonical records, native gates or the executed builder.
"""

import argparse
import json
import re
from pathlib import Path

import build_gtdb_batch_diagnostic_20261115 as builder

core = builder.core
BUILDER_SHA = "c6bf0d09dc3d01797ab5d956a4f7458a9a153a8704508f50e656729e4ee1b860"


def build(config_name, config_sha, output_name, revision, wrapper_sha):
    output = core.path(output_name, private=True)
    if output.exists() or core.head() != revision:
        raise ValueError("exclusive private output and exact revision required")
    captured = {}
    config_raw = core.capture(captured, config_name, config_sha)
    config = json.loads(config_raw)
    core.capture(captured, str(Path(__file__).relative_to(core.ROOT)), wrapper_sha)
    core.capture(captured, str(Path(builder.__file__).relative_to(core.ROOT)), BUILDER_SHA)
    additions = config["additional_review_inputs"]
    if not isinstance(additions, dict) or not 1 <= len(additions) <= 32:
        raise ValueError("one to 32 explicit provenance inputs required")
    for name, expected in additions.items():
        if (
            not name.startswith((".temp/", "reviews/structured/", "reports/"))
            or not isinstance(expected, str)
            or not re.fullmatch(r"[0-9a-f]{64}", expected)
        ):
            raise ValueError("exact retained provenance paths and SHA256 values required")
        core.capture(captured, name, expected)
    core.unchanged(captured, revision)
    output.mkdir(parents=True)
    base_name = str((output / "base-draft").relative_to(core.ROOT))
    result = builder.build(config_name, config_sha, base_name, revision)
    if result["review"] != base_name + "/review.json":
        raise ValueError("unexpected builder draft path")
    review = json.loads(core.capture(captured, result["review"], result["sha256"]))
    for item in review["source"]["inputs"]:
        core.capture(captured, item["path"], item["sha256"])
    core.capture(captured, base_name + "/inspection.json")
    core.unchanged(captured, revision)
    native = builder.native_review()
    inspection = native.inspect_source(
        core.ROOT,
        review["targets"],
        [str(path.relative_to(core.ROOT)) for path in captured],
    )
    builder.verify_inspection(inspection, captured, revision)
    review["source"] = inspection["source"]
    review["finished_at"] = builder.now()
    native.validate_review(review)
    core.unchanged(captured, revision)
    for name, document in (("inspection.json", inspection), ("review.json", review)):
        raw = (json.dumps(document, indent=2) + "\n").encode()
        destination = output / name
        with destination.open("xb") as stream:
            stream.write(raw)
        if destination.read_bytes() != raw:
            raise ValueError("persisted draft differs")
    return {
        "review": str((output / "review.json").relative_to(core.ROOT)),
        "sha256": core.sha((output / "review.json").read_bytes()),
        "inputs": len(inspection["source"]["inputs"]),
        "additional_provenance_inputs": len(additions),
        "native_validation": True,
        "inputs_unchanged": True,
        "saved_review_or_canonical_writes": False,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True)
    parser.add_argument("--config-sha256", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--expected-revision", required=True)
    parser.add_argument("--wrapper-sha256", required=True)
    args = parser.parse_args()
    print(
        json.dumps(
            build(
                args.config,
                args.config_sha256,
                args.output,
                args.expected_revision,
                args.wrapper_sha256,
            ),
            indent=2,
        )
    )
