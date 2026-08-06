"""What is left ungrounded on purpose, and why (#401).

`NOT_ATTEMPTED` means "the tool would ground this and the KB does not" — the one
status that is unambiguously outstanding work. #401 found nine. Four were
unambiguous and are now grounded; one (Desulfobacteraceae) was grounded in the
meantime. **Four remain, each held for a reason that is not "nobody got round
to it"**, and this file records which is which so a future sweep does not
mistake a decision for a backlog.

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

The four that were grounded were checked against exactly that: each
`preferred_term` names the taxon its id names, and each majority is >= 0.88.
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
    assert block.get("gtdb_grounding_status") == "NOT_ATTEMPTED", (
        f"'{preferred}' in {record} was left ungrounded on purpose: "
        f"{HELD[(record, preferred)]}. If it is being grounded now, that is a "
        f"curation call — make it explicitly and update this test (#401)."
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


def test_no_other_taxon_is_silently_outstanding():
    """`NOT_ATTEMPTED` should mean *held*, not *forgotten*, from here on."""
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
