"""Prepare one anonymous primary article for the resumed campaign, 2026-11-15.

Input: fixed public Europe PMC article for CommunityMech:000296 (#1428/#2828).
Output: exclusive private XML, text/asset inventory and hash receipt. No earlier
private checkpoint is copied; no canonical record/cache or review is changed.
This source canary is not the later scientific review or a validator run.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from defusedxml import ElementTree

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/campaign-resume-20261115"
TARGET = "kb/communities/Ecoli_Bifidobacterium_bifidum_Infant_gut_HMO_Mutualism_Coculture.yaml"
CACHE = "references_cache/PMID_42020426.md"
PMCID = "PMC13103366"
PMID = "42020426"
DOI = "10.1038/s41467-026-71764-7"
URL = f"https://www.ebi.ac.uk/europepmc/webservices/rest/{PMCID}/fullTextXML"
XLINK = "{http://www.w3.org/1999/xlink}href"


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def text(element):
    return " ".join("".join(element.itertext()).split()) if element is not None else ""


def inspect_primary(payload):
    article = ElementTree.fromstring(payload)
    if article.tag != "article" or len(payload) < 10000:
        raise ValueError("expected substantive primary JATS article")
    ids = {
        row.get("pub-id-type"): text(row)
        for row in article.findall("./front/article-meta/article-id")
    }
    pmc = ids.get("pmc", ids.get("pmcid", ""))
    if ids.get("pmid") != PMID or ids.get("doi") != DOI or pmc.removeprefix("PMC") != PMCID[3:]:
        raise ValueError("primary identity differs from the fixed canary source")
    body = article.find("body")
    if body is None:
        raise ValueError("primary body missing")
    sections = [text(sec.find("title")) for sec in body.iter("sec")]
    if not any("method" in value.lower() for value in sections) or not any(
        "result" in value.lower() for value in sections
    ):
        raise ValueError("expected Results and Methods sections")
    paragraphs = [
        {
            "section_id": sec.get("id"),
            "section": text(sec.find("title")),
            "paragraph_id": paragraph.get("id"),
            "text": text(paragraph),
        }
        for sec in body.iter("sec")
        for paragraph in sec.findall("p")
    ]
    assets = [
        {
            "kind": row.tag,
            "id": row.get("id"),
            "label": text(row.find("label")),
            "caption": text(row.find("caption")),
            "links": sorted({child.get(XLINK) for child in row.iter() if child.get(XLINK)}),
        }
        for row in article.iter()
        if row.tag in {"fig", "supplementary-material"}
    ]
    return {
        "identity": ids,
        "title": text(article.find("./front/article-meta/title-group/article-title")),
        "sections": sections,
        "paragraphs": paragraphs,
        "assets": assets,
    }


def write_json(path, value):
    with path.open("x") as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write("\n")


def prepare(output, expected_revision, plan_only):
    output = output.resolve()
    if output.exists() or not output.is_relative_to(STATE.resolve()):
        raise ValueError("new exclusive private destination required")
    revision = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    if revision != expected_revision:
        raise ValueError("source preparation revision changed")
    inputs = {name: sha((ROOT / name).read_bytes()) for name in (TARGET, CACHE)}
    plan = {
        "mode": "plan" if plan_only else "source_capture",
        "revision": revision,
        "url": URL,
        "identity": {"pmcid": PMCID, "pmid": PMID, "doi": DOI},
        "output": str(output.relative_to(ROOT)),
        "input_sha256": inputs,
        "helper_sha256": sha(Path(__file__).read_bytes()),
        "scope": "One public primary article; no scientific assessment or canonical mutation.",
    }
    if plan_only:
        print(json.dumps(plan, indent=2))
        return
    output.mkdir(parents=True)
    plan["started_at"] = datetime.now(timezone.utc).isoformat()
    write_json(output / "started.json", plan)
    try:
        request = urllib.request.Request(
            URL, headers={"User-Agent": "CommunityMech anonymous primary-source preparation"}
        )
        with urllib.request.urlopen(request, timeout=60) as response:
            payload = response.read()
        inspected = inspect_primary(payload)
        with (output / "article.xml").open("xb") as stream:
            stream.write(payload)
        write_json(output / "paragraphs.json", inspected["paragraphs"])
        write_json(output / "assets.json", inspected["assets"])
        if inputs != {name: sha((ROOT / name).read_bytes()) for name in inputs}:
            raise ValueError("canonical input changed during source capture")
        if (
            subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
            != revision
        ):
            raise ValueError("revision changed during source capture")
        artifacts = {
            name: {
                "bytes": (output / name).stat().st_size,
                "sha256": sha((output / name).read_bytes()),
            }
            for name in ("article.xml", "paragraphs.json", "assets.json")
        }
        if (
            not all(item["bytes"] for item in artifacts.values())
            or sha(payload) != artifacts["article.xml"]["sha256"]
        ):
            raise ValueError("source persistence verification failed")
        receipt = {
            **plan,
            "finished_at": datetime.now(timezone.utc).isoformat(),
            "title": inspected["title"],
            "artifacts": artifacts,
            "inputs_unchanged": True,
            "limitations": "Main article identity/body verified; visual figures, separate supplements and source data are inventoried, not downloaded or scientifically assessed.",
        }
        write_json(output / "receipt.json", receipt)
        print(json.dumps(receipt, indent=2))
    except Exception as exc:
        write_json(output / "failure.json", {"type": type(exc).__name__, "message": str(exc)})
        raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--expected-revision", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    prepare(args.output, args.expected_revision, args.plan)


if __name__ == "__main__":
    main()
