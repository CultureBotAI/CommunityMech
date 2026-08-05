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
    for index, entry in enumerate((doc or {}).get("taxonomy") or []):
        if not isinstance(entry, dict):
            continue
        term_block = entry.get("taxon_term") or {}
        if not isinstance(term_block, dict):
            continue
        grounding = term_block.get("gtdb_classification")
        if isinstance(grounding, dict):
            name = (
                term_block.get("preferred_term") or (term_block.get("term") or {}).get("id") or "?"
            )
            yield f"taxonomy[{index}] {name}", grounding


def check_block(block: dict) -> list[tuple[str, str]]:
    """Return (category, message) for each incoherence in one block.

    Split out from the file walk so callers can check a block they hold in
    memory — the tests use it, and so does anything validating before a write.
    """
    problems: list[tuple[str, str]] = []
    support = block.get("support_genomes")
    total = block.get("total_genomes")
    fraction = block.get("majority_fraction")

    # An explicitly-null count is the case the schema's class rule misses.
    for slot, value in (("support_genomes", support), ("total_genomes", total)):
        if slot in block and value is None:
            problems.append(
                (
                    "null_count",
                    f"{slot} is present but null; `linkml-validate` accepts this "
                    f"because a null satisfies JSON-Schema `required` (#387). Omit "
                    f"the key instead.",
                )
            )

    if support is not None and total is None:
        problems.append(
            (
                "numerator_without_denominator",
                f"support_genomes={support} with no total_genomes — a numerator "
                f"says nothing without what it is out of (#383).",
            )
        )

    if isinstance(total, int) and total <= 0:
        problems.append(
            ("nonpositive_total", f"total_genomes={total} — a majority over no genomes.")
        )

    if isinstance(support, int) and isinstance(total, int):
        if support > total:
            problems.append(
                (
                    "support_exceeds_total",
                    f"support_genomes={support} > total_genomes={total} — more "
                    f"supporting genomes than genomes counted.",
                )
            )
        elif total > 0 and isinstance(fraction, (int, float)):
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

    if isinstance(fraction, (int, float)) and not (MIN_FRACTION <= fraction <= 1.0):
        problems.append(
            (
                "fraction_out_of_range",
                f"majority_fraction={fraction} outside ({MIN_FRACTION}, 1.0] — the "
                f"tool grounds on a majority, so this cannot be one.",
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

    return [
        CoherenceIssue(file=str(path), taxon=label, category=category, message=message)
        for label, block in _blocks(doc)
        for category, message in check_block(block)
    ]
