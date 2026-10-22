#!/usr/bin/env python3
"""Audit completeness and field presence across CommunityMech YAML records.

Implements the proportional 0-100 ``calculate_completeness`` and
``calculate_validation_score`` metrics specified in
``.claude/skills/review-communities/reference/metrics-and-reports.md`` alongside
binary field-presence diagnostics across ``kb/communities/*.yaml``,
``data/isolates/*.yaml``, and optionally ``kb/taxa/*.yaml``.

Uses a Seatbelt-safe ``_repo_root()`` helper that falls back to
``Path(__file__).absolute()`` if parent-directory ``stat`` calls in
``Path.resolve()`` raise ``PermissionError`` inside restricted sandboxes.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Any

import yaml


def _repo_root() -> Path:
    """Resolve repository root safely under macOS Seatbelt sandboxes."""
    try:
        return Path(__file__).resolve().parent.parent
    except PermissionError:
        return Path(__file__).absolute().parent.parent


REPO_ROOT = _repo_root()


def all_required_fields_present(community_data: dict[str, Any]) -> bool:
    """Return True if all required MicrobialCommunity fields are populated."""
    if not isinstance(community_data, dict):
        return False
    for key in ("id", "name", "description", "ecological_state", "community_category"):
        if not str(community_data.get(key) or "").strip():
            return False
    taxonomy = [t for t in (community_data.get("taxonomy") or []) if isinstance(t, dict)]
    if not taxonomy:
        return False
    return all(bool(t.get("functional_role")) for t in taxonomy)


def calculate_completeness(community_data: dict[str, Any]) -> int:
    """Calculate proportional completeness score (0-100) for a community record.

    Matches `.claude/skills/review-communities/reference/metrics-and-reports.md`:
    - Required fields (50 points): id, name, description, taxonomy with roles,
      ecological_state, community_category
    - Recommended fields (30 points):
      - environment_term (+5)
      - environmental_factors >= 3 (+10)
      - ecological_interactions >= 3 (+10)
      - external_resources >= 1 (+5)
    - Enrichment fields (20 points):
      - growth_media (+10)
      - associated_datasets (+5)
      - metabolites in ecological_interactions (+5)
    """
    if not isinstance(community_data, dict):
        return 0

    # Support CommonTaxon records when --include-taxa is enabled
    if "taxon_term" in community_data and "taxonomy" not in community_data:
        score = 0
        if community_data.get("id") and community_data.get("taxon_term"):
            score += 50
        genes = [g for g in (community_data.get("genes") or []) if isinstance(g, dict)]
        if genes:
            score += 30
        if any(g.get("evidence") for g in genes):
            score += 10
        if community_data.get("genomes"):
            score += 10
        return min(100, score)

    score = 0
    if all_required_fields_present(community_data):
        score += 50

    if community_data.get("environment_term"):
        score += 5
    if len(community_data.get("environmental_factors") or []) >= 3:
        score += 10
    interactions = [
        i for i in (community_data.get("ecological_interactions") or []) if isinstance(i, dict)
    ]
    if len(interactions) >= 3:
        score += 10
    if community_data.get("external_resources"):
        score += 5

    if community_data.get("growth_media"):
        score += 10
    if community_data.get("associated_datasets"):
        score += 5
    if any(bool(i.get("metabolites")) for i in interactions):
        score += 5

    return min(100, score)


def calculate_validation_score(validation_summary: dict[str, Any]) -> float:
    """Calculate validation quality score (0-100) from P1/P2/P3 issue counts."""
    base_score = 100.0
    base_score -= float(validation_summary.get("P1", 0)) * 50.0
    base_score -= float(validation_summary.get("P2", 0)) * 10.0
    base_score -= float(validation_summary.get("P3", 0)) * 2.0

    avg_evidence = float(validation_summary.get("avg_evidence", 0.0))
    base_score += min(avg_evidence / 2.0, 1.0) * 20.0

    if validation_summary.get("network_integrity") == "COMPLETE":
        base_score += 15.0

    return max(0.0, min(100.0, base_score))


def audit_record(record_path: Path, repo_root: Path | None = None) -> dict[str, Any]:
    """Compute binary field-presence flags, counts, and completeness_score for one record."""
    root = repo_root or _repo_root()
    doc = yaml.safe_load(record_path.read_text(encoding="utf-8")) or {}
    try:
        rel_path = record_path.relative_to(root).as_posix()
    except ValueError:
        rel_path = record_path.as_posix()

    if "taxon_term" in doc and "taxonomy" not in doc:
        taxon_term = doc.get("taxon_term") or {}
        genes = [g for g in (doc.get("genes") or []) if isinstance(g, dict)]
        return {
            "record_path": rel_path,
            "id": str(doc.get("id") or ""),
            "name": str(taxon_term.get("preferred_term") or record_path.stem),
            "target_class": "CommonTaxon",
            "community_category": "TAXON",
            "ecological_state": "NA",
            "num_taxa": 1,
            "num_interactions": 0,
            "num_env_factors": 0,
            "num_growth_media": 0,
            "num_genes": len(genes),
            "has_required_fields": bool(doc.get("id") and doc.get("taxon_term")),
            "has_environment_term": False,
            "has_growth_media": False,
            "has_external_resources": False,
            "has_associated_datasets": False,
            "has_interaction_metabolites": False,
            "completeness_score": calculate_completeness(doc),
        }

    taxonomy = [t for t in (doc.get("taxonomy") or []) if isinstance(t, dict)]
    interactions = [i for i in (doc.get("ecological_interactions") or []) if isinstance(i, dict)]
    env_factors = doc.get("environmental_factors") or []
    growth_media = doc.get("growth_media") or []

    return {
        "record_path": rel_path,
        "id": str(doc.get("id") or ""),
        "name": str(doc.get("name") or record_path.stem),
        "target_class": "MicrobialCommunity",
        "community_category": str(doc.get("community_category") or ""),
        "ecological_state": str(doc.get("ecological_state") or ""),
        "num_taxa": len(taxonomy),
        "num_interactions": len(interactions),
        "num_env_factors": len(env_factors),
        "num_growth_media": len(growth_media),
        "num_genes": 0,
        "has_required_fields": all_required_fields_present(doc),
        "has_environment_term": bool(doc.get("environment_term")),
        "has_growth_media": bool(growth_media),
        "has_external_resources": bool(doc.get("external_resources")),
        "has_associated_datasets": bool(doc.get("associated_datasets")),
        "has_interaction_metabolites": any(bool(i.get("metabolites")) for i in interactions),
        "completeness_score": calculate_completeness(doc),
    }


def audit_corpus(
    repo_root: Path | None = None,
    *,
    include_isolates: bool = True,
    include_taxa: bool = False,
) -> list[dict[str, Any]]:
    """Audit all records across configured roots and return sorted per-record dicts."""
    root = repo_root or _repo_root()
    roots = [root / "kb" / "communities"]
    if include_isolates:
        roots.append(root / "data" / "isolates")
    if include_taxa:
        roots.append(root / "kb" / "taxa")

    records: list[dict[str, Any]] = []
    for directory in roots:
        if not directory.exists():
            continue
        for record_path in sorted(directory.glob("*.yaml")):
            records.append(audit_record(record_path, repo_root=root))
    return records


def summarize_corpus(rows: list[dict[str, Any]]) -> dict[str, Any]:
    """Aggregate corpus-level completeness statistics."""
    total = len(rows)
    if total == 0:
        return {
            "total_records": 0,
            "avg_completeness_score": 0.0,
            "min_completeness_score": 0,
            "max_completeness_score": 0,
            "required_fields_complete": 0,
        }
    scores = [int(r["completeness_score"]) for r in rows]
    req_ok = sum(1 for r in rows if r["has_required_fields"])
    return {
        "total_records": total,
        "avg_completeness_score": round(sum(scores) / total, 2),
        "min_completeness_score": min(scores),
        "max_completeness_score": max(scores),
        "required_fields_complete": req_ok,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--format",
        choices=("summary", "tsv", "json"),
        default="summary",
        help="Output format (default: summary)",
    )
    parser.add_argument(
        "--communities-only",
        action="store_true",
        help="Only scan kb/communities/*.yaml (exclude data/isolates/*.yaml)",
    )
    parser.add_argument(
        "--include-taxa",
        action="store_true",
        help="Also scan kb/taxa/*.yaml reusable CommonTaxon records",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Optional output file path (default: stdout)",
    )
    args = parser.parse_args(argv)

    rows = audit_corpus(
        include_isolates=not args.communities_only,
        include_taxa=args.include_taxa,
    )
    summary = summarize_corpus(rows)

    if args.format == "json":
        payload = json.dumps({"summary": summary, "records": rows}, indent=2) + "\n"
    elif args.format == "tsv":
        fields = [
            "record_path",
            "id",
            "name",
            "target_class",
            "community_category",
            "ecological_state",
            "num_taxa",
            "num_interactions",
            "num_env_factors",
            "num_growth_media",
            "num_genes",
            "has_required_fields",
            "has_environment_term",
            "has_growth_media",
            "has_external_resources",
            "has_associated_datasets",
            "has_interaction_metabolites",
            "completeness_score",
        ]
        lines = ["\t".join(fields)]
        for row in rows:
            lines.append("\t".join(str(row[f]) for f in fields))
        payload = "\n".join(lines) + "\n"
    else:
        payload = (
            f"CommunityMech Completeness Audit\n"
            f"  Total records audited:      {summary['total_records']}\n"
            f"  Required fields complete:   {summary['required_fields_complete']}/{summary['total_records']}\n"
            f"  Average completeness score: {summary['avg_completeness_score']}/100\n"
            f"  Score range:                {summary['min_completeness_score']}..{summary['max_completeness_score']}\n"
        )

    if args.out is not None:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        with args.out.open("w", encoding="utf-8", newline="") as out_fh:
            out_fh.write(payload)
    else:
        sys.stdout.write(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
