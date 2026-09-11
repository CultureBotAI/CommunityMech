"""Rank community records by causal-graph readiness.

The causal graph is encoded in ``ecological_interactions``: each interaction is a
node, and each ``downstream`` item names a directed edge to another interaction
node. This script gives curators a deterministic worst-first ordering so causal
graph review starts with records that have the least curated graph structure.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Any, TextIO

import yaml
from yaml import SafeLoader

try:
    from yaml import CSafeLoader
except ImportError:  # pragma: no cover - depends on the installed PyYAML build
    CSafeLoader = SafeLoader

from communitymech.paths import REPO_ROOT, record_files

TARGET_INTERACTIONS = 3
TARGET_DOWNSTREAM_EDGES = 2

TSV_FIELDS = [
    "rank",
    "score",
    "path",
    "id",
    "name",
    "taxonomy",
    "connected_taxa",
    "disconnected_taxa",
    "ecological_interactions",
    "downstream_edges",
    "interaction_evidence",
    "missing",
    "dangling_downstream",
    "self_downstream",
]


def _as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _as_mapping(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def _has_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _has_grounded_term(value: Any) -> bool:
    if not isinstance(value, dict):
        return False
    term = value.get("term")
    return isinstance(term, dict) and _has_text(term.get("id")) and _has_text(term.get("label"))


def _has_grounded_item(items: Any) -> bool:
    return any(_has_grounded_term(item) for item in _as_list(items))


def _fraction(count: int, total: int) -> float:
    return count / total if total else 0.0


def _fraction_or_full(count: int, total: int) -> float:
    return count / total if total else 1.0


def _score_cap(count: int, target: int, weight: float) -> float:
    return min(count / target, 1.0) * weight


def display_path(path: Path) -> str:
    """Return a stable repo-relative path when possible."""
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _taxon_tokens(taxon: dict[str, Any]) -> set[str]:
    tokens = set()
    if _has_text(taxon.get("preferred_term")):
        tokens.add(taxon["preferred_term"])
    term = _as_mapping(taxon.get("term"))
    for key in ("id", "label"):
        if _has_text(term.get(key)):
            tokens.add(term[key])
    return tokens


def _taxonomy_lookup(taxonomy: list[dict[str, Any]]) -> dict[str, set[str]]:
    lookup: dict[str, set[str]] = {}
    for entry in taxonomy:
        taxon = _as_mapping(entry.get("taxon_term"))
        term = _as_mapping(taxon.get("term"))
        key = taxon.get("preferred_term") or term.get("label") or term.get("id")
        if not _has_text(key):
            continue
        for token in _taxon_tokens(taxon):
            lookup.setdefault(token, set()).add(key)
    return lookup


def _connected_taxa(
    interactions: list[dict[str, Any]], taxonomy: list[dict[str, Any]]
) -> set[str]:
    lookup = _taxonomy_lookup(taxonomy)
    all_taxa = {taxon for taxa in lookup.values() for taxon in taxa}
    connected = set()

    for interaction in interactions:
        if interaction.get("scope") == "COMMUNITY_LEVEL":
            participants = _as_list(interaction.get("participating_taxa"))
            if participants:
                for participant in participants:
                    for token in _taxon_tokens(_as_mapping(participant)):
                        connected.update(lookup.get(token, set()))
            else:
                connected.update(all_taxa)

        for slot in ("source_taxon", "target_taxon"):
            for token in _taxon_tokens(_as_mapping(interaction.get(slot))):
                connected.update(lookup.get(token, set()))

    return connected


def score_document(document: dict[str, Any]) -> dict[str, Any]:
    """Score one MicrobialCommunity mapping for causal-graph readiness."""
    raw_interactions = _as_list(document.get("ecological_interactions"))
    interactions = [_as_mapping(item) for item in raw_interactions if isinstance(item, dict)]
    interaction_count = len(interactions)
    taxonomy = [
        _as_mapping(item) for item in _as_list(document.get("taxonomy")) if isinstance(item, dict)
    ]
    connected_taxa = _connected_taxa(interactions, taxonomy)
    taxonomy_count = len(taxonomy)
    disconnected_taxa = max(0, taxonomy_count - len(connected_taxa))

    missing = []
    if taxonomy_count == 0:
        missing.append("taxonomy")

    if interaction_count == 0:
        return {
            "id": document.get("id", ""),
            "name": document.get("name", ""),
            "score": 0.0,
            "taxonomy": taxonomy_count,
            "connected_taxa": len(connected_taxa),
            "disconnected_taxa": disconnected_taxa,
            "ecological_interactions": 0,
            "downstream_edges": 0,
            "interaction_evidence": 0,
            "dangling_downstream": 0,
            "self_downstream": 0,
            "missing": [*missing, "ecological_interactions"],
        }

    interaction_names = {
        interaction.get("name") for interaction in interactions if _has_text(interaction.get("name"))
    }
    downstream_edges = []
    self_edges = []
    for interaction in interactions:
        interaction_name = interaction.get("name")
        for edge in _as_list(interaction.get("downstream")):
            if not isinstance(edge, dict):
                continue
            edge = _as_mapping(edge)
            downstream_edges.append(edge)
            if _has_text(interaction_name) and edge.get("target") == interaction_name:
                self_edges.append(edge)

    dangling_edges = [
        edge for edge in downstream_edges if edge.get("target") not in interaction_names
    ]

    with_descriptions = sum(1 for item in interactions if _has_text(item.get("description")))
    with_evidence = sum(1 for item in interactions if _as_list(item.get("evidence")))
    with_type = sum(1 for item in interactions if _has_text(item.get("interaction_type")))
    with_scope = sum(1 for item in interactions if _has_text(item.get("scope")))
    requires_interaction_types = taxonomy_count != 1
    pairwise = [item for item in interactions if item.get("scope", "PAIRWISE") == "PAIRWISE"]
    pairwise_with_source = sum(1 for item in pairwise if item.get("source_taxon"))
    with_mediators = sum(
        1
        for item in interactions
        if _has_grounded_item(item.get("metabolites"))
        or _has_grounded_item(item.get("biological_processes"))
    )
    described_edges = sum(1 for edge in downstream_edges if _has_text(edge.get("description")))

    score = (
        _score_cap(interaction_count, TARGET_INTERACTIONS, 15)
        + _score_cap(len(downstream_edges), TARGET_DOWNSTREAM_EDGES, 20)
        + _fraction(with_descriptions, interaction_count) * 10
        + _fraction(with_evidence, interaction_count) * 20
        + (
            _fraction(with_type, interaction_count)
            if requires_interaction_types
            else 1.0
        )
        * 10
        + _fraction(with_scope, interaction_count) * 5
        + _fraction_or_full(pairwise_with_source, len(pairwise)) * 5
        + _fraction(len(connected_taxa), taxonomy_count) * 5
        + _fraction(with_mediators, interaction_count) * 5
        + _fraction(described_edges, len(downstream_edges)) * 5
    )

    score = min(score, 100.0)
    if dangling_edges:
        score = max(0.0, score - 10 * len(dangling_edges))
    if self_edges:
        score = max(0.0, score - 10 * len(self_edges))

    if interaction_count < TARGET_INTERACTIONS:
        missing.append("additional_interactions")
    if len(downstream_edges) == 0:
        missing.append("downstream")
    elif len(downstream_edges) < TARGET_DOWNSTREAM_EDGES:
        missing.append("additional_downstream")
    if with_evidence < interaction_count:
        missing.append("interaction_evidence")
    if with_mediators < interaction_count:
        missing.append("metabolites_or_biological_processes")
    if with_descriptions < interaction_count:
        missing.append("interaction_description")
    if requires_interaction_types and with_type < interaction_count:
        missing.append("interaction_type")
    if with_scope < interaction_count:
        missing.append("scope")
    if pairwise_with_source < len(pairwise):
        missing.append("pairwise_source_taxon")
    if disconnected_taxa:
        missing.append("disconnected_taxa")
    if described_edges < len(downstream_edges):
        missing.append("downstream_description")
    if dangling_edges:
        missing.append("dangling_downstream")
    if self_edges:
        missing.append("self_downstream")

    return {
        "id": document.get("id", ""),
        "name": document.get("name", ""),
        "score": round(score, 1),
        "taxonomy": taxonomy_count,
        "connected_taxa": len(connected_taxa),
        "disconnected_taxa": disconnected_taxa,
        "ecological_interactions": interaction_count,
        "downstream_edges": len(downstream_edges),
        "interaction_evidence": sum(len(_as_list(item.get("evidence"))) for item in interactions),
        "dangling_downstream": len(dangling_edges),
        "self_downstream": len(self_edges),
        "missing": missing,
    }


def score_path(path: Path) -> dict[str, Any]:
    try:
        document = yaml.load(
            path.read_text(encoding="utf-8"), Loader=CSafeLoader  # noqa: S506
        ) or {}
    except (OSError, yaml.YAMLError) as exc:
        return {
            "path": display_path(path),
            "id": "",
            "name": "",
            "score": 0.0,
            "taxonomy": 0,
            "connected_taxa": 0,
            "disconnected_taxa": 0,
            "ecological_interactions": 0,
            "downstream_edges": 0,
            "interaction_evidence": 0,
            "dangling_downstream": 0,
            "self_downstream": 0,
            "missing": [f"unreadable:{type(exc).__name__}"],
        }

    score = score_document(document if isinstance(document, dict) else {})
    score["path"] = display_path(path)
    return score


def rank_paths(paths: list[Path]) -> list[dict[str, Any]]:
    """Score paths and return them in deterministic worst-first order."""
    return sorted((score_path(path) for path in paths), key=lambda row: (row["score"], row["path"]))


def ranked_rows(paths: list[Path], limit: int | None = None) -> list[dict[str, Any]]:
    rows = rank_paths(paths)
    if limit is not None:
        rows = rows[:limit]
    return [{"rank": rank, **row} for rank, row in enumerate(rows, start=1)]


def write_json(rows: list[dict[str, Any]], output: TextIO) -> None:
    json.dump(rows, output, indent=2)
    output.write("\n")


def write_tsv(rows: list[dict[str, Any]], output: TextIO) -> None:
    writer = csv.DictWriter(output, TSV_FIELDS, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    for row in rows:
        formatted = dict(row)
        formatted["missing"] = ",".join(formatted["missing"])
        writer.writerow(formatted)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        help="Specific record YAML files to score. Defaults to every MicrobialCommunity record.",
    )
    parser.add_argument(
        "--format",
        choices=("tsv", "json"),
        default="tsv",
        help="Output format.",
    )
    parser.add_argument("--limit", type=int, help="Limit output to the N lowest-scoring records.")
    args = parser.parse_args(argv)

    paths = args.paths or record_files()
    rows = ranked_rows(paths, args.limit)
    if args.format == "json":
        write_json(rows, sys.stdout)
    else:
        write_tsv(rows, sys.stdout)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
