"""A leading "Candidatus" made a taxon silently unresolvable (#419).

`_clean_label` strips a leading ``Candidatus`` so the binomial heuristic and the
CURIE builder see a bare name. The NCBI2GTDB species and genus columns **keep**
it. Looking up only the stripped form therefore matched nothing for every
*Candidatus* taxon, and the tool reported the ordinary
``no GTDB mapping (rank absent from the NCBI2GTDB table, or eukaryote)`` —
indistinguishable from a taxon GTDB genuinely does not cover.

That is how #419's defect got into the KB. *Candidatus Accumulibacter*
(`NCBITaxon:327159`) has 45 genomes under ``GTDB:g__Accumulibacter``, but
grounding the genus returned nothing, so the record fell back to the
*Betaproteobacteria* **class** — 41937 genomes, and `c__Gammaproteobacteria`
after GTDB's reclassification. The note on that entry read as a curation
choice; it was a workaround for this bug.

Measured when it was fixed: **11 taxa** across the KB were unresolvable for this
reason alone (7 on the higher-rank path, 4 on the species path), all of them
reporting no mapping rather than an error.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).parent.parent
ACCUMULIBACTER_RECORD = REPO / "kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml"


@pytest.fixture(scope="module")
def gtdb():
    spec = importlib.util.spec_from_file_location("gtdb_ground", REPO / "scripts/gtdb_ground.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def mapping(gtdb):
    try:
        path = gtdb.resolve_kg_microbe_dir(None) / "data/raw/NCBI2GTDB.tsv.gz"
    except SystemExit as exc:
        pytest.skip(f"kg-microbe mapping unavailable: {str(exc).splitlines()[0]}")
    if not path.exists():
        pytest.skip(f"kg-microbe NCBI2GTDB mapping not available at {path}")
    return path


@pytest.mark.parametrize(
    ("label", "expected"),
    [
        # Exact first: a genuine un-prefixed homonym must not capture a
        # Candidatus lookup.
        ("Candidatus Accumulibacter", ["candidatus accumulibacter", "accumulibacter"]),
        ("Candidatus Brocadia sinica", ["candidatus brocadia sinica", "brocadia sinica"]),
        # No prefix to strip: one key, not a duplicated pair.
        ("Bosea", ["bosea"]),
        ("Bacteroides ovatus", ["bacteroides ovatus"]),
        # NCBITaxon disambiguators are stripped, so both spellings survive.
        ("Bosea <bacteria>", ["bosea <bacteria>", "bosea"]),
        ("", []),
        (None, []),
    ],
)
def test_both_spellings_are_offered_most_specific_first(gtdb, label, expected):
    assert gtdb.lookup_keys(label) == expected


def test_the_table_really_does_keep_the_prefix(gtdb, mapping):
    """The premise of the fix — assert it rather than trusting the docstring."""
    _, _, by_higher = gtdb.collect_rows(
        mapping, set(), set(), {"accumulibacter", "candidatus accumulibacter"}
    )
    assert by_higher.get("accumulibacter", []) == [], "stripped key should match nothing"
    assert len(by_higher.get("candidatus accumulibacter", [])) > 0, "table keeps the prefix"


def test_a_candidatus_genus_now_grounds(gtdb, mapping):
    """The #419 case: 45 genomes that used to be invisible."""
    _, _, by_higher = gtdb.collect_rows(
        mapping, set(), set(), set(gtdb.lookup_keys("Candidatus Accumulibacter"))
    )
    found = gtdb.resolve_target("327159", "Candidatus Accumulibacter", {}, {}, by_higher)
    assert found is not None, "the genus must resolve"
    assert found["gtdb_id"] == "GTDB:g__Accumulibacter"
    assert found["total_genomes"] == 45


def test_a_candidatus_species_now_grounds(gtdb, mapping):
    """The species path had the same defect, via `by_name` rather than `by_higher`."""
    keys = set(gtdb.lookup_keys("Candidatus Brocadia sinica"))
    _, by_name, _ = gtdb.collect_rows(mapping, set(), keys, set())
    found = gtdb.resolve_target("795830", "Candidatus Brocadia sinica", {}, by_name, {})
    assert found is not None, "the species must resolve"
    assert found["gtdb_id"] == "GTDB:s__Brocadia_sinica"


def test_an_unprefixed_taxon_is_unaffected(gtdb, mapping):
    """Regression: the fix must not change what already worked."""
    _, _, by_higher = gtdb.collect_rows(mapping, set(), set(), {"bosea"})
    found = gtdb.resolve_target("85413", "Bosea", {}, {}, by_higher)
    assert found is not None
    assert found["gtdb_id"] == "GTDB:g__Bosea"
    assert found["total_genomes"] == 34


def _accumulibacter_entry():
    doc = yaml.safe_load(ACCUMULIBACTER_RECORD.read_text())
    for entry in doc["taxonomy"]:
        block = entry.get("taxon_term") or {}
        if "Accumulibacter" in (block.get("preferred_term") or ""):
            return block
    raise AssertionError("the Accumulibacter entry is gone from the EBPR record")


def test_accumulibacter_is_grounded_at_genus_not_class():
    """The KB half of #419, pinned so a tool re-run cannot quietly undo it."""
    block = _accumulibacter_entry()
    assert block["term"]["id"] == "NCBITaxon:327159", "the genus, not Betaproteobacteria"
    assert block["term"]["label"] == "Candidatus Accumulibacter"

    grounding = block["gtdb_classification"]
    assert grounding["gtdb_id"] == "GTDB:g__Accumulibacter"
    assert grounding["total_genomes"] == 45, "not the class's 41937"
    assert block["gtdb_grounding_status"] == "GROUNDED"


def test_no_record_grounds_accumulibacter_on_the_class_id():
    """`NCBITaxon:28216` is legitimate for entries that *name* the class.

    Two records use it correctly (`Betaproteobacteria`, and a floodplain core
    microbiome described as Betaproteobacteria-dominated). What must not come
    back is an entry naming a genus and storing that class.
    """
    offenders = []
    for directory in ("kb/communities", "data/isolates"):
        for path in sorted((REPO / directory).glob("*.yaml")):
            doc = yaml.safe_load(path.read_text()) or {}
            for entry in doc.get("taxonomy") or []:
                block = (entry or {}).get("taxon_term") or {}
                term = block.get("term") or {}
                if term.get("id") != "NCBITaxon:28216":
                    continue
                if "Accumulibacter" in (block.get("preferred_term") or ""):
                    offenders.append(f"{path.name}: {block.get('preferred_term')}")
    assert offenders == [], "\n".join(offenders)
