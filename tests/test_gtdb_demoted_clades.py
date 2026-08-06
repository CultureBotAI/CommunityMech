"""GTDB demotions, where the rank-for-rank vote is true but uninformative (#445).

`gtdb_ground.py` votes at the rank the NCBI taxon sits at. When GTDB has
**demoted** an NCBI clade — kept the organism concept but placed it lower — that
answer names a broader taxon than the record meant. *Candidatus Dormiibacterota*
is an NCBI candidate phylum that GTDB keeps as `c__Dormibacteria` inside
Chloroflexota, so the phylum vote returned `p__Chloroflexota` — which the same
record already used for its *Chloroflexi* entry, collapsing two of the three
phyla its cited snippet contrasts into one GTDB concept.

**No automatic rule is safe here, and the measurement is what shows it.** Of the
KB's 159 groundings above genus rank, **20 look sharpenable** under the tool's
own default policy (`exclude_unnamed=True`, which produced every stored block):
every row behind the winning taxon agrees at some finer rank. Only **three** are
demotions.

* **15 keep their own NCBI name in GTDB** (`is_reclassified: false`) —
  `Gemmatimonadota`, `Thermotogota`, `Verrucomicrobiota`, `Thermoplasmatales`
  and others. The NCBI taxon *is* the GTDB taxon; sharpening to a child would
  assert something the data does not say. A rule keyed on agreement alone
  mis-sharpens all fifteen.
* `Rhodospirillales` -> `o__RF32` and `Ca. Methanophagales` ->
  `o__Alkanophagales` are real reclassifications with **nothing to sharpen to**:
  the finer terms are `f__CAG-239`, an alphanumeric placeholder, and
  `f__Methanospirareceae`, which does not bear the NCBI clade's name.

What marks a demotion is that a finer rank still carries the clade's *name*, and
testing that mechanically is where it fails. Longest common prefix of the NCBI
name and its GTDB counterpart, for the four reclassified cases:

    Ignavibacteriota / Ignavibacteria      14   demotion
    Parvarchaeota    / Parvarchaeales      10   demotion
    Chlorobiota      / Chlorobiia           8   demotion
    Methanophagales  / Methanospirareceae   7   NOT a demotion
    Dormiibacterota  / Dormibacteria        5   demotion (NCBI doubles the i)

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
    values = {row[column].strip() for row in named}
    assert values == {name}, (
        f"{chosen} claims every named-species row for {label!r} is {name!r} at "
        f"{prefix}__ rank, but the crosswalk says {sorted(values)}"
    )
