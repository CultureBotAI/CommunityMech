#!/usr/bin/env python3
"""Measure one exact historical GTDB contract for #2947, 2026-11-16.

Inputs: an explicit known Git revision and the frozen read-only CI inventory
helper. Output: exclusive JSON observations; no source or test mutations.
"""

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HELPER = ROOT / "scripts/adhoc/inventory_phase2_ci_causes_20261116.py"
HELPER_SHA = "6d14e991c6562fa4c5af46a8cd8f825bf4fb5a3a1e1fe522c0b89e05d5031828"
REVISIONS = (
    "edd740d502690303a691935d1ee8deef911362f8",
    "68699871415fda3c9eebf20382a315f9f3c7b17a",
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--revision", required=True, choices=REVISIONS)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    raw = HELPER.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == HELPER_SHA
    spec = importlib.util.spec_from_file_location("captured_ci_inventory", HELPER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    result = module.snapshot(ROOT, args.revision)
    assert HELPER.read_bytes() == raw
    result["inventory_helper_sha256"] = HELPER_SHA
    result["launcher_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result["scope"] = "immutable historical observations, not current scientific or QC approval"
    with args.output.open("x") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    print(json.dumps({"path": str(args.output), "sha256": module.sha(args.output.read_bytes())}))


if __name__ == "__main__":
    main()
