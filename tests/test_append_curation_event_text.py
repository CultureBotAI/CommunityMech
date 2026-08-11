"""The text-append curation helper, outside its original caller (#526).

`_append_curation_event` was written inside `scripts/gtdb_ground.py` for #395 and
is the only code in the repo that can add a `CurationEvent` to a record **without
a YAML round-trip**. That matters because the nine writers #325 lists as owing a
trace are line editors — `splitlines()`, regex, `write_text` — deliberately, since
re-dumping would reflow every record they touch.

Nine copies of it would be nine chances to re-hit what it already knows:

* `- timestamp:` starts at column 0, so a naive "next top-level key" scan treats
  the history's own first item as the next section and inserts the event **above**
  the existing history;
* `curation_history: []` is the same key as `curation_history:`, and matching only
  the bare string appends a *second* one, which PyYAML resolves by keeping the
  last — silently dropping the existing history;
* a comment block before the next key belongs to that key, not to the history.

So it moved to `communitymech.curate.curation_event`. These tests exercise it
**as a library**, with a curator that is not `gtdb_ground.py` — the case the
existing `tests/test_gtdb_curation_history.py` cannot reach, since it only ever
calls through the original caller.

One deliberate behaviour change: the library raises `ValueError` where the script
raised `SystemExit`. A helper that exits the process cannot be used by anything
with its own error handling, which is the point of lifting it. `gtdb_ground.py`
converts at its own boundary, so its CLI behaviour and message are unchanged.
"""

from __future__ import annotations

import pathlib
import subprocess
import sys

import pytest
import yaml

from communitymech.curate.curation_event import append_curation_event_text

REPO = pathlib.Path(__file__).parent.parent

_MINIMAL = """id: CommunityMech:000999
name: helper test record
description: a record with no curation history
"""

_WITH_HISTORY = """id: CommunityMech:000999
name: helper test record
curation_history:
- timestamp: '2026-01-01T00:00:00Z'
  curator: someone
  action: FIRST
  changes: the pre-existing event
description: a key after the history
"""


def _appended(text: str, **kwargs) -> list[dict]:
    result = append_curation_event_text(
        text, curator="a_test", action="TEST_ACTION", changes="what changed", **kwargs
    )
    return yaml.safe_load(result)["curation_history"]


def test_it_creates_the_block_when_there_is_none():
    events = _appended(_MINIMAL)
    assert len(events) == 1
    assert events[0]["curator"] == "a_test"
    assert events[0]["action"] == "TEST_ACTION"


def test_the_rest_of_the_document_is_untouched():
    """A line editor's whole reason for existing."""
    result = append_curation_event_text(
        _MINIMAL, curator="a_test", action="TEST_ACTION", changes="what changed"
    )
    assert result.startswith(_MINIMAL.rstrip("\n"))


def test_it_appends_after_an_existing_event_not_before_it():
    """The column-0 trap: `- timestamp:` is not the next top-level key."""
    events = _appended(_WITH_HISTORY)
    assert [event["action"] for event in events] == ["FIRST", "TEST_ACTION"], (
        "the new event was inserted above the existing history, which the "
        "append-only write guard in gtdb_ground correctly refuses (#395)"
    )


def test_a_key_after_the_history_survives():
    result = append_curation_event_text(
        _WITH_HISTORY, curator="a_test", action="TEST_ACTION", changes="what changed"
    )
    document = yaml.safe_load(result)
    assert document["description"] == "a key after the history"


def test_an_empty_inline_list_becomes_a_block_rather_than_a_second_key():
    """`curation_history: []` is the same key; appending a second one is lossy."""
    text = "id: CommunityMech:000999\ncuration_history: []\nname: x\n"
    result = append_curation_event_text(
        text, curator="a_test", action="TEST_ACTION", changes="what changed"
    )
    assert result.count("curation_history:") == 1
    assert len(yaml.safe_load(result)["curation_history"]) == 1


def test_a_non_empty_inline_value_is_refused_rather_than_mangled():
    text = "id: CommunityMech:000999\ncuration_history: [{a: 1}]\nname: x\n"
    with pytest.raises(ValueError, match="inline curation_history"):
        append_curation_event_text(
            text, curator="a_test", action="TEST_ACTION", changes="what changed"
        )


def test_document_markers_are_refused():
    """Appending past a `...` would put the key outside the document."""
    text = _MINIMAL + "...\n"
    with pytest.raises(ValueError, match="document markers"):
        append_curation_event_text(
            text, curator="a_test", action="TEST_ACTION", changes="what changed"
        )


def test_it_raises_rather_than_exiting():
    """The reason for the lift, asserted directly.

    `SystemExit` does not inherit from `Exception`, so a caller with
    `except Exception` would not catch the old behaviour — it would take the
    process down mid-sweep.
    """
    text = "id: x\ncuration_history: [{a: 1}]\n"
    with pytest.raises(ValueError):
        append_curation_event_text(text, curator="c", action="A", changes="c")


def test_the_curator_is_not_hardcoded_to_gtdb_ground():
    """It was, in the original. Everything above would pass if it still were."""
    events = _appended(_MINIMAL)
    assert events[0]["curator"] == "a_test"


def test_a_wired_line_editor_actually_writes_the_event_to_disk(tmp_path):
    """End-to-end through `drop_obsolete_go_bp.py`, the first writer wired (#325).

    The corpus has no droppable annotations left, so a dry run against it
    reports zero and proves nothing — exactly the shape of canary that passes
    while persisting nothing. This builds a record that *does* have one, runs
    the script in a temporary tree the way the batch would, and reads the file
    back off disk.
    """
    communities = tmp_path / "kb/communities"
    communities.mkdir(parents=True)
    (communities / "r.yaml").write_text(
        "id: CommunityMech:000999\n"
        "name: droppable\n"
        "taxonomy:\n"
        "- taxon_term:\n"
        "    preferred_term: Escherichia coli\n"
        "  biological_processes:\n"
        "  - preferred_term: oxidation-reduction process\n"
        "    term:\n"
        "      id: GO:0016491\n"
        "      label: oxidoreductase activity\n",
        encoding="utf-8",
    )
    result = subprocess.run(
        [sys.executable, str(REPO / "scripts/drop_obsolete_go_bp.py")],
        capture_output=True,
        text=True,
        cwd=tmp_path,
        timeout=600,
    )
    assert result.returncode == 0, result.stderr[-500:]

    document = yaml.safe_load((communities / "r.yaml").read_text(encoding="utf-8"))
    history = document.get("curation_history") or []
    assert len(history) == 1, (
        f"the script edited the record but left no trace on disk: {result.stdout!r}. "
        f"A write that reports success and persists nothing is the failure this "
        f"repo keeps finding (#325)."
    )
    assert history[0]["curator"] == "drop_obsolete_go_bp.py"
    assert history[0]["action"] == "DROP_OBSOLETE_GO_BP"
