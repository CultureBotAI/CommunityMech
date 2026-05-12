"""Lightweight KGX TSV validator — no external dependencies.

Verifies the TSV files emitted by `kgx_export.py` against a basic set
of structural and semantic invariants. Run via:

    python -m communitymech.export.validate_kgx

Or in CI; exits 2 on any failure.

Why not the full `kgx-python` package? It's a heavy install (>100 MB)
for a small repo with 565 edges. This validator catches the
structural problems we actually see in practice (column drift,
unbalanced rows, missing CURIEs, predicate typos). Promote to
`kgx validate` if/when biolink-model compliance becomes a release gate.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

# Required columns
NODE_COLS = ["id", "category", "name", "description", "provided_by"]
EDGE_COLS = [
    "id",
    "subject",
    "predicate",
    "object",
    "category",
    "publications",
    "supporting_text",
    "knowledge_level",
    "agent_type",
    "primary_knowledge_source",
]

# Pattern: anything matching `<prefix>:<localpart>` where prefix is
# alpha[alphanumeric] and localpart is non-empty. Permissive.
_CURIE_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_.-]*:[^\s]+$")
_BIOLINK_RE = re.compile(r"^biolink:[A-Za-z][A-Za-z0-9_]*$")


def _check_columns(header: list[str], expected: list[str], path: Path, errors: list[str]) -> None:
    if header != expected:
        errors.append(
            f"{path.name}: column header mismatch.\n"
            f"  expected: {expected}\n"
            f"  got:      {header}"
        )


def validate_nodes(path: Path, errors: list[str]) -> dict[str, int]:
    """Validate nodes.tsv. Returns {id: row_index} for cross-ref."""
    seen: dict[str, int] = {}
    with open(path) as f:
        rdr = csv.reader(f, delimiter="\t")
        try:
            header = next(rdr)
        except StopIteration:
            errors.append(f"{path.name}: empty file")
            return seen
        _check_columns(header, NODE_COLS, path, errors)
        for i, row in enumerate(rdr, 2):  # data starts at line 2
            if len(row) != len(NODE_COLS):
                errors.append(
                    f"{path.name}:{i}: expected {len(NODE_COLS)} columns, " f"got {len(row)}"
                )
                continue
            nid, cat, *_ = row
            if not nid or not _CURIE_RE.match(nid):
                errors.append(f"{path.name}:{i}: invalid id {nid!r}")
            if cat and not _BIOLINK_RE.match(cat):
                errors.append(f"{path.name}:{i}: category {cat!r} is not a " f"biolink: CURIE")
            if nid in seen:
                errors.append(
                    f"{path.name}:{i}: duplicate id {nid!r} " f"(also at line {seen[nid]})"
                )
            else:
                seen[nid] = i
    return seen


def validate_edges(
    path: Path, node_ids: dict[str, int], errors: list[str], warnings: list[str]
) -> int:
    """Validate edges.tsv. Returns row count."""
    n = 0
    with open(path) as f:
        rdr = csv.reader(f, delimiter="\t")
        try:
            header = next(rdr)
        except StopIteration:
            errors.append(f"{path.name}: empty file")
            return 0
        _check_columns(header, EDGE_COLS, path, errors)
        seen: dict[str, int] = {}
        for i, row in enumerate(rdr, 2):
            n += 1
            if len(row) != len(EDGE_COLS):
                errors.append(
                    f"{path.name}:{i}: expected {len(EDGE_COLS)} cols, " f"got {len(row)}"
                )
                continue
            eid, subj, pred, obj, cat, pubs, _supp, _kl, _at, _pks = row
            if not eid:
                errors.append(f"{path.name}:{i}: empty edge id")
            if eid in seen:
                errors.append(
                    f"{path.name}:{i}: duplicate edge id {eid!r} " f"(also at line {seen[eid]})"
                )
            seen[eid] = i
            if not _CURIE_RE.match(subj):
                errors.append(f"{path.name}:{i}: invalid subject {subj!r}")
            elif subj not in node_ids:
                warnings.append(f"{path.name}:{i}: subject {subj!r} not in nodes.tsv")
            if not _CURIE_RE.match(obj):
                errors.append(f"{path.name}:{i}: invalid object {obj!r}")
            elif obj not in node_ids:
                warnings.append(f"{path.name}:{i}: object {obj!r} not in nodes.tsv")
            if pred and not _BIOLINK_RE.match(pred):
                errors.append(f"{path.name}:{i}: predicate {pred!r} is not a " f"biolink: CURIE")
            if cat and not _BIOLINK_RE.match(cat):
                errors.append(f"{path.name}:{i}: edge category {cat!r} is not a " f"biolink: CURIE")
            # Each publication entry should look like a CURIE
            for p in pubs.split("|"):
                if p and not _CURIE_RE.match(p):
                    warnings.append(f"{path.name}:{i}: publication {p!r} is not " f"CURIE-shaped")
    return n


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--kgx-dir",
        type=Path,
        default=Path("output/kgx"),
        help="dir containing nodes.tsv and edges.tsv",
    )
    ap.add_argument("--strict", action="store_true", help="treat warnings as errors")
    args = ap.parse_args()

    nodes_path = args.kgx_dir / "nodes.tsv"
    edges_path = args.kgx_dir / "edges.tsv"
    for p in (nodes_path, edges_path):
        if not p.is_file():
            print(f"missing: {p}", file=sys.stderr)
            return 2

    errors: list[str] = []
    warnings: list[str] = []

    node_ids = validate_nodes(nodes_path, errors)
    n_edges = validate_edges(edges_path, node_ids, errors, warnings)

    print(f"Nodes:    {len(node_ids):>5}")
    print(f"Edges:    {n_edges:>5}")
    print(f"Errors:   {len(errors):>5}")
    print(f"Warnings: {len(warnings):>5}")

    if errors:
        print("\n--- ERRORS ---", file=sys.stderr)
        for e in errors[:50]:
            print(f"  {e}", file=sys.stderr)
        if len(errors) > 50:
            print(f"  ... and {len(errors) - 50} more", file=sys.stderr)
    if warnings:
        print("\n--- WARNINGS ---", file=sys.stderr)
        for w in warnings[:20]:
            print(f"  {w}", file=sys.stderr)
        if len(warnings) > 20:
            print(f"  ... and {len(warnings) - 20} more", file=sys.stderr)

    if errors:
        return 2
    if args.strict and warnings:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
