# Ontology term requests — CommunityMech (#182 "mint")

Concepts used in `kb/communities/` whose intended term does not exist in the target
ontology. Each is currently grounded to the **nearest valid** existing term (so the
id↔label gate stays green and `preferred_term` keeps the specific meaning); this file
requests the proper terms so the groundings can be tightened once minted. Verified
absent via OAK (sqlite:obo:*) + live OLS/NCBI.

## CHEBI term requests (submit at https://github.com/ebi-teams/chebi-submissions)

| Requested term | Formula | Proposed parent (CHEBI) | Current stopgap grounding | Source community |
|---|---|---|---|---|
| lead(II) sulfide (galena) | PbS | metal sulfide / sulfide salt (CHEBI:46718); cf. lead(2+) CHEBI:49807 | CHEBI:46718 sulfide salt | Australian_Lead_Zinc_Polymetallic |
| zinc sulfide (sphalerite) | ZnS | metal sulfide / sulfide salt (CHEBI:46718); cf. zinc(2+) CHEBI:29105 | CHEBI:46718 sulfide salt | Australian_Lead_Zinc_Polymetallic |
| chromium(III) hydroxide | Cr(OH)3 | transition-element hydroxide; cf. chromium(3+) CHEBI:49544 | CHEBI:49544 chromium(3+) | Chromium_Sulfur_Reduction_Enrichment |
| N-(3-hydroxytetradecanoyl)-L-homoserine lactone (3-OH-C14-HSL) | C18H33NO4 | N-acyl-L-homoserine lactone (CHEBI:55474) | CHEBI:55474 N-acyl-L-homoserine lactone | Thermophilic_Pyrite_QS_Consortium |

Definitions (Aristotelian, for the submission):
- **lead(II) sulfide** — a metal sulfide that is the lead(2+) salt of sulfide; the mineral galena.
- **zinc sulfide** — a metal sulfide that is the zinc(2+) salt of sulfide; the mineral sphalerite/wurtzite.
- **chromium(III) hydroxide** — a chromium hydroxide in which chromium is in the +3 oxidation state.
- **N-(3-hydroxytetradecanoyl)-L-homoserine lactone** — an N-acyl-L-homoserine lactone in which the acyl group is 3-hydroxytetradecanoyl (a saturated 3-OH C14 AHL quorum-sensing signal).

## ENVO term request (submit at https://github.com/EnvironmentOntology/envo/issues)

| Requested term | Proposed parent (ENVO) | Current stopgap grounding | Source community |
|---|---|---|---|
| phyllosphere | plant-associated environment (ENVO:01001001) | ENVO:01001001 plant-associated environment | Arabidopsis_Phyllosphere_SynCom7 |

- **phyllosphere** — a plant-associated environment comprising the aerial surfaces of a plant (leaves and stems) and their resident microbiota.

## Regrounding notes (no new term needed)
- **organic matter** — reground from `CHEBI:50860` (organic molecular entity) to **`ENVO:01000155` organic material** (already exists; better fit for a material/factor). Affects Avena_Rhizosphere_Detritusphere_Niche_Succession, Brachypodium_Young_Root_Rhizosphere_EcoFAB_Community.
- **humic acid**, **yeast extract** — complex undefined mixtures; CHEBI does not mint undefined mixtures. Better handled as a MediaIngredientMech / FoodOn ingredient term (yeast extract) or ENVO material (humic substance). Kept at the current broad CHEBI grounding for now.
- **Stenotrophomonas goyi** — a validly published 2023 species not yet in the pinned NCBITaxon snapshot; grounded at genus `NCBITaxon:40323`. No proposal — it will resolve when NCBITaxon is refreshed.

## Companion: dropped terms
The generic obsolete-GO annotations (redox process, organic-substance metabolic/catabolic)
were **dropped** rather than kept (131 entries, 48 files) — see `scripts/drop_obsolete_go_bp.py`.
Meaningful obsolete-GO remaps were kept (multi-organism → interspecies interaction
`GO:0044419`, metal-ion sequestering `GO:0140487`, anion transporter `GO:0008509`).
