"""Publish verified Phase 2 native QC receipts for PR #2804 (2026-11-15).

Inputs: explicitly named completed driver receipts and their exact logs/exits,
mirrored from M5 into repository .temp. Outputs: immutable sanitized derivatives
under reports/phase2-completion-20261115/technical-evidence. Never alters raw
evidence or promotes separate diagnostics into an aggregate QC pass.
"""

import argparse
import json
import re
from collections import Counter

from export_m5_technical_evidence_20261114 import ROOT, digest, immutable, sanitize

STATE = ROOT / ".temp/m5-completion-20261114"
OUTPUT = ROOT / "reports/phase2-completion-20261115/technical-evidence"


def export(name):
    if not re.fullmatch(r"phase2-[A-Za-z0-9-]+-(?:plan|canary|qc|products|docs)", name):
        raise ValueError("expected a named Phase 2 driver run")
    receipt_path = STATE / f"{name}.json"
    raw_receipt = receipt_path.read_bytes()
    receipt = json.loads(raw_receipt)
    log_path = STATE / f"{name}.log"
    exit_path = STATE / f"{name}.exit"
    raw_log = log_path.read_bytes()
    raw_exit = exit_path.read_bytes()
    if (
        receipt.get("name") != name
        or not receipt.get("finished_at")
        or receipt.get("status") not in {"PASSED", "FAILED", "COMPLETED WITH SKIPS"}
        or not re.fullmatch(r"[0-9a-f]{40}", receipt.get("head", ""))
        or receipt.get("log") != str(log_path.relative_to(ROOT))
        or not raw_log
        or len(raw_log) != receipt.get("log_bytes")
        or digest(raw_log) != receipt.get("log_sha256")
        or int(raw_exit.strip()) != receipt.get("exit_code")
        or (receipt["status"] in {"PASSED", "COMPLETED WITH SKIPS"}) != (receipt["exit_code"] == 0)
    ):
        raise ValueError("incomplete or inconsistent native evidence")
    counts = Counter()
    private_cwd = receipt.get("cwd")

    def scrub(text):
        if private_cwd:
            occurrences = text.count(private_cwd)
            counts["source_repository_absolute_path"] += occurrences
            text = text.replace(private_cwd, "<REPO>")
        return sanitize(text, counts)

    public_log = scrub(raw_log.decode("utf-8")).encode("utf-8")
    public_receipt = json.loads(scrub(raw_receipt.decode("utf-8")))
    public_receipt.pop("cwd", None)
    public_receipt["log"] = str((OUTPUT / f"{name}.log.txt").relative_to(ROOT))
    public_receipt["public_evidence"] = {
        "raw_receipt_sha256": digest(raw_receipt),
        "raw_log_sha256": digest(raw_log),
        "raw_exit_sha256": digest(raw_exit),
        "public_log_sha256": digest(public_log),
        "public_log_bytes": len(public_log),
        "redactions": {key: value for key, value in sorted(counts.items()) if value},
        "raw_evidence_location": "M5 execution checkout and verified local mirror, repository .temp",
        "limits": "Native technical result only; diagnostics do not complete failed aggregate stages or scientific review.",
    }
    OUTPUT.mkdir(parents=True, exist_ok=True)
    immutable(OUTPUT / f"{name}.log.txt", public_log)
    immutable(OUTPUT / f"{name}.exit.txt", raw_exit)
    immutable(
        OUTPUT / f"{name}.receipt.json",
        (json.dumps(public_receipt, indent=2) + "\n").encode("utf-8"),
    )
    print(json.dumps({"name": name, "status": receipt["status"], "revision": receipt["head"]}))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--name", action="append", required=True)
    args = parser.parse_args()
    for name in args.name:
        export(name)


if __name__ == "__main__":
    main()
