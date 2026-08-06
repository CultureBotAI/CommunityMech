"""A prokaryotic GTDB lineage sitting on a non-prokaryotic NCBITaxon id (#365).

`NCBITaxon:169215` is the **plant** genus *Bosea* (Viridiplantae, Amaranthaceae).
Two records used it for the alphaproteobacterium of the same name and carried a
GTDB block derived from it, reading
`d__Bacteria;p__Pseudomonadota;...;g__Bosea`. The KB therefore asserted that a
plant genus is a bacterium, in a field that looked independently sourced.

The block came from a **name collision**, not a typo: `gtdb_ground.py`'s
higher-rank path matches on the cleaned label string rather than the id, so
"Bosea" resolved to the bacterial genus while the id pointed at the plant. The
bacterium is `NCBITaxon:85413`, which NCBI now labels *Allobosea* and aliases
"Bosea Das et al. 1996" — the two genera are homonyms, and the bacterial one was
renamed.

**No existing gate could see it.** `ncbi_source_id == term.id`, so the freshness
check from #364 passes. "Bosea" genuinely *is* `NCBITaxon:169215`'s label, so
id<->label correspondence passes. `linkml-validate` has nothing to say. And the
#292 shared-id gate cannot help either: the id appears once per record, so there
is no second organism to disagree with.

The signal this check uses needs no curation judgement at all: **GTDB is
prokaryote-only.** Its domains are `d__Bacteria` and `d__Archaea` and nothing
else, so an id outside those two domains can never carry a GTDB lineage. That
makes a mismatch a contradiction rather than a suspicion, and it would have
caught this at write time.

Both directions are checked, because both are the same contradiction:

* a **non-prokaryotic id** under a prokaryotic lineage — the #365 defect;
* a **domain disagreement**, an `NCBITaxon` archaeon under `d__Bacteria` or the
  reverse. GTDB and NCBI can and do disagree about phyla and genera, which is
  what `is_reclassified` records; they do not disagree about which of the two
  prokaryotic domains an organism is in.

As in the #292 gate, an id whose domain cannot be resolved is never judged. No
rank filter is needed here: the domain of a genus, a species and a strain are
all equally well defined.
"""

from __future__ import annotations

import functools
import sys

# The only two domains GTDB models, and the NCBITaxon ids that root them.
PROKARYOTE_ROOTS = {"NCBITaxon:2": "Bacteria", "NCBITaxon:2157": "Archaea"}
# Everything else an NCBITaxon id can be rooted under. Named so the message can
# say *what* the id is rather than only that it is wrong.
OTHER_ROOTS = {"NCBITaxon:2759": "Eukaryota", "NCBITaxon:10239": "Viruses"}


@functools.lru_cache(maxsize=1)
def _adapter():
    try:
        from oaklib import get_adapter  # type: ignore[import-untyped]

        return get_adapter("sqlite:obo:ncbitaxon")
    except Exception:
        return None


_warned_no_adapter = False


def _warn_once_if_unavailable() -> None:
    """Say so when the check is being skipped rather than passed (cf. #426)."""
    global _warned_no_adapter
    if not _warned_no_adapter and _adapter() is None:
        _warned_no_adapter = True
        print(
            "[gtdb-domain] NCBITaxon is unavailable, so the prokaryote-only check "
            "(#365) was skipped, not passed.",
            file=sys.stderr,
        )


@functools.lru_cache(maxsize=4096)
def domain_of(curie: str) -> str | None:
    """`Bacteria`, `Archaea`, `Eukaryota`, `Viruses`, or None if undetermined.

    None whenever the adapter is missing or the id is not in NCBITaxon, which
    callers must treat as "cannot judge". A gate that fired when it could not
    look anything up would be noise on any machine without the database.
    """
    adapter = _adapter()
    if adapter is None or not curie.startswith("NCBITaxon:"):
        return None
    try:
        from oaklib.datamodels.vocabulary import IS_A  # type: ignore[import-untyped]

        ancestors = set(adapter.ancestors([curie], predicates=[IS_A]))
    except Exception:
        return None
    if not ancestors:
        return None
    for root, name in {**PROKARYOTE_ROOTS, **OTHER_ROOTS}.items():
        if root in ancestors:
            return name
    return None


def lineage_domain(lineage: str) -> str | None:
    """The domain a GTDB lineage string declares, or None if it declares none."""
    head = (lineage or "").split(";", 1)[0].strip()
    if head == "d__Bacteria":
        return "Bacteria"
    if head == "d__Archaea":
        return "Archaea"
    return None


def _terms(taxonomy: list):
    """Every `taxon_term` block in a record, skipping anything malformed.

    Defensive for the same reason as the #292 gate (#429): this runs inside
    `validate_strict`, and raising here would abort the run and discard every
    other file's findings, when the schema validator in that same pass
    diagnoses a malformed record properly.
    """
    if not isinstance(taxonomy, list):
        return
    for entry in taxonomy:
        if not isinstance(entry, dict):
            continue
        term_block = entry.get("taxon_term")
        if isinstance(term_block, dict):
            yield term_block


def check_record(taxonomy: list) -> list[str]:
    """Messages for each GTDB block whose lineage contradicts its id's domain."""
    _warn_once_if_unavailable()
    problems = []
    for term_block in _terms(taxonomy):
        block = term_block.get("gtdb_classification")
        if not isinstance(block, dict):
            continue
        declared = lineage_domain(block.get("gtdb_lineage") or "")
        if declared is None:
            continue
        term = term_block.get("term")
        curie = (term or {}).get("id") if isinstance(term, dict) else None
        if not isinstance(curie, str) or not curie:
            continue
        actual = domain_of(curie)
        if actual is None or actual == declared:
            continue
        name = term_block.get("preferred_term") or (term or {}).get("label") or curie
        if actual in PROKARYOTE_ROOTS.values():
            detail = f"but the id is {actual}, not {declared}"
        else:
            detail = (
                f"but the id is {actual}, and GTDB classifies only Bacteria and Archaea "
                f"— so this id cannot have a GTDB lineage at all"
            )
        problems.append(f"{curie} ({name!r}) carries a d__{declared} GTDB lineage, {detail}.")
    return problems
