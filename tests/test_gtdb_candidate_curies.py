"""`gtdb_candidates` are CURIEs, spelled like the grounding they may become (#415).

They were plain names, on the reasoning — written into the schema — that "they
are candidates, not identifiers". That does not hold up. A candidate names a real
GTDB taxon; being unchosen does not make it identify nothing. Concretely:

* no rank, so the 85 AMBIGUOUS taxa could not be filtered or counted the way #414
  filters groundings — and those are exactly the taxa a curator must return to;
* nothing resolvable, so `RDYJ01` — an alphanumeric GTDB placeholder genus — sat
  in a record meaning nothing to a reader. `GTDB:g__RDYJ01` resolves;
* the old spelling was not even internally consistent: species candidates used a
  space (`Bacillus_A thuringiensis`) while `gtdb_id` uses an underscore, so
  promoting a candidate meant re-deriving it rather than copying it.

The tests below cover the two producers separately (species rank and
genus-or-higher), because they are different code paths that were both wrong.
"""

from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).parent.parent
CURIE = re.compile(r"^GTDB:[cdfgops]__.+")
ROOTS = ("kb/communities", "data/isolates", "kb/taxa")


def _candidate_blocks():
    """(file, preferred_term, candidates) for every taxon carrying candidates."""
    found = []
    for root in ROOTS:
        for path in sorted((REPO / root).glob("*.yaml")):
            document = yaml.safe_load(path.read_text()) or {}
            for entry in document.get("taxonomy") or []:
                term = entry.get("taxon_term") or {}
                candidates = term.get("gtdb_candidates") or []
                if candidates:
                    found.append((path.name, term.get("preferred_term"), candidates))
    return found


def test_the_sweep_finds_the_ambiguous_taxa():
    """Vacuity guard: an empty list would pass every assertion below."""
    blocks = _candidate_blocks()

    assert len(blocks) > 50, f"expected the AMBIGUOUS taxa, found {len(blocks)}"
    assert sum(len(c) for _, _, c in blocks) > 500


def test_every_stored_candidate_is_a_ranked_curie():
    bad = [
        f"{name} / {taxon}: {value!r}"
        for name, taxon, candidates in _candidate_blocks()
        for value in candidates
        if not CURIE.match(str(value))
    ]
    assert not bad, "candidates without a GTDB rank prefix:\n" + "\n".join(bad[:10])


def test_no_candidate_contains_a_space():
    """The old species spelling was `Bacillus_A thuringiensis`.

    `gtdb_id` uses underscores, so a spaced candidate could not be promoted by
    copying — which is the entire point of storing it.
    """
    spaced = [
        f"{name}: {value!r}"
        for name, _, candidates in _candidate_blocks()
        for value in candidates
        if " " in str(value)
    ]
    assert not spaced, spaced[:10]


def test_the_schema_rejects_a_bare_name():
    """The gate, not just the data. Drives linkml-validate over a real record."""
    source = REPO / "kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml"
    document = yaml.safe_load(source.read_text())

    def accepts(candidates: list[str]) -> bool:
        for entry in document["taxonomy"]:
            term = entry.get("taxon_term") or {}
            if term.get("gtdb_candidates"):
                term["gtdb_candidates"] = candidates
                break
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "probe.yaml"
            path.write_text(yaml.dump(document, sort_keys=False, allow_unicode=True))
            return (
                subprocess.run(
                    [
                        "uv",
                        "run",
                        "linkml-validate",
                        "-s",
                        "src/communitymech/schema/communitymech.yaml",
                        str(path),
                    ],
                    capture_output=True,
                    cwd=REPO,
                ).returncode
                == 0
            )

    assert accepts(["GTDB:g__Anabaena", "GTDB:g__Trichormus"]), "a valid list must validate"
    assert not accepts(["Anabaena", "Trichormus"]), "the old bare-name form still validates"
    assert not accepts(["GTDB:Anabaena"]), "a CURIE with no rank validated"
    assert not accepts(["GTDB:__Anabaena"]), "an empty rank validated"


@pytest.mark.parametrize(
    ("name", "expected_rank"),
    [
        # Genus-or-higher path: `resolve_higher` ranks GTDB taxa by genome weight.
        ("Anabaena", "g"),
        # Species path: an NCBI species GTDB splits across several species.
        ("Escherichia coli", "s"),
    ],
)
def test_the_tool_emits_curies_on_both_ambiguous_paths(name, expected_rank):
    """Two separate producers in the script, both of which emitted bare names."""
    result = subprocess.run(
        ["uv", "run", "python", "scripts/gtdb_ground.py", "--name", name],
        capture_output=True,
        text=True,
        cwd=REPO,
        timeout=600,
    )
    if "AMBIGUOUS" not in result.stdout:
        pytest.skip(f"{name} no longer resolves as AMBIGUOUS; this test is stale")

    line = next(ln for ln in result.stdout.splitlines() if "AMBIGUOUS" in ln)
    options = [o.strip() for o in line.split("into:", 1)[1].split(",")]
    # The CLI appends "(+N more)" past eight; drop that tail before matching.
    options = [o for o in options if not o.startswith("(+")]

    assert options, line
    for option in options:
        option = option.split(" (")[0]
        assert CURIE.match(option), f"{name}: bare candidate {option!r}"
        assert option.startswith(f"GTDB:{expected_rank}__"), f"{name}: wrong rank in {option!r}"


def test_a_candidate_is_spelled_like_the_gtdb_id_it_would_become():
    """Promoting a candidate should be a copy, not a re-derivation.

    Both come from `_curie()`, so this pins that they stay that way.
    """
    import importlib.util

    spec = importlib.util.spec_from_file_location("_gtdb", REPO / "scripts/gtdb_ground.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    assert module._curie("Bacillus_A thuringiensis", "s") == "GTDB:s__Bacillus_A_thuringiensis"
    assert module._curie("RDYJ01", "g") == "GTDB:g__RDYJ01"
