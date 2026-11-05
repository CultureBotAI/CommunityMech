"""Freeze a native-valid timestamp successor after formatting the review helpers."""

import hashlib
import json
import sys
from pathlib import Path

import yaml
from pr2034_321_capture import ROOT, SCRATCH, run, write
from pr2034_321_review import NoAliases


def main():
    cleanup = "--helper-cleanup" in sys.argv
    version = 3 if cleanup else 2
    inspection_version = 5 if cleanup else 4
    before = SCRATCH / f"candidate-v{version - 1}.yaml"
    data = yaml.safe_load(before.read_text())
    paths = {x["path"] for x in data["source"]["inputs"] if x["role"] != "target"}
    paths.add(str(Path(__file__).relative_to(ROOT)))
    paths.add(".temp/pr2034/321/candidate-native-v1.json")
    command = [
        "uv",
        "run",
        "python",
        "scripts/record_review.py",
        "inspect",
        "--targets",
        str(SCRATCH / "targets.json"),
    ]
    for p in sorted(paths):
        command.extend(["--input", p])
    receipt = run(f"inspect-command-v{inspection_version}", command)
    assert receipt["exit_code"] == 0
    inspected = json.loads(receipt["stdout"])
    write(f"inspect-v{inspection_version}.json", inspected)
    old_source = data["source"]
    data["source"] = inspected["source"]
    initial = json.loads((SCRATCH / "inspect-command.json").read_text())
    data["started_at"] = initial["started_at"].replace("+00:00", "Z")
    data["finished_at"] = data["finished_at"].replace("+00:00", "Z")
    for evidence in data["evidence"]:
        evidence["accessed_at"] = evidence["accessed_at"].replace("+00:00", "Z")
    after = SCRATCH / f"candidate-v{version}.yaml"
    with after.open("x") as f:
        yaml.dump(data, f, Dumper=NoAliases, sort_keys=False, allow_unicode=True, width=110)
    write(
        f"candidate-v{version}-delta.json",
        {
            "before": {
                "path": str(before.relative_to(ROOT)),
                "sha256": hashlib.sha256(before.read_bytes()).hexdigest(),
            },
            "after": {
                "path": str(after.relative_to(ROOT)),
                "sha256": hashlib.sha256(after.read_bytes()).hexdigest(),
            },
            "changes": (
                [
                    "Native input recapture after helper-only lint cleanup; all scientific fields unchanged."
                ]
                if cleanup
                else [
                    "UTC timestamps normalized from +00:00 to schema-required Z; scientific access instants unchanged.",
                    "Started time bound to the first actual native inspection receipt, rather than a rounded task-start estimate.",
                    "Native input recapture pins formatted helper bytes, this successor helper and the preserved V1 timestamp validation failure.",
                ]
            ),
            "prior_source": old_source,
            "current_source": data["source"],
            "scientific_change": False,
        },
    )
    result = run(
        f"candidate-native-v{version}",
        ["uv", "run", "python", "scripts/record_review.py", "validate", str(after)],
    )
    assert result["exit_code"] == 0
    print(
        json.dumps(
            {
                "candidate": str(after.relative_to(ROOT)),
                "review_id": data["review_id"],
                "sha256": hashlib.sha256(after.read_bytes()).hexdigest(),
            }
        )
    )


if __name__ == "__main__":
    assert Path.cwd() == ROOT
    main()
