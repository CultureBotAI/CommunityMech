"""The middle of `gtdb_lineage`, which nothing checked until #454.

The freshness checks compare `gtdb_id`, `gtdb_taxon` and the lineage's *tail*;
the prokaryote-only gate (#365) reads its *head*. A segment corrupted in
between passed every gate and the whole suite:

    d__Bacteria;p__Bacteroidota;c__Chlorobiia
    d__Archaea;p__Nonsense;c__Chlorobiia        <- indistinguishable

That was tolerable while `gtdb_ground.py` wrote every lineage from the
crosswalk. #450 made seven of them hand-written curator pins, so it stopped
being theoretical — and the review that found it could only find it by asking
the crosswalk, which CI has no checkout of.

Both checks here are corpus-internal and need no mapping, which is what lets
them run in CI: ranks must be prefixed and get finer left to right, and — since
GTDB is a hierarchy — a taxon must sit under exactly one parent path across
every record that mentions it.
"""

from __future__ import annotations

import pathlib

import pytest
import yaml

from communitymech.validators.gtdb_lineage_tree import check_corpus, check_lineage_shape

REPO = pathlib.Path(__file__).parent.parent
RECORD_DIRS = ("kb/communities", "data/isolates")


def _doc(lineage) -> dict:
    return {
        "taxonomy": [
            {
                "taxon_term": {
                    "preferred_term": "X",
                    "gtdb_classification": {"gtdb_lineage": lineage},
                }
            }
        ]
    }


@pytest.mark.parametrize(
    ("label", "lineage"),
    [
        ("ranks out of order", "d__Bacteria;c__Chlorobiia;p__Bacteroidota"),
        ("a repeated rank", "d__Bacteria;p__Bacteroidota;p__Chlorobiota"),
        ("a segment with no rank prefix", "Bacteria;p__Bacteroidota"),
        ("an unknown rank prefix", "d__Bacteria;x__Bacteroidota"),
    ],
)
def test_a_malformed_lineage_is_reported(label, lineage):
    assert check_lineage_shape(_doc(lineage)), label


@pytest.mark.parametrize(
    ("label", "lineage"),
    [
        (
            "a full species lineage",
            "d__Bacteria;p__Bacteroidota;c__Chlorobiia;o__x;f__y;g__z;s__z a",
        ),
        ("a domain-only lineage", "d__Bacteria"),
        ("a curated class pin", "d__Bacteria;p__Bacteroidota;c__Chlorobiia"),
        # Not a lineage at all, and must not raise: `gtdb_lineage` has no
        # `range` in the schema, so these are all schema-valid (#429, #438).
        ("a list", ["d__Bacteria", "p__x"]),
        ("nothing", None),
        ("an empty string", ""),
    ],
)
def test_a_well_formed_or_unusable_lineage_is_silent(label, lineage):
    assert check_lineage_shape(_doc(lineage)) == [], label


def test_malformed_records_do_not_raise():
    """An exception here would abort validate-strict and lose every file."""
    for document in ({"taxonomy": [None]}, {"taxonomy": "x"}, "nonsense", None, {}):
        assert check_lineage_shape(document) == []
        assert check_corpus([("a.yaml", document)]) == []


def test_the_corruption_that_prompted_this_is_caught():
    """The exact edit that passed every other gate."""
    problems = check_corpus(
        [
            ("good.yaml", _doc("d__Bacteria;p__Bacteroidota;c__Chlorobiia")),
            ("bad.yaml", _doc("d__Archaea;p__Nonsense;c__Chlorobiia")),
        ]
    )
    assert len(problems) == 1, problems
    assert "c__Chlorobiia" in problems[0]
    assert "good.yaml" in problems[0] and "bad.yaml" in problems[0]


def test_one_taxon_under_one_parent_is_silent():
    """The same taxon in many records is the normal case, not a conflict."""
    lineage = "d__Bacteria;p__Bacteroidota;c__Chlorobiia"
    assert check_corpus([(f"r{n}.yaml", _doc(lineage)) for n in range(5)]) == []


def _corpus():
    for directory in RECORD_DIRS:
        for path in sorted((REPO / directory).glob("*.yaml")):
            yield path.name, yaml.safe_load(path.read_text())


def test_the_committed_kb_is_a_consistent_hierarchy():
    corpus = list(_corpus())
    blocks = sum(1 for _, doc in corpus for _ in (doc.get("taxonomy") or []) if _)
    assert len(corpus) > 300, f"expected the KB, read {len(corpus)} records"
    assert blocks > 300, "expected the KB's taxonomy entries"

    conflicts = check_corpus(corpus)
    assert conflicts == [], "\n".join(conflicts)

    shape = [f"{name}: {m}" for name, doc in corpus for m in check_lineage_shape(doc)]
    assert shape == [], "\n".join(shape)
