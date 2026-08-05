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
    check_status,
    validate_gtdb_coherence,
)

REPO = Path(__file__).parent.parent
SCHEMA = REPO / "src/communitymech/schema/communitymech.yaml"
FIXTURE = REPO / "kb/communities/Lake_Washington_Methane_Oxygen_Methylotroph_Community.yaml"


@pytest.fixture(scope="module")
def gtdb():
    """The grounding script, loaded by path like the other suites do."""
    import importlib.util

    spec = importlib.util.spec_from_file_location("gtdb_ground", REPO / "scripts/gtdb_ground.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def mapping(gtdb):
    try:
        path = gtdb.resolve_kg_microbe_dir(None) / "data/raw/NCBI2GTDB.tsv.gz"
    except SystemExit as exc:
        pytest.skip(f"kg-microbe mapping unavailable: {str(exc).splitlines()[0]}")
    if not path.exists():
        pytest.skip(f"kg-microbe NCBI2GTDB mapping not available at {path}")
    return path


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


# ---------------------------------------------------------------------------
# The grounding-status enum (#294).
# ---------------------------------------------------------------------------


def _term(status=None, block=None, candidates=None, **extra):
    term_block = {"preferred_term": "Some taxon", "term": {"id": "NCBITaxon:1"}, **extra}
    if status is not None:
        term_block["gtdb_grounding_status"] = status
    if block is not None:
        term_block["gtdb_classification"] = block
    if candidates is not None:
        term_block["gtdb_candidates"] = candidates
    return term_block


def test_grounded_status_requires_a_block():
    assert "grounded_without_block" in {c for c, _ in check_status(_term(status="GROUNDED"))}


@pytest.mark.parametrize("status", ["NO_GTDB_EQUIVALENT", "AMBIGUOUS", "WITHHELD", "NOT_ATTEMPTED"])
def test_a_stored_block_means_grounded(status):
    """A grounding is a grounding whatever the reason it was once withheld."""
    assert "block_without_grounded_status" in {
        c for c, _ in check_status(_term(status=status, block=_valid_block()))
    }


def test_the_matched_pair_is_clean():
    assert check_status(_term(status="GROUNDED", block=_valid_block())) == []
    assert check_status(_term(status="NO_GTDB_EQUIVALENT")) == []


def test_candidates_belong_only_to_ambiguous():
    assert "candidates_on_unambiguous_taxon" in {
        c for c, _ in check_status(_term(status="NO_GTDB_EQUIVALENT", candidates=["A", "B"]))
    }
    assert check_status(_term(status="AMBIGUOUS", candidates=["A", "B"])) == []


def test_an_ambiguity_needs_two_candidates():
    assert "ambiguous_without_candidates" in {
        c for c, _ in check_status(_term(status="AMBIGUOUS", candidates=["A"]))
    }


def test_candidates_without_a_status_are_flagged():
    assert "candidates_without_status" in {c for c, _ in check_status(_term(candidates=["A", "B"]))}


def test_a_taxon_with_no_status_is_tolerated():
    """Absence must stay legal — the schema calls the slot optional."""
    assert check_status(_term()) == []
    assert check_status(_term(block=_valid_block())) == []


def test_every_kb_taxonomy_entry_carries_a_status():
    """The sweep must reach all of them, not just the grounded ones.

    Scoped to `taxonomy`, which is what `--apply-status` writes. Interaction
    `source_taxon`/`target_taxon` share the range and so may carry the slots —
    `check_status` validates them if present — but nothing populates them, and
    demanding a status there would fail the whole KB.
    """
    total, missing = 0, []
    for directory in ("kb/communities", "data/isolates"):
        for path in sorted((REPO / directory).glob("*.yaml")):
            for index, entry in enumerate(yaml.safe_load(path.read_text()).get("taxonomy") or []):
                term_block = entry.get("taxon_term") or {}
                total += 1
                if "gtdb_grounding_status" not in term_block:
                    missing.append(f"{path.name}: taxonomy[{index}]")
    assert total > 1000, f"expected the whole KB, saw {total} taxa"
    assert not missing, f"{len(missing)} taxa have no status:\n" + "\n".join(missing[:10])


def test_the_stored_statuses_reproduce_from_the_classifier(gtdb, mapping):
    """Re-derive every status and compare it to disk.

    The KB-level assertions elsewhere read files the sweep already wrote, so a
    classifier regression is invisible to them — changing the final
    `return "NOT_ATTEMPTED"` to `return "UNRESOLVED"` left every ranged
    assertion green (#392 review). This is the one test that can fail on that.
    """
    want_ids, want_species, want_higher, records = set(), set(), set(), []
    for directory in ("kb/communities", "data/isolates"):
        for path in sorted((REPO / directory).glob("*.yaml")):
            for entry in yaml.safe_load(path.read_text()).get("taxonomy") or []:
                term_block = entry.get("taxon_term") or {}
                term = term_block.get("term") or {}
                tid, label = str(term.get("id", "")), term.get("label", "")
                records.append((path.name, tid, label, term_block))
                if tid.startswith("NCBITaxon:"):
                    want_ids.add(tid.split(":")[1])
                    clean = gtdb._clean_label(label)
                    (want_species if " " in clean else want_higher).add(clean.lower())
    rows = gtdb.collect_rows(mapping, want_ids, want_species, want_higher)

    wrong = []
    for record, tid, label, term_block in records:
        status, candidates = gtdb.classify_status(
            record,
            tid,
            label,
            "gtdb_classification" in term_block,
            *rows,
            preferred=term_block.get("preferred_term"),
        )
        stored = term_block.get("gtdb_grounding_status")
        if stored != status:
            wrong.append(f"{record}: {label} stored {stored}, classifier says {status}")
        if sorted(term_block.get("gtdb_candidates") or []) != sorted(candidates):
            wrong.append(f"{record}: {label} candidate list does not reproduce")
    assert not wrong, f"{len(wrong)} statuses do not reproduce:\n" + "\n".join(wrong[:10])


def test_the_status_distribution_is_what_was_measured():
    """The counts #294 turns on, pinned tightly enough to catch a collapse.

    An earlier version used only upper/lower bounds so loose that folding
    NOT_ATTEMPTED into UNRESOLVED — the exact confusion this enum exists to
    prevent — passed every assertion. The ratio and the floor are what bite.
    """
    from collections import Counter

    counts = Counter()
    for directory in ("kb/communities", "data/isolates"):
        for path in sorted((REPO / directory).glob("*.yaml")):
            for entry in yaml.safe_load(path.read_text()).get("taxonomy") or []:
                counts[(entry.get("taxon_term") or {}).get("gtdb_grounding_status")] += 1

    assert counts["GROUNDED"] > 600
    assert counts["UNRESOLVED"] > 250, "the ungrounded-but-unexplained bucket vanished"
    assert counts["AMBIGUOUS"] > 50
    assert counts["WITHHELD"] == 2, "the #292 withholds must still be marked"
    # A floor as well as a ceiling: `< 50` alone is satisfied by zero, so
    # collapsing NOT_ATTEMPTED into another bucket passed.
    assert 1 <= counts["NOT_ATTEMPTED"] < 50, (
        "NOT_ATTEMPTED is the only value meaning outstanding work; 0 almost "
        "certainly means it is being mislabelled, not that the work is done"
    )
    assert (
        counts["NO_GTDB_EQUIVALENT"] == 0
    ), "the tool must not assert NO_GTDB_EQUIVALENT — it cannot establish it (#393)"


def test_the_withholds_are_marked_withheld_not_grounded():
    """The #292 pair, and the id collision that mislabelled three neighbours.

    Keying the withhold list by NCBITaxon id marked three *correct* groundings
    WITHHELD, because both records reuse the offending id for a legitimate entry
    — BioModels uses 821 for its real Bacteroides vulgatus, KBase uses 1236 for
    two Steroidobacteraceae. Keyed by preferred_term instead.
    """
    from communitymech.validators.gtdb_coherence import _taxon_terms

    for record, preferred in [
        ("BioModels_MODEL2405300001_Infant_Gut_HMO_SynCom.yaml", "Bacteroides ovatus"),
        ("KBase_ORT_Workflow_Community_Model.yaml", "Nitrospiraceae bacterium"),
    ]:
        doc = yaml.safe_load((REPO / "kb/communities" / record).read_text())
        terms = {t.get("preferred_term"): t for _, t in _taxon_terms(doc)}
        assert terms[preferred].get("gtdb_grounding_status") == "WITHHELD"

    # And the neighbours sharing those ids must be unaffected.
    doc = yaml.safe_load(
        (REPO / "kb/communities/BioModels_MODEL2405300001_Infant_Gut_HMO_SynCom.yaml").read_text()
    )
    siblings = [
        t
        for _, t in _taxon_terms(doc)
        if (t.get("term") or {}).get("id") == "NCBITaxon:821"
        and t.get("preferred_term") != "Bacteroides ovatus"
    ]
    assert siblings, "expected another entry on NCBITaxon:821 in this record"
    for term_block in siblings:
        assert (
            term_block.get("gtdb_grounding_status") == "GROUNDED"
        ), "a correct grounding sharing the withheld id was marked WITHHELD"
