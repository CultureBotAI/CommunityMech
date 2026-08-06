"""A GTDB classification on a taxon GTDB cannot classify (#365).

Two records used `NCBITaxon:169215` — the *plant* genus *Bosea* (Amaranthaceae)
— for the alphaproteobacterium of the same name, and carried a GTDB block
reading `d__Bacteria;...;g__Bosea` derived from it. The KB asserted a plant was
a bacterium, in the field that looks most independently sourced.

Nothing could see it: `ncbi_source_id == term.id` (so #364's freshness test
passes), "Bosea" really is that id's label (so id<->label passes), and the id
appears once per record (so #292's shared-id gate has nothing to compare).

The signal needs no judgement: GTDB classifies prokaryotes only, so a eukaryote
or a virus can carry no GTDB block at all.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

import pytest
import yaml

import communitymech.validators.prokaryotic_lineage as module
from communitymech.validators.ncbi_domain import domain_of
from communitymech.validators.prokaryotic_lineage import check_record, lineage_domain

REPO = Path(__file__).parent.parent
BACTERIAL = "d__Bacteria;p__Pseudomonadota;c__Alphaproteobacteria;o__Rhizobiales"
ARCHAEAL = "d__Archaea;p__Methanobacteriota;c__Methanobacteria"

# The plant genus Bosea, and the bacterium NCBI renamed Allobosea.
PLANT_BOSEA = "NCBITaxon:169215"
BACTERIAL_BOSEA = "NCBITaxon:85413"


def _doc(curie: str, lineage: str | None, name: str = "x") -> dict:
    descriptor = {"preferred_term": name, "term": {"id": curie, "label": name}}
    if lineage is not None:
        descriptor["gtdb_classification"] = {"gtdb_lineage": lineage}
    return {"taxonomy": [{"taxon_term": descriptor}]}


def test_the_defect_that_prompted_this_is_caught():
    """#365, reconstructed: the plant Bosea carrying a bacterial lineage."""
    problems = check_record(_doc(PLANT_BOSEA, BACTERIAL, "Bosea sp."))

    assert len(problems) == 1, problems
    assert PLANT_BOSEA in problems[0]
    assert "eukaryote" in problems[0]


def test_a_block_on_a_eukaryote_is_caught_whatever_the_lineage_says():
    """The id alone settles it — GTDB models no eukaryotic lineage to compare."""
    assert len(check_record(_doc(PLANT_BOSEA, "", "Bosea sp."))) == 1
    empty_block = {
        "taxonomy": [
            {
                "taxon_term": {
                    "preferred_term": "Bosea sp.",
                    "term": {"id": PLANT_BOSEA, "label": "Bosea"},
                    "gtdb_classification": {"gtdb_id": "GTDB:g__Bosea"},
                }
            }
        ]
    }
    assert len(check_record(empty_block)) == 1


def test_the_corrected_id_is_accepted():
    """`NCBITaxon:85413` is the bacterium NCBI renamed Allobosea."""
    assert check_record(_doc(BACTERIAL_BOSEA, BACTERIAL, "Bosea sp.")) == []


def test_the_two_ids_really_are_what_the_fix_assumes():
    """The whole fix rests on these two lookups, so assert them directly."""
    assert domain_of(PLANT_BOSEA) == "NCBITaxon:2759", "169215 must be the plant"
    assert domain_of(BACTERIAL_BOSEA) == "NCBITaxon:2", "85413 must be the bacterium"


@pytest.mark.parametrize(
    ("label", "curie", "lineage"),
    [
        ("a bacterium under a bacterial lineage", "NCBITaxon:562", BACTERIAL),
        ("an archaeon under an archaeal lineage", "NCBITaxon:2172", ARCHAEAL),
        # Grounding at a high rank is normal and says nothing about domain.
        ("a domain-rank id", "NCBITaxon:2", "d__Bacteria"),
        ("no gtdb block on a eukaryote", PLANT_BOSEA, None),
    ],
)
def test_legitimate_cases_are_silent(label, curie, lineage):
    """These are silent because they are *right*, not because they are opaque."""
    assert check_record(_doc(curie, lineage)) == [], label


@pytest.mark.parametrize(
    ("label", "curie"),
    [
        ("an id newer than the local NCBITaxon snapshot", "NCBITaxon:99999999"),
        ("a non-NCBITaxon id", "GTDB:g__Bosea"),
        ("a taxon above every domain", "NCBITaxon:131567"),
    ],
)
def test_unjudgeable_ids_are_silent_and_really_are_unjudgeable(label, curie):
    """Separated from the legitimate cases, which they were conflated with (#440).

    Silence alone proves nothing here — these would also pass if `domain_of`
    were broken to return None for everything. Asserting that the domain is
    genuinely unresolvable is what makes the case meaningful.
    """
    assert domain_of(curie) is None, f"{label} should be unresolvable"
    assert check_record(_doc(curie, BACTERIAL)) == [], label


def test_an_archaeon_under_a_bacterial_lineage_is_not_flagged():
    """The arm that used to fire here was removed, and the reason matters (#437).

    NCBI and GTDB *do* disagree about domain: 8 rows of this repo's own
    `NCBI2GTDB.tsv.gz` do, and the gate fired on every block `gtdb_ground.py`
    would build from them. A gate that rejects its own grounding tool's output
    is worse than none, so only the prokaryote-only rule — which has no
    counterexamples — survives.
    """
    assert check_record(_doc("NCBITaxon:2172", BACTERIAL, "Methanobrevibacter")) == []


@pytest.mark.parametrize(
    ("lineage", "expected"),
    [
        (BACTERIAL, "Bacteria"),
        (ARCHAEAL, "Archaea"),
        ("d__Eukaryota;p__x", None),
        ("", None),
        ("p__Pseudomonadota", None),
        # `gtdb_lineage` has no `range` in the schema, so these are all
        # schema-valid and must not raise (#438).
        (None, None),
        (["d__Bacteria"], None),
        (17, None),
        ({"d__Bacteria": 1}, None),
    ],
)
def test_the_lineage_domain_is_read_from_the_first_field(lineage, expected):
    assert lineage_domain(lineage) == expected


@pytest.mark.parametrize(
    ("label", "document"),
    [
        ("a bare taxonomy item", {"taxonomy": [None]}),
        ("taxon_term as a string", {"taxonomy": [{"taxon_term": "Bosea"}]}),
        (
            "gtdb_classification as a string",
            {"taxonomy": [{"taxon_term": {"gtdb_classification": "x"}}]},
        ),
        (
            "term as a list",
            {"taxonomy": [{"taxon_term": {"term": [1, 2], "gtdb_classification": {}}}]},
        ),
        ("taxonomy that is not a list", {"taxonomy": "nonsense"}),
        ("a non-string lineage", _doc(PLANT_BOSEA, None) | {}),
        ("interactions that are not a list", {"ecological_interactions": "nonsense"}),
        ("a bare interaction", {"ecological_interactions": [None]}),
        ("a document that is not a mapping", "nonsense"),
        ("no document at all", None),
    ],
)
def test_malformed_input_is_skipped_not_raised_on(label, document):
    """Raising here would abort validate-strict and discard every file (#429)."""
    assert check_record(document) == [], label


def test_a_non_string_lineage_does_not_abort_the_run():
    """The specific crash #438 found: schema-valid YAML, AttributeError, no TSV."""
    document = _doc(BACTERIAL_BOSEA, None)
    document["taxonomy"][0]["taxon_term"]["gtdb_classification"] = {
        "gtdb_lineage": ["d__Bacteria", "p__Pseudomonadota"]
    }
    assert check_record(document) == []


def test_an_interaction_participant_is_checked_too():
    """`source_taxon`/`target_taxon` share `taxon_term`'s range, so a block is
    schema-valid there — and both #365 records named the plant id in one (#439).
    """
    document = {
        "ecological_interactions": [
            {
                "name": "Syntrophic Partnership with Bosea",
                "target_taxon": {
                    "preferred_term": "Bosea sp.",
                    "term": {"id": PLANT_BOSEA, "label": "Bosea"},
                    "gtdb_classification": {"gtdb_lineage": BACTERIAL},
                },
            }
        ]
    }
    problems = check_record(document)
    assert len(problems) == 1, problems
    assert "target_taxon" in problems[0]
    assert "Syntrophic Partnership with Bosea" in problems[0]


def test_the_committed_kb_is_clean():
    # Without this the test passes vacuously wherever NCBITaxon is missing:
    # every domain comes back None and nothing is judged (cf. #433).
    assert domain_of("NCBITaxon:2") == "NCBITaxon:2", "NCBITaxon unavailable; this proves nothing"

    scanned, problems = 0, []
    for directory in ("kb/communities", "data/isolates"):
        for path in sorted((REPO / directory).glob("*.yaml")):
            scanned += 1
            problems += [
                f"{path.name}: {m}" for m in check_record(yaml.safe_load(path.read_text()) or {})
            ]
    assert scanned > 300, f"expected the KB, scanned {scanned}"
    assert not problems, "\n".join(problems)


def _grounded_ids(node):
    """Every `term.id` anywhere in a record — taxonomy and interactions alike."""
    if isinstance(node, dict):
        term = node.get("term")
        if isinstance(term, dict) and isinstance(term.get("id"), str):
            yield term["id"]
        for value in node.values():
            yield from _grounded_ids(value)
    elif isinstance(node, list):
        for value in node:
            yield from _grounded_ids(value)


def test_no_record_still_grounds_anything_on_the_plant_bosea():
    """The id as a *grounding*, anywhere — including interaction participants.

    Matching on `term.id` rather than on the file text is deliberate. The
    corrected records name the wrong id in their `curation_note`, explaining
    what it was and why it was wrong — prose that a substring search cannot
    tell apart from the defect it describes.
    """
    hits = sorted(
        {
            path.name
            for directory in ("kb/communities", "data/isolates")
            for path in sorted((REPO / directory).glob("*.yaml"))
            if PLANT_BOSEA in set(_grounded_ids(yaml.safe_load(path.read_text()) or {}))
        }
    )
    assert hits == [], f"the plant genus Bosea is still used for a bacterium in {hits}"


def test_the_gate_fires_through_validate_strict(tmp_path):
    """It must run in CI, not only when called directly."""
    probe = tmp_path / "Broken.yaml"
    probe.write_text(
        yaml.safe_dump(
            {
                "id": "CommunityMech:TEST",
                "name": "pre-fix fixture for #365",
                "taxonomy": [
                    {
                        "taxon_term": {
                            "preferred_term": "Bosea sp.",
                            "term": {"id": PLANT_BOSEA, "label": "Bosea"},
                            "gtdb_classification": {
                                "gtdb_id": "GTDB:g__Bosea",
                                "gtdb_lineage": f"{BACTERIAL};f__Beijerinckiaceae;g__Bosea",
                                "ncbi_source_id": PLANT_BOSEA,
                            },
                        }
                    }
                ],
            },
            sort_keys=False,
        )
    )
    result = subprocess.run(
        [
            "uv",
            "run",
            "python",
            "scripts/validate_strict.py",
            str(probe),
            "--out",
            str(tmp_path / "r.tsv"),
        ],
        capture_output=True,
        text=True,
        cwd=REPO,
        timeout=900,
    )

    assert result.returncode != 0
    assert "gtdb_lineage_contradicts_id_domain" in (result.stdout + result.stderr)


def test_an_unavailable_ontology_is_reported_not_silently_passed(monkeypatch, capsys):
    """No domain means no judgement — but say so, or a green run reads as coverage.

    Also asserts the warning itself, which had no test, and restores the
    once-only flag the earlier version leaked into the rest of the session
    (#440).
    """
    import communitymech.validators.ncbi_domain as ncbi_domain

    real = ncbi_domain._adapter
    was_warned = module._warned_no_adapter
    ncbi_domain.domain_of.cache_clear()
    monkeypatch.setattr(ncbi_domain, "_adapter", lambda: None)
    module._warned_no_adapter = False
    try:
        assert ncbi_domain.domain_of(PLANT_BOSEA) is None
        assert check_record(_doc(PLANT_BOSEA, BACTERIAL)) == []
        assert "skipped, not passed" in capsys.readouterr().err
    finally:
        module._warned_no_adapter = was_warned
        ncbi_domain.domain_of.cache_clear()
        real.cache_clear()
