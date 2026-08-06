"""GTDB demotions, where the rank-for-rank vote is true but uninformative (#445).

`gtdb_ground.py` votes at the rank the NCBI taxon sits at. When GTDB has
**demoted** an NCBI clade — kept the organism concept but placed it lower — that
answer names a broader taxon than the record meant. *Candidatus Dormiibacterota*
is an NCBI candidate phylum that GTDB keeps as `c__Dormibacteria` inside
Chloroflexota, so the phylum vote returned `p__Chloroflexota` — which the same
record already used for its *Chloroflexi* entry, collapsing two of the three
phyla its cited snippet contrasts into one GTDB concept.

**No automatic rule is safe here, and three rounds of review are the evidence.**
Every attempt to *enumerate* the KB's demotions has been falsified by the next
one, each time through a different structural blind spot:

* demanding strict string unanimity at the finer rank missed `Nitrososphaerota`,
  whose rows read `Nitrososphaeria` 57 and `Nitrososphaeria_A` 8 — GTDB splits a
  clade it finds polyphyletic, so a suffix is not disagreement (#453);
* demanding *any* unanimity missed `Betaproteobacteria`, which is 0.999 —
  41903 of 41937 genomes in `o__Burkholderiales`, with 34 strays elsewhere;
* keying on the clade's surviving *name* missed it too, because GTDB **renamed
  while demoting**: `Betaproteobacteria` and `Burkholderiales` share one letter.

So this module does not claim to list every demotion, and a screen is not what
makes one findable. What it does is record the calls a curator made, with the
evidence for each, so that a tool re-run cannot quietly undo them and the next
person can see what the reasoning was.

The counter-examples are as load-bearing as the cases. Sharpening is wrong
whenever GTDB kept the NCBI name — `Gemmatimonadota`, `Thermotogota`,
`Verrucomicrobiota`, `Thermoplasmatales` and eleven more are `is_reclassified:
false`, the NCBI taxon *is* the GTDB taxon, and a rule keyed on rank agreement
alone mis-sharpens all fifteen. It is wrong again where a reclassification has
nothing to sharpen *to*: `Rhodospirillales` -> `f__CAG-239` and
`Ca. Eiseniibacteriota` -> `c__RBG-16-71-46` are alphanumeric placeholders, and
`Ca. Methanophagales` -> `f__Methanospirareceae` does not bear the clade's name.

Longest common prefix of each reclassified NCBI name and its GTDB counterpart,
which is why no threshold works:

    Nitrososphaerota   / Nitrososphaeria      13   demotion
    Ignavibacteriota   / Ignavibacteria       13   demotion
    Parvarchaeota      / Parvarchaeales       10   demotion
    Chlorobiota        / Chlorobiia            8   demotion
    Methanophagales    / Methanospirareceae    7   NOT a demotion
    Dormiibacterota    / Dormibacteria         5   demotion
    Betaproteobacteria / Burkholderiales       1   demotion
    Rhodospirillales   / CAG-239               0   NOT a demotion
    Eiseniibacteriota  / RBG-16-71-46          0   NOT a demotion

A note on what the pin does. `--apply` only ever creates blocks on *ungrounded*
taxa, so it could not overwrite one of these anyway; `curated: true` is what
stops `--refresh` and `--withdraw-ambiguous`. What these tests add on top is
that deleting the pin, or quietly re-broadening the term, fails.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).parent.parent
COMMUNITIES = REPO / "kb/communities"

# (record, preferred_term) -> the term a curator chose, and what the tool's
# rank-for-rank vote would have returned instead.
SHARPENED = {
    ("Richmond_Mine_AMD_Biofilm.yaml", "Parvarchaeota (ARMAN-4/5)"): (
        "GTDB:o__Parvarchaeales",
        "GTDB:p__Nanoarchaeota",
    ),
    (
        "Soil_BGC_Phylum_Depth_Vegetation_Community.yaml",
        "Candidatus Dormibacteraeota (prolific BGC producers)",
    ): ("GTDB:c__Dormibacteria", "GTDB:p__Chloroflexota"),
    (
        "Anammox_Granule_Metabolic_Interaction_Community.yaml",
        "Chlorobi-affiliated heterotrophic bacteria",
    ): ("GTDB:c__Chlorobiia", "GTDB:p__Bacteroidota"),
    (
        "Rifle_Aquifer_Bioanode_EET_Community.yaml",
        "EET-capable Rifle aquifer Ignavibacteria",
    ): ("GTDB:c__Ignavibacteria", "GTDB:p__Bacteroidota"),
    ("Naica_Deep_Subsurface_Thermophilic.yaml", "Thaumarchaeota"): (
        "GTDB:c__Nitrososphaeria",
        "GTDB:p__Thermoproteota",
    ),
    ("Naica_Deep_Subsurface_Thermophilic.yaml", "Betaproteobacteria"): (
        "GTDB:o__Burkholderiales",
        "GTDB:c__Gammaproteobacteria",
    ),
    (
        "East_River_Floodplain_Core_Microbiome.yaml",
        "Betaproteobacteria-dominated core floodplain microbiome",
    ): ("GTDB:o__Burkholderiales", "GTDB:c__Gammaproteobacteria"),
}

# Demotions where GTDB *renamed* the clade on the way down, so the surviving
# term shares almost none of the NCBI name. The name test below cannot see
# these — it is the blind spot that hid Betaproteobacteria through two rounds of
# review — so they are listed rather than inferred.
RENAMED_WHILE_DEMOTED = {
    ("Naica_Deep_Subsurface_Thermophilic.yaml", "Betaproteobacteria"),
    (
        "East_River_Floodplain_Core_Microbiome.yaml",
        "Betaproteobacteria-dominated core floodplain microbiome",
    ),
}

# The mirror case: reclassified, and deliberately *not* sharpened, because no
# GTDB taxon carries the NCBI clade's name.
LEFT_BROAD = {
    (
        "ANME_SRB_Anaerobic_Methanotrophic_Syntrophic_Consortia.yaml",
        "ANME-1 (anaerobic methanotrophic archaea, clade 1)",
    ): "GTDB:o__Alkanophagales",
}


@pytest.fixture(scope="module")
def gtdb():
    spec = importlib.util.spec_from_file_location("gtdb_ground", REPO / "scripts/gtdb_ground.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def mapping(gtdb):
    try:
        path = gtdb.resolve_kg_microbe_dir(None) / "data/raw/NCBI2GTDB.tsv.gz"
    except SystemExit as exc:
        pytest.skip(f"kg-microbe mapping unavailable: {str(exc).splitlines()[0]}")
    if not path.exists():
        pytest.skip(f"kg-microbe NCBI2GTDB mapping not available at {path}")
    return path


def _entry(record: str, preferred: str) -> dict:
    doc = yaml.safe_load((COMMUNITIES / record).read_text())
    for item in doc.get("taxonomy") or []:
        block = (item or {}).get("taxon_term") or {}
        if block.get("preferred_term") == preferred:
            return block
    raise AssertionError(f"{preferred!r} is gone from {record}")


@pytest.mark.parametrize(
    ("record", "preferred"), list(SHARPENED), ids=[f"{r}::{p}"[:60] for r, p in SHARPENED]
)
def test_a_sharpened_grounding_keeps_its_curated_term(record: str, preferred: str):
    chosen, would_be = SHARPENED[(record, preferred)]
    grounding = _entry(record, preferred).get("gtdb_classification") or {}

    assert grounding.get("gtdb_id") == chosen, (
        f"'{preferred}' in {record} should be grounded at {chosen}. If it now reads "
        f"{would_be}, the rank-for-rank vote has been reapplied over a curator's "
        f"decision — GTDB demoted this clade, so the vote names a broader taxon "
        f"than the record means (#445, #451)."
    )
    assert grounding.get("curated") is True, (
        f"the pin on '{preferred}' is what stops `--refresh` and "
        f"`--withdraw-ambiguous`; without it the decision survives only in git."
    )
    assert grounding.get("curation_note"), "a pin without its reason is unreviewable"


@pytest.mark.parametrize(
    ("record", "preferred"), list(LEFT_BROAD), ids=[f"{r}::{p}"[:60] for r, p in LEFT_BROAD]
)
def test_a_reclassification_with_no_named_equivalent_is_left_alone(record: str, preferred: str):
    """Not every reclassification is a demotion, and this is the counterexample.

    Its winning rows do agree at a finer rank (`f__Methanospirareceae`), so a
    rule keyed on agreement alone would sharpen it. Nothing in GTDB carries the
    name *Methanophagales*, so there is no exact equivalent to sharpen to, and
    the order term is the honest answer.
    """
    grounding = _entry(record, preferred).get("gtdb_classification") or {}
    assert grounding.get("gtdb_id") == LEFT_BROAD[(record, preferred)]


def _shared_stem(first: str, second: str) -> int:
    """Length of the longest common prefix, case-insensitively."""
    first, second = first.lower(), second.lower()
    n = 0
    while n < min(len(first), len(second)) and first[n] == second[n]:
        n += 1
    return n


@pytest.mark.parametrize(
    ("record", "preferred"), list(SHARPENED), ids=[f"{r}::{p}"[:60] for r, p in SHARPENED]
)
def test_the_curated_term_bears_the_clade_name_and_the_broad_one_does_not(
    record: str, preferred: str
):
    """One property that marks a demotion — for the cases where it holds.

    GTDB usually keeps the clade's name when it moves it, so the chosen term
    still reads like the NCBI one and the term the vote returned does not. That
    is a real check, and it fails if a pin is re-broadened.

    It is *not* a definition. `Betaproteobacteria` -> `o__Burkholderiales` is a
    genuine demotion that shares one letter, because GTDB renamed on the way
    down; it is listed in `RENAMED_WHILE_DEMOTED` and skipped here rather than
    weakening the threshold to admit it, which would admit everything.
    """
    if (record, preferred) in RENAMED_WHILE_DEMOTED:
        pytest.skip("GTDB renamed this clade while demoting it; see the module docstring")
    chosen, would_be = SHARPENED[(record, preferred)]
    label = (_entry(record, preferred).get("term") or {}).get("label") or ""
    clade = label.replace("Candidatus ", "")

    kept = _shared_stem(clade, chosen.split("__", 1)[1])
    broad = _shared_stem(clade, would_be.split("__", 1)[1])
    assert kept >= 5, f"{chosen} does not bear {clade!r}'s name (shared stem {kept})"
    assert broad < kept, (
        f"{would_be} shares as much of {clade!r}'s name as {chosen} does, so this "
        f"is not a demotion — re-check whether the sharpening is justified"
    )


@pytest.mark.parametrize(
    ("record", "preferred"), list(SHARPENED), ids=[f"{r}::{p}"[:60] for r, p in SHARPENED]
)
def test_the_curated_term_is_what_the_mapping_actually_supports(
    gtdb, mapping, record: str, preferred: str
):
    """Check the pin's own numbers against GTDB, not against the same YAML block.

    An earlier version compared `gtdb_id` with `gtdb_lineage` — both written by
    the same curator in the same block — so any descendant of the vote's taxon
    passed. A later one demanded that *every* named-species row carry the chosen
    term, which `Betaproteobacteria` fails at 0.999: unanimity was never the
    property, it was an artefact of the small cases looked at first.

    What actually has to hold is that the block's stored counts are the ones the
    crosswalk gives for the chosen term at its own rank, which is the claim each
    `curation_note` makes in prose.
    """
    chosen, _ = SHARPENED[(record, preferred)]
    prefix, name = chosen.split(":", 1)[1].split("__", 1)
    block = _entry(record, preferred)
    grounding = block.get("gtdb_classification") or {}
    label = (block.get("term") or {}).get("label") or ""

    _, _, by_higher = gtdb.collect_rows(mapping, set(), set(), set(gtdb.lookup_keys(label)))
    cells = next((by_higher[k] for k in gtdb.lookup_keys(label) if k in by_higher), [])
    named = gtdb.named_species_only(cells)
    assert named, f"no named-species rows for {label!r}; the pin cannot be checked"

    column = {pr: col for col, pr in gtdb.GTDB_RANK_COLS}[prefix]
    support = sum(gtdb._genomes(r) for r in named if r[column].strip() == name)
    total = sum(gtdb._genomes(r) for r in named if r[column].strip())

    assert support == grounding.get("support_genomes"), (
        f"{chosen} stores support_genomes={grounding.get('support_genomes')}, "
        f"but the crosswalk gives {support} genomes for {name!r} at {prefix}__"
    )
    assert total == grounding.get("total_genomes"), (
        f"{chosen} stores total_genomes={grounding.get('total_genomes')}, "
        f"but the crosswalk gives {total}"
    )
    assert round(support / total, 3) == grounding.get("majority_fraction")
