"""Record-local arm/member/timepoint references and observation bounds (#2796).

These are structural consistency checks, not proof that an assay comparison or
causal claim is supported. Legacy scalar abundances remain deliberately unscoped.
"""

from __future__ import annotations

import math
from collections import Counter
from collections.abc import Iterator


def _objects(value: object) -> list[dict]:
    return [item for item in value if isinstance(item, dict)] if isinstance(value, list) else []


def _index(items: list[dict], key: str) -> tuple[dict[str, dict], set[str]]:
    counts = Counter(item[key] for item in items if isinstance(item.get(key), str) and item[key])
    duplicates = {identifier for identifier, count in counts.items() if count > 1}
    return (
        {
            item[key]: item
            for item in items
            if isinstance(item.get(key), str) and counts[item[key]] == 1
        },
        duplicates,
    )


def _references(value: object) -> list[str]:
    """Safe lookup inputs; callers separately reject malformed raw entries."""
    return [item for item in value if isinstance(item, str)] if isinstance(value, list) else []


def _reference_type_errors(value: object, path: str) -> Iterator[tuple[str, str]]:
    """Never turn malformed declared references into silently absent scope (#2807)."""
    if value is None:
        return
    if not isinstance(value, list):
        yield "treatment_reference_type", f"{path}: expected a list of string identifiers"
        return
    for index, reference in enumerate(value):
        if not isinstance(reference, str):
            yield (
                "treatment_reference_type",
                f"{path}[{index}]: expected a string identifier, got {type(reference).__name__}",
            )


def _text(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _measurements(observation: dict, path: str) -> Iterator[tuple[str, str]]:
    if not _text(observation.get("measurement_basis")):
        yield "treatment_abundance_measure", f"{path}: measurement_basis must contain text"
    if not any(
        observation.get(key) is not None for key in ("absolute_abundance", "relative_abundance")
    ):
        yield "treatment_abundance_measure", f"{path}: at least one abundance value is required"
    for kind in ("absolute", "relative"):
        key = f"{kind}_abundance"
        value, unit = observation.get(key), observation.get(f"{key}_unit")
        if (value is not None) != _text(unit):
            yield (
                "treatment_abundance_measure",
                f"{path}.{key}: a value and explicit unit must be paired",
            )
        if key not in observation:
            continue
        if (
            isinstance(value, bool)
            or not isinstance(value, (int, float))
            or (isinstance(value, float) and not math.isfinite(value))
            or value < 0
        ):
            yield "treatment_abundance_value", f"{path}.{key}: value must be finite and nonnegative"
            continue
        limit = (
            {"FRACTION": 1, "PERCENT": 100}.get(unit)
            if kind == "relative" and isinstance(unit, str)
            else None
        )
        if limit is not None and value > limit:
            yield "treatment_abundance_value", f"{path}.{key}: {unit} cannot exceed {limit}"


def check_record(instance: dict) -> Iterator[tuple[str, str]]:
    """Yield categories/messages through the maintained strict gate."""
    if not isinstance(instance, dict):
        return
    taxonomy = _objects(instance.get("taxonomy"))
    arms = _objects(instance.get("treatment_arms"))
    for index, member in enumerate(taxonomy):
        identifier = member.get("member_id")
        if identifier is not None and not isinstance(identifier, str):
            yield "treatment_reference_type", f"taxonomy[{index}].member_id: expected a string"
    # The current ontology plugin's reflexive ancestry accepts include_self:false
    # roots (#2802). Protect only these new slots here; all descendant and label
    # validation still belongs to the ordinary ontology gate.
    factor_groups = [("environmental_factors", _objects(instance.get("environmental_factors")))]
    factor_groups.extend(
        (f"treatment_arms[{index}].conditions", _objects(arm.get("conditions")))
        for index, arm in enumerate(arms)
    )
    for path, factors in factor_groups:
        for index, factor in enumerate(factors):
            term = factor.get("term")
            if isinstance(term, dict) and term.get("id") in (
                "CHEBI:24431",
                "PATO:0000001",
                "ENVO:01000203",
            ):
                yield (
                    "environmental_factor_generic_root",
                    f"{path}[{index}].term: use a supported specific term or omit this field",
                )
    members, duplicate_members = _index(taxonomy, "member_id")
    arm_index, duplicate_arms = _index(arms, "id")
    for kind, duplicates in (("member", duplicate_members), ("arm", duplicate_arms)):
        for identifier in sorted(duplicates):
            yield "treatment_duplicate_id", f"{kind} identifier {identifier!r} is not unique"

    timepoints: dict[str, dict[str, dict]] = {}
    for position, arm in enumerate(arms):
        arm_id = arm.get("id")
        path = f"treatment_arms[{position}]"
        for field in ("id", "name", "context"):
            if not _text(arm.get(field)):
                yield "treatment_required_value", f"{path}.{field}: a nonempty value is required"
        points, duplicates = _index(_objects(arm.get("timepoints")), "id")
        if isinstance(arm_id, str) and arm_id not in duplicate_arms:
            timepoints[arm_id] = points
        for identifier in sorted(duplicates):
            yield "treatment_duplicate_id", f"{path}: timepoint {identifier!r} is not unique"
        for point in _objects(arm.get("timepoints")):
            for field in ("id", "name"):
                if not _text(point.get(field)):
                    yield "treatment_required_value", f"{path}.timepoints.{field}: text is required"
            elapsed = point.get("elapsed")
            unit = elapsed.get("unit") if isinstance(elapsed, dict) else None
            if isinstance(unit, dict) and unit.get("id") == "UO:0000003":
                yield (
                    "time_quantity_generic_root",
                    f"{path}.{point.get('id')}: elapsed requires a specific time unit",
                )
            if point.get("elapsed") is not None and not _text(point.get("reference_event")):
                yield (
                    "treatment_timepoint_anchor",
                    f"{path}.{point.get('id')}: elapsed requires an explicit reference_event",
                )
        participants = _references(arm.get("participant_member_ids"))
        comparators = _references(arm.get("comparator_arm_ids"))
        for key, references in (
            ("participant_member_ids", participants),
            ("comparator_arm_ids", comparators),
        ):
            yield from _reference_type_errors(arm.get(key), f"{path}.{key}")
            if len(references) != len(set(references)):
                yield "treatment_duplicate_reference", f"{path}.{key}: duplicate references"
        for participant in participants:
            if participant not in members:
                yield (
                    "treatment_unknown_reference",
                    f"{path}: member {participant!r} is absent or ambiguous",
                )
        status = arm.get("membership_status")
        if not isinstance(status, str) or status not in {
            "DEFINED_MEMBERS",
            "NO_MICROBES",
            "NOT_REPORTED",
        }:
            yield (
                "treatment_required_value",
                f"{path}.membership_status: an explicit status is required",
            )
        if (status == "DEFINED_MEMBERS" and not participants) or (
            isinstance(status, str) and status in {"NO_MICROBES", "NOT_REPORTED"} and participants
        ):
            yield (
                "treatment_membership_scope",
                f"{path}: {status} is inconsistent with participant_member_ids",
            )
        for comparator in comparators:
            target = arm_index.get(comparator)
            if target is None:
                yield (
                    "treatment_unknown_reference",
                    f"{path}: comparator {comparator!r} is absent or ambiguous",
                )
            elif comparator == arm_id or target.get("context") != arm.get("context"):
                yield (
                    "treatment_comparator_scope",
                    f"{path}: comparator must be a different arm in the same context",
                )

    for index, member in enumerate(taxonomy):
        member_id = member.get("member_id")
        observations = _objects(member.get("abundance_observations"))
        if observations and (not isinstance(member_id, str) or member_id not in members):
            yield (
                "treatment_observation_scope",
                f"taxonomy[{index}]: observations require a unique member_id",
            )
        for position, observation in enumerate(observations):
            path = f"taxonomy[{index}].abundance_observations[{position}]"
            yield from _measurements(observation, path)
            arm_id = observation.get("treatment_arm_id")
            observed_arm = arm_index.get(arm_id) if isinstance(arm_id, str) else None
            if not isinstance(arm_id, str) or observed_arm is None:
                yield (
                    "treatment_unknown_reference",
                    f"{path}: arm {arm_id!r} is absent or ambiguous",
                )
                continue
            point_id = observation.get("timepoint_id")
            if point_id is not None and (
                not isinstance(point_id, str) or point_id not in timepoints.get(arm_id, {})
            ):
                yield (
                    "treatment_unknown_reference",
                    f"{path}: timepoint {point_id!r} is absent or ambiguous in {arm_id}",
                )
            status = observed_arm.get("membership_status")
            if status == "NO_MICROBES" or (
                status == "DEFINED_MEMBERS"
                and member_id not in _references(observed_arm.get("participant_member_ids"))
            ):
                yield (
                    "treatment_observation_scope",
                    f"{path}: member is excluded by the arm's explicit roster",
                )

    for index, interaction in enumerate(_objects(instance.get("ecological_interactions"))):
        yield from _reference_type_errors(
            interaction.get("treatment_arm_ids"),
            f"ecological_interactions[{index}].treatment_arm_ids",
        )
        references = _references(interaction.get("treatment_arm_ids"))
        if len(references) != len(set(references)):
            yield (
                "treatment_duplicate_reference",
                f"ecological_interactions[{index}]: duplicate arm references",
            )
        for arm_id in references:
            if arm_id not in arm_index:
                yield (
                    "treatment_unknown_reference",
                    f"ecological_interactions[{index}]: arm {arm_id!r} is absent or ambiguous",
                )
