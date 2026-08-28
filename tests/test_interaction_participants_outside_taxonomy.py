"""The 25 interaction participants that are not taxonomy members (#319).

`UNKNOWN_SOURCE`/`UNKNOWN_TARGET` gate at error severity unless the interaction
carries `scope: COMMUNITY_LEVEL`, which downgrades them to warning (#326). Every
one is a warning today, so `main` is green — but the population has grown since
#319 counted it, unnoticed, which is the thing this file fixes.

The auditor reports **27 findings** over **25 distinct participants**: two are
named as both a source and a target, in different interactions. The sets below
are the 25, since the question is about organisms rather than edges.

#319 asks a policy question: **should hosts and antagonists be `taxonomy`
members?** That is a curation decision and this file does not make it. What it
does is stop the population drifting while the decision is pending, and split it
into the groups the decision actually applies to — because "23 unexplained
warnings" is much harder to decide about than four kinds of thing:

* **UMBRELLA (14)** — an aggregate name for members that *are* in taxonomy.
  `Variovorax` where the records list `Variovorax sp. CF313`, `YR634`, …;
  `Olsenella (Actinobacteriota)` where taxonomy has `Olsenella_B sp. (MAG ATO3)`.
  These are not missing members; they are a coarser way of naming present ones.
  Nothing to decide.
* **HOST (6)** — the plant or animal the community lives on or in. `Medicago
  truncatula (host legume)`, `Arabidopsis thaliana`, `Lactuca sativa`,
  `Hordeum vulgare`, `Hypnum plumaeforme (moss host)`.
* **ANTAGONIST (3)** — a pathogen the community suppresses, i.e. the point of
  the experiment rather than a member of it. `Rhizoctonia solani`,
  `Aeromonas hydrophila`, `Pseudomonas aeruginosa`.
* **ABIOTIC (2)** — `anode`, and the biofilm on it.

HOST and ANTAGONIST are the real question, and they are **9 of the 25** — a
much smaller commitment than the headline count suggests. A community
*interacts with* its host
without the host being a member, which is an argument for leaving them out; the
counter is that an edge to something absent from `taxonomy` is dangling by any
graph reading. #307 asks the mirror-image question about deliberately excluded
candidates and answered "no" there.

A new participant in none of these lists fails, which forces the decision at the
moment somebody adds one rather than in a bulk audit months later.
"""

from __future__ import annotations

import pathlib

import pytest

from communitymech.network.auditor import IssueType, NetworkIntegrityAuditor
from communitymech.paths import record_files

REPO = pathlib.Path(__file__).parent.parent

# Both record roots, not kb/communities alone. `data/isolates` holds the same
# root class -- 4 records with 66 snippets, 3 ecological_interactions and 3
# gtdb_classification blocks -- and this module could not see any of it (#689).

# (record, participant) for every interaction endpoint absent from `taxonomy`,
# grouped by why it is absent. Sourced from the auditor itself, not re-derived:
# an independent matcher disagreed with it on 8 entries, because the auditor
# resolves a participant by id as well as by name.
UMBRELLA = {
    (
        "Drosophila_FiveSpecies_Gnotobiotic_Gut_Microbiota.yaml",
        "Drosophila five-species bacterial microbiota",
    ),
    ("East_River_Floodplain_Core_Microbiome.yaml", "East River floodplain bacteria"),
    ("East_River_Floodplain_Core_Microbiome.yaml", "core floodplain bacteria"),
    ("GLBRC_UFMP_Fermentation_Community.yaml", "Olsenella (Actinobacteriota)"),
    ("Hanford_300_Area_Unconfined_Aquifer_Community.yaml", "Hanford groundwater bacteria"),
    (
        "Hanford_300_Area_Unconfined_Aquifer_Community.yaml",
        "aquifer redox guild bacteria and archaea",
    ),
    (
        "Model_Lignocellulose_Formaldehyde_Crossfeeding_Community.yaml",
        "model lignocellulose consortium members",
    ),
    (
        "ORNL_Clostridium_Desulfovibrio_Geobacter_Trophic_Model.yaml",
        "Desulfovibrio vulgaris Hildenborough and Geobacter sulfurreducens",
    ),
    (
        "ORNL_Clostridium_Desulfovibrio_Geobacter_Trophic_Model.yaml",
        "three-species model community",
    ),
    ("Oak_Ridge_FRC_Uranium_Nitrate_Groundwater_Community.yaml", "other groundwater bacteria"),
    (
        "PET_Artificial_FourSpecies_Degradation_Consortium.yaml",
        "engineered PETase/MHETase and TPA-utilization members",
    ),
    ("PMI_Variovorax_Thermotolerance_Collection.yaml", "Variovorax"),
    ("Rice_Duckweed_Bacillus_SynCom.yaml", "Bacillus SynCom"),
    (
        "Saanich_Inlet_OMZ_Redox_Gradient_Community.yaml",
        "Saanich Inlet redox-gradient microorganisms",
    ),
}
HOST = {
    ("Legume_Rhizobia_Mars_Simulant_Symbiosis.yaml", "Medicago truncatula (host legume)"),
    ("Lunar_Martian_Simulant_PGPB_Lettuce_SynCom.yaml", "Lactuca sativa (lettuce host)"),
    ("Lunar_Simulant_Phosphate_Solubilizing_Bacteria_Nicotiana.yaml", "Nicotiana benthamiana"),
    ("Moss_Microbe_Complex_Regolith_Biofertilizer.yaml", "Hordeum vulgare (barley model crop)"),
    ("Moss_Microbe_Complex_Regolith_Biofertilizer.yaml", "Hypnum plumaeforme (moss host)"),
    ("PMI_Variovorax_Thermotolerance_Collection.yaml", "Arabidopsis thaliana"),
}
ANTAGONIST = {
    ("Crucian_Carp_Gut_Disease_Resistance_SynCom.yaml", "Aeromonas hydrophila"),
    ("Rice_Duckweed_Bacillus_SynCom.yaml", "Rhizoctonia solani"),
    (
        "Thermophilic_Lignocellulose_Composting_SynCom_Biosanitization.yaml",
        "Pseudomonas aeruginosa",
    ),
}
ABIOTIC = {
    ("Shewanella_Geobacter_Exoelectrogenic_Biofilm_Community.yaml", "anode"),
    (
        "Shewanella_Geobacter_Exoelectrogenic_Biofilm_Community.yaml",
        "anode-associated biofilm community",
    ),
}

ACCOUNTED_FOR = UMBRELLA | HOST | ANTAGONIST | ABIOTIC


def _outside_taxonomy() -> set[tuple[str, str]]:
    """Every (record, participant) the auditor reports as not a member."""
    auditor = NetworkIntegrityAuditor()
    found = set()
    for path in record_files():
        for issue in auditor.audit_community(path) or []:
            if issue["type"] in (IssueType.UNKNOWN_SOURCE, IssueType.UNKNOWN_TARGET):
                found.add((path.name, issue.get("taxon")))
    return found


@pytest.fixture(scope="module")
def outside() -> set[tuple[str, str]]:
    return _outside_taxonomy()


def test_there_are_participants_to_account_for(outside):
    """Guard: at zero the accounting below passes vacuously."""
    assert len(outside) > 20, (
        f"only {len(outside)} participants sit outside taxonomy; if the policy "
        f"in #319 has been settled and they were added as members, delete this "
        f"file rather than letting it pass on an empty set"
    )


def test_every_one_is_accounted_for(outside):
    """A new host or antagonist has to be classified, not absorbed.

    This is the drift #319 could not see: it counted 23, and there are 27. Four
    arrived without anyone deciding they should.
    """
    unaccounted = sorted(outside - ACCOUNTED_FOR)
    assert unaccounted == [], (
        "these interaction participants are absent from `taxonomy` and are in "
        "none of the four groups this file tracks:\n"
        + "\n".join(f"  {record}: {name!r}" for record, name in unaccounted)
        + "\n\nAdd each to UMBRELLA, HOST, ANTAGONIST or ABIOTIC — or make it a "
        "taxonomy member. Which of those is right is #319, and the point of "
        "this failure is that the choice gets made now rather than in a bulk "
        "audit later."
    )


def test_nothing_accounted_for_has_quietly_become_a_member(outside):
    """The list must not rot in the other direction either."""
    stale = sorted(ACCOUNTED_FOR - outside)
    assert stale == [], (
        "these are listed here but the auditor no longer reports them — they "
        "were probably added to `taxonomy`, which is a #319 decision worth "
        "recording. Remove them from this file:\n"
        + "\n".join(f"  {record}: {name!r}" for record, name in stale)
    )


def test_all_of_them_are_warnings_not_errors(outside):
    """`main` is green only because every one is COMMUNITY_LEVEL.

    That is the fragility #319 names: the shielding rests on a single optional
    key, and `scope` has `ifabsent: string(PAIRWISE)`. Dropping it from one
    interaction turns that participant into an error and reddens the build on a
    record nobody changed the biology of.
    """
    auditor = NetworkIntegrityAuditor()
    errors = []
    for path in record_files():
        for issue in auditor.audit_community(path) or []:
            if (
                issue["type"] in (IssueType.UNKNOWN_SOURCE, IssueType.UNKNOWN_TARGET)
                and issue["severity"] != "warning"
            ):
                errors.append(f"{path.name}: {issue.get('taxon')!r}")
    assert errors == [], (
        "these participants are outside `taxonomy` at error severity, so the "
        "network gate fails. Either the interaction lost its "
        "`scope: COMMUNITY_LEVEL`, or the participant belongs in `taxonomy` "
        "(#319):\n" + "\n".join(errors)
    )


@pytest.mark.parametrize(
    ("group", "expected"),
    [("UMBRELLA", 14), ("HOST", 6), ("ANTAGONIST", 3), ("ABIOTIC", 2)],
)
def test_the_group_sizes_are_what_the_decision_was_sized_against(group: str, expected: int):
    """#319's decision applies per group, so the group sizes are the input to it.

    UMBRELLA needs no decision — those name members that are present, only more
    coarsely. HOST and ANTAGONIST are the real question, and they are 9 of 25,
    which is a much smaller commitment than the headline count suggests.
    """
    assert len(globals()[group]) == expected


def test_the_schema_records_the_membership_decision():
    """#319's question, answered in the slot rather than in an issue thread.

    "Should hosts and antagonists be taxonomy members?" was re-derived at least
    twice — once when the auditor was written and once when this file was — and
    each time from the same evidence. Recording it on `taxonomy` means the next
    reader finds the answer where they are already looking.

    Asserted positively: the description must *say* hosts and antagonists are
    not members. A check that some phrase is absent would pass on a rewrite
    that dropped the reasoning entirely.
    """
    import yaml

    schema = yaml.safe_load(
        (REPO / "src/communitymech/schema/communitymech.yaml").read_text(encoding="utf-8")
    )
    description = schema["classes"]["MicrobialCommunity"]["attributes"]["taxonomy"]["description"]

    assert "#319" in description
    lowered = description.lower()
    assert "host" in lowered and "antagonist" in lowered, (
        "the taxonomy slot no longer states whether hosts and antagonists are "
        "members, which is the question #319 asked and this file pins the "
        "population for"
    )
    assert "not" in lowered, "the decision was 'no'; the description must say so"
