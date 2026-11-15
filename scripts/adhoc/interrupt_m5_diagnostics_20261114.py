"""Stop only the superseded baseline diagnostic batch (2026-11-14).

Inputs: exact pinned checkout and its currently running native terms recipe.
Outputs: interruption receipt, preserved native exit/log, and a NOT RUN marker
that prevents this batch from starting another baseline validator.
"""

from __future__ import annotations

import argparse
import json
import os
import signal
import subprocess

from m5_completion_checks import PIN, STATE, git, now, write_json


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--term-after-ignored-int", action="store_true")
    args = parser.parse_args()
    if git("rev-parse", "HEAD") != PIN:
        raise ValueError("not the expected baseline checkout")
    active = STATE / "diagnostic-validate-terms-all.json"
    result = json.loads(active.read_text())
    if result["status"] != "RUNNING":
        raise ValueError("the expected baseline terms diagnostic is not running")
    table = subprocess.check_output(["ps", "-axo", "pid=,ppid=,command="], text=True)
    processes = {}
    for line in table.splitlines():
        pid, parent, command = line.strip().split(None, 2)
        processes[int(pid)] = {"ppid": int(parent), "command": command}
    expected = (
        "/opt/homebrew/bin/just --verbose --no-dotenv --color never --no-deps validate-terms-all"
    )
    matches = [
        pid
        for pid, row in processes.items()
        if row["command"] == expected
        and processes.get(row["ppid"], {}).get("command")
        == ".venv/bin/python scripts/adhoc/m5_completion_checks.py diagnostic-batch"
    ]
    if len(matches) != 1:
        raise ValueError("cannot identify exactly one owned native terms child")
    pid = matches[0]
    receipt = STATE / "baseline-diagnostic-interruption.json"
    next_marker = STATE / "diagnostic-validate-products.json"
    if args.term_after_ignored_int:
        prior = json.loads(receipt.read_text())
        if prior["target"]["pid"] != pid or not next_marker.exists():
            raise ValueError("the persisted SIGINT attempt does not match this subprocess")
        tree = [pid]
        for parent in tree:
            tree.extend(child for child, row in processes.items() if row["ppid"] == parent)
        term_receipt = STATE / "baseline-diagnostic-termination.json"
        if term_receipt.exists():
            raise ValueError("termination fallback has already been attempted")
        write_json(
            term_receipt,
            {
                "time": now(),
                "reason": "Background/nohup child ignored SIGINT; terminate only its verified descendant tree.",
                "targets": [{"pid": child, **processes[child]} for child in tree],
                "signals": ["SIGSTOP", "SIGTERM", "SIGCONT"],
            },
        )
        # Pause the recipe shell first so it cannot start another loop iteration.
        for child in tree:
            try:
                os.kill(child, signal.SIGSTOP)
            except ProcessLookupError:
                continue
        for child in reversed(tree):
            try:
                os.kill(child, signal.SIGTERM)
                os.kill(child, signal.SIGCONT)
            except ProcessLookupError:
                continue
        print("Terminated only the verified owned native diagnostic tree after ignored SIGINT.")
        return
    if receipt.exists() or next_marker.exists():
        raise ValueError("stop receipt or next-stage marker already exists")
    reason = "Superseded baseline: stop before final-revision validation; not a repository failure."
    write_json(
        next_marker, {"name": "diagnostic-validate-products", "status": "NOT RUN", "reason": reason}
    )
    write_json(
        receipt,
        {
            "time": now(),
            "reason": reason,
            "signal": "SIGINT",
            "target": {"pid": pid, **processes[pid]},
            "parent": processes[processes[pid]["ppid"]],
            "active_run": result["name"],
            "next_stage_guard": str(next_marker.relative_to(STATE.parent.parent)),
        },
    )
    os.kill(pid, signal.SIGINT)
    print("Interrupted the exact owned native terms child; next baseline stage is guarded NOT RUN.")


if __name__ == "__main__":
    main()
