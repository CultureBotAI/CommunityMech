"""GTDB demotions, where the rank-for-rank vote is true but uninformative (#445).

`gtdb_ground.py` votes at the rank the NCBI taxon sits at. When GTDB has
**demoted** an NCBI clade — kept the organism concept but placed it lower — that
answer names a broader taxon than the record meant. *Candidatus Dormiibacterota*
is an NCBI candidate phylum that GTDB keeps as `c__Dormibacteria` inside
Chloroflexota, so the phylum vote returned `p__Chloroflexota` — which the same
record already used for its *Chloroflexi* entry, collapsing two of the three
phyla its cited snippet contrasts into one GTDB concept.

**No automatic rule is safe here, which is the finding rather than the
workaround.** Measured over all 159 higher-rank groundings in the KB, six look
sharpenable — every one of the winning rows agrees at a finer rank — but only
two are demotions:

* `Gemmatimonadota` (×2) and `Thermotogota` keep their own names in GTDB
  (`is_reclassified: false`). The NCBI taxon *is* the GTDB phylum; sharpening to
  a class would assert something the data does not say. A rule keyed on
  "the winning rows agree at a finer rank" would have mis-sharpened all three.
* `Rhodospirillales` -> `o__RF32` looks weak by *rows* (7 of 328) but is a
  0.704 majority by *genomes*, which is the denominator the tool uses.
* `Candidatus Methanophagales` -> `o__Alkanophagales` is a genuine
  reclassification, but **no** GTDB taxon bears the NCBI clade's name, so there
  is nothing to sharpen *to*. It stays where it is.

What separates a demotion is that a finer GTDB rank still carries the clade's
name — and testing *that* mechanically is where it breaks down: the shared stem
of `Parvarchaeota`/`Parvarchaeales` is 10 characters, of
`Dormiibacterota`/`Dormibacteria` only 5 (NCBI doubles the `i`), and of
`Methanophagales`/`Methanospirareceae` 7. No threshold separates the two real
cases from the false one.

So this is a curator's call, and these tests pin the calls that were made rather
than trying to re-derive them. Each decision travels with the data as
`curated: true`, so `--apply` will not overwrite it; what these tests add is
that removing the pin, or quietly re-broadening the term, fails.
"""

from __future__ import annotations

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
    ): (
        "GTDB:c__Dormibacteria",
        "GTDB:p__Chloroflexota",
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
    block = _entry(record, preferred)
    grounding = block.get("gtdb_classification") or {}

    assert grounding.get("gtdb_id") == chosen, (
        f"'{preferred}' in {record} should be grounded at {chosen}. If it now reads "
        f"{would_be}, the rank-for-rank vote has been reapplied over a curator's "
        f"decision — GTDB demoted this clade, so the vote names a broader taxon "
        f"than the record means (#445)."
    )
    assert grounding.get("curated") is True, (
        f"the pin on '{preferred}' is what stops `gtdb_ground.py --apply` "
        f"rewriting it; without it the decision survives only in git."
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
    block = _entry(record, preferred)
    grounding = block.get("gtdb_classification") or {}
    assert grounding.get("gtdb_id") == LEFT_BROAD[(record, preferred)]


def test_the_sharpened_terms_are_not_broader_than_what_they_replaced():
    """A sharpening must move *down* the lineage, never sideways.

    The chosen term has to appear in its own stored lineage below the rank the
    vote would have picked — which is what makes it the same clade rather than
    a different one.
    """
    ranks = ["d__", "p__", "c__", "o__", "f__", "g__"]
    for (record, preferred), (chosen, would_be) in SHARPENED.items():
        grounding = _entry(record, preferred).get("gtdb_classification") or {}
        lineage = grounding.get("gtdb_lineage") or ""
        chosen_name = chosen.split(":", 1)[1]
        broad_name = would_be.split(":", 1)[1]

        assert chosen_name in lineage.split(";"), f"{chosen} missing from its own lineage"
        assert broad_name in lineage.split(";"), (
            f"{would_be} should still appear in {record}'s lineage — a sharpening "
            f"stays inside the broader taxon, it does not move to another one"
        )
        assert ranks.index(chosen_name[:3]) > ranks.index(
            broad_name[:3]
        ), f"{chosen} is not finer than {would_be}"
