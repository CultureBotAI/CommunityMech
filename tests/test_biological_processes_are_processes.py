"""`biological_processes` must hold GO *biological process* terms (#751).

`BiologicalProcessDescriptor.term` is described as "GO biological process term",
and `just validate-terms` checks that an id and its label agree. Nothing checked
the aspect, so a molecular function or a cellular component with a perfectly
correct label passed every gate. **32 entries did**: 28 molecular functions
(`GO:0009055` electron transfer activity, `GO:0008810` cellulase activity,
`GO:0018597` ammonia monooxygenase activity, ...), 2 cellular components
(`GO:0005576` extracellular region), and 3 that do not resolve at all.

That is not a naming quibble. An enzyme activity is a property of a protein and
a cellular component is a place; neither is something a community *does*, and a
KGX consumer reading this slot as "processes" gets statements of a different
kind mixed in.

The aspect is checked **structurally** — GO's three roots are `GO:0008150`
biological_process, `GO:0005575` cellular_component and `GO:0003674`
molecular_function, and every term descends from exactly one. A label check
would not do: "electron transfer activity" reads like a process to anyone not
looking it up.
"""

from __future__ import annotations

import collections

import pytest
import yaml

from communitymech.ontology_adapters import ontology_adapter
from communitymech.paths import record_files

ROOTS = {
    "GO:0008150": "biological_process",
    "GO:0005575": "cellular_component",
    "GO:0003674": "molecular_function",
}

# `GO:0070812` organohalide respiration resolves to nothing in the pinned GO
# build and is already carried as an exception in conf/id_label_targets.yaml.
# It is a process by any reading; its aspect is simply unaskable here, so it is
# exempted from the aspect check and from nothing else.
UNRESOLVABLE = {"GO:0070812"}


@pytest.fixture(scope="module")
def go():
    adapter = ontology_adapter("GO")
    if adapter is None:
        pytest.skip("no local GO build available")
    return adapter


def _entries():
    for path in record_files():
        doc = yaml.safe_load(path.read_text()) or {}
        for interaction in doc.get("ecological_interactions") or []:
            for item in interaction.get("biological_processes") or []:
                term = (item or {}).get("term") or {}
                if term.get("id"):
                    yield path.name, interaction.get("name"), term["id"], term.get("label")


def _aspect(go, curie, cache):
    if curie not in cache:
        try:
            ancestors = set(go.ancestors([curie], predicates=["rdfs:subClassOf"]))
        except Exception:
            ancestors = set()
        cache[curie] = next((v for k, v in ROOTS.items() if k in ancestors), "unresolved")
    return cache[curie]


def test_every_entry_is_a_biological_process(go):
    cache: dict[str, str] = {}
    offenders = []
    for record, interaction, curie, label in _entries():
        if not curie.startswith("GO:") or curie in UNRESOLVABLE:
            continue
        aspect = _aspect(go, curie, cache)
        if aspect != "biological_process":
            offenders.append(f"{record} [{interaction}]: {curie} {label!r} is a {aspect}")
    assert offenders == [], (
        "these `biological_processes` entries are not biological processes "
        "(#751). Use the process term, not the activity or the location — e.g. "
        "cellulase activity -> GO:0030245 cellulose catabolic process:\n" + "\n".join(offenders)
    )


def test_the_check_can_actually_fail(go):
    """A molecular function must be rejected by the same predicate the test uses.

    Pins the mechanism rather than the data: if `_aspect` ever returned
    "biological_process" for everything — an exception swallowed, a wrong
    predicate — the test above would pass on a corpus full of enzyme activities.
    """
    cache: dict[str, str] = {}
    assert _aspect(go, "GO:0009055", cache) == "molecular_function"
    assert _aspect(go, "GO:0005576", cache) == "cellular_component"
    assert _aspect(go, "GO:0030245", cache) == "biological_process"


def test_no_interaction_lists_the_same_process_twice():
    """Regrounding two different activities onto one process term can collide —
    `ammonia monooxygenase activity` and `ammonia oxidation` both became
    `GO:0019329`. 13 such pairs existed after the #751 sweep; 2 predated it.
    """
    duplicates = []
    per_interaction: dict[tuple[str, str], list[str]] = collections.defaultdict(list)
    for record, interaction, curie, _ in _entries():
        per_interaction[(record, interaction)].append(curie)
    for (record, interaction), curies in per_interaction.items():
        for curie, count in collections.Counter(curies).items():
            if count > 1:
                duplicates.append(f"{record} [{interaction}]: {curie} x{count}")
    assert (
        duplicates == []
    ), "these interactions list one process term more than once (#751):\n" + "\n".join(duplicates)
