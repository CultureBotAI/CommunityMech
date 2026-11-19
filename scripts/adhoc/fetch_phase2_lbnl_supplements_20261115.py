"""Retrieve one anonymous Europe PMC supplement archive for #1548, 2026-11-15.

Inputs: fixed open-access PMC9765266 supplementary-files endpoint.
Outputs: exclusive private archive, exact S1/S3 DOCX members and hash receipt.
No credentials, email parameters, article-cache writes or canonical edits.
"""

import hashlib
import io
import json
import urllib.request
import zipfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEST = ROOT / ".temp/phase2-science-20261115/lbnl-supplements"
URL = "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9765266/supplementaryFiles"
LIMIT = 50 * 1024 * 1024


def main():
    if DEST.exists():
        raise ValueError("exclusive supplementary-source destination already exists")
    request = urllib.request.Request(
        URL, headers={"User-Agent": "CommunityMech-scientific-review/1.0"}
    )
    with urllib.request.urlopen(request, timeout=50) as response:
        raw = response.read(LIMIT + 1)
        content_type = response.headers.get("Content-Type")
        final_url = response.url
    if len(raw) > LIMIT:
        raise ValueError("supplement archive exceeds bounded download size")
    if not raw.startswith(b"PK") or not zipfile.is_zipfile(io.BytesIO(raw)):
        raise ValueError(f"expected a ZIP supplement archive; got {content_type}")
    retained = []
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        names = archive.namelist()
        for name in names:
            if name.endswith(("msystems.00951-22-s0006.docx", "msystems.00951-22-s0008.docx")):
                member = archive.read(name)
                if not member.startswith(b"PK") or not zipfile.is_zipfile(io.BytesIO(member)):
                    raise ValueError("expected an actual DOCX member")
                retained.append((Path(name).name, member))
    if not any(name.endswith("s0006.docx") for name, _ in retained):
        raise ValueError("archive did not contain the exact Table S1 member")
    DEST.mkdir(parents=True, exist_ok=False)
    with (DEST / "PMC9765266-supplementaryFiles.zip").open("xb") as stream:
        stream.write(raw)
    for name, member in retained:
        with (DEST / name).open("xb") as stream:
            stream.write(member)
    receipt = {
        "url": URL,
        "final_url": final_url,
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "content_type": content_type,
        "bytes": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "archive_members": names,
        "retained_members": [
            {"filename": name, "bytes": len(member), "sha256": hashlib.sha256(member).hexdigest()}
            for name, member in retained
        ],
        "limitations": "Acquisition and file-type verification only; scientific content requires inspection.",
    }
    with (DEST / "retrieval.json").open("x") as stream:
        json.dump(receipt, stream, indent=2)
        stream.write("\n")
    if not (DEST / "PMC9765266-supplementaryFiles.zip").stat().st_size:
        raise ValueError("archive was not persisted")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
