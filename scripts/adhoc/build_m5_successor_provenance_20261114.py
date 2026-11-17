"""Bind reviewed M5 corrections to immutable predecessors (#2782; 2026-11-14).

Inputs: existing review ledgers/bundles, public curation receipts, baseline Git
objects and current records/caches. Output: append-only successor provenance.
This records corrections; it does not claim final QC or scientific approval.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
BASELINE = "76aa644cd6803ea2c9545d4c704276ede219d354"
OUT = ROOT / "reports/m5-completion-20261114/successor-provenance.yaml"
RECEIPTS = "reports/m5-completion-20261114/curation-receipts/"
CAUSAL = "reports/causal_graph_review/decisions/"
RECORDS = (
    (
        "CommunityMech:000025",
        "EcoFAB_Ring_Trial_SynCom17",
        "20261029-host-soil-related-communities-paper-test.yaml",
        ["ecofab-relation"],
        "20261114T212137Z-m5-ecofab-completion-canary",
    ),
    (
        "CommunityMech:000515",
        "Yolo_Silt_Loam_Soil_Dopamine_Amendment_Microcosm",
        "20261106-stage2-seven-records-batch141.yaml",
        ["yolo-provenance"],
        "20261114T213322Z-m5-yolo-scientific-completion",
    ),
    (
        "CommunityMech:000516",
        "Brachypodium_Natural_Variation_Dopamine_SynCom16",
        "20261106-stage2-seven-records-batch141.yaml",
        ["syncom-mechanism", "syncom-endpoint"],
        "20261114T213444Z-m5-dopamine-syncom-primary-review",
    ),
)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def artifact(path):
    return {"path": path, "sha256": sha((ROOT / path).read_bytes())}


def original(path):
    return subprocess.check_output(["git", "show", f"{BASELINE}:{path}"], cwd=ROOT)


def body(raw):
    assert raw.startswith(b"---\n")
    frontmatter, delimiter, content = raw.partition(b"\n---\n")
    assert delimiter
    return frontmatter, content


def main():
    if OUT.exists():
        raise ValueError("successor provenance already exists; append a later successor instead")
    result = {
        "schema_version": 1,
        "issue": 2782,
        "source_baseline": BASELINE,
        "canonical_revision": "76686e5b03335baec13885196d0f736511b6a04a",
        "independent_approval": False,
        "scope": "Hash-bound M5 curation succession; original graph ledgers remain unchanged. Final aggregate QC and post-curation scientific delta are pending.",
        "records": [],
        "cache_corrections": [],
    }
    for identifier, stem, predecessor, receipt_names, review in RECORDS:
        path = f"kb/communities/{stem}.yaml"
        ledger_path = CAUSAL + predecessor
        old = next(
            row
            for row in yaml.safe_load((ROOT / ledger_path).read_text())["records"]
            if row["id"] == identifier
        )
        before = sha(original(path))
        assert before == old["record_sha256"]
        chain = []
        for name in receipt_names:
            receipt_path = RECEIPTS + name + ".json"
            receipt = json.loads((ROOT / receipt_path).read_text())
            assert receipt["path"] == path and receipt["applied"] is True
            assert receipt["before_sha256"] == before
            before = receipt["after_sha256"]
            chain.append(artifact(receipt_path))
        assert before == sha((ROOT / path).read_bytes())
        result["records"].append(
            {
                "id": identifier,
                "path": path,
                "original_sha256": old["record_sha256"],
                "record_sha256": before,
                "supersedes_review": {
                    "review_file": ledger_path,
                    "record_sha256": old["record_sha256"],
                },
                "curation_receipts": chain,
                "scientific_review": artifact(f"reviews/structured/{review}/review.yaml"),
            }
        )
    for name in ("cache-ecofab", "cache-nitrogen", "cache-dopamine"):
        receipt_path = RECEIPTS + name + ".json"
        receipt = json.loads((ROOT / receipt_path).read_text())
        path = receipt["path"]
        old = original(path)
        current = (ROOT / path).read_bytes()
        assert sha(old) == receipt["before_sha256"]
        assert sha(current) == receipt["after_sha256"]
        old_header, old_body = body(old)
        current_header, current_body = body(current)
        assert old_body == current_body
        assert old_header.count(b"content_type: abstract_only") == 1
        assert current_header == old_header.replace(
            b"content_type: abstract_only", b"content_type: abstract_and_full_text", 1
        )
        result["cache_corrections"].append(
            {
                "path": path,
                "original_sha256": sha(old),
                "current_sha256": sha(current),
                "article_body_sha256": sha(old_body),
                "receipt": artifact(receipt_path),
                "allowed_header_change": {
                    "content_type": ["abstract_only", "abstract_and_full_text"]
                },
            }
        )
    OUT.write_text(yaml.safe_dump(result, sort_keys=False, width=100), encoding="utf-8")
    print(str(OUT.relative_to(ROOT)))


if __name__ == "__main__":
    main()
