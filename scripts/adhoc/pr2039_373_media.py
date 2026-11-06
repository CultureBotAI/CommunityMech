"""Retrieve public figures, supplement and issue state for the bounded 373 review."""

from __future__ import annotations

import json
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from pr2039_373_audit import SCRATCH, now, run, sha, write


def main():
    soup = BeautifulSoup((SCRATCH / "pmc.html").read_bytes(), "html.parser")
    sources = []
    for section in soup.find_all("figure"):
        image = section.find("img")
        if not image:
            continue
        url = image.get("src")
        name = section.get("id", "figure") + ".webp"
        result = run(
            "fetch-" + name,
            [
                "curl",
                "--fail",
                "--silent",
                "--show-error",
                "--location",
                "--retry",
                "3",
                "--connect-timeout",
                "20",
                "--max-time",
                "120",
                url,
            ],
        )
        if result.returncode == 0:
            (SCRATCH / name).write_bytes(result.stdout)
        sources.append(
            {
                "name": name,
                "url": url,
                "exit_code": result.returncode,
                "sha256": sha(result.stdout),
                "accessed_at": now(),
            }
        )
    href = "/articles/instance/13569317/bin/PS-82-10331-s001.docx"
    url = urljoin("https://pmc.ncbi.nlm.nih.gov/", href)
    result = run(
        "fetch-supplement",
        [
            "curl",
            "--fail",
            "--silent",
            "--show-error",
            "--location",
            "--retry",
            "3",
            "--connect-timeout",
            "20",
            "--max-time",
            "120",
            url,
        ],
    )
    if result.returncode == 0:
        (SCRATCH / "supplement.docx").write_bytes(result.stdout)
    sources.append(
        {
            "name": "supplement.docx",
            "url": url,
            "exit_code": result.returncode,
            "sha256": sha(result.stdout),
            "accessed_at": now(),
        }
    )
    write("media-sources.json", sources)
    for number in [1248, 880, 2049]:
        result = run(
            f"fetch-issue-{number}",
            [
                "gh",
                "issue",
                "view",
                str(number),
                "--repo",
                "CultureBotAI/CommunityMech",
                "--json",
                "number,title,state,body,comments,url,closedAt,updatedAt",
            ],
        )
        assert result.returncode == 0
        write(f"issue-{number}.json", json.loads(result.stdout))


if __name__ == "__main__":
    main()
