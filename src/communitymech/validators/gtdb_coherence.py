"""Relational checks on `gtdb_classification` that LinkML cannot express (#387).

The schema types the evidence counts and bounds them individually — `range:
integer`, `minimum_value: 1`, and a class rule requiring `total_genomes` whenever
`support_genomes` is present. What it cannot do is relate two slots to each
other, because the JSON-Schema backend has no cross-field arithmetic. So
`linkml-validate` accepts all of these:

    support_genomes: 99   total_genomes: 3      # more supporters than genomes
    support_genomes: 2    total_genomes: 9999   majority_fraction: 1.0
    support_genomes: 5    total_genomes: null   # a null satisfies `required`

The last is the sharpest, and is why this module exists rather than a note in the
schema. `value_presence: PRESENT` compiles to JSON-Schema `required`, which an
explicit null satisfies, and `minimum` does not apply to null either — so the
class rule guards a *missing* key only. LinkML emits `type: ["integer", "null"]`
for every optional slot, so this is not something the schema can be coaxed into.

These checks previously lived only in `tests/test_gtdb_grounding_freshness.py`,
which covers the committed KB on every CI run but does nothing for a
hand-authored record someone validates with `just validate` alone. Here they run
wherever schema validation runs — `just validate-gtdb`, and folded into
`just validate-strict`, which is a CI gate.

Usage:

    from pathlib import Path
    from communitymech.validators.gtdb_coherence import validate_gtdb_coherence

    for issue in validate_gtdb_coherence(Path("kb/communities/Foo.yaml")):
        print(issue.category, issue.message)
"""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

# `majority_fraction` is stored rounded to 3 places, so an exact comparison
# against support/total would fail on legitimate blocks. One unit in the last
# place is the whole tolerance — anything looser stops catching real drift.
FRACTION_TOLERANCE = 0.001

# The tool grounds on a majority, so a fraction at or below 0.5 is not one. This
# duplicates the schema's 0.0–1.0 bound deliberately: the schema cannot express
# the lower half, and a 0.4 "majority" is the kind of thing that survives a
# hand-edit.
MIN_FRACTION = 0.5


def _as_number(value: Any) -> float | None:
    """The value as a number, or None if it is not one.

    `isinstance(x, int)` was the original guard and it was a regression: it is
    False for `3.0`, and JSON-Schema `type: integer` accepts `3.0`, so
    `total_genomes: 3.0` slipped past every comparison below while the inline
    logic this module replaced caught it (#390 review). It is also True for
    `True`, which would read `total_genomes: true` as 1.

    Anything non-numeric returns None and is reported separately rather than
    silently skipped — silently skipping is what made the float case invisible.
    """
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    return None


@dataclass(frozen=True)
class CoherenceIssue:
    """One problem with one `gtdb_classification` block."""

    file: str
    taxon: str
    category: str
    message: str

    def __str__(self) -> str:  # pragma: no cover - display only
        return f"{self.file}: {self.taxon} [{self.category}] {self.message}"


def _blocks(doc: Any) -> Iterator[tuple[str, dict]]:
    """Yield (label, gtdb_classification) for each taxonomy entry that has one.

    Positional index is included in the label because a record may legitimately
    list the same NCBITaxon id many times — `GLBRC_Populus_Variovorax_SynCom28`
    has 28 isolates on one id — and an id-keyed message would point at the wrong
    entry.
    """
    # Every level is type-guarded, not just truth-tested. `validate_one` in
    # scripts/validate_strict.py calls this outside its try/except, so an
    # AttributeError here does not fail one file — it kills the run and the TSV
    # report is never written, losing every other file's errors (#390 review).
    if not isinstance(doc, dict):
        return
    taxonomy = doc.get("taxonomy")
    if not isinstance(taxonomy, list):
        return
    for index, entry in enumerate(taxonomy):
        if not isinstance(entry, dict):
            continue
        term_block = entry.get("taxon_term")
        if not isinstance(term_block, dict):
            continue
        grounding = term_block.get("gtdb_classification")
        if isinstance(grounding, dict):
            term = term_block.get("term")
            name = (
                term_block.get("preferred_term")
                or (term.get("id") if isinstance(term, dict) else None)
                or "?"
            )
            yield f"taxonomy[{index}] {name}", grounding


def _taxon_terms(doc: Any) -> Iterator[tuple[str, dict]]:
    """Yield (label, taxon_term) for every taxonomy entry, grounded or not.

    `_blocks` only reaches taxa that already carry a grounding, which is exactly
    the population the status enum exists to look past.
    """
    if not isinstance(doc, dict):
        return

    def _label(term_block: dict) -> str:
        term = term_block.get("term")
        return (
            term_block.get("preferred_term")
            or (term.get("id") if isinstance(term, dict) else None)
            or "?"
        )

    taxonomy = doc.get("taxonomy")
    if isinstance(taxonomy, list):
        for index, entry in enumerate(taxonomy):
            if not isinstance(entry, dict):
                continue
            term_block = entry.get("taxon_term")
            if isinstance(term_block, dict):
                yield f"taxonomy[{index}] {_label(term_block)}", term_block

    # `EcologicalInteraction.source_taxon` / `target_taxon` also have range
    # TaxonDescriptor, so they carry the same two slots — 1139 more instances
    # than `taxonomy` alone. Walking only `taxonomy` meant an interaction taxon
    # could claim GROUNDED with no block, or carry a single candidate, and every
    # gate reported clean (#392 review).
    interactions = doc.get("ecological_interactions")
    if isinstance(interactions, list):
        for index, entry in enumerate(interactions):
            if not isinstance(entry, dict):
                continue
            for slot in ("source_taxon", "target_taxon"):
                term_block = entry.get(slot)
                if isinstance(term_block, dict):
                    yield (
                        f"ecological_interactions[{index}].{slot} {_label(term_block)}",
                        term_block,
                    )


def check_block(block: dict) -> list[tuple[str, str]]:
    """Return (category, message) for each incoherence in one block.

    Split out from the file walk so callers can check a block they hold in
    memory — the tests use it, and so does anything validating before a write.
    """
    problems: list[tuple[str, str]] = []
    raw_support = block.get("support_genomes")
    raw_total = block.get("total_genomes")
    raw_fraction = block.get("majority_fraction")

    for slot, value in (
        ("support_genomes", raw_support),
        ("total_genomes", raw_total),
        ("majority_fraction", raw_fraction),
    ):
        if slot not in block:
            continue
        # An explicitly-null count is the case the schema's class rule misses.
        if value is None:
            if slot != "majority_fraction":
                problems.append(
                    (
                        "null_count",
                        f"{slot} is present but null; `linkml-validate` accepts this "
                        f"because a null satisfies JSON-Schema `required` (#387). Omit "
                        f"the key instead.",
                    )
                )
            continue
        if _as_number(value) is None:
            problems.append(
                (
                    "non_numeric_count",
                    f"{slot}={value!r} is not a number, so none of the relational "
                    f"checks below can run on it.",
                )
            )
        elif slot != "majority_fraction" and float(value) != int(float(value)):
            problems.append(
                (
                    "non_integral_count",
                    f"{slot}={value!r} is a genome count and must be a whole number.",
                )
            )

    support = _as_number(raw_support)
    total = _as_number(raw_total)
    fraction = _as_number(raw_fraction)

    if raw_support is not None and "total_genomes" not in block:
        problems.append(
            (
                "numerator_without_denominator",
                f"support_genomes={raw_support} with no total_genomes — a numerator "
                f"says nothing without what it is out of (#383).",
            )
        )

    if total is not None and total <= 0:
        problems.append(
            ("nonpositive_total", f"total_genomes={raw_total} — a majority over no genomes.")
        )

    if support is not None and total is not None:
        if support > total:
            problems.append(
                (
                    "support_exceeds_total",
                    f"support_genomes={raw_support} > total_genomes={raw_total} — more "
                    f"supporting genomes than genomes counted.",
                )
            )
        elif total > 0 and fraction is not None:
            computed = round(support / total, 3)
            if abs(computed - fraction) > FRACTION_TOLERANCE:
                problems.append(
                    (
                        "fraction_disagrees_with_counts",
                        f"{support}/{total} = {computed} but majority_fraction="
                        f"{fraction}. One of the three is stale — re-run "
                        f"`gtdb_ground.py --refresh --apply` on this record.",
                    )
                )

    if fraction is not None and not (MIN_FRACTION <= fraction <= 1.0):
        problems.append(
            (
                "fraction_out_of_range",
                f"majority_fraction={raw_fraction} outside [{MIN_FRACTION}, 1.0]. "
                f"The bound is inclusive because one KB block sits at exactly 0.5 "
                f"— an unresolved two-way tie, tracked in #382 — not because a tie "
                f"is a majority.",
            )
        )

    return problems


def check_status(term_block: dict) -> list[tuple[str, str]]:
    """Relate `gtdb_grounding_status` to the rest of the taxon (#294).

    The enum is deliberately redundant with the block's presence — a consumer
    should read a state, not infer one — and redundancy that nothing checks is
    just two sources of truth. The schema can express neither half: it cannot
    say "GROUNDED iff gtdb_classification exists", nor "gtdb_candidates only
    when AMBIGUOUS".
    """
    problems: list[tuple[str, str]] = []
    status = term_block.get("gtdb_grounding_status")
    has_block = isinstance(term_block.get("gtdb_classification"), dict)
    candidates = term_block.get("gtdb_candidates")

    if status is None:
        # Absence is tolerated: a record predating #294, or one hand-authored
        # since. Flagging it would make the slot required in practice while the
        # schema calls it optional.
        if candidates:
            problems.append(
                (
                    "candidates_without_status",
                    "gtdb_candidates with no gtdb_grounding_status — candidates are "
                    "only meaningful for AMBIGUOUS.",
                )
            )
        return problems

    if status == "GROUNDED" and not has_block:
        problems.append(
            (
                "grounded_without_block",
                "gtdb_grounding_status is GROUNDED but there is no "
                "gtdb_classification. Re-run `gtdb_ground.py --apply-status`.",
            )
        )
    elif status != "GROUNDED" and has_block:
        problems.append(
            (
                "block_without_grounded_status",
                f"gtdb_grounding_status is {status} but a gtdb_classification is "
                f"present. A stored grounding is a grounding whatever the reason "
                f"it was withheld.",
            )
        )

    if candidates and status != "AMBIGUOUS":
        problems.append(
            (
                "candidates_on_unambiguous_taxon",
                f"gtdb_candidates on a {status} taxon — the contenders only exist "
                f"where the tool declined to choose.",
            )
        )
    # `candidates is not None` let the *more* degenerate case through: an
    # AMBIGUOUS taxon with no `gtdb_candidates` key at all passed, while an
    # explicit empty list was flagged. `apply_status_to_community` writes the key
    # only `if candidates:`, so the case that actually occurs was the unchecked
    # one (#392 review).
    if status == "AMBIGUOUS" and len(candidates or []) < 2:
        problems.append(
            (
                "ambiguous_without_candidates",
                "AMBIGUOUS with fewer than two candidates — an ambiguity needs at "
                "least two things to be ambiguous between.",
            )
        )
    return problems


def validate_gtdb_coherence(path: Path) -> list[CoherenceIssue]:
    """Check every `gtdb_classification` in one record."""
    try:
        doc = yaml.safe_load(path.read_text())
    except yaml.YAMLError as exc:
        return [
            CoherenceIssue(
                file=str(path),
                taxon="-",
                category="yaml_parse_error",
                message=str(exc).splitlines()[0][:300],
            )
        ]

    issues = [
        CoherenceIssue(file=str(path), taxon=label, category=category, message=message)
        for label, block in _blocks(doc)
        for category, message in check_block(block)
    ]
    issues += [
        CoherenceIssue(file=str(path), taxon=label, category=category, message=message)
        for label, term_block in _taxon_terms(doc)
        for category, message in check_status(term_block)
    ]
    return issues
