"""Is a taxon outside GTDB's scope entirely? (#393)

GTDB classifies **bacteria and archaea only**. So a taxon under Eukaryota or
Viruses can never be grounded — not "the tool failed", but "there is nothing to
find, now or later". That is the distinction #294 wanted and #392 could not make.

Why this needs an ontology and not the crosswalk: a eukaryote does not appear in
NCBI2GTDB at all, so the crosswalk cannot tell "absent because out of scope" from
"absent because the name is spelled differently" (NCBI *Sulcia* is `Candidatus
Karelsulcia`). Both look identical from there. #393 tried settling it by name
matching and withdrew the attempt for exactly this reason.

Measured over the KB's 220 UNRESOLVED taxa:

    Eukaryota            92   final
    Viruses               6   final
    Bacteria             90   genuinely outstanding
    Archaea              16   genuinely outstanding
    other/above-domain   16   `cellular organisms` and similar

So 98 of 220 are not work at all. Without this, the count of outstanding
grounding work overstates itself by about 45%.

**Degrades rather than guesses.** If the adapter cannot be built or a lookup
fails, `outside_gtdb_scope()` returns False — "I could not tell" collapses to the
weaker, safer status, never to a false claim of finality. That keeps
`gtdb_ground.py` runnable without the NCBITaxon database, which is a large
download that the grounding path did not previously need.
"""

from __future__ import annotations

import functools

from communitymech import ontology_adapters

# NCBI's top-level divisions. A taxon at or under one of the first two is in
# GTDB's scope; at or under one of the last two it is permanently outside it.
BACTERIA = "NCBITaxon:2"
ARCHAEA = "NCBITaxon:2157"
EUKARYOTA = "NCBITaxon:2759"
VIRUSES = "NCBITaxon:10239"

OUT_OF_SCOPE = (EUKARYOTA, VIRUSES)


# The shared accessor, bound to the module-local name the callers below and the
# tests that simulate an outage both use. Aliased rather than called through
# `ontology_adapters.` so `monkeypatch.setattr(module, "_adapter", ...)` keeps
# working -- several tests take that route to assert the ABSENT case, which is
# the behaviour that matters most when the ontology is genuinely gone.
_adapter = ontology_adapters.ncbitaxon_adapter


@functools.lru_cache(maxsize=4096)
def domain_of(curie: str) -> str | None:
    """`NCBITaxon:2` / `:2157` / `:2759` / `:10239`, or None if undetermined.

    None covers three different situations on purpose — no adapter, a lookup
    failure, and a taxon above every domain (`cellular organisms`, `root`). All
    three mean "cannot claim finality", which is the only thing callers act on.
    """
    if not curie or not curie.startswith("NCBITaxon:"):
        return None
    adapter = _adapter()
    if adapter is None:
        return None
    try:
        ancestors = set(adapter.ancestors([curie], predicates=["rdfs:subClassOf"]))
    except Exception:
        return None
    for domain in (BACTERIA, ARCHAEA, EUKARYOTA, VIRUSES):
        if curie == domain or domain in ancestors:
            return domain
    return None


def outside_gtdb_scope(curie: str) -> bool:
    """True only when the taxon is provably a eukaryote or a virus.

    Deliberately one-directional: False means "not established", not "in scope".
    A caller may downgrade on False but must never upgrade on it.
    """
    return domain_of(curie) in OUT_OF_SCOPE
