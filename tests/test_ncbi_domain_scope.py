"""NO_GTDB_EQUIVALENT is now evidence-backed, not inferred from failure (#393).

GTDB classifies bacteria and archaea only, so a eukaryote or virus can never be
grounded. #294 wanted that said; #392 had to withdraw it, because inferring
"final" from "the resolve failed" was wrong for at least 82 of 293 entries.

The missing piece was an NCBI lineage source, which `outside_gtdb_scope()` now
supplies from the NCBITaxon ontology OAK already configures. Of the KB's 220
UNRESOLVED taxa, 95 turn out to be eukaryotes or viruses — the backlog of
outstanding grounding work overstated itself by roughly 43%.

The direction matters more than the count. `outside_gtdb_scope()` returns False
whenever it cannot tell — no adapter, a failed lookup, a taxon above every domain
— so an unavailable database degrades to the weaker status and never to a false
claim of finality.
"""

from __future__ import annotations

import collections
import pathlib

import pytest
import yaml

from communitymech.paths import taxon_descriptor_roots
from communitymech.taxon_blocks import iter_taxon_descriptors
from communitymech.validators.ncbi_domain import BACTERIA, EUKARYOTA, domain_of, outside_gtdb_scope

REPO = pathlib.Path(__file__).parent.parent


# A GTDB grounding can live on any `TaxonDescriptor`, and the schema hangs that
# class off two roots: MicrobialCommunity.taxonomy[].taxon_term and
# CommonTaxon.taxon_term. So this needs BOTH the wider directory list and the
# shared walker -- iterating `document["taxonomy"]` over kb/taxa finds nothing,
# because a CommonTaxon has no `taxonomy` key at all (#656, #689).
def _record_paths() -> list[pathlib.Path]:
    return [p for root in taxon_descriptor_roots() for p in sorted(root.glob("*.yaml"))]


@pytest.mark.parametrize(
    ("curie", "expected"),
    [
        ("NCBITaxon:4932", True),  # Saccharomyces cerevisiae
        ("NCBITaxon:3702", True),  # Arabidopsis thaliana
        ("NCBITaxon:2759", True),  # Eukaryota itself
        ("NCBITaxon:10239", True),  # Viruses itself
        ("NCBITaxon:2", False),  # Bacteria
        ("NCBITaxon:2157", False),  # Archaea
        ("NCBITaxon:1239", False),  # Bacillota
        ("NCBITaxon:336809", False),  # Candidatus Karelsulcia — see below
        # Above every domain: "cannot tell" must read as not-final.
        ("NCBITaxon:131567", False),  # cellular organisms
        ("NCBITaxon:1", False),  # root
        # Malformed input must never claim finality.
        ("", False),
        ("GTDB:s__Bacillus_velezensis", False),
        ("not-a-curie", False),
    ],
)
def test_scope_is_decided_only_when_it_can_be(curie, expected, request):
    """`False` holds with or without a lookup; `True` cannot be reached without one.

    Only the True cases request the adapter. The False half is the
    one-directional property every caller relies on -- "not established" rather
    than "in scope" -- so skipping it when the database is missing would drop the
    safety check exactly when the risk is highest (#704).
    """
    if expected:
        request.getfixturevalue("requires_ncbi_adapter")
    assert outside_gtdb_scope(curie) is expected


def test_an_unavailable_adapter_degrades_rather_than_guesses(monkeypatch):
    """The property that makes this safe to depend on.

    Without it, running `gtdb_ground.py` on a machine lacking the NCBITaxon
    database would silently relabel every unresolved taxon as final.
    """
    import communitymech.validators.ncbi_domain as module

    real_adapter = module._adapter
    # `domain_of` is lru_cached, so a real answer from an earlier test would be
    # returned without ever consulting the patched adapter.
    module.domain_of.cache_clear()
    monkeypatch.setattr(module, "_adapter", lambda: None)
    try:
        assert module.domain_of("NCBITaxon:4932") is None
        assert module.outside_gtdb_scope("NCBITaxon:4932") is False
    finally:
        # Clear again before the real adapter is restored, or every later test
        # inherits the None answers cached here. `real_adapter` is the lru_cached
        # original — the patched stand-in has no `cache_clear`.
        module.domain_of.cache_clear()
        real_adapter.cache_clear()


def _statuses():
    counts = collections.Counter()
    offenders = []
    for path in _record_paths():
        for term_block in iter_taxon_descriptors(yaml.safe_load(path.read_text())):
            status = term_block.get("gtdb_grounding_status")
            if not status:
                continue
            counts[status] += 1
            term = term_block.get("term") or {}
            curie = term.get("id") if isinstance(term, dict) else None
            if status == "NO_GTDB_EQUIVALENT" and curie and not outside_gtdb_scope(curie):
                offenders.append(f"{path.name}: {curie} {term.get('label')!r}")
    return counts, offenders


def test_every_final_status_is_backed_by_a_domain_lookup(requires_ncbi_adapter):
    """The claim #392 could not make, now checkable rather than asserted.

    A NO_GTDB_EQUIVALENT whose taxon is a bacterium is the exact failure that
    made 57 KB entries read "GTDB has no counterpart" for *Bacteria*, the root
    of GTDB.
    """
    counts, offenders = _statuses()

    assert not offenders, "NO_GTDB_EQUIVALENT on an in-scope taxon:\n" + "\n".join(offenders[:10])
    assert counts["NO_GTDB_EQUIVALENT"] > 50, (
        f"only {counts['NO_GTDB_EQUIVALENT']} final statuses; the domain lookup "
        f"may have stopped working (#393)"
    )
    assert counts["UNRESOLVED"] > 0, "nothing unresolved at all — suspiciously clean"


def test_sulcia_is_a_bacterium_not_a_spider(requires_ncbi_adapter):
    """`NCBITaxon:2716471` is a spider genus, and three records used it.

    Found because the domain lookup called a bacterial endosymbiont a eukaryote.
    NCBI renamed *Candidatus Sulcia* to *Candidatus Karelsulcia*
    (`NCBITaxon:336809`); GTDB still calls it `g__Sulcia`, which is why the
    crosswalk lookup misses and it stays UNRESOLVED rather than becoming final.

    The id↔label gate cannot catch this class: `NCBITaxon:2716471` really is
    labelled "Sulcia" (#292).
    """
    for path in _record_paths():
        text = path.read_text()
        assert "NCBITaxon:2716471" not in text, f"{path.name} still uses the spider id"

    assert domain_of("NCBITaxon:336809") == BACTERIA
    assert domain_of("NCBITaxon:2716471") == EUKARYOTA
