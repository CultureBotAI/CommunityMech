"""One NCBITaxon id standing in for two different organisms (#292).

`Bacteroides ovatus` carried `NCBITaxon:821`, which is *Phocaeicola vulgatus* —
and the record used that same id, correctly, for its *Bacteroides vulgatus*
entry. A GTDB block was then derived from the wrong id, restating the error in a
second field where it looked better sourced.

No gate could see it. `linkml-term-validator` checks `term.id` against
`term.label`, and those agree; only `preferred_term` disagrees, and comparing
*that* against the label is not viable because it legitimately differs across the
KB to preserve source-paper names through NCBI renames.

The design problem #292 flagged was false positives, and the naive version has
plenty: on this KB it fires on nine records, every one legitimate — strain
variants (`Bacillus velezensis OB3` / `NA3`), engineered constructs
(`B. subtilis 168 Bs_PETase` / `Bs_MHETase`), and `sp.` isolates under a genus
(`Variovorax sp. BK119` .. `BK752`). Comparing the *binomial core* and letting
the id's rank decide what counts as a clash takes that to zero while still
catching the real defect.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

import pytest
import yaml

from communitymech.validators.shared_taxon_ids import _core, check_record, rank_of

REPO = Path(__file__).parent.parent


def _entry(name: str, curie: str) -> dict:
    return {"taxon_term": {"preferred_term": name, "term": {"id": curie, "label": name}}}


def test_the_defect_that_prompted_this_is_caught():
    """#292's first error, reconstructed exactly."""
    problems = check_record(
        [
            _entry("Bacteroides vulgatus", "NCBITaxon:821"),
            _entry("Bacteroides ovatus", "NCBITaxon:821"),
        ]
    )

    assert len(problems) == 1, problems
    assert "NCBITaxon:821" in problems[0]
    assert "ovatus" in problems[0] and "vulgatus" in problems[0]


@pytest.mark.parametrize(
    ("label", "names", "curie"),
    [
        # Every one of these is a real KB pattern the naive version flagged.
        (
            "strain variants",
            ["Bacillus velezensis OB3", "Bacillus velezensis NA3"],
            "NCBITaxon:492670",
        ),
        (
            "engineered constructs",
            ["Bacillus subtilis 168 Bs_PETase", "Bacillus subtilis 168 Bs_MHETase"],
            "NCBITaxon:1423",
        ),
        (
            "sp. isolates under a genus",
            ["Variovorax sp. BK119", "Variovorax sp. BK151", "Variovorax sp. YR752"],
            "NCBITaxon:34072",
        ),
        (
            "named species beside an sp. under a genus",
            ["Bifidobacterium tibiigranuli (MAG BIF2)", "Bifidobacterium sp. (MAG BIF11)"],
            "NCBITaxon:1678",
        ),
        (
            "GTDB placeholder epithets",
            ["Olsenella_B sp. (MAG ATO3)", "Olsenella_B sp900119625 (MAG ATO6)"],
            "NCBITaxon:133926",
        ),
        (
            "guild labels that are not binomials",
            ["rhizosphere Actinobacteria", "rhizosphere Firmicutes"],
            "NCBITaxon:1239",
        ),
    ],
)
def test_legitimate_sharing_is_not_flagged(label, names, curie):
    """False positives are the whole design problem — a noisy gate gets removed."""
    assert check_record([_entry(n, curie) for n in names]) == [], label


def test_a_broad_id_shared_across_guilds_is_fine():
    """Environmental records put several guilds under one clade on purpose."""
    assert (
        check_record(
            [
                _entry("Prairie Pothole methanogens", "NCBITaxon:2157"),
                _entry("Prairie Pothole sulfate reducers", "NCBITaxon:2157"),
            ]
        )
        == []
    )


def test_a_differing_genus_is_caught_even_under_a_genus_id():
    """The one clash a genus-rank id cannot absorb."""
    problems = check_record(
        [
            _entry("Variovorax sp. BK119", "NCBITaxon:34072"),
            _entry("Bacillus subtilis", "NCBITaxon:34072"),
        ]
    )
    assert len(problems) == 1, problems


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("Bacteroides ovatus", ("bacteroides", "ovatus")),
        ("Bacillus velezensis OB3", ("bacillus", "velezensis")),
        ("Variovorax sp. BK119", ("variovorax", "sp")),
        ("Olsenella_B sp900119625 (MAG ATO6)", ("olsenella_b", "sp")),
        ("rhizosphere Actinobacteria", None),
        ("Bacteria", None),
        ("", None),
        # A *mid-name* parenthetical, which is the only case where stripping
        # them changes the answer — every KB name today puts its parenthetical
        # last, where it cannot affect the leading two tokens. Without the
        # strip this yields None and the pair is silently waived.
        ("Bacillus (Weizmannia) coagulans", ("bacillus", "coagulans")),
        ("Clostridium (sensu stricto) butyricum", ("clostridium", "butyricum")),
    ],
)
def test_the_binomial_core_is_extracted_as_documented(name, expected):
    assert _core(name) == expected


def test_the_committed_kb_is_clean():
    scanned, problems = 0, []
    for directory in ("kb/communities", "data/isolates"):
        for path in sorted((REPO / directory).glob("*.yaml")):
            scanned += 1
            document = yaml.safe_load(path.read_text()) or {}
            problems += [f"{path.name}: {m}" for m in check_record(document.get("taxonomy") or [])]
    assert scanned > 300, f"expected the KB, scanned {scanned}"
    assert not problems, "\n".join(problems)


def test_the_gate_fires_through_validate_strict(tmp_path):
    """It must run in CI, not only when called directly.

    Uses the pre-fix version of the record from `main`, so the fixture is the
    real defect rather than a hand-built imitation.
    """
    source = subprocess.run(
        ["git", "show", "main:kb/communities/BioModels_MODEL2405300001_Infant_Gut_HMO_SynCom.yaml"],
        capture_output=True,
        text=True,
        cwd=REPO,
    )
    if source.returncode != 0 or "NCBITaxon:821" not in source.stdout:
        pytest.skip("main no longer carries the pre-fix record; this fixture is stale")

    probe = tmp_path / "Broken.yaml"
    probe.write_text(source.stdout)
    result = subprocess.run(
        [
            "uv",
            "run",
            "python",
            "scripts/validate_strict.py",
            str(probe),
            "--out",
            str(tmp_path / "report.tsv"),
        ],
        capture_output=True,
        text=True,
        cwd=REPO,
        timeout=900,
    )

    assert result.returncode != 0
    assert "taxon_id_reused_for_another_organism" in (result.stdout + result.stderr)


def test_an_unavailable_ontology_stays_silent(monkeypatch):
    """No rank means no judgement — the gate must not fire on a bare checkout."""
    import communitymech.validators.shared_taxon_ids as module

    real = module._adapter
    module.rank_of.cache_clear()
    monkeypatch.setattr(module, "_adapter", lambda: None)
    try:
        assert module.rank_of("NCBITaxon:821") is None
        assert (
            module.check_record(
                [
                    _entry("Bacteroides vulgatus", "NCBITaxon:821"),
                    _entry("Bacteroides ovatus", "NCBITaxon:821"),
                ]
            )
            == []
        )
    finally:
        module.rank_of.cache_clear()
        real.cache_clear()


def test_what_this_gate_does_not_catch():
    """Stated plainly, because #292's *second* defect is outside it.

    `Nitrospiraceae bacterium` carried `NCBITaxon:1236` (class
    Gammaproteobacteria) beside two `Steroidobacteraceae denitrifier` entries
    where that id was correct. The rank filter passes over it: a class id shared
    by several entries is exactly the legitimate pattern this gate must not
    flag, so no threshold separates the two.

    That defect was found and fixed by hand (PR #420). Catching its shape needs a
    different signal — comparing the entry's claimed lineage against the id's —
    which is #365's territory, not this one.
    """
    assert rank_of("NCBITaxon:1236") == "class"
    assert (
        check_record(
            [
                _entry("Steroidobacteraceae denitrifier 1", "NCBITaxon:1236"),
                _entry("Nitrospiraceae bacterium", "NCBITaxon:1236"),
            ]
        )
        == []
    ), "if this now fires, the gate got stronger and the docstring is stale"
