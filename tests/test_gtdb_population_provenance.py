"""Source-population controls for #2833; no record or source mutations."""

from copy import deepcopy

import pytest
import test_gtdb_support_counts as counts
import yaml


def species_block(name):
    record = yaml.safe_load((counts.REPO / "kb/communities" / name).read_text())
    blocks = [
        row["taxon_term"]["gtdb_classification"]
        for row in record["taxonomy"]
        if row["taxon_term"]["term"]["id"] == "NCBITaxon:53443"
    ]
    assert len(blocks) == 1
    return ("kb/communities/" + name, "Blautia hydrogenotrophica", blocks[0])


@pytest.fixture
def actual_populations():
    return [
        species_block("LBNL_Human_Gut_Interaction_SynCom.yaml"),
        species_block("Mucin_Glycan_MDSC_Synthetic_Gut_Community.yaml"),
    ]


def test_verified_distinct_populations_keep_their_actual_counts(actual_populations):
    assert [row[2]["total_genomes"] for row in actual_populations] == [15, 25]
    counts.test_every_kb_taxon_reports_one_denominator(actual_populations)


def test_conflicting_counts_within_one_source_still_fail(actual_populations):
    original = actual_populations[0]
    altered = deepcopy(original[2])
    altered["total_genomes"] += 1
    with pytest.raises(AssertionError, match="several denominators"):
        counts.test_every_kb_taxon_reports_one_denominator(
            [original, ("Other_record.yaml", original[1], altered)]
        )


@pytest.mark.parametrize(
    "source",
    ["novel curated dataset", "manual GTDB R232 ncbi_vs_gtdb_r232_bacteria.xlsx species tally"],
)
def test_curated_or_source_labels_cannot_create_a_population_exemption(actual_populations, source):
    original = actual_populations[0]
    altered = deepcopy(original[2])
    altered.update(total_genomes=25, curated=True, mapping_source=source)
    with pytest.raises(AssertionError, match="several denominators"):
        counts.test_every_kb_taxon_reports_one_denominator(
            [original, ("Unverified_record.yaml", original[1], altered)]
        )


@pytest.mark.parametrize(
    "field,value",
    [
        ("total_genomes", 15),
        ("total_genomes", None),
        ("support_genomes", 25),
        ("majority_fraction", 0.9),
        ("mapping_source", "different release"),
        ("gtdb_id", "GTDB:s__Different_species"),
    ],
)
def test_changed_pinned_assertion_needs_fresh_source_review(actual_populations, field, value):
    changed = deepcopy(actual_populations)
    changed[1][2][field] = value
    with pytest.raises(AssertionError):
        counts.test_every_kb_taxon_reports_one_denominator(changed)


def test_changed_primary_evidence_is_not_accepted(actual_populations, monkeypatch):
    original = counts.Path.read_bytes

    def changed_bytes(path):
        raw = original(path)
        if path.name == "gtdb-r232-blautia-source-proof.json":
            return raw.replace(b"25,", b"26,", 1)
        return raw

    monkeypatch.setattr(counts.Path, "read_bytes", changed_bytes)
    with pytest.raises(AssertionError):
        counts.test_every_kb_taxon_reports_one_denominator(actual_populations)
