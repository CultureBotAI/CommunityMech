# METPO proposal — interaction semantics (CommunityMech, 2026-09)

Eight classes, from three CommunityMech issues that share one cause:
`InteractionTypeEnum` classifies an interaction by **sign** — who benefits — and
several real interactions are not describable that way.

| id | label | parent | issue |
|---|---|---|---|
| METPO:1008200 | obligate syntrophy interaction | METPO:1007127 | #752 |
| METPO:1008201 | facultative syntrophy interaction | METPO:1007127 | #752 |
| METPO:1008210 | material transfer interaction | METPO:1007120 | #749 |
| METPO:1008211 | interspecies cell fusion | METPO:1008210 | #749 |
| METPO:1008212 | interspecies cytoplasmic material exchange | METPO:1008210 | #749 |
| METPO:1008213 | interspecies horizontal gene transfer | METPO:1008210 | #749 |
| METPO:1008214 | interspecies electron transfer | METPO:1008210 | #751 |
| METPO:1008215 | direct interspecies electron transfer | METPO:1008214 | #751 |

## Why these, and not a widened enum

### Obligate vs facultative (#752)

`InteractionTypeEnum.SYNTROPHY` is defined as **"Obligate metabolic
cooperation"**, and `METPO:1007127 syntrophy interaction` inherits that wording:
*"obligate metabolic cooperation ... thermodynamically infeasible for either
partner alone."* The literature does not use the word that strictly, and neither
does the corpus — SYNTROPHY is the third most-used type, 135 times.

The confirmed case is CommunityMech:000336. Every paper on the
*C. acetobutylicum*–*C. ljungdahlii* pairing calls it a syntrophy, and the seed
paper (PMID:40298437) grows **both species as monocultures in the same
experiment** — that arm is the study's control. Obligacy is disproved by the
source the record cites.

METPO already models this distinction elsewhere in exactly this shape:
`metpo:1000607 obligately anaerobic` and `metpo:1000605 facultatively anaerobic`
are siblings under `metpo:1000601 oxygen preference`. These two classes apply the
same pattern to syntrophy.

**This requires amending METPO:1007127's definition** to drop "obligate", so that
a facultative child is not a contradiction of its parent. That amendment is part
of the proposal, not a side effect of it.

### Transfer without a sign (#749)

Three mechanisms in CommunityMech:000336 have no home in a sign-based enum:

- **cell fusion** — *C. acetobutylicum* and *C. ljungdahlii* join cell walls and
  membranes (PMID:32873766, by TEM and electron tomography);
- **bulk cytoplasmic exchange** — protein, RNA and ribosomes crossing between
  them (PMID:32873766, PMID:39254339);
- **horizontal gene transfer through that fusion** — plasmid DNA acquired and
  integrated (PMID:38214507), which is the finding of that paper precisely
  because it is *not* conjugation, transduction or transformation.

Curating any of them as MUTUALISM or COMMENSALISM asserts a benefit no cited
paper establishes. CommunityMech:000336 and :000338 therefore leave
`interaction_type` unset on four interactions and say why — legal, since the slot
is optional, but conspicuous: exactly **1** of the corpus's other 899
interactions does so.

`METPO:1008210 material transfer interaction` is deliberately a **sibling** of the
sign types under `METPO:1007120 ecological interaction type`, not a subtype. An
interaction can be both a fusion and a mutualism; those are answers to different
questions, and forcing one slot to carry both is what ran the enum out of room.

### Interspecies electron transfer (#751)

Twelve CommunityMech interactions were annotated `GO:0009055 electron transfer
activity`. That is a **molecular function**, not a process, and it sat in
`biological_processes` where nothing checked the aspect.

There is no GO replacement. Searching EBI OLS for *extracellular electron
transport* and *interspecies electron transfer* returns nothing, and every GO
electron-transport-chain term (`GO:0022900` and its children) denotes an
intracellular series of complexes — wrong for DIET through conductive pili. The
nearest existing anchor is `metpo:1000805 Electron transfer`, which is itself
xrefed to `GO:0009055`.

#751 removed those twelve annotations rather than substitute a term meaning
something else. These two classes are where they should go once minted.

## Verification performed

- GO aspects checked structurally, by ancestor rather than by label:
  `GO:0008150` / `GO:0005575` / `GO:0003674` against the pinned local build.
- METPO checked against `metpo-full.obo` (255 terms): `Syntrophy` (metpo:1002006)
  and `Electron transfer` (metpo:1000805) exist; **cell fusion, horizontal gene
  transfer and conjugation do not.**
- TraitMech and CellStructureMech schemas searched for all six concepts — no
  matches, so this is not a case of a sibling repo already owning them.
- Proposed ids start at 1007200; the highest id in the existing CommunityMech
  cohorts is 1007193, and METPO itself mints nothing in the 1007xxx block.

## Upstream path

Merge with the kg-microbe METPO proposal pipeline as the existing cohorts do.
The two syntrophy classes and the METPO:1007127 amendment can go independently of
the transfer block; the electron-transfer pair is the one that unblocks re-adding
information #751 had to remove.
