"""Capture one anonymous primary source for 000088/#1548, 2026-11-15.

Inputs: explicit HTTPS source URL and fresh artifact name. Outputs: private raw
bytes and SHA256 acquisition receipt; XML optionally yields a readable structural
index. Existing complete or partial captures refuse before any network request.
"""

import argparse
import hashlib
import json
import re
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from defusedxml import ElementTree

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/phase2-brachypodium-20261115/sources"
HOSTS = {
    "www.ebi.ac.uk",
    "www.frontiersin.org",
    "public-pages-files-2025.frontiersin.org",
    "www.ncbi.nlm.nih.gov",
    "eutils.ncbi.nlm.nih.gov",
    "pmc.ncbi.nlm.nih.gov",
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", required=True)
    parser.add_argument("--name", required=True)
    args = parser.parse_args()
    source = urllib.parse.urlsplit(args.url)
    if (
        source.scheme != "https"
        or source.hostname not in HOSTS
        or source.username
        or source.password
    ):
        raise ValueError("only explicit anonymous HTTPS primary-source hosts are allowed")
    if not re.fullmatch(r"[A-Za-z0-9_-]+\.(?:xml|html|pdf|zip|docx|xlsx|webp|json|js)", args.name):
        raise ValueError("unsafe artifact basename")
    if "@" in args.url or any(
        key in source.query.lower() for key in ("email", "mailto", "api_key")
    ):
        raise ValueError("no email or credentials in source requests")
    target = STATE / args.name
    receipt = STATE / (args.name + ".receipt.json")
    index = STATE / (args.name + ".index.txt")
    if any(path.exists() or path.is_symlink() for path in (target, receipt, index)):
        raise ValueError("existing or partial capture; use a new version path")
    STATE.mkdir(parents=True, exist_ok=True)
    started = datetime.now(timezone.utc).isoformat()
    request = urllib.request.Request(
        args.url, headers={"User-Agent": "CommunityMech-source-review/1.0"}
    )  # noqa: S310
    with urllib.request.urlopen(request, timeout=45) as response:  # noqa: S310
        raw = response.read()
        content_type = response.headers.get("Content-Type")
        final_url = response.geturl()
    if not raw:
        raise ValueError("empty source response")
    document = ElementTree.fromstring(raw) if target.suffix == ".xml" else None
    if target.suffix == ".pdf" and not raw.startswith(b"%PDF-"):
        raise ValueError("response is not a PDF")
    if target.suffix in {".docx", ".xlsx", ".zip"} and not raw.startswith(b"PK"):
        raise ValueError("response is not a ZIP-based artifact")
    with target.open("xb") as stream:
        stream.write(raw)
    result = {
        "source_url": args.url,
        "final_url_private_only": final_url,
        "started_at": started,
        "accessed_at": datetime.now(timezone.utc).isoformat(),
        "content_type": content_type,
        "bytes": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "path": str(target.relative_to(ROOT)),
    }
    with receipt.open("x") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    if document is not None:
        with index.open("x") as stream:
            for element in document.iter():
                if element.tag in {
                    "article-id",
                    "title",
                    "p",
                    "caption",
                    "table",
                    "supplementary-material",
                }:
                    stream.write(
                        f"[{element.tag} {element.attrib}] " + " ".join(element.itertext()) + "\n"
                    )
                if element.tag in {"graphic", "media", "ext-link"}:
                    stream.write(f"[{element.tag}] {element.attrib}\n")
    print(json.dumps({key: result[key] for key in ("source_url", "bytes", "sha256", "path")}))


if __name__ == "__main__":
    main()
