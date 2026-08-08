"""The type-species question is a policy choice, not a representational block (#374).

`WITHHELD_GROUNDINGS` justified holding *Nitrospira* by saying the type-bearing
term "would need majority_fraction 0.048, which the **[0.5, 1.0] bound**
rejects". There is no such bound. The schema declares
`majority_fraction: minimum_value 0.0, maximum_value 1.0`; what refuses 0.048 is
`gtdb_ground.py`'s own `if frac > 0.5`, a policy that only a majority grounds.

The distinction is the whole of #374. "Unrepresentable" closes the question —
nothing can be done until the schema changes. "Refused by our own rule" leaves
three live options:

* ground to the non-type split GTDB's genomes favour (`g__Nitrospira_D` at
  0.81);
* ground to the type-bearing term at 0.048 and let the fraction show how thin
  the support is — which is arguably what a confidence field is *for*;
* withhold, which is the status quo.

None is obviously right, so the blocks stay withheld. But they stay withheld as
a decision that has not been made, not as one that cannot be.

These tests pin the two facts that distinguish those readings, because the false
one survived in a code comment long enough to be repeated as fact several times.
"""

from __future__ import annotations

import pathlib

import yaml

REPO = pathlib.Path(__file__).parent.parent
SCHEMA = REPO / "src/communitymech/schema/communitymech.yaml"
TOOL = REPO / "scripts/gtdb_ground.py"


def test_the_schema_permits_a_minority_fraction():
    """0.048 is representable. If this ever fails, #374 really is blocked."""
    attributes = yaml.safe_load(SCHEMA.read_text(encoding="utf-8"))["classes"][
        "GtdbClassification"
    ]["attributes"]["majority_fraction"]
    assert attributes["minimum_value"] == 0.0, (
        f"majority_fraction now has a floor of {attributes['minimum_value']}. If it "
        f"was raised deliberately then #374 is a schema question after all, and the "
        f"WITHHELD notes should say so — they currently say the opposite."
    )
    assert attributes["maximum_value"] == 1.0


def test_the_floor_that_exists_is_the_tool_s_own():
    """`if frac > 0.5` is where a minority is actually refused."""
    assert "if frac > 0.5:" in TOOL.read_text(encoding="utf-8"), (
        "the majority floor has moved or been rewritten; #374's framing depends "
        "on it being a tool policy, so re-check the WITHHELD notes"
    )


def test_the_withheld_notes_do_not_blame_a_schema_bound():
    """The false claim, kept out.

    It read "which the [0.5, 1.0] bound rejects" and was load-bearing: it was
    the stated reason for withholding, and it made the question look settled.
    """
    source = TOOL.read_text(encoding="utf-8")
    assert "[0.5, 1.0] bound" not in source, (
        "a WITHHELD note is blaming a [0.5, 1.0] schema bound again. The schema "
        "permits [0.0, 1.0]; the refusal is this module's own majority policy "
        "(#374)."
    )
    assert "unrepresentable" not in source.lower(), (
        "a WITHHELD note calls the type-bearing grounding unrepresentable. It is "
        "representable — see test_the_schema_permits_a_minority_fraction (#374)."
    )


def test_nitrospira_is_still_withheld_pending_the_decision():
    """Status quo preserved: correcting the reasoning is not making the call."""
    import importlib.util
    import sys

    spec = importlib.util.spec_from_file_location("gtdb_ground", TOOL)
    module = importlib.util.module_from_spec(spec)
    sys.modules["gtdb_ground"] = module
    spec.loader.exec_module(module)

    withheld = {name for _, name in module.WITHHELD_GROUNDINGS}
    assert "Nitrospira-like nitrite oxidizer" in withheld
    assert "Nitrospirae core floodplain members" in withheld
