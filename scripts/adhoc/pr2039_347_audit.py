"""Read-only source/check receipts for the PR 2039 record 347 review refresh."""

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
from bs4 import BeautifulSoup
from defusedxml import ElementTree

ROOT = Path(__file__).resolve().parents[2]
SCRATCH = ROOT / ".temp/pr2039/347"
TARGET = "kb/communities/Bacillus_siamensis_vallismortis_HT_Masson_Pine_SynCom.yaml"
OLD = "reviews/structured/20261021T092904Z-masson-pine-ht-syncom-record/review.yaml"
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
    write(
        f"{name}.json",
        {
            "command": shlex.join(args),
            "cwd": str(ROOT),
            "environment": {
                key: ENV[key]
                for key in ["UV_PROJECT_ENVIRONMENT", "UV_CACHE_DIR", "UV_NO_SYNC", "UV_OFFLINE"]
            }
            | {"PYTHONPATH": ENV["PYTHONPATH"], "JUST_NO_DOTENV": "true"},
            "started_at": started,
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
        [OLD, str(Path(__file__).relative_to(ROOT)), "src/communitymech/ontology_adapters.py"]
    )
    paths.update(
        str(p.relative_to(ROOT))
        for p in (ROOT / "history/records" / Path(TARGET).stem).glob("*.yaml")
    )
    lineage = []
    for path in sorted((ROOT / "reviews/structured").glob("*/review.yaml")):
        doc = yaml.safe_load(path.read_text())
        findings = [
            f for f in doc.get("findings", []) if "CommunityMech:000347" in f.get("target_ids", [])
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
    write(
        "adapter-discovery.json",
        {
            "console_script": shutil.which("kg-microbe-sources"),
            "bounded_paths": [{"path": str(p), "exists": p.exists()} for p in candidates],
            "scope": "Exact paths include ignored files; no machine-wide absence claim.",
        },
    )
    run(
        "local-search",
        [
            "rg",
            "--no-ignore",
            "--hidden",
            "-l",
            "CommunityMech:000347|Bacillus_siamensis_vallismortis_HT|42144568|OQ996945|OQ996934|PRJNA1166410",
            "references_cache",
            "history",
            "reports/causal_graph_review/decisions",
            "kb/taxa",
        ],
    )


def sources():
    urls = {
        "primary.xml": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13453252/fullTextXML",
        "publication.xml": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=42144568&retmode=xml",
        "crossref.json": "https://api.crossref.org/works/10.1002/ps.70924",
        "bioproject.xml": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=bioproject&id=1166410&retmode=xml",
        "OQ996945.embl": "https://www.ebi.ac.uk/ena/browser/api/embl/OQ996945.1?download=false",
        "OQ996934.embl": "https://www.ebi.ac.uk/ena/browser/api/embl/OQ996934.1?download=false",
        "imodulon-catalog.json": "https://imodulondb.org/api/datasets",
    }
    for name, url in urls.items():
        run(
            "fetch-" + name,
            [
                "curl",
                "-L",
                "--fail",
                "--retry",
                "2",
                "--max-time",
                "60",
                "-o",
                str(SCRATCH / name),
                url,
            ],
        )


def checks():
    for name in [
        "validate",
        "validate-strict",
        "validate-terms",
        "validate-gtdb",
        "validate-gtdb-domain",
        "validate-references-explained",
    ]:
        args = ["just", "--no-dotenv", name, TARGET]
        if name == "validate-strict":
            args += ["--out", str(SCRATCH / "strict.tsv")]
        run(name, args)
    run(
        "validate-history",
        ["just", "--no-dotenv", "validate-history", "history/records/" + Path(TARGET).stem],
    )
    run(
        "normalize-cache-names-check",
        ["uv", "run", "python", "scripts/normalize_cache_names.py", "--check"],
    )
    for name in ["audit-network", "check-network-quality"]:
        run(name, ["just", "--no-dotenv", name])


def fallback():
    urls = {
        "pmc-main.html": "https://pmc.ncbi.nlm.nih.gov/articles/PMC13453252/",
        "pmc-efetch.xml": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=13453252",
        "europepmc-main.html": "https://europepmc.org/articles/PMC13453252",
        "publisher-main.html": "https://scijournals.onlinelibrary.wiley.com/doi/full/10.1002/ps.70924",
        "pmc-bioc.xml": "https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/PMC13453252/unicode",
    }
    for name, url in urls.items():
        run(
            "fetch-" + name,
            [
                "curl",
                "-L",
                "--fail",
                "--retry",
                "1",
                "--max-time",
                "40",
                "-o",
                str(SCRATCH / name),
                url,
            ],
        )


def assets():
    shared = ROOT / ".temp/pr2039/adversarial/347.html"
    raw = shared.read_bytes()
    assert sha(raw) == "117f9510e9b94be6721d5a2ebe293472d5693f802f0dd7655b7be4dc315dbf07"
    (SCRATCH / "primary.html").write_bytes(raw)
    write(
        "shared-retrieval.json",
        {
            "source": str(shared.relative_to(ROOT)),
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC13453252/",
            "retrieved_no_later_than": "2026-11-06T02:42:17.671292Z",
            "copied_at": now(),
            "sha256": sha(raw),
            "scope": "Public primary source retrieved by separate reviewer, independently read by this author. No independent approval claimed.",
        },
    )
    soup = BeautifulSoup(raw, "html.parser")
    for image in soup.find_all("img"):
        if image.get("alt") in ["Figure 4", "Figure 5", "Figure 6", "Figure 7"]:
            name = image["alt"].replace(" ", "-").lower() + ".jpg"
            run(
                "fetch-" + name,
                [
                    "curl",
                    "-L",
                    "--fail",
                    "--retry",
                    "2",
                    "--max-time",
                    "45",
                    "-o",
                    str(SCRATCH / name),
                    image["src"],
                ],
            )
    urls = sorted(
        {
            "https://pmc.ncbi.nlm.nih.gov" + a["href"]
            for a in soup.find_all("a", href=True)
            if a["href"].endswith(".docx")
        }
    )
    for url in urls:
        name = url.rsplit("/", 1)[-1]
        run(
            "fetch-" + name,
            ["curl", "-L", "--fail", "--max-time", "35", "-o", str(SCRATCH / name), url],
        )


def replay():
    from communitymech.network.auditor import NetworkIntegrityAuditor
    from communitymech.ontology_adapters import ontology_adapter

    doc = yaml.safe_load((ROOT / TARGET).read_text())
    soup = BeautifulSoup((SCRATCH / "primary.html").read_bytes(), "html.parser")
    article = soup.find("article") or soup.find("main") or soup
    text = article.get_text(" ", strip=True)
    pubmed = ElementTree.parse(SCRATCH / "publication.xml").getroot()
    text += " " + "".join(pubmed.itertext())
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
                        "article_or_abstract": normalize(obj["snippet"]) in normalize(text),
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
    write("snippet-replay.json", snippets)
    write("target-network.json", NetworkIntegrityAuditor().audit_community(ROOT / TARGET))
    write(
        "primary-sections.json",
        [
            {"id": sec.get("id"), "text": sec.get_text(" ", strip=True)}
            for sec in article.find_all("section")
        ],
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "phase", choices=["inspect", "sources", "fallback", "assets", "checks", "replay"]
    )
    parsed = parser.parse_args()
    SCRATCH.mkdir(parents=True, exist_ok=True)
    globals()[parsed.phase]()
