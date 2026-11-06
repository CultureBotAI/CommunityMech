"""Read-only input, source, and native-check receipts for PR 2053 record 175."""

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
SCRATCH = ROOT / ".temp/pr2053/175"
TARGET = "kb/communities/Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml"
COMMON = "kb/taxa/Geobacter_sulfurreducens.yaml"
OLD = "reviews/structured/20261021T212006Z-cellulose-mfc-record-review/review.yaml"
ID = "CommunityMech:000175"
ENV = {
    **os.environ,
    "UV_PROJECT_ENVIRONMENT": str(ROOT.parent / "pr-2034-canary/.venv"),
    "UV_CACHE_DIR": str(ROOT.parent / "pr-2034-canary/.temp/uv-cache"),
    "UV_NO_SYNC": "1",
    "UV_OFFLINE": "1",
    "PYTHONPATH": str(ROOT / "src"),
    "JUST_NO_DOTENV": "true",
}


def now():
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def write(name, obj):
    path = SCRATCH / name
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x") as stream:
        json.dump(obj, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    return path


def run(name, args):
    SCRATCH.mkdir(parents=True, exist_ok=True)
    started = now()
    result = subprocess.run(args, cwd=ROOT, env=ENV, capture_output=True)
    for suffix, raw in [("stdout", result.stdout), ("stderr", result.stderr)]:
        (SCRATCH / f"{name}.{suffix}.txt").write_bytes(raw)
    write(
        name + ".json",
        {
            "command": shlex.join(args),
            "cwd": str(ROOT),
            "environment": {
                key: ENV[key]
                for key in (
                    "UV_PROJECT_ENVIRONMENT",
                    "UV_CACHE_DIR",
                    "UV_NO_SYNC",
                    "UV_OFFLINE",
                    "PYTHONPATH",
                    "JUST_NO_DOTENV",
                )
            },
            "started_at": started,
            "finished_at": now(),
            "exit_code": result.returncode,
            "stdout_sha256": sha(result.stdout),
            "stderr_sha256": sha(result.stderr),
        },
    )
    print(json.dumps({"check": name, "exit_code": result.returncode}), flush=True)
    return result


def inspect(label):
    old = yaml.safe_load((ROOT / OLD).read_text())
    manifest = write(label + "-targets.json", {"targets": old["targets"]})
    paths = {
        "AGENTS.md" if item["path"] == "CLAUDE.md" else item["path"]
        for item in old["source"]["inputs"]
        if item["role"] != "target"
    }
    paths.update([OLD, COMMON, "AGENTS.md", ".temp/pr2053/staleness.json"])
    paths.update(
        str(p.relative_to(ROOT))
        for p in (ROOT / "history/records" / Path(TARGET).stem).glob("*.yaml")
    )
    lineage = []
    for path in sorted((ROOT / "reviews/structured").glob("*/review.yaml")):
        doc = yaml.safe_load(path.read_text())
        findings = [f for f in doc.get("findings", []) if ID in f.get("target_ids", [])]
        if findings:
            paths.add(str(path.relative_to(ROOT)))
            lineage.append(
                {
                    "path": str(path.relative_to(ROOT)),
                    "review_id": doc["review_id"],
                    "findings": findings,
                }
            )
    write(label + "-lineage.json", lineage)
    args = [
        "uv",
        "run",
        "python",
        "scripts/record_review.py",
        "inspect",
        "--targets",
        str(manifest),
    ]
    for path in sorted(paths):
        args += ["--input", path]
    result = run(label + "-inspect", args)
    assert result.returncode == 0, result.stderr.decode()
    write(label + "-inspection.json", json.loads(result.stdout))
    run(label + "-frozen-target", ["git", "show", old["source"]["git_revision"] + ":" + TARGET])
    run(
        label + "-target-diff", ["git", "diff", old["source"]["git_revision"], "HEAD", "--", TARGET]
    )
    run(
        label + "-local-search",
        [
            "rg",
            "--no-ignore",
            "--hidden",
            "-l",
            "CommunityMech:000175|Clostridium_Cellulolyticum_Geobacter|17695929|18725730",
            "references_cache",
            "history",
            "reports/causal_graph_review/decisions",
            "kb/taxa",
        ],
    )


def checks():
    for name in [
        "validate",
        "validate-strict",
        "validate-terms",
        "validate-gtdb",
        "validate-gtdb-domain",
        "validate-history",
        "normalize-cache-names-check",
        "validate-references-explained",
        "audit-network",
        "check-network-quality",
    ]:
        if name == "normalize-cache-names-check":
            args = ["uv", "run", "python", "scripts/normalize_cache_names.py", "--check"]
        else:
            args = ["just", "--no-dotenv", name]
            if name not in {"audit-network", "check-network-quality"}:
                args += [
                    "history/records/" + Path(TARGET).stem if name == "validate-history" else TARGET
                ]
            if name == "validate-strict":
                args += ["--out", str(SCRATCH / "strict.tsv")]
        run(name, args)


def fetch(name, url):
    assert Path(name).name == name and not name.startswith("."), name
    result = run(
        "fetch-" + name,
        [
            "curl",
            "--silent",
            "--show-error",
            "--location",
            "--retry",
            "2",
            "--connect-timeout",
            "20",
            "--max-time",
            "90",
            "--write-out",
            "\nHTTP_STATUS:%{http_code}",
            url,
        ],
    )
    body, status = (
        result.stdout.rsplit(b"\nHTTP_STATUS:", 1)
        if b"\nHTTP_STATUS:" in result.stdout
        else (result.stdout, b"unknown")
    )
    (SCRATCH / name).write_bytes(body)
    write(
        name + ".receipt.json",
        {
            "url": url,
            "accessed_at": now(),
            "curl_exit_code": result.returncode,
            "http_status": status.decode(),
            "sha256": sha(body),
        },
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["inspect", "checks", "fetch"])
    parser.add_argument("--name")
    parser.add_argument("--url")
    parser.add_argument("--label", default="initial")
    args = parser.parse_args()
    if args.mode == "fetch":
        assert args.name and args.url
        fetch(args.name, args.url)
    else:
        if args.mode == "inspect":
            inspect(args.label)
        else:
            checks()
