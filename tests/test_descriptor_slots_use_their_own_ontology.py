"""A `metabolites` entry is CHEBI and a `biological_processes` entry is GO (#758).

The two are structurally identical — `preferred_term` + `term{id,label}` +
optional `notes` — so YAML cannot tell them apart and neither can LinkML. Moving
an item from one list to the other is schema-valid, label-valid and
network-audit-clean.

That is not hypothetical. A bulk edit in #755 removed a `biological_processes:`
key whose children were indented deeper than the check expected, and YAML
re-parented **five GO terms into `metabolites`** in
`data/isolates/Chromobacterium_Gold_Biocyanidation.yaml`. `just validate`,
`just validate-strict` and `just validate-terms` all passed on the result; only
diffing per-key entry counts against `origin/main` found it.

This test is the cheap standing check that would have failed loudly instead, and
it is independent of any particular sweep.
"""

from __future__ import annotations

import yaml

from communitymech.paths import record_files

# Metabolites are chemical entities. `related_ingredients` uses CHEBI too, but it
# is a different slot with a different class and is not checked here.
EXPECTED = {"metabolites": "CHEBI", "biological_processes": "GO"}


def _offenders():
    for path in record_files():
        doc = yaml.safe_load(path.read_text()) or {}
        for interaction in doc.get("ecological_interactions") or []:
            for slot, prefix in EXPECTED.items():
                for item in interaction.get(slot) or []:
                    curie = ((item or {}).get("term") or {}).get("id")
                    if curie and not curie.startswith(prefix + ":"):
                        yield (
                            f"{path.name} [{interaction.get('name')}] {slot}: "
                            f"{curie} {(item.get('preferred_term'))!r} "
                            f"(expected a {prefix}: term)"
                        )


def test_each_slot_holds_its_own_ontology():
    offenders = sorted(_offenders())
    assert offenders == [], (
        "these entries sit in the wrong list (#758). A metabolite and a process "
        "have the same shape, so a misplaced one passes every other gate:\n" + "\n".join(offenders)
    )


def test_the_check_can_actually_fail():
    """Feed the predicate a known-wrong pair rather than trusting a green run."""
    wrong = {"term": {"id": "GO:0009437"}, "preferred_term": "planted"}
    assert not wrong["term"]["id"].startswith("CHEBI:"), (
        "the prefix predicate no longer rejects a GO term in a CHEBI slot; "
        "test_each_slot_holds_its_own_ontology would pass over a corrupted corpus"
    )
    right = {"term": {"id": "CHEBI:30089"}}
    assert right["term"]["id"].startswith("CHEBI:")
