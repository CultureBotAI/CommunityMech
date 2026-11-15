"""Publish bounded 000122 technical receipts for #1548/#2816, 2026-11-15.

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
        name = "canary-" + gate + "-applied-001"
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
    measurement_path = STATE / "measured-applied-001/receipt.json"
    measurement_raw = measurement_path.read_bytes()
    measurement = json.loads(measurement_raw)
    audit_path = STATE / "saved-review-audit-001.json"
    audit_raw = audit_path.read_bytes()
    audit = json.loads(audit_raw)
    if not audit["all_inputs_match"] or not audit["markdown_matches_native_render"]:
        raise ValueError("saved review audit failed")
    summary = {
        "scope": "Nine scoped native gates; not a full repository QC claim. Sanitized logs only; no article bodies.",
        "publisher_sha256": digest(Path(__file__).read_bytes()),
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
