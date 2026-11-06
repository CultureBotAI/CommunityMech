"""Capture reproducible, read-only evidence for the PR 2034 record-321 successor."""

from __future__ import annotations

import concurrent.futures
import datetime as dt
import hashlib
import json
import os
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRATCH = ROOT / ".temp/pr2034/321"
TARGET = "data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml"
OLD = "reviews/structured/20261019T074329Z-kefir-rothia-model-record/review.yaml"
PYTHON = "/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.venv/bin/python"


def now():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def digest(path):
    data = Path(path).read_bytes()
    return {
        "path": str(Path(path).relative_to(ROOT)),
        "sha256": hashlib.sha256(data).hexdigest(),
        "bytes": len(data),
    }


def write(name, value):
    SCRATCH.mkdir(parents=True, exist_ok=True)
    path = SCRATCH / name
    with path.open("x") as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write("\n")
    return digest(path)


def environment():
    env = os.environ.copy()
    env.update(
        UV_PROJECT_ENVIRONMENT=str(Path(PYTHON).parent.parent),
        UV_NO_SYNC="1",
        UV_CACHE_DIR=str(ROOT / ".temp/uv-cache"),
        PYTHONPATH=str(ROOT / "src"),
        JUST_NO_DOTENV="true",
    )
    return env


def run(name, command):
    started = now()
    result = subprocess.run(command, cwd=ROOT, env=environment(), capture_output=True, text=True)
    receipt = {
        "name": name,
        "command": command,
        "cwd": str(ROOT),
        "started_at": started,
        "finished_at": now(),
        "exit_code": result.returncode,
        "environment_overrides": {
            k: environment()[k]
            for k in [
                "UV_PROJECT_ENVIRONMENT",
                "UV_NO_SYNC",
                "UV_CACHE_DIR",
                "PYTHONPATH",
                "JUST_NO_DOTENV",
            ]
        },
        "stdout": result.stdout,
        "stderr": result.stderr,
    }
    pin = write(name + ".json", receipt)
    print(json.dumps({"name": name, "exit_code": result.returncode, "receipt": pin}), flush=True)
    return receipt


def inspect():
    # CLAUDE.md is a symlink to this regular AGENTS.md; the native helper forbids symlinks.
    paths = [
        "AGENTS.md",
        "docs/record-reviews.md",
        "docs/record-review-profile.md",
        "conf/record_review.yaml",
        "conf/reference_validator.yaml",
        "justfile",
        "schema/record_review.yaml",
        "scripts/record_review.py",
        "src/communitymech/schema/communitymech.yaml",
        "src/communitymech/schema/mech_shared.yaml",
        "src/communitymech/schema/history.yaml",
        ".claude/skills/review-yaml-record/SKILL.md",
        ".claude/skills/review-communities/reference/execution-protocol.md",
        ".claude/skills/review-communities/reference/validation-rules.md",
        ".claude/skills/review-communities/reference/metrics-and-reports.md",
        ".claude/skills/curate-yaml-record/references/review-checklist.md",
        OLD,
        "references_cache/PMID_28963201.txt",
        "references_cache/PMID_33398099.md",
        "reports/causal_graph_review/decisions/20261005-six-records-batch3.yaml",
        "reports/causal_graph_review/decisions/20261021-stage5-review-remediation.yaml",
    ]
    paths += [
        str(p.relative_to(ROOT))
        for p in sorted(
            (ROOT / "history/records/BioModels_MODEL2204300002_Kefir_Rothia_Model").glob("*.yaml")
        )
    ]
    targets = {
        "targets": [
            {
                "target_id": "CommunityMech:000321",
                "path": TARGET,
                "label": "BioModels MODEL2204300002 Kefir Rothia Model",
                "kind": "maintained",
                "owner_paths": [
                    {
                        "repository": "CultureBotAI/CommunityMech",
                        "path": TARGET,
                        "role": "canonical_record",
                    }
                ],
            }
        ]
    }
    if not (SCRATCH / "targets.json").exists():
        write("targets.json", targets)
    else:
        assert json.loads((SCRATCH / "targets.json").read_text()) == targets
    write("context-inputs-v2.json", paths)
    command = [
        "uv",
        "run",
        "python",
        "scripts/record_review.py",
        "inspect",
        "--targets",
        str(SCRATCH / "targets.json"),
    ]
    for path in paths:
        command += ["--input", path]
    receipt = run("inspect-command-v2", command)
    if receipt["exit_code"]:
        raise SystemExit(receipt["exit_code"])
    write("inspect.json", json.loads(receipt["stdout"]))


def validators():
    jobs = [
        (name, ["just", "--no-dotenv", name, TARGET])
        for name in ["validate", "validate-terms", "validate-gtdb", "validate-gtdb-domain"]
    ]
    jobs += [
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
        (
            "validate-history",
            [
                "just",
                "--no-dotenv",
                "validate-history",
                "history/records/BioModels_MODEL2204300002_Kefir_Rothia_Model",
            ],
        ),
    ]
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        list(pool.map(lambda job: run(*job), jobs))
    # This documented recipe also normalizes cache filenames. It is run separately.
    run(
        "validate-references-explained",
        ["just", "--no-dotenv", "validate-references-explained", TARGET],
    )


SOURCES = {
    "biomodels-metadata.json": "https://www.biomodels.org/MODEL2204300002?format=json",
    "biomodels-model.xml": "https://www.biomodels.org/model/download/MODEL2204300002?filename=MODEL2204300002.xml",
    "authors-species.tsv": "https://raw.githubusercontent.com/cdanielmachado/kefir_paper/master/species_list.tsv",
    "authors-readme.md": "https://raw.githubusercontent.com/cdanielmachado/kefir_paper/master/README.md",
    "authors-model.xml": "https://raw.githubusercontent.com/cdanielmachado/kefir_paper/master/models/156_03182016.xml",
    "nuccore.gb": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NDFM00000000&rettype=gb&retmode=text",
    "ena.embl": "https://www.ebi.ac.uk/ena/browser/api/embl/NDFM00000000.1?download=false",
    "biosample.xml": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=SAMN06718477&retmode=xml",
    "assembly.json": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=assembly&id=1163481&retmode=json",
}


def fetch_one(item):
    name, url = item
    receipt = {"url": url, "started_at": now()}
    try:
        request = urllib.request.Request(
            url, headers={"User-Agent": "CommunityMech record review (public evidence)"}
        )
        with urllib.request.urlopen(request, timeout=45) as response:
            data = response.read()
            receipt.update(
                status=response.status,
                final_url=response.url,
                content_type=response.headers.get("Content-Type"),
            )
        path = SCRATCH / "sources" / name
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("xb") as stream:
            stream.write(data)
        receipt["snapshot"] = digest(path)
    except Exception as error:
        receipt["error"] = str(error)
    receipt["finished_at"] = now()
    print(json.dumps({"source": name, **receipt}), flush=True)
    return receipt


def fetch():
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        receipts = list(pool.map(fetch_one, SOURCES.items()))
    name = (
        "source-retrieval-v2.json"
        if (SCRATCH / "source-retrieval.json").exists()
        else "source-retrieval.json"
    )
    write(name, receipts)


if __name__ == "__main__":
    assert Path.cwd() == ROOT
    {"inspect": inspect, "validators": validators, "fetch": fetch}[sys.argv[1]]()
