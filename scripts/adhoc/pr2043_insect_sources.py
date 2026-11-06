"""Read-only source extraction and term/snippet replay for PR 2043 insects."""

from __future__ import annotations

import argparse
import io
import json
import re
import unicodedata
import zipfile
from pathlib import Path

import yaml
from defusedxml import ElementTree
from pr2043_insect_audit import RECORDS, ROOT, SCRATCH, fetch, now, run, sha, write


def extract():
    folder = SCRATCH / "shared"
    root = ElementTree.parse(folder / "primary.xml").getroot()
    for section in root.findall(".//body/sec"):
        (folder / (section.attrib["id"] + ".txt")).write_text(
            "\n\n".join("".join(e.itertext()) for e in section)
        )
    inventory = []

    def unpack(raw, prefix):
        with zipfile.ZipFile(io.BytesIO(raw)) as archive:
            for entry in archive.infolist():
                if entry.is_dir():
                    continue
                data = archive.read(entry)
                name = prefix + Path(entry.filename).name
                inventory.append(
                    {
                        "archive_member": entry.filename,
                        "saved_name": name,
                        "size": len(data),
                        "sha256": sha(data),
                    }
                )
                if name.lower().endswith(".zip"):
                    unpack(data, prefix + "nested-")
                elif Path(name).suffix.lower() in {
                    ".jpg",
                    ".jpeg",
                    ".png",
                    ".pdf",
                    ".docx",
                    ".xlsx",
                    ".xls",
                }:
                    (folder / name).write_bytes(data)
                    if name.lower().endswith(".docx"):
                        with zipfile.ZipFile(io.BytesIO(data)) as doc:
                            docroot = ElementTree.fromstring(doc.read("word/document.xml"))
                            (folder / (name + ".txt")).write_text(
                                "\n".join(
                                    "".join(p.itertext())
                                    for p in docroot.findall(
                                        ".//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p"
                                    )
                                )
                            )
                    elif name.lower().endswith(".pdf"):
                        run(
                            folder,
                            "pdftotext-" + name,
                            [
                                "pdftotext",
                                "-layout",
                                str(folder / name),
                                str(folder / (name + ".txt")),
                            ],
                        )
                        run(
                            folder,
                            "render-" + name,
                            [
                                "pdftoppm",
                                "-png",
                                "-scale-to",
                                "1600",
                                str(folder / name),
                                str(folder / name),
                            ],
                        )

    unpack((folder / "supplement.zip").read_bytes(), "")
    write(folder / "archive-inventory.json", inventory)


def extra_sources():
    fetch(
        "history-pmid-29944653.xml",
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=29944653&retmode=xml",
    )
    fetch(
        "envo.json",
        "https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_01001002",
    )
    fetch(
        "ncbi-taxonomy.xml",
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=36667,236401,1699721,336809,84565,186490,573657&retmode=xml",
    )
    fetch(
        "author-tree.json",
        "https://api.github.com/repos/Bessem06/Hemipteran/git/trees/bb20c83c112331442b19a7b5f16f6cd6389221b4?recursive=1",
    )
    fetch(
        "bioproject.xml",
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=bioproject&id=341855,342845,343314&retmode=xml",
    )
    fetch("imodulon-catalog.json", "https://imodulondb.org/api/datasets")
    for key, filename in zip(
        RECORDS,
        ["Philaenus_iNA761.xml", "Graphocephala_iNA629.xml", "Neotibicen_iNA533.xml"],
        strict=True,
    ):
        model = "MODEL180625000" + str(int(key) - 3)
        fetch(
            filename, f"https://www.ebi.ac.uk/biomodels/model/download/{model}?filename={filename}"
        )


def replay():
    from communitymech.network.auditor import NetworkIntegrityAuditor
    from communitymech.ontology_adapters import ontology_adapter

    folder = SCRATCH / "shared"
    article = "".join(ElementTree.parse(folder / "primary.xml").getroot().itertext())
    pubmed = "".join(ElementTree.parse(folder / "pubmed.xml").getroot().itertext())

    def norm(s):
        return " ".join(unicodedata.normalize("NFKC", s).split())

    for key, row in RECORDS.items():
        d = yaml.safe_load((ROOT / row["target_path"]).read_text())
        snippets, terms = [], []

        def walk(obj, path="", snippets=snippets, terms=terms):
            if isinstance(obj, dict):
                if "snippet" in obj:
                    snippets.append(
                        {
                            "path": path,
                            "reference": obj["reference"],
                            "fresh_article_match": norm(obj["snippet"]) in norm(article),
                            "fresh_pubmed_match": norm(obj["snippet"]) in norm(pubmed),
                        }
                    )
                if isinstance(obj.get("id"), str) and re.match(
                    r"(?:NCBITaxon|ENVO|GO|CHEBI):", obj["id"]
                ):
                    adapter = ontology_adapter(obj["id"].split(":")[0])
                    terms.append(
                        {
                            "path": path,
                            "id": obj["id"],
                            "label": obj["label"],
                            "authority_label": adapter.label(obj["id"]),
                        }
                    )
                for k, v in obj.items():
                    walk(v, f"{path}.{k}" if path else k)
            elif isinstance(obj, list):
                for i, v in enumerate(obj):
                    walk(v, f"{path}[{i}]")

        walk(d)
        write(
            SCRATCH / key / "replay-qualified.json",
            {
                "observed_at": now(),
                "snippets": snippets,
                "terms": terms,
                "network": [
                    str(x)
                    for x in NetworkIntegrityAuditor().audit_community(ROOT / row["target_path"])
                ],
            },
        )


def models():
    from openpyxl import load_workbook

    folder = SCRATCH / "shared"
    reports = []
    for n, filename in enumerate(
        ["Philaenus_iNA761.xml", "Graphocephala_iNA629.xml", "Neotibicen_iNA533.xml"], 3
    ):
        fetch(
            "author-" + filename,
            "https://raw.githubusercontent.com/Bessem06/Hemipteran/bb20c83c112331442b19a7b5f16f6cd6389221b4/Models/"
            + filename,
        )
        raw = (folder / filename).read_bytes()
        root = ElementTree.fromstring(raw)
        metadata = json.loads((folder / f"MODEL180625000{n}-files.json").read_text())["main"][0]
        assert sha(raw) == metadata["sha256sum"]
        reports.append(
            {
                "filename": filename,
                "sha256": sha(raw),
                "archive_hash_matches": True,
                "author_sha256": sha((folder / ("author-" + filename)).read_bytes()),
                "compartments": [x.attrib for x in root.iter() if x.tag.endswith("}compartment")],
                "model": [x.attrib for x in root.iter() if x.tag.endswith("}model")],
                "selected_bounds": [
                    {
                        "reaction": x.attrib,
                        "parameters": [a.attrib for a in x.iter() if a.tag.endswith("}parameter")],
                    }
                    for x in root.iter()
                    if x.tag.endswith("}reaction")
                    and any(
                        t in x.attrib.get("id", "")
                        for t in ["EX_glc", "EX_nh4", "EX_o2", "BIOMASS"]
                    )
                ],
            }
        )
    write(folder / "model-audit.json", reports)
    sheets = {}
    for n in range(1, 7):
        book = load_workbook(folder / f"mbo005184075st{n}.xlsx", read_only=True, data_only=True)
        for sheet in book:
            selected = sheet.title in {
                "Table S1e",
                "Table S1f",
                "Table S1g",
                "Table S1h",
                "Table S1i",
                "Table S5o",
                "Table S6a",
                "Table S6d",
                "Table S6g",
            }
            rows = list(sheet.iter_rows(values_only=True))
            sheets[sheet.title] = {
                "workbook": f"mbo005184075st{n}.xlsx",
                "rows": sheet.max_row,
                "columns": sheet.max_column,
                "read_scope": "all rows" if selected else "first three rows and dimensions only",
                "values": rows if selected else rows[:3],
            }
    write(folder / "table-audit.json", sheets)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("mode", choices=["extract", "extra-sources", "replay", "models"])
    args = p.parse_args()
    {"extract": extract, "extra-sources": extra_sources, "replay": replay, "models": models}[
        args.mode
    ]()
