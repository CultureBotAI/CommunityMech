"""Join two actual mapping canaries without rewriting batch144 (#2849), 2026-11-15.

Inputs: exact public BR1/Terrabacter proofs and their maintained records,
immutable diagnostics, actual apply receipts and native sidecars. Output: one
exclusive combined successor manifest; --plan validates without writes.
No canonical, history, old review, source acquisition or validator mutation.
"""

import argparse
import copy
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tests"))
from batch144_mapping_successor import (  # noqa: E402
    BASELINE,
    BR1,
    MANIFEST,
    current_record_sha256,
    digest,
)

SOURCES = {
    "reports/gtdb-source-routes-2849-20261115/terrabacter-successor-001.json": "3ebccc9e03e97580ba4333d7b8863e0b1991916ad9a48d48481a5ea7c2f626cb",
    "reports/br1-source-review-20261115/br1-successor-001.json": "50db2de5ad9d4dce228640b5a3018aff9529399ed8d326668e944609f3364d11",
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    output = ROOT / MANIFEST
    if not args.plan and (output.exists() or output.is_symlink()):
        raise ValueError("existing combined manifest must remain immutable")
    captured = {}
    entries = []
    for relative, expected in SOURCES.items():
        path = ROOT / relative
        raw = path.read_bytes()
        if digest(raw) != expected:
            raise ValueError("reviewed child proof differs: " + relative)
        captured[path] = raw
        doc = json.loads(raw)
        if doc["source_baseline"] != BASELINE:
            raise ValueError("child predecessor baseline differs")
        if "records" in doc:
            if len(doc["records"]) != 1:
                raise ValueError("one child record required")
            entries.append(doc["records"][0])
        else:
            entry = copy.deepcopy(doc)
            if entry["target"] != BR1:
                raise ValueError("BR1 child required")
            entry.pop("source_baseline")
            entry["grounding_proof"] = dict(entry["grounding_evidence"])
            entry["grounding_proof"]["raw_path"] = entry["grounding_evidence"]["path"]
            entries.append(entry)
    helpers = (
        Path(__file__).relative_to(ROOT),
        Path("tests/batch144_mapping_successor.py"),
        Path("tests/sulfobacillus_mapping_successor.py"),
        Path("scripts/record_review.py"),
        Path("schema/record_review.yaml"),
    )
    for relative in helpers:
        path = ROOT / relative
        captured[path] = path.read_bytes()
    for entry in entries:
        for name in [entry["target"]] + [
            value["path"]
            for value in entry.values()
            if isinstance(value, dict) and "path" in value and "sha256" in value
        ]:
            path = (ROOT / name).resolve()
            if not path.is_relative_to(ROOT):
                raise ValueError("artifact escapes checkout")
            if path not in captured:
                captured[path] = path.read_bytes()
    combined = {
        "source_baseline": BASELINE,
        "child_manifests": [{"path": path, "sha256": sha} for path, sha in SOURCES.items()],
        "records": sorted(entries, key=lambda row: row["target_id"]),
        "helper_sources": [
            {"path": str(path), "sha256": digest(captured[ROOT / path])} for path in helpers
        ],
        "scope": "Two individually reviewed source-supported GTDB corrections. The original batch144 ledger and every biological/graph assertion remain unchanged; BR1 alone replaces one exact GTDB identifier in its description. No new whole-record scientific approval.",
    }
    for entry in entries:
        current_record_sha256(ROOT, entry["target"], entry["before_sha256"], manifest=combined)
    for path, raw in captured.items():
        if path.read_bytes() != raw:
            raise ValueError("input changed before manifest persistence")
    raw_output = (json.dumps(combined, indent=2) + "\n").encode()
    if not args.plan:
        with output.open("xb") as stream:
            stream.write(raw_output)
        if output.read_bytes() != raw_output:
            raise ValueError("combined manifest persistence differs")
    print(
        json.dumps(
            {
                "targets_verified": len(entries),
                "plan": args.plan,
                "manifest": MANIFEST,
                "manifest_sha256": digest(raw_output),
            }
        )
    )


if __name__ == "__main__":
    main()
