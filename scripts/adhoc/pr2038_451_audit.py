"""Read-only PR 2038 record 451 audit; writes JSON receipts and source scratch."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shlex
import shutil
import subprocess
import unicodedata
import zipfile
from datetime import datetime, timezone
from pathlib import Path

import yaml
from defusedxml import ElementTree

ROOT = Path(__file__).resolve().parents[2]
SCRATCH = ROOT / ".temp/pr2038/451"
TARGET = "kb/communities/Auxenochlorella_Pseudomonas_Florfenicol_Phycosphere_Coculture.yaml"
OLD = "reviews/structured/20261021T074752Z-auxenochlorella-pseudomonas-record/review.yaml"
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


def write(name, value):
    path = SCRATCH / name
    with path.open("x") as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write("\n")
    return path


def run(name, args):
    start = now()
    result = subprocess.run(args, cwd=ROOT, env=ENV, capture_output=True)
    for suffix, raw in [("stdout", result.stdout), ("stderr", result.stderr)]:
        (SCRATCH / f"{name}.{suffix}.txt").write_bytes(raw)
    write(
        f"{name}.json",
        {
            "command": shlex.join(args),
            "cwd": str(ROOT),
            "environment": {
                key: ENV[key]
                for key in [
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
    paths.update(
        [OLD, "scripts/adhoc/pr2038_451_audit.py", "src/communitymech/ontology_adapters.py"]
    )
    paths.update(
        str(p.relative_to(ROOT))
        for p in (ROOT / "history/records" / Path(TARGET).stem).glob("*.yaml")
    )
    lineage = []
    for path in sorted((ROOT / "reviews/structured").glob("*/review.yaml")):
        doc = yaml.safe_load(path.read_text())
        findings = [
            f for f in doc.get("findings", []) if "CommunityMech:000451" in f.get("target_ids", [])
        ]
        if findings:
            paths.add(str(path.relative_to(ROOT)))
            lineage.append(
                {
                    "path": str(path.relative_to(ROOT)),
                    "review_id": doc["review_id"],
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
    frozen = run("frozen-target", ["git", "show", old["source"]["git_revision"] + ":" + TARGET])
    assert frozen.returncode == 0
    run("target-diff", ["git", "diff", old["source"]["git_revision"], "HEAD", "--", TARGET])
    changes = []

    def compare(left, right, path=""):
        if isinstance(left, dict) and isinstance(right, dict):
            for key in sorted(left.keys() | right.keys()):
                compare(left.get(key), right.get(key), f"{path}.{key}" if path else key)
        elif isinstance(left, list) and isinstance(right, list):
            for i in range(max(len(left), len(right))):
                compare(
                    left[i] if i < len(left) else None,
                    right[i] if i < len(right) else None,
                    f"{path}[{i}]",
                )
        elif left != right:
            changes.append({"path": path, "before": left, "after": right})

    compare(yaml.safe_load(frozen.stdout), yaml.safe_load((ROOT / TARGET).read_text()))
    write("semantic-diff.json", changes)
    canonical = ROOT.parents[1]
    candidates = [
        canonical.parent / "culturebotai-claw",
        canonical.parents[1] / "culturebotai-claw",
    ]
    runner = shutil.which("kg-microbe-sources")
    write(
        "adapter-discovery.json",
        {
            "console_script": runner,
            "bounded_paths": [
                {
                    "path": str(p),
                    "exists": p.exists(),
                    "pyproject_exists": (p / "pyproject.toml").is_file(),
                }
                for p in candidates
            ],
            "scope": "Exact paths inspected including ignored files; no machine-wide absence assertion.",
        },
    )
    if runner:
        run("adapter-catalog", [runner, "imodulondb", "datasets"])
    run(
        "local-search",
        [
            "rg",
            "--no-ignore",
            "--hidden",
            "-l",
            "CommunityMech:000451|Auxenochlorella_Pseudomonas_Florfenicol|41724996|Pseudomonas_sp1|NCBITaxon:3078",
            "references_cache",
            "history",
            "reports/causal_graph_review/decisions",
            "kb/taxa",
        ],
    )


def sources():
    specs = {
        "primary.xml": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13037320/fullTextXML",
        "publication.xml": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=41724996&retmode=xml",
        "crossref.json": "https://api.crossref.org/works/10.1186/s40168-026-02335-7",
        "bioproject.xml": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=bioproject&id=1171391&retmode=xml",
        "supplement.docx": "https://static-content.springer.com/esm/art%3A10.1186%2Fs40168-026-02335-7/MediaObjects/40168_2026_2335_MOESM1_ESM.docx",
        "imodulon-catalog.json": "https://imodulondb.org/api/datasets",
    }
    rows = []
    for filename, url in specs.items():
        result = run(
            "fetch-" + filename,
            [
                "curl",
                "--fail",
                "--silent",
                "--show-error",
                "--location",
                "--retry",
                "3",
                "--connect-timeout",
                "20",
                "--max-time",
                "120",
                url,
            ],
        )
        if result.returncode == 0:
            (SCRATCH / filename).write_bytes(result.stdout)
        rows.append(
            {
                "url": url,
                "path": str((SCRATCH / filename).relative_to(ROOT)),
                "sha256": sha(result.stdout),
                "accessed_at": now(),
                "exit_code": result.returncode,
            }
        )
    write("sources.json", rows)


def checks():
    for name, args in [
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
            ["just", "--no-dotenv", "validate-history", "history/records/" + Path(TARGET).stem],
        ),
        (
            "normalize-cache-names-check",
            ["uv", "run", "python", "scripts/normalize_cache_names.py", "--check"],
        ),
        (
            "validate-references-explained",
            ["just", "--no-dotenv", "validate-references-explained", TARGET],
        ),
        ("audit-network", ["just", "--no-dotenv", "audit-network"]),
        ("check-network-quality", ["just", "--no-dotenv", "check-network-quality"]),
    ]:
        result = run(name, args)
        if name == "normalize-cache-names-check":
            assert result.returncode == 0


def replay():
    from communitymech.network.auditor import NetworkIntegrityAuditor
    from communitymech.ontology_adapters import ontology_adapter

    doc = yaml.safe_load((ROOT / TARGET).read_text())
    xml = ElementTree.parse(SCRATCH / "primary.xml").getroot()
    text = "".join(xml.itertext())
    cache = (ROOT / "references_cache/PMID_41724996.txt").read_text()
    snippets, terms = [], {}

    def normalize(value):
        return " ".join(unicodedata.normalize("NFKC", value).split())

    def walk(obj, path=""):
        if isinstance(obj, dict):
            if "snippet" in obj:
                snippets.append(
                    {
                        "path": path,
                        "snippet": obj["snippet"],
                        "xml": normalize(obj["snippet"]) in normalize(text),
                        "cache": normalize(obj["snippet"]) in normalize(cache),
                    }
                )
            if isinstance(obj.get("term"), dict):
                terms[obj["term"]["id"]] = obj["term"]["label"]
            for key, value in obj.items():
                walk(value, f"{path}.{key}" if path else key)
        elif isinstance(obj, list):
            for i, value in enumerate(obj):
                walk(value, f"{path}[{i}]")

    walk(doc)
    authorities = []
    for curie, label in sorted(terms.items()):
        adapter = ontology_adapter(curie.split(":")[0])
        actual = adapter.label(curie) if adapter is not None else None
        authorities.append(
            {
                "id": curie,
                "record_label": label,
                "authority_label": actual,
                "matches": actual == label,
            }
        )
    write("ontology-authorities.json", authorities)
    chebi = ontology_adapter("CHEBI")
    write(
        "chemical-authorities.json",
        [
            {"id": c, "label": chebi.label(c), "definition": chebi.definition(c)}
            for c in ["CHEBI:17310", "CHEBI:87185", "CHEBI:60159"]
        ],
    )
    write(
        "snippet-replay.json",
        {
            "count": len(snippets),
            "xml_matches": sum(s["xml"] for s in snippets),
            "cache_matches": sum(s["cache"] for s in snippets),
            "rows": snippets,
        },
    )
    write(
        "primary-sections.json",
        [
            {"id": sec.get("id"), "text": "".join(sec.itertext())}
            for sec in xml.findall(".//body/sec")
        ],
    )
    write("target-network.json", NetworkIntegrityAuditor().audit_community(ROOT / TARGET))
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    with zipfile.ZipFile(SCRATCH / "supplement.docx") as archive:
        root = ElementTree.fromstring(archive.read("word/document.xml"))
    blocks = []
    for i, child in enumerate(root.find("w:body", ns)):
        if child.tag.endswith("}tbl"):
            rows = [
                ["".join(cell.itertext()) for cell in row.findall("w:tc", ns)]
                for row in child.findall("w:tr", ns)
            ]
            blocks.append({"block": i, "kind": "table", "rows": rows})
        else:
            blocks.append({"block": i, "kind": "paragraph", "text": "".join(child.itertext())})
    write("supplement-blocks.json", blocks)
    print(
        json.dumps(
            {
                "snippets": len(snippets),
                "xml_matches": sum(s["xml"] for s in snippets),
                "terms": len(terms),
                "term_matches": all(t["matches"] for t in authorities),
            }
        )
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["inspect", "sources", "checks", "replay"])
    arguments = parser.parse_args()
    SCRATCH.mkdir(parents=True, exist_ok=True)
    globals()[arguments.mode]()
