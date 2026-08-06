"""A prokaryotic GTDB lineage on a non-prokaryotic NCBITaxon id (#365).

Two records used `NCBITaxon:169215` — the *plant* genus *Bosea* (Amaranthaceae)
— for the alphaproteobacterium of the same name, and carried a GTDB block
reading `d__Bacteria;...;g__Bosea` derived from it. The KB asserted a plant was
a bacterium, in the field that looks most independently sourced.

Nothing could see it: `ncbi_source_id == term.id` (so #364's freshness test
passes), "Bosea" really is that id's label (so id<->label passes), and the id
appears once per record (so #292's shared-id gate has nothing to compare).

The signal needs no judgement: GTDB classifies only Bacteria and Archaea, so an
id outside those domains cannot have a GTDB lineage at all.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

import pytest
import yaml

from communitymech.validators.prokaryotic_lineage import (
    check_record,
    domain_of,
    lineage_domain,
)

REPO = Path(__file__).parent.parent
BACTERIAL = "d__Bacteria;p__Pseudomonadota;c__Alphaproteobacteria;o__Rhizobiales"
ARCHAEAL = "d__Archaea;p__Methanobacteriota;c__Methanobacteria"


def _entry(curie: str, lineage: str | None, name: str = "x") -> dict:
    block = {"taxon_term": {"preferred_term": name, "term": {"id": curie, "label": name}}}
    if lineage is not None:
        block["taxon_term"]["gtdb_classification"] = {"gtdb_lineage": lineage}
    return block


def test_the_defect_that_prompted_this_is_caught():
    """#365, reconstructed: the plant Bosea carrying a bacterial lineage."""
    problems = check_record([_entry("NCBITaxon:169215", BACTERIAL, "Bosea sp.")])

    assert len(problems) == 1, problems
    assert "NCBITaxon:169215" in problems[0]
    assert "Eukaryota" in problems[0]


def test_the_corrected_id_is_accepted():
    """`NCBITaxon:85413` is the bacterium NCBI renamed Allobosea."""
    assert check_record([_entry("NCBITaxon:85413", BACTERIAL, "Bosea sp.")]) == []


def test_the_two_ids_really_are_what_the_fix_assumes():
    """The whole fix rests on these two lookups, so assert them directly."""
    assert domain_of("NCBITaxon:169215") == "Eukaryota"
    assert domain_of("NCBITaxon:85413") == "Bacteria"


@pytest.mark.parametrize(
    ("label", "curie", "lineage"),
    [
        ("a bacterium under a bacterial lineage", "NCBITaxon:562", BACTERIAL),
        ("an archaeon under an archaeal lineage", "NCBITaxon:2172", ARCHAEAL),
        # Grounding at a high rank is normal and says nothing about domain.
        ("a domain-rank id", "NCBITaxon:2", "d__Bacteria"),
        # No GTDB block at all, and a block with no lineage to judge.
        ("no gtdb block", "NCBITaxon:169215", None),
        ("an empty lineage", "NCBITaxon:169215", ""),
        # An id NCBITaxon cannot resolve must never be judged.
        ("an unresolvable id", "NCBITaxon:99999999", BACTERIAL),
        ("a non-NCBITaxon id", "GTDB:g__Bosea", BACTERIAL),
    ],
)
def test_legitimate_or_unjudgeable_cases_are_silent(label, curie, lineage):
    assert check_record([_entry(curie, lineage)]) == [], label


def test_the_two_prokaryotic_domains_are_not_interchangeable():
    """GTDB and NCBI disagree about phyla; they do not disagree about domain."""
    problems = check_record([_entry("NCBITaxon:2172", BACTERIAL, "Methanosarcina")])
    assert len(problems) == 1, problems
    assert "Archaea" in problems[0] and "Bacteria" in problems[0]


@pytest.mark.parametrize(
    ("lineage", "expected"),
    [
        (BACTERIAL, "Bacteria"),
        (ARCHAEAL, "Archaea"),
        ("d__Eukaryota;p__x", None),
        ("", None),
        ("p__Pseudomonadota", None),
    ],
)
def test_the_lineage_domain_is_read_from_the_first_field(lineage, expected):
    assert lineage_domain(lineage) == expected


@pytest.mark.parametrize(
    ("label", "taxonomy"),
    [
        ("a bare list item", [None]),
        ("taxon_term as a string", [{"taxon_term": "Bosea"}]),
        ("gtdb_classification as a string", [{"taxon_term": {"gtdb_classification": "x"}}]),
        ("term as a list", [{"taxon_term": {"term": [1, 2], "gtdb_classification": {}}}]),
        ("taxonomy that is not a list", "nonsense"),
        ("no taxonomy at all", None),
    ],
)
def test_malformed_input_is_skipped_not_raised_on(label, taxonomy):
    """Raising here would abort validate-strict and discard every file (#429)."""
    assert check_record(taxonomy) == [], label


def test_the_committed_kb_is_clean():
    # Without this the test passes vacuously wherever NCBITaxon is missing:
    # every domain comes back None and nothing is judged (cf. #433).
    assert domain_of("NCBITaxon:2") == "Bacteria", "NCBITaxon unavailable; this proves nothing"

    scanned, problems = 0, []
    for directory in ("kb/communities", "data/isolates"):
        for path in sorted((REPO / directory).glob("*.yaml")):
            scanned += 1
            document = yaml.safe_load(path.read_text()) or {}
            problems += [f"{path.name}: {m}" for m in check_record(document.get("taxonomy"))]
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

    The GTDB block was only half the defect: both records also named
    `NCBITaxon:169215` as an interaction participant, where there is no lineage
    for the validator to compare against, so the gate cannot see it.

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
            if "NCBITaxon:169215" in set(_grounded_ids(yaml.safe_load(path.read_text()) or {}))
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
                            "term": {"id": "NCBITaxon:169215", "label": "Bosea"},
                            "gtdb_classification": {
                                "gtdb_id": "GTDB:g__Bosea",
                                "gtdb_lineage": f"{BACTERIAL};f__Beijerinckiaceae;g__Bosea",
                                "ncbi_source_id": "NCBITaxon:169215",
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


def test_an_unavailable_ontology_stays_silent(monkeypatch):
    """No domain means no judgement — the gate must not fire on a bare checkout."""
    import communitymech.validators.prokaryotic_lineage as module

    real = module._adapter
    module.domain_of.cache_clear()
    monkeypatch.setattr(module, "_adapter", lambda: None)
    try:
        assert module.domain_of("NCBITaxon:169215") is None
        assert module.check_record([_entry("NCBITaxon:169215", BACTERIAL)]) == []
    finally:
        module.domain_of.cache_clear()
        real.cache_clear()
