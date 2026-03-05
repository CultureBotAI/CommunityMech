"""Tests for UniProt reference proteome strain coverage logic."""

from pathlib import Path

import yaml

from communitymech.uniprot_reference_proteomes import (
    ProteomeSummary,
    _write_proteome_csv_output,
    determine_strain_reference_proteome_coverage,
    extract_ncbi_taxonomy_id,
    infer_strain_name,
    strain_matches_proteome,
)


class StubUniProtClient:
    """Deterministic UniProt client stub for unit tests."""

    def __init__(self, mapping: dict[int, list[ProteomeSummary]]) -> None:
        self.mapping = mapping

    def search_reference_proteomes(self, taxonomy_id: int) -> list[ProteomeSummary]:
        return self.mapping.get(taxonomy_id, [])


def test_extract_ncbi_taxonomy_id() -> None:
    """NCBITaxon CURIE parsing should be strict and predictable."""
    assert extract_ncbi_taxonomy_id("NCBITaxon:83333") == 83333
    assert extract_ncbi_taxonomy_id("NCBITaxon:abc") is None
    assert extract_ncbi_taxonomy_id("GO:0008150") is None


def test_infer_strain_name_from_explicit_designation() -> None:
    """Explicit strain_name should be preferred over heuristics."""
    strain_designation = {"strain_name": "PCC 7942"}
    inferred = infer_strain_name(
        strain_designation,
        preferred_term="Synechococcus elongatus PCC 7942 cscB+",
        taxon_label="Synechococcus elongatus",
    )
    assert inferred == "PCC 7942"


def test_infer_strain_name_from_taxon_label() -> None:
    """A label with 'str.' marker should yield the trailing strain name."""
    inferred = infer_strain_name(
        strain_designation=None,
        preferred_term="Escherichia coli",
        taxon_label="Escherichia coli str. K-12",
    )
    assert inferred == "K-12"


def test_infer_strain_name_skips_generic_phrase() -> None:
    """Generic descriptors should not be treated as strain designations."""
    inferred = infer_strain_name(
        strain_designation=None,
        preferred_term="Short motile rod bacterium",
        taxon_label="Bacteria",
    )
    assert inferred is None


def test_strain_matching_token_overlap() -> None:
    """Strain matcher should tolerate equivalent tokenized variants."""
    proteome = ProteomeSummary(
        upid="UP000889800",
        proteome_type="Reference and representative proteome",
        strain="ATCC 33912 / PCC 7942 / FACHB-805",
        taxonomy_id=1140,
        scientific_name="Synechococcus elongatus (strain ATCC 33912 / PCC 7942 / FACHB-805)",
    )

    assert strain_matches_proteome("PCC 7942 cscB+", proteome)
    assert not strain_matches_proteome("DSM 8584", proteome)


def test_determine_coverage_for_single_community(tmp_path: Path) -> None:
    """End-to-end coverage check should return represented strain entries."""
    community_path = tmp_path / "example.yaml"
    data = {
        "name": "Example Community",
        "taxonomy": [
            {
                "taxon_term": {
                    "preferred_term": "Synechococcus elongatus PCC 7942 cscB+",
                    "term": {"id": "NCBITaxon:32046", "label": "Synechococcus elongatus"},
                },
                "strain_designation": {"strain_name": "PCC 7942"},
            },
            {
                "taxon_term": {
                    "preferred_term": "Bacillus subtilis",
                    "term": {"id": "NCBITaxon:1423", "label": "Bacillus subtilis"},
                }
            },
        ],
    }

    with community_path.open("w") as handle:
        yaml.safe_dump(data, handle, sort_keys=False)

    stub_client = StubUniProtClient(
        {
            32046: [
                ProteomeSummary(
                    upid="UP000889800",
                    proteome_type="Reference and representative proteome",
                    strain="ATCC 33912 / PCC 7942 / FACHB-805",
                    taxonomy_id=1140,
                    scientific_name=(
                        "Synechococcus elongatus (strain ATCC 33912 / PCC 7942 / FACHB-805)"
                    ),
                )
            ],
            1423: [],
        }
    )

    results = determine_strain_reference_proteome_coverage(
        community_path,
        include_non_strains=False,
        client=stub_client,
    )

    assert len(results) == 1
    assert results[0].preferred_term == "Synechococcus elongatus PCC 7942 cscB+"
    assert results[0].represented is True
    assert len(results[0].matched_proteomes) == 1

    all_results = determine_strain_reference_proteome_coverage(
        community_path,
        include_non_strains=True,
        client=stub_client,
    )
    assert len(all_results) == 2


def test_determine_coverage_skips_coarse_taxa_by_default(tmp_path: Path) -> None:
    """Coarse taxon IDs (e.g., NCBITaxon:2) should be excluded unless requested."""
    coarse_path = tmp_path / "coarse.yaml"
    data = {
        "name": "Coarse Community",
        "taxonomy": [
            {
                "taxon_term": {
                    "preferred_term": "Unknown bacterium X1",
                    "term": {"id": "NCBITaxon:2", "label": "Bacteria"},
                },
                "strain_designation": {"strain_name": "X1"},
            }
        ],
    }
    with coarse_path.open("w") as handle:
        yaml.safe_dump(data, handle, sort_keys=False)

    stub_client = StubUniProtClient(
        {
            2: [
                ProteomeSummary(
                    upid="UP000010310",
                    proteome_type="Representative proteome",
                    strain="X1",
                    taxonomy_id=2,
                    scientific_name="Bacteria",
                )
            ]
        }
    )

    default_results = determine_strain_reference_proteome_coverage(
        coarse_path,
        include_non_strains=False,
        client=stub_client,
    )
    assert default_results == []

    include_results = determine_strain_reference_proteome_coverage(
        coarse_path,
        include_non_strains=False,
        include_coarse_taxa=True,
        client=stub_client,
    )
    assert len(include_results) == 1


def test_write_proteome_csv_output(tmp_path: Path) -> None:
    """Proteome CSV should aggregate communities per proteome/taxon."""
    first = tmp_path / "community_a.yaml"
    second = tmp_path / "community_b.yaml"

    base_taxon = {
        "taxon_term": {
            "preferred_term": "Escherichia coli K-12",
            "term": {"id": "NCBITaxon:83333", "label": "Escherichia coli str. K-12"},
        }
    }

    with first.open("w") as handle:
        yaml.safe_dump({"name": "Community A", "taxonomy": [base_taxon]}, handle, sort_keys=False)
    with second.open("w") as handle:
        yaml.safe_dump({"name": "Community B", "taxonomy": [base_taxon]}, handle, sort_keys=False)

    stub_client = StubUniProtClient(
        {
            83333: [
                ProteomeSummary(
                    upid="UP000000625",
                    proteome_type="Reference and representative proteome",
                    strain="K12 / MG1655 / ATCC 47076",
                    taxonomy_id=83333,
                    scientific_name="Escherichia coli (strain K12)",
                )
            ]
        }
    )

    results = determine_strain_reference_proteome_coverage(
        tmp_path, include_non_strains=False, client=stub_client
    )
    output_csv = tmp_path / "proteome_report.csv"
    _write_proteome_csv_output(results, output_csv)

    rows = output_csv.read_text().strip().splitlines()
    assert (
        rows[0]
        == "uniprot_proteome_id,taxon_id,gtdb_id,is_reference,proteome_type,communities_found_in"
    )
    assert len(rows) == 2
    assert "UP000000625,NCBITaxon:83333,,true,Reference and representative proteome," in rows[1]
    assert "Community A; Community B" in rows[1]
