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
        lambda path, doc, text: (calls.append(path), real(path, doc, text))[1],
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
