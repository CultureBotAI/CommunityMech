#!/usr/bin/env python3
"""Strict LinkML validation harness for CommunityMech instance records.

Wraps the in-process ``linkml.validator`` with
``JsonschemaValidationPlugin(closed=True)`` so unknown fields are flagged.
(The existing ``just validate-all`` target shells out to ``linkml-validate``
per file in open mode and silently lets unknown fields pass.) Emits a
structured TSV of every ERROR result and exits non-zero if any are found.

Usage::

    python scripts/validate_strict.py [PATH ...]
    python scripts/validate_strict.py --sample 50
    python scripts/validate_strict.py --out reports/instance_validation_failures.tsv

Paths may be files or directories; directories are walked for ``*.yaml``.

Default scope when no paths given:
    kb/communities/

CommunityMech has a single root class (``MicrobialCommunity``); no class
routing required.

Ported from CultureMech / MediaIngredientMech / TraitMech.
"""

from __future__ import annotations

import argparse
import csv
import os
import re
import sys
from collections.abc import Iterable
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

import yaml
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml.validator.report import Severity

from communitymech.validators.gtdb_coherence import validate_gtdb_coherence
from communitymech.validators.gtdb_lineage_tree import check_lineage_shape
from communitymech.validators.prokaryotic_lineage import check_record as check_prokaryotic_lineage
from communitymech.validators.shared_taxon_ids import check_record as check_shared_taxon_ids
from communitymech.validators.yaml_scalars import find_truncated_scalars

_REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = _REPO_ROOT / "src" / "communitymech" / "schema" / "communitymech.yaml"
# `data/isolates` uses the same taxon_term shape and was outside this gate
# while the comment below claimed "the same gate as everything else"
# (#390 review). It has been outside a gate once before (#310).
DEFAULT_ROOTS = [_REPO_ROOT / "kb" / "communities", _REPO_ROOT / "data" / "isolates"]
TARGET_CLASS = "MicrobialCommunity"


# Per-worker singleton — built lazily after fork so the schema parses once per
# worker process, not once per file.
_VALIDATOR: Validator | None = None


def _get_validator() -> Validator:
    global _VALIDATOR
    if _VALIDATOR is None:
        _VALIDATOR = Validator(
            schema=str(SCHEMA_PATH),
            validation_plugins=[JsonschemaValidationPlugin(closed=True)],
        )
    return _VALIDATOR


# Classifier regexes — keep narrow so each category is meaningful and the rest
# fall into "other" for manual review rather than getting silently bucketed.
_CATEGORY_RULES: list[tuple[str, re.Pattern[str]]] = [
    (
        "unexpected_field",
        re.compile(
            r"Additional properties are not allowed \('(?P<key>[^']+)'"
            r" was unexpected\) in (?P<path>\S+)"
        ),
    ),
    ("missing_required", re.compile(r"'(?P<key>[^']+)' is a required property in (?P<path>\S+)")),
    ("enum_mismatch", re.compile(r"'(?P<value>[^']+)' is not one of \[(?P<choices>[^\]]+)\]")),
    ("type_mismatch", re.compile(r"(?P<value>'[^']+'|\S+) is not of type '(?P<type>[^']+)'")),
    ("pattern_mismatch", re.compile(r"(?P<value>'[^']+'|\S+) does not match (?P<pattern>'[^']+')")),
    ("format_mismatch", re.compile(r"(?P<value>'[^']+'|\S+) is not a '(?P<format>[^']+)'")),
    ("range_violation", re.compile(r"(?P<value>\S+) is (less than|greater than) (?P<bound>\S+)")),
]


def classify(message: str) -> tuple[str, str]:
    """Return (category, detail) for a validator message."""
    for name, rule in _CATEGORY_RULES:
        m = rule.search(message)
        if m:
            parts = m.groupdict()
            detail = "|".join(f"{k}={v}" for k, v in parts.items())
            return name, detail
    return "other", ""


def validate_one(path: Path) -> list[dict]:
    """Validate a single YAML file. Returns one dict per ERROR result."""
    validator = _get_validator()
    try:
        with path.open() as f:
            instance = yaml.safe_load(f)
    except yaml.YAMLError as e:
        return [
            {
                "file": str(path),
                "category": "yaml_parse_error",
                "detail": "",
                "path": "",
                "message": str(e).splitlines()[0][:300],
            }
        ]
    if instance is None:
        return [
            {
                "file": str(path),
                "category": "empty_file",
                "detail": "",
                "path": "",
                "message": "file parsed as None",
            }
        ]

    try:
        report = validator.validate(instance, target_class=TARGET_CLASS)
    except Exception as e:  # noqa: BLE001 — surface anything weird as a row
        return [
            {
                "file": str(path),
                "category": "validator_crash",
                "detail": type(e).__name__,
                "path": "",
                "message": str(e)[:300],
            }
        ]

    rows = []
    for result in report.results:
        if result.severity != Severity.ERROR:
            continue
        category, detail = classify(result.message)
        rows.append(
            {
                "file": str(path),
                "category": category,
                "detail": detail,
                "path": result.instance_index or "",
                "message": result.message[:300],
            }
        )

    # Relational checks the schema cannot express (#387). LinkML has no
    # cross-field arithmetic, so `support_genomes: 99` beside `total_genomes: 3`
    # is valid to it, as is an explicit `total_genomes: null` — a null satisfies
    # JSON-Schema `required`, which is what `value_presence: PRESENT` compiles
    # to. Running them here rather than only in pytest means a hand-authored
    # record is checked by the same gate as everything else.
    # A mid-scalar `#` silently truncates an unquoted value, and the file stays
    # valid YAML — so no schema check can see it (#398). Raw-text, hence here
    # rather than in the instance validator.
    for scalar in find_truncated_scalars(path):
        rows.append(
            {
                "file": str(path),
                "category": "yaml_truncated_scalar",
                "detail": f"line={scalar.line}|key={scalar.key}",
                "path": "",
                "message": scalar.message[:300],
            }
        )

    for issue in validate_gtdb_coherence(path):
        rows.append(
            {
                "file": str(path),
                "category": f"gtdb_{issue.category}",
                "detail": issue.taxon,
                "path": "",
                "message": issue.message[:300],
            }
        )

    # One specific NCBITaxon id standing in for two different organisms (#292).
    # Not covered by the id<->label gate: the id and label agree, and only the
    # `preferred_term` disagrees.
    taxonomy = instance.get("taxonomy") if isinstance(instance, dict) else None
    for message in check_shared_taxon_ids(taxonomy):
        rows.append(
            {
                "file": str(path),
                "category": "taxon_id_reused_for_another_organism",
                "detail": message.split(" ", 1)[0],
                "path": "",
                "message": message[:300],
            }
        )

    # A lineage that is not a contiguous chain of ranks from d__ (#454).
    # Contiguity is what makes the corpus half of that check sound, and the
    # corpus half — one taxon, one parent — needs every record at once, so it
    # runs in `just validate-gtdb-all` rather than here.
    for message in check_lineage_shape(instance):
        rows.append(
            {
                "file": str(path),
                "category": "gtdb_lineage_malformed",
                "detail": message.split(":", 1)[0],
                "path": "",
                "message": message[:300],
            }
        )

    # A GTDB block on a eukaryote or a virus (#365). GTDB classifies prokaryotes
    # only, so this is a contradiction rather than a suspicion — and no other
    # gate sees it, because id, label and ncbi_source_id all agree. Takes the
    # whole document because interaction participants can carry a block too.
    for message in check_prokaryotic_lineage(instance):
        rows.append(
            {
                "file": str(path),
                "category": "gtdb_lineage_contradicts_id_domain",
                "detail": message.split(" ", 1)[0],
                "path": "",
                "message": message[:300],
            }
        )
    return rows


_DEFAULT_EXCLUDE_PARTS = {"backups", ".backups", "snapshots"}


def iter_yaml_files(paths: Iterable[Path]) -> list[Path]:
    """Walk inputs, filtering out backup / snapshot subtrees."""
    out: list[Path] = []
    for p in paths:
        if p.is_file():
            out.append(p)
        elif p.is_dir():
            for f in sorted(p.rglob("*.yaml")):
                if _DEFAULT_EXCLUDE_PARTS.intersection(f.parts):
                    continue
                out.append(f)
    return out


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths", nargs="*", type=Path, help="Files or directories. Defaults to kb/communities/."
    )
    parser.add_argument(
        "--out",
        type=Path,
        # Resolved against the repo, not the cwd. The relative default wrote a
        # stray `reports/` tree wherever the script was run from, and any test
        # invoking it without `--out` overwrote the committed report — which
        # happened twice, surviving only because a full run left the file
        # byte-identical (#391).
        default=_REPO_ROOT / "reports" / "instance_validation_failures.tsv",
        help="TSV output path (default: <repo>/reports/instance_validation_failures.tsv).",
    )
    parser.add_argument(
        "--sample",
        type=int,
        metavar="N",
        help="Validate only the first N files (after sorting). Useful for smoke tests.",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=max(1, (os.cpu_count() or 4) - 1),
        help="Process pool size. Default: ncpu - 1.",
    )
    parser.add_argument(
        "--fail-on",
        choices=("error", "never"),
        default="error",
        help="Exit non-zero policy. 'error' (default) exits 1 if any ERROR row was emitted.",
    )
    parser.add_argument("--quiet", action="store_true", help="Suppress per-file progress lines.")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    roots = args.paths or DEFAULT_ROOTS
    files = iter_yaml_files(roots)
    if args.sample:
        files = files[: args.sample]
    if not files:
        print("No YAML files found.", file=sys.stderr)
        return 2

    args.out.parent.mkdir(parents=True, exist_ok=True)

    print(
        f"Validating {len(files)} files with {args.workers} workers; schema={SCHEMA_PATH}",
        file=sys.stderr,
    )

    all_rows: list[dict] = []
    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(validate_one, p): p for p in files}
        for done, fut in enumerate(as_completed(futures), 1):
            rows = fut.result()
            all_rows.extend(rows)
            if not args.quiet and done % 50 == 0:
                print(
                    f"  {done}/{len(files)} files processed, {len(all_rows)} ERROR rows so far",
                    file=sys.stderr,
                )

    all_rows.sort(key=lambda r: (r["file"], r["path"], r["category"], r["message"]))
    with args.out.open("w", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=["file", "category", "detail", "path", "message"],
            delimiter="\t",
            quoting=csv.QUOTE_MINIMAL,
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(all_rows)

    by_cat: dict[str, int] = {}
    files_with_errors: set[str] = set()
    for row in all_rows:
        by_cat[row["category"]] = by_cat.get(row["category"], 0) + 1
        files_with_errors.add(row["file"])

    print("", file=sys.stderr)
    print("=== validate-strict summary ===", file=sys.stderr)
    print(f"  files scanned:      {len(files)}", file=sys.stderr)
    print(f"  files with ERROR:   {len(files_with_errors)}", file=sys.stderr)
    print(f"  total ERROR rows:   {len(all_rows)}", file=sys.stderr)
    print(f"  TSV:                {args.out}", file=sys.stderr)
    if by_cat:
        print("  by category:", file=sys.stderr)
        for cat, count in sorted(by_cat.items(), key=lambda kv: -kv[1]):
            print(f"    {cat:24s} {count:>8d}", file=sys.stderr)

    if args.fail_on == "error" and all_rows:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
