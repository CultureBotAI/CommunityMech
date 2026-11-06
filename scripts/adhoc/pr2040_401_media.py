"""Read public media and issue state for the bounded record 401 review."""

from __future__ import annotations

import json
import zipfile

from bs4 import BeautifulSoup
from defusedxml import ElementTree
from pr2040_401_audit import SCRATCH, now, run, sha, write


def fetch(name, url):
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
    return {
        "name": name,
        "url": url,
        "exit_code": result.returncode,
        "sha256": sha(result.stdout),
        "accessed_at": now(),
    }


def main():
    tree = ElementTree.parse(SCRATCH / "primary.xml").getroot()
    for section in tree.findall("./body/sec"):
        (SCRATCH / (section.get("id") + ".txt")).write_text(
            "\n\n".join("".join(p.itertext()) for p in section if p.tag in ["title", "p", "sec"])
        )
    for name in ["jcm1254", "jcm31915"]:
        (SCRATCH / f"{name}.txt").write_text(
            BeautifulSoup((SCRATCH / f"{name}.html").read_bytes(), "html.parser").get_text(
                " ", strip=True
            )
        )
    write(
        "ncbi-authorities.json",
        [
            {
                **{
                    key: t.findtext(key)
                    for key in ["TaxId", "ScientificName", "Rank", "ParentTaxId", "Lineage"]
                },
                "source_sha256": sha((SCRATCH / "ncbi-taxonomy.xml").read_bytes()),
            }
            for t in ElementTree.parse(SCRATCH / "ncbi-taxonomy.xml").getroot().findall("Taxon")
        ],
    )
    rows = [fetch("pmc.html", "https://pmc.ncbi.nlm.nih.gov/articles/PMC13515949/")]
    soup = BeautifulSoup((SCRATCH / "pmc.html").read_bytes(), "html.parser")
    for section in soup.find_all("figure"):
        img = section.find("img")
        if img:
            rows.append(fetch(section.get("id") + ".webp", img["src"]))
    rows.append(
        fetch(
            "supplement.zip",
            "https://pmc.ncbi.nlm.nih.gov/articles/instance/13515949/bin/microorganisms-14-01812-s001.zip",
        )
    )
    if zipfile.is_zipfile(SCRATCH / "supplement.zip"):
        with zipfile.ZipFile(SCRATCH / "supplement.zip") as archive:
            names = archive.namelist()
            write("supplement-members.json", names)
            for name in names:
                if name.lower().endswith(".pdf"):
                    (SCRATCH / "supplement.pdf").write_bytes(archive.read(name))
    else:
        rows.append(
            fetch(
                "supplement.pdf",
                "https://mdpi-res.com/d_attachment/microorganisms/microorganisms-14-01812/article_deploy/microorganisms-14-01812-s001.pdf",
            )
        )
    write("media-sources.json", rows)
    for number in [991, 992, 993, 994, 1254, 1256, 2113]:
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


def supplementary_fallback():
    row = fetch(
        "supplement-epmc.zip",
        "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13515949/supplementaryFiles",
    )
    extracted = []
    if zipfile.is_zipfile(SCRATCH / "supplement-epmc.zip"):
        with zipfile.ZipFile(SCRATCH / "supplement-epmc.zip") as archive:
            write("supplement-epmc-members.json", archive.namelist())
            for index, name in enumerate(archive.namelist()):
                if name.lower().endswith(".pdf"):
                    destination = SCRATCH / f"supplement-epmc-{index}.pdf"
                    destination.write_bytes(archive.read(name))
                    extracted.append(
                        {
                            "member": name,
                            "path": str(destination),
                            "sha256": sha(destination.read_bytes()),
                        }
                    )
                elif name.lower().endswith(".zip"):
                    import io

                    with zipfile.ZipFile(io.BytesIO(archive.read(name))) as nested:
                        for subindex, subname in enumerate(nested.namelist()):
                            if subname.lower().endswith(".pdf"):
                                destination = SCRATCH / f"supplement-epmc-{index}-{subindex}.pdf"
                                destination.write_bytes(nested.read(subname))
                                extracted.append(
                                    {
                                        "member": name + "/" + subname,
                                        "path": str(destination),
                                        "sha256": sha(destination.read_bytes()),
                                    }
                                )
    write("supplement-fallback.json", {"retrieval": row, "extracted": extracted})


def render_supplement():
    receipt = json.loads((SCRATCH / "supplement-fallback.json").read_text())
    assert len(receipt["extracted"]) == 1
    pdf = receipt["extracted"][0]["path"]
    assert (
        run(
            "supplement-text", ["pdftotext", "-layout", pdf, str(SCRATCH / "supplement-text.txt")]
        ).returncode
        == 0
    )
    assert (
        run(
            "supplement-image",
            ["pdftoppm", "-png", "-r", "150", "-singlefile", pdf, str(SCRATCH / "supplement-page")],
        ).returncode
        == 0
    )


if __name__ == "__main__":
    main()
