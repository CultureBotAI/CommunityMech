"""Retain C1 references as NOT RUN before the authoritative C2 rerun (2026-11-14).

Input: root's explicit supersession instruction and the frozen remote C1 checkout.
Output: exclusive control marker/receipt; no running source/helper is changed.
The native runner refuses existing names, so it stops before the reference sweep.
"""

from __future__ import annotations

import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ".temp/m5-completion-20261114"
HEAD = "76686e5b03335baec13885196d0f736511b6a04a"


def main():
    receipt = {
        "name": "final-reference-diagnostic",
        "status": "NOT RUN",
        "head": HEAD,
        "time": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "reason": "C1 aggregate failed predecessor-hash tests. Retain its focused diagnostics, then run actual full qc-references on C2; do not duplicate the C1 corpus reference fallback.",
        "planned_native_recipe": "validate-references-all",
    }
    payload = json.dumps(receipt, indent=2) + "\n"
    marker = f"{STATE}/final-reference-diagnostic.json"
    saved = f"{STATE}/c1-reference-supersession.json"
    command = (
        f'cd {ROOT} && test "$(git rev-parse HEAD)" = {HEAD} '
        f"&& test ! -e {saved} && set -C && cat > {marker} && cp {marker} {saved}"
    )
    subprocess.run(
        [
            "ssh",
            "-o",
            "BatchMode=yes",
            "-o",
            "ConnectTimeout=10",
            "marcins-MacBook-Pro-3.local",
            command,
        ],
        input=payload,
        text=True,
        check=True,
    )
    with (ROOT / saved).open("x", encoding="utf-8") as handle:
        handle.write(payload)
    print("C1 fallback guarded NOT RUN; authoritative full references are deferred to C2.")


if __name__ == "__main__":
    main()
