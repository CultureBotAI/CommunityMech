"""Inspect retained R232 populations for the MDSC hold, #2877, 2026-11-15.

Inputs: exact previously downloaded official workbook, source receipt and record.
Output: metadata-only JSON on stdout; no downloads, record writes or approval.
Read NCBI-row identities separately from mentions in the GTDB result column.
"""

import hashlib
import io
import json
from pathlib import Path

import openpyxl
import yaml

ROOT = Path(__file__).resolve().parents[2]
CAPTURE = ".temp/gtdb-r232-mdsc-20261115/source-001/"
WORKBOOK = CAPTURE + "ncbi_vs_gtdb_r232_bacteria.xlsx"
RECEIPT = CAPTURE + "source-receipt.json"
RECORD = "kb/communities/Mucin_Glycan_MDSC_Synthetic_Gut_Community.yaml"
SOURCE_URL = (
    "https://data.gtdb.ecogenomic.org/releases/release232/232.0/"
    "auxillary_files/ncbi_vs_gtdb_r232_bacteria.xlsx"
)
SOURCE_SHA = "e401d80c914c727268c184d19201aa35dcd23aabfd027a0d6e5a57476e71f3de"
RECORD_SHA = "4ef5925538ded3549c72fd84eaa0786922b4f9565de33946289104cef18a5d49"
NAMES = ("Desulfovibrio piger", "Faecalibacterium duncaniae", "Faecalibacterium prausnitzii")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def inspect():
    helper = str(Path(__file__).resolve().relative_to(ROOT))
    captured = {name: (ROOT / name).read_bytes() for name in (WORKBOOK, RECEIPT, RECORD, helper)}
    metadata = json.loads(captured[RECEIPT])
    if (
        sha(captured[WORKBOOK]) != SOURCE_SHA
        or metadata["source_url"] != SOURCE_URL
        or metadata["sha256"] != SOURCE_SHA
        or metadata["bytes"] != len(captured[WORKBOOK])
        or sha(captured[RECORD]) != RECORD_SHA
    ):
        raise ValueError("retained source or record differs from the reviewed input")
    workbook = openpyxl.load_workbook(
        io.BytesIO(captured[WORKBOOK]), read_only=True, data_only=True
    )
    sheet = workbook["Species"]
    rows = list(sheet.iter_rows(values_only=True))
    workbook.close()
    expected_header = (
        "NCBI species",
        "Number of genomes",
        "Number of R232 species",
        "List of R232 species",
    )
    if tuple(rows[0]) != expected_header:
        raise ValueError("unexpected primary Species worksheet layout")
    observations = []
    for name in NAMES:
        exact_rows, mentions = [], []
        for number, values in enumerate(rows[1:], start=2):
            if values[0] == "s__" + name:
                exact_rows.append({"row": number, "values": list(values)})
            if isinstance(values[3], str) and name.lower() in values[3].replace("_", " ").lower():
                mentions.append({"row": number, "values": list(values)})
        observations.append(
            {"query": name, "exact_ncbi_species_rows": exact_rows, "gtdb_column_mentions": mentions}
        )
    record = yaml.safe_load(captured[RECORD])
    descriptors = [
        {
            "taxonomy_index": index,
            "taxon_term": entry["taxon_term"],
            "strain_designation": entry.get("strain_designation"),
        }
        for index, entry in enumerate(record["taxonomy"])
        if entry["taxon_term"]["term"]["id"] in {"NCBITaxon:901", "NCBITaxon:411483"}
    ]
    if len(descriptors) != 2:
        raise ValueError("expected exactly two held descriptors")
    if any((ROOT / name).read_bytes() != raw for name, raw in captured.items()):
        raise ValueError("captured input changed during inspection")
    return {
        "issue": 2877,
        "source": metadata,
        "inputs": {name: sha(raw) for name, raw in captured.items()},
        "worksheet": "Species",
        "header": list(expected_header),
        "data_rows_scanned": len(rows) - 1,
        "observations": observations,
        "stored_descriptors": descriptors,
        "stored_curation_events": [
            event
            for event in record["curation_history"]
            if event.get("action") == "FIX_MDSC_GTDB_GROUNDINGS"
        ],
        "inputs_unchanged": True,
        "canonical_writes": False,
        "scientific_review": False,
        "limits": "Exact NCBI species rows and GTDB-column mentions are different selections. Empty exact-row results refer only to this worksheet and spelling. Cells do not independently identify study-stock assemblies, numeric NCBI IDs or complete lineages. No crosswalk release equivalence or application approval is inferred.",
    }


if __name__ == "__main__":
    print(json.dumps(inspect(), indent=2))
