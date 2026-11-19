"""Retain anonymous HMO primary assets for #1428/#2828/#2843, 2026-11-15.

Inputs: the previously verified PMC13103366 JATS XML, exact current revision,
and explicit figure/supplement IDs. Outputs: exclusive private source bytes,
format/content inventories and retrieval/hash receipts. No canonical/cache
writes, credentials, scientific verdict, validator run or review save.
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import re
import subprocess
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
import zipfile
from datetime import datetime, timezone
from pathlib import Path

from defusedxml import ElementTree as SafeET

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/campaign-resume-20261115"
ARTICLE = STATE / "hmo-source-001/article.xml"
ARTICLE_SHA = "a100510b84bb68dbb4e1fe1163a1dcaaf2167566fc43b7bcf3740901ac385447"
TARGET = "kb/communities/Ecoli_Bifidobacterium_bifidum_Infant_gut_HMO_Mutualism_Coculture.yaml"
CACHE = "references_cache/PMID_42020426.md"
MAX_ASSET_BYTES = 40 * 1024 * 1024
MAX_TOTAL_BYTES = 64 * 1024 * 1024
ALLOWED_HOSTS = {"cdn.ncbi.nlm.nih.gov", "static-content.springer.com"}
ASSETS = [f"Fig{i}" for i in range(1, 5)] + [f"MOESM{i}" for i in range(1, 8)] + ["MOESM9"]
XLINK = "{http://www.w3.org/1999/xlink}href"


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def utc():
    return datetime.now(timezone.utc).isoformat()


def write_json(path, data):
    with path.open("x") as stream:
        json.dump(data, stream, indent=2, ensure_ascii=False)
        stream.write("\n")


def checked_url(url):
    parts = urllib.parse.urlsplit(url)
    if (
        parts.scheme != "https"
        or parts.hostname not in ALLOWED_HOSTS
        or parts.username
        or parts.password
        or parts.port
        or parts.query
        or parts.fragment
    ):
        raise ValueError("asset URL outside the fixed anonymous primary-source hosts")
    return url


class PrimaryRedirects(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        checked_url(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def asset_plan(payload, asset):
    if sha(payload) != ARTICLE_SHA or asset not in ASSETS:
        raise ValueError("wrong retained primary XML or unsupported asset")
    parser = SafeET.DefusedXMLParser(target=ET.TreeBuilder(insert_pis=True), forbid_dtd=True)
    parser.feed(payload)
    tree = parser.close()
    figure = asset.startswith("Fig")
    node = tree.find(f".//{'fig' if figure else 'supplementary-material'}[@id='{asset}']")
    if node is None:
        raise ValueError("selected asset is absent from retained article")
    media = node.find(".//graphic[@content-type='image']" if figure else "media")
    if media is None:
        raise ValueError("selected asset lacks primary media")
    filename = media.get(XLINK, "")
    if not re.fullmatch(
        r"41467_2026_71764_(?:Fig[1-4]_HTML|MOESM[1-9]_ESM)\.(?:jpg|pdf|xls|xlsx)", filename
    ):
        raise ValueError("unexpected primary filename")
    instructions = dict(
        child.text.split(" ", 1)
        for child in media
        if child.tag is ET.ProcessingInstruction and child.text and " " in child.text
    )
    if figure:
        cloud_path = instructions.get("cloudpmc-path", "")
        if not re.fullmatch(r"blobs/be48/13103366/[a-f0-9]{12}/" + re.escape(filename), cloud_path):
            raise ValueError("unexpected exact primary figure route")
        url = "https://cdn.ncbi.nlm.nih.gov/pmc/" + cloud_path
    else:
        url = (
            "https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-026-71764-7/MediaObjects/"
            + filename
        )
    caption = media.find("caption")
    return {
        "id": asset,
        "filename": filename,
        "url": checked_url(url),
        "label": " ".join("".join(caption.itertext()).split()) if caption is not None else asset,
        "expected_bytes": int(instructions["size"]) if "size" in instructions else None,
        "expected_dimensions": (
            [int(instructions["original-width"]), int(instructions["original-height"])]
            if figure
            else None
        ),
        "expected_scaled_dimensions": (
            [int(instructions["scaled-width"]), int(instructions["scaled-height"])]
            if figure and "scaled-width" in instructions and "scaled-height" in instructions
            else None
        ),
    }


def inspect_format(raw, plan, mime):
    suffix = Path(plan["filename"]).suffix
    if mime in {"text/html", "text/plain"}:
        raise ValueError("text response is not a primary binary asset")
    if plan["expected_bytes"] is not None and len(raw) != plan["expected_bytes"]:
        raise ValueError("asset byte count differs from the retained JATS size")
    if suffix == ".jpg":
        from PIL import Image

        if mime != "image/jpeg" or not raw.startswith(b"\xff\xd8\xff"):
            raise ValueError("expected JPEG content and MIME")
        with Image.open(io.BytesIO(raw)) as image:
            dimensions = list(image.size)
            image.verify()
        if dimensions not in [plan["expected_dimensions"], plan.get("expected_scaled_dimensions")]:
            raise ValueError("figure dimensions differ from the retained JATS")
        return {
            "format": "JPEG",
            "dimensions": dimensions,
            "rendition": "original" if dimensions == plan["expected_dimensions"] else "scaled",
        }, None
    if suffix == ".pdf":
        from pypdf import PdfReader

        if mime not in {"application/pdf", "application/octet-stream"} or not raw.startswith(
            b"%PDF-"
        ):
            raise ValueError("expected PDF content and MIME")
        reader = PdfReader(io.BytesIO(raw), strict=True)
        if reader.is_encrypted or not len(reader.pages):
            raise ValueError("PDF is encrypted or empty")
        pages = [
            {"page": i + 1, "text": page.extract_text() or ""}
            for i, page in enumerate(reader.pages)
        ]
        return {
            "format": "PDF",
            "pages": len(pages),
            "pages_with_text": sum(bool(p["text"].strip()) for p in pages),
        }, pages
    if suffix == ".xlsx":
        if mime not in {
            "application/octet-stream",
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        } or not raw.startswith(b"PK"):
            raise ValueError("expected XLSX content and MIME")
        with zipfile.ZipFile(io.BytesIO(raw)) as archive:
            if sum(row.file_size for row in archive.infolist()) > 128 * 1024 * 1024:
                raise ValueError("workbook expansion exceeds bounded inspection")
            workbook = SafeET.fromstring(archive.read("xl/workbook.xml"))
            sheets = [row.attrib for row in workbook.findall("{*}sheets/{*}sheet")]
        if not sheets:
            raise ValueError("workbook has no worksheets")
        return {"format": "XLSX", "worksheets": sheets}, None
    if mime not in {"application/octet-stream", "application/vnd.ms-excel"} or not raw.startswith(
        b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1"
    ):
        raise ValueError("expected legacy spreadsheet content and MIME")
    return {
        "format": "OLE spreadsheet",
        "limitation": "Container identity only; worksheet contents not yet inspected.",
    }, None


def run(args):
    output = args.output.resolve()
    if output.exists() or output.parent != STATE.resolve():
        raise ValueError("new direct private namespace required")
    if len(set(args.asset)) != len(args.asset):
        raise ValueError("duplicate requested asset")
    revision = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    if revision != args.expected_revision:
        raise ValueError("expected full current revision required")
    bound = [ROOT / TARGET, ROOT / CACHE, ARTICLE, Path(__file__)]
    inputs = {str(path.relative_to(ROOT)): sha(path.read_bytes()) for path in bound}
    plans = [asset_plan(ARTICLE.read_bytes(), name) for name in args.asset]
    plan = {
        "mode": "plan" if args.plan else "primary_asset_capture",
        "revision": revision,
        "input_sha256": inputs,
        "assets": plans,
        "output": str(output.relative_to(ROOT)),
        "limits": {"per_asset_bytes": MAX_ASSET_BYTES, "total_bytes": MAX_TOTAL_BYTES},
        "scope": "Primary source acquisition and format verification only; no scientific review or gate execution.",
    }
    if args.plan:
        print(json.dumps(plan, indent=2))
        return
    output.mkdir()
    plan["started_at"] = utc()
    write_json(output / "started.json", plan)
    opener = urllib.request.build_opener(PrimaryRedirects())
    retained = []
    total = 0
    try:
        for selected in plans:
            request = urllib.request.Request(
                selected["url"],
                headers={"User-Agent": "CommunityMech anonymous primary-asset preparation"},
            )
            with opener.open(request, timeout=60) as response:
                final_url = checked_url(response.url)
                mime = response.headers.get_content_type()
                raw = response.read(MAX_ASSET_BYTES + 1)
                if response.status != 200 or not 0 < len(raw) <= MAX_ASSET_BYTES:
                    raise ValueError("asset response missing or exceeds size limit")
            total += len(raw)
            if total > MAX_TOTAL_BYTES:
                raise ValueError("total capture exceeds size limit")
            with (output / selected["filename"]).open("xb") as stream:
                stream.write(raw)
            parsed, pages = inspect_format(raw, selected, mime)
            entry = {
                **selected,
                "retrieved_at": utc(),
                "final_url": final_url,
                "mime": mime,
                "bytes": len(raw),
                "sha256": sha(raw),
                "content": parsed,
            }
            if pages is not None:
                derived = output / (selected["filename"] + ".pages.json")
                write_json(derived, pages)
                entry["text_derivative"] = {
                    "filename": derived.name,
                    "sha256": sha(derived.read_bytes()),
                    "method": "pypdf extract_text, no OCR; page boundaries retained",
                }
            if sha((output / selected["filename"]).read_bytes()) != entry["sha256"]:
                raise ValueError("persisted asset differs")
            write_json(output / (selected["id"] + ".receipt.json"), entry)
            retained.append(entry)
        if inputs != {str(path.relative_to(ROOT)): sha(path.read_bytes()) for path in bound}:
            raise ValueError("bound input changed during capture")
        if (
            subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
            != revision
        ):
            raise ValueError("revision changed during capture")
        receipt = {**plan, "finished_at": utc(), "retained": retained, "inputs_unchanged": True}
        write_json(output / "receipt.json", receipt)
        print(json.dumps(receipt, indent=2))
    except Exception as exc:
        write_json(
            output / "failure.json",
            {
                "finished_at": utc(),
                "exception_type": type(exc).__name__,
                "completed_assets": [row["id"] for row in retained],
            },
        )
        raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--expected-revision", required=True)
    parser.add_argument("--asset", action="append", choices=ASSETS, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--plan", action="store_true")
    run(parser.parse_args())


if __name__ == "__main__":
    main()
