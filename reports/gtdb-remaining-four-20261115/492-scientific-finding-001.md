CommunityMech:000492 stores one isolate, Intrasporangium chromatireducens Q5-1,
but represents three physiological/application observations as COMMENSALISM at
COMMUNITY_LEVEL with two directed causal arrows. The current record is
`data/isolates/Intrasporangium_Chromatireducens_Q5_1_Chromate_Reduction.yaml`,
SHA256 `3be922d81b044ad742cd52ae866f3007d2f17141fc7355c4a34ad9f96ca304c4`.
The historical batch135 ledger declares those arrows directly supported.

A fresh whole-record and ledger read against both retained primary abstracts
raises three related scientific findings:

- The evidence describes a single bacterial isolate and separate assay or
  immobilization conditions. It does not identify a commensal partner or a
  demonstrated community interaction.
- Co-occurrence of aerobic resistance, resting-cell reduction and useful bead
  immobilization does not by itself establish the two directed dependencies in
  the graph. The retained abstracts do not establish that resistance or a
  demonstrated reductase mechanism causes the resting-cell phenotype, or that
  resting-cell activity causally enables immobilization.
- The first node's PMID21441371 quotation covers origin and morphology, while
  its explanation additionally claims high aerobic Cr(VI)-reducing activity.
  That activity appears elsewhere in the abstract, but is absent from this
  particular supporting quotation.

The retained sources are PMID21441371 (DOI10.1099/ijs.0.030528-0), cache SHA256
`32f3d015e3c3baf2736ec129ee462156645cfb9233014fd96205096a6d97fd53`, and
DOI10.1007/s11274-009-0047-x, cache SHA256
`3e70900a2ca51a6ecc8617c423e586441c110b4f89ebb10b710068d653816a1f`.
Both declare abstract-only coverage. The abstract reports resting-cell activity
even without an added carbon source, acetate stimulation and similar bead/free
cell rates; these distinctions must survive correction. MIC17 mmol/L is not a
demonstrated treatment concentration or successful growth at that concentration.

This is a blocker for full scientific approval, not a claim that the complete
papers cannot support additional detail. Read the full primary methods/results
and relevant figures, determine an appropriate isolate observation model,
retain or remove each arrow according to direct evidence, and align each
quotation with its explanation. Save a new native review and make any bounded
corrections through a separately reviewed PR. Preserve the historical ledger
and explain its supersession; passing validators do not settle these findings.

The current GTDB task only proposes a generic reference correspondence. It
must retain these scientific findings and must not promote review status.
Live all-state searches for Intrasporangium, Q5-1 and chromate preceded filing;
the returned chromate issues concerned other records or infrastructure.
