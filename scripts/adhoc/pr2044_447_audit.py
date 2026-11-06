"""Read-only input, source and native-check receipts for PR 2044 record 447."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shlex
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
SCRATCH = ROOT / ".temp/pr2044/447"
TARGET = "kb/communities/Brocadia_Low_Nitrogen_Anammox_Consortium.yaml"
OLD = "reviews/structured/20261021T133803Z-brocadia-low-nitrogen-anammox-record/review.yaml"
ID = "CommunityMech:000447"
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
    start = now()
    result = subprocess.run(args, cwd=ROOT, env=ENV, capture_output=True)
    for suffix, raw in [("stdout", result.stdout), ("stderr", result.stderr)]:
        (SCRATCH / f"{name}.{suffix}.txt").write_bytes(raw)
    write(
        name + ".json",
        {
            "command": shlex.join(args),
            "cwd": str(ROOT),
            "environment": {
                k: ENV[k]
                for k in [
                    "UV_PROJECT_ENVIRONMENT",
                    "UV_CACHE_DIR",
                    "UV_NO_SYNC",
                    "UV_OFFLINE",
                    "PYTHONPATH",
                    "JUST_NO_DOTENV",
                ]
            },
            "started_at": start,
            "finished_at": now(),
            "exit_code": result.returncode,
            "stdout_sha256": sha(result.stdout),
            "stderr_sha256": sha(result.stderr),
        },
    )
    print(json.dumps({"check": name, "exit_code": result.returncode}), flush=True)
    return result


def inspect():
    old = yaml.safe_load((ROOT / OLD).read_text())
    manifest = write("targets.json", {"targets": old["targets"]})
    paths = {
        "AGENTS.md" if x["path"] == "CLAUDE.md" else x["path"]
        for x in old["source"]["inputs"]
        if x["role"] != "target"
    }
    paths.update([OLD, "src/communitymech/ontology_adapters.py", ".temp/pr2044/staleness.json"])
    paths.update(
        str(p.relative_to(ROOT))
        for p in (ROOT / "history/records" / Path(TARGET).stem).glob("*.yaml")
    )
    lineage = []
    for p in sorted((ROOT / "reviews/structured").glob("*/review.yaml")):
        d = yaml.safe_load(p.read_text())
        findings = [f for f in d.get("findings", []) if ID in f.get("target_ids", [])]
        if findings:
            paths.add(str(p.relative_to(ROOT)))
            lineage.append(
                {
                    "path": str(p.relative_to(ROOT)),
                    "review_id": d["review_id"],
                    "findings": findings,
                }
            )
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
    for path in sorted(paths):
        args += ["--input", path]
    result = run("inspect", args)
    assert result.returncode == 0, result.stderr.decode()
    write("inspection.json", json.loads(result.stdout))
    run("frozen-target", ["git", "show", old["source"]["git_revision"] + ":" + TARGET])
    run("target-diff", ["git", "diff", old["source"]["git_revision"], "HEAD", "--", TARGET])
    run(
        "local-search",
        [
            "rg",
            "--no-ignore",
            "--hidden",
            "-l",
            "CommunityMech:000447|Brocadia_Low_Nitrogen|42323145|135206",
            "references_cache",
            "history",
            "reports/causal_graph_review/decisions",
            "kb/taxa",
        ],
    )
    write(
        "adapter-discovery.json",
        {
            "observed_at": now(),
            "console_script": shutil.which("kg-microbe-sources"),
            "scope": "PATH discovery only; no machine-wide absence assertion. Public structured organism catalog is queried separately.",
        },
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


def sources():
    for name, url in {
        "pubmed.xml": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=42323145&retmode=xml",
        "epmc.json": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42323145%20AND%20SRC:MED&format=json&resultType=core",
        "crossref.json": "https://api.crossref.org/works/10.1016/j.biortech.2026.135206",
        "doi.html": "https://doi.org/10.1016/j.biortech.2026.135206",
        "publisher.html": "https://www.sciencedirect.com/science/article/pii/S0960852426012885",
        "article-api.xml": "https://api.elsevier.com/content/article/pii/S0960852426012885?httpAccept=text/xml",
        "openalex.json": "https://api.openalex.org/works/https://doi.org/10.1016/j.biortech.2026.135206",
        "ncbi-taxonomy.xml": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=380240,380738&retmode=xml",
        "imodulon-catalog.json": "https://imodulondb.org/api/datasets",
    }.items():
        fetch(name, url)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["inspect", "checks", "sources"])
    args = parser.parse_args()
    {"inspect": inspect, "checks": checks, "sources": sources}[args.mode]()
