"""Tests for the reusable CommonTaxon records (kb/taxa/) and the new
abundance / common_taxon fields on TaxonomicComposition."""

import subprocess
from pathlib import Path

import yaml

SCHEMA = "src/communitymech/schema/communitymech.yaml"
TAXA_DIR = Path("kb/taxa")


def _validate(target_class: str, path: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["uv", "run", "linkml-validate", "-s", SCHEMA, "--target-class", target_class, str(path)],
        capture_output=True,
        text=True,
    )


def test_taxa_records_validate_against_common_taxon():
    files = sorted(TAXA_DIR.glob("*.yaml"))
    assert files, "no kb/taxa/*.yaml records found"
    for f in files:
        res = _validate("CommonTaxon", f)
        assert (
            res.returncode == 0
        ), f"{f} failed CommonTaxon validation:\n{res.stdout}\n{res.stderr}"


def test_taxa_record_structure():
    rec = yaml.safe_load((TAXA_DIR / "Shewanella_oneidensis_MR1.yaml").read_text())
    assert rec["id"] == "CommunityMech:taxon:000001"
    assert rec["taxon_term"]["term"]["id"] == "NCBITaxon:211586"
    # genomes use NCBI Assembly accessions
    assert rec["genomes"][0]["id"].startswith("GCF_")
    # genes carry standardized ids + locus tags + GO function terms
    genes = {g["gene_symbol"]: g for g in rec["genes"]}
    assert "mtrC" in genes
    assert genes["mtrC"]["gene_id"].startswith("KEGG:")
    assert genes["mtrC"]["locus_tag"] == "SO_1778"
    assert genes["mtrC"]["go_terms"][0]["id"] == "GO:0009055"
    assert genes["mtrC"]["genome"] == rec["genomes"][0]["id"]


def test_schema_defines_new_fields():
    schema = yaml.safe_load(Path(SCHEMA).read_text())
    classes = schema["classes"]
    tc = classes["TaxonomicComposition"]["attributes"]
    for slot in ("absolute_abundance", "relative_abundance", "common_taxon"):
        assert slot in tc, f"TaxonomicComposition missing {slot}"
    # absolute and relative abundance are independent, optional, numeric
    assert tc["absolute_abundance"]["range"] == "float"
    assert tc["relative_abundance"]["range"] == "float"
    assert tc["absolute_abundance"].get("required", False) is False
    assert tc["relative_abundance"].get("required", False) is False
    for cls in ("CommonTaxon", "GenomeRecord", "GeneAnnotation"):
        assert cls in classes, f"schema missing class {cls}"


def test_community_links_common_taxon():
    """The demonstration community references the reusable taxon records."""
    comm = yaml.safe_load(
        Path(
            "kb/communities/Shewanella_Geobacter_Exoelectrogenic_Biofilm_Community.yaml"
        ).read_text()
    )
    refs = {t.get("common_taxon") for t in comm["taxonomy"] if t.get("common_taxon")}
    assert {"CommunityMech:taxon:000001", "CommunityMech:taxon:000002"} <= refs


def test_taxoncomposition_accepts_separate_abundances(tmp_path):
    """A TaxonomicComposition with both absolute and relative abundance validates."""
    community = {
        "id": "CommunityMech:000999",
        "name": "abundance field smoke test",
        "taxonomy": [
            {
                "taxon_term": {
                    "preferred_term": "Escherichia coli",
                    "term": {"id": "NCBITaxon:562", "label": "Escherichia coli"},
                },
                "absolute_abundance": 1.2e8,
                "absolute_abundance_unit": "cells/mL",
                "relative_abundance": 0.35,
                "relative_abundance_unit": "fraction",
            }
        ],
    }
    f = tmp_path / "c.yaml"
    f.write_text(yaml.safe_dump(community))
    res = _validate("MicrobialCommunity", f)
    assert res.returncode == 0, f"abundance smoke test failed:\n{res.stdout}\n{res.stderr}"
