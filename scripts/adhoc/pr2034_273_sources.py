"""Capture read-only authority, corpus hashes, and exact old/current record delta.

The independent public publisher abstract was read via web.run and projected to
publisher.json in isolated scratch. A direct HTTP attempt returned challenge
HTML and is not treated as article content. This helper performs no acquisition.
"""

import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import yaml
from oaklib import get_adapter

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / ".temp/pr2034/273"
TARGET = "data/isolates/Chromobacterium_Gold_Biocyanidation.yaml"


def save(name, value):
    with (OUT / name).open("x") as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2)
        stream.write("\n")


def changed(a, b, path=""):
    if isinstance(a, dict) and isinstance(b, dict):
        return sum(
            (
                changed(a.get(k), b.get(k), f"{path}.{k}" if path else k)
                for k in sorted(a.keys() | b.keys())
            ),
            [],
        )
    if a == b:
        return []
    return [{"path": path, "before": a, "after": b}]


def main():
    adapter = get_adapter("sqlite:obo:envo")
    save(
        "envo.json",
        {
            "adapter": "sqlite:obo:envo",
            "id": "ENVO:00000003",
            "label": adapter.label("ENVO:00000003"),
            "definition": adapter.definition("ENVO:00000003"),
            "accessed_at": datetime.now(timezone.utc).isoformat(),
        },
    )
    files = sorted(
        [*(ROOT / "kb/communities").glob("*.yaml"), *(ROOT / "data/isolates").glob("*.yaml")]
    )
    save(
        "network-corpus-inputs.json",
        {
            "git_revision": subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
            ).strip(),
            "scope": "All direct YAML records in both native default roots; pathlib ignores no files",
            "captured_at": datetime.now(timezone.utc).isoformat(),
            "inputs": [
                {
                    "path": str(p.relative_to(ROOT)),
                    "sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
                }
                for p in files
            ],
        },
    )
    old = yaml.safe_load(
        (
            ROOT / "reviews/structured/" "20261019T233358Z-chromobacterium-gold-record/review.yaml"
        ).read_text()
    )
    raw = subprocess.check_output(
        ["git", "show", f"{old['source']['git_revision']}:{TARGET}"], cwd=ROOT
    )
    expected = next(x["sha256"] for x in old["source"]["inputs"] if x["path"] == TARGET)
    assert hashlib.sha256(raw).hexdigest() == expected
    current = (ROOT / TARGET).read_bytes()
    before, after = yaml.safe_load(raw), yaml.safe_load(current)
    save(
        "record-delta.json",
        {
            "old_revision": old["source"]["git_revision"],
            "old_sha256": expected,
            "current_sha256": hashlib.sha256(current).hexdigest(),
            "graphs_equal": before["ecological_interactions"] == after["ecological_interactions"],
            "changed": changed(before, after),
        },
    )
    print(
        json.dumps(
            {
                "corpus_records": len(files),
                "graphs_unchanged": before["ecological_interactions"]
                == after["ecological_interactions"],
                "changed_fields": [x["path"] for x in changed(before, after)],
            }
        )
    )


if __name__ == "__main__":
    main()
