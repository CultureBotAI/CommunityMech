"""Capture one anonymous primary article for the #2848 status canary, 2026-11-15.

Inputs: fixed Europe PMC XML endpoint and unchanged record/cache/helper bytes.
Outputs: exclusive private XML plus identity/hash receipt. No retries, credentials,
cache edits, canonical application, or scientific completion assertion.
"""

import argparse
import hashlib
import json
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from defusedxml import ElementTree as SafeET

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/gtdb-ambiguity-20261115"
URL = "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13515949/fullTextXML"
RECORD = "data/isolates/Faecalibacterium_Prausnitzii_A2_165_2FL_FOS_Monoculture_Baseline.yaml"


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


class FixedHostRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        parsed = urllib.parse.urlsplit(newurl)
        if parsed.scheme != "https" or parsed.netloc != "www.ebi.ac.uk":
            raise ValueError("unexpected primary-source redirect")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--attempt", required=True)
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    if not args.attempt.isdigit():
        raise ValueError("numeric exclusive attempt required")
    output = STATE / f"faecalibacterium-source-{args.attempt}"
    if output.exists() or output.is_symlink():
        raise ValueError("preserve prior or partial source capture")
    paths = [ROOT / RECORD, ROOT / "references_cache/PMID_42655156.txt", Path(__file__)]
    captures = {path: path.read_bytes() for path in paths}
    receipt = {
        "url": URL,
        "output": str(output.relative_to(ROOT)),
        "inputs": {str(path.relative_to(ROOT)): sha(raw) for path, raw in captures.items()},
    }
    if args.plan:
        print(json.dumps({**receipt, "requests": 0}, indent=2))
        return
    output.mkdir(parents=True)
    receipt["accessed_at"] = datetime.now(timezone.utc).isoformat()
    try:
        request = urllib.request.Request(
            URL, headers={"User-Agent": "CommunityMech-source-review/1.0"}
        )  # noqa: S310
        with urllib.request.build_opener(FixedHostRedirect()).open(
            request, timeout=45
        ) as response:  # noqa: S310
            if response.status != 200:
                raise ValueError("primary source returned non-success status")
            raw = response.read(5_000_001)
        if not raw or len(raw) > 5_000_000:
            raise ValueError("primary source size outside limits")
        (output / "article.xml").write_bytes(raw)
        article = SafeET.fromstring(raw)
        ids = {
            node.get("pub-id-type"): node.text
            for node in article.findall("./front/article-meta/article-id")
        }
        if (
            ids.get("doi") != "10.3390/microorganisms14081812"
            or ids.get("pmid") != "42655156"
            or (ids.get("pmcid") or ids.get("pmc")) != "PMC13515949"
        ):
            raise ValueError("primary article identity mismatch")
        methods = []
        for section in article.findall("./body//sec"):
            title = " ".join(section.findtext("title", "").split())
            for paragraph in section.findall("./p"):
                text = " ".join("".join(paragraph.itertext()).split())
                if "A2-165" in text and "JCM31915" in text:
                    methods.append({"section_id": section.get("id"), "title": title, "text": text})
        if not methods:
            raise ValueError("expected study-stock identity paragraph absent")
        if any(path.read_bytes() != value for path, value in captures.items()):
            raise ValueError("record/cache/helper changed during capture")
        receipt.update(
            status="verified", file="article.xml", bytes=len(raw), sha256=sha(raw), identity=ids
        )
        with (output / "receipt.json").open("x") as stream:
            json.dump(receipt, stream, indent=2)
            stream.write("\n")
        with (output / "stock-identity.json").open("x") as stream:
            json.dump({"article_sha256": sha(raw), "paragraphs": methods}, stream, indent=2)
            stream.write("\n")
        print(json.dumps(receipt, indent=2))
    except Exception as error:
        with (output / "failure.json").open("x") as stream:
            json.dump({**receipt, "error_category": type(error).__name__}, stream, indent=2)
        raise


if __name__ == "__main__":
    main()
