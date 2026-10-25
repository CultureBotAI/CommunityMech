"""Regression tests for Stage 6 infrastructure tasks (#2055, #2056, #2057)."""

from __future__ import annotations

import copy
import importlib.util
from pathlib import Path
from unittest.mock import patch

import yaml

from communitymech.paths import record_files

REPO = Path(__file__).parent.parent


def _load_script(script_name: str):
    path = REPO / "scripts" / script_name
    spec = importlib.util.spec_from_file_location(path.stem, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_infra_0001_downstream_edge_contract_and_decision_provenance():
    """#2055: every InteractionDownstream edge resolves to an in-record target and has evidence."""
    schema = yaml.safe_load((REPO / "src/communitymech/schema/communitymech.yaml").read_text())
    downstream_cls = schema["classes"]["InteractionDownstream"]
    assert "target" in downstream_cls["attributes"]
    assert "description" in downstream_cls["attributes"]

    edge_count = 0
    for path in record_files():
        doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        interactions = [
            i for i in (doc.get("ecological_interactions") or []) if isinstance(i, dict)
        ]
        names = {str(i.get("name") or "") for i in interactions if i.get("name")}
        for interaction in interactions:
            downstream_edges = [
                d for d in (interaction.get("downstream") or []) if isinstance(d, dict)
            ]
            if not downstream_edges:
                continue
            assert interaction.get("evidence"), (
                f"{path.name}: interaction {interaction.get('name')!r} has downstream edges "
                f"without primary EvidenceItem entries on the parent node"
            )
            for edge in downstream_edges:
                edge_count += 1
                target = str(edge.get("target") or "")
                assert target in names, (
                    f"{path.name}: downstream edge target {target!r} does not match any "
                    f"in-record EcologicalInteraction.name"
                )
    assert edge_count >= 100


def test_infra_0002_build_sequence_map_projects_commontaxon_genes(tmp_path: Path):
    """#2056: build_sequence_map loads both CommonTaxon.genes and legacy functional_genes."""
    bsm = _load_script("build_sequence_map.py")
    curated = bsm.load_curated_genes()
    by_acc = {g["accession"]: g for g in curated}

    expected_accessions = {
        "UniProtKB:Q74A86",
        "UniProtKB:Q749X9",
        "UniProtKB:Q74A90",
        "UniProtKB:Q74BW5",
        "UniProtKB:Q8EG35",
        "UniProtKB:Q8EG34",
        "UniProtKB:Q8EG33",
        "UniProtKB:Q8EG32",
        "UniProtKB:Q8E945",
    }
    assert expected_accessions == set(by_acc.keys())

    mtrc = by_acc["UniProtKB:Q8EG33"]
    assert mtrc["gene_symbol"] == "mtrC"
    assert mtrc["locus_tag"] == "SO_1778"
    assert "decaheme c-type cytochrome" in mtrc["function"]
    assert "Mtr extracellular electron transfer" in mtrc["phenotype"]
    assert "PMID:42733304" in mtrc["references"]
    assert mtrc["source_taxon_yaml"] == "kb/taxa/Shewanella_oneidensis_MR1.yaml"

    proteins = copy.deepcopy(bsm.REFERENCE_PROTEINS)
    bsm._enrich_from_taxa_yaml(proteins)
    enriched_by_acc = {p["accession"]: p for p in proteins}
    for acc in expected_accessions:
        entry = enriched_by_acc[acc]
        assert entry.get("function"), f"{acc} missing function after _enrich_from_taxa_yaml"
        assert entry.get("phenotype"), f"{acc} missing phenotype after _enrich_from_taxa_yaml"
        assert entry.get("references"), f"{acc} missing references after _enrich_from_taxa_yaml"
        assert entry.get("source_taxon_yaml", "").startswith("kb/taxa/")

    # Also verify legacy functional_genes compatibility
    legacy_yaml = tmp_path / "Legacy_Taxon.yaml"
    legacy_yaml.write_text(
        yaml.safe_dump(
            {
                "id": "CommunityMech:taxon:999999",
                "functional_genes": [
                    {
                        "gene_id": "UniProtKB:P07962",
                        "function": "Legacy McrA function",
                        "phenotype": "Legacy methanogenesis phenotype",
                        "evidence": [{"reference": "PMID:12345678"}],
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    legacy_loaded = bsm.load_curated_genes(taxa_dir=tmp_path)
    assert len(legacy_loaded) == 1
    assert legacy_loaded[0]["accession"] == "UniProtKB:P07962"
    assert legacy_loaded[0]["function"] == "Legacy McrA function"
    assert legacy_loaded[0]["phenotype"] == "Legacy methanogenesis phenotype"
    assert legacy_loaded[0]["references"] == ["PMID:12345678"]


def test_infra_0003_audit_completeness_and_seatbelt_safe_root():
    """#2057: scripts/audit_completeness.py computes 0-100 scores and handles Seatbelt."""
    ac = _load_script("audit_completeness.py")

    # Verify Seatbelt PermissionError fallback on Path.resolve
    with patch.object(Path, "resolve", side_effect=PermissionError("Seatbelt stat blocked")):
        fallback_root = ac._repo_root()
        assert fallback_root == REPO

    rows_default = ac.audit_corpus()
    assert len(rows_default) >= 477
    roots_seen = {r["record_path"].split("/")[0] for r in rows_default}
    assert roots_seen == {"kb", "data"}

    rows_with_taxa = ac.audit_corpus(include_taxa=True)
    assert len(rows_with_taxa) == len(rows_default) + 2
    taxa_rows = [r for r in rows_with_taxa if r["target_class"] == "CommonTaxon"]
    assert len(taxa_rows) == 2
    assert all(r["completeness_score"] == 100 for r in taxa_rows)

    summary = ac.summarize_corpus(rows_default)
    assert summary["total_records"] == len(rows_default)
    assert summary["required_fields_complete"] >= 330
    assert 60.0 <= summary["avg_completeness_score"] <= 100.0
    assert 0 <= summary["min_completeness_score"] <= summary["max_completeness_score"] <= 100

    # Verify calculate_validation_score matches metrics-and-reports.md
    assert (
        ac.calculate_validation_score(
            {"P1": 0, "P2": 1, "P3": 2, "avg_evidence": 2.0, "network_integrity": "COMPLETE"}
        )
        == 100.0
    )
    assert (
        ac.calculate_validation_score(
            {"P1": 1, "P2": 0, "P3": 0, "avg_evidence": 0.0, "network_integrity": "INCOMPLETE"}
        )
        == 50.0
    )


def test_infra_0004_corpus_count_decoupling_preserves_invariants():
    """#2063: decoupled test suites accept valid new records while catching invariant violations."""
    spec_pt = importlib.util.spec_from_file_location(
        "test_participating_taxa_infra0004",
        REPO / "tests" / "test_participating_taxa.py",
    )
    assert spec_pt is not None and spec_pt.loader is not None
    pt_mod = importlib.util.module_from_spec(spec_pt)
    spec_pt.loader.exec_module(pt_mod)

    valid_doc = {
        "taxonomy": [
            {
                "taxon_term": {
                    "preferred_term": "Escherichia coli K-12",
                    "term": {"id": "NCBITaxon:83333", "label": "Escherichia coli K-12"},
                }
            }
        ],
        "ecological_interactions": [
            {
                "name": "Community acetate production",
                "scope": "COMMUNITY_LEVEL",
                "participating_taxa": [
                    {
                        "preferred_term": "Escherichia coli K-12",
                        "term": {"id": "NCBITaxon:83333", "label": "Escherichia coli K-12"},
                    }
                ],
            }
        ],
    }
    assert pt_mod._is_legitimate_participating_taxa_user(valid_doc) is True

    pairwise_doc = copy.deepcopy(valid_doc)
    pairwise_doc["ecological_interactions"][0]["scope"] = "PAIRWISE"
    assert pt_mod._is_legitimate_participating_taxa_user(pairwise_doc) is False

    dangling_doc = copy.deepcopy(valid_doc)
    dangling_doc["ecological_interactions"][0]["participating_taxa"] = [
        {"preferred_term": "Nonexistent taxon", "term": {"id": "NCBITaxon:9999999"}}
    ]
    assert pt_mod._is_legitimate_participating_taxa_user(dangling_doc) is False
    assert pt_mod.BASELINE_USERS <= pt_mod.USERS

    spec_ir = importlib.util.spec_from_file_location(
        "test_is_reclassified_infra0004",
        REPO / "tests" / "test_is_reclassified_semantics.py",
    )
    assert spec_ir is not None and spec_ir.loader is not None
    ir_mod = importlib.util.module_from_spec(spec_ir)
    spec_ir.loader.exec_module(ir_mod)

    base_blocks = list(ir_mod._blocks())
    with patch.object(
        ir_mod,
        "_blocks",
        side_effect=lambda: iter(
            [*base_blocks, ("Agrobacterium deltae", "Agrobacterium leguminum", "GTDB:s__0001")]
        ),
    ):
        ir_mod.test_the_flag_is_set_on_the_expected_number_of_blocks()
        ir_mod.test_the_buckets_partition_the_whole_set()
        for bucket in sorted(ir_mod.EXPECTED):
            ir_mod.test_each_bucket_holds_what_it_held(bucket)
        ir_mod.test_the_majority_of_true_values_are_not_reclassifications()
        ir_mod.test_the_flag_is_not_confined_to_species_rank()

    with patch.object(
        ir_mod,
        "_blocks",
        side_effect=lambda: iter(
            [*base_blocks, ("Escherichia coli K-12", "Escherichia coli", "GTDB:s__0002")]
        ),
    ):
        try:
            ir_mod.test_each_bucket_holds_what_it_held("strain_dropped")
        except AssertionError:
            pass
        else:
            raise AssertionError("strain_dropped regression was not caught")

