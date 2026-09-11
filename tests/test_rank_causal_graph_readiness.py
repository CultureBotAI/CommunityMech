from __future__ import annotations

import importlib.util
import io
import json
from pathlib import Path

REPO = Path(__file__).parent.parent
SCRIPT = REPO / "scripts" / "rank_causal_graph_readiness.py"


spec = importlib.util.spec_from_file_location("rank_causal_graph_readiness", SCRIPT)
ranker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ranker)


def _taxon(name: str, curie: str = "NCBITaxon:1", label: str | None = None) -> dict:
    return {
        "taxon_term": {
            "preferred_term": name,
            "term": {"id": curie, "label": label or name},
        }
    }


def _participant(name: str, curie: str = "NCBITaxon:1", label: str | None = None) -> dict:
    return {
        "preferred_term": name,
        "term": {"id": curie, "label": label or name},
    }


def _interaction(name: str, downstream: list[dict] | None = None) -> dict:
    return {
        "name": name,
        "description": f"{name} description",
        "interaction_type": "CROSS_FEEDING",
        "scope": "PAIRWISE",
        "source_taxon": _participant("source", "NCBITaxon:1"),
        "target_taxon": _participant("target", "NCBITaxon:2"),
        "metabolites": [_participant("acetate", "CHEBI:30089")],
        "evidence": [{"reference": "PMID:1", "snippet": "evidence"}],
        "downstream": downstream or [],
    }


def test_empty_record_scores_zero():
    score = ranker.score_document({"id": "empty", "taxonomy": [_taxon("source")]})

    assert score["score"] == 0.0
    assert score["ecological_interactions"] == 0
    assert score["missing"] == ["ecological_interactions"]


def test_downstream_edges_raise_readiness():
    document = {
        "taxonomy": [
            _taxon("source", "NCBITaxon:1"),
            _taxon("target", "NCBITaxon:2"),
        ],
        "ecological_interactions": [
            _interaction(
                "first",
                downstream=[
                    {
                        "target": "second",
                        "description": "first drives second",
                    }
                ],
            ),
            _interaction("second"),
        ],
    }
    without_downstream = {
        **document,
        "ecological_interactions": [_interaction("first"), _interaction("second")],
    }

    assert (
        ranker.score_document(document)["score"]
        > ranker.score_document(without_downstream)["score"]
    )
    assert "downstream" not in ranker.score_document(document)["missing"]


def test_below_target_counts_are_reported():
    document = {
        "ecological_interactions": [
            _interaction(
                "first",
                downstream=[
                    {
                        "target": "second",
                        "description": "first drives second",
                    }
                ],
            ),
            _interaction("second"),
        ],
    }

    score = ranker.score_document(document)

    assert "additional_interactions" in score["missing"]
    assert "additional_downstream" in score["missing"]
    assert "downstream" not in score["missing"]


def test_missing_taxonomy_is_reported_without_other_slot_gaps():
    score = ranker.score_document(
        {
            "ecological_interactions": [
                _interaction(
                    "first",
                    downstream=[
                        {
                            "target": "second",
                            "description": "first drives second",
                        }
                    ],
                ),
                _interaction(
                    "second",
                    downstream=[
                        {
                            "target": "third",
                            "description": "second drives third",
                        }
                    ],
                ),
                _interaction("third"),
            ],
        }
    )

    assert score["score"] == 95.0
    assert score["missing"] == ["taxonomy"]


def test_dangling_downstream_edges_are_reported_and_penalized():
    clean = {
        "ecological_interactions": [
            _interaction(
                "first",
                downstream=[
                    {
                        "target": "second",
                        "description": "first drives second",
                    }
                ],
            ),
            _interaction("second"),
        ],
    }
    dangling = {
        "ecological_interactions": [
            _interaction(
                "first",
                downstream=[
                    {
                        "target": "missing",
                        "description": "this edge has no node",
                    }
                ],
            ),
            _interaction("second"),
        ],
    }

    score = ranker.score_document(dangling)
    assert score["dangling_downstream"] == 1
    assert score["score"] == ranker.score_document(clean)["score"] - 10
    assert "dangling_downstream" in score["missing"]


def test_self_downstream_edges_are_reported_and_penalized():
    clean = {
        "ecological_interactions": [
            _interaction(
                "first",
                downstream=[
                    {
                        "target": "second",
                        "description": "first drives second",
                    }
                ],
            ),
            _interaction(
                "second",
                downstream=[
                    {
                        "target": "third",
                        "description": "second drives third",
                    }
                ],
            ),
            _interaction("third"),
        ],
    }
    self_loop = {
        "ecological_interactions": [
            _interaction(
                "first",
                downstream=[
                    {
                        "target": "first",
                        "description": "first drives itself",
                    }
                ],
            ),
            _interaction(
                "second",
                downstream=[
                    {
                        "target": "third",
                        "description": "second drives third",
                    }
                ],
            ),
            _interaction("third"),
        ],
    }

    score = ranker.score_document(self_loop)
    assert score["self_downstream"] == 1
    assert score["score"] == ranker.score_document(clean)["score"] - 10
    assert "self_downstream" in score["missing"]


def test_pairwise_source_and_target_taxa_are_counted_as_connected():
    score = ranker.score_document(
        {
            "taxonomy": [
                _taxon("source", "NCBITaxon:1"),
                _taxon("target", "NCBITaxon:2"),
                _taxon("absent", "NCBITaxon:3"),
            ],
            "ecological_interactions": [_interaction("first")],
        }
    )

    assert score["connected_taxa"] == 2
    assert score["disconnected_taxa"] == 1
    assert "disconnected_taxa" in score["missing"]


def test_pairwise_preferred_term_beats_shared_taxon_id():
    score = ranker.score_document(
        {
            "taxonomy": [
                _taxon("strain A", "NCBITaxon:1", "Variovorax"),
                _taxon("strain B", "NCBITaxon:1", "Variovorax"),
            ],
            "ecological_interactions": [
                {
                    "name": "specific strain edge",
                    "scope": "PAIRWISE",
                    "source_taxon": _participant("strain A", "NCBITaxon:1", "Variovorax"),
                }
            ],
        }
    )

    assert score["connected_taxa"] == 1
    assert score["disconnected_taxa"] == 1


def test_pairwise_id_fallback_only_credits_unique_taxon_ids():
    score = ranker.score_document(
        {
            "taxonomy": [
                _taxon("strain A", "NCBITaxon:1", "Variovorax"),
                _taxon("strain B", "NCBITaxon:1", "Variovorax"),
                _taxon("unique", "NCBITaxon:2", "Unique"),
            ],
            "ecological_interactions": [
                {
                    "name": "ambiguous shared id",
                    "scope": "PAIRWISE",
                    "source_taxon": {"term": {"id": "NCBITaxon:1", "label": "paper shorthand"}},
                },
                {
                    "name": "unique id fallback",
                    "scope": "PAIRWISE",
                    "source_taxon": {"term": {"id": "NCBITaxon:2", "label": "paper shorthand"}},
                },
            ],
        }
    )

    assert score["connected_taxa"] == 1
    assert score["disconnected_taxa"] == 2


def test_community_level_participating_taxa_narrows_connectivity():
    score = ranker.score_document(
        {
            "taxonomy": [
                _taxon("included", "NCBITaxon:1"),
                _taxon("excluded", "NCBITaxon:2"),
            ],
            "ecological_interactions": [
                {
                    "name": "community",
                    "description": "community description",
                    "interaction_type": "CROSS_FEEDING",
                    "scope": "COMMUNITY_LEVEL",
                    "participating_taxa": [_participant("included", "NCBITaxon:1")],
                    "metabolites": [_participant("acetate", "CHEBI:30089")],
                    "evidence": [{"reference": "PMID:1", "snippet": "evidence"}],
                }
            ],
        }
    )

    assert score["connected_taxa"] == 1
    assert score["disconnected_taxa"] == 1


def test_community_level_participating_taxa_prefer_names_to_shared_ids():
    score = ranker.score_document(
        {
            "taxonomy": [
                _taxon("included", "NCBITaxon:1", "Variovorax"),
                _taxon("excluded", "NCBITaxon:1", "Variovorax"),
            ],
            "ecological_interactions": [
                {
                    "name": "community",
                    "description": "community description",
                    "interaction_type": "CROSS_FEEDING",
                    "scope": "COMMUNITY_LEVEL",
                    "participating_taxa": [_participant("included", "NCBITaxon:1", "Variovorax")],
                    "metabolites": [_participant("acetate", "CHEBI:30089")],
                    "evidence": [{"reference": "PMID:1", "snippet": "evidence"}],
                }
            ],
        }
    )

    assert score["connected_taxa"] == 1
    assert score["disconnected_taxa"] == 1


def test_community_level_only_graph_gets_pairwise_source_credit():
    score = ranker.score_document(
        {
            "ecological_interactions": [
                {
                    "name": "community",
                    "description": "community description",
                    "interaction_type": "CROSS_FEEDING",
                    "scope": "COMMUNITY_LEVEL",
                    "metabolites": [_participant("acetate", "CHEBI:30089")],
                    "evidence": [{"reference": "PMID:1", "snippet": "evidence"}],
                }
            ],
        }
    )

    assert "pairwise_source_taxon" not in score["missing"]


def test_single_taxon_graphs_do_not_require_interaction_type():
    document = {
        "taxonomy": [_taxon("source", "NCBITaxon:1")],
        "ecological_interactions": [
            {
                "name": "first",
                "description": "first description",
                "scope": "COMMUNITY_LEVEL",
                "participating_taxa": [_participant("source", "NCBITaxon:1")],
                "metabolites": [_participant("acetate", "CHEBI:30089")],
                "evidence": [{"reference": "PMID:1", "snippet": "evidence"}],
                "downstream": [{"target": "second", "description": "first drives second"}],
            },
            {
                "name": "second",
                "description": "second description",
                "scope": "COMMUNITY_LEVEL",
                "participating_taxa": [_participant("source", "NCBITaxon:1")],
                "metabolites": [_participant("lactate", "CHEBI:24996")],
                "evidence": [{"reference": "PMID:1", "snippet": "evidence"}],
                "downstream": [{"target": "third", "description": "second drives third"}],
            },
            {
                "name": "third",
                "description": "third description",
                "scope": "COMMUNITY_LEVEL",
                "participating_taxa": [_participant("source", "NCBITaxon:1")],
                "metabolites": [_participant("succinate", "CHEBI:30031")],
                "evidence": [{"reference": "PMID:1", "snippet": "evidence"}],
            },
        ],
    }

    score = ranker.score_document(document)

    assert score["score"] == 100.0
    assert "interaction_type" not in score["missing"]


def test_rank_paths_orders_worst_first(tmp_path):
    empty = tmp_path / "empty.yaml"
    empty.write_text("id: empty\n", encoding="utf-8")
    complete = tmp_path / "complete.yaml"
    complete.write_text(
        """
id: complete
ecological_interactions:
- name: first
  description: first
  interaction_type: CROSS_FEEDING
  scope: PAIRWISE
  source_taxon:
    preferred_term: source
    term:
      id: NCBITaxon:1
      label: source
  metabolites:
  - preferred_term: acetate
    term:
      id: CHEBI:30089
      label: acetate
  evidence:
  - reference: PMID:1
    snippet: evidence
  downstream:
  - target: second
    description: first drives second
- name: second
  description: second
  interaction_type: CROSS_FEEDING
  scope: COMMUNITY_LEVEL
  metabolites:
  - preferred_term: acetate
    term:
      id: CHEBI:30089
      label: acetate
  evidence:
  - reference: PMID:1
    snippet: evidence
""",
        encoding="utf-8",
    )

    assert ranker.rank_paths([complete, empty])[0]["path"] == str(empty)


def test_json_preserves_missing_as_a_list():
    output = io.StringIO()
    ranker.write_json(
        [
            {
                "rank": 1,
                "score": 0.0,
                "path": "record.yaml",
                "missing": ["ecological_interactions", "downstream"],
            }
        ],
        output,
    )

    assert json.loads(output.getvalue())[0]["missing"] == [
        "ecological_interactions",
        "downstream",
    ]


def test_tsv_flattens_missing_as_a_comma_separated_field():
    output = io.StringIO()
    ranker.write_tsv(
        [
            {
                "rank": 1,
                "score": 0.0,
                "path": "record.yaml",
                "id": "CommunityMech:1",
                "name": "Record",
                "taxonomy": 0,
                "connected_taxa": 0,
                "disconnected_taxa": 0,
                "ecological_interactions": 0,
                "downstream_edges": 0,
                "interaction_evidence": 0,
                "missing": ["ecological_interactions", "downstream"],
                "dangling_downstream": 0,
                "self_downstream": 0,
            }
        ],
        output,
    )

    lines = output.getvalue().splitlines()
    assert lines[0].split("\t") == ranker.TSV_FIELDS
    assert "ecological_interactions,downstream" in lines[1]
