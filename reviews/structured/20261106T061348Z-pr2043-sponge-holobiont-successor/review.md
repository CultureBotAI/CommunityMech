# Current-main sponge holobiont review and bounded source-context correction

- Review: 20261106T061348Z-pr2043-sponge-holobiont-successor
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-06T06:04:02.889917Z
- Finished UTC: 2026-11-06T06:13:48.795691Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The added animal-associated environment is supported; its repaired omission is removed from the residual context finding. All four original finding keys remain open: two P2 membership/state findings and two P3 computational/resource findings. A new P3 finding records an unrelated PMID in the appended history. Six qualified computational nodes and two conditional arrows remain supported. Bounded corrections identify the actual sponge DOI, Great Barrier Reef sampling and unsupported quotation in three prior cohort-review contexts without superseding their multi-target findings.

## Scope And Provenance

Entire current record and source delta; complete primary scientific main, six main figures, scientific SI text, selected supplementary tables, public model/archive metadata and bounded prior-review source context.

Selection: PR2043 stale record CommunityMech:000013; no other cohort target reassessed.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base c1846ce378828d0a2e2d80312ac784a47430a617.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000013 | kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml | maintained | BioModels MODEL2407300002 Sponge Holobiont Network |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000013 | Documented focused/native check passed with exit 0. |
| validate-terms | passed | True | CommunityMech:000013 | Documented focused/native check passed with exit 0. |
| validate-gtdb | passed | True | CommunityMech:000013 | Documented focused/native check passed with exit 0. |
| validate-gtdb-domain | passed | True | CommunityMech:000013 | Documented focused/native check passed with exit 0. |
| validate-references-explained | passed | True | CommunityMech:000013 | Documented focused/native check passed with exit 0. |
| validate-strict | passed | True | CommunityMech:000013 | Documented focused/native check passed with exit 0. |
| validate-history | passed | True | CommunityMech:000013 | Documented focused/native check passed with exit 0. |
| normalize-cache-names | passed | True | CommunityMech:000013 | Documented focused/native check passed with exit 0. |
| audit-network | failed | True | CommunityMech:000013 | Full corpus: 44 warnings across 16 of 508 records,0 errors; known baseline, target has0 issues. |
| check-network-quality | failed | True | CommunityMech:000013 | Full corpus: 44 warnings across 16 of 508 records,0 errors; known baseline, target has0 issues. |
| Fresh scientific source reassessment | passed | True | CommunityMech:000013 | Four original findings reassessed; five current open findings. Author pass, not independent approval. |
| iModulonDB applicability | not_applicable | False | CommunityMech:000013 | No focal gene/locus/accession or covered strain-specific transcriptomic dataset is asserted; this is a MAG-derived model community. |
| Culture/ingredient identifiers | not_applicable | False | CommunityMech:000013 | No CultureMech/MediaIngredientMech link encoded; in-silico media are not wetlab cultivation. |

## Scientific And Domain Assessments

### Sponge microbiome model scope

identity: concern. Targets: CommunityMech:000013.

The archive identity is correct, but three guild entries do not represent all eight reconstructed members.

### Eight-member composition and roles

grounding: concern. Targets: CommunityMech:000013.

The current three broad entries have supported conditional roles but omit five named reconstructions.

Missing Spongiicolonus versatilis, Spongiihabitans thiooxidans, Oxydemutator thiolithooxidans, Parasynechococcus marinus and Gammaporibacter thiotrophicus materially changes the represented metabolic roster. Cenoporarchaeum/Nitrospongiibacter producer roles and Deltaporibacter cross-feeding are source-supported in modeled regimes; attach specific evidence rather than the generic network snippet.

### ecological_state: STABLE

evidence: concern. Targets: CommunityMech:000013.

An unqualified ecological-equilibrium label is not established by the conditional simulation endpoints.

Distinguish the ratio-of-ratios criterion for the nitrifying model from eight-member Bray–Curtis similarity and late-cycle stabilization. The optional schema field may be omitted or supported with an explicit scope; do not automatically substitute ENGINEERED or TRANSIENT. NATURAL origin remains appropriate for the modeled microbiome.

### ecological_interactions[0]

graph: supported. Targets: CommunityMech:000013.

Retain modeled nitrite cross-feeding.

C. stylissae ammonia oxidation provides nitrite to N. stylissae. NO-reaction disabling and nutrient/removal constraints are explicit; neither measured transfer nor thermodynamic obligacy is established.

### ecological_interactions[0].downstream[0]

graph: supported. Targets: CommunityMech:000013.

Retain conditional nitrification → nitrifier growth support.

C. stylissae supplies the substrate for N. stylissae growth; joint persistence depends on imposed ammonia and removal. This is a source-supported model mechanism, not a general ecological stability claim.

### ecological_interactions[1]

graph: supported. Targets: CommunityMech:000013.

Retain the nutrient-responsive eight-member exchange network.

Alternative input regimes affect predicted exchanges; Deltaporibacter is a participant, not a demonstrated active coordinator. Preserve the removal of part-whole/common-input summary arrows.

### ecological_interactions[2]

graph: supported. Targets: CommunityMech:000013.

Retain candidate host nutrient inputs with the existing uncertainty.

Tissue-enriched substrates are treated as available to microbial models. Origin and delivery are assumptions, and the host is an external context rather than a modeled fitness beneficiary.

### ecological_interactions[2].downstream[0]

graph: supported. Targets: CommunityMech:000013.

Retain conditional candidate-input → microbial exchange direction.

Supplying selected substrates changes the available model resources and predicted exchanges. It does not establish host secretion, reciprocal fitness or the same fluxes in vivo.

### ecological_interactions[3]

graph: supported. Targets: CommunityMech:000013.

Retain the operational nitrifier stability endpoint.

The final/initial AOA:NOB population-ratio criterion is correctly stated as 0.5–2. It is not an absolute abundance bound, measured environmental threshold or independent syntrophic interaction.

### ecological_interactions[4]

graph: supported. Targets: CommunityMech:000013.

Retain condition-specific Deltaporibacter nitrogen-linked exchange.

Hypotaurine scenarios predict nitrate reduction and NO release; mixed-input scenarios predict laurate use and acetate donation. Neither active coordination nor measured flux is asserted.

### ecological_interactions[5]

graph: supported. Targets: CommunityMech:000013.

Retain nutrient-dependent microbial carbon balance.

This aggregate model endpoint excludes host respiration. Carbon fixation is a contributing process and does not make every input regime or the whole living holobiont autotrophic.

### Model assumptions, source context and cultivation

provenance: concern. Targets: CommunityMech:000013.

The new host-associated environment is supported; fourteen computational claims still lack structured provenance.

Retain ENVO:01001002 and its source-backed sponge context. Recover software/model/MAG/scenario provenance with no invented cultivation. Natural sampling is Great Barrier Reef, December 2015; simulated mesohyl and medium constraints are model context. No requirement to populate all optional fields.

### Model, code and data resources

provenance: concern. Targets: CommunityMech:000013.

The exact RDS listing is valid; the bibliography-as-dataset and omitted source-resource context need repair.

PRJNA602572 is a broad prior marine-sponge project, not solely the four focal specimens or a metabolomics archive. STY8 v1.0.0 and Zenodo 14030749 are verified metadata/code inventories. The paper-linked MSV000083743 currently describes EMP soil/fecal samples; resolve before claiming a focal metabolomics link. RDS objects were not parsed or executed.

### Prior repairs, evidence and current limitations

provenance: concern. Targets: CommunityMech:000013.

All 14 snippets match and graph repairs persist, but the appended history cites an unrelated source.

Environment addition is sound; sidecar PMID:39604529 needs append-only correction. Historic unread-source limitations are not rewritten. This current author read expanded primary/supplement scope; no canonical/cache/history content changed.

### Native checks and ontology semantics

schema: supported. Targets: CommunityMech:000013.

Eight native checks pass; this does not resolve membership or scope findings.

### Native mechanical scores

completeness: supported. Targets: CommunityMech:000013.

Completeness rises 75 to 80 after environment repair; quality remains capped 100, distinct from five open findings.

### Sponge-specific context in c2s4/c2s5 reviews

provenance: supported. Targets: CommunityMech:000013.

Correct the sponge source identity, geography and unsupported quotation in three prior-review contexts.

The two c2s4 ev-sponge-pmid39738126 entries incorrectly couple PMID:39738126 with DOI 10.1038/s43705-024-00531-6 and a Red Sea statement presented as a quotation. The focal source instead identifies DOI 10.1038/s41467-024-55222-w and four Great Barrier Reef specimens collected December 2015; the quoted sentence is not present. The c2s5 environment assessment repeats Red Sea and is corrected here only for 000013. ENVO:01001002 remains sound. No terminal disposition or supersession of communitymech-c2s4-biomodels-missing-environment-term is made, and 000006/000007/000008 are not assessed or dropped from that grouped lineage.

## Findings

### eight-member-roster: Represent all eight modeled microbial members

major / open / confirmed; issue key: cm-000013-eight-member-roster.

Three domain-grounded guild entries omit five named reconstructions and do not preserve the full source model composition.

### stable-state: Bound ecological state to the demonstrated evidence

major / open / confirmed; issue key: cm-000013-stable-state.

STABLE globally asserts ecological equilibrium while the source demonstrates conditional model composition outcomes under imposed inputs and turnover.

### computational-context: Complete computational provenance after the environment repair

minor / open / confirmed; issue key: cm-000013-computational-context.

The added ENVO:01001002 environment is supported. Fourteen computational evidence items still lack queryable model/tool/scenario provenance; recoverable model context remains incompletely represented. This residual finding does not demand every optional field.

### resource-scope: Separate publication evidence and reconcile public resource scope

minor / open / confirmed; issue key: cm-000013-resource-scope.

The publication is listed as a dataset while recoverable data/code provenance is absent; the reported metabolomics accession has a current scope mismatch that must not be imported uncritically.

### history-source-identity: Correct the environment-history source identity append-only

minor / open / confirmed; issue key: cm-000013-history-source-identity.

The new 2026-10-25 history sidecar details cite PMID:39604529, an unrelated NLRP3 author correction. The sponge source is PMID:39738126/doi:10.1038/s41467-024-55222-w. Inline record notes retain the correct PMID.

## Recommended Actions And Acceptance Checks

### repair-eight-member-roster

Represent all eight modeled microbial members.

- Represent all eight source members and their model/MAG identifiers, keeping the seven-bacteria/one-archaeon scope and excluding the sponge host. Preserve the 98.3% MAG-mapped-read denominator.
- Fresh NCBI metadata verifies Candidatus Spongiicolonus versatilis 2973585, Candidatus Spongiihabitans thiooxidans 1671877 and Candidatus Oxydemutator thiolithooxidans 2973566; Parasynechococcus 2881427 is genus-level. Preserve source-name notes and unresolved identities rather than inventing species CURIEs/GTDB mappings; reverify candidates during curation.
- Attach narrow membership and condition-specific role evidence; distinguish merged MAG reconstructions from experimental isolates. Revalidate taxonomy, terms and GTDB/domain after curation.

### repair-stable-state

Bound ecological state to the demonstrated evidence.

- Omit the optional ecological_state field if ecological equilibrium cannot be supported, or supply an explicit source-grounded scope that does not present simulated stability as observed in-vivo persistence.
- Preserve NATURAL origin and the existing operational node definition; do not replace the state automatically with ENGINEERED/TRANSIENT or confuse the 0.5–2 ratio-of-ratios criterion with absolute population bounds.

### repair-computational-context

Record structured model and environmental provenance.

- Add claim-specific computational_provenance for gapseq v1.1 b568a4e reconstruction/manual curation/gap-filling and BacArena v1.8.2 pFBA, preserving model identifiers and the source scenarios.
- Separate individual, two-/three-member and eight-member runs. Record the relevant input/removal/death/replenishment assumptions; the eight-member model uses 100 one-hour cycles, 10 mM ammonia, 10% removal and 5% death. Do not generalize those settings to every simulation.
- Retain the now-supported ENVO:01001002 animal-associated environment. Distinguish Great Barrier Reef natural sampling and modeled mesohyl in source-grounded notes where useful; do not require every optional modeled_environment field. Put simulated media in computational provenance, never invented wetlab vessels/temperature/salinity; preserve host-input and host-respiration limitations.

### repair-resource-scope

Separate publication evidence and reconcile public resource scope.

- Keep the verified BioModels entry and exact combined-input RDS filename, while stating listing/metadata verification rather than parsed payload or reproduced simulation.
- Move the paper to bibliographic evidence/resources. Link PRJNA602572 with its broad prior-project scope and source-reported focal subset; link STY8 v1.0.0 commit 17fd9c4eb5bd1f4cdf2c6402a2cdf3958e380546 and Zenodo 10.5281/zenodo.14030749 without claiming execution.
- Record the MSV000083743 source/archive discrepancy and resolve the focal metabolomics deposit before adding a verified dataset link. Do not invent a replacement or label the upstream unencoded discrepancy as an existing wrong record accession.

### append-history-source-correction

Append a history correction without rewriting old provenance.

- Append a new native history event referencing the 2026-10-25 sidecar, correcting 39604529 to 39738126 and focal DOI 10.1038/s41467-024-55222-w; preserve original history bytes.
- State that the animal-associated environment itself is supported, and validate the new history entry. Do not invent a fresh canonical-record change merely to correct provenance.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| roster | doi:10.1038/s41467-024-55222-w; Sec3/15-17; Figure1 pixels; SD2 rows4-11 | supports | Eight named merged/representative MAG reconstructions (seven bacteria, one archaeon) represent 98.3 percent of MAG-mapped reads. Three broad current entries omit five members. |
| nitrification | doi:10.1038/s41467-024-55222-w; Sec5-6; Figure3 pixels; SI CenSfMM8/NitSfMM6 curation and TableS1 | supports | Predicted archaeal nitrite supports bacterial nitrifier growth after an NO-forming reaction is disabled; neither measured partner transfer nor thermodynamic obligacy follows. |
| stability | doi:10.1038/s41467-024-55222-w; Sec6-7/21; Figures3-4 pixels | supports | Normalized final/initial AOA:NOB ratio of 0.5-2 is a conditional model criterion. Eight-member composition depends on imposed inputs, removal, death and grid dynamics; these endpoints do not establish unqualified natural ecological equilibrium. |
| host-input | doi:10.1038/s41467-024-55222-w; Sec4/8/13/19-21; Figure2 pixels | supports | Two samples per metabolomics group inform candidate tissue-enriched host inputs. Origin/delivery remain assumptions, and host metabolism/respiration are excluded. |
| network | doi:10.1038/s41467-024-55222-w; Sec7-12; Figures4-6 pixels; focal SD7/11 exchange rows | supports | Alternative hypotaurine/laurate regimes change predicted exchange; a whole-network summary is not an independent cause of component routes or proof of active coordination. |
| deltaporibacter | doi:10.1038/s41467-024-55222-w; Sec10-11; Figures5-6 pixels; SD7 nitrate/NO and SD11 laurate/acetate rows | supports | Conditional predictions support nitrate reduction and NO release under hypotaurine, and laurate use with acetate donation under mixed inputs; no measured flux claimed. |
| carbon | doi:10.1038/s41467-024-55222-w; Sec8/11-13; Figures5-6 pixels | supports | Input-dependent microbial carbon balance excludes host respiration. Pathway carbon fixation does not establish every regime or the whole living holobiont as autotrophic. |
| model-methods | doi:10.1038/s41467-024-55222-w; Sec15-21; SI scientific methods/notes; SD5 selected media and SD9/13 | supports | Merged MAGs, gapseq 1.1 b568a4e/manual curation/gap-filling and BacArena 1.8.2 pFBA define simulations. Eight-member runs use 100 hourly cycles, 10 mM ammonia,10 percent removal and 5 percent death; distinguish single/two/three-member settings from these. |
| source-resources | doi:10.1038/s41467-024-55222-w; Data and Code Availability | supports | Focal model MODEL2407300002, broad prior project PRJNA602572 and STY8 v1.0.0 are source-reported. The linked MassIVE task and MSV000083743 currently describe EMP soil/fecal samples, leaving the focal metabolomics pointer unresolved. |
| record | kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml; Entire current file | supports | Three taxa, six nodes, two arrows; ENVO:01001002 and appended2026-10-25 history are the only changes since the frozen input. |
| pubmed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=39738126,39604529&amp;retmode=xml; Both PubmedArticle identities | supports | 39738126 is the sponge paper;39604529 is an unrelated NLRP3 author correction, contradicting the new history sidecar citation. |
| supplement | doi:10.1038/s41467-024-55222-w; MOESM1 scientific methods/notes/TablesS1-S3; MOESM5 SD2,9,12,13 and selected SD5/7/11 rows | supports | Model/MAG identities, reconstruction/curation assumptions and conditional exchanges corroborate the qualified graph. SD7/11 NO/nitrite identifier reversal and SD7 header-layout ambiguity remain source discrepancies rather than imported chemical IDs. |
| supplement-tables | doi:10.1038/s41467-024-55222-w; MOESM5; focal-tables.json retains selected sheets | supports | Eight listed members; scenario media and model parameter provenance. Focal nitrogen/acetate directions agree with narrative and figures; no raw matrix/statistics reanalysis. |
| schema | src/communitymech/schema/communitymech.yaml; MicrobialCommunity; EcologicalStateEnum; ComputationalProvenance | supports | STABLE means equilibrium; ecological_state is optional. Structured computational provenance is available for these fourteen computational claims. Environment presence is now repaired. |
| ontology | kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml; target-audit.json ontology_authorities; native validate-terms | supports | All 11 distinct pairs across 20 occurrences resolve with exact labels, including newly added ENVO:01001002 animal-associated environment. Canonical label validity is distinct from specificity and scientific support. |
| roster-authority | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=2973585,1671877,2973566,2881427&amp;retmode=xml; Four requested Taxon records | supports | Three Candidatus-prefixed species candidates and Parasynechococcus genus resolve. Other proposed names retain source-name uncertainty; this refresh makes no global negative identity claim. |
| resources | https://www.ebi.ac.uk/biomodels/model/files/MODEL2407300002?format=json; Fresh metadata/listing | supports | Exact combined-input RDS filename and eight model files verified as archive listings; payloads not parsed or executed. |
| model-identity | https://www.ebi.ac.uk/biomodels/MODEL2407300002?format=json; Fresh metadata/listing | supports | Archive title/description identify the focal eight-species Stylissa model. |
| bioproject | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=bioproject&amp;id=602572&amp;retmode=xml; Fresh metadata/listing | supports | Returned accession PRJNA602572 is a broad marine-sponge metagenome project, not solely four focal specimens or a metabolomics archive. |
| massive | https://massive.ucsd.edu/ProteoSAFe/dataset.jsp?accession=MSV000083743; Fresh metadata/listing | supports | Returned accession/task identifies public EMP soil and fecal GC-MS data. No replacement focal accession inferred. |
| code-tag | https://api.github.com/repos/zhssakura/STY8/git/ref/tags/v1.0.0; Fresh metadata/listing | supports | Tag resolves to 17fd9c4eb5bd1f4cdf2c6402a2cdf3958e380546; immutable tree inventory inspected, code not executed. |
| zenodo | https://zenodo.org/api/records/14030749; Fresh metadata/listing | supports | DOI10.5281/zenodo.14030749 is STY8 v1.0.0 software metadata linked to the source repository. |
| snippets | kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml; target-audit.json exact whitespace-normalized match | supports | All 14 current snippets match fresh primary XML; lexical matching does not certify each claim's scientific scope. |
| history | history/records/BioModels_MODEL2407300002_Sponge_Holobiont_Network/2026-10-25T151200Z-antigravity-2072.yaml; Full sidecar and inline curation history | supports | New environment block/append are preserved, but sidecar details cite unrelated 39604529. Correct with a new append-only record; do not rewrite the old entry. |
| native-target | kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml; target-audit.json and native metrics rubric | supports | No target network issues;6 nodes, 2 arrows, 9 node evidence items. Completeness 80; quality 100 capped from 104 with 2 P2 + 3 P3. Neither score is scientific approval. |
| source-scope | doi:10.1038/s41467-024-55222-w; Current author reading scope and source receipts | supports | Complete scientific main, all six main figures, scientific SI text and selected tables read. No model execution, raw sequence/spectra/statistical reanalysis or external code execution. |
| context-20261025T113500Z-c2s4-record-deep-audit | reviews/structured/20261025T113500Z-c2s4-record-deep-audit/review.yaml; Only ev-sponge-pmid39738126 or assess-c2s5-biomodels-environment-term and associated grouped lineage | supports | Bounded source correction: focal DOI 10.1038/s41467-024-55222-w, four Great Barrier Reef samples December 2015; not Red Sea or DOI s43705-024-00531-6. Prior purported source quotation is not present in focal primary text. Other cohort targets/dispositions not reassessed. |
| context-20261025T113600Z-c2s4-frozen-cohort-review | reviews/structured/20261025T113600Z-c2s4-frozen-cohort-review/review.yaml; Only ev-sponge-pmid39738126 or assess-c2s5-biomodels-environment-term and associated grouped lineage | supports | Bounded source correction: focal DOI 10.1038/s41467-024-55222-w, four Great Barrier Reef samples December 2015; not Red Sea or DOI s43705-024-00531-6. Prior purported source quotation is not present in focal primary text. Other cohort targets/dispositions not reassessed. |
| context-20261025T161500Z-c2s5-remediation-verification | reviews/structured/20261025T161500Z-c2s5-remediation-verification/review.yaml; Only ev-sponge-pmid39738126 or assess-c2s5-biomodels-environment-term and associated grouped lineage | supports | Bounded source correction: focal DOI 10.1038/s41467-024-55222-w, four Great Barrier Reef samples December 2015; not Red Sea or DOI s43705-024-00531-6. Prior purported source quotation is not present in focal primary text. Other cohort targets/dispositions not reassessed. |
| check-validate | just --no-dotenv validate kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml; Actual run 2026-11-06T06:05:07.107977Z to 2026-11-06T06:05:07.632594Z | supports | Documented focused/native check passed with exit 0. |
| check-validate-terms | just --no-dotenv validate-terms kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml; Actual run 2026-11-06T06:05:07.632640Z to 2026-11-06T06:05:08.761229Z | supports | Documented focused/native check passed with exit 0. |
| check-validate-gtdb | just --no-dotenv validate-gtdb kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml; Actual run 2026-11-06T06:05:08.761253Z to 2026-11-06T06:05:08.821360Z | supports | Documented focused/native check passed with exit 0. |
| check-validate-gtdb-domain | just --no-dotenv validate-gtdb-domain kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml; Actual run 2026-11-06T06:05:08.821383Z to 2026-11-06T06:05:09.725437Z | supports | Documented focused/native check passed with exit 0. |
| check-validate-references-explained | just --no-dotenv validate-references-explained kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml; Actual run 2026-11-06T06:05:09.725457Z to 2026-11-06T06:05:10.679260Z | supports | Documented focused/native check passed with exit 0. |
| check-validate-strict | just --no-dotenv validate-strict kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml --out /Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2043-batch07/.temp/pr2043/013/strict.tsv; Actual run 2026-11-06T06:05:10.679279Z to 2026-11-06T06:05:16.012597Z | supports | Documented focused/native check passed with exit 0. |
| check-validate-history | just --no-dotenv validate-history history/records/BioModels_MODEL2407300002_Sponge_Holobiont_Network; Actual run 2026-11-06T06:05:16.012616Z to 2026-11-06T06:05:16.542117Z | supports | Documented focused/native check passed with exit 0. |
| check-normalize-cache-names | /Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv/bin/python scripts/normalize_cache_names.py --check; Actual run 2026-11-06T06:05:16.542137Z to 2026-11-06T06:05:16.575379Z | supports | Documented focused/native check passed with exit 0. |
| check-audit-network | just --no-dotenv audit-network; Actual run 2026-11-06T06:06:14.244334+00:00 to 2026-11-06T06:06:18.574703+00:00 | supports | Full corpus: 44 warnings across 16 of 508 records,0 errors; known baseline, target has0 issues. |
| check-check-network-quality | just --no-dotenv check-network-quality; Actual run 2026-11-06T06:06:14.244470+00:00 to 2026-11-06T06:06:18.607826+00:00 | supports | Full corpus: 44 warnings across 16 of 508 records,0 errors; known baseline, target has0 issues. |

## Limits And Additional Notes

- Eight merged/representative MAG reconstructions are seven bacteria and one archaeon; no host model or cultured eight-strain consortium.98.3 percent denominator is MAG-mapped reads.
- Complete scientific main and all six main figure pixels were read, along with scientific SI text/TablesS1-S3. Supplementary figure captions were read, but SI figure pixels and whole raw SourceData matrices were not independently analyzed. SD2/9/12/13 were read; SD5/7/11 inspection is limited to relevant model media/exchange rows and headers.
- Candidate host inputs rely on two samples per group; source/delivery, host respiration and reciprocal fitness are unresolved. No model execution, RDS deserialization, external code execution, raw sequence/spectra/FISH/flux/statistical reanalysis.
- Current corpus checks exit 1 with44 warnings across 16 of 508 records,0 errors. Target native network has0 issues; neither is a whole-corpus scientific approval.
- SD7/11 NO/nitrite compound identifiers disagree and SD7 header placement differs from numeric pairs; use narrative/figures for bounded direction without importing those IDs. SI model-name variants and the S.thiooxidans abundance statement are not silently imported into canonical fields.
- Public archive metadata verifies listings and source pointers, not model reproducibility or correct focal metabolomics deposition. MSV000083743 currently resolves to EMP soil/fecal data; no replacement accession inferred.
- Fresh NCBI checks verify four candidate taxon records only. Proposed names otherwise retain uncertainty; no global absence or species-level GTDB mapping asserted. Historical GTDB support counts not recomputed.
- The initial inspection failed on CLAUDE.md symbolic-link resolution; readable canonical AGENTS.md was inspected instead. No file/symlink was changed. Initial wrong-owner STY8 URLs and aggregate-supplement timeout were retained as failed acquisition receipts; corrected public routes succeeded.
- Prior cohort-review context is assessed only for 000013. Their grouped multi-target finding dispositions remain untouched; this is an author refresh awaiting independent review.
- Immutable successor; original four stable keys retain exact previous_occurrences. No original bundle or canonical/cache/history file rewritten.
- Scratch candidates are JSON; only the native helper writes saved YAML/Markdown. Helper scripts were formatted before final inspection and are frozen inputs.
- Native input count: 32. Source receipt timestamps denote fresh retrieval; assertions reflect the separately stated actual reading scope.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261106T061348Z-pr2043-sponge-holobiont-successor
kind: record
repository: CultureBotAI/CommunityMech
title: Current-main sponge holobiont review and bounded source-context correction
started_at: '2026-11-06T06:04:02.889917Z'
finished_at: '2026-11-06T06:13:48.795691Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Author refresh; separate adversarial approval is not claimed
    here.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'The added animal-associated environment is supported; its repaired omission
  is removed from the residual context finding. All four original finding keys remain
  open: two P2 membership/state findings and two P3 computational/resource findings.
  A new P3 finding records an unrelated PMID in the appended history. Six qualified
  computational nodes and two conditional arrows remain supported. Bounded corrections
  identify the actual sponge DOI, Great Barrier Reef sampling and unsupported quotation
  in three prior cohort-review contexts without superseding their multi-target findings.'
source:
  git_revision: c1846ce378828d0a2e2d80312ac784a47430a617
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: d2f94c87b82f59663bc2b0c91ac04a245e56fab52d8c11e6bddb559eb9237c84
    role: context
  - path: .claude/skills/review-communities/reference/execution-protocol.md
    sha256: 0d4448074611c020c54b6b20c478b24e2cf2a195f7fc4f7dbcfac19134f731c4
    role: context
  - path: .claude/skills/review-communities/reference/metrics-and-reports.md
    sha256: 2647416ac98a8f9569e0afbd826a0d1229bb4262639934848639ce536b0974fc
    role: context
  - path: .claude/skills/review-communities/reference/validation-rules.md
    sha256: 3860e91a64f7c1f55f80e3d7a361d0798bbd00cbaf5cb7720a7533673e5afe2e
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 1005e1b9eb7f83306a1f88a6d22ec7954a54c2bf2e2fc15923fdaaa1111a3d2b
    role: context
  - path: AGENTS.md
    sha256: 8f23dcad7ed9c9873f00058995d1219cca8810c27ed5d787cb9b66a8abf96728
    role: context
  - path: conf/record_review.yaml
    sha256: c4ad25505a87a040c57eb93f1ee9673a09389a474c6d4e1136781456ff190fc8
    role: context
  - path: conf/reference_validator.yaml
    sha256: 5cd4781c7e15b7c5472f0b008e41764842cc023a7ba99f4273298f421be36652
    role: context
  - path: docs/record-review-profile.md
    sha256: 285f79747999f83edbe63e5efde349a5cc063e9e486ce1a748b47b76c6631f31
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/README.md
    sha256: 86c0347d77402bcecdec466b01974ad53beddb9cf1bd17cf085674970542a101
    role: context
  - path: history/records/BioModels_MODEL2407300002_Sponge_Holobiont_Network/2026-10-05T142601Z-codex-76c203.yaml
    sha256: 283858e364f718cdf1d04f09a035e19b5e8a5223edd8c80221191e55c06b2624
    role: context
  - path: history/records/BioModels_MODEL2407300002_Sponge_Holobiont_Network/2026-10-25T151200Z-antigravity-2072.yaml
    sha256: 8cfd91fc76f343236183048d7ac538b33a54c75ba7419c77a6186bfad80ce868
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml
    sha256: 2d2c5858211115cc74035f627a0a51376c22703929bfae077ebada161c6924c8
    role: target
  - path: references_cache/PMID_39738126.txt
    sha256: 9197188a018fe80ca6d1f44bc3ab9e102c254c2ce6fd131d82be516f45087d53
    role: context
  - path: references_cache/doi_10.1038_s41467-024-55222-w.json
    sha256: 1ef65854921cbf7f63876353922b315b71ac8a507f1f8b4f8bef55f0214c0bd2
    role: context
  - path: references_cache/doi_10.1038_s41467-024-55222-w.md
    sha256: 824118196672b53f3c367488b5ccf1e5a57f1ddeca0c3d671915b89a8490f436
    role: context
  - path: reports/causal_graph_review/decisions/20261005-twelve-records-batch8.yaml
    sha256: a03eceb4ca205fdd9092a4f18c0fa4c068e8ec91ee5a62d09da97b87a4f50a25
    role: context
  - path: reviews/structured/20261021T124426Z-sponge-holobiont-model-record/review.yaml
    sha256: 5d599562f4ba3dfa74817eb8fbae5df9850f632b447038db09cd084792885f5b
    role: context
  - path: reviews/structured/20261025T113500Z-c2s4-record-deep-audit/review.yaml
    sha256: 440a518b290067b197bb4b8549bc71408076d6fe93fe3ef5ce4a316f17edacef
    role: context
  - path: reviews/structured/20261025T113600Z-c2s4-frozen-cohort-review/review.yaml
    sha256: 702d202105025d44fc469e588a43967388443aad84a355bc80ea45ebab36338a
    role: context
  - path: reviews/structured/20261025T161500Z-c2s5-remediation-verification/review.yaml
    sha256: c8b7bd9b8e462081a734db496e8314848c4474a56deadbec891cf4af6f9ea644
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/adhoc/pr2043_013_audit.py
    sha256: e07a82d07de74f91a381663e686d4e48c2849b5cf1c7ccf57fc966a1b8dbac09
    role: context
  - path: scripts/adhoc/pr2043_013_review.py
    sha256: d448bec27b34553a4236d9303025563b58860d79812c1562afc98c2029c8567f
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: src/communitymech/network/auditor.py
    sha256: fe32aa2eddf9e09c153c47576f943bf08a6019f650bf2575e3ddc8e14675049b
    role: context
  - path: src/communitymech/ontology_adapters.py
    sha256: bb3803581ac2946b2ca8e14278e36cd660faf12db9237f9688a6cef577fa9016
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: a00434e0d75020b2926c9f755d625c09cc78b6f88135805991fcb0ecd4230c83
    role: context
  - path: src/communitymech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
    role: context
  - path: src/communitymech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
targets:
- target_id: CommunityMech:000013
  path: kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml
  label: BioModels MODEL2407300002 Sponge Holobiont Network
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml
    role: canonical_record
scope:
  description: Entire current record and source delta; complete primary scientific
    main, six main figures, scientific SI text, selected supplementary tables, public
    model/archive metadata and bounded prior-review source context.
  selection: PR2043 stale record CommunityMech:000013; no other cohort target reassessed.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000013
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Documented focused/native check passed with exit 0.
  target_ids:
  - CommunityMech:000013
  command: just --no-dotenv validate kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Reused canary Python 3.13 venv; UV_NO_SYNC=1 UV_OFFLINE=1 PYTHONPATH=src
    JUST_NO_DOTENV=true. Corpus failures are not target passes.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Documented focused/native check passed with exit 0.
  target_ids:
  - CommunityMech:000013
  command: just --no-dotenv validate-terms kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Reused canary Python 3.13 venv; UV_NO_SYNC=1 UV_OFFLINE=1 PYTHONPATH=src
    JUST_NO_DOTENV=true. Corpus failures are not target passes.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Documented focused/native check passed with exit 0.
  target_ids:
  - CommunityMech:000013
  command: just --no-dotenv validate-gtdb kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Reused canary Python 3.13 venv; UV_NO_SYNC=1 UV_OFFLINE=1 PYTHONPATH=src
    JUST_NO_DOTENV=true. Corpus failures are not target passes.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Documented focused/native check passed with exit 0.
  target_ids:
  - CommunityMech:000013
  command: just --no-dotenv validate-gtdb-domain kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Reused canary Python 3.13 venv; UV_NO_SYNC=1 UV_OFFLINE=1 PYTHONPATH=src
    JUST_NO_DOTENV=true. Corpus failures are not target passes.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Documented focused/native check passed with exit 0.
  target_ids:
  - CommunityMech:000013
  command: just --no-dotenv validate-references-explained kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Reused canary Python 3.13 venv; UV_NO_SYNC=1 UV_OFFLINE=1 PYTHONPATH=src
    JUST_NO_DOTENV=true. Corpus failures are not target passes.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Documented focused/native check passed with exit 0.
  target_ids:
  - CommunityMech:000013
  command: just --no-dotenv validate-strict kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml
    --out /Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2043-batch07/.temp/pr2043/013/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Reused canary Python 3.13 venv; UV_NO_SYNC=1 UV_OFFLINE=1 PYTHONPATH=src
    JUST_NO_DOTENV=true. Corpus failures are not target passes.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: Documented focused/native check passed with exit 0.
  target_ids:
  - CommunityMech:000013
  command: just --no-dotenv validate-history history/records/BioModels_MODEL2407300002_Sponge_Holobiont_Network
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Reused canary Python 3.13 venv; UV_NO_SYNC=1 UV_OFFLINE=1 PYTHONPATH=src
    JUST_NO_DOTENV=true. Corpus failures are not target passes.
- check_id: normalize-cache-names
  name: normalize-cache-names
  status: passed
  required: true
  summary: Documented focused/native check passed with exit 0.
  target_ids:
  - CommunityMech:000013
  command: /Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv/bin/python
    scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names
  scope_note: Reused canary Python 3.13 venv; UV_NO_SYNC=1 UV_OFFLINE=1 PYTHONPATH=src
    JUST_NO_DOTENV=true. Corpus failures are not target passes.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: 'Full corpus: 44 warnings across 16 of 508 records,0 errors; known baseline,
    target has0 issues.'
  target_ids:
  - CommunityMech:000013
  command: just --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  scope_note: Reused canary Python 3.13 venv; UV_NO_SYNC=1 UV_OFFLINE=1 PYTHONPATH=src
    JUST_NO_DOTENV=true. Corpus failures are not target passes.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: 'Full corpus: 44 warnings across 16 of 508 records,0 errors; known baseline,
    target has0 issues.'
  target_ids:
  - CommunityMech:000013
  command: just --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  scope_note: Reused canary Python 3.13 venv; UV_NO_SYNC=1 UV_OFFLINE=1 PYTHONPATH=src
    JUST_NO_DOTENV=true. Corpus failures are not target passes.
- check_id: scientific-source
  name: Fresh scientific source reassessment
  status: passed
  required: true
  summary: Four original findings reassessed; five current open findings. Author pass,
    not independent approval.
  target_ids:
  - CommunityMech:000013
  evidence_ids:
  - source-scope
  - pubmed
  - resources
- check_id: structured-adapter
  name: iModulonDB applicability
  status: not_applicable
  required: false
  summary: No focal gene/locus/accession or covered strain-specific transcriptomic
    dataset is asserted; this is a MAG-derived model community.
  target_ids:
  - CommunityMech:000013
  evidence_ids:
  - record
  - model-methods
- check_id: cross-mech
  name: Culture/ingredient identifiers
  status: not_applicable
  required: false
  summary: No CultureMech/MediaIngredientMech link encoded; in-silico media are not
    wetlab cultivation.
  target_ids:
  - CommunityMech:000013
  evidence_ids:
  - record
  - model-methods
evidence:
- evidence_id: roster
  kind: primary_source
  reference: doi:10.1038/s41467-024-55222-w
  locator: Sec3/15-17; Figure1 pixels; SD2 rows4-11
  summary: Eight named merged/representative MAG reconstructions (seven bacteria,
    one archaeon) represent 98.3 percent of MAG-mapped reads. Three broad current
    entries omit five members.
  support: supports
  accessed_at: '2026-11-06T06:05:14.661778Z'
  snapshot_sha256: 4abe065eaece8d6942cc7549bef83efb8015d6648441b9f4a320680f60b88768
- evidence_id: nitrification
  kind: primary_source
  reference: doi:10.1038/s41467-024-55222-w
  locator: Sec5-6; Figure3 pixels; SI CenSfMM8/NitSfMM6 curation and TableS1
  summary: Predicted archaeal nitrite supports bacterial nitrifier growth after an
    NO-forming reaction is disabled; neither measured partner transfer nor thermodynamic
    obligacy follows.
  support: supports
  accessed_at: '2026-11-06T06:05:14.661778Z'
  snapshot_sha256: 4abe065eaece8d6942cc7549bef83efb8015d6648441b9f4a320680f60b88768
- evidence_id: stability
  kind: primary_source
  reference: doi:10.1038/s41467-024-55222-w
  locator: Sec6-7/21; Figures3-4 pixels
  summary: Normalized final/initial AOA:NOB ratio of 0.5-2 is a conditional model
    criterion. Eight-member composition depends on imposed inputs, removal, death
    and grid dynamics; these endpoints do not establish unqualified natural ecological
    equilibrium.
  support: supports
  accessed_at: '2026-11-06T06:05:14.661778Z'
  snapshot_sha256: 4abe065eaece8d6942cc7549bef83efb8015d6648441b9f4a320680f60b88768
- evidence_id: host-input
  kind: primary_source
  reference: doi:10.1038/s41467-024-55222-w
  locator: Sec4/8/13/19-21; Figure2 pixels
  summary: Two samples per metabolomics group inform candidate tissue-enriched host
    inputs. Origin/delivery remain assumptions, and host metabolism/respiration are
    excluded.
  support: supports
  accessed_at: '2026-11-06T06:05:14.661778Z'
  snapshot_sha256: 4abe065eaece8d6942cc7549bef83efb8015d6648441b9f4a320680f60b88768
- evidence_id: network
  kind: primary_source
  reference: doi:10.1038/s41467-024-55222-w
  locator: Sec7-12; Figures4-6 pixels; focal SD7/11 exchange rows
  summary: Alternative hypotaurine/laurate regimes change predicted exchange; a whole-network
    summary is not an independent cause of component routes or proof of active coordination.
  support: supports
  accessed_at: '2026-11-06T06:05:14.661778Z'
  snapshot_sha256: 4abe065eaece8d6942cc7549bef83efb8015d6648441b9f4a320680f60b88768
- evidence_id: deltaporibacter
  kind: primary_source
  reference: doi:10.1038/s41467-024-55222-w
  locator: Sec10-11; Figures5-6 pixels; SD7 nitrate/NO and SD11 laurate/acetate rows
  summary: Conditional predictions support nitrate reduction and NO release under
    hypotaurine, and laurate use with acetate donation under mixed inputs; no measured
    flux claimed.
  support: supports
  accessed_at: '2026-11-06T06:05:14.661778Z'
  snapshot_sha256: 4abe065eaece8d6942cc7549bef83efb8015d6648441b9f4a320680f60b88768
- evidence_id: carbon
  kind: primary_source
  reference: doi:10.1038/s41467-024-55222-w
  locator: Sec8/11-13; Figures5-6 pixels
  summary: Input-dependent microbial carbon balance excludes host respiration. Pathway
    carbon fixation does not establish every regime or the whole living holobiont
    as autotrophic.
  support: supports
  accessed_at: '2026-11-06T06:05:14.661778Z'
  snapshot_sha256: 4abe065eaece8d6942cc7549bef83efb8015d6648441b9f4a320680f60b88768
- evidence_id: model-methods
  kind: primary_source
  reference: doi:10.1038/s41467-024-55222-w
  locator: Sec15-21; SI scientific methods/notes; SD5 selected media and SD9/13
  summary: Merged MAGs, gapseq 1.1 b568a4e/manual curation/gap-filling and BacArena
    1.8.2 pFBA define simulations. Eight-member runs use 100 hourly cycles, 10 mM
    ammonia,10 percent removal and 5 percent death; distinguish single/two/three-member
    settings from these.
  support: supports
  accessed_at: '2026-11-06T06:05:14.661778Z'
  snapshot_sha256: 4abe065eaece8d6942cc7549bef83efb8015d6648441b9f4a320680f60b88768
- evidence_id: source-resources
  kind: primary_source
  reference: doi:10.1038/s41467-024-55222-w
  locator: Data and Code Availability
  summary: Focal model MODEL2407300002, broad prior project PRJNA602572 and STY8 v1.0.0
    are source-reported. The linked MassIVE task and MSV000083743 currently describe
    EMP soil/fecal samples, leaving the focal metabolomics pointer unresolved.
  support: supports
  accessed_at: '2026-11-06T06:05:14.661778Z'
  snapshot_sha256: 4abe065eaece8d6942cc7549bef83efb8015d6648441b9f4a320680f60b88768
- evidence_id: record
  kind: record_content
  reference: kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml
  locator: Entire current file
  summary: Three taxa, six nodes, two arrows; ENVO:01001002 and appended2026-10-25
    history are the only changes since the frozen input.
  support: supports
  accessed_at: '2026-11-06T06:13:48.795691Z'
  snapshot_sha256: 2d2c5858211115cc74035f627a0a51376c22703929bfae077ebada161c6924c8
- evidence_id: pubmed
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=39738126,39604529&retmode=xml
  locator: Both PubmedArticle identities
  summary: 39738126 is the sponge paper;39604529 is an unrelated NLRP3 author correction,
    contradicting the new history sidecar citation.
  support: supports
  accessed_at: '2026-11-06T06:13:48.795691Z'
  snapshot_sha256: e5d4d3ecf1c93063c0286e51a0c7c95214d85f0b431e921dcf9a80d1649b7d43
- evidence_id: supplement
  kind: primary_source
  reference: doi:10.1038/s41467-024-55222-w
  locator: MOESM1 scientific methods/notes/TablesS1-S3; MOESM5 SD2,9,12,13 and selected
    SD5/7/11 rows
  summary: Model/MAG identities, reconstruction/curation assumptions and conditional
    exchanges corroborate the qualified graph. SD7/11 NO/nitrite identifier reversal
    and SD7 header-layout ambiguity remain source discrepancies rather than imported
    chemical IDs.
  support: supports
  accessed_at: '2026-11-06T06:13:48.795691Z'
  snapshot_sha256: ada2c347ba4450aa34647cfa7b12fd54cdf6186924ed0cb0afbf17f5c1832202
- evidence_id: supplement-tables
  kind: primary_source
  reference: doi:10.1038/s41467-024-55222-w
  locator: MOESM5; focal-tables.json retains selected sheets
  summary: Eight listed members; scenario media and model parameter provenance. Focal
    nitrogen/acetate directions agree with narrative and figures; no raw matrix/statistics
    reanalysis.
  support: supports
  accessed_at: '2026-11-06T06:13:48.795691Z'
  snapshot_sha256: e0471a524b6621bb824caa95a67e0f7749c90e2bba187af11a254093258276d4
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: MicrobialCommunity; EcologicalStateEnum; ComputationalProvenance
  summary: STABLE means equilibrium; ecological_state is optional. Structured computational
    provenance is available for these fourteen computational claims. Environment presence
    is now repaired.
  support: supports
  accessed_at: '2026-11-06T06:13:48.795691Z'
  snapshot_sha256: a00434e0d75020b2926c9f755d625c09cc78b6f88135805991fcb0ecd4230c83
- evidence_id: ontology
  kind: authority
  reference: kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml
  locator: target-audit.json ontology_authorities; native validate-terms
  summary: All 11 distinct pairs across 20 occurrences resolve with exact labels,
    including newly added ENVO:01001002 animal-associated environment. Canonical label
    validity is distinct from specificity and scientific support.
  support: supports
  accessed_at: '2026-11-06T06:13:48.795691Z'
  snapshot_sha256: 0d06643e3f046261ab962516d1838d01e65c1f09c1f0e396c9f29f4a16cb67a5
- evidence_id: roster-authority
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=2973585,1671877,2973566,2881427&retmode=xml
  locator: Four requested Taxon records
  summary: Three Candidatus-prefixed species candidates and Parasynechococcus genus
    resolve. Other proposed names retain source-name uncertainty; this refresh makes
    no global negative identity claim.
  support: supports
  accessed_at: '2026-11-06T06:13:48.795691Z'
  snapshot_sha256: e5498ecc4a6e28e1dcf3be7638507074889b2f8753af9cdbd003a5901caa32ec
- evidence_id: resources
  kind: database
  reference: https://www.ebi.ac.uk/biomodels/model/files/MODEL2407300002?format=json
  locator: Fresh metadata/listing
  summary: Exact combined-input RDS filename and eight model files verified as archive
    listings; payloads not parsed or executed.
  support: supports
  accessed_at: '2026-11-06T06:13:48.795691Z'
  snapshot_sha256: 1cd5886b2178517d30623001c7ebe2b7efc147b70ccd3943d40f7dad8ae0329a
- evidence_id: model-identity
  kind: database
  reference: https://www.ebi.ac.uk/biomodels/MODEL2407300002?format=json
  locator: Fresh metadata/listing
  summary: Archive title/description identify the focal eight-species Stylissa model.
  support: supports
  accessed_at: '2026-11-06T06:13:48.795691Z'
  snapshot_sha256: ef4eb8757600ab9b0ff9ffa28cad74f125fb90446425167f37d8b75df6c6a855
- evidence_id: bioproject
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=bioproject&id=602572&retmode=xml
  locator: Fresh metadata/listing
  summary: Returned accession PRJNA602572 is a broad marine-sponge metagenome project,
    not solely four focal specimens or a metabolomics archive.
  support: supports
  accessed_at: '2026-11-06T06:13:48.795691Z'
  snapshot_sha256: a323e6e6333ca3afcd6cd8e33c8e573cff04edb89c3cbd8115967cdabff28cdc
- evidence_id: massive
  kind: database
  reference: https://massive.ucsd.edu/ProteoSAFe/dataset.jsp?accession=MSV000083743
  locator: Fresh metadata/listing
  summary: Returned accession/task identifies public EMP soil and fecal GC-MS data.
    No replacement focal accession inferred.
  support: supports
  accessed_at: '2026-11-06T06:13:48.795691Z'
  snapshot_sha256: 68da838b727b155e00613f31c0c89cfa302a7565e05741bba2bbec9759474708
- evidence_id: code-tag
  kind: database
  reference: https://api.github.com/repos/zhssakura/STY8/git/ref/tags/v1.0.0
  locator: Fresh metadata/listing
  summary: Tag resolves to 17fd9c4eb5bd1f4cdf2c6402a2cdf3958e380546; immutable tree
    inventory inspected, code not executed.
  support: supports
  accessed_at: '2026-11-06T06:13:48.795691Z'
  snapshot_sha256: 3475f210e2504598ef4ec5d8c1941b130ac4bdb12b0b7844096f47cb26f3dc77
- evidence_id: zenodo
  kind: database
  reference: https://zenodo.org/api/records/14030749
  locator: Fresh metadata/listing
  summary: DOI10.5281/zenodo.14030749 is STY8 v1.0.0 software metadata linked to the
    source repository.
  support: supports
  accessed_at: '2026-11-06T06:13:48.795691Z'
  snapshot_sha256: 86a63ffecfc35b2965be09b8752e6f1571cacfd4e61df521837e94562407e15d
- evidence_id: snippets
  kind: validation
  reference: kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml
  locator: target-audit.json exact whitespace-normalized match
  summary: All 14 current snippets match fresh primary XML; lexical matching does
    not certify each claim's scientific scope.
  support: supports
  accessed_at: '2026-11-06T06:13:48.795691Z'
  snapshot_sha256: 0d06643e3f046261ab962516d1838d01e65c1f09c1f0e396c9f29f4a16cb67a5
- evidence_id: history
  kind: record_content
  reference: history/records/BioModels_MODEL2407300002_Sponge_Holobiont_Network/2026-10-25T151200Z-antigravity-2072.yaml
  locator: Full sidecar and inline curation history
  summary: New environment block/append are preserved, but sidecar details cite unrelated
    39604529. Correct with a new append-only record; do not rewrite the old entry.
  support: supports
  accessed_at: '2026-11-06T06:13:48.795691Z'
  snapshot_sha256: 8cfd91fc76f343236183048d7ac538b33a54c75ba7419c77a6186bfad80ce868
- evidence_id: native-target
  kind: validation
  reference: kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml
  locator: target-audit.json and native metrics rubric
  summary: No target network issues;6 nodes, 2 arrows, 9 node evidence items. Completeness
    80; quality 100 capped from 104 with 2 P2 + 3 P3. Neither score is scientific
    approval.
  support: supports
  accessed_at: '2026-11-06T06:13:48.795691Z'
  snapshot_sha256: 0d06643e3f046261ab962516d1838d01e65c1f09c1f0e396c9f29f4a16cb67a5
- evidence_id: source-scope
  kind: validation
  reference: doi:10.1038/s41467-024-55222-w
  locator: Current author reading scope and source receipts
  summary: Complete scientific main, all six main figures, scientific SI text and
    selected tables read. No model execution, raw sequence/spectra/statistical reanalysis
    or external code execution.
  support: supports
  accessed_at: '2026-11-06T06:13:48.795691Z'
  snapshot_sha256: 4abe065eaece8d6942cc7549bef83efb8015d6648441b9f4a320680f60b88768
- evidence_id: context-20261025T113500Z-c2s4-record-deep-audit
  kind: record_content
  reference: reviews/structured/20261025T113500Z-c2s4-record-deep-audit/review.yaml
  locator: Only ev-sponge-pmid39738126 or assess-c2s5-biomodels-environment-term and
    associated grouped lineage
  summary: 'Bounded source correction: focal DOI 10.1038/s41467-024-55222-w, four
    Great Barrier Reef samples December 2015; not Red Sea or DOI s43705-024-00531-6.
    Prior purported source quotation is not present in focal primary text. Other cohort
    targets/dispositions not reassessed.'
  support: supports
  accessed_at: '2026-11-06T06:13:48.795691Z'
  snapshot_sha256: 440a518b290067b197bb4b8549bc71408076d6fe93fe3ef5ce4a316f17edacef
- evidence_id: context-20261025T113600Z-c2s4-frozen-cohort-review
  kind: record_content
  reference: reviews/structured/20261025T113600Z-c2s4-frozen-cohort-review/review.yaml
  locator: Only ev-sponge-pmid39738126 or assess-c2s5-biomodels-environment-term and
    associated grouped lineage
  summary: 'Bounded source correction: focal DOI 10.1038/s41467-024-55222-w, four
    Great Barrier Reef samples December 2015; not Red Sea or DOI s43705-024-00531-6.
    Prior purported source quotation is not present in focal primary text. Other cohort
    targets/dispositions not reassessed.'
  support: supports
  accessed_at: '2026-11-06T06:13:48.795691Z'
  snapshot_sha256: 702d202105025d44fc469e588a43967388443aad84a355bc80ea45ebab36338a
- evidence_id: context-20261025T161500Z-c2s5-remediation-verification
  kind: record_content
  reference: reviews/structured/20261025T161500Z-c2s5-remediation-verification/review.yaml
  locator: Only ev-sponge-pmid39738126 or assess-c2s5-biomodels-environment-term and
    associated grouped lineage
  summary: 'Bounded source correction: focal DOI 10.1038/s41467-024-55222-w, four
    Great Barrier Reef samples December 2015; not Red Sea or DOI s43705-024-00531-6.
    Prior purported source quotation is not present in focal primary text. Other cohort
    targets/dispositions not reassessed.'
  support: supports
  accessed_at: '2026-11-06T06:13:48.795691Z'
  snapshot_sha256: c8b7bd9b8e462081a734db496e8314848c4474a56deadbec891cf4af6f9ea644
- evidence_id: check-validate
  kind: validation
  reference: just --no-dotenv validate kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml
  locator: Actual run 2026-11-06T06:05:07.107977Z to 2026-11-06T06:05:07.632594Z
  summary: Documented focused/native check passed with exit 0.
  support: supports
  accessed_at: '2026-11-06T06:05:07.632594Z'
  snapshot_sha256: de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- evidence_id: check-validate-terms
  kind: validation
  reference: just --no-dotenv validate-terms kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml
  locator: Actual run 2026-11-06T06:05:07.632640Z to 2026-11-06T06:05:08.761229Z
  summary: Documented focused/native check passed with exit 0.
  support: supports
  accessed_at: '2026-11-06T06:05:08.761229Z'
  snapshot_sha256: 23acda1c1d3194d12bc947d897d07de83f4a076a9d93c135148885108530e018
- evidence_id: check-validate-gtdb
  kind: validation
  reference: just --no-dotenv validate-gtdb kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml
  locator: Actual run 2026-11-06T06:05:08.761253Z to 2026-11-06T06:05:08.821360Z
  summary: Documented focused/native check passed with exit 0.
  support: supports
  accessed_at: '2026-11-06T06:05:08.821360Z'
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: just --no-dotenv validate-gtdb-domain kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml
  locator: Actual run 2026-11-06T06:05:08.821383Z to 2026-11-06T06:05:09.725437Z
  summary: Documented focused/native check passed with exit 0.
  support: supports
  accessed_at: '2026-11-06T06:05:09.725437Z'
  snapshot_sha256: ede937293c42cad366f434dce49a485a9a0c56fe86620b52ca243ad10e09ecae
- evidence_id: check-validate-references-explained
  kind: validation
  reference: just --no-dotenv validate-references-explained kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml
  locator: Actual run 2026-11-06T06:05:09.725457Z to 2026-11-06T06:05:10.679260Z
  summary: Documented focused/native check passed with exit 0.
  support: supports
  accessed_at: '2026-11-06T06:05:10.679260Z'
  snapshot_sha256: 4aa3b29320f67595eddf0c8c05e2f9283494b516d1e515900a5ae5f0cdf5cf52
- evidence_id: check-validate-strict
  kind: validation
  reference: just --no-dotenv validate-strict kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml
    --out /Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2043-batch07/.temp/pr2043/013/strict.tsv
  locator: Actual run 2026-11-06T06:05:10.679279Z to 2026-11-06T06:05:16.012597Z
  summary: Documented focused/native check passed with exit 0.
  support: supports
  accessed_at: '2026-11-06T06:05:16.012597Z'
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: check-validate-history
  kind: validation
  reference: just --no-dotenv validate-history history/records/BioModels_MODEL2407300002_Sponge_Holobiont_Network
  locator: Actual run 2026-11-06T06:05:16.012616Z to 2026-11-06T06:05:16.542117Z
  summary: Documented focused/native check passed with exit 0.
  support: supports
  accessed_at: '2026-11-06T06:05:16.542117Z'
  snapshot_sha256: de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- evidence_id: check-normalize-cache-names
  kind: validation
  reference: /Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv/bin/python
    scripts/normalize_cache_names.py --check
  locator: Actual run 2026-11-06T06:05:16.542137Z to 2026-11-06T06:05:16.575379Z
  summary: Documented focused/native check passed with exit 0.
  support: supports
  accessed_at: '2026-11-06T06:05:16.575379Z'
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: check-audit-network
  kind: validation
  reference: just --no-dotenv audit-network
  locator: Actual run 2026-11-06T06:06:14.244334+00:00 to 2026-11-06T06:06:18.574703+00:00
  summary: 'Full corpus: 44 warnings across 16 of 508 records,0 errors; known baseline,
    target has0 issues.'
  support: supports
  accessed_at: '2026-11-06T06:06:18.574703Z'
  snapshot_sha256: e8ebf9ba0a67e945a00eb7ee67c5cc886a3fa5165ceeea6dad115d754cbb144a
- evidence_id: check-check-network-quality
  kind: validation
  reference: just --no-dotenv check-network-quality
  locator: Actual run 2026-11-06T06:06:14.244470+00:00 to 2026-11-06T06:06:18.607826+00:00
  summary: 'Full corpus: 44 warnings across 16 of 508 records,0 errors; known baseline,
    target has0 issues.'
  support: supports
  accessed_at: '2026-11-06T06:06:18.607826Z'
  snapshot_sha256: f9a8e9fb5a4e4ea545236a809393dbc1ce4325b14579c65a3130bcfe713e798a
assessments:
- assessment_id: identity
  area: identity
  topic: Sponge microbiome model scope
  outcome: concern
  summary: The archive identity is correct, but three guild entries do not represent
    all eight reconstructed members.
  target_ids:
  - CommunityMech:000013
  evidence_ids:
  - roster
  - roster-authority
  - resources
  dimensions:
  - name: community_scope
    value: Eight modeled microbial species, seven bacteria and one archaeon
    definition: A dominant modeled subset of the natural Stylissa microbiome; no host
      reconstruction and no cultured eight-strain consortium.
    evidence_ids:
    - roster
    - host-input
  - name: source_strain
    value: Representative and merged MAG identities
    definition: Preserve species, model identifiers and MAG provenance; merged MAGs
      are not culture-collection strains.
    evidence_ids:
    - roster
    - supplement
  - name: environment
    value: Natural shallow-water Stylissa mesohyl represented computationally
    definition: Four sponge specimens were sampled at the Great Barrier Reef in December
      2015. Grid geometry and replenishment are model inputs, not vessel or culture
      conditions.
    evidence_ids:
    - roster
    - model-methods
  - name: medium
    value: Seawater-derived in-silico media with scenario-specific inputs
    definition: Hypotaurine, laurate, ammonia, diffusion, removal and death settings
      belong to computational provenance.
    evidence_ids:
    - model-methods
    - supplement
  - name: experimental_setting
    value: Metagenome/metabolomics-informed pFBA simulations
    definition: Individual growth tests and two-/three-/eight-member simulations use
      distinct settings; tissue enrichment informs candidate host inputs.
    evidence_ids:
    - model-methods
    - host-input
  - name: evidence_tier
    value: COMPUTATIONAL predictions informed by environmental observations
    definition: Fluxes and host origin are not validated by direct partner-transfer
      or host-fitness measurements.
    evidence_ids:
    - host-input
    - network
  - name: grounding_status
    value: Current broad terms valid; more specific identities partly recoverable
    definition: Use verified names/CURIEs where available and explicit uncertainty
      elsewhere. No guessed species or species-level GTDB mapping.
    evidence_ids:
    - ontology
    - roster-authority
- assessment_id: taxonomy
  area: grounding
  topic: Eight-member composition and roles
  outcome: concern
  summary: The current three broad entries have supported conditional roles but omit
    five named reconstructions.
  target_ids:
  - CommunityMech:000013
  evidence_ids:
  - roster
  - roster-authority
  - supplement
  details: Missing Spongiicolonus versatilis, Spongiihabitans thiooxidans, Oxydemutator
    thiolithooxidans, Parasynechococcus marinus and Gammaporibacter thiotrophicus
    materially changes the represented metabolic roster. Cenoporarchaeum/Nitrospongiibacter
    producer roles and Deltaporibacter cross-feeding are source-supported in modeled
    regimes; attach specific evidence rather than the generic network snippet.
- assessment_id: state
  area: evidence
  topic: 'ecological_state: STABLE'
  outcome: concern
  summary: An unqualified ecological-equilibrium label is not established by the conditional
    simulation endpoints.
  target_ids:
  - CommunityMech:000013
  evidence_ids:
  - stability
  - schema
  details: Distinguish the ratio-of-ratios criterion for the nitrifying model from
    eight-member Bray–Curtis similarity and late-cycle stabilization. The optional
    schema field may be omitted or supported with an explicit scope; do not automatically
    substitute ENGINEERED or TRANSIENT. NATURAL origin remains appropriate for the
    modeled microbiome.
- assessment_id: node-0
  area: graph
  topic: ecological_interactions[0]
  outcome: supported
  summary: Retain modeled nitrite cross-feeding.
  target_ids:
  - CommunityMech:000013
  evidence_ids:
  - nitrification
  - supplement
  details: C. stylissae ammonia oxidation provides nitrite to N. stylissae. NO-reaction
    disabling and nutrient/removal constraints are explicit; neither measured transfer
    nor thermodynamic obligacy is established.
- assessment_id: arrow-0
  area: graph
  topic: ecological_interactions[0].downstream[0]
  outcome: supported
  summary: Retain conditional nitrification → nitrifier growth support.
  target_ids:
  - CommunityMech:000013
  evidence_ids:
  - nitrification
  - stability
  details: C. stylissae supplies the substrate for N. stylissae growth; joint persistence
    depends on imposed ammonia and removal. This is a source-supported model mechanism,
    not a general ecological stability claim.
- assessment_id: node-1
  area: graph
  topic: ecological_interactions[1]
  outcome: supported
  summary: Retain the nutrient-responsive eight-member exchange network.
  target_ids:
  - CommunityMech:000013
  evidence_ids:
  - network
  - deltaporibacter
  details: Alternative input regimes affect predicted exchanges; Deltaporibacter is
    a participant, not a demonstrated active coordinator. Preserve the removal of
    part-whole/common-input summary arrows.
- assessment_id: node-2
  area: graph
  topic: ecological_interactions[2]
  outcome: supported
  summary: Retain candidate host nutrient inputs with the existing uncertainty.
  target_ids:
  - CommunityMech:000013
  evidence_ids:
  - host-input
  - model-methods
  details: Tissue-enriched substrates are treated as available to microbial models.
    Origin and delivery are assumptions, and the host is an external context rather
    than a modeled fitness beneficiary.
- assessment_id: arrow-2
  area: graph
  topic: ecological_interactions[2].downstream[0]
  outcome: supported
  summary: Retain conditional candidate-input → microbial exchange direction.
  target_ids:
  - CommunityMech:000013
  evidence_ids:
  - host-input
  - network
  details: Supplying selected substrates changes the available model resources and
    predicted exchanges. It does not establish host secretion, reciprocal fitness
    or the same fluxes in vivo.
- assessment_id: node-3
  area: graph
  topic: ecological_interactions[3]
  outcome: supported
  summary: Retain the operational nitrifier stability endpoint.
  target_ids:
  - CommunityMech:000013
  evidence_ids:
  - stability
  - nitrification
  details: The final/initial AOA:NOB population-ratio criterion is correctly stated
    as 0.5–2. It is not an absolute abundance bound, measured environmental threshold
    or independent syntrophic interaction.
- assessment_id: node-4
  area: graph
  topic: ecological_interactions[4]
  outcome: supported
  summary: Retain condition-specific Deltaporibacter nitrogen-linked exchange.
  target_ids:
  - CommunityMech:000013
  evidence_ids:
  - deltaporibacter
  - network
  - supplement
  details: Hypotaurine scenarios predict nitrate reduction and NO release; mixed-input
    scenarios predict laurate use and acetate donation. Neither active coordination
    nor measured flux is asserted.
- assessment_id: node-5
  area: graph
  topic: ecological_interactions[5]
  outcome: supported
  summary: Retain nutrient-dependent microbial carbon balance.
  target_ids:
  - CommunityMech:000013
  evidence_ids:
  - carbon
  - host-input
  details: This aggregate model endpoint excludes host respiration. Carbon fixation
    is a contributing process and does not make every input regime or the whole living
    holobiont autotrophic.
- assessment_id: provenance
  area: provenance
  topic: Model assumptions, source context and cultivation
  outcome: concern
  summary: The new host-associated environment is supported; fourteen computational
    claims still lack structured provenance.
  target_ids:
  - CommunityMech:000013
  evidence_ids:
  - model-methods
  - host-input
  - schema
  details: Retain ENVO:01001002 and its source-backed sponge context. Recover software/model/MAG/scenario
    provenance with no invented cultivation. Natural sampling is Great Barrier Reef,
    December 2015; simulated mesohyl and medium constraints are model context. No
    requirement to populate all optional fields.
- assessment_id: resources
  area: provenance
  topic: Model, code and data resources
  outcome: concern
  summary: The exact RDS listing is valid; the bibliography-as-dataset and omitted
    source-resource context need repair.
  target_ids:
  - CommunityMech:000013
  evidence_ids:
  - resources
  - source-resources
  - bioproject
  - massive
  - code-tag
  - zenodo
  details: PRJNA602572 is a broad prior marine-sponge project, not solely the four
    focal specimens or a metabolomics archive. STY8 v1.0.0 and Zenodo 14030749 are
    verified metadata/code inventories. The paper-linked MSV000083743 currently describes
    EMP soil/fecal samples; resolve before claiming a focal metabolomics link. RDS
    objects were not parsed or executed.
- assessment_id: history
  area: provenance
  topic: Prior repairs, evidence and current limitations
  outcome: concern
  summary: All 14 snippets match and graph repairs persist, but the appended history
    cites an unrelated source.
  target_ids:
  - CommunityMech:000013
  evidence_ids:
  - history
  - pubmed
  - snippets
  - source-scope
  details: Environment addition is sound; sidecar PMID:39604529 needs append-only
    correction. Historic unread-source limitations are not rewritten. This current
    author read expanded primary/supplement scope; no canonical/cache/history content
    changed.
- assessment_id: validation
  area: schema
  topic: Native checks and ontology semantics
  outcome: supported
  summary: Eight native checks pass; this does not resolve membership or scope findings.
  target_ids:
  - CommunityMech:000013
  evidence_ids:
  - check-validate
  - check-validate-references-explained
  - ontology
  - schema
- assessment_id: metrics
  area: completeness
  topic: Native mechanical scores
  outcome: supported
  summary: Completeness rises 75 to 80 after environment repair; quality remains capped
    100, distinct from five open findings.
  target_ids:
  - CommunityMech:000013
  evidence_ids:
  - native-target
  metrics:
  - name: completeness
    value: 80
    unit: points
    minimum: 0
    maximum: 100
    definition: 50required-fields/roles +5environment +10nodes +5resources +5datasets
      +5metabolites; factor/media bonuses0.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100-50P1-10P2-2P3+20min(mean node evidence/2,1)+15ifCOMPLETE,0,100);
      P1=0/P2=2/P3=3/P4=0,9/6mean evidence, raw 104 capped 100.
  - name: P1
    value: 0
    unit: findings
    definition: Native severity count.
  - name: P2
    value: 2
    unit: findings
    definition: Native severity count.
  - name: P3
    value: 3
    unit: findings
    definition: Native severity count.
  - name: P4
    value: 0
    unit: findings
    definition: Native severity count.
- assessment_id: bounded-prior-source-correction
  area: provenance
  topic: Sponge-specific context in c2s4/c2s5 reviews
  outcome: supported
  target_ids:
  - CommunityMech:000013
  evidence_ids:
  - pubmed
  - roster
  - model-methods
  - context-20261025T113500Z-c2s4-record-deep-audit
  - context-20261025T113600Z-c2s4-frozen-cohort-review
  - context-20261025T161500Z-c2s5-remediation-verification
  summary: Correct the sponge source identity, geography and unsupported quotation
    in three prior-review contexts.
  details: The two c2s4 ev-sponge-pmid39738126 entries incorrectly couple PMID:39738126
    with DOI 10.1038/s43705-024-00531-6 and a Red Sea statement presented as a quotation.
    The focal source instead identifies DOI 10.1038/s41467-024-55222-w and four Great
    Barrier Reef specimens collected December 2015; the quoted sentence is not present.
    The c2s5 environment assessment repeats Red Sea and is corrected here only for
    000013. ENVO:01001002 remains sound. No terminal disposition or supersession of
    communitymech-c2s4-biomodels-missing-environment-term is made, and 000006/000007/000008
    are not assessed or dropped from that grouped lineage.
findings:
- finding_id: eight-member-roster
  issue_key: cm-000013-eight-member-roster
  category: completeness
  severity: major
  native_severity: P2
  normalization_reason: 'P2: material membership or evidence-scope defect; graph qualifications
    remain intact.'
  rule_id: review-checklist.claim-scope-and-completeness
  status: open
  certainty: confirmed
  title: Represent all eight modeled microbial members
  description: Three domain-grounded guild entries omit five named reconstructions
    and do not preserve the full source model composition.
  target_ids:
  - CommunityMech:000013
  field_paths:
  - taxonomy
  evidence_ids:
  - roster
  - roster-authority
  - resources
  - supplement
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T124426Z-sponge-holobiont-model-record
    finding_id: eight-member-roster
- finding_id: stable-state
  issue_key: cm-000013-stable-state
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: 'P2: material membership or evidence-scope defect; graph qualifications
    remain intact.'
  rule_id: review-checklist.claim-scope-and-completeness
  status: open
  certainty: confirmed
  title: Bound ecological state to the demonstrated evidence
  description: STABLE globally asserts ecological equilibrium while the source demonstrates
    conditional model composition outcomes under imposed inputs and turnover.
  target_ids:
  - CommunityMech:000013
  field_paths:
  - ecological_state
  evidence_ids:
  - stability
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T124426Z-sponge-holobiont-model-record
    finding_id: stable-state
- finding_id: computational-context
  issue_key: cm-000013-computational-context
  category: provenance
  severity: minor
  native_severity: P3
  normalization_reason: 'P3: bounded recoverable provenance/resource gap; graph qualifications
    remain intact.'
  rule_id: review-checklist.claim-scope-and-completeness
  status: open
  certainty: confirmed
  title: Complete computational provenance after the environment repair
  description: The added ENVO:01001002 environment is supported. Fourteen computational
    evidence items still lack queryable model/tool/scenario provenance; recoverable
    model context remains incompletely represented. This residual finding does not
    demand every optional field.
  target_ids:
  - CommunityMech:000013
  field_paths:
  - external_resources[0].evidence[0]
  - external_resources[1].evidence[0]
  - taxonomy[0].evidence
  - taxonomy[1].evidence
  - taxonomy[2].evidence
  - ecological_interactions[0].evidence
  - ecological_interactions[1].evidence
  - ecological_interactions[2].evidence
  - ecological_interactions[3].evidence
  - ecological_interactions[4].evidence
  - ecological_interactions[5].evidence
  evidence_ids:
  - model-methods
  - host-input
  - supplement
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T124426Z-sponge-holobiont-model-record
    finding_id: computational-context
- finding_id: resource-scope
  issue_key: cm-000013-resource-scope
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: 'P3: bounded recoverable provenance/resource gap; graph qualifications
    remain intact.'
  rule_id: review-checklist.claim-scope-and-completeness
  status: open
  certainty: confirmed
  title: Separate publication evidence and reconcile public resource scope
  description: The publication is listed as a dataset while recoverable data/code
    provenance is absent; the reported metabolomics accession has a current scope
    mismatch that must not be imported uncritically.
  target_ids:
  - CommunityMech:000013
  field_paths:
  - associated_datasets[0]
  - associated_datasets
  - external_resources
  evidence_ids:
  - resources
  - source-resources
  - bioproject
  - massive
  - code-tag
  - zenodo
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T124426Z-sponge-holobiont-model-record
    finding_id: resource-scope
- finding_id: history-source-identity
  issue_key: cm-000013-history-source-identity
  category: provenance
  severity: minor
  native_severity: P3
  normalization_reason: 'P3: bounded audit-trail source mismatch; the current environment
    claim itself is supported.'
  rule_id: review-checklist.audit
  status: open
  certainty: confirmed
  title: Correct the environment-history source identity append-only
  description: The new 2026-10-25 history sidecar details cite PMID:39604529, an unrelated
    NLRP3 author correction. The sponge source is PMID:39738126/doi:10.1038/s41467-024-55222-w.
    Inline record notes retain the correct PMID.
  target_ids:
  - CommunityMech:000013
  field_paths:
  - events[0].details in history/records/BioModels_MODEL2407300002_Sponge_Holobiont_Network/2026-10-25T151200Z-antigravity-2072.yaml
  evidence_ids:
  - history
  - pubmed
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: history/records/BioModels_MODEL2407300002_Sponge_Holobiont_Network/2026-10-25T151200Z-antigravity-2072.yaml
    role: append_only_history
actions:
- action_id: repair-eight-member-roster
  description: Represent all eight modeled microbial members.
  finding_ids:
  - eight-member-roster
  target_ids:
  - CommunityMech:000013
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml
    role: canonical_record
  acceptance_checks:
  - Represent all eight source members and their model/MAG identifiers, keeping the
    seven-bacteria/one-archaeon scope and excluding the sponge host. Preserve the
    98.3% MAG-mapped-read denominator.
  - Fresh NCBI metadata verifies Candidatus Spongiicolonus versatilis 2973585, Candidatus
    Spongiihabitans thiooxidans 1671877 and Candidatus Oxydemutator thiolithooxidans
    2973566; Parasynechococcus 2881427 is genus-level. Preserve source-name notes
    and unresolved identities rather than inventing species CURIEs/GTDB mappings;
    reverify candidates during curation.
  - Attach narrow membership and condition-specific role evidence; distinguish merged
    MAG reconstructions from experimental isolates. Revalidate taxonomy, terms and
    GTDB/domain after curation.
- action_id: repair-stable-state
  description: Bound ecological state to the demonstrated evidence.
  finding_ids:
  - stable-state
  target_ids:
  - CommunityMech:000013
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml
    role: canonical_record
  acceptance_checks:
  - Omit the optional ecological_state field if ecological equilibrium cannot be supported,
    or supply an explicit source-grounded scope that does not present simulated stability
    as observed in-vivo persistence.
  - Preserve NATURAL origin and the existing operational node definition; do not replace
    the state automatically with ENGINEERED/TRANSIENT or confuse the 0.5–2 ratio-of-ratios
    criterion with absolute population bounds.
- action_id: repair-computational-context
  description: Record structured model and environmental provenance.
  finding_ids:
  - computational-context
  target_ids:
  - CommunityMech:000013
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml
    role: canonical_record
  acceptance_checks:
  - Add claim-specific computational_provenance for gapseq v1.1 b568a4e reconstruction/manual
    curation/gap-filling and BacArena v1.8.2 pFBA, preserving model identifiers and
    the source scenarios.
  - Separate individual, two-/three-member and eight-member runs. Record the relevant
    input/removal/death/replenishment assumptions; the eight-member model uses 100
    one-hour cycles, 10 mM ammonia, 10% removal and 5% death. Do not generalize those
    settings to every simulation.
  - Retain the now-supported ENVO:01001002 animal-associated environment. Distinguish
    Great Barrier Reef natural sampling and modeled mesohyl in source-grounded notes
    where useful; do not require every optional modeled_environment field. Put simulated
    media in computational provenance, never invented wetlab vessels/temperature/salinity;
    preserve host-input and host-respiration limitations.
- action_id: repair-resource-scope
  description: Separate publication evidence and reconcile public resource scope.
  finding_ids:
  - resource-scope
  target_ids:
  - CommunityMech:000013
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml
    role: canonical_record
  acceptance_checks:
  - Keep the verified BioModels entry and exact combined-input RDS filename, while
    stating listing/metadata verification rather than parsed payload or reproduced
    simulation.
  - Move the paper to bibliographic evidence/resources. Link PRJNA602572 with its
    broad prior-project scope and source-reported focal subset; link STY8 v1.0.0 commit
    17fd9c4eb5bd1f4cdf2c6402a2cdf3958e380546 and Zenodo 10.5281/zenodo.14030749 without
    claiming execution.
  - Record the MSV000083743 source/archive discrepancy and resolve the focal metabolomics
    deposit before adding a verified dataset link. Do not invent a replacement or
    label the upstream unencoded discrepancy as an existing wrong record accession.
- action_id: append-history-source-correction
  description: Append a history correction without rewriting old provenance.
  finding_ids:
  - history-source-identity
  target_ids:
  - CommunityMech:000013
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: history/records/BioModels_MODEL2407300002_Sponge_Holobiont_Network
    role: append_only_history
  acceptance_checks:
  - Append a new native history event referencing the 2026-10-25 sidecar, correcting
    39604529 to 39738126 and focal DOI 10.1038/s41467-024-55222-w; preserve original
    history bytes.
  - State that the animal-associated environment itself is supported, and validate
    the new history entry. Do not invent a fresh canonical-record change merely to
    correct provenance.
limitations:
- Eight merged/representative MAG reconstructions are seven bacteria and one archaeon;
  no host model or cultured eight-strain consortium.98.3 percent denominator is MAG-mapped
  reads.
- Complete scientific main and all six main figure pixels were read, along with scientific
  SI text/TablesS1-S3. Supplementary figure captions were read, but SI figure pixels
  and whole raw SourceData matrices were not independently analyzed. SD2/9/12/13 were
  read; SD5/7/11 inspection is limited to relevant model media/exchange rows and headers.
- Candidate host inputs rely on two samples per group; source/delivery, host respiration
  and reciprocal fitness are unresolved. No model execution, RDS deserialization,
  external code execution, raw sequence/spectra/FISH/flux/statistical reanalysis.
- Current corpus checks exit 1 with44 warnings across 16 of 508 records,0 errors.
  Target native network has0 issues; neither is a whole-corpus scientific approval.
- SD7/11 NO/nitrite compound identifiers disagree and SD7 header placement differs
  from numeric pairs; use narrative/figures for bounded direction without importing
  those IDs. SI model-name variants and the S.thiooxidans abundance statement are
  not silently imported into canonical fields.
- Public archive metadata verifies listings and source pointers, not model reproducibility
  or correct focal metabolomics deposition. MSV000083743 currently resolves to EMP
  soil/fecal data; no replacement accession inferred.
- Fresh NCBI checks verify four candidate taxon records only. Proposed names otherwise
  retain uncertainty; no global absence or species-level GTDB mapping asserted. Historical
  GTDB support counts not recomputed.
- The initial inspection failed on CLAUDE.md symbolic-link resolution; readable canonical
  AGENTS.md was inspected instead. No file/symlink was changed. Initial wrong-owner
  STY8 URLs and aggregate-supplement timeout were retained as failed acquisition receipts;
  corrected public routes succeeded.
- Prior cohort-review context is assessed only for 000013. Their grouped multi-target
  finding dispositions remain untouched; this is an author refresh awaiting independent
  review.
notes:
- Immutable successor; original four stable keys retain exact previous_occurrences.
  No original bundle or canonical/cache/history file rewritten.
- Scratch candidates are JSON; only the native helper writes saved YAML/Markdown.
  Helper scripts were formatted before final inspection and are frozen inputs.
- 'Native input count: 32. Source receipt timestamps denote fresh retrieval; assertions
  reflect the separately stated actual reading scope.'
tags:
- record-review
- sponge
- computational
- batch-07
- staleness-refresh
related_reviews:
- repository: CultureBotAI/CommunityMech
  review_id: 20261021T124426Z-sponge-holobiont-model-record
  relationship: Original single-target observation; all four finding lineages retained.
- repository: CultureBotAI/CommunityMech
  review_id: 20261025T113500Z-c2s4-record-deep-audit
  relationship: Bounded sponge source-context correction only; no grouped supersession
    or other-target disposition.
- repository: CultureBotAI/CommunityMech
  review_id: 20261025T113600Z-c2s4-frozen-cohort-review
  relationship: Bounded sponge source-context correction only; no grouped supersession
    or other-target disposition.
- repository: CultureBotAI/CommunityMech
  review_id: 20261025T161500Z-c2s5-remediation-verification
  relationship: Bounded sponge source-context correction only; no grouped supersession
    or other-target disposition.
```
