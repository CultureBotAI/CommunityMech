"""Reconcile actual BioProject/Sample metadata to source S1, #1548, 2026-11-15.

Inputs: retained public NCBI HTML/XML and publisher Table S1; read-only NCBI DB.
Output: JSON on stdout, no source/canonical writes or network. Stock matches
require the linked project, source genus/sample-name agreement and the exact
numeric strain suffix, not punctuation alone. Extra project stocks are excluded.
"""

import argparse
import hashlib
import json
import re
import sqlite3
from pathlib import Path

import openpyxl
from bs4 import BeautifulSoup
from defusedxml import ElementTree


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, required=True)
    parser.add_argument("--samples", type=Path, required=True)
    parser.add_argument("--table", type=Path, required=True)
    parser.add_argument("--ncbi", type=Path, required=True)
    args = parser.parse_args()
    soup = BeautifulSoup(args.project.read_bytes(), "html.parser")
    projects = []
    for row in soup.find_all("tr"):
        assembly = row.find("a", href=re.compile(r"/datasets/genome/GCA_"))
        if not assembly or assembly.find_parent("tr") is not row:
            continue
        sample = row.find("a", href=re.compile(r"/biosample/SAMN"))
        taxon = row.find("a", href=re.compile(r"/(?:datasets/)?taxonomy/\d+"))
        cells = row.find_all("td", recursive=False)
        projects.append(
            {
                "assembly": assembly.get_text(strip=True),
                "assembly_url": "https://www.ncbi.nlm.nih.gov" + assembly["href"],
                "biosample": sample.get_text(strip=True),
                "strain": cells[-2].get_text(strip=True),
                "taxon_name": taxon.get_text(strip=True),
                "taxon_id": "NCBITaxon:" + re.search(r"taxonomy/(\d+)", taxon["href"]).group(1),
            }
        )
    samples = {}
    for item in ElementTree.fromstring(args.samples.read_bytes()).findall("BioSample"):
        attributes = {
            node.attrib["attribute_name"]: node.text
            for node in item.findall("./Attributes/Attribute")
        }
        samples[item.attrib["accession"]] = {
            "biosample": item.attrib["accession"],
            "sample_name": item.findtext("./Ids/Id[@db_label='Sample name']"),
            "attributes": attributes,
            "organism": item.find("./Description/Organism").attrib,
            "linked_projects": [
                node.attrib.get("label")
                for node in item.findall("./Links/Link")
                if node.attrib.get("target") == "bioproject"
            ],
            "published": item.attrib.get("publication_date"),
        }
    book = openpyxl.load_workbook(args.table, data_only=True, read_only=True)
    roster = list(book["Table S1"].iter_rows(min_row=3, max_row=17, values_only=True))
    results = []
    with sqlite3.connect(args.ncbi.resolve().as_uri() + "?mode=ro", uri=True) as db:
        db.execute("PRAGMA query_only=ON")
        for number, source in enumerate(roster, 3):
            genus, paper_stock = source[0].split(" sp. ")
            suffix = paper_stock.removeprefix("RCC-").replace(".", "_")
            matches = [row for row in projects if row["strain"] == "RCC_" + suffix]
            if len(matches) != 1:
                raise ValueError(f"project match not unique: {paper_stock}")
            row = matches[0]
            sample = samples[row["biosample"]]
            if (
                sample["attributes"].get("strain") != row["strain"]
                or sample["sample_name"] != "Isolate " + genus
            ):
                raise ValueError(
                    f"independent BioSample strain/genus evidence differs: {paper_stock}: {sample}"
                )
            if sample["attributes"].get("host") != "Brachypodium distachyon" or sample[
                "linked_projects"
            ] != ["PRJNA1127609"]:
                raise ValueError("sample project/host identity differs")
            if "NCBITaxon:" + sample["organism"]["taxonomy_id"] != row["taxon_id"]:
                raise ValueError("sample/project taxon IDs differ")
            authority = db.execute(
                "SELECT predicate,value,object FROM statements WHERE subject=? AND (predicate='rdfs:label' OR predicate LIKE '%has_rank' OR predicate='rdfs:subClassOf') ORDER BY predicate",
                (row["taxon_id"],),
            ).fetchall()
            labels = [value for predicate, value, _ in authority if predicate == "rdfs:label"]
            if labels != [row["taxon_name"]]:
                raise ValueError(f"native current taxon label differs: {row['taxon_id']}")
            domains = db.execute(
                "WITH RECURSIVE parents(id) AS (SELECT ? UNION SELECT object FROM statements JOIN parents ON subject=parents.id WHERE predicate='rdfs:subClassOf') SELECT id FROM parents WHERE id IN ('NCBITaxon:2','NCBITaxon:2157','NCBITaxon:2759') ORDER BY id",
                (row["taxon_id"],),
            ).fetchall()
            if domains != [("NCBITaxon:2",)]:
                raise ValueError("sample taxon is not verified bacterial")
            results.append(
                {
                    "paper_stock": paper_stock,
                    "paper_name": source[0],
                    "source_cell": f"Table S1!A{number}",
                    **row,
                    "sample": sample,
                    "native_authority_rows": authority,
                    "verified_domain_ancestors": domains,
                    "identity_boundary": "NCBI sequence-record taxon/assembly identity, not independent species delineation or confirmation of source GTDB-tk placement",
                }
            )
    if len(results) != 15 or len({row["biosample"] for row in results}) != 15:
        raise ValueError("source roster multiplicity changed")
    excluded = [
        row for row in projects if row["biosample"] not in {item["biosample"] for item in results}
    ]
    print(
        json.dumps(
            {
                "input_sha256": {
                    str(path): digest(path) for path in (args.project, args.samples, args.table)
                },
                "study_project": "PRJNA1127609",
                "roster": results,
                "excluded_project_entries": excluded,
                "limitation": "Current linked assemblies can postdate publication; accession metadata is not proof these exact versions were used for the paper's genome analysis. No raw sequences reanalyzed.",
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
