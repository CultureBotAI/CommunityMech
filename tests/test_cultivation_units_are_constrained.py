"""The `CultivationSetup` unit slots are enums now, not free text (#514).

Six slots on `CultivationSetup` carry a unit or a kind — `working_volume_unit`,
`operating_temperature_unit`, `feed_or_dilution_rate_unit`,
`retention_time_unit`, `applied_potential_unit`, `retention_time_type` — and
every one of them had **no range**, so `linkml-validate` accepted any string.

That is not hypothetical drift. Adding two records to the #183 sweep I wrote
`retention_time_unit: HOURS` and `feed_or_dilution_rate_unit: PER_HOUR`,
enum-shaped because `cultivation_mode` and `system_type` sit right beside them
and *are* enums. The corpus had been writing symbols: `h`, `d`, `L/day`, `mL`.
Nothing failed. I found it by grepping what other records had used.

`retention_time_type` is the sharper case, because there the convention was
never ambiguous — the slot description has said `"HRT" or "SRT"` since it was
written, and a record still arrived saying `HYDRAULIC`. A description is not a
constraint. Setting the range caught it on the first `just validate-all`.

Why symbols rather than SCREAMING_CASE, given the neighbouring enums: a unit is
not a category. `°C` and `1/h` are the notation every source and every reader
already uses, and a slot that says `PER_HOUR` has to be translated back before
it means anything. The cost is that permissible values here are not valid Python
identifiers — LinkML emits them through `_addvals`/`setattr` rather than as
class attributes, which is why `test_the_generated_datamodel_carries_them`
below checks the runtime enum rather than `dir()`.

What this file defends is that the ranges stay attached. Deleting a `range:`
line is a one-character-looking edit that silently reopens free text, and no
existing test would notice — the corpus would still validate, because every
value in it is already legal.
"""

from __future__ import annotations

import pathlib
import subprocess

import pytest
import yaml

from communitymech.paths import record_files

REPO = pathlib.Path(__file__).parent.parent
SCHEMA = REPO / "src/communitymech/schema/communitymech.yaml"

# Both record roots, not kb/communities alone. `data/isolates` holds the same
# root class -- 4 records with 66 snippets, 3 ecological_interactions and 3
# gtdb_classification blocks -- and this module could not see any of it (#689).

# slot -> the enum it must be ranged to.
CONSTRAINED = {
    "working_volume_unit": "VolumeUnitEnum",
    "operating_temperature_unit": "TemperatureUnitEnum",
    "feed_or_dilution_rate_unit": "RateUnitEnum",
    "retention_time_unit": "TimeUnitEnum",
    "applied_potential_unit": "PotentialUnitEnum",
    "retention_time_type": "RetentionTimeTypeEnum",
}


@pytest.fixture(scope="module")
def schema() -> dict:
    return yaml.safe_load(SCHEMA.read_text(encoding="utf-8"))


@pytest.mark.parametrize(("slot", "enum_name"), sorted(CONSTRAINED.items()))
def test_the_slot_is_ranged_to_its_enum(schema, slot: str, enum_name: str):
    """The whole point: a missing `range` is free text again, silently."""
    attributes = schema["classes"]["CultivationSetup"]["attributes"]
    assert slot in attributes, f"{slot} is gone from CultivationSetup"
    assert attributes[slot].get("range") == enum_name, (
        f"`{slot}` is no longer ranged to {enum_name}. Without a range the slot "
        f"accepts any string, which is how `HOURS`, `PER_HOUR` and `HYDRAULIC` "
        f"got in (#514). If the enum was genuinely too narrow, widen the enum "
        f"rather than dropping the range."
    )


def test_every_value_in_the_corpus_is_permissible(schema):
    """Guard the other way: the enums must cover what curation actually writes.

    If this fails the fix is usually to add a permissible value, not to relax
    the slot — but it should fail loudly either way rather than have someone
    reach for `range:` deletion.
    """
    enums = schema["enums"]
    offenders = []
    for path in record_files():
        for entry in (yaml.safe_load(path.read_text()) or {}).get("cultivation_setup") or []:
            for slot, enum_name in CONSTRAINED.items():
                value = entry.get(slot)
                if value is None:
                    continue
                if value not in enums[enum_name]["permissible_values"]:
                    offenders.append(f"{path.name}: {slot}={value!r} not in {enum_name}")
    assert offenders == [], "\n".join(offenders)


def test_the_corpus_actually_uses_these_slots():
    """Guard: at zero populated slots the test above passes on nothing."""
    populated = sum(
        1
        for path in record_files()
        for entry in (yaml.safe_load(path.read_text()) or {}).get("cultivation_setup") or []
        for slot in CONSTRAINED
        if entry.get(slot) is not None
    )
    assert populated >= 10, (
        f"only {populated} constrained unit slots are populated across the "
        f"corpus; the coverage test above is close to vacuous"
    )


def test_the_generated_datamodel_carries_them():
    """`°C` and `1/h` are not Python identifiers, so check the runtime enum.

    LinkML emits them via a `_addvals` classmethod using `setattr`, not as
    class attributes — `dir()` and a static import both miss them, which is
    exactly the sort of check that would pass while the value was absent.
    """
    from communitymech.datamodel.communitymech import RateUnitEnum, TemperatureUnitEnum

    assert getattr(TemperatureUnitEnum, "°C", None) is not None
    assert getattr(RateUnitEnum, "1/h", None) is not None


def test_a_wrong_unit_is_actually_rejected(tmp_path):
    """Mutation check, run against the real validator.

    Every test above reads the schema and would pass if `linkml-validate`
    ignored these ranges entirely. This one asserts the gate bites: it takes a
    real record, writes the exact string this issue was filed about, and
    requires a non-zero exit.
    """
    source = next(p for p in record_files() if "operating_temperature_unit: °C" in p.read_text())
    broken = tmp_path / "broken.yaml"
    broken.write_text(
        source.read_text().replace(
            "operating_temperature_unit: °C", "operating_temperature_unit: CELSIUS", 1
        ),
        encoding="utf-8",
    )
    result = subprocess.run(
        ["uv", "run", "linkml-validate", "-s", str(SCHEMA), str(broken)],
        capture_output=True,
        text=True,
        cwd=REPO,
        timeout=900,
    )
    assert result.returncode != 0, (
        "`operating_temperature_unit: CELSIUS` validated clean, so the enum "
        "range is not being enforced and #514 is open again"
    )
    assert "CELSIUS" in result.stdout + result.stderr


def test_the_reference_electrode_is_not_smuggled_into_the_unit(schema):
    """`applied_potential_unit` is a unit; "vs SHE" is not part of one.

    The slot description used to offer `"mV vs SHE"` as an example, which makes
    the value a unit *and* a reference electrode at once — unjoinable across
    records, and unconvertible. The enum is {V, mV}; the reference belongs in
    `electrode_detail`. Asserted positively, on the description saying where it
    goes, because a check that "SHE" is absent would also pass on a description
    rewritten to say nothing at all.
    """
    attributes = schema["classes"]["CultivationSetup"]["attributes"]
    values = schema["enums"]["PotentialUnitEnum"]["permissible_values"]
    assert set(values) == {"V", "mV"}
    described = schema["enums"]["PotentialUnitEnum"]["description"]
    assert "electrode_detail" in described, (
        "PotentialUnitEnum no longer says where the reference electrode goes, "
        "so the next curator will put it back in the unit (#514)"
    )
    assert "applied_potential_unit" in attributes
