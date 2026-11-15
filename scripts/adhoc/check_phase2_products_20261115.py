"""Run and retain Phase 2 product canary/batch checks (2026-11-15, #2430/#2705–2707).

Inputs: current records and renderer/export implementation. Outputs: normal docs/
and output/kgx products, exclusive private logs/receipts under .temp. The batch
requires a passing canary bound to unchanged implementation bytes. No network,
reference acquisition or canonical record writes are performed.
"""

import argparse
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CANARY = "Yolo_Silt_Loam_Soil_Dopamine_Amendment_Microcosm.yaml"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def implementation():
    paths = [ROOT / "src/communitymech/render.py", Path(__file__).resolve()]
    paths.extend((ROOT / "src/communitymech/export").glob("*.py"))
    paths.extend((ROOT / "src/communitymech/templates").rglob("*.html"))
    return {str(p.relative_to(ROOT)): sha(p) for p in sorted(paths)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["canary", "batch"])
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--canary-receipt", type=Path)
    args = parser.parse_args()
    output = args.output.resolve()
    if not output.is_relative_to((ROOT / ".temp").resolve()):
        parser.error("receipt directory must be new and beneath .temp")
    before = implementation()
    if args.mode == "batch":
        if args.canary_receipt is None:
            parser.error("batch requires --canary-receipt")
        canary = json.loads(args.canary_receipt.read_text())
        if canary["mode"] != "canary" or canary["exit_code"] or canary["implementation"] != before:
            parser.error("canary failed or implementation changed; re-canary first")
    output.mkdir(parents=True, exist_ok=False)
    receipt = {
        "mode": args.mode,
        "started_at": datetime.now(timezone.utc).isoformat(),
        "revision": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip(),
        "implementation": before,
        "commands": [],
        "exit_code": 0,
    }
    environment = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "PYTHONPATH": str(ROOT / "src")}
    render = [sys.executable, "-m", "communitymech.render"]
    export = [
        sys.executable,
        "-m",
        "communitymech.export",
        "--kb",
        "kb/communities",
        "--output",
        "output/kgx",
    ]
    if args.mode == "canary":
        render.append(f"kb/communities/{CANARY}")
        export.extend(["--record", CANARY])
    else:
        render.append("--all")
    commands = [
        ("render", render),
        ("export", export),
        (
            "validate-export",
            [sys.executable, "-m", "communitymech.export.validate_kgx", "--strict"],
        ),
    ]
    for name, command in commands:
        with (output / f"{name}.log.txt").open("x") as handle:
            result = subprocess.run(
                command, cwd=ROOT, env=environment, stdout=handle, stderr=subprocess.STDOUT
            )
        receipt["commands"].append({"name": name, "argv": command, "exit_code": result.returncode})
        if result.returncode:
            receipt["exit_code"] = result.returncode
            break
    paths = [ROOT / f"docs/communities/{Path(CANARY).stem}.html"]
    paths.extend(ROOT / "output/kgx" / name for name in ["nodes.tsv", "edges.tsv", "manifest.json"])
    receipt["products"] = {
        str(p.relative_to(ROOT)): {"sha256": sha(p), "bytes": p.stat().st_size}
        for p in paths
        if p.is_file()
    }
    if len(receipt["products"]) != len(paths) or not all(
        v["bytes"] for v in receipt["products"].values()
    ):
        receipt["exit_code"] = 2
    if before != implementation():
        receipt["exit_code"] = 2
    receipt["finished_at"] = datetime.now(timezone.utc).isoformat()
    with (output / "receipt.json").open("x") as handle:
        json.dump(receipt, handle, indent=2)
        handle.write("\n")
    print(json.dumps({"receipt": str(output / "receipt.json"), "exit_code": receipt["exit_code"]}))
    return receipt["exit_code"]


if __name__ == "__main__":
    raise SystemExit(main())
