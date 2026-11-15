"""Read captured 000088 primary HTML and expose text/links, #1548, 2026-11-15.

Input is an ignored source capture; stdout is a readable primary-source index.
No network or canonical writes. Nuxt string entries expose publisher attachments.
"""

import argparse
import json
from pathlib import Path

from bs4 import BeautifulSoup


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--attachments", action="store_true")
    parser.add_argument("--nuxt-start", type=int)
    args = parser.parse_args()
    soup = BeautifulSoup(args.path.read_bytes(), "html.parser")
    if args.nuxt_start is not None:
        items = json.loads(soup.find("script", id="__NUXT_DATA__").get_text())
        for index in range(args.nuxt_start, min(args.nuxt_start + 100, len(items))):
            print(index, repr(items[index])[:1800])
        return
    if args.attachments:
        for element in soup.find_all(["a", "img", "source"]):
            value = element.get("href") or element.get("src") or element.get("srcset") or ""
            if any(word in value.lower() for word in ("suppl", "1649750", "download")):
                print(value)
        for element in soup.find_all("script", id="__NUXT_DATA__"):
            items = json.loads(element.get_text())
            for index, item in enumerate(items):
                if isinstance(item, str) and any(
                    word in item.lower()
                    for word in ("suppl", ".pdf", ".doc", ".xlsx", "datafile", "sm1")
                ):
                    print(index, repr(item)[:1800])
    else:
        for index, element in enumerate(soup.find_all(["h1", "h2", "h3", "p", "table"])):
            if not element.find_parent("table"):
                print(
                    f"[{index}:{element.name} {element.get('id', '')}] {element.get_text(' ', strip=True)}"
                )


if __name__ == "__main__":
    main()
