"""Real source admissions, CLI refusals and restoration, #2833/#2948, 2026-11-16."""

import shutil
import subprocess
import sys
from copy import deepcopy
from pathlib import Path

import pytest
import yaml

from communitymech.validators.gtdb_lineage_tree import _blocks, check_corpus
from communitymech.validators.gtdb_source_provenance import (
    AMSTERDAM,
    DEFAULT,
    EXPECTED,
    PROOFS,
    R232,
    AkkermansiaSources,
    SourceProvenanceError,
    check_source_bound_corpus,
    partition_corpus,
)

ROOT = Path(__file__).resolve().parents[1]
MUC2 = "kb/communities/MUC2_Human_Gut_Commensal_Defined_Consortium.yaml"


@pytest.fixture
def actual(tmp_path):
    paths = [
        *PROOFS,
        *EXPECTED,
        "reports/phase2-completion-20261115/gtdb-r232-blautia-source-proof.json",
        "scripts/validate_gtdb_coherence.py",
        "src/communitymech/__init__.py",
        "src/communitymech/taxon_blocks.py",
        "src/communitymech/validators/__init__.py",
        "src/communitymech/validators/gtdb_coherence.py",
        "src/communitymech/validators/gtdb_lineage_tree.py",
        "src/communitymech/validators/gtdb_source_provenance.py",
    ]
    for path in paths:
        target = tmp_path / path
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / path, target)
    return tmp_path


def documents(root):
    return [(path, yaml.safe_load((root / path).read_bytes())) for path in EXPECTED]


def cli(root, *paths):
    return subprocess.run(
        [sys.executable, "scripts/validate_gtdb_coherence.py", *(paths or EXPECTED)],
        cwd=root,
        text=True,
        capture_output=True,
        check=False,
    )


def test_actual_sources_preserve_both_groups_and_real_cli(actual):
    docs = documents(actual)
    assert len(check_corpus(docs)) == 4, "unpartitioned historical conflict must remain visible"
    groups = partition_corpus(docs, root=actual)
    assert len(groups[R232]) == 2
    assert {path for path, _ in groups[R232]} == set(EXPECTED) - {AMSTERDAM}
    assert sum(len(list(_blocks(doc))) for _, doc in docs) == sum(map(len, groups.values()))
    assert check_source_bound_corpus(docs, root=actual) == []
    sources = AkkermansiaSources(actual)
    observed = []
    for path, doc in docs:
        block = doc["taxonomy"][EXPECTED[path][1]]["taxon_term"]["gtdb_classification"]
        observed.append((sources.population(path, block), block["total_genomes"]))
    assert observed == [(DEFAULT, 4983), (R232, 1806), (R232, 1806)]
    result = cli(actual)
    assert result.returncode == 0, result.stdout + result.stderr
    assert "files checked: 3" in result.stderr
    assert "lineage conflicts: 0" in result.stderr


@pytest.mark.parametrize("path", list(PROOFS))
def test_changed_source_bytes_refuse_then_restore(actual, path):
    source = actual / path
    original = source.read_bytes()
    assert cli(actual).returncode == 0
    try:
        source.write_bytes(original + b" ")
        assert source.read_bytes() != original
        result = cli(actual)
        assert result.returncode == 1
        assert "source proof changed" in result.stdout
    finally:
        source.write_bytes(original)
    assert source.read_bytes() == original
    assert cli(actual).returncode == 0


@pytest.mark.parametrize(
    "field,value",
    [
        ("total_genomes", 4983),
        ("majority_fraction", 1.0),
        ("gtdb_lineage", "d__Bacteria;p__Verrucomicrobiota;c__Verrucomicrobiae"),
        ("ncbi_source_id", "NCBITaxon:1"),
        ("gtdb_id", "GTDB:s__Invented_species"),
        ("mapping_source", "invented R232 label"),
        ("curated", False),
    ],
)
def test_changed_actual_assertion_refuses_then_restores(actual, field, value):
    path = actual / MUC2
    original = path.read_bytes()
    assert cli(actual).returncode == 0
    try:
        doc = yaml.safe_load(original)
        block = doc["taxonomy"][13]["taxon_term"]["gtdb_classification"]
        block[field] = value
        path.write_text(yaml.safe_dump(doc))
        assert (
            yaml.safe_load(path.read_bytes())["taxonomy"][13]["taxon_term"]["gtdb_classification"][
                field
            ]
            == value
        )
        result = cli(actual)
        assert result.returncode == 1
        assert "source-bound assertion differs" in result.stdout
    finally:
        path.write_bytes(original)
    assert path.read_bytes() == original
    assert cli(actual).returncode == 0


@pytest.mark.parametrize("mutation", ["stock", "identity", "missing", "duplicate", "not_mapping"])
def test_known_record_structure_cannot_evade_binding(actual, mutation):
    docs = documents(actual)
    original = deepcopy(docs)
    doc = docs[1][1]
    if mutation == "stock":
        doc["taxonomy"][13]["strain_designation"]["strain_name"] = "ATCC BAA-835"
    elif mutation == "identity":
        doc["id"] = "CommunityMech:invented"
    elif mutation == "missing":
        doc["taxonomy"].pop(13)
    elif mutation == "duplicate":
        doc["taxonomy"].append(deepcopy(doc["taxonomy"][13]))
    else:
        docs[1] = (MUC2, None)
    assert docs != original
    assert "source provenance refused" in check_source_bound_corpus(docs, root=actual)[0]
    assert check_source_bound_corpus(original, root=actual) == []


@pytest.mark.parametrize("label", [Path(MUC2).name, "kb/communities/Copied.yaml"])
def test_basename_and_copied_path_refuse(actual, label):
    docs = documents(actual)
    docs[1] = (label, docs[1][1])
    assert "path differs" in check_source_bound_corpus(docs, root=actual)[0]
    # The actual CLI resolves a copied file to its full wrong relative path.
    target = actual / label
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(actual / MUC2, target)
    result = cli(actual, label)
    assert result.returncode == 1
    assert "path differs" in result.stdout
    assert cli(actual).returncode == 0


def test_unknown_source_label_cannot_authorize_copy(actual):
    docs = documents(actual)
    changed = deepcopy(docs[1][1])
    changed["id"] = "CommunityMech:unreviewed"
    changed["taxonomy"][13]["taxon_term"]["gtdb_classification"]["mapping_source"] = "R232"
    docs.append(("kb/communities/Unreviewed.yaml", changed))
    assert (
        "unknown Akkermansia source-bound path" in check_source_bound_corpus(docs, root=actual)[0]
    )
    assert check_source_bound_corpus(documents(actual), root=actual) == []


def test_each_partition_retains_the_same_source_hierarchy_guard(actual):
    groups = partition_corpus(documents(actual), root=actual)
    for rows in groups.values():
        assert check_corpus(rows) == []
        changed = deepcopy(rows[-1])
        block = changed[1]["taxonomy"][0]["taxon_term"]["gtdb_classification"]
        original_lineage = block["gtdb_lineage"]
        block["gtdb_lineage"] = original_lineage.replace("p__", "p__Invented_", 1)
        assert block["gtdb_lineage"] != original_lineage
        assert check_corpus([*rows, changed]), "same-source corruption must not be partitioned away"
        assert check_corpus(rows) == []


def test_unselected_block_conflict_stays_visible(actual):
    docs = documents(actual)
    changed = deepcopy(docs[0][1]["taxonomy"][1])
    changed["taxon_term"]["gtdb_classification"]["gtdb_lineage"] = changed["taxon_term"][
        "gtdb_classification"
    ]["gtdb_lineage"].replace("c__Bacteroidia", "c__Wrong")
    docs.append(("kb/communities/Other.yaml", {"taxonomy": [changed]}))
    result = check_source_bound_corpus(docs, root=actual)
    assert any("different lineages" in problem for problem in result)
    assert check_source_bound_corpus(documents(actual), root=actual) == []


def test_denominator_consumer_rejects_changed_supplied_blocks(actual, monkeypatch):
    import test_gtdb_support_counts as counts

    monkeypatch.setattr(counts, "REPO", actual)
    rows = []
    for path, doc in documents(actual):
        term = doc["taxonomy"][EXPECTED[path][1]]["taxon_term"]
        rows.append((path, term["preferred_term"], term["gtdb_classification"]))
    counts.test_every_kb_taxon_reports_one_denominator(rows)
    changed = deepcopy(rows)
    changed[1][2].update(ncbi_source_id="NCBITaxon:1", gtdb_id="GTDB:s__Fake", total_genomes=1)
    with pytest.raises(SourceProvenanceError, match="supplied block"):
        counts.test_every_kb_taxon_reports_one_denominator(changed)
    counts.test_every_kb_taxon_reports_one_denominator(rows)


def test_existing_blautia_guard_refuses_and_restores_without_route_escape(actual, monkeypatch):
    import test_gtdb_support_counts as counts

    monkeypatch.setattr(counts, "REPO", actual)
    path, doc = documents(actual)[2]
    blocks = list(_blocks(doc))
    original = next(block for _, block in blocks if block["ncbi_source_id"] == "NCBITaxon:53443")
    row = (path, "Blautia hydrogenotrophica", original)
    counts.test_every_kb_taxon_reports_one_denominator([row])
    changed = deepcopy(original)
    changed["total_genomes"] += 1
    assert changed != original
    with pytest.raises(AssertionError, match="pinned R232 assertion changed"):
        counts.test_every_kb_taxon_reports_one_denominator([(path, row[1], changed)])
    counts.test_every_kb_taxon_reports_one_denominator([row])

    # Adopting the Blautia ID must not let a changed Akkermansia block escape.
    akkermansia = next(
        block for _, block in blocks if block["ncbi_source_id"] == "NCBITaxon:239935"
    )
    altered = deepcopy(akkermansia)
    altered["ncbi_source_id"] = "NCBITaxon:53443"
    assert altered != akkermansia
    with pytest.raises(AssertionError, match="pinned R232 assertion changed"):
        counts.test_every_kb_taxon_reports_one_denominator([(path, "Akkermansia", altered)])
    counts.test_every_kb_taxon_reports_one_denominator([(path, "Akkermansia", akkermansia)])
