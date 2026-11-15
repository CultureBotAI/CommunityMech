"""Finite typed Quantity values and the soil pH unit boundary (#2702, #2703)."""

from __future__ import annotations

import functools
import math
from collections.abc import Iterator

from linkml_runtime.utils.schemaview import SchemaView  # type: ignore[import-untyped]

from communitymech.paths import REPO_ROOT


@functools.lru_cache(maxsize=1)
def _schema() -> SchemaView:
    return SchemaView(str(REPO_ROOT / "src/communitymech/schema/communitymech.yaml"))


def _quantities(value: object, class_name: str, path: str = "") -> Iterator[tuple[str, dict]]:
    """Follow schema class ranges, never guess Quantity from a dict's key names."""
    if not isinstance(value, dict):
        return
    if class_name == "Quantity":
        yield path, value
        return
    schema = _schema()
    for slot in schema.class_induced_slots(class_name):
        if slot.range not in schema.all_classes():
            continue
        child = value.get(slot.name)
        child_path = f"{path}.{slot.name}" if path else slot.name
        if isinstance(child, list):
            for index, item in enumerate(child):
                yield from _quantities(item, slot.range, f"{child_path}[{index}]")
        else:
            yield from _quantities(child, slot.range, child_path)


def check_record(instance: dict) -> Iterator[tuple[str, str]]:
    """Yield strict errors; schema validation owns missing values and wrong types."""
    if not isinstance(instance, dict):
        return
    for path, quantity in _quantities(instance, "MicrobialCommunity"):
        value = quantity.get("value")
        if isinstance(value, (int, float)) and not math.isfinite(value):
            yield "quantity_nonfinite", f"{path}.value: Quantity values must be finite"
    for index, soil in enumerate(instance.get("soils") or []):
        if not isinstance(soil, dict) or not isinstance(soil.get("ph"), dict):
            continue
        unit = soil["ph"].get("unit")
        if isinstance(unit, dict) and unit.get("id") != "UO:0000196":
            yield (
                "soil_ph_unit",
                f"soils[{index}].ph.unit: pH requires UO:0000196, not {unit.get('id')}",
            )
