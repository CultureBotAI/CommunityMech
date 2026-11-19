"""Retain one anonymous primary source for the #2849 stock review, 2026-11-15.

Inputs: fixed article/stock/taxonomy URLs and unchanged canonical/cache bytes.
Outputs: exclusive private source bytes and hash/identity receipt. No retries,
credentials, paid providers, canonical/cache writes or source bodies in Git.
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
STATE = ROOT / ".temp/gtdb-source-routes-2849-20261115/terrabacter-sources"
URLS = {
    "article": (
        "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13472149/fullTextXML",
        "article.xml",
    ),
    "stock": ("https://bacdive.dsmz.de/strain/157986", "bacdive-157986.html"),
    "taxonomy": (
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1472881&retmode=xml",
        "taxonomy-1472881.xml",
    ),
}
INPUTS = (
    "data/isolates/Terrabacter_2APm3_Sulfadiazine_Isolate_Baseline.yaml",
    "references_cache/PMID_42598292.txt",
)
MAX_BYTES = 5_000_000


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


class FixedHostRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        parsed = urllib.parse.urlsplit(newurl)
        original = urllib.parse.urlsplit(req.full_url)
        if parsed.scheme != "https" or parsed.netloc != original.netloc:
            raise ValueError("unexpected source redirect host")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("asset", choices=URLS)
    parser.add_argument("--attempt", required=True)
    parser.add_argument("--plan", action="store_true")
    parser.add_argument("--retained-source", type=Path)
    parser.add_argument("--expected-source-sha256")
    args = parser.parse_args()
    if not args.attempt.isdigit():
        raise ValueError("numeric capture attempt required")
    destination = STATE / f"{args.asset}-{args.attempt}"
    if destination.exists() or destination.is_symlink():
        raise ValueError("prior or partial capture must remain immutable")
    retained = args.retained_source.resolve() if args.retained_source else None
    retained_bytes = None
    if retained:
        if not retained.is_relative_to(STATE) or not args.expected_source_sha256:
            raise ValueError("exact retained private source/hash required")
        retained_bytes = retained.read_bytes()
        if sha(retained_bytes) != args.expected_source_sha256:
            raise ValueError("retained source hash differs")
    elif args.expected_source_sha256:
        raise ValueError("source hash requires retained source")
    url, filename = URLS[args.asset]
    bound = {name: sha((ROOT / name).read_bytes()) for name in INPUTS}
    bound[str(Path(__file__).relative_to(ROOT))] = sha(Path(__file__).read_bytes())
    if args.plan:
        print(
            json.dumps(
                {
                    "url": url,
                    "output": str(destination.relative_to(ROOT)),
                    "requests": 0,
                    "inputs": bound,
                }
            )
        )
        return
    destination.mkdir(parents=True)
    receipt = {"url": url, "accessed_at": datetime.now(timezone.utc).isoformat(), "inputs": bound}
    try:
        if retained:
            raw = retained_bytes
            receipt.update(
                acquisition="retained prior response; no new request",
                retained_path=str(retained.relative_to(ROOT)),
                retained_sha256=sha(raw),
            )
        else:
            request = urllib.request.Request(
                url, headers={"User-Agent": "CommunityMech-source-review/1.0"}
            )  # noqa: S310
            with urllib.request.build_opener(FixedHostRedirect()).open(
                request, timeout=45
            ) as response:  # noqa: S310
                if response.status != 200:
                    raise ValueError("non-success HTTP status")
                raw = response.read(MAX_BYTES + 1)
            receipt["acquisition"] = "anonymous live request"
        if not raw or len(raw) > MAX_BYTES:
            raise ValueError("source size outside allowed bounds")
        # Retain the response even if identity validation fails, without using
        # it as evidence; the fixed output path then refuses an accidental retry.
        (destination / filename).write_bytes(raw)
        if args.asset == "article":
            root = SafeET.fromstring(raw)
            doi = root.findtext("./front/article-meta/article-id[@pub-id-type='doi']")
            pmc = root.findtext(
                "./front/article-meta/article-id[@pub-id-type='pmcid']"
            ) or root.findtext("./front/article-meta/article-id[@pub-id-type='pmc']")
            if doi != "10.1021/acs.estlett.6c00474" or pmc != "PMC13472149":
                raise ValueError("wrong primary article identity")
            license_text = " ".join(root.find("./front/article-meta/permissions").itertext())
            if "CC-BY" not in license_text and "CC BY" not in license_text:
                raise ValueError("expected open-access license missing")
            receipt["identity"] = {"doi": doi, "pmcid": pmc, "license": license_text.strip()}
        elif args.asset == "stock":
            text = raw.decode()
            if not all(value in text for value in ("28514", "2APm3", "Terrabacter")):
                raise ValueError("stock identity missing")
            receipt["identity"] = {
                "bacdive": "157986",
                "collection": "DSM28514",
                "designation": "2APm3",
            }
        else:
            root = SafeET.fromstring(raw)
            taxa = root.findall("./Taxon")
            if len(taxa) != 1 or taxa[0].findtext("TaxId") != "1472881":
                raise ValueError("wrong taxonomy identity")
            receipt["identity"] = {
                "taxid": "1472881",
                "scientific_name": taxa[0].findtext("ScientificName"),
                "rank": taxa[0].findtext("Rank"),
            }
        if bound != {name: sha((ROOT / name).read_bytes()) for name in bound}:
            raise ValueError("review inputs changed during source capture")
        if retained and retained.read_bytes() != retained_bytes:
            raise ValueError("retained source changed during verification")
        receipt.update(status="verified", file=filename, bytes=len(raw), sha256=sha(raw))
        with (destination / "receipt.json").open("x") as stream:
            json.dump(receipt, stream, indent=2)
            stream.write("\n")
        print(json.dumps({key: value for key, value in receipt.items() if key != "inputs"}))
    except Exception as error:
        receipt.update(status="failed", error_category=type(error).__name__, message=str(error))
        with (destination / "failure.json").open("x") as stream:
            json.dump(receipt, stream, indent=2)
        raise


if __name__ == "__main__":
    main()
