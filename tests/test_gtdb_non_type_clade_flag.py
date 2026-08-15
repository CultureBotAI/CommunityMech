"""Grounding to a non-type clade is reported, not resolved (#374).

`gtdb_ground.py` grounds a higher-rank NCBI taxon to whichever GTDB taxon holds
the most genomes. GTDB names by **nomenclatural type**: the lineage containing
the type species keeps the unsuffixed name and the rest take alphabetic
suffixes. The two rules disagree whenever a non-type clade is more heavily
sequenced.

Verified against GTDB R226 (the mapping this repo reads), `Enterococcus` grounds
to `g__Enterococcus_B` at 0.598 while *E. faecalis* — the type species — sits in
`g__Enterococcus`, which drew 9904 of the 28462 genomes. The other four taxa
where the denominators differ agree only because the majority happens to be the
type clade, which is luck rather than construction.

**Reported, not resolved, by decision.** Preferring the type clade would change
what every existing grounding means on the evidence of one live case, and the
majority answer is not obviously wrong — someone asking for "NCBI genus X" may
well want the clade most of X's genomes are in. So the tool emits both and the
curator decides.

The suffix is not a heuristic: it is GTDB's own published marker for "this clade
does not contain the type". That is why the check can be a regex and still be
correct.
"""

from __future__ import annotations

import importlib.util
import pathlib

import pytest

REPO = pathlib.Path(__file__).parent.parent
SCRIPT = REPO / "scripts/gtdb_ground.py"


@pytest.fixture(scope="module")
def gtdb():
    spec = importlib.util.spec_from_file_location("gtdb_ground_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.mark.parametrize(
    ("name", "expected_base"),
    [
        # Every non-type clade actually present in the KB today.
        ("Enterococcus_B", "Enterococcus"),
        ("Cetobacterium_A", "Cetobacterium"),
        ("Methanobrevibacter_A", "Methanobrevibacter"),
        ("Bacillota_A", "Bacillota"),
        ("Clostridium_AM", "Clostridium"),
        ("Acidithiobacillus_A", "Acidithiobacillus"),
        ("Pseudomonas_E", "Pseudomonas"),
        ("Ruminococcus_B", "Ruminococcus"),
    ],
)
def test_a_suffixed_name_is_a_non_type_clade(gtdb, name, expected_base):
    assert gtdb.non_type_clade(name) == expected_base


@pytest.mark.parametrize(
    "name",
    [
        # The type-anchored names themselves.
        "Enterococcus",
        "Pseudomonas",
        "Bacillus",
        "Leptospirillum",
        # A binomial is not a genus name; the species path does not get this
        # warning, and passing one here must not produce a false positive.
        "Ruminococcus_B gnavus",
        "Clostridium_AM drakei",
        # Genuine names that merely contain characters the pattern touches.
        "Candidatus Nitrosocosmicus",
        "CAG-267",
        "",
    ],
)
def test_these_are_not_flagged(gtdb, name):
    assert gtdb.non_type_clade(name) is None


def test_the_warning_names_the_type_clade_and_its_support(gtdb):
    """The message has to tell a curator what to compare against.

    Numbers from the real Enterococcus case: the type clade is not a fringe
    option, it drew 9904 genomes against the winner's 17011, which is exactly
    the situation where a curator's judgement is worth having.
    """
    warning = gtdb._non_type_warning(
        "Enterococcus_B", {"Enterococcus_B": 17011, "Enterococcus": 9904}
    )

    assert "Enterococcus_B is not the type-anchored clade" in warning
    assert "reserves Enterococcus for" in warning
    assert "9904 genomes" in warning
    assert "#374" in warning


def test_the_warning_distinguishes_a_type_clade_with_no_genomes(gtdb):
    """Different curator action, so a different sentence.

    If the type clade drew nothing, the NCBI name's genomes simply do not sit in
    it — a stronger statement than a close call, and it should not read as one.
    """
    warning = gtdb._non_type_warning("Cetobacterium_A", {"Cetobacterium_A": 40})

    assert "drew no genomes here" in warning
    assert "0 genomes" not in warning, "a bare 0 reads like a close call that lost"


def _ground(name: str) -> str:
    """Run the real CLI against the real GTDB mapping."""
    import subprocess

    result = subprocess.run(
        ["uv", "run", "python", str(SCRIPT), "--name", name],
        capture_output=True,
        text=True,
        cwd=REPO,
    )
    return result.stdout


@pytest.mark.integration
def test_enterococcus_warns_and_still_returns_the_majority_answer():
    """End-to-end on the one taxon in the KB where the rules actually disagree.

    Flagging must not change the answer — that was the decision. If someone
    later makes this prefer the type clade, the second assertion goes red and
    they have to say so deliberately.
    """
    out = _ground("Enterococcus")
    if "GTDB taxon" not in out:
        pytest.skip("local GTDB mapping unavailable")

    assert "NON-TYPE" in out, "the one real conflict in the KB produced no warning"
    assert "g__Enterococcus_B" in out, "the majority answer was silently overridden"


@pytest.mark.integration
@pytest.mark.parametrize("name", ["Pseudomonas", "Acetobacter", "Leptospirillum", "Bacillus"])
def test_the_four_that_agree_do_not_warn(name):
    """The other four taxa where the denominators differ.

    They agree with the type rule only because the majority happens to be the
    type clade. A warning here would be a false positive on 4 of 5 cases, which
    would train a curator to ignore it.
    """
    out = _ground(name)
    if "GTDB taxon" not in out:
        pytest.skip("local GTDB mapping unavailable")

    assert "NON-TYPE" not in out, f"{name} agrees with the type rule but was flagged"
