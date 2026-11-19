"""Read retained official R232 correspondence for #2833/#2948, 2026-11-16.

Inputs: exact workbook/receipt and three frozen community records.
Output: exclusive metadata JSON; no acquisition, canonical edits or approval.
Parse the captured workbook bytes, then recheck every captured input.
"""

import argparse
import hashlib
import io
import json
from pathlib import Path

import openpyxl
import yaml

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ".temp/akkermansia-source-20261116/retained-source-001/"
WORKBOOK = SOURCE + "ncbi_vs_gtdb_r232_bacteria.xlsx"
RECEIPT = SOURCE + "source-receipt.json"
SOURCE_SHA = "e401d80c914c727268c184d19201aa35dcd23aabfd027a0d6e5a57476e71f3de"
RECEIPT_SHA = "9f0222100c6b5b4952d83ac0733ffba4d07e39471e69caa0420a8aa233157cf2"
SOURCE_URL = (
    "https://data.gtdb.ecogenomic.org/releases/release232/232.0/"
    "auxillary_files/ncbi_vs_gtdb_r232_bacteria.xlsx"
)
RECORDS = {
    "kb/communities/Amsterdam_10Species_Gut_Invasion_SynCom.yaml": (
        "CommunityMech:000382",
        "215177f0e7ebc45fa0b436e3877625722a6b5b1f3f0245e974fe7cda5abc2076",
    ),
    "kb/communities/MUC2_Human_Gut_Commensal_Defined_Consortium.yaml": (
        "CommunityMech:000351",
        "01cb4512723915154b17fa1676382c9807fda7f733fc62efb63afabdad3e3742",
    ),
    "kb/communities/Mucin_Glycan_MDSC_Synthetic_Gut_Community.yaml": (
        "CommunityMech:000392",
        "5beb7303470d09713d43acaeca51691badf905e3d8044341a5402695ead28393",
    ),
}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def inspect():
    helper = str(Path(__file__).resolve().relative_to(ROOT))
    captured = {path: (ROOT / path).read_bytes() for path in (WORKBOOK, RECEIPT, helper, *RECORDS)}
    receipt = json.loads(captured[RECEIPT])
    if (
        sha(captured[WORKBOOK]) != SOURCE_SHA
        or sha(captured[RECEIPT]) != RECEIPT_SHA
        or receipt["source_url"] != SOURCE_URL
        or receipt["sha256"] != SOURCE_SHA
        or receipt["bytes"] != len(captured[WORKBOOK])
        or receipt["http_status"] != 200
    ):
        raise ValueError("retained official source differs from reviewed capture")
    records = []
    for path, (record_id, expected_sha) in RECORDS.items():
        if sha(captured[path]) != expected_sha:
            raise ValueError(f"frozen record differs: {path}")
        document = yaml.safe_load(captured[path])
        if document["id"] != record_id:
            raise ValueError(f"record identity differs: {path}")
        selected = [
            {"taxonomy_index": index, "entry": entry}
            for index, entry in enumerate(document["taxonomy"])
            if entry["taxon_term"]["term"]["id"] == "NCBITaxon:239935"
        ]
        if len(selected) != 1:
            raise ValueError(f"expected one Akkermansia descriptor: {path}")
        records.append({"path": path, "record_id": record_id, "selected": selected})
    workbook = openpyxl.load_workbook(
        io.BytesIO(captured[WORKBOOK]), read_only=True, data_only=True
    )
    rows = list(workbook["Species"].iter_rows(values_only=True))
    sheets = workbook.sheetnames
    workbook.close()
    header = (
        "NCBI species",
        "Number of genomes",
        "Number of R232 species",
        "List of R232 species",
    )
    if tuple(rows[0]) != header:
        raise ValueError("unexpected Species worksheet header")
    exact = []
    mentions = []
    for number, values in enumerate(rows[1:], start=2):
        observation = {"row": number, "values": list(values)}
        if values[0] == "s__Akkermansia muciniphila":
            exact.append(observation)
        if isinstance(values[3], str) and "Akkermansia" in values[3]:
            mentions.append(observation)
    if any((ROOT / path).read_bytes() != raw for path, raw in captured.items()):
        raise ValueError("captured input changed during inspection")
    return {
        "issues": [2833, 2948],
        "source": receipt,
        "inputs": {path: sha(raw) for path, raw in captured.items()},
        "sheets": sheets,
        "worksheet": "Species",
        "header": list(header),
        "data_rows_scanned": len(rows) - 1,
        "exact_ncbi_name": "s__Akkermansia muciniphila",
        "exact_ncbi_name_rows": exact,
        "gtdb_genus_mentions": mentions,
        "current_descriptors": records,
        "inputs_unchanged": True,
        "canonical_writes": False,
        "scientific_review": False,
        "limits": [
            "Exact NCBI-name rows and GTDB-column mentions are different populations.",
            "This workbook does not independently prove numeric NCBI IDs or full lineages.",
            "No exact experimental-stock genome or BAA-83/BAA-835 synonymy is inferred.",
            "The 761 crosswalk release and its relationship to R232 remain unestablished.",
            "Source extraction alone authorizes no canonical change or test exemption.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    result = inspect()
    with args.output.open("x") as handle:
        json.dump(result, handle, indent=2)
        handle.write("\n")
    print(json.dumps({"output": str(args.output), "sha256": sha(args.output.read_bytes())}))


if __name__ == "__main__":
    main()
