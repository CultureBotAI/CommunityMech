"""Every tool that edits a record either leaves a trace or says why not (#325).

#325 counted `curation_history` on **2 of 311** records and read it as a
coverage gap. That framing does not survive looking at the two entries: both
record a cross-reference between two ANME/SRB records — "these describe the same
community type from different studies, candidates for consolidation" — which is
a fact about the corpus that git cannot express and no other field carries.

`curation_history` is an **event log, not a coverage metric**. A record that has
had no such event correctly has none, and backfilling 310 records would mean
inventing events. That is why the QC threshold is 0.0: not a capitulation, a
category correction.

The real gap is on the writing side, and it is measurable. `scripts/audit_writers.py`
finds **26 scripts that write record YAML, of which 16 append nothing**. A tool
that rewrites 300 records in place and leaves no trace is the thing #325 was
pointing at — the low record count is a symptom of it.

This file does not fix those 16. It stops the set growing silently, and splits
it into the two groups the fix applies to differently:

* **exempt** — writes something that is not a curated record (`research/`,
  `data/ingredients/`), or creates records rather than editing them, where git
  already shows everything.
* **owed** — edits existing `kb/communities` records in place and should append
  an event. Named individually so the backlog is itemised rather than implied.

A new writer in neither list fails, which forces the decision when the tool is
written instead of in the next audit.
"""

from __future__ import annotations

import csv
import pathlib
import subprocess

import pytest

REPO = pathlib.Path(__file__).parent.parent

# Writes YAML, but not a curated community record — so there is no record whose
# history it could belong to.
_EXEMPT = {
    "scripts/enrich_edison_response.py": "writes research/communities, not kb records",
    "scripts/research_community_edison.py": "writes research/communities, not kb records",
    "scripts/suggest_related_ingredients.py": "writes data/ingredients, not kb records",
    "scripts/scout_communities.py": (
        "creates new records rather than editing existing ones; a creation is "
        "fully visible in git, which is not true of an in-place edit"
    ),
    "src/communitymech/validation/write_validated.py": (
        "the shared validated-write helper — it writes on behalf of a caller, "
        "and the event belongs to the operation, not to the mechanism"
    ),
    "src/communitymech/network/batch_reporter.py": (
        "drives llm_repair, which records the event itself (llm_repair.py:244); "
        "recording here too would double-log every repair"
    ),
    "src/communitymech/cli.py": (
        "dispatcher — the commands it invokes carry their own events, and an "
        "event recorded here would name the CLI rather than the operation"
    ),
}

# Edits existing kb/communities records in place and appends nothing. Each is
# work, not a decision: the trace is owed. Listed so the number is itemised
# rather than a headline, and so a fix removes a line here.
_OWED = {
    "scripts/apply_strain_designations.py",
    "scripts/apply_taxonomy_corrections.py",
    "scripts/backfill_metals.py",
    "scripts/chebi_fix_apply.py",
    "scripts/fix_reference_formats.py",
    "scripts/suggest_related_media.py",
    "scripts/term_fix_apply.py",
    "scripts/term_remap.py",
}


@pytest.fixture(scope="module")
def audit() -> list[dict[str, str]]:
    """The audit's own output, not a reimplementation of it.

    Re-deriving "does this write YAML" in the test would give two answers to one
    question, and the one that drifts is the one nobody runs.
    """
    result = subprocess.run(
        ["uv", "run", "python", "scripts/audit_writers.py"],
        capture_output=True,
        text=True,
        cwd=REPO,
        timeout=900,
    )
    assert result.returncode == 0, result.stderr[-500:]
    return list(csv.DictReader(result.stdout.splitlines(), delimiter="\t"))


def test_the_audit_sees_the_writers(audit):
    """Guard: an audit returning nothing makes every check below vacuous."""
    writers = [row for row in audit if row["writes_yaml"] == "yes"]
    assert len(writers) >= 20, f"only {len(writers)} YAML writers found; audit_writers.py broke"


def test_every_writer_is_classified(audit):
    """A new tool must say whether it owes a trace, when it is written."""
    unclassified = sorted(
        row["path"]
        for row in audit
        if row["writes_yaml"] == "yes"
        and row["appends_curation_history"] == "no"
        and row["path"] not in _EXEMPT
        and row["path"] not in _OWED
    )
    assert unclassified == [], (
        "these write record YAML and append no curation event, and are in "
        "neither list:\n"
        + "\n".join(f"  {path}" for path in unclassified)
        + "\n\nAdd `record_curation_event(...)`, or classify it: `_EXEMPT` "
        "with a reason if it does not touch kb/communities, `_OWED` if it "
        "does and the trace is simply not written yet (#325)."
    )


def test_neither_list_has_rotted(audit):
    """A tool that gained a trace must leave `_OWED`, or the list is a fiction."""
    appending = {row["path"] for row in audit if row["appends_curation_history"] == "yes"}
    fixed = sorted(_OWED & appending)
    assert fixed == [], f"these now append a curation event and should come out of _OWED: {fixed}"

    known = {row["path"] for row in audit}
    gone = sorted((set(_EXEMPT) | _OWED) - known)
    assert gone == [], f"these are classified but the audit no longer sees them: {gone}"


def test_the_exemptions_have_reasons():
    """An allow-list without reasons is how the next one gets waved through."""
    blank = sorted(path for path, why in _EXEMPT.items() if not (why or "").strip())
    assert blank == [], f"exemptions need a reason: {blank}"
    assert not (set(_EXEMPT) & _OWED), "a writer cannot be both exempt and owed"


def test_the_owed_backlog_has_not_grown(audit):
    """#325's real number, bounded.

    16 of 26 writers appended nothing when this was measured: 9 owed and 7
    exempt. `drop_obsolete_go_bp.py` was wired in #526, leaving 8. The point of
    a bound is that adding a ninth back is a decision someone makes on purpose,
    not a drift.
    """
    assert len(_OWED) <= 8, (
        f"{len(_OWED)} writers now owe a curation trace, up from 9. Adding one "
        f"is a choice worth defending — the alternative is calling "
        f"`record_curation_event` in the new tool (#325)."
    )


def test_the_two_records_that_do_have_history_are_event_logs_not_stubs():
    """The evidence for the reframing above, asserted rather than assumed.

    If these ever become empty or auto-generated boilerplate, the argument that
    `curation_history` records what git cannot stops holding, and the 0.0 QC
    threshold would need revisiting.
    """
    import yaml

    with_history = {
        path.name: (yaml.safe_load(path.read_text(encoding="utf-8")) or {}).get("curation_history")
        for path in sorted((REPO / "kb/communities").glob("*.yaml"))
    }
    populated = {name: events for name, events in with_history.items() if events}
    assert populated, "no record carries curation_history; the reframing needs re-checking"
    for name, events in populated.items():
        for event in events:
            assert event.get("action"), f"{name}: a curation event with no action"
            assert len((event.get("changes") or "").split()) >= 5, (
                f"{name}: a curation event whose `changes` says almost nothing — "
                f"an event log of stubs is the coverage metric #325 mistook this for"
            )
