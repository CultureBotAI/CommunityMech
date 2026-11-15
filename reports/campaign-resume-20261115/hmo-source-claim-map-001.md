# HMO 000296 source preparation

This is preparation for the next single-record scientific review. It does not resume the campaign, run the record's gates, save a native review, certify the record, or alter any canonical record or article cache.

Target: `kb/communities/Ecoli_Bifidobacterium_bifidum_Infant_gut_HMO_Mutualism_Coculture.yaml`, CommunityMech:000296. The unchanged record SHA256 is `31e420e8e1553817b77ff5bde0d4229ee09eca2cbf62e5d6524a275801475627`. The unchanged `references_cache/PMID_42020426.md` SHA256 is `b9d67d6a9cceb1a072d6cfdf08d59a7c4b5edadb1759fa46bfb54aa05744d1fc`.

The M5 source execution used revision `ce5c79738e4ad5217ec4e9f41bdcc44ce1ce3414` plus the separately reviewed acquisition helper SHA256 `e24ad2493735ac4aefe5516b312dec484a7f5c60a40935cdde9b67dfbe79dbb0`. Local preparation started at `5f4644874ec644ec76588f3685681301fbf12219`. Those distinct revisions are not a claim to test the eventual integrated campaign revision.

## Retained primary evidence

The article is [PMID 42020426 / PMC13103366](https://pmc.ncbi.nlm.nih.gov/articles/PMC13103366/), DOI `10.1038/s41467-026-71764-7`. The previously verified JATS XML remains SHA256 `a100510b84bb68dbb4e1fe1163a1dcaaf2167566fc43b7bcf3740901ac385447`.

The [Figure 4 canary receipt](hmo-assets-figure-canary-002.json) and [seven-asset receipt](hmo-assets-required-001.json) are byte-identical copies of the completed private M5 receipts. They bind primary URLs, source MIME, byte lengths, hashes, format checks, revision and unchanged scientific inputs. The source helper used anonymous requests, bounded response sizes and fixed primary hosts; it read no credentials or environment files.

| Asset | Persisted content | Inspected during this preparation |
|---|---|---|
| Main Figures 1–4 | Four JPEGs at the exact scaled dimensions declared by their JATS entries | All four images, alongside their primary captions |
| MOESM1: Supplementary Information | 10-page PDF, 33,305,148 bytes | Relevant text and rendered PDF pages 4, 8 and 10: Figures S3, S5 and S6 |
| MOESM2: supplementary-file description | One-page PDF, 19,525 bytes | All five supplementary-data descriptions |
| MOESM7: Supplementary Data 5 | 58-page microscopy/counting PDF, 3,292,377 bytes | Format and extracted-text inventory; individual image/counting records remain to assess |
| MOESM9: Source Data | XLSX, 9,511,233 bytes, 14 worksheets | Verified workbook identity and bounded Figure 4D/4E/S5E/S6 cell reads; no recalculation or statistical reanalysis |

Originals are durable on M5 under `.temp/campaign-resume-20261115/{hmo-source-001,assets-figure-canary-002,assets-required-001}/`, with private local mirrors. They remain separate from the article cache. Only acquisition metadata is published here; raw paper/supplement bodies, images and cells remain private.

## Claim map for the eventual full review

Paragraph locators below refer to the retained article XML/`paragraphs.json`. They locate inspected evidence, not completed review verdicts.

| Current surface | Evidence to bind | Required assessment or unresolved boundary |
|---|---|---|
| Record description, synthetic origin and infant-gut context | Results Par24–26; Methods Par39–40; Discussion Par27–33; Figure 4 | The target is a restricted laboratory pair. Cohort association, genomic co-evolution and proposed infant-host effects must remain distinct from the experimental mutualism. |
| Two species and experimental strain identity | Methods Par39–40; Figure 4E and its source-data conditions | E. coli K-12 is the donor; B. bifidum is a selected infant-stool isolate; BW25113 ΔcysE is the separate control. Do not infer an exact wild-type sub-strain, isogenic comparison, deposited B. bifidum designation or genome accession without a source. Do not borrow the unrelated JCM1254 strain from a neighboring record. |
| Taxonomy abundance prose about transmission | Results Par15–19; Figure 2; Figure S3, PDF pages 4–5 | The primary text separates B. longum's frequent maternal transmission from less frequent B. bifidum transmission. Current B. bifidum family-sharing prose and E. coli external-origin prose need source-specific assessment, separate from experimental membership and abundance. Existing owner: [1428](https://github.com/CultureBotAI/CommunityMech/issues/1428). |
| Cysteine provision node and forward arrow | Par26; Figure 4E; Figure S5B/C/F; control rows in Source Data Figure 4E | The mutant and viable-partner comparisons support cysteine-dependent cooperation. They do not directly measure a cysteine export rate, active secretion, or an isotope-resolved transfer route. Preserve the existing mechanistic limit. |
| Monosaccharide return node | Par25, Par28, Par41–42; Figure 4B/C; Figure S6, PDF page 10; Source Data Figure S6 | Fucose and galactose consumption is measured in a separate spent-medium assay. Preserve its pH condition; do not turn it into a measured sugar-to-cysteine flux or a demonstrated host outcome. |
| Reverse arrow and mutualism summary node | Par26, Par31, Par33; Figure 4D–F | Keep donor-maintenance feedback qualified. The summary is not a separately demonstrated downstream host endpoint; the prior graph correction [1425](https://github.com/CultureBotAI/CommunityMech/issues/1425) must not be undone. |
| Single growth-media entry and cultivation prose | Par25–26, Par39–40; Figure S5; Source Data Figure S5E | Separate 0.1% screening, 0.5% live coculture, pre-growth and spent-medium stages. Bifidobacterium isolation/pre-growth uses modified MRS; E. coli uses BHI. Do not apply selective bifidobacterial isolation to the laboratory donor or equate all photographed/monitored vessels. |
| Concentration and pH qualifiers | Par25–26/28; Figure S5E and S6 labels/captions; Source Data Figure S5E | Primary text labels 0.1% as w/v and the live 0.5% coculture as v/v; Methods/figure labels do not justify silently converting them. Main Discussion states unadjusted pH 4.3, while actual S5/S6 and Source Data S5E specify 4.1. Retain both source contexts until reconciled, under [1428](https://github.com/CultureBotAI/CommunityMech/issues/1428). |
| Possible quantitative coculture abundance | Par26/40; Figure 4D; Supplementary Data 5; Source Data Figure 4D | Approximate 1:1 inoculation is a starting condition; later counts are microscopy estimates, not read abundance or CFU. Source Data has fractions and Figure 4D labels a percentage axis. Any future numeric addition needs explicit scale, timepoint, replicate and nine-field counting scope; the 58-page microscopy file has not been fully assessed. |
| Ontology and GTDB statements | Existing local NCBITaxon, ENVO, CHEBI and GO authorities; pinned GTDB crosswalk | Ground the seven distinct existing CURIEs below, verify bacterial ancestry and the two stored classifications. Authority files were confirmed present, but these record-specific checks have not run in this preparation. |
| Article-cache declaration and exact snippets | Main JATS identity/body, unchanged retained cache, future actual assertion measurement | The cache declares abstract-only despite a labeled main-text payload. [2828](https://github.com/CultureBotAI/CommunityMech/issues/2828) owns that provenance discrepancy. Separate supplements must not be inserted into the article cache. No fresh matcher coverage or snippet-validity count is claimed here. |

Required existing CURIE checks: `NCBITaxon:562`, `NCBITaxon:1681`, `ENVO:2100002`, `CHEBI:15356`, `CHEBI:147155`, `CHEBI:35381`, and `GO:0044419`. Species-level mappings do not identify the cultured stocks. The record's old GTDB genome counts and release wording require an explicit retained mapping source, not an inferred current release.

The supplement description identifies Data 1 as cohort demographics, Data 2 as abundance distributions, Data 3 as MAG/GH2 metadata, Data 4 as variable genes and Data 5 as coculture Gram-stain quantification. Data 1–4 and peer-review files were not acquired in this bounded step. The 458-MAG archive and PRJNA1230889 are population resources, not automatically the cultured isolate's genome accession. Any further acquisition should answer a concrete unresolved identity or claim.

## Remaining sequence

1. Finish Phase 2 accounting and select the exact campaign code revision; preserve this preparation and prior campaign ordering.
2. Resolve or explicitly retain the strain, concentration, pH and microscopy-scope limits using the bound primary inputs. Review every current field, three nodes and two arrows; a successful source download is not that review.
3. Capture native review inputs on the selected revision, including original sources, derivatives, actual cache, schema/config, history and relevant helpers. Reconcile any changed input rather than replacing hashes in an old report.
4. Run the prepared single-record launcher only when released: nine scoped native gates plus actual assertion-comparison measurement. Verify all artifacts and unchanged inputs. Do not substitute an issue count or zero native result count for comparisons performed.
5. Save one full immutable native assessment with all required checks and truthful unresolved findings, then verify every bound input and native Markdown. Only that save advances the campaign. Curation, if later required, needs its own reviewed candidate, guarded application and append-only history.

## Acquisition/control limits

[2843](https://github.com/CultureBotAI/CommunityMech/issues/2843) records the failed direct-child JATS lookup and original-only dimension assumption. Both failed attempts and exact helper versions remain private on M5. The corrected parser accepts only explicit original/scaled dimension pairs from the pinned JATS. A separately reviewed fresh Figure 4 canary passed, its 120,112-byte image/hash was verified and pixels inspected before the seven-asset capture.

[2845](https://github.com/CultureBotAI/CommunityMech/issues/2845) records a review finding in the new read-only workbook helper: the receipt's reported hash could have come from a different read than its parsed bytes. The actual XLSX mutation control failed before the fix, then passed through unchanged → mutation rejected before output → restored. The helper now parses/hashes one snapshot and rechecks it before stdout; independent re-review accepted the correction before source-cell use. Combined acquisition/reader controls: eight passed. These are helper controls, not campaign record gates.
