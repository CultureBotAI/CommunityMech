"""Exercise #1548 current-boundary tests on two isolated worktrees, 2026-11-15.

Inputs: explicit applied Brachypodium/gut records and the maintained test module.
Output: exclusive private receipt with exact source hashes and positive/mutation
results. No canonical edits or pytest scope exemptions; integration runs pytest.
"""

import argparse
import hashlib
import importlib.util
import json
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
TEST = ROOT / "tests/test_phase2_scientific_boundaries.py"


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--brachypodium", type=Path, required=True)
    parser.add_argument("--gut", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    if output.exists() or output.is_symlink() or not output.is_relative_to(ROOT / ".temp"):
        raise ValueError("fresh private receipt required")
    spec = importlib.util.spec_from_file_location("phase2_boundaries", TEST)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    rows = []
    for name, record_path, check, mutate, cases in (
        (
            "brachypodium",
            args.brachypodium,
            module.check_brachypodium,
            module.mutate_brachypodium,
            module.BRACH_MUTATIONS,
        ),
        ("gut", args.gut, module.check_gut, module.mutate_gut, module.GUT_MUTATIONS),
    ):
        raw = record_path.read_bytes()
        record = yaml.safe_load(raw)
        check(record)
        for case in cases:
            module.assert_mutation_rejected(check, mutate, record, case)
        if record_path.read_bytes() != raw:
            raise ValueError("record changed during controls")
        rows.append(
            {
                "name": name,
                "path": str(record_path.resolve()),
                "sha256": digest(raw),
                "positive": "passed",
                "mutations_rejected": list(cases),
                "restored_original_controls": "passed",
            }
        )
    result = {
        "created_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "test_module_sha256": digest(TEST.read_bytes()),
        "scope": "Same maintained check/mutation functions on exact applied records in two isolated worktrees; not a full pytest or integration-QC claim.",
        "records": rows,
    }
    with output.open("x") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
