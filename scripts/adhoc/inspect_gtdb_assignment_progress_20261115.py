"""Compare frozen GTDB assignment bytes with a current checkout, #2848, 2026-11-15.

Inputs: pinned assignment ledger and actual current canonical record files.
Output: exclusive JSON inventory; changed bytes do not imply completed review.
No canonical writes, resolver calls, network or assignment/completion inference.
"""

import argparse
import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LEDGER = ROOT / "reports/phase2-completion-20261115/gtdb-repair-assignments-001/assignments.json"
LEDGER_SHA = "ccb27e378794d589d3b2eede61b1babf59a758c921b632e6cb3534789c87536e"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    raw = LEDGER.read_bytes()
    if hashlib.sha256(raw).hexdigest() != LEDGER_SHA:
        raise ValueError("frozen assignment ledger differs")
    revision = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    captured = {LEDGER: raw}
    rows = []
    for item in json.loads(raw)["records"]:
        path = ROOT / item["record"]
        if path.is_symlink() or not path.resolve().is_relative_to(ROOT):
            raise ValueError("unsafe record path")
        captured[path] = path.read_bytes()
        digest = hashlib.sha256(captured[path]).hexdigest()
        rows.append(
            {
                "record_id": item["record_id"],
                "record": item["record"],
                "lane": item["lane"],
                "baseline_sha256": item["baseline_sha256"],
                "current_sha256": digest,
                "byte_state": (
                    "unchanged_from_assignment"
                    if digest == item["baseline_sha256"]
                    else "changed_since_assignment_not_completion_proof"
                ),
            }
        )
    if len({row["record_id"] for row in rows}) != len(rows):
        raise ValueError("duplicate assignment identity")
    result = {
        "revision": revision,
        "source_state": "working_tree",
        "assignment_sha256": LEDGER_SHA,
        "scope": "Byte inventory only. Changes are not proof of review or completion; pending branches are not inspected.",
        "counts": dict(Counter(row["byte_state"] for row in rows)),
        "records": rows,
    }
    output = args.output.resolve()
    if not output.is_relative_to(ROOT) or output.is_symlink():
        raise ValueError("repository-local exclusive output required")
    # Cooperative snapshot check, not a lock against unrelated external writers.
    for path, content in captured.items():
        if path.is_symlink() or path.read_bytes() != content:
            raise ValueError("captured input changed during inventory: " + str(path))
    final_revision = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
    ).strip()
    if final_revision != revision:
        raise ValueError("checkout revision changed during inventory")
    result["captured_inputs_unchanged"] = True
    with output.open("x") as handle:
        json.dump(result, handle, indent=2)
        handle.write("\n")
    print(json.dumps({"revision": revision, "counts": result["counts"], "output": str(output)}))


if __name__ == "__main__":
    main()
