"""Publish successor 000122 technical receipts for #2831/#2818, 2026-11-15.

Inputs: nine finished private native gates, measured assertion counts and saved
review audit. Outputs: exclusive public metadata/log derivatives; source bodies
and raw logs remain private. No validation rerun, network or canonical write.
"""

import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/phase2-gut-20261115"


def digest(content):
    return hashlib.sha256(content).hexdigest()


def clean(text):
    text = text.replace(str(ROOT), "<checkout>")
    text = re.sub(r"/Users/[^/\s]+", "<home>", text)
    return re.sub(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", "<redacted-address>", text)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    if not output.is_relative_to(ROOT / "reports/phase2-gut-20261115") or output.exists():
        raise ValueError("exclusive public report directory required")
    rows = []
    material = {}
    for gate in (
        "schema",
        "strict",
        "terms",
        "references",
        "gtdb",
        "domain",
        "scalars",
        "history",
        "network",
    ):
        name = "canary-" + gate + "-historical-001"
        path = STATE / (name + ".json")
        raw = path.read_bytes()
        receipt = json.loads(raw)
        log = (ROOT / receipt["log"]).read_bytes()
        if (
            receipt["status"] != "PASSED"
            or receipt["exit_code"] != 0
            or (STATE / (name + ".exit")).read_text().strip() != "0"
            or digest(log) != receipt["log_sha256"]
            or not log
            or not receipt["inputs_unchanged"]
            or digest((ROOT / receipt["record"]).read_bytes()) != receipt["record_worktree_sha256"]
        ):
            raise ValueError("native completion proof differs: " + gate)
        log_public = clean(log.decode()).encode()
        material[gate + ".log.txt"] = log_public
        rows.append(
            {
                "gate": gate,
                "receipt_path": str(path.relative_to(ROOT)),
                "raw_receipt_sha256": digest(raw),
                "receipt": json.loads(clean(raw.decode())),
                "raw_log_sha256": digest(log),
                "public_log": gate + ".log.txt",
                "public_log_sha256": digest(log_public),
                "redacted": log_public != log,
            }
        )
    measurement_path = STATE / "measured-historical-001/receipt.json"
    measurement_raw = measurement_path.read_bytes()
    measurement = json.loads(measurement_raw)
    audit_path = STATE / "historical-saved-review-audit-001.json"
    audit_raw = audit_path.read_bytes()
    audit = json.loads(audit_raw)
    if not audit["all_inputs_match"] or not audit["markdown_matches_native_render"]:
        raise ValueError("saved review audit failed")
    for item in audit["inputs"]:
        if digest((ROOT / item["path"]).read_bytes()) != item["expected_sha256"]:
            raise ValueError("saved review input changed after audit")
    if (
        not measurement["measurement_valid"]
        or not measurement["inputs_unchanged"]
        or not measurement["assertion_coverage_complete"]
        or measurement["assertion_status_counts"] != {"matched": 44}
        or measurement["native_exit_code"] != 0
        or (measurement_path.parent / "exit").read_text().strip() != "0"
    ):
        raise ValueError("successor measurement incomplete")
    application_path = STATE / "historical-scope-applied-001/receipt.json"
    application_raw = application_path.read_bytes()
    if (
        digest(application_raw)
        != "7752c6f3470f9d8312cc8406313158b04500472eaf6b1a9b50973185400eefe6"
        or clean(application_raw.decode()).encode() != application_raw
        or not json.loads(application_raw)["applied"]
    ):
        raise ValueError("exact public application receipt or privacy boundary differs")
    material["application.raw.json"] = application_raw
    summary = {
        "scope": "Nine scoped native gates; not a full repository QC claim. Sanitized logs only; no article bodies.",
        "publisher_sha256": digest(Path(__file__).read_bytes()),
        "actual_application": {
            "raw_path": str(application_path.relative_to(ROOT)),
            "raw_sha256": digest(application_raw),
            "public_path": "application.raw.json",
            "byte_identical": True,
        },
        "gates": rows,
        "measurement": {
            "raw_path": str(measurement_path.relative_to(ROOT)),
            "raw_sha256": digest(measurement_raw),
            **{
                key: measurement[key]
                for key in (
                    "head",
                    "record_sha256",
                    "counts",
                    "assertion_status_counts",
                    "measurement_valid",
                    "assertion_coverage_complete",
                    "inputs_unchanged",
                )
            },
        },
        "saved_review_audit": {
            "raw_path": str(audit_path.relative_to(ROOT)),
            "raw_sha256": digest(audit_raw),
            "review_id": audit["review_id"],
            "review_sha256": audit["review_sha256"],
            "input_count": audit["input_count"],
            "all_inputs_match": audit["all_inputs_match"],
            "markdown_matches_native_render": audit["markdown_matches_native_render"],
        },
    }
    output.mkdir(parents=True)
    for name, content in material.items():
        (output / name).write_bytes(content)
    (output / "receipts.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(
        json.dumps(
            {
                "output": str(output.relative_to(ROOT)),
                "logs": len(material),
                "review_id": audit["review_id"],
                "inputs": audit["input_count"],
            }
        )
    )


if __name__ == "__main__":
    main()
