"""The relational checks LinkML cannot express, and the gate that runs them (#387).

The schema bounds `support_genomes` and `total_genomes` individually but has no
cross-field arithmetic, so `linkml-validate` accepts a block claiming 99
supporting genomes out of 3. It also accepts `total_genomes: null`, because
`value_presence: PRESENT` compiles to JSON-Schema `required` and a null satisfies
that — LinkML emits `type: ["integer", "null"]` for every optional slot, so the
class rule can only ever guard a *missing* key.

These rules used to live only in `tests/test_gtdb_grounding_freshness.py`. That
covers the committed KB on every CI run and does nothing for a hand-authored
record someone validates with `just validate`. They now live in
`communitymech.validators.gtdb_coherence`, called from that test, from
`just validate-gtdb`, and from `scripts/validate_strict.py` — which is a CI gate.

Each check below is paired with an assertion that `linkml-validate` **accepts**
the same instance, so the tests document what the schema does not cover rather
than asserting it in prose. If one of those starts failing, LinkML tightened and
the constraint should move into the schema.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

import pytest
import yaml

from communitymech.validators.gtdb_coherence import (
    _blocks,
    check_block,
    validate_gtdb_coherence,
)

REPO = Path(__file__).parent.parent
SCHEMA = REPO / "src/communitymech/schema/communitymech.yaml"
FIXTURE = REPO / "kb/communities/Lake_Washington_Methane_Oxygen_Methylotroph_Community.yaml"


def _valid_block() -> dict:
    return {
        "gtdb_id": "GTDB:f__Methylomonadaceae",
        "gtdb_taxon": "Methylomonadaceae",
        "ncbi_source_id": "NCBITaxon:403",
        "majority_fraction": 0.695,
        "support_genomes": 107,
        "total_genomes": 154,
        "is_reclassified": True,
    }


def _linkml_accepts(tmp_path: Path, block: dict) -> bool:
    """Does `linkml-validate` accept a real record carrying this block?"""
    doc = yaml.safe_load(FIXTURE.read_text())
    for entry in doc["taxonomy"]:
        term = entry.get("taxon_term") or {}
        if term.get("gtdb_classification") and "support_genomes" in term["gtdb_classification"]:
            term["gtdb_classification"] = block
            break
    else:  # pragma: no cover - fixture drift
        pytest.fail("fixture has no block with support_genomes")

    path = tmp_path / "probe.yaml"
    path.write_text(yaml.dump(doc, sort_keys=False, allow_unicode=True))
    result = subprocess.run(
        ["uv", "run", "linkml-validate", "-s", str(SCHEMA), str(path)],
        capture_output=True,
        text=True,
        cwd=REPO,
    )
    if result.returncode != 0:
        # Distinguish "linkml rejected the instance" from "the subprocess never
        # ran". Without this the negative assertions pass whenever `uv` errors —
        # and that is exactly the test whose job is to prove False is reachable.
        output = result.stdout + result.stderr
        assert "[ERROR]" in output, (
            f"linkml-validate failed without reporting a validation error, so this "
            f"says nothing about the schema:\n{output[-1500:]}"
        )
    return result.returncode == 0


def test_a_correct_block_is_clean():
    """Guards every negative case below: if all blocks failed, they'd pass vacuously."""
    assert check_block(_valid_block()) == []


@pytest.mark.parametrize(
    ("mutation", "expected"),
    [
        ({"support_genomes": 99, "total_genomes": 3}, "support_exceeds_total"),
        ({"support_genomes": 2, "total_genomes": 9999}, "fraction_disagrees_with_counts"),
        ({"total_genomes": None}, "null_count"),
        ({"support_genomes": None}, "null_count"),
        ({"majority_fraction": 0.4}, "fraction_out_of_range"),
        ({"majority_fraction": 7.5}, "fraction_out_of_range"),
    ],
)
def test_incoherent_blocks_are_caught(mutation, expected):
    block = _valid_block()
    block.update(mutation)
    assert expected in {category for category, _ in check_block(block)}


def test_a_numerator_without_a_denominator_is_caught():
    block = _valid_block()
    del block["total_genomes"]
    assert "numerator_without_denominator" in {c for c, _ in check_block(block)}


def test_a_species_block_with_only_a_denominator_is_fine():
    """The normal species case — 336 blocks. Flagging it would fail the whole KB."""
    block = _valid_block()
    del block["support_genomes"]
    assert check_block(block) == []


def test_rounding_slack_is_tolerated_but_drift_is_not():
    """`majority_fraction` is stored rounded, so the check needs a tolerance.

    107/154 is 0.6948..., stored as 0.695. A tolerance any looser than one unit
    in the last place stops catching real drift, so both sides are pinned.
    """
    ok = _valid_block()
    assert check_block(ok) == [], "legitimate rounding must not be flagged"

    drifted = _valid_block()
    drifted["majority_fraction"] = 0.71
    assert "fraction_disagrees_with_counts" in {c for c, _ in check_block(drifted)}

    # 0.71 is 0.015 away, so it survives any tolerance below ~0.0149 — loosening
    # 0.001 to 0.01 passed the whole suite (#390 review). This sits two units in
    # the last place out, the smallest drift that must still be caught.
    just_outside = _valid_block()
    just_outside["majority_fraction"] = 0.697
    assert "fraction_disagrees_with_counts" in {
        c for c, _ in check_block(just_outside)
    }, "a two-in-the-last-place drift went unreported — the tolerance is too loose"


@pytest.mark.parametrize("total", [0, -5])
def test_a_nonpositive_total_is_caught(total):
    block = _valid_block()
    block.update(total_genomes=total, support_genomes=0)
    assert "nonpositive_total" in {c for c, _ in check_block(block)}


# ---------------------------------------------------------------------------
# What the schema does NOT catch — asserted, so the gap is a decision.
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "mutation",
    [
        {"support_genomes": 99, "total_genomes": 3},
        {"support_genomes": 2, "total_genomes": 9999},
        {"total_genomes": None},
    ],
)
def test_linkml_accepts_what_this_validator_rejects(tmp_path, mutation):
    """The reason this module exists rather than a schema constraint.

    If one of these starts failing, LinkML gained cross-field expression (or
    stopped allowing nulls on optional slots) and the check should move into the
    schema — delete the corresponding case here when it does.
    """
    block = _valid_block()
    block.update(mutation)
    assert check_block(block), "this fixture is supposed to be incoherent"
    assert _linkml_accepts(
        tmp_path, block
    ), "linkml-validate now rejects this — move the constraint into the schema"


def test_linkml_still_rejects_what_the_schema_does_cover(tmp_path):
    """Guards the above: proves `_linkml_accepts` can return False at all."""
    block = _valid_block()
    del block["total_genomes"]  # class rule: support present -> total present
    assert not _linkml_accepts(tmp_path, block)


# ---------------------------------------------------------------------------
# The gate itself.
# ---------------------------------------------------------------------------


def test_the_committed_kb_is_coherent():
    """Every record, not just the ones with counts."""
    issues, scanned, blocks = [], 0, 0
    for directory in ("kb/communities", "data/isolates"):
        for path in sorted((REPO / directory).glob("*.yaml")):
            scanned += 1
            blocks += len(list(_blocks(yaml.safe_load(path.read_text()))))
            issues.extend(validate_gtdb_coherence(path))
    # Without these, moving or renaming kb/communities empties both globs and
    # this passes having checked nothing (#390 review).
    assert scanned > 300, f"expected the whole KB, scanned only {scanned} records"
    assert blocks > 500, f"expected the grounded KB, saw only {blocks} blocks"
    assert not issues, "incoherent gtdb_classification in the KB:\n" + "\n".join(
        f"  {issue}" for issue in issues[:20]
    )


def test_validate_strict_reports_the_incoherence(tmp_path):
    """The check must fire through the CI gate, not only when called directly.

    `validate-strict` is where this actually protects the repo; wiring it in and
    never exercising the wiring is how a gate ends up green and blind.
    """
    doc = yaml.safe_load(FIXTURE.read_text())
    for entry in doc["taxonomy"]:
        block = (entry.get("taxon_term") or {}).get("gtdb_classification")
        if block and "support_genomes" in block:
            block.update(support_genomes=99, total_genomes=3)
            break
    path = tmp_path / "broken.yaml"
    path.write_text(yaml.dump(doc, sort_keys=False, allow_unicode=True))

    result = subprocess.run(
        # `--out` matters: the default is cwd-relative and lands on the
        # git-tracked reports/instance_validation_failures.tsv, so running this
        # test alone left the tree dirty with /tmp paths in a committed file.
        [
            "uv",
            "run",
            "python",
            "scripts/validate_strict.py",
            str(path),
            "--out",
            str(tmp_path / "report.tsv"),
        ],
        capture_output=True,
        text=True,
        cwd=REPO,
    )

    assert result.returncode == 1, "validate-strict passed a record it should fail"
    assert "gtdb_support_exceeds_total" in (result.stdout + result.stderr)


def test_validate_strict_still_passes_the_real_kb_record(tmp_path):
    """Guards the test above against failing for an unrelated reason."""
    path = tmp_path / "clean.yaml"
    path.write_text(FIXTURE.read_text())
    result = subprocess.run(
        [
            "uv",
            "run",
            "python",
            "scripts/validate_strict.py",
            str(path),
            "--out",
            str(tmp_path / "report.tsv"),
        ],
        capture_output=True,
        text=True,
        cwd=REPO,
    )
    assert (
        result.returncode == 0
    ), f"a clean record failed validate-strict:\n{result.stdout[-2000:]}"


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (3.0, "support_exceeds_total"),  # integral float: comparisons must still run
        (0.0, "nonpositive_total"),
        (3.5, "non_integral_count"),  # a genome count cannot be fractional
        ("3", "non_numeric_count"),
        ([3], "non_numeric_count"),
        (True, "non_numeric_count"),  # isinstance(True, int) is True in Python
    ],
)
def test_non_integer_counts_do_not_slip_through(value, expected):
    """The regression this module shipped with, and the type holes around it.

    Guarding with `isinstance(total, int)` reads as type-safety and is not:
    it is False for `3.0`, and JSON-Schema `type: integer` accepts `3.0`. So
    `total_genomes: 3.0` passed both gates while the inline logic this module
    replaced caught it. Skipping a value silently is what made that invisible,
    so anything non-numeric is now reported rather than ignored (#390 review).
    """
    block = _valid_block()
    block.update(support_genomes=99, total_genomes=value)
    assert expected in {category for category, _ in check_block(block)}


def test_a_malformed_term_does_not_crash_the_run(tmp_path):
    """A crash here kills `validate-strict` outright, not just one file.

    `validate_one` calls this outside its try/except, so an AttributeError
    propagates through the process pool and `main()` dies — taking the TSV
    report with it, so every other file's errors are lost too. A scalar `term:`
    is an ordinary hand-edit (#390 review).
    """
    record = tmp_path / "malformed.yaml"
    record.write_text(
        "taxonomy:\n"
        "- taxon_term:\n"
        "    term: NCBITaxon:403\n"  # a scalar where a mapping belongs
        "    gtdb_classification:\n"
        "      support_genomes: 9\n"
        "      total_genomes: 3\n"
    )

    issues = validate_gtdb_coherence(record)

    assert "support_exceeds_total" in {
        issue.category for issue in issues
    }, "the malformed term must not stop the block being checked"


@pytest.mark.parametrize(
    "text",
    ["- just\n- a list\n", "a bare scalar\n", "taxonomy: not-a-list\n", "taxonomy:\n- 3\n"],
)
def test_structurally_odd_documents_are_survived(tmp_path, text):
    """`validate_one` hands these straight here — only `None` is short-circuited."""
    record = tmp_path / "odd.yaml"
    record.write_text(text)
    assert validate_gtdb_coherence(record) == []
