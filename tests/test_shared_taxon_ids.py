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

from communitymech.validators.shared_taxon_ids import (
    _core,
    check_record,
    known_cores,
    rank_of,
)

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


@pytest.mark.parametrize(
    ("label", "names", "curie"),
    [
        # An NCBI rename, which is exactly what `preferred_term` exists to
        # preserve. Different genus *and* different epithet — otherwise the
        # strongest clash signal there is — but NCBITaxon lists both names for
        # the id, so they are one organism (#430).
        (
            "a source-paper name preserved across an NCBI rename",
            ["Agathobacter rectalis DSM 17629", "Eubacterium rectale ATCC 33656"],
            "NCBITaxon:39491",
        ),
        (
            "the same rename in the other direction",
            ["Clostridium difficile 630", "Clostridioides difficile R20291"],
            "NCBITaxon:1496",
        ),
        # A GTDB split of one NCBI genus, already in the KB as `Olsenella_B`.
        (
            "a GTDB genus split",
            ["Olsenella sp. (MAG A)", "Olsenella_B sp. (MAG B)"],
            "NCBITaxon:133925",
        ),
        # The abbreviation a paper uses after first mention. This one is live:
        # the KB's own PET consortium spells one entry `B. subtilis 168 ...`.
        (
            "a genus abbreviated after first mention",
            ["B. subtilis 168 Bs_PETase", "Bacillus subtilis 168 Bs_MHETase"],
            "NCBITaxon:1423",
        ),
        (
            "the same abbreviation for E. coli",
            ["E. coli K-12", "Escherichia coli Nissle 1917"],
            "NCBITaxon:562",
        ),
    ],
)
def test_one_organism_spelled_two_ways_is_not_a_clash(label, names, curie):
    """Each of these fired before #430 and is legitimate."""
    assert check_record([_entry(n, curie) for n in names]) == [], label


def test_a_rename_exemption_does_not_swallow_the_real_defect():
    """The exemption is per-name, so an unrelated species is still caught.

    `Bacteroides vulgatus` *is* a name NCBITaxon lists for 821; `Bacteroides
    ovatus` is not. Exempting the first must not exempt the pair.
    """
    assert ("bacteroides", "vulgatus") in known_cores("NCBITaxon:821")
    assert ("bacteroides", "ovatus") not in known_cores("NCBITaxon:821")
    problems = check_record(
        [
            _entry("Bacteroides vulgatus", "NCBITaxon:821"),
            _entry("Bacteroides ovatus", "NCBITaxon:821"),
        ]
    )
    assert len(problems) == 1, problems


@pytest.mark.parametrize(
    ("label", "taxonomy"),
    [
        ("a bare list item", [{"taxon_term": {"preferred_term": "A"}}, None]),
        ("taxon_term as a string", [{"taxon_term": "Bacteroides"}]),
        ("term as a list", [{"taxon_term": {"term": [1, 2]}}]),
        ("a non-string id", [{"taxon_term": {"preferred_term": "A", "term": {"id": 123}}}]),
        ("taxonomy that is not a list", "nonsense"),
        ("no taxonomy at all", None),
    ],
)
def test_malformed_input_is_skipped_not_raised_on(label, taxonomy):
    """An exception here would abort validate-strict and discard every file.

    The schema validator in that same pass diagnoses these properly; this check
    must stay out of its way rather than crash the run (#429).
    """
    assert check_record(taxonomy) == [], label


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        # `Candidatus` is a nomenclatural status, not part of the name (#431).
        ("Candidatus Nitrosotalea devanaterra", ("nitrosotalea", "devanaterra")),
        ("Candidatus Accumulibacter", None),
        # A strain code is not an epithet: it names a genus and no species, so
        # it reduces exactly as `Marinobacter sp. CS1` would.
        ("Marinobacter CS1", ("marinobacter", "sp")),
        ("Parabacteroides ASF519", ("parabacteroides", "sp")),
        ("Bradyrhizobium PHNZY-24-6", ("bradyrhizobium", "sp")),
        ("Synechococcus PCC 7002", ("synechococcus", "sp")),
        ("Croceibacter Crocei1", ("croceibacter", "sp")),
        # A provisional genus is bracketed in NCBI.
        ("[Clostridium] scindens", ("clostridium", "scindens")),
        # The narrowness that keeps guild labels out: an ordinary capitalised
        # word is not a strain code, so this is not a genus named "Prairie".
        ("Prairie Pothole methanogens", None),
        ("13C-labeled rhizosphere bacteria", None),
        ("ANME-1 (anaerobic methanotrophic archaea, clade 1)", None),
    ],
)
def test_the_two_conventions_431_added_are_read_as_binomials(name, expected):
    assert _core(name) == expected


def test_the_431_defect_shape_is_now_caught():
    """Two *Candidatus* species under one species id — #431's worked example."""
    problems = check_record(
        [
            _entry("Candidatus Nitrosotalea devanaterra", "NCBITaxon:1903276"),
            _entry("Candidatus Phormidium alkaliphilum", "NCBITaxon:1903276"),
        ]
    )
    assert len(problems) == 1, problems


def test_two_strain_isolates_of_different_genera_are_caught():
    problems = check_record(
        [_entry("Marinobacter CS1", "NCBITaxon:2742"), _entry("Mameliella CS4", "NCBITaxon:2742")]
    )
    assert len(problems) == 1, problems


@pytest.mark.parametrize(
    ("label", "names", "curie"),
    [
        # Widening `_core` put more names into the `sp` bucket, which exposed a
        # latent false positive the `sp.` spelling already had: an *unnamed*
        # species says nothing about which species it is, so it cannot
        # contradict a named one. CS1 may well be that very species.
        (
            "a strain code beside the named species, under a species id",
            ["Marinobacter CS1", "Marinobacter hydrocarbonoclasticus"],
            "NCBITaxon:2743",
        ),
        (
            "the same, spelled sp.",
            ["Variovorax sp. BK119", "Variovorax paradoxus"],
            "NCBITaxon:34073",
        ),
        (
            "two strain isolates of one genus",
            ["Marinobacter CS1", "Marinobacter CS9"],
            "NCBITaxon:2742",
        ),
    ],
)
def test_an_unnamed_species_cannot_contradict_a_named_one(label, names, curie):
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
    # Without this the test passes vacuously wherever NCBITaxon is missing
    # (#433): every rank comes back None, nothing is judged, and "no problems"
    # means "nothing was looked at".
    assert rank_of("NCBITaxon:821") == "species", "NCBITaxon unavailable; this proves nothing"

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

    The fixture is vendored rather than fetched with `git show main:...`. That
    read the pre-fix record straight from history, which was appealing, but it
    failed in both directions (#428): CI checks out at `fetch-depth: 1`, so
    there was no local `main` and the test skipped on every PR; and once this
    fix merged, `main` would return the *corrected* record while the staleness
    guard — keyed on `NCBITaxon:821`, which the record still legitimately uses
    for its `Bacteroides vulgatus` entry — would not notice, so the test would
    assert a failure against a clean file and turn `main` red.

    The two entries below are that record's, verbatim, as of the defect.
    """
    probe = tmp_path / "Broken.yaml"
    probe.write_text(
        yaml.safe_dump(
            {
                "id": "CommunityMech:TEST",
                "name": "pre-fix fixture for #292",
                "taxonomy": [
                    {
                        "taxon_term": {
                            "preferred_term": "Bacteroides vulgatus",
                            "term": {"id": "NCBITaxon:821", "label": "Phocaeicola vulgatus"},
                        }
                    },
                    {
                        "taxon_term": {
                            "preferred_term": "Bacteroides ovatus",
                            "term": {"id": "NCBITaxon:821", "label": "Phocaeicola vulgatus"},
                        }
                    },
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
            str(tmp_path / "report.tsv"),
        ],
        capture_output=True,
        text=True,
        cwd=REPO,
        timeout=900,
    )

    assert result.returncode != 0
    assert "taxon_id_reused_for_another_organism" in (result.stdout + result.stderr)


def _cli(*args, cwd):
    return subprocess.run(
        ["uv", "run", "python", "scripts/validate_shared_taxon_ids.py", *args],
        capture_output=True,
        text=True,
        cwd=cwd,
        timeout=900,
    )


def test_the_cli_separates_a_finding_from_a_usage_error(tmp_path):
    """`just validate-taxon-ids` must not report a typo'd path as a finding."""
    clean = tmp_path / "Clean.yaml"
    clean.write_text(
        yaml.safe_dump({"taxonomy": [{"taxon_term": {"preferred_term": "A", "term": {}}}]})
    )
    dirty = tmp_path / "Dirty.yaml"
    dirty.write_text(
        yaml.safe_dump(
            {
                "taxonomy": [
                    {"taxon_term": {"preferred_term": n, "term": {"id": "NCBITaxon:821"}}}
                    for n in ("Bacteroides vulgatus", "Bacteroides ovatus")
                ]
            }
        )
    )

    assert _cli(str(clean), cwd=REPO).returncode == 0
    found = _cli(str(dirty), cwd=REPO)
    assert found.returncode == 1
    assert "NCBITaxon:821" in found.stdout

    missing = _cli(str(tmp_path / "Nope.yaml"), cwd=REPO)
    assert missing.returncode == 2, "a missing file must not look like a reused id"
    assert "cannot read" in missing.stderr

    assert _cli(cwd=REPO).returncode == 2, "no arguments is a usage error"


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
