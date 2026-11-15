"""Retain DSM17677 stock reclassification evidence for 000122/#1548, 2026-11-15.

Input: public DSMZ catalogue; outputs: exclusive private HTML, text and receipt.
Anonymous, read-only acquisition; no personal identifiers sent to the service.
"""

import hashlib
import json
import textwrap
import urllib.request
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
URL = "https://www.dsmz.de/collection/catalogue/details/culture/DSM-17677"


class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hidden = 0
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style"}:
            self.hidden += 1

    def handle_endtag(self, tag):
        if tag in {"script", "style"}:
            self.hidden -= 1

    def handle_data(self, data):
        if not self.hidden:
            self.parts.append(data)


def main():
    state = ROOT / ".temp/phase2-gut-20261115/dsm17677-catalog-001"
    state.mkdir()
    request = urllib.request.Request(URL, headers={"User-Agent": "CommunityMech source inspection"})
    with urllib.request.urlopen(request, timeout=60) as response:
        data = response.read()
    parser = Text()
    parser.feed(data.decode())
    text = " ".join(" ".join(parser.parts).split())
    for required in (
        "DSM 17677",
        "Faecalibacterium duncaniae",
        "Originally deposited as Faecalibacterium prausnitzii",
    ):
        if required not in text:
            raise ValueError("catalogue lacks required stock/reclassification text")
    (state / "catalog.html").write_bytes(data)
    (state / "catalog.txt").write_text(textwrap.fill(text, width=110) + "\n")
    report = {
        "url": URL,
        "accessed_at": datetime.now(timezone.utc).isoformat(),
        "html_sha256": hashlib.sha256(data).hexdigest(),
        "bytes": len(data),
        "text_sha256": hashlib.sha256((state / "catalog.txt").read_bytes()).hexdigest(),
    }
    (state / "receipt.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
