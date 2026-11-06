"""Capture read-only PR 2035 / record 434 review inputs and validation receipts."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / ".temp/pr2035/434"
OLD = "reviews/structured/20261020T035434Z-acidic-nitrification-record/review.yaml"
TARGET = "kb/communities/Acidic_Nitrification_Minimal_Consortium.yaml"
RUNTIME = ROOT.parent / "pr-2034-canary"
ENV = dict(os.environ)
ENV.update(
    UV_PROJECT_ENVIRONMENT=str(RUNTIME / ".venv"),
    UV_CACHE_DIR=str(RUNTIME / ".temp/uv-cache"),
    UV_NO_SYNC="1",
    UV_OFFLINE="1",
    PYTHONPATH="src",
    JUST_NO_DOTENV="true",
)


def now():
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def write_json(path, value):
    with path.open("x") as stream:
        json.dump(value, stream, indent=2)
        stream.write("\n")


def run(name, command):
    start = now()
    result = subprocess.run(command, cwd=ROOT, env=ENV, capture_output=True, check=False)
    (OUT / f"{name}.stdout").write_bytes(result.stdout)
    (OUT / f"{name}.stderr").write_bytes(result.stderr)
    receipt = {
        "name": name,
        "command": command,
        "started_at": start,
        "finished_at": now(),
        "exit_code": result.returncode,
        "stdout_sha256": digest(result.stdout),
        "stderr_sha256": digest(result.stderr),
        "stdout": result.stdout.decode(errors="replace"),
        "stderr": result.stderr.decode(errors="replace"),
    }
    write_json(OUT / f"{name}.json", receipt)
    print(name, result.returncode, flush=True)
    return receipt


def inspect(name):
    prior = yaml.safe_load((ROOT / OLD).read_text())
    manifest = OUT / "targets.json"
    if not manifest.exists():
        write_json(manifest, {"targets": prior["targets"]})
    paths = {
        "AGENTS.md" if item["path"] == "CLAUDE.md" else item["path"]
        for item in prior["source"]["inputs"]
        if item["path"] != TARGET
    }
    paths.update(
        str(path.relative_to(ROOT))
        for path in (ROOT / "history/records/Acidic_Nitrification_Minimal_Consortium").glob(
            "*.yaml"
        )
    )
    paths.update({OLD, "scripts/record_review.py", str(Path(__file__).relative_to(ROOT))})
    paths.update(
        {
            "reports/causal_graph_review/decisions/20261021-stage5-review-remediation.yaml",
            "reports/causal_graph_review/decisions/20261031-c3s5-review-remediation.yaml",
        }
    )
    builder = ROOT / "scripts/adhoc/pr2035_434_review.py"
    if builder.exists():
        paths.add(str(builder.relative_to(ROOT)))
    command = [
        "uv",
        "run",
        "python",
        "scripts/record_review.py",
        "inspect",
        "--targets",
        str(manifest),
    ]
    for path in sorted(paths):
        command.extend(["--input", path])
    return run(name, command)


SOURCES = {
    "pubmed": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=42762737&retmode=xml",
    "europepmc": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42762737&format=json&resultType=core",
    "crossref": "https://api.crossref.org/works/10.1016/j.watres.2026.126966",
    "publisher": "https://www.sciencedirect.com/science/article/pii/S0043135426016374",
    "publisher-xml": "https://api.elsevier.com/content/article/PII:S0043135426016374?httpAccept=text/xml",
    "taxonomy": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=taxonomy&term=Nitrosoglobus%20kelleri&retmode=json",
    "imodulondb": "https://imodulondb.org/api/datasets",
}


def fetch(item):
    name, url = item
    result = {"name": name, "url": url, "started_at": now()}
    request = urllib.request.Request(
        url, headers={"User-Agent": "CommunityMech source verification"}
    )
    try:
        response = urllib.request.urlopen(request, timeout=45)
    except urllib.error.HTTPError as error:
        response = error
    except Exception as error:
        result.update(error=repr(error), finished_at=now())
        write_json(OUT / f"source-{name}.json", result)
        print(name, result["error"], flush=True)
        return result
    with response:
        body = response.read()
        (OUT / f"source-{name}.body").write_bytes(body)
        result.update(
            status=response.status,
            final_url=response.url,
            content_type=response.headers.get("Content-Type"),
            finished_at=now(),
            sha256=digest(body),
            size_bytes=len(body),
        )
    write_json(OUT / f"source-{name}.json", result)
    print(name, result["status"], result["size_bytes"], flush=True)
    return result


def checks():
    recipes = [
        ("validate", [TARGET]),
        ("validate-strict", [TARGET, "--out", str(OUT / "strict.tsv")]),
        ("validate-terms", [TARGET]),
        ("validate-gtdb", [TARGET]),
        ("validate-gtdb-domain", [TARGET]),
        ("validate-history", ["history/records/Acidic_Nitrification_Minimal_Consortium"]),
        ("audit-network", []),
        ("check-network-quality", []),
    ]
    for name, arguments in recipes:
        run(name, ["just", "--no-dotenv", name, *arguments])
    preflight = run(
        "cache-preflight", ["uv", "run", "python", "scripts/normalize_cache_names.py", "--check"]
    )
    if preflight["exit_code"] == 0:
        run(
            "validate-references-explained",
            ["just", "--no-dotenv", "validate-references-explained", TARGET],
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["inspect-initial", "inspect-final", "sources", "checks"])
    args = parser.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    if args.mode.startswith("inspect"):
        inspect(args.mode)
    elif args.mode == "sources":
        with ThreadPoolExecutor(max_workers=3) as pool:
            list(pool.map(fetch, SOURCES.items()))
    else:
        checks()


if __name__ == "__main__":
    main()
