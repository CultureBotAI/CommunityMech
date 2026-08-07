"""A withdrawn grounding survived only in git (#395).

`just audit-writers` reported `scripts/gtdb_ground.py` as the one YAML-writing
module with no `record_curation_event` append. So when #394 withdrew
`NCBITaxon:429` *Methylobacter* (`g__Methylobacter_A`, 0.662) and
`NCBITaxon:613` *Serratia* (`g__Serratia`, 0.519), those values left the records
entirely. `gtdb_grounding_status: AMBIGUOUS` says the tool is unsure *now*; it
does not say a grounding was once stored, or what it was.

That matters most for *Serratia*, where #373/#374 argue the withdrawn answer may
have been the better one — its grounding was type-anchored, and the recompute
that removed it was a raw majority. A curator revisiting the decision had to
read git to find out what had been taken away.

All three write paths now append a `CurationEvent`, and the withdrawal records
**the value**, not merely the fact:

    Withdrew 1 GTDB grounding(s) the recompute now calls AMBIGUOUS:
    Methylobacter was GTDB:g__Methylobacter_A @0.662 (#382, #395).

The append is text-level, because every write path here is a line-level editor —
a YAML round-trip would reformat the whole record, which is the corruption class
`_assert_only_grounding_changed` exists to prevent (#378). Both write guards
were widened by exactly one thing: `curation_history` may gain one entry at the
end. That narrowness is the point, and it earned its keep immediately — the
first version of the insertion scanned for the next line starting at column 0 to
find the end of the block, which matched the list's own `- timestamp:` item and
inserted the event ABOVE the existing history. The guard refused the write.
"""

from __future__ import annotations

import importlib.util
import re
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).parent.parent

# One line in the fixture, split here only to stay inside the 100-column lint.
LINEAGE = (
    "d__Bacteria;p__Pseudomonadota;c__Gammaproteobacteria;o__Methylococcales;"
    "f__Methylomonadaceae;g__Methylobacter_A"
)

PROBE = """id: CommunityMech:TEST
name: withdraw probe
taxonomy:
- taxon_term:
    preferred_term: Methylobacter
    term:
      id: NCBITaxon:429
      label: Methylobacter
    gtdb_classification:
      gtdb_id: GTDB:g__Methylobacter_A
      gtdb_taxon: Methylobacter_A
      gtdb_lineage: {LINEAGE}
      ncbi_source_id: NCBITaxon:429
      majority_fraction: 0.662
      support_genomes: 43
      total_genomes: 65
      is_reclassified: true
      mapping_source: probe
""".replace("{LINEAGE}", LINEAGE)


@pytest.fixture(scope="module")
def gtdb():
    spec = importlib.util.spec_from_file_location("gtdb_ground", REPO / "scripts/gtdb_ground.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules["gtdb_ground"] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def mapping(gtdb):
    """Skip where the kg-microbe crosswalk is absent, CI included."""
    try:
        path = gtdb.resolve_kg_microbe_dir(None) / "data/raw/NCBI2GTDB.tsv.gz"
    except SystemExit as exc:
        pytest.skip(f"kg-microbe mapping unavailable: {str(exc).splitlines()[0]}")
    if not path.exists():
        pytest.skip(f"kg-microbe NCBI2GTDB mapping not available at {path}")
    return path


def _run(*args):
    return subprocess.run(
        ["uv", "run", "python", "scripts/gtdb_ground.py", *args],
        capture_output=True,
        text=True,
        cwd=REPO,
        timeout=1800,
    )


def _history(path: Path) -> list[dict]:
    return (yaml.safe_load(path.read_text()) or {}).get("curation_history") or []


def test_a_withdrawal_records_what_it_removed(gtdb, mapping, tmp_path):
    """The point of #395: the value must survive, not just the fact of removal."""
    record = tmp_path / "wd.yaml"
    record.write_text(PROBE)

    result = _run("--community", str(record), "--withdraw-ambiguous")
    assert result.returncode == 0, result.stderr[-500:]

    document = yaml.safe_load(record.read_text())
    assert "gtdb_classification" not in document["taxonomy"][0]["taxon_term"]

    events = _history(record)
    assert len(events) == 1, f"expected one curation event, got {events}"
    event = events[0]
    assert event["action"] == "GTDB_WITHDRAW_AMBIGUOUS"
    assert event["curator"] == "gtdb_ground.py"
    # The two facts a curator needs and would otherwise have to git-blame for.
    assert "GTDB:g__Methylobacter_A" in event["changes"]
    assert "0.662" in event["changes"]


def test_applying_a_grounding_records_it(gtdb, mapping, tmp_path):
    record = tmp_path / "apply.yaml"
    record.write_text(
        "id: CommunityMech:TEST\n"
        "name: probe\n"
        "taxonomy:\n"
        "- taxon_term:\n"
        "    preferred_term: Bosea\n"
        "    term:\n"
        "      id: NCBITaxon:85413\n"
        "      label: Bosea\n"
    )
    result = _run("--community", str(record), "--apply")
    assert result.returncode == 0, result.stderr[-500:]

    events = _history(record)
    assert [e["action"] for e in events] == ["GTDB_GROUND"]


def test_setting_status_records_it(gtdb, mapping, tmp_path):
    record = tmp_path / "status.yaml"
    record.write_text(PROBE)

    result = _run("--community", str(record), "--apply-status")
    assert result.returncode == 0, result.stderr[-500:]
    assert [e["action"] for e in _history(record)] == ["GTDB_SET_STATUS"]


def test_an_existing_history_is_preserved_and_appended_to(gtdb, mapping, tmp_path):
    """The bug the write guard caught: the event landed above the existing list.

    `curation_history:`'s own items start at column 0 (`- timestamp:`), so a
    scan for "the next line not starting with whitespace" finds the first item
    and treats it as the next top-level key.
    """
    source = REPO / "kb/communities/ANME_SRB_Anaerobic_Methanotrophic_Syntrophic_Consortia.yaml"
    original = _history(source)
    assert original, "this fixture needs a record that already has curation_history"

    # Strip the statuses so the run has something to do. Without this the edit
    # is a no-op, no event is appended, and the test fails for the right reason
    # but the wrong subject — it is the *insertion point* under test here, not
    # the no-op short-circuit.
    record = tmp_path / source.name
    record.write_text(
        "\n".join(
            line
            for line in source.read_text().splitlines()
            if not line.strip().startswith(("gtdb_grounding_status:", "gtdb_candidates:"))
            and not re.match(r"^\s+- GTDB:", line)
        )
        + "\n"
    )
    assert _history(record), "history must survive the strip"

    result = _run("--community", str(record), "--apply-status")
    assert result.returncode == 0, result.stderr[-500:]

    events = _history(record)
    assert len(events) == len(original) + 1
    assert events[: len(original)] == original, "existing events must be untouched"
    assert events[-1]["action"] == "GTDB_SET_STATUS", "the new event goes last"


def test_the_write_guard_refuses_a_rewrite_of_existing_history(gtdb):
    """The exemption is append-only, and narrow on purpose.

    Called directly: no write path should be able to produce this, which is
    exactly why the guard should still refuse it.
    """
    before = {"taxonomy": [], "curation_history": [{"action": "KEEP"}]}
    rewritten = yaml.safe_dump(
        {"taxonomy": [], "curation_history": [{"action": "CLOBBERED"}, {"action": "NEW"}]}
    )
    with pytest.raises(SystemExit, match="may only append"):
        gtdb._assert_only_grounding_changed(
            Path("probe.yaml"), before, rewritten, curation_event=True
        )


def test_the_write_guard_refuses_more_than_one_new_event(gtdb):
    before = {"taxonomy": [], "curation_history": [{"action": "KEEP"}]}
    two = yaml.safe_dump(
        {
            "taxonomy": [],
            "curation_history": [{"action": "KEEP"}, {"action": "A"}, {"action": "B"}],
        }
    )
    with pytest.raises(SystemExit, match="at most one new curation event"):
        gtdb._assert_only_grounding_changed(Path("probe.yaml"), before, two, curation_event=True)


def test_the_guard_still_refuses_unrelated_changes(gtdb):
    """Widening it for curation_history must not have opened anything else.

    The edit here is otherwise well-formed — it appends exactly one event — so
    the only thing left to refuse is the changed `name`. An earlier version of
    this test supplied no event at all and passed for the wrong reason: it
    tripped the "exactly one new curation event" check before reaching the one
    it meant to exercise.
    """
    before = {"taxonomy": [], "name": "before", "curation_history": [{"action": "KEEP"}]}
    changed = yaml.safe_dump(
        {
            "taxonomy": [],
            "name": "after",
            "curation_history": [{"action": "KEEP"}, {"action": "NEW"}],
        }
    )
    with pytest.raises(SystemExit, match="outside taxonomy changed"):
        gtdb._assert_only_grounding_changed(
            Path("probe.yaml"), before, changed, curation_event=True
        )


def test_the_guard_allows_no_event_when_nothing_changed(gtdb):
    """Zero is legitimate, and is what keeps `--apply-status` idempotent.

    Appending unconditionally made every re-run grow the history by an entry
    saying nothing happened, which broke the byte-idempotence the existing
    suite asserts and buries the real events.
    """
    before = {"taxonomy": [], "curation_history": [{"action": "KEEP"}]}
    unchanged = yaml.safe_dump({"taxonomy": [], "curation_history": [{"action": "KEEP"}]})
    gtdb._assert_only_grounding_changed(Path("probe.yaml"), before, unchanged, curation_event=True)


def test_the_writer_audit_now_sees_the_append():
    """`audit-writers` is what reported this gap; it should stop reporting it."""
    result = subprocess.run(
        ["uv", "run", "python", "scripts/audit_writers.py"],
        capture_output=True,
        text=True,
        cwd=REPO,
        timeout=600,
    )
    row = [line for line in result.stdout.splitlines() if line.startswith("scripts/gtdb_ground.py")]
    assert row, f"gtdb_ground.py is missing from the writer audit:\n{result.stdout[:400]}"
    # By column, not by substring: `"\tno\t" not in row` cannot see a `no` in the
    # LAST field, which has no trailing tab, and says nothing if the audit
    # reorders its columns (review of #483).
    fields = row[0].split("\t")
    assert len(fields) >= 3, f"the audit's row format changed: {row[0]!r}"
    assert fields[2] == "yes", (
        f"audit-writers reports gtdb_ground.py still has no curation_history "
        f"append: {row[0]} (#395)"
    )
    assert (
        "no" not in fields[1:]
    ), f"audit-writers reports another missing safeguard for gtdb_ground.py: {row[0]}"


# ---------------------------------------------------------------------------
# Pure-text tests for the insertion itself. These need NO crosswalk, so unlike
# the end-to-end tests above they actually run in CI — where the four
# `mapping`-dependent ones skip, leaving the one piece of genuinely new,
# edge-case-prone logic exercised only on the author's machine (review of #483).
# ---------------------------------------------------------------------------


def _appended(gtdb, text: str) -> dict:
    out = gtdb._append_curation_event(text, action="GTDB_SET_STATUS", changes="probe")
    return yaml.safe_load(out)


def test_a_record_with_no_history_gains_the_key(gtdb):
    doc = _appended(gtdb, "id: X\nname: probe\n")
    assert [e["action"] for e in doc["curation_history"]] == ["GTDB_SET_STATUS"]
    assert doc["name"] == "probe"


def test_an_empty_inline_list_is_not_duplicated(gtdb):
    """`curation_history: []` is the same key.

    Matching only the bare string appended a SECOND `curation_history:`, and
    PyYAML keeps the last of two identical keys — silently dropping whatever
    the first held. The write guard caught it, but producing corruption and
    relying on the guard is the wrong order.
    """
    out = gtdb._append_curation_event(
        "id: X\ncuration_history: []\nname: probe\n", action="GTDB_GROUND", changes="probe"
    )
    assert out.count("curation_history:") == 1, out
    assert [e["action"] for e in yaml.safe_load(out)["curation_history"]] == ["GTDB_GROUND"]


def test_a_trailing_comment_on_the_key_is_handled(gtdb):
    out = gtdb._append_curation_event(
        "id: X\ncuration_history:  # notes follow\n- action: KEEP\nname: probe\n",
        action="GTDB_GROUND",
        changes="probe",
    )
    assert out.count("curation_history:") == 1
    assert [e["action"] for e in yaml.safe_load(out)["curation_history"]] == [
        "KEEP",
        "GTDB_GROUND",
    ]


def test_an_indented_sequence_stays_parseable(gtdb):
    """A column-0 item cannot be appended to an indented sequence."""
    doc = _appended(gtdb, "id: X\ncuration_history:\n  - action: KEEP\nname: probe\n")
    assert [e["action"] for e in doc["curation_history"]] == ["KEEP", "GTDB_SET_STATUS"]


def test_the_event_goes_last_not_first(gtdb):
    """The bug the append-only write guard caught."""
    doc = _appended(gtdb, "id: X\ncuration_history:\n- action: FIRST\n- action: SECOND\n")
    assert [e["action"] for e in doc["curation_history"]] == [
        "FIRST",
        "SECOND",
        "GTDB_SET_STATUS",
    ]


def test_a_comment_introducing_the_next_key_is_not_absorbed(gtdb):
    """Inserting below it would silently re-attach the comment to the history."""
    out = gtdb._append_curation_event(
        "id: X\ncuration_history:\n- action: KEEP\n# about the name\nname: probe\n",
        action="GTDB_GROUND",
        changes="probe",
    )
    lines = out.splitlines()
    assert lines.index("# about the name") > lines.index("  action: GTDB_GROUND")
    assert [e["action"] for e in yaml.safe_load(out)["curation_history"]] == ["KEEP", "GTDB_GROUND"]


def test_a_document_end_marker_is_refused_rather_than_corrupted(gtdb):
    with pytest.raises(SystemExit, match="document markers"):
        gtdb._append_curation_event("id: X\nname: probe\n...\n", action="A", changes="b")


def test_a_missing_trailing_newline_is_not_a_change(gtdb):
    """Byte comparison called this a change and earned a false event.

    The callers rebuild text with `splitlines()` + `"\\n".join(...) + "\\n"`, so a
    file without a trailing newline is never byte-equal to its own rewrite.
    """
    assert gtdb._semantically_equal("id: X\nname: probe", "id: X\nname: probe\n")
    assert (
        gtdb._record_edit("id: X\nname: probe", "id: X\nname: probe\n", action="A", changes="b")
        == "id: X\nname: probe\n"
    )


def test_the_event_counts_entries_that_actually_differ(gtdb):
    """`{n}` must not restate how many entries the line editor visited."""
    before = "taxonomy:\n- taxon_term: {a: 1}\n- taxon_term: {b: 2}\n"
    after = "taxonomy:\n- taxon_term: {a: 9}\n- taxon_term: {b: 2}\n"
    assert gtdb._changed_entries(before, after) == 1

    out = gtdb._record_edit(before, after, action="GTDB_GROUND", changes="changed {n} block(s)")
    assert "changed 1 block(s)" in out
