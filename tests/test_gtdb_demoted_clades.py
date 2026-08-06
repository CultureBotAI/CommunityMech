"""GTDB demotions, where the rank-for-rank vote is true but uninformative (#445).

`gtdb_ground.py` votes at the rank the NCBI taxon sits at. When GTDB has
**demoted** an NCBI clade — kept the organism concept but placed it lower — that
answer names a broader taxon than the record meant. *Candidatus Dormiibacterota*
is an NCBI candidate phylum that GTDB keeps as `c__Dormibacteria` inside
Chloroflexota, so the phylum vote returned `p__Chloroflexota` — which the same
record already used for its *Chloroflexi* entry, collapsing two of the three
phyla its cited snippet contrasts into one GTDB concept.

**No automatic rule is safe here, and the measurement is what shows it.** Of the
KB's 159 groundings above genus rank, **21 look sharpenable** under the tool's
own default policy (`exclude_unnamed=True`, which produced every stored block):
every row behind the winning taxon agrees at some finer rank, once GTDB's `_A`
polyphyly suffix is set aside. Only **five** are demotions.

* **15 keep their own NCBI name in GTDB** (`is_reclassified: false`) —
  `Gemmatimonadota`, `Thermotogota`, `Verrucomicrobiota`, `Thermoplasmatales`
  and others. The NCBI taxon *is* the GTDB taxon; sharpening to a child would
  assert something the data does not say. A rule keyed on agreement alone
  mis-sharpens all fifteen.
* Of the 6 reclassified, `Rhodospirillales` -> `o__RF32`,
  `Ca. Methanophagales` -> `o__Alkanophagales` and `Ca. Eiseniibacteriota` ->
  `p__Eisenbacteria` have **nothing to sharpen to**: the finer terms are
  `f__CAG-239` and `c__RBG-16-71-46`, alphanumeric placeholders, and
  `f__Methanospirareceae`, which does not bear the NCBI clade's name.

The suffix point is not incidental. An earlier version of this sweep demanded
*strict* string unanimity and so was blind to any demotion GTDB had split for
monophyly — which is exactly how it missed `Nitrososphaerota`, whose rows read
`Nitrososphaeria` 57 and `Nitrososphaeria_A` 8.

What marks a demotion is that a finer rank still carries the clade's *name*, and
testing that mechanically is where it fails. Longest common prefix of the NCBI
name and its GTDB counterpart, across the reclassified cases:

    Nitrososphaerota / Nitrososphaeria     13   demotion
    Ignavibacteriota / Ignavibacteria      13   demotion
    Parvarchaeota    / Parvarchaeales      10   demotion
    Chlorobiota      / Chlorobiia           8   demotion
    Methanophagales  / Methanospirareceae   7   NOT a demotion
    Dormiibacterota  / Dormibacteria        5   demotion (NCBI doubles the i)
    Eiseniibacteriota/ RBG-16-71-46         0   NOT a demotion

No threshold separates them — a cut anywhere above 5 loses Dormibacteria, and
anywhere below 8 admits Methanospirareceae. So this stays a curator's call, and
these tests pin the calls that were made rather than trying to re-derive them.

A note on what the pin does. `--apply` only ever creates blocks on *ungrounded*
taxa, so it could not overwrite one of these anyway; `curated: true` is what
stops `--refresh` and `--withdraw-ambiguous`. What these tests add on top is
that deleting the pin, or quietly re-broadening the term, fails.
"""

from __future__ import annotations

import importlib.util
import re
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
    """The property that makes a sharpening a *demotion* rather than a guess.

    This is what stops the pin being re-broadened. Checking the crosswalk alone
    cannot: "every named row carries X at rank Y" is true of every **ancestor**
    too, so `p__Bacteroidota` and `p__Nanoarchaeota` both satisfy it and the
    earlier version of this test passed with the pins reverted.

    What separates them is the name. GTDB kept the clade and moved it, so the
    chosen term still reads like the NCBI one, and the term the vote returned
    does not.
    """
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
    """Check the pin against GTDB, not against the rest of the same YAML block.

    An earlier version compared `gtdb_id` with `gtdb_lineage` — both written by
    the same curator in the same block — so any descendant of the vote's taxon
    passed, including a wrong clade with a matching hand-written lineage. This
    goes back to the crosswalk: every named-species row behind the grounding
    must carry the chosen term at its own rank, which is exactly the claim each
    `curation_note` makes.
    """
    chosen, _ = SHARPENED[(record, preferred)]
    prefix, name = chosen.split(":", 1)[1].split("__", 1)
    label = (_entry(record, preferred).get("term") or {}).get("label") or ""

    _, _, by_higher = gtdb.collect_rows(mapping, set(), set(), set(gtdb.lookup_keys(label)))
    cells = next((by_higher[k] for k in gtdb.lookup_keys(label) if k in by_higher), [])
    named = gtdb.named_species_only(cells)
    assert named, f"no named-species rows for {label!r}; the pin cannot be checked"

    column = {pr: col for col, pr in gtdb.GTDB_RANK_COLS}[prefix]
    # GTDB splits a clade it finds polyphyletic into `X`, `X_A`, `X_B`. Those
    # are the same clade for this purpose — demanding strict string unanimity
    # is precisely what hid the Nitrososphaerota demotion until review.
    values = {re.sub(r"_[A-Z]$", "", row[column].strip()) for row in named}
    assert values == {re.sub(r"_[A-Z]$", "", name)}, (
        f"{chosen} claims every named-species row for {label!r} is {name!r} at "
        f"{prefix}__ rank, but the crosswalk says {sorted(values)}"
    )
