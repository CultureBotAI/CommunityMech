"""What is left ungrounded on purpose, and why (#401).

`NOT_ATTEMPTED` means "the tool would ground this and the KB does not" — the one
status that is unambiguously outstanding work. #401 found nine, and this closes
all of them: one (Desulfobacteraceae) was grounded in the meantime, four are
grounded here, and four are **`WITHHELD`**, which is the value that says a
curator decided rather than that nothing explains why. Each carries its reason
in `WITHHELD_GROUNDINGS`, so `--apply` skips it — without that the hold is a
comment, and a routine re-run puts `g__Cognaticolwellia @0.548` into the KB.

Held on a bare majority — #396 is about how little one says:

* `Colwellia` -> `g__Cognaticolwellia` at **0.548**. A rename decided by a coin
  flip: adopting it would restate a near-tie as a fact, on a genus the record
  names plainly.
* `Euryarchaeota` -> `p__Methanobacteriota` at **0.531**. Same shape.

Held on the type-species question — #374, and see #377 for why it is stuck:

* both `Nitrospira` entries -> `g__Nitrospira_D` at 0.81. `_D` is a
  non-type split, so this is the pathology of #377 again. It cannot be fixed by
  grounding to the type-bearing term either, because that term holds a minority
  of genomes and `majority_fraction` is bounded `[0.5, 1.0]` — the field means
  "the fraction backing the winner". Grounding to `_D` or to the type-bearing
  split both assert something unsupported, so neither is done.

Two of the four also carry a `preferred_term` that is an informal descriptor
rather than the NCBI label — `Nitrospira-like nitrite oxidizer`, `Nitrospirae
core floodplain members` — so grounding them would assert an identity the source
may not support. That is a curation question, not a tool one.

The four grounded ones were each checked before grounding, but not against a
single criterion — two of them have a `preferred_term` that is *not* the NCBI
label either:

* *Chromobacterium violaceum* and *Methylobacterium extorquens* name their taxon
  exactly, at species rank, 0.97 and 0.88.
* `Rothia kefirresidentii KRP` names a species while its id is the genus
  *Rothia*. Grounding follows the id, and there was no alternative: the
  crosswalk has no *R. kefirresidentii* row at all.
* `novel multiheme-cytochrome Geobacter sp.` is a descriptor, but it names
  *Geobacter*, its id is the *Geobacter* genus, and the grounding is
  `g__Geobacter` at 0.948 — so the descriptor adds nothing the grounding
  contradicts.

What distinguishes these from the two held descriptors is that "Nitrospira-like"
and "Nitrospirae core floodplain members" would have to be grounded to a
*non-type split*, so the descriptor and the weak target compound.
"""

from __future__ import annotations

import pathlib

import pytest
import yaml

REPO = pathlib.Path(__file__).parent.parent
RECORD_DIRS = ("kb/communities", "data/isolates")

# (record, preferred_term) -> why it stays ungrounded.
HELD = {
    ("Deepwater_Horizon_Deep_Sea_Oil_Plume_Succession.yaml", "Colwellia"): (
        "g__Cognaticolwellia wins at 0.548 — a rename on a coin flip (#396)"
    ),
    ("High_Solids_Switchgrass_Methanogenic_Microbiome.yaml", "Euryarchaeota"): (
        "p__Methanobacteriota wins at 0.531 (#396)"
    ),
    ("AMD_Nitrososphaerota_Archaeal.yaml", "Nitrospira-like nitrite oxidizer"): (
        "g__Nitrospira_D is a non-type split, and the type-bearing one holds a "
        "minority of genomes, which majority_fraction cannot express (#374, #377)"
    ),
    ("East_River_Floodplain_Core_Microbiome.yaml", "Nitrospirae core floodplain members"): (
        "as above, plus a preferred_term that is a descriptor rather than a taxon"
    ),
}

# Grounded by #401 after checking the preferred_term against the id.
GROUNDED_BY_401 = {
    ("Chromobacterium_Gold_Biocyanidation.yaml", "Chromobacterium violaceum"): (
        "GTDB:s__Chromobacterium_violaceum"
    ),
    ("Methylobacterium_REE_Ewaste_Platform.yaml", "Methylobacterium extorquens"): (
        "GTDB:s__Methylobacterium_extorquens"
    ),
    ("BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml", "Rothia kefirresidentii KRP"): (
        "GTDB:g__Rothia"
    ),
    ("Rifle_Aquifer_Bioanode_EET_Community.yaml", "novel multiheme-cytochrome Geobacter sp."): (
        "GTDB:g__Geobacter"
    ),
}


def _entry(record: str, preferred: str) -> dict:
    for directory in RECORD_DIRS:
        path = REPO / directory / record
        if not path.exists():
            continue
        document = yaml.safe_load(path.read_text()) or {}
        for item in document.get("taxonomy") or []:
            block = (item or {}).get("taxon_term") or {}
            if block.get("preferred_term") == preferred:
                return block
    raise AssertionError(f"{preferred!r} is gone from {record}")


@pytest.mark.parametrize(("record", "preferred"), list(HELD), ids=[r for r, _ in HELD])
def test_a_deliberately_ungrounded_taxon_stays_ungrounded(record: str, preferred: str):
    """Holding these is a decision, so sweeping them in should have to be one too."""
    block = _entry(record, preferred)
    assert block.get("gtdb_grounding_status") == "WITHHELD", (
        f"'{preferred}' in {record} is ungrounded on purpose: "
        f"{HELD[(record, preferred)]}. WITHHELD is the value that says a curator "
        f"decided; NOT_ATTEMPTED says nothing explains why. If it is being "
        f"grounded now, that is a curation call — make it explicitly, drop it "
        f"from WITHHELD_GROUNDINGS, and update this test (#401)."
    )
    assert "gtdb_classification" not in block


@pytest.mark.parametrize(
    ("record", "preferred"), list(GROUNDED_BY_401), ids=[r[:40] for r, _ in GROUNDED_BY_401]
)
def test_the_unambiguous_ones_were_grounded(record: str, preferred: str):
    block = _entry(record, preferred)
    grounding = block.get("gtdb_classification") or {}
    assert grounding.get("gtdb_id") == GROUNDED_BY_401[(record, preferred)]
    assert block.get("gtdb_grounding_status") == "GROUNDED", (
        "the tool writes the block but not the status, so `--apply` has to be "
        "followed by `--apply-status` or the record contradicts itself"
    )
    assert grounding.get("majority_fraction") >= 0.88, (
        "#401's split was to ground only the clear ones; anything weaker is a "
        "judgement that belongs with #396"
    )


def test_no_taxon_is_silently_outstanding():
    """NOT_ATTEMPTED should now be empty, and stay accounted for if it is not.

    #401 emptied it: five grounded, four moved to WITHHELD with a reason each.
    So a taxon appearing here is one nobody has triaged — which is exactly what
    the status is for, and what the count assertion in
    tests/test_gtdb_coherence_validator.py used to guard before it could be
    stated this precisely.
    """
    outstanding = []
    for directory in RECORD_DIRS:
        for path in sorted((REPO / directory).glob("*.yaml")):
            document = yaml.safe_load(path.read_text()) or {}
            for item in document.get("taxonomy") or []:
                block = (item or {}).get("taxon_term") or {}
                if block.get("gtdb_grounding_status") != "NOT_ATTEMPTED":
                    continue
                key = (path.name, block.get("preferred_term"))
                if key not in HELD:
                    outstanding.append(f"{path.name}: {block.get('preferred_term')}")
    assert outstanding == [], (
        "these are NOT_ATTEMPTED and unaccounted for — either ground them, or "
        "add them to HELD with the reason (#401):\n" + "\n".join(outstanding)
    )
