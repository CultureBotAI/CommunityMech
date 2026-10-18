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


def test_taxa_records_have_gtdb_and_lpsn_grounding():
    """Every CommonTaxon record in kb/taxa/ carries NCBITaxon, GTDB, and LPSN grounding."""
    from communitymech.validators.gtdb_coherence import validate_gtdb_coherence
    from communitymech.validators.gtdb_lineage_tree import check_lineage_shape

    files = sorted(TAXA_DIR.glob("*.yaml"))
    assert files, "no kb/taxa/*.yaml records found"
    for path in files:
        rec = yaml.safe_load(path.read_text())
        taxon_term = rec["taxon_term"]
        term = taxon_term["term"]
        assert term["id"].startswith("NCBITaxon:")
        assert term["label"]
        assert taxon_term.get("gtdb_grounding_status") == "GROUNDED"
        gtdb = taxon_term.get("gtdb_classification")
        assert isinstance(gtdb, dict), f"{path} missing gtdb_classification"
        assert gtdb["gtdb_id"].startswith("GTDB:")
        assert gtdb["ncbi_source_id"] == term["id"]
        assert gtdb["gtdb_lineage"].startswith("d__")
        assert "LPSN" in (taxon_term.get("notes") or "")
        assert validate_gtdb_coherence(path) == []
        assert check_lineage_shape(rec) == []
        history = rec.get("curation_history") or []
        assert any(
            e.get("curator") == "gtdb_ground.py" and e.get("action") == "GTDB_GROUND"
            for e in history
            if isinstance(e, dict)
        ), f"{path} missing GTDB_GROUND curation_history event (#2028)"


def test_gtdb_ground_community_taxa_reads_common_taxon():
    """gtdb_ground.py::community_taxa extracts top-level taxon_term on CommonTaxon (#2028)."""
    import importlib.util
    import sys

    spec = importlib.util.spec_from_file_location("gtdb_ground", Path("scripts/gtdb_ground.py"))
    module = importlib.util.module_from_spec(spec)
    sys.modules["gtdb_ground"] = module
    spec.loader.exec_module(module)

    assert module.community_taxa(TAXA_DIR / "Geobacter_sulfurreducens.yaml") == [
        ("35554", "Geobacter sulfurreducens")
    ]
    assert module.community_taxa(TAXA_DIR / "Shewanella_oneidensis_MR1.yaml") == [
        ("211586", "Shewanella oneidensis MR-1")
    ]


def test_taxon_descriptor_slots_match_schema():
    """TAXON_DESCRIPTOR_SLOTS matches every range: TaxonDescriptor slot in the schema (#2029)."""
    from communitymech.taxon_blocks import TAXON_DESCRIPTOR_SLOTS

    schema = yaml.safe_load(Path(SCHEMA).read_text())
    found = set()
    for cls_name, cls_def in (schema.get("classes") or {}).items():
        for slot_name, slot_def in ((cls_def or {}).get("attributes") or {}).items():
            if isinstance(slot_def, dict) and slot_def.get("range") == "TaxonDescriptor":
                found.add((cls_name, slot_name))
    assert found == set(TAXON_DESCRIPTOR_SLOTS), (
        f"Schema range: TaxonDescriptor slots {sorted(found)} drifted from "
        f"TAXON_DESCRIPTOR_SLOTS {sorted(TAXON_DESCRIPTOR_SLOTS)} (#2029)"
    )


def test_iter_taxon_descriptors_reaches_all_six_schema_slots():
    """iter_taxon_descriptors and all validator walkers agree across all 6 slots (#2029)."""
    from communitymech.taxon_blocks import iter_taxon_descriptors
    from communitymech.validators.gtdb_coherence import _taxon_terms
    from communitymech.validators.gtdb_lineage_tree import _descriptors as _lineage_descriptors
    from communitymech.validators.prokaryotic_lineage import _descriptors as _prok_descriptors

    doc = {
        "taxon_term": {"preferred_term": "RootTaxon"},
        "taxonomy": [
            {"taxon_term": {"preferred_term": "MemberTaxon"}},
            None,
        ],
        "ecological_interactions": [
            {
                "name": "Syntrophy",
                "source_taxon": {"preferred_term": "SourceTaxon"},
                "target_taxon": {"preferred_term": "TargetTaxon"},
                "participating_taxa": [
                    {"preferred_term": "ParticipantA"},
                    "malformed-non-dict",
                    {"preferred_term": "ParticipantB"},
                ],
            },
            None,
        ],
        "engineering_design": {
            "counter_selection": [
                {"excluded_taxon": {"preferred_term": "ExcludedTaxon"}},
                None,
            ]
        },
    }
    expected = [
        "RootTaxon",
        "MemberTaxon",
        "SourceTaxon",
        "TargetTaxon",
        "ParticipantA",
        "ParticipantB",
        "ExcludedTaxon",
    ]
    assert [d["preferred_term"] for d in iter_taxon_descriptors(doc)] == expected
    assert [d["preferred_term"] for _, d in _taxon_terms(doc)] == expected
    assert [d["preferred_term"] for d in _lineage_descriptors(doc)] == expected
    assert [d["preferred_term"] for _, d in _prok_descriptors(doc)] == expected

    # Malformed non-list container slots must not raise TypeError.
    malformed = {
        "taxonomy": "not-a-list",
        "ecological_interactions": 42,
        "engineering_design": {"counter_selection": "not-a-list"},
    }
    assert list(iter_taxon_descriptors(malformed)) == []
    assert list(_taxon_terms(malformed)) == []
    assert list(_lineage_descriptors(malformed)) == []
    assert list(_prok_descriptors(malformed)) == []
