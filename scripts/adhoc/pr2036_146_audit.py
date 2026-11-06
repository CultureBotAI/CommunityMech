"""Read-only PR2036/146 inspection; writes JSON receipts and public-source scratch."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shlex
import shutil
import subprocess
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

import yaml
from defusedxml import ElementTree

ROOT = Path(__file__).resolve().parents[2]
SCRATCH = ROOT / ".temp/pr2036/146"
TARGET = "kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml"
OLD = "reviews/structured/20261020T073708Z-anammox-granule-record/review.yaml"
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
    started = now()
    result = subprocess.run(args, cwd=ROOT, env=ENV, capture_output=True)
    for suffix, raw in [("stdout", result.stdout), ("stderr", result.stderr)]:
        (SCRATCH / f"{name}.{suffix}.txt").write_bytes(raw)
    receipt = {
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
        "started_at": started,
        "finished_at": now(),
        "exit_code": result.returncode,
        "stdout_sha256": sha(result.stdout),
        "stderr_sha256": sha(result.stderr),
    }
    write(f"{name}.json", receipt)
    print(json.dumps({"name": name, "exit_code": result.returncode}), flush=True)
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
        [
            OLD,
            "scripts/record_review.py",
            "scripts/adhoc/pr2036_146_audit.py",
            "src/communitymech/ontology_adapters.py",
        ]
    )
    paths.update(
        str(p.relative_to(ROOT))
        for p in (ROOT / "history/records/Anammox_Granule_Metabolic_Interaction_Community").glob(
            "*.yaml"
        )
    )
    lineage = []
    for path in sorted((ROOT / "reviews/structured").glob("*/review.yaml")):
        doc = yaml.safe_load(path.read_text())
        findings = [
            f for f in doc.get("findings", []) if "CommunityMech:000146" in f.get("target_ids", [])
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
    result = run(
        "target-diff", ["git", "diff", old["source"]["git_revision"], "HEAD", "--", TARGET]
    )
    assert result.returncode == 0
    frozen = run("frozen-target", ["git", "show", old["source"]["git_revision"] + ":" + TARGET])
    assert frozen.returncode == 0
    before = yaml.safe_load(frozen.stdout)
    after = yaml.safe_load((ROOT / TARGET).read_text())
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

    compare(before, after)
    write("target-semantic-diff.json", changes)
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
            "bounded_local_roots": [
                {
                    "path": str(p),
                    "exists": p.exists(),
                    "pyproject_exists": (p / "pyproject.toml").is_file(),
                }
                for p in candidates
            ],
            "scope": "Exact paths inspected, including gitignored paths; not an exhaustive machine-wide absence claim.",
        },
    )
    if runner:
        run("adapter-catalog", [runner, "imodulondb", "datasets"])


def sources():
    specs = {
        "primary.xml": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5460018/fullTextXML",
        "publication.xml": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=28561030&retmode=xml",
        "crossref.json": "https://api.crossref.org/works/10.1038/ncomms15416",
        "bioproject.json": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=bioproject&id=343219&retmode=json",
        "biosamples.xml": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=SAMN05785375,SAMN05785376,SAMN05785373&retmode=xml",
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
        assert result.returncode == 0, result.stderr.decode()
        (SCRATCH / filename).write_bytes(result.stdout)
        rows.append(
            {
                "url": url,
                "path": str((SCRATCH / filename).relative_to(ROOT)),
                "sha256": sha(result.stdout),
                "accessed_at": now(),
            }
        )
    write("sources.json", rows)


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
                "history/records/Anammox_Granule_Metabolic_Interaction_Community",
            ],
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
    ]
    for name, command in commands:
        result = run(name, command)
        if name == "normalize-cache-names-check":
            assert result.returncode == 0, "Reference validation needs clean read-only preflight"


def replay():
    from communitymech.network.auditor import NetworkIntegrityAuditor
    from communitymech.ontology_adapters import ontology_adapter

    doc = yaml.safe_load((ROOT / TARGET).read_text())
    xml = ElementTree.parse(SCRATCH / "primary.xml").getroot()
    text = "".join(xml.itertext())
    cache = (ROOT / "references_cache/doi_10.1038_ncomms15416.txt").read_text()
    pubmed = "".join(ElementTree.parse(SCRATCH / "publication.xml").getroot().itertext())

    def normalize(s):
        return " ".join(unicodedata.normalize("NFKC", s).split())

    snippets = []
    terms = {}

    def walk(obj, path=""):
        if isinstance(obj, dict):
            if "snippet" in obj:
                snippet = obj["snippet"]
                snippets.append(
                    {
                        "path": path,
                        "snippet": snippet,
                        "xml": normalize(snippet) in normalize(text),
                        "cache": normalize(snippet) in normalize(cache),
                        "pubmed": normalize(snippet) in normalize(pubmed),
                    }
                )
            if "term" in obj and isinstance(obj["term"], dict):
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
    sections = [
        {
            "id": sec.get("id"),
            "title": "".join(sec.find("title").itertext()) if sec.find("title") is not None else "",
            "text": "".join(sec.itertext()),
        }
        for sec in xml.findall(".//body/sec")
    ]
    write("primary-sections.json", sections)
    write(
        "snippet-replay.json",
        {
            "source_sha256": sha((SCRATCH / "primary.xml").read_bytes()),
            "count": len(snippets),
            "xml_matches": sum(x["xml"] for x in snippets),
            "cache_matches": sum(x["cache"] for x in snippets),
            "rows": snippets,
        },
    )
    write("ontology-authorities.json", authorities)
    adapter = ontology_adapter("NCBITaxon")
    ancestry = []
    for curie in ["NCBITaxon:1334117", "NCBITaxon:795749", "NCBITaxon:1090"]:
        ancestors = sorted(set(adapter.ancestors([curie], predicates=["rdfs:subClassOf"])))
        ancestry.append(
            {
                "id": curie,
                "label": adapter.label(curie),
                "ancestors": [{"id": a, "label": adapter.label(a)} for a in ancestors],
            }
        )
    write("source-family-ancestry.json", ancestry)
    extra_terms = []
    envo = ontology_adapter("ENVO")
    for curie in ["ENVO:00002123", "ENVO:01001405"]:
        extra_terms.append({"id": curie, "label": envo.label(curie)})
    write("alternative-settings.json", extra_terms)
    write("target-network.json", NetworkIntegrityAuditor().audit_community(ROOT / TARGET))
    print(
        json.dumps(
            {
                "snippets": len(snippets),
                "xml_matches": sum(x["xml"] for x in snippets),
                "terms": len(terms),
                "terms_match": all(x["matches"] for x in authorities),
            }
        )
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["inspect", "sources", "checks", "replay"])
    args = parser.parse_args()
    SCRATCH.mkdir(parents=True, exist_ok=True)
    globals()[args.mode]()
