"""`--refresh` must replace grounding blocks and change nothing else (#378).

`gtdb_ground.py --apply` skips taxa that already carry a `gtdb_classification`,
so there was no supported way to re-ground the KB — which any mapping-release
bump requires, and which flipping a denominator or filter default requires too.

Four hand-rolled attempts at this edit corrupted records: one deleted a sibling
`evidence` list and a PMID reference, one dropped a newline and joined two lines,
one emitted duplicate `gtdb_classification` keys across 11 records, and one
grounded taxa that are withheld on purpose (#292). Each was caught only by
inspecting afterwards.

So the two invariants are enforced in the code, not by the caller:

* **refresh only, never create** — an ungrounded taxon stays ungrounded, because
  it may be ungrounded deliberately;
* **a structural gate before the write** — parse the result and refuse unless the
  only difference is inside `gtdb_classification`.
"""

import importlib.util
import re
import shutil
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).parent.parent
SAMPLE = REPO / "kb/communities/Lake_Washington_Methane_Oxygen_Methylotroph_Community.yaml"


@pytest.fixture(scope="module")
def gtdb():
    spec = importlib.util.spec_from_file_location("gtdb_ground", REPO / "scripts/gtdb_ground.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def rows(gtdb):
    try:
        mapping = gtdb.resolve_kg_microbe_dir(None) / "data/raw/NCBI2GTDB.tsv.gz"
    except SystemExit as exc:
        pytest.skip(f"kg-microbe mapping unavailable: {str(exc).splitlines()[0]}")
    if not mapping.exists():
        pytest.skip("kg-microbe NCBI2GTDB mapping not available")
    doc = yaml.safe_load(SAMPLE.read_text())
    pairs = [
        (
            (e["taxon_term"].get("term") or {}).get("id", ""),
            (e["taxon_term"].get("term") or {}).get("label", ""),
        )
        for e in doc["taxonomy"]
    ]
    cleaned = [gtdb._clean_label(lb) for _, lb in pairs]
    return gtdb.collect_rows(
        mapping,
        {i.split(":")[1] for i, _ in pairs if i},
        {c.lower() for c in cleaned if " " in c},
        {c.lower() for c in cleaned if " " not in c},
    )


@pytest.fixture
def record(tmp_path):
    dest = tmp_path / SAMPLE.name
    shutil.copy(SAMPLE, dest)
    return dest


def test_refresh_replaces_blocks_without_duplicating_the_key(gtdb, rows, record):
    before = yaml.safe_load(record.read_text())
    n = gtdb.apply_to_community(record, *rows, "test-source", refresh=True)
    after = yaml.safe_load(record.read_text())

    assert n > 0, "expected some blocks to be refreshed"
    grounded = sum(
        1 for e in after["taxonomy"] if (e.get("taxon_term") or {}).get("gtdb_classification")
    )
    assert record.read_text().count("gtdb_classification:") == grounded
    assert len(after["taxonomy"]) == len(before["taxonomy"])


def _grounded_ids(path):
    return {
        (e["taxon_term"].get("term") or {}).get("id")
        for e in yaml.safe_load(path.read_text())["taxonomy"]
        if (e.get("taxon_term") or {}).get("gtdb_classification")
    }


def test_refresh_creates_no_new_groundings(gtdb, rows, record):
    """The withheld set (#292) depends on this asymmetry.

    One block is removed first, so the record contains a taxon that is
    ungrounded *and* groundable — otherwise there is nothing for a
    creates-anyway bug to create, and the test passes vacuously.
    """
    text = record.read_text()
    start = text.index("    gtdb_classification:")
    end = start + len("    gtdb_classification:\n")
    while end < len(text):
        line_end = text.index("\n", end) + 1
        if not text[end:line_end].startswith("      "):
            break
        end = line_end
    record.write_text(text[:start] + text[end:])

    before = _grounded_ids(record)
    assert len(before) >= 1

    gtdb.apply_to_community(record, *rows, "test-source", refresh=True)

    assert _grounded_ids(record) == before, (
        "refresh grounded a taxon that had no block — an ungrounded taxon may be "
        "ungrounded deliberately (#292)"
    )


def test_the_gate_runs_on_every_write(gtdb, rows, record, monkeypatch):
    """Removing the gate must not go unnoticed.

    It never fires on a correct edit, so nothing else here exercises it.
    """
    calls = []
    real = gtdb._assert_only_grounding_changed
    monkeypatch.setattr(
        gtdb,
        "_assert_only_grounding_changed",
        lambda path, doc, text, **kw: (calls.append(path), real(path, doc, text, **kw))[1],
    )

    gtdb.apply_to_community(record, *rows, "test-source", refresh=True)

    assert calls, "apply_to_community wrote without running the structural gate"


def test_refresh_preserves_everything_outside_the_grounding(gtdb, rows, record):
    before = yaml.safe_load(record.read_text())
    gtdb.apply_to_community(record, *rows, "test-source", refresh=True)
    after = yaml.safe_load(record.read_text())

    assert {k: v for k, v in before.items() if k != "taxonomy"} == {
        k: v for k, v in after.items() if k != "taxonomy"
    }
    for b, a in zip(before["taxonomy"], after["taxonomy"], strict=True):
        bt, at = dict(b["taxon_term"]), dict(a["taxon_term"])
        bt.pop("gtdb_classification", None)
        at.pop("gtdb_classification", None)
        assert bt == at, "a taxon_term changed outside its grounding block"
        assert {k: v for k, v in b.items() if k != "taxon_term"} == {
            k: v for k, v in a.items() if k != "taxon_term"
        }


def test_without_refresh_existing_blocks_are_left_alone(gtdb, rows, record):
    original = record.read_text()
    gtdb.apply_to_community(record, *rows, "test-source")
    assert record.read_text() == original, "default apply must not touch grounded taxa"


def test_the_gate_refuses_an_edit_that_drops_a_sibling(gtdb, record):
    """The failure that deleted `evidence` and a PMID reference."""
    doc = yaml.safe_load(record.read_text())
    broken = record.read_text().replace("  evidence:\n", "", 1)
    with pytest.raises(SystemExit, match="outside taxonomy|taxon_term|taxonomy entry"):
        gtdb._assert_only_grounding_changed(record, doc, broken)


def test_the_gate_refuses_a_duplicate_key(gtdb, record):
    """PyYAML keeps the last of two identical keys, so linkml-validate is blind."""
    doc = yaml.safe_load(record.read_text())
    dup = record.read_text().replace(
        "    gtdb_classification:\n",
        "    gtdb_classification:\n      x: 1\n    gtdb_classification:\n",
        1,
    )
    with pytest.raises(SystemExit, match="duplicate"):
        gtdb._assert_only_grounding_changed(record, doc, dup)


def test_the_gate_refuses_unparseable_output(gtdb, record):
    doc = yaml.safe_load(record.read_text())
    with pytest.raises(SystemExit, match="unparseable"):
        gtdb._assert_only_grounding_changed(record, doc, "taxonomy:\n  - : :\n bad: [\n")


# ---------------------------------------------------------------------------
# The shape that broke it: a wrapped scalar inside an existing block.
# ---------------------------------------------------------------------------


@pytest.fixture
def wrapped_record(tmp_path):
    """A record whose block carries a PyYAML line-wrap continuation.

    Built rather than borrowed. 13 KB records had this shape, pasted from the
    `--emit-yaml` path, which dumps at width ~100 while `--apply` uses 4096
    (#380) — but a refresh normalises them, so a fixture pointing at a real
    record stops testing anything the moment the KB is swept.

    Continuations sit deeper than the block keys, so a span matching *exactly*
    six spaces stopped short and orphaned them into duplicate keys.
    """
    source = REPO / "kb/communities/Lake_Washington_Methane_Oxygen_Methylotroph_Community.yaml"
    text = source.read_text()
    marker = "      mapping_source: "
    i = text.index(marker)
    eol = text.index("\n", i)
    cut = i + len(marker) + 40
    wrapped = text[i:cut] + "\n        " + text[cut:eol].strip()
    dest = tmp_path / source.name
    dest.write_text(text[:i] + wrapped + text[eol:])
    assert re.search(r"^        \S", dest.read_text(), re.M), "fixture lost its wrapped line"
    return dest


def test_refresh_of_a_wrapped_block_produces_no_duplicate_keys(gtdb, wrapped_record):
    doc = yaml.safe_load(wrapped_record.read_text())
    pairs = [
        (
            (e["taxon_term"].get("term") or {}).get("id", ""),
            (e["taxon_term"].get("term") or {}).get("label", ""),
        )
        for e in doc["taxonomy"]
    ]
    cleaned = [gtdb._clean_label(lb) for _, lb in pairs]
    try:
        mapping = gtdb.resolve_kg_microbe_dir(None) / "data/raw/NCBI2GTDB.tsv.gz"
    except SystemExit:
        pytest.skip("kg-microbe mapping unavailable")
    if not mapping.exists():
        pytest.skip("kg-microbe mapping unavailable")
    rows = gtdb.collect_rows(
        mapping,
        {i.split(":")[1] for i, _ in pairs if i},
        {c.lower() for c in cleaned if " " in c},
        {c.lower() for c in cleaned if " " not in c},
    )

    before = wrapped_record.read_text()
    written = gtdb.apply_to_community(wrapped_record, *rows, "test-source", refresh=True)

    text = wrapped_record.read_text()
    # Without these three, every assertion below passes on the *un-refreshed*
    # fixture — it already has 7 grounded blocks and one of each key, so a
    # regression making refresh a silent no-op would go undetected (#372 review).
    assert written, "refresh reported writing no blocks"
    assert text != before, "refresh left the file byte-identical — it did nothing"
    assert "test-source" in text, "the refreshed blocks do not carry the new mapping_source"

    after = yaml.safe_load(text)
    grounded = sum(
        1 for e in after["taxonomy"] if (e.get("taxon_term") or {}).get("gtdb_classification")
    )
    for key in ("ncbi_source_id", "majority_fraction", "mapping_source"):
        assert text.count(f"      {key}:") == grounded, f"duplicate {key} after refresh"


def test_span_covers_a_wrapped_continuation(gtdb, wrapped_record):
    """Unit-level: the span must run past a deeper-indented continuation line."""
    lines = wrapped_record.read_text().splitlines()
    # The anchor of the entry that actually carries the wrapped block — the
    # nearest `id:` line above it, not simply the first in the file.
    wrapped_at = next(i for i, ln in enumerate(lines) if re.match(r"^\s{8,}\S", ln))
    anchor = max(i for i in range(wrapped_at) if re.match(r"^\s+id: NCBITaxon:\d+\s*$", lines[i]))
    span = gtdb._block_span(lines, anchor, len(lines))
    assert span, "expected a block for this entry"
    assert not re.match(
        r"^\s{6,}\S", lines[span[1]]
    ), "span ended while the block was still going — a wrapped line was orphaned"


# ---------------------------------------------------------------------------
# The gate's per-entry checks. The document-level check alone satisfied the
# earlier sibling test, so removing any of these passed (#378 review).
# ---------------------------------------------------------------------------


def test_the_gate_refuses_a_changed_taxon_term_sibling(gtdb, record):
    doc = yaml.safe_load(record.read_text())
    broken = record.read_text().replace("    notes:", "    notes_RENAMED:", 1)
    with pytest.raises(SystemExit, match="taxon_term changed"):
        gtdb._assert_only_grounding_changed(record, doc, broken)


def test_the_gate_refuses_a_changed_entry_level_sibling(gtdb, record):
    """A key beside `taxon_term` on a taxonomy entry — `evidence`, `notes`."""
    doc = yaml.safe_load(record.read_text())
    after = yaml.safe_load(record.read_text())
    target = next(e for e in after["taxonomy"] if "evidence" in e)
    target["evidence"] = []
    with pytest.raises(SystemExit, match="outside taxon_term"):
        gtdb._assert_only_grounding_changed(record, doc, yaml.dump(after, sort_keys=False))


def test_the_gate_refuses_a_dropped_taxonomy_entry(gtdb, record):
    doc = yaml.safe_load(record.read_text())
    after = yaml.safe_load(record.read_text())
    after["taxonomy"] = after["taxonomy"][:-1]
    with pytest.raises(SystemExit, match="taxonomy went from|was dropped"):
        gtdb._assert_only_grounding_changed(record, doc, yaml.dump(after, sort_keys=False))


def test_the_gate_refuses_a_dropped_grounding_on_refresh(gtdb, record):
    """A span that swallowed a block would otherwise be written silently."""
    doc = yaml.safe_load(record.read_text())
    after = yaml.safe_load(record.read_text())
    for entry in after["taxonomy"]:
        if (entry.get("taxon_term") or {}).pop("gtdb_classification", None):
            break
    with pytest.raises(SystemExit, match="set of grounded taxa changed"):
        gtdb._assert_only_grounding_changed(
            record, doc, yaml.dump(after, sort_keys=False), refresh=True
        )
