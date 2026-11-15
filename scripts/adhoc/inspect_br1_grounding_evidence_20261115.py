"""Inspect exact BR1 genome/source grounding for #2849, 2026-11-15.

Inputs: frozen NCBI/GTDB snapshots, primary XML and SHA-pinned local crosswalk.
Output: public metadata JSON on stdout. No matching rerun, network or writes.
"""

import argparse
import csv
import gzip
import hashlib
import json
from pathlib import Path

from defusedxml import ElementTree

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/br1-source-review-20261115"
TABLE_SHA = "761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd"
EXPECTED = {
    "assembly-001/source.json": "d94ccc026216f2751d7d758e85c435a6f7464e797089ad9e639c8825b18c6dea",
    "gtdb-card-001/source.json": "3d9c1d568a0423d638dc272ab79ee1335e364472e172e7074d86df4438ca36e4",
    "gtdb-history-001/source.json": "f96b4c8f28a77e385d2017b66455022e621f0dfb1f9e4013cc4618f6ed31c583",
    "gtdb-version-001/source.json": "b99336a0d4b7d5fc8e05a863eb991129ac0835794e9356a2f629c85bf2a2e159",
    "study-001/article.xml": "21e4eab4a11a23d72b2e0b22d83d6d98d8e0fb5897bb1485dfcbe484d80e9cb8",
}
RECORD = "data/isolates/Microbacterium_BR1_Sulfadiazine_Cleaving_Isolate_Baseline.yaml"
RECORD_SHA = "c0326c5cdaf678c922659c33dbe4fe1b5717be2bf79dab54d672f160574c0fe5"


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--crosswalk", type=Path, required=True)
    args = parser.parse_args()
    inputs = {name: (STATE / name).read_bytes() for name in EXPECTED}
    require(
        all(sha(raw) == EXPECTED[name] for name, raw in inputs.items()),
        "authority snapshot differs",
    )
    require(sha((ROOT / RECORD).read_bytes()) == RECORD_SHA, "target record differs")
    require(sha(args.crosswalk.read_bytes()) == TABLE_SHA, "crosswalk differs")
    assembly_doc = json.loads(inputs["assembly-001/source.json"])
    require(
        assembly_doc["total_count"] == 1 and len(assembly_doc["reports"]) == 1,
        "one assembly required",
    )
    assembly = assembly_doc["reports"][0]
    require(
        assembly["accession"] == "GCF_002812725.1"
        and assembly["paired_accession"] == "GCA_002812725.1",
        "assembly pair differs",
    )
    require(
        assembly["organism"]["tax_id"] == 1070896
        and assembly["organism"]["infraspecific_names"]["strain"] == "BR1",
        "BR1 identity differs",
    )
    card = json.loads(inputs["gtdb-card-001/source.json"])
    require(
        card["genome"] == {"accession": "GCA_002812725.1", "name": "GCF_002812725.1"},
        "GTDB assembly differs",
    )
    require(
        card["metadata_ncbi"]["ncbi_taxid"] == 1070896
        and card["metadata_ncbi"]["ncbi_strain_identifiers"] == "BR1",
        "GTDB stock differs",
    )
    require(
        card["metadata_ncbi"]["ncbi_biosample"]
        == assembly["assembly_info"]["biosample"]["accession"]
        == "SAMN07351343",
        "sample identity differs",
    )
    history = json.loads(inputs["gtdb-history-001/source.json"])
    rows = [row for row in history if row["release"] == "R220"]
    require(len(rows) == 1, "one explicit R220 history entry required")
    r220 = rows[0]
    require(
        r220["s"] == card["metadataTaxonomy"]["gtdbSpecies"] == "s__Microbacterium sp002812725",
        "species identity differs",
    )
    fields = {
        "d": "gtdbDomain",
        "p": "gtdbPhylum",
        "c": "gtdbClass",
        "o": "gtdbOrder",
        "f": "gtdbFamily",
        "g": "gtdbGenus",
        "s": "gtdbSpecies",
    }
    require(
        all(r220[key] == card["metadataTaxonomy"][value] for key, value in fields.items()),
        "R220/current lineage differs",
    )
    article = ElementTree.fromstring(inputs["study-001/article.xml"])
    ids = {item.attrib.get("pub-id-type"): item.text for item in article.findall(".//article-id")}
    require(
        ids.get("doi") == "10.1021/acs.estlett.6c00474"
        and ids.get("pmid") == "42598292"
        and ids.get("pmcid") == "PMC13472149",
        "paper identity differs",
    )
    references = []
    for item in article.findall(".//ref-list/ref"):
        text = " ".join("".join(item.itertext()).split())
        if "SDZm4" in text or "Ricken" in text or "Bouju" in text:
            references.append(
                {
                    "id": item.get("id"),
                    "identifiers": [node.text for node in item.findall(".//pub-id")],
                }
            )
    exact_ids, exact_names, gtdb_species = [], [], []
    with gzip.open(args.crosswalk, "rt") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            if row["taxonID NCBI"] == "1070896":
                exact_ids.append(row)
            if row["species (NCBI)"].casefold() == "microbacterium sp. br1":
                exact_names.append(row)
            if row["species (GTDB)"] == "Microbacterium sp002812725":
                gtdb_species.append(row)
    result = {
        "record": RECORD,
        "record_sha256": RECORD_SHA,
        "scope": "Only BR1 stock/genome/GTDB identity; not a full-record scientific review or curation receipt.",
        "assembly": {
            "refseq": assembly["accession"],
            "genbank": assembly["paired_accession"],
            "ncbi_taxon": 1070896,
            "strain": "BR1",
            "biosample": "SAMN07351343",
            "bioproject": assembly["assembly_info"]["bioproject_accession"],
        },
        "gtdb_release_history": history,
        "r220_lineage": ";".join(r220[key] for key in fields),
        "current_card_species": card["metadataTaxonomy"]["gtdbSpecies"],
        "current_card_representative": card["metadataTaxonomy"]["gtdb_genome_representative"],
        "current_card_species_cluster_count_not_crosswalk_population": card["speciesClusterCount"],
        "api_software_version_not_database_release": json.loads(
            inputs["gtdb-version-001/source.json"]
        ),
        "primary_article": {"identifiers": ids, "stock_reference_locators": references},
        "crosswalk": {
            "sha256": TABLE_SHA,
            "exact_ncbi_id_rows": exact_ids,
            "exact_ncbi_species_name_rows": exact_names,
            "gtdb_placeholder_species_rows": gtdb_species,
        },
        "recommendation": {
            "gtdb_id": "GTDB:s__Microbacterium_sp002812725",
            "gtdb_taxon": "Microbacterium sp002812725",
            "curated": True,
            "basis": "Exact BR1 assembly and BioSample identity plus explicit R220 GTDB genome history.",
            "unsupported_fields_to_omit": ["majority_fraction", "total_genomes"],
            "reason": "The source route is an exact genome card/history, not an NCBI2GTDB population. Cluster size is a different denominator.",
        },
        "source_sha256": EXPECTED,
        "helper_sha256": sha(Path(__file__).read_bytes()),
        "limits": [
            "API software version2.28.1 is not a GTDB release.",
            "Release-specific assignment is from the API's explicit taxon history, not an independently downloaded R220 bulk table.",
            "No genome sequence download, ANI recomputation, canonical mutation or validator rerun was performed.",
            "Historical paper stock identity and formal species naming remain distinct from GTDB placeholder taxonomy.",
        ],
    }
    require(
        all((STATE / name).read_bytes() == raw for name, raw in inputs.items()), "sources changed"
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
