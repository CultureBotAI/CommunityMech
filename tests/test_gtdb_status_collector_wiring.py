"""The corpus reproducibility collector must use the real CLI keys (#2854)."""

import gzip
import importlib.util
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]


def load(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.mark.parametrize(
    "label,rank,normalized",
    [
        ("Mycobacterium", "genus", "Mycobacterium"),
        ("Candidatus Brocadia", "genus", "Brocadia"),
        ("Family Group", "family", "FamilyGroup"),
        ("Candidatus Brocadia sinica", "species", "Brocadia sinica"),
    ],
)
def test_real_native_classification_and_collector_agree(
    tmp_path, monkeypatch, label, rank, normalized
):
    native = load("native_status_collector", "scripts/gtdb_ground.py")
    corpus = load("corpus_status_collector", "tests/test_gtdb_coherence_validator.py")
    mapping = tmp_path / "kg-microbe/data/raw/NCBI2GTDB.tsv.gz"
    mapping.parent.mkdir(parents=True)
    row = [""] * 19
    row[0], row[2], row[3] = "999999", "10", "1.0"
    row[4:11] = [
        "Bacteria",
        "Actinomycetota",
        "Actinomycetes",
        "Mycobacteriales",
        "Mycobacteriaceae",
        "Mycobacterium",
        "Mycobacterium example",
    ]
    row[12:19] = row[4:11]
    ncbi_column, gtdb_column = {"genus": (9, 17), "family": (8, 16), "species": (10, 18)}[rank]
    row[ncbi_column], row[gtdb_column] = label, normalized
    with gzip.open(mapping, "wt") as stream:
        stream.write("\t".join(f"column{i}" for i in range(19)) + "\n")
        stream.write("\t".join(row) + "\n")
    record = tmp_path / "kb/communities/collector.yaml"
    record.parent.mkdir(parents=True)
    (tmp_path / "data/isolates").mkdir(parents=True)
    document = {
        "id": "CommunityMech:999999",
        "taxonomy": [
            {
                "taxon_term": {
                    "term": {"id": "NCBITaxon:123456", "label": label},
                    "gtdb_grounding_status": "NOT_ATTEMPTED",
                }
            }
        ],
    }
    record.write_text(yaml.safe_dump(document, sort_keys=False))
    monkeypatch.setattr(native, "outside_gtdb_scope", lambda _: False)
    monkeypatch.setattr(corpus, "REPO", tmp_path)
    # The real CLI collector and writer first certify this current status.
    assert (
        native.main(
            [
                "--community",
                str(record),
                "--kg-microbe-dir",
                str(mapping.parents[2]),
                "--apply-status",
            ]
        )
        == 0
    )
    written = yaml.safe_load(record.read_bytes())
    assert written["taxonomy"][0]["taxon_term"]["gtdb_grounding_status"] == "NOT_ATTEMPTED"
    corpus.test_the_stored_statuses_reproduce_from_the_classifier(native, mapping, True)
    # A wrong stored status must still fail; restore must immediately pass.
    written["taxonomy"][0]["taxon_term"]["gtdb_grounding_status"] = "UNRESOLVED"
    record.write_text(yaml.safe_dump(written, sort_keys=False))
    with pytest.raises(AssertionError, match="classifier says NOT_ATTEMPTED"):
        corpus.test_the_stored_statuses_reproduce_from_the_classifier(native, mapping, True)
    written["taxonomy"][0]["taxon_term"]["gtdb_grounding_status"] = "NOT_ATTEMPTED"
    record.write_text(yaml.safe_dump(written, sort_keys=False))
    corpus.test_the_stored_statuses_reproduce_from_the_classifier(native, mapping, True)
