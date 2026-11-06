"""Extract fresh public primary HTML and replay current snippets without KB writes."""

from __future__ import annotations

import unicodedata

import yaml
from bs4 import BeautifulSoup
from pr2039_373_audit import ROOT, SCRATCH, TARGET, sha, write


def normalize(value):
    return " ".join(unicodedata.normalize("NFKC", value).split())


def main():
    raw = (SCRATCH / "pmc.html").read_bytes()
    soup = BeautifulSoup(raw, "html.parser")
    article = soup.find("article") or soup
    text = article.get_text(" ", strip=True)
    (SCRATCH / "pmc-text.txt").write_text(article.get_text("\n", strip=True))
    rows = []

    def walk(obj, path=""):
        if isinstance(obj, dict):
            if "snippet" in obj:
                snippet = obj["snippet"]
                rows.append(
                    {
                        "path": path,
                        "snippet": snippet,
                        "fresh_primary_html_match": normalize(snippet) in normalize(text),
                    }
                )
            for key, value in obj.items():
                walk(value, f"{path}.{key}" if path else key)
        elif isinstance(obj, list):
            for i, value in enumerate(obj):
                walk(value, f"{path}[{i}]")

    walk(yaml.safe_load((ROOT / TARGET).read_text()))
    write(
        "primary-html-replay.json",
        {
            "source_sha256": sha(raw),
            "title": soup.title.get_text(),
            "count": len(rows),
            "matches": sum(row["fresh_primary_html_match"] for row in rows),
            "rows": rows,
            "links": [
                {"text": a.get_text(" ", strip=True), "url": a["href"]}
                for a in article.find_all("a", href=True)
                if any(word in a["href"] for word in ["suppl", "bin/", "s001", "s002"])
            ],
        },
    )
    print(
        {
            "title": soup.title.get_text(),
            "count": len(rows),
            "matches": sum(r["fresh_primary_html_match"] for r in rows),
        }
    )


if __name__ == "__main__":
    main()
