"""Read-only PR 2043 insect review input/check/source receipts; JSON scratch only."""

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
SCRATCH = ROOT / ".temp/pr2043/insects"
ENV = {
    **os.environ,
    "UV_PROJECT_ENVIRONMENT": str(ROOT.parent / "pr-2034-canary/.venv"),
    "UV_CACHE_DIR": str(ROOT.parent / "pr-2034-canary/.temp/uv-cache"),
    "UV_NO_SYNC": "1",
    "UV_OFFLINE": "1",
    "PYTHONPATH": str(ROOT / "src"),
    "JUST_NO_DOTENV": "true",
}
RECORDS = {
    r["target_id"].split(":")[1]: r
    for r in json.loads((ROOT / ".temp/pr2043/staleness.json").read_text())["records"]
    if r["target_id"] in {"CommunityMech:000006", "CommunityMech:000007", "CommunityMech:000008"}
}


def now():
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x") as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write("\n")
    return path


def run(folder, name, args):
    folder.mkdir(parents=True, exist_ok=True)
    start = now()
    result = subprocess.run(args, cwd=ROOT, env=ENV, capture_output=True)
    for suffix, raw in [("stdout", result.stdout), ("stderr", result.stderr)]:
        (folder / f"{name}.{suffix}.txt").write_bytes(raw)
    write(
        folder / f"{name}.json",
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
    print(
        json.dumps({"folder": folder.name, "check": name, "exit_code": result.returncode}),
        flush=True,
    )
    return result


def inspect(key):
    row = RECORDS[key]
    folder = SCRATCH / key
    old = yaml.safe_load((ROOT / row["review"]).read_text())
    manifest = write(folder / "targets.json", {"targets": old["targets"]})
    paths = {
        "AGENTS.md" if p["path"] == "CLAUDE.md" else p["path"]
        for p in old["source"]["inputs"]
        if p["role"] != "target"
    }
    paths.update([row["review"], "src/communitymech/ontology_adapters.py"])
    paths.update(
        str(p.relative_to(ROOT))
        for p in (ROOT / "history/records" / Path(row["target_path"]).stem).glob("*.yaml")
    )
    lineage = []
    for path in sorted((ROOT / "reviews/structured").glob("*/review.yaml")):
        d = yaml.safe_load(path.read_text())
        findings = [f for f in d.get("findings", []) if row["target_id"] in f.get("target_ids", [])]
        if findings:
            paths.add(str(path.relative_to(ROOT)))
            lineage.append(
                {
                    "path": str(path.relative_to(ROOT)),
                    "review_id": d["review_id"],
                    "findings": findings,
                }
            )
    write(folder / "lineage.json", lineage)
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
    result = run(folder, "inspect", args)
    assert result.returncode == 0, result.stderr.decode()
    write(folder / "inspection.json", json.loads(result.stdout))
    frozen = run(
        folder,
        "frozen-target",
        ["git", "show", old["source"]["git_revision"] + ":" + row["target_path"]],
    )
    assert frozen.returncode == 0
    run(
        folder,
        "target-diff",
        ["git", "diff", old["source"]["git_revision"], "HEAD", "--", row["target_path"]],
    )
    run(
        folder,
        "local-search",
        [
            "rg",
            "--no-ignore",
            "--hidden",
            "-l",
            row["target_id"] + "|" + Path(row["target_path"]).stem + "|30254121",
            "references_cache",
            "history",
            "reports/causal_graph_review/decisions",
            "kb/taxa",
        ],
    )


def checks(key):
    row = RECORDS[key]
    folder = SCRATCH / key
    target = row["target_path"]
    for name in [
        "validate",
        "validate-strict",
        "validate-terms",
        "validate-gtdb",
        "validate-gtdb-domain",
        "validate-history",
        "normalize-cache-names-check",
        "validate-references-explained",
    ]:
        if name == "normalize-cache-names-check":
            args = ["uv", "run", "python", "scripts/normalize_cache_names.py", "--check"]
        else:
            args = [
                "just",
                "--no-dotenv",
                name,
                "history/records/" + Path(target).stem if name == "validate-history" else target,
            ]
            if name == "validate-strict":
                args += ["--out", str(folder / "strict.tsv")]
        run(folder, name, args)


def fetch(name, url):
    folder = SCRATCH / "shared"
    result = run(
        folder,
        "fetch-" + name,
        [
            "curl",
            "--fail",
            "--silent",
            "--show-error",
            "--location",
            "--retry",
            "2",
            "--connect-timeout",
            "20",
            "--max-time",
            "120",
            url,
        ],
    )
    if result.returncode == 0:
        (folder / name).write_bytes(result.stdout)
    write(
        folder / (name + ".receipt.json"),
        {
            "url": url,
            "accessed_at": now(),
            "exit_code": result.returncode,
            "sha256": sha(result.stdout),
        },
    )
    return result


def sources():
    fetch(
        "pubmed.xml",
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=30254121&retmode=xml",
    )
    fetch("crossref.json", "https://api.crossref.org/works/10.1128/mBio.01433-18")
    result = fetch(
        "epmc.json",
        "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:30254121&format=json&resultType=core",
    )
    pmcid = json.loads(result.stdout)["resultList"]["result"][0]["pmcid"]
    fetch("primary.xml", f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML")
    fetch(
        "supplement.zip",
        f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/supplementaryFiles",
    )
    for key in RECORDS:
        model = "MODEL180625000" + str(int(key) - 3)
        fetch(model + ".json", f"https://www.ebi.ac.uk/biomodels/{model}?format=json")
        fetch(
            model + "-files.json",
            f"https://www.ebi.ac.uk/biomodels/model/files/{model}?format=json",
        )


def main():
    p = argparse.ArgumentParser()
    p.add_argument("mode", choices=["inspect", "checks", "sources", "network"])
    p.add_argument("--record", choices=list(RECORDS))
    args = p.parse_args()
    if args.mode in {"inspect", "checks"}:
        assert args.record
        (inspect if args.mode == "inspect" else checks)(args.record)
    elif args.mode == "sources":
        sources()
    else:
        for recipe in ["audit-network", "check-network-quality"]:
            run(SCRATCH / "shared", recipe, ["just", "--no-dotenv", recipe])


if __name__ == "__main__":
    main()
