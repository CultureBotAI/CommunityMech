"""A grounding just over 0.5 is a coin flip that landed right (#396).

#394 moved the threshold from `>=0.5` to `>0.5`, so a tie-break can no longer
*decide* a grounding. That is narrower than it sounds, and #396 was filed so the
stronger reading does not take hold: it removed the exact ties, not the near
ones. Four blocks sit at **0.50098** — 226306 against 225423, a margin of 883
genomes in 451729.

The marker is advisory. It stores nothing and withholds nothing, because there is
no natural cut point in the distribution and raising the threshold is a curation
policy call (#396 option 3, rejected there). What it does is tell a curator at
the moment of decision.

#416 is why that matters. NCBI *Nitrospiraceae* grounds to
`f__Leptospirillaceae` at 0.534 — and *Leptospirillum* is an **iron** oxidizer
while the record's genome is its **nitrite** oxidizer. The majority vote would
have assigned the wrong physiology, wearing a confidence number that looked like
a decision rather than a coin flip.
"""

from __future__ import annotations

import importlib.util
import pathlib
import subprocess
from pathlib import Path

import pytest
import yaml
from genus_gtdb_successors import admit_genus_successor
from shrimp_lane_gtdb_successors import BEFORE as SHRIMP_BEFORE
from shrimp_lane_gtdb_successors import THERMO_PATH, admit_shrimp_lane_successor

from communitymech.paths import taxon_descriptor_roots
from communitymech.taxon_blocks import iter_taxon_descriptors

REPO = Path(__file__).parent.parent
ALGAL = "kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml"
ALGAL_BEFORE = "d317416542deab471a12785f688c23d08ed5a7eea2894dbde489f40c0df80806"


# A GTDB grounding can live on any `TaxonDescriptor`, and the schema hangs that
# class off two roots: MicrobialCommunity.taxonomy[].taxon_term and
# CommonTaxon.taxon_term. So this needs BOTH the wider directory list and the
# shared walker -- iterating `document["taxonomy"]` over kb/taxa finds nothing,
# because a CommonTaxon has no `taxonomy` key at all (#656, #689).
def _record_paths() -> list[pathlib.Path]:
    return [p for root in taxon_descriptor_roots() for p in sorted(root.glob("*.yaml"))]


def _module():
    spec = importlib.util.spec_from_file_location("_gtdb", REPO / "scripts/gtdb_ground.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.mark.parametrize(
    ("fraction", "expected"),
    [
        (0.50098, True),  # the four Bacillota blocks
        (0.501, True),
        (0.534, True),  # the #416 Nitrospiraceae case
        (0.5449, True),
        (0.55, False),  # the bound is exclusive
        (0.57, False),  # g__Bacillus, the next real population up
        (1.0, False),
        # "unknown" is not "marginal". (A curated block may still carry a
        # fraction — the KB's does, at 0.5 — so this is about absence, not
        # about curation.)
        (None, False),
        ("0.5", False),
        # Booleans are ints in Python. They are excluded by the range rather
        # than by a type guard: `True` is 1 (above the bound) and `False` is 0
        # (fails `0 < fraction`). An explicit guard was dead code.
        (True, False),
        (False, False),
        (0, False),
    ],
)
def test_the_predicate_fires_only_on_a_near_tie(fraction, expected):
    assert _module()._is_near_tie(fraction) is expected


def test_the_bound_is_where_the_population_gap_is():
    """The threshold is a judgement call, so pin what justified it.

    5 blocks below 0.55, then a gap to 0.57. If the KB drifts so the marker
    covers a crowd, it stops pointing at anything and should be revisited.
    """
    fractions = sorted(
        block["majority_fraction"]
        for _, block in _grounded()
        if isinstance(block.get("majority_fraction"), (int, float))
    )
    marked = [f for f in fractions if f < _module().NEAR_TIE_BELOW]

    assert len(marked) <= 12, (
        f"{len(marked)} of {len(fractions)} groundings are now near-ties; the "
        f"marker is supposed to single out the marginal few (#396)"
    )
    assert marked, "no near-ties at all — either the KB changed or the bound is wrong"


def _grounded():
    for path in _record_paths():
        for descriptor in iter_taxon_descriptors(yaml.safe_load(path.read_text())):
            block = descriptor.get("gtdb_classification")
            if block:
                yield path.relative_to(REPO).as_posix(), block


def _known_uncurated_near_tie(name, block):
    """Preserve historical Bacillota plus exact source-bound additions (#2947)."""
    if name == THERMO_PATH:
        current = (REPO / name).read_bytes()
        admission = admit_shrimp_lane_successor(REPO, name, SHRIMP_BEFORE[name], current=current)
        assert admission.changed, "reviewed Thermophilic mapping proof is required"
        descriptors = yaml.safe_load(current)["taxonomy"]
        expected = {
            "GTDB:p__Methanobacteriota": (0, 2815, 5300, 0.531),
            "GTDB:p__Bacillota_A": (1, 226306, 451729, 0.501),
        }
        assert block["gtdb_id"] in expected, "inspected near-tie block differs"
        index, support, total, fraction = expected[block["gtdb_id"]]
        assert (
            block == descriptors[index]["taxon_term"]["gtdb_classification"]
        ), "inspected near-tie block differs"
        assert (block["support_genomes"], block["total_genomes"], block["majority_fraction"]) == (
            support,
            total,
            fraction,
        )
        return True
    if name != ALGAL:
        return block["gtdb_id"] == "GTDB:p__Bacillota_A"
    current = (REPO / name).read_bytes()
    admission = admit_genus_successor(REPO, name, ALGAL_BEFORE, current=current)
    assert admission.changed, "reviewed Algal mapping proof is required"
    descriptor = yaml.safe_load(current)["taxonomy"][2]["taxon_term"]
    assert block == descriptor["gtdb_classification"], "inspected near-tie block differs"
    assert block["gtdb_id"] == "GTDB:g__Leptolyngbya"
    assert (block["support_genomes"], block["total_genomes"], block["majority_fraction"]) == (
        13,
        24,
        0.542,
    )
    return True


def test_the_known_near_ties_are_still_there():
    """The population #396 documents, so it cannot shrink unnoticed.

    The original five blocks were two different things:

    * four `p__Bacillota_A` at 0.50098 — the tool's own output, retained because
      0.50098 > 0.5. These are what #396 is about.
    * one `g__Syntrophotalea` at exactly 0.5, which the threshold would reject.
      It is in the KB because a curator pinned it against the vote (#384), and
      it carries `curated: true` saying so.

    That second one is why the *flag* stays a pure function of the fraction while
    the *judgement* does not: 0.5 really is a coin flip, and the record already
    answers "should someone look at this" with a curation note.
    Later source-bound additions require their complete current strict proof;
    their admission does not recast a narrow majority as stock identification.
    """
    near = [
        (name, block)
        for name, block in _grounded()
        if _module()._is_near_tie(block.get("majority_fraction"))
    ]
    uncurated = [(name, block) for name, block in near if not block.get("curated")]

    bacillota = [block for _, block in uncurated if block["gtdb_id"] == "GTDB:p__Bacillota_A"]
    assert len(bacillota) >= 4, f"expected the 0.50098 Bacillota blocks, found {near}"
    assert all(_known_uncurated_near_tie(name, block) for name, block in uncurated), uncurated
    # Every block at or below the strict threshold must be a deliberate override,
    # or the threshold is not being enforced.
    for name, block in _grounded():
        fraction = block.get("majority_fraction")
        if isinstance(fraction, (int, float)) and fraction <= 0.5:
            assert block.get("curated") is True, (
                f"{name}: {block['gtdb_id']} sits at {fraction} with no `curated` "
                f"flag — a non-majority grounding that nobody chose (#394)"
            )


@pytest.mark.parametrize(
    ("name", "marked"),
    [
        ("Bacillota", True),  # 0.501 -- 226306/451729
        ("Nitrospiraceae", True),  # 0.534 -- the #416 case
        ("Bacillus", False),  # 0.57 -- just above
        ("Steroidobacteraceae", False),  # 1.0
    ],
)
def test_the_cli_marks_the_right_groundings(name, marked):
    """End to end through the CLI, which is where a curator actually sees it."""
    result = subprocess.run(
        ["uv", "run", "python", "scripts/gtdb_ground.py", "--name", name],
        capture_output=True,
        text=True,
        cwd=REPO,
        timeout=900,
    )
    lines = [ln for ln in result.stdout.splitlines() if "majority" in ln]
    if not lines:
        pytest.skip(f"{name} no longer grounds; this test is stale")

    assert ("NEAR-TIE" in lines[0]) is marked, lines[0]


def test_the_marker_does_not_replace_thin():
    """Two different weaknesses; a block can have either, both, or neither.

    THIN is "too few genomes to say anything"; NEAR-TIE is "plenty of genomes,
    split down the middle". Collapsing them would hide the 0.50098 blocks, which
    have 451729 genomes and are anything but thin.
    """
    source = (REPO / "scripts/gtdb_ground.py").read_text()

    assert "⚠ THIN" in source and "⚠ NEAR-TIE" in source
    assert "{thin}{near}" in source, "both markers should be able to appear together"
