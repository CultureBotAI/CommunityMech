"""Inspect stock/genus evidence without applying a GTDB block, #2849, 2026-11-15.

Inputs: exact000532, retained primary XML/BacDive/NCBI and761crosswalk.
Output: metadata JSON stdout, no network or filesystem writes. Reference-genus
mapping is kept distinct from exact stock/genome assignment and native route.
"""

import gzip
import hashlib
import importlib.util
import json
import subprocess
from pathlib import Path

import yaml
from defusedxml import ElementTree as SafeET

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/gtdb-source-routes-2849-20261115"
RECORD = "data/isolates/Terrabacter_2APm3_Sulfadiazine_Isolate_Baseline.yaml"
PIN = "c87ef5166e75e2b7985d2b4113cacf58c369cc78"
FILES = {
    RECORD: "81c8fd983bc57050595d7a4d51b64acdf2617ce9fea0f03f7ec9db4fa617c05e",
    "scripts/gtdb_ground.py": "0fc1ba926a56e5be85cdf064db0cf56452aeeee93f15b0ced98e8f11b5296175",
    ".temp/gtdb-source-routes-2849-20261115/kg-microbe/data/raw/NCBI2GTDB.tsv.gz": "761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd",
    ".temp/gtdb-source-routes-2849-20261115/terrabacter-sources/article-002/article.xml": "21e4eab4a11a23d72b2e0b22d83d6d98d8e0fb5897bb1485dfcbe484d80e9cb8",
    ".temp/gtdb-source-routes-2849-20261115/terrabacter-sources/stock-001/bacdive-157986.html": "72345d3a4842fe66660dd41fe9222d0e4509f11b72bbfac1ed40a5ce76e804a5",
    ".temp/gtdb-source-routes-2849-20261115/terrabacter-sources/taxonomy-001/taxonomy-1472881.xml": "4ce765ceedd45b62b5766fb657cda15bab3c982242ee0e164b7207b4f354ec53",
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    if subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip() != PIN:
        raise ValueError("exact execution revision required")
    bound = dict(FILES)
    bound[str(Path(__file__).relative_to(ROOT))] = sha(Path(__file__))
    for name, expected in bound.items():
        if sha(ROOT / name) != expected:
            raise ValueError("source bytes changed: " + name)
    source = ROOT / "scripts/gtdb_ground.py"
    spec = importlib.util.spec_from_file_location("terrabacter_native_gtdb", source)
    native = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(native)
    table = STATE / "kg-microbe/data/raw/NCBI2GTDB.tsv.gz"
    rows = native.collect_rows(
        table, {"1472881", "53355", "37948"}, {"terrabacter sp. 2apm3"}, {"terrabacter"}
    )
    with gzip.open(table, "rt") as stream:
        header = next(stream).rstrip("\n").split("\t")
    exact = native.resolve_target("1472881", "Terrabacter sp. 2APm3", *rows)
    genus = native.resolve_target("53355", "Terrabacter", *rows)
    taxon = (
        SafeET.parse(STATE / "terrabacter-sources/taxonomy-001/taxonomy-1472881.xml")
        .getroot()
        .find("Taxon")
    )
    lineage = [
        {
            "id": node.findtext("TaxId"),
            "name": node.findtext("ScientificName"),
            "rank": node.findtext("Rank"),
        }
        for node in taxon.findall("./LineageEx/Taxon")
    ]
    assert taxon.findtext("TaxId") == "1472881"
    assert {"id": "53355", "name": "Terrabacter", "rank": "genus"} in lineage
    article = SafeET.parse(STATE / "terrabacter-sources/article-002/article.xml").getroot()
    paragraphs = []
    for section in article.findall(".//sec"):
        for index, node in enumerate(section.findall("p")):
            text = "".join(node.itertext())
            if "Preculture of Terrabacter" in text:
                paragraphs.append(
                    {
                        "section_id": section.attrib.get("id"),
                        "section_title": "".join(section.find("title").itertext()),
                        "paragraph_index": index,
                        "quote": "Preculture of Terrabacter (DSMZ 28514)",
                        "quote_present": "Preculture of Terrabacter (DSMZ 28514)" in text,
                    }
                )
    assert len(paragraphs) == 1 and paragraphs[0]["quote_present"]
    stored = yaml.safe_load((ROOT / RECORD).read_bytes())["taxonomy"][0]["taxon_term"]
    result = {
        "execution_revision": PIN,
        "record": RECORD,
        "inputs": bound,
        "source_stock_identity": {
            "paper": "https://pmc.ncbi.nlm.nih.gov/articles/PMC13472149/",
            "paper_locators": paragraphs,
            "catalogue": "https://bacdive.dsmz.de/strain/157986",
            "designation": "2APm3",
            "collection": "DSM28514",
            "catalogue_ncbi_link": "54015 (generic Terrabacter sp.; not used to replace exact stock identifier)",
        },
        "ncbi_authority": {
            "id": taxon.findtext("TaxId"),
            "label": taxon.findtext("ScientificName"),
            "rank": taxon.findtext("Rank"),
            "lineage": lineage,
        },
        "stored_descriptor": stored,
        "native_exact_stock_result": exact,
        "reference_genus_result": genus,
        "exact_stock_rows": [
            dict(zip(header, row, strict=True)) for row in rows[0].get("1472881", [])
        ],
        "reference_genus_rows": [
            dict(zip(header, row, strict=True)) for row in rows[2].get("terrabacter", [])
        ],
        "old_prose_37948_rows": [
            dict(zip(header, row, strict=True)) for row in rows[0].get("37948", [])
        ],
        "limits": "This establishes stock-name/deposit identity and authoritative NCBI genus ancestry. Genus crosswalk rows are reference-population evidence, not a sequenced-genome identity for2APm3. No block or scientific status is changed by this output.",
    }
    if bound != {name: sha(ROOT / name) for name in bound}:
        raise ValueError("inputs changed during read-only inspection")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
