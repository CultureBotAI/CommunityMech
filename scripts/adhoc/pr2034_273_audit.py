"""Read-only PR2034/273 inspection and validation; writes isolated audit scratch.

Run with the repository's configured Python environment. No scientific record,
history, cache, shared environment, Git state, or review bundle is mutated.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shlex
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
SCRATCH = ROOT / ".temp/pr2034/273"
TARGET = "data/isolates/Chromobacterium_Gold_Biocyanidation.yaml"
OLD = "reviews/structured/20261019T233358Z-chromobacterium-gold-record/review.yaml"
ENV = {
    **os.environ,
    "UV_PROJECT_ENVIRONMENT": str(ROOT.parents[1] / ".venv"),
    "UV_NO_SYNC": "1",
    "UV_CACHE_DIR": str(ROOT / ".temp/uv-cache"),
    "PYTHONPATH": str(ROOT / "src"),
    "JUST_NO_DOTENV": "true",
}


def now():
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def write(name, value):
    path = SCRATCH / name
    with path.open("x") as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write("\n")
    return path


def run(name, args):
    started = now()
    result = subprocess.run(args, cwd=ROOT, env=ENV, capture_output=True)
    for suffix, data in [("stdout", result.stdout), ("stderr", result.stderr)]:
        with (SCRATCH / f"{name}.{suffix}.txt").open("xb") as stream:
            stream.write(data)
    receipt = {
        "command": shlex.join(args),
        "cwd": str(ROOT),
        "environment": {
            k: ENV[k]
            for k in ENV
            if k
            in {
                "UV_PROJECT_ENVIRONMENT",
                "UV_NO_SYNC",
                "UV_CACHE_DIR",
                "PYTHONPATH",
                "JUST_NO_DOTENV",
            }
        },
        "started_at": started,
        "finished_at": now(),
        "exit_code": result.returncode,
        "stdout_sha256": sha(result.stdout),
        "stderr_sha256": sha(result.stderr),
        "stdout_path": str((SCRATCH / f"{name}.stdout.txt").relative_to(ROOT)),
        "stderr_path": str((SCRATCH / f"{name}.stderr.txt").relative_to(ROOT)),
    }
    write(f"{name}.json", receipt)
    print(json.dumps({"name": name, "exit_code": result.returncode}), flush=True)
    return result


def inspect():
    old = yaml.safe_load((ROOT / OLD).read_text())
    target = old["targets"][0]
    manifest = SCRATCH / "targets.yaml"
    if not manifest.exists():
        with manifest.open("x") as stream:
            yaml.safe_dump({"targets": [target]}, stream, sort_keys=False)
    contexts = [item["path"] for item in old["source"]["inputs"] if item["role"] != "target"]
    contexts = ["AGENTS.md" if path == "CLAUDE.md" else path for path in contexts]
    contexts += [
        OLD,
        "schema/record_review.yaml",
        "conf/record_review.yaml",
        "scripts/record_review.py",
        "scripts/adhoc/pr2034_273_audit.py",
        "history/records/Chromobacterium_Gold_Biocyanidation/"
        "2026-10-21T190000Z-claude-2050.yaml",
    ]
    lineage = []
    for path in sorted((ROOT / "reviews/structured").glob("*/review.yaml")):
        document = yaml.safe_load(path.read_text())
        findings = [
            f
            for f in document.get("findings", [])
            if "CommunityMech:000273" in f.get("target_ids", [])
        ]
        if findings:
            contexts.append(str(path.relative_to(ROOT)))
            lineage.append(
                {
                    "path": str(path.relative_to(ROOT)),
                    "review_id": document["review_id"],
                    "findings": findings,
                }
            )
    if not (SCRATCH / "lineage.json").exists():
        write("lineage.json", lineage)
    args = [
        "uv",
        "run",
        "python",
        "scripts/record_review.py",
        "inspect",
        "--targets",
        str(manifest),
    ]
    for path in sorted(set(contexts)):
        args.extend(["--input", path])
    result = run("inspect-v2", args)
    if result.returncode:
        raise SystemExit(result.stderr.decode())
    write("inspection.json", json.loads(result.stdout))


def checks():
    commands = [
        ("validate", ["just", "--no-dotenv", "validate", TARGET]),
        (
            "validate-strict",
            [
                "just",
                "--no-dotenv",
                "validate-strict",
                TARGET,
                "--out",
                str(SCRATCH / "strict.tsv"),
            ],
        ),
        ("validate-terms", ["just", "--no-dotenv", "validate-terms", TARGET]),
        ("validate-gtdb", ["just", "--no-dotenv", "validate-gtdb", TARGET]),
        ("validate-gtdb-domain", ["just", "--no-dotenv", "validate-gtdb-domain", TARGET]),
        (
            "validate-history",
            [
                "just",
                "--no-dotenv",
                "validate-history",
                "history/records/Chromobacterium_Gold_Biocyanidation",
            ],
        ),
        (
            "normalize-cache-names",
            ["uv", "run", "python", "scripts/normalize_cache_names.py", "--check"],
        ),
        (
            "validate-references-explained",
            ["just", "--no-dotenv", "validate-references-explained", TARGET],
        ),
        ("audit-network", ["just", "--no-dotenv", "audit-network"]),
        ("check-network-quality", ["just", "--no-dotenv", "check-network-quality"]),
    ]
    for name, command in commands:
        run(name, command)


def replay():
    doc = yaml.safe_load((ROOT / TARGET).read_text())
    cache = (ROOT / "references_cache/doi_10.1007_s10163-014-0276-4.md").read_text()
    source = json.loads((SCRATCH / "publisher.json").read_text())
    body = source["title"] + "\n" + "\n".join(source["abstract"])
    rows = []

    def walk(obj, path=""):
        if isinstance(obj, dict):
            if "snippet" in obj:
                snippet = obj["snippet"]
                rows.append(
                    {
                        "path": path,
                        "snippet": snippet,
                        "raw_publisher": snippet in body,
                        "whitespace_publisher": " ".join(snippet.split()) in " ".join(body.split()),
                        "cache": snippet in cache,
                    }
                )
            for key, value in obj.items():
                walk(value, f"{path}.{key}" if path else key)
        elif isinstance(obj, list):
            for index, value in enumerate(obj):
                walk(value, f"{path}[{index}]")

    walk(doc)
    from communitymech.network.auditor import NetworkIntegrityAuditor

    issues = NetworkIntegrityAuditor().audit_community(ROOT / TARGET)
    write(
        "direct-replay.json",
        {
            "target_sha256": sha((ROOT / TARGET).read_bytes()),
            "publisher_snapshot_sha256": sha((SCRATCH / "publisher.json").read_bytes()),
            "placements": rows,
            "count": len(rows),
            "raw_count": sum(row["raw_publisher"] for row in rows),
            "whitespace_count": sum(row["whitespace_publisher"] for row in rows),
            "target_network_issues": issues,
            "graphs": [
                {
                    "index": i,
                    "name": node["name"],
                    "evidence": node.get("evidence", []),
                    "downstream": node.get("downstream", []),
                }
                for i, node in enumerate(doc["ecological_interactions"])
            ],
        },
    )
    print(
        json.dumps(
            {
                "placements": len(rows),
                "raw": sum(r["raw_publisher"] for r in rows),
                "whitespace": sum(r["whitespace_publisher"] for r in rows),
                "target_network_issues": issues,
            }
        )
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("step", choices=["inspect", "checks", "replay"])
    options = parser.parse_args()
    SCRATCH.mkdir(parents=True, exist_ok=True)
    globals()[options.step]()
