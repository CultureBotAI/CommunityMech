"""Some GO terms are true of every record here, so they annotate nothing (#182).

The #180 id↔label cleanup remapped obsolete GO ids to their nearest *valid*
term. For a handful that meant climbing to a near-root process, and the result
was sixteen annotations reading

    - preferred_term: metabolic process
      term:
        id: GO:0008152
        label: metabolic process

on records in a knowledge base about **microbial communities**, every one of
which does metabolism. Nine were exactly that and were dropped. Seven carried a
real concept in `preferred_term` that had been flattened onto the generic
parent, and were re-grounded rather than deleted:

    organic substance catabolic process  ->  GO:0009056  catabolic process
    nitrogen compound metabolic process  ->  GO:0071941  nitrogen cycle metabolic process

Both targets are current; the precise terms a curator would want
(`GO:0006807`, `GO:1901575`) are **obsolete in GO**, which is why they were
flattened in the first place. `GO:0071941` was already used twice elsewhere in
the KB, so this follows an existing convention rather than inventing one.

`term` is `required: true` on `BiologicalProcessDescriptor`, so "drop the
annotation" necessarily means dropping the whole descriptor — there is no way to
keep an ungrounded `preferred_term`. That is why upgrading beats deleting
wherever a current term exists.
"""

from __future__ import annotations

import pathlib

import pytest
import yaml

from communitymech.paths import record_files

REPO = pathlib.Path(__file__).parent.parent

# Both record roots, not kb/communities alone. `data/isolates` holds the same
# root class -- 4 records with 66 snippets, 3 ecological_interactions and 3
# gtdb_classification blocks -- and this module could not see any of it (#689).

# GO terms so close to the root of the biological-process branch that asserting
# them of a microbial community conveys nothing. Each needs a reason, so that
# adding one is a decision rather than a reflex.
_VACUOUS = {
    "GO:0008152": "'metabolic process' — true of every organism in the KB",
    "GO:0008150": "'biological_process' — the branch root",
}


def _walk(node, filename):
    """Descriptors under `node`. Module-level so it does not close over the loop
    variable — a nested closure here reads `path` from the enclosing scope at
    *call* time, which for a generator is after the loop has moved on (ruff
    B023). Harmless in this shape, wrong the moment the generator is not drained
    immediately."""
    if isinstance(node, dict):
        term = node.get("term")
        if node.get("preferred_term") and isinstance(term, dict) and term.get("id"):
            yield filename, node["preferred_term"], term["id"], term.get("label")
        for value in node.values():
            yield from _walk(value, filename)
    elif isinstance(node, list):
        for value in node:
            yield from _walk(value, filename)


def _descriptors(corpus: pathlib.Path | None = None):
    """Every (file, preferred_term, id, label) biological-process descriptor."""
    for path in sorted(corpus.glob("*.yaml")) if corpus else record_files():
        document = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        yield from _walk(document, path.name)


def test_no_record_is_annotated_with_a_vacuous_process():
    """The gate."""
    offenders = [
        f"{name}: {preferred!r} -> {identifier} ({_VACUOUS[identifier]})"
        for name, preferred, identifier, _label in _descriptors()
        if identifier in _VACUOUS
    ]
    assert offenders == [], (
        "these annotations are true of every community in the KB and so "
        "distinguish nothing (#182). Ground the concept in `preferred_term` to "
        "a specific current GO term, or drop the descriptor:\n"
        + "\n".join(f"  {line}" for line in offenders)
    )


def test_the_upgraded_terms_are_present_and_correctly_labelled():
    """The seven that were re-grounded rather than deleted.

    Asserts the label travelled with the id: a remap that changed one and not
    the other is the exact defect #180 existed to clear, and re-introducing it
    here would be ironic.
    """
    by_id = {}
    for _name, _preferred, identifier, label in _descriptors():
        by_id.setdefault(identifier, set()).add(label)

    assert by_id.get("GO:0009056") == {
        "catabolic process"
    }, f"GO:0009056 carries unexpected labels: {by_id.get('GO:0009056')}"
    assert by_id.get("GO:0071941") == {
        "nitrogen cycle metabolic process"
    }, f"GO:0071941 carries unexpected labels: {by_id.get('GO:0071941')}"


@pytest.mark.parametrize("identifier", sorted(_VACUOUS))
def test_every_blocked_term_has_a_reason(identifier):
    """A blocklist without reasons becomes a place things get added silently."""
    assert _VACUOUS[identifier].strip()


def test_the_walk_reaches_the_corpus():
    """An empty walk passes the gate as surely as a clean corpus does."""
    seen = list(_descriptors())
    assert len(seen) > 500, f"only {len(seen)} descriptors walked; the walk is broken"


def test_the_gate_can_fire(tmp_path):
    """Mutation check, driving the real walk over a record built to offend."""
    corpus = tmp_path / "communities"
    corpus.mkdir()
    (corpus / "r.yaml").write_text(
        "id: CommunityMech:000999\n"
        "ecological_interactions:\n"
        "- biological_processes:\n"
        "  - preferred_term: metabolic process\n"
        "    term:\n"
        "      id: GO:0008152\n"
        "      label: metabolic process\n",
        encoding="utf-8",
    )
    offenders = [d for d in _descriptors(corpus) if d[2] in _VACUOUS]
    assert offenders, "the gate found nothing in a record built to contain the defect"
    assert offenders[0][1] == "metabolic process"


def test_a_specific_process_is_not_flagged(tmp_path):
    """Guard against the gate being over-broad.

    A correctly grounded specific term also has `preferred_term == label`; that
    is what good curation looks like, not a defect. The gate must key on the
    identifier, never on the two strings matching.
    """
    corpus = tmp_path / "communities"
    corpus.mkdir()
    (corpus / "r.yaml").write_text(
        "id: CommunityMech:000998\n"
        "ecological_interactions:\n"
        "- biological_processes:\n"
        "  - preferred_term: nitrogen cycle metabolic process\n"
        "    term:\n"
        "      id: GO:0071941\n"
        "      label: nitrogen cycle metabolic process\n",
        encoding="utf-8",
    )
    assert [d for d in _descriptors(corpus) if d[2] in _VACUOUS] == []
