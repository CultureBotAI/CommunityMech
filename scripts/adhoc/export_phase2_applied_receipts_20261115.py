"""Publish immutable metadata for five verified Phase2 writes, 2026-11-15.

Inputs: original applied receipts, exact retained canonical before/after copies,
current three records and native history sidecars. Output: exclusive public
metadata directory. Serves #2816; no full papers, private prompts or host paths.
No canonical/history mutation and no inference that future corrections occurred.
"""

import argparse
import hashlib
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/phase2-science-20261115"
BASE = "68699871415fda3c9eebf20382a315f9f3c7b17a"
STEPS = (
    ("lbnl-source-scope", "curation-applied-001", "receipt.json"),
    ("lbnl-mapping-note", "mapping-note-applied-001", "receipt.json"),
    ("ecofab-linked-stock", "linked-stock-plan-003/ecofab", "apply/receipt.json"),
    ("dopamine-linked-stock", "linked-stock-plan-003/dopamine", "apply/receipt.json"),
    ("lbnl-linked-stock", "linked-stock-plan-003/lbnl", "apply/receipt.json"),
)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def privacy_check(raw):
    text = raw.decode("utf-8")
    if re.search(r"/Users/|/home/|(?<!\S)@[\w.-]+|[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}", text):
        raise ValueError("public metadata privacy guard refused content")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    if output.exists() or not output.is_relative_to(ROOT / "reports/phase2-science-20261115"):
        raise ValueError("new exclusive public metadata directory required")
    files, rows, last = {}, [], {}
    for key, directory, receipt_name in STEPS:
        directory = STATE / directory
        receipt_path = directory / receipt_name
        raw = receipt_path.read_bytes()
        privacy_check(raw)
        receipt = json.loads(raw)
        if not (receipt.get("applied") is True or receipt.get("applied_at")):
            raise ValueError("only actual applied receipts may enter completion chain")
        before = (directory / "before.yaml").read_bytes()
        after = (directory / "candidate.yaml").read_bytes()
        target = receipt["target"]
        if sha(before) != receipt["before_sha256"] or sha(after) != receipt["after_sha256"]:
            raise ValueError("receipt differs from retained canonical snapshots")
        if target not in last:
            historic = subprocess.check_output(["git", "show", BASE + ":" + target], cwd=ROOT)
            if historic != before:
                raise ValueError("chain does not start at public baseline: " + target)
        elif before != last[target]:
            raise ValueError("applied chain is discontinuous: " + target)
        first, second = yaml.safe_load(before), yaml.safe_load(after)
        prior = first.get("curation_history", [])
        current = second.get("curation_history", [])
        if current[: len(prior)] != prior or len(current) != len(prior) + 1:
            raise ValueError("exactly one append-only native inline event required")
        event = current[-1]
        if event.get("curator") != "codex" or event.get("llm_assisted") is not True:
            raise ValueError("incorrect native agent attribution")
        if first["id"] != second["id"]:
            raise ValueError("record identity changed")
        filename = key + ".json"
        files[filename] = raw
        rows.append(
            {
                "step": key,
                "target": target,
                "target_id": first["id"],
                "source_receipt": str(receipt_path.relative_to(ROOT)),
                "public_receipt": str((output / filename).relative_to(ROOT)),
                "original_receipt_sha256": sha(raw),
                "public_receipt_sha256": sha(raw),
                "before_sha256": sha(before),
                "after_sha256": sha(after),
                "prior_history_events_preserved": len(prior),
                "appended_event": event,
                "before_snapshot": str((directory / "before.yaml").relative_to(ROOT)),
                "after_snapshot": str((directory / "candidate.yaml").relative_to(ROOT)),
            }
        )
        last[target] = after
    for target, raw in last.items():
        if (ROOT / target).read_bytes() != raw:
            raise ValueError("current record differs from final applied chain step: " + target)
    sidecars = {}
    for target in last:
        directory = ROOT / "history/records" / Path(target).stem
        for path in sorted(directory.glob("2026-11-15T*.yaml")):
            doc = yaml.safe_load(path.read_text())
            if doc["target"]["path"] != target:
                raise ValueError("native sidecar target mismatch")
            sidecars[str(path.relative_to(ROOT))] = sha(path.read_bytes())
    result = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "scope": "Five applied scientific/metadata writes through linked-stock checkpoint; no later1427/2675 correction or full-QC completion claimed.",
        "baseline_revision": BASE,
        "checkpoint_revision": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip(),
        "helper_sha256": sha(Path(__file__).read_bytes()),
        "steps": rows,
        "current_target_sha256": {target: sha(raw) for target, raw in sorted(last.items())},
        "native_sidecars": sidecars,
        "limitations": [
            "Original applied receipt bytes are metadata-only and pass the privacy guard; copied byte-for-byte. Private before/after canonical snapshots remain separately retained; no primary paper text is published.",
            "Earlier staged plan receipts are not applied events and are deliberately excluded. The exact supplemental quote was corrected before the first000087 apply, not by an invented later write.",
            "Inline append-only checks and sidecar byte identity are reproducible metadata proof, not scientific support or a substitute for native history validation.",
        ],
    }
    encoded = (json.dumps(result, indent=2) + "\n").encode()
    privacy_check(encoded)
    files["chain.json"] = encoded
    output.mkdir()
    for name, raw in files.items():
        with (output / name).open("xb") as stream:
            stream.write(raw)
        if (output / name).read_bytes() != raw:
            raise ValueError("persisted public receipt differs")
    print(
        json.dumps(
            {
                "output": str(output.relative_to(ROOT)),
                "steps": len(rows),
                "sidecars": len(sidecars),
                "public_files": len(files),
            }
        )
    )


if __name__ == "__main__":
    main()
