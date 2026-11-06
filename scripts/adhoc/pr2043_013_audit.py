"""Read-only receipts for PR2043 sponge review; writes JSON/text scratch only."""

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import yaml
from lxml import etree

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / ".temp/pr2043/013"
PYTHON = (
    "/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/"
    ".temp/pr-2034-canary/.venv/bin/python"
)
ENV = dict(
    os.environ,
    UV_PROJECT_ENVIRONMENT=str(Path(PYTHON).parents[1]),
    UV_CACHE_DIR=(
        "/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/"
        ".temp/pr-2034-canary/.temp/uv-cache"
    ),
    UV_NO_SYNC="1",
    UV_OFFLINE="1",
    PYTHONPATH="src",
    JUST_NO_DOTENV="true",
)
TARGET = "kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml"
URLS = {
    "article.xml": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11685487/fullTextXML",
    "pubmed.xml": (
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?"
        "db=pubmed&id=39738126,39604529&retmode=xml"
    ),
    "biomodels.json": "https://www.ebi.ac.uk/biomodels/MODEL2407300002?format=json",
    "biomodels-files.json": "https://www.ebi.ac.uk/biomodels/model/files/MODEL2407300002?format=json",
    "zenodo.json": "https://zenodo.org/api/records/14030749",
    "project.xml": (
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?"
        "db=bioproject&id=602572&retmode=xml"
    ),
    "massive.html": "https://massive.ucsd.edu/ProteoSAFe/dataset.jsp?accession=MSV000083743",
    "sty8-tag-correct.json": "https://api.github.com/repos/zhssakura/STY8/git/ref/tags/v1.0.0",
    "sty8-tree-correct.json": (
        "https://api.github.com/repos/zhssakura/STY8/git/trees/"
        "17fd9c4eb5bd1f4cdf2c6402a2cdf3958e380546?recursive=1"
    ),
}


def target_audit():
    """Measure current bytes and exact snippets; does not decide source support."""
    sys.path.insert(0, str(ROOT / "src"))
    from communitymech.network.auditor import NetworkIntegrityAuditor
    from communitymech.ontology_adapters import ontology_adapter

    target = ROOT / TARGET
    data = yaml.safe_load(target.read_text())
    article = etree.parse(str(OUT / "article.xml"))
    body = " ".join(article.xpath("//article//text()"))

    def normalize(value):
        return re.sub(r"\s+", " ", value).strip().lower()

    snippets, terms = [], []

    def walk(value, path=""):
        if isinstance(value, dict):
            if "snippet" in value:
                snippets.append(
                    {
                        "path": path + ".snippet",
                        "matched": normalize(value["snippet"]) in normalize(body),
                        "reference": value["reference"],
                    }
                )
            if isinstance(value.get("term"), dict):
                terms.append(value["term"])
            for key, child in value.items():
                walk(child, path + "." + key)
        elif isinstance(value, list):
            for index, child in enumerate(value):
                walk(child, path + f"[{index}]")

    walk(data)
    authorities = []
    for curie, label in sorted({(term["id"], term["label"]) for term in terms}):
        adapter = ontology_adapter(curie.split(":")[0])
        actual = adapter.label(curie) if adapter else None
        authorities.append({"id": curie, "label": label, "authority_label": actual})
    issues = NetworkIntegrityAuditor().audit_community(target)
    nodes = data["ecological_interactions"]
    node_evidence = sum(len(node.get("evidence", [])) for node in nodes)
    completeness = 50 + 5 + 10 + 5 + 5 + 5
    uncapped_quality = 100 - 10 * 2 - 2 * 3 + 20 * min(node_evidence / len(nodes) / 2, 1) + 15
    return {
        "target_sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
        "snippets": snippets,
        "term_occurrences": terms,
        "ontology_authorities": authorities,
        "network_issues": issues,
        "nodes": len(nodes),
        "arrows": sum(len(node.get("downstream", [])) for node in nodes),
        "node_evidence": node_evidence,
        "completeness": completeness,
        "validation_quality": min(100, max(0, uncapped_quality)),
        "validation_quality_uncapped": uncapped_quality,
        "P1": 0,
        "P2": 2,
        "P3": 3,
        "P4": 0,
        "note": "Severity counts are supplied by source assessment, not inferred from native checks.",
    }


def now():
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def run(name, command):
    start = now()
    proc = subprocess.run(command, cwd=ROOT, env=ENV, capture_output=True, text=True)
    (OUT / (name + ".stdout")).write_text(proc.stdout)
    (OUT / (name + ".stderr")).write_text(proc.stderr)
    return {
        "name": name,
        "command": command,
        "started_at": start,
        "finished_at": now(),
        "exit_code": proc.returncode,
        "stdout_sha256": hashlib.sha256(proc.stdout.encode()).hexdigest(),
        "stderr_sha256": hashlib.sha256(proc.stderr.encode()).hexdigest(),
    }


def fetch(item):
    name, url = item
    receipt = run(name, ["curl", "-LsS", "--fail", "--max-time", "50", "-o", str(OUT / name), url])
    receipt["url"] = url
    if (OUT / name).exists():
        receipt["sha256"] = hashlib.sha256((OUT / name).read_bytes()).hexdigest()
        receipt["bytes"] = (OUT / name).stat().st_size
    return receipt


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["fetch", "checks", "inspect", "audit"])
    args = parser.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    if args.mode == "audit":
        receipt = target_audit()
        (OUT / "target-audit.json").write_text(json.dumps(receipt, indent=2) + "\n")
        print(json.dumps({key: receipt[key] for key in ["nodes", "arrows", "completeness"]}))
        return
    if args.mode == "fetch":
        with ThreadPoolExecutor(max_workers=4) as pool:
            receipts = list(pool.map(fetch, URLS.items()))
    elif args.mode == "checks":
        commands = [
            (name, ["just", "--no-dotenv", name, TARGET])
            for name in [
                "validate",
                "validate-terms",
                "validate-gtdb",
                "validate-gtdb-domain",
                "validate-references-explained",
            ]
        ]
        commands += [
            (
                "validate-strict",
                [
                    "just",
                    "--no-dotenv",
                    "validate-strict",
                    TARGET,
                    "--out",
                    str(OUT / "strict.tsv"),
                ],
            ),
            (
                "validate-history",
                ["just", "--no-dotenv", "validate-history", "history/records/" + Path(TARGET).stem],
            ),
            (
                "normalize-cache-names",
                [PYTHON, "scripts/normalize_cache_names.py", "--check"],
            ),
        ]
        receipts = [run(name, command) for name, command in commands]
    else:
        command = [
            PYTHON,
            "scripts/record_review.py",
            "inspect",
            "--targets",
            str(OUT / "targets.json"),
        ]
        for path in json.loads((OUT / "inputs.json").read_text()):
            command += ["--input", path]
        receipts = [run("inspect-final", command)]
    (OUT / (args.mode + "-receipts.json")).write_text(json.dumps(receipts, indent=2) + "\n")
    print(json.dumps([{k: r.get(k) for k in ["name", "exit_code", "bytes"]} for r in receipts]))


if __name__ == "__main__":
    main()
