# Eight source-scoped records: 22 genus-reference correspondences

- Review: 20261115T090205Z-eight-record-genus-reference-diagnostic
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-15T09:02:03.738836Z
- Finished UTC: 2026-11-15T09:02:05.624143Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

Eight whole records receive 22 declared genus-reference blocks and matching statuses, with 16 actual native inline events and one append-only sidecar per record. Source stock identities or their absence, all unselected taxonomy, biological claims, quotes, experimental distinctions and historical scientific dispositions remain unchanged. Reference-genome correspondence is separate from study-organism identity and scientific support.

## Scope And Provenance

Only the declared GTDB correspondence/status fields and actual application, history and native-check provenance for records 415, 477, 353, 440, 447, 433, 474 and 403. Each target has explicit source, population and preservation assessments. This partial diagnostic does not reassess every scientific claim.

Selection: The eight remaining whole-record units in the independently source-prepared nine-record batch, after record 410 completed its separately saved and verified canary. The reviewed population here is exactly eight records; 410 and other campaign records are excluded.
Coverage: partial; 8 reviewed / 8 in the declared population.
Source: working_tree at Git base e83c687c56beb7160be20a0db2439dab92cfdb67.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000415 | kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml # taxonomy[2:6].taxon_term.gtdb_classification; gtdb_grounding_status | maintained | Four enrichment-community genus descriptors without named stocks |
| CommunityMech:000477 | kb/communities/Cucumber_Low_Phosphorus_Cross_Kingdom_Biocontrol_SynCom.yaml # taxonomy[2:4].taxon_term.gtdb_classification; gtdb_grounding_status | maintained | Two genus summaries within the 19-stock cross-kingdom consortium |
| CommunityMech:000353 | kb/communities/Hualgayoc_Acidic_Sulfate_Reducing_AMD_Consortium.yaml # taxonomy[0:2].taxon_term.gtdb_classification; gtdb_grounding_status | maintained | MAG003 and MAG013 genus-reference correspondences |
| CommunityMech:000440 | kb/communities/Electrostimulated_Toluene_Methanogenic_Microbiota.yaml # taxonomy[1:3].taxon_term.gtdb_classification; gtdb_grounding_status | maintained | Alternative acetoclastic partner genus correspondences |
| CommunityMech:000447 | kb/communities/Brocadia_Low_Nitrogen_Anammox_Consortium.yaml # taxonomy[0:2].taxon_term.gtdb_classification; gtdb_grounding_status | maintained | Temporal Brocadia and Kuenenia assemblage descriptors |
| CommunityMech:000433 | kb/communities/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium.yaml # taxonomy[0:3].taxon_term.gtdb_classification; gtdb_grounding_status | maintained | Three genus-level MAG descriptors in a wastewater enrichment |
| CommunityMech:000474 | kb/communities/Whale_Fall_Vallitalea_Trichloromonas_Chitin_EET_Consortium.yaml # taxonomy[0:2].taxon_term.gtdb_classification; gtdb_grounding_status | maintained | Vallitalea and Trichloromonas genus correspondence with stock omissions retained |
| CommunityMech:000403 | kb/communities/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom.yaml # taxonomy[0:5].taxon_term.gtdb_classification; gtdb_grounding_status | maintained | Five distinct SynLAV stocks with genus-reference correspondence |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000415 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-strict | passed | True | CommunityMech:000415 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb | passed | True | CommunityMech:000415 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb-domain | passed | True | CommunityMech:000415 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-scalars | passed | True | CommunityMech:000415 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-history | passed | True | CommunityMech:000415 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| new-history | passed | True | CommunityMech:000415 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-terms | passed | True | CommunityMech:000415 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate | passed | True | CommunityMech:000477 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-strict | passed | True | CommunityMech:000477 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb | passed | True | CommunityMech:000477 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb-domain | passed | True | CommunityMech:000477 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-scalars | passed | True | CommunityMech:000477 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-history | passed | True | CommunityMech:000477 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| new-history | passed | True | CommunityMech:000477 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-terms | passed | True | CommunityMech:000477 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate | passed | True | CommunityMech:000353 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-strict | passed | True | CommunityMech:000353 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb | passed | True | CommunityMech:000353 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb-domain | passed | True | CommunityMech:000353 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-scalars | passed | True | CommunityMech:000353 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-history | passed | True | CommunityMech:000353 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| new-history | passed | True | CommunityMech:000353 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-terms | passed | True | CommunityMech:000353 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate | passed | True | CommunityMech:000440 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-strict | passed | True | CommunityMech:000440 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb | passed | True | CommunityMech:000440 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb-domain | passed | True | CommunityMech:000440 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-scalars | passed | True | CommunityMech:000440 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-history | passed | True | CommunityMech:000440 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| new-history | passed | True | CommunityMech:000440 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-terms | passed | True | CommunityMech:000440 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate | passed | True | CommunityMech:000447 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-strict | passed | True | CommunityMech:000447 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb | passed | True | CommunityMech:000447 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb-domain | passed | True | CommunityMech:000447 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-scalars | passed | True | CommunityMech:000447 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-history | passed | True | CommunityMech:000447 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| new-history | passed | True | CommunityMech:000447 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-terms | passed | True | CommunityMech:000447 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate | passed | True | CommunityMech:000433 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-strict | passed | True | CommunityMech:000433 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb | passed | True | CommunityMech:000433 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb-domain | passed | True | CommunityMech:000433 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-scalars | passed | True | CommunityMech:000433 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-history | passed | True | CommunityMech:000433 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| new-history | passed | True | CommunityMech:000433 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-terms | passed | True | CommunityMech:000433 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate | passed | True | CommunityMech:000474 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-strict | passed | True | CommunityMech:000474 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb | passed | True | CommunityMech:000474 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb-domain | passed | True | CommunityMech:000474 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-scalars | passed | True | CommunityMech:000474 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-history | passed | True | CommunityMech:000474 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| new-history | passed | True | CommunityMech:000474 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-terms | passed | True | CommunityMech:000474 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate | passed | True | CommunityMech:000403 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-strict | passed | True | CommunityMech:000403 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb | passed | True | CommunityMech:000403 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb-domain | passed | True | CommunityMech:000403 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-scalars | passed | True | CommunityMech:000403 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-history | passed | True | CommunityMech:000403 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| new-history | passed | True | CommunityMech:000403 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-terms | passed | True | CommunityMech:000403 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |

## Scientific And Domain Assessments

### Enrichment descriptors are not named experimental isolates

grounding: supported. Targets: CommunityMech:000415.

All six source descriptors and both eukaryotic exclusions remain intact. The four selected bacterial genera retain absent stock/species identity; no genome or strain is inferred.

### Narrow majority and small reference populations

grounding: supported. Targets: CommunityMech:000415.

The 13/24 Leptolyngbya majority across six reference genera is explicitly limited, not unanimous. Counts of 8/8, 45/45 and 1/1 do not measure community abundance or verify study genomes. The source's 50:40 methylotroph composition remains distinct from the 50:50 culture inoculum.

### Bounded actual correction preserves historical science

provenance: supported. Targets: CommunityMech:000415.

Only the approved mapping/status fields and native provenance changed. Main-assay 6% versus enrichment 3% salt, metagenomic potential, carbon-balance limits, quotes and the stage5 chain remain unchanged.

### Stock roster versus genus descriptors

grounding: supported. Targets: CommunityMech:000477.

The 19-stock roster is not collapsed into six organisms. The two selected genus descriptors retain their absent formal stock fields and source-specific multiple-stock scope.

### Reference genus correspondence without stock-genome inference

grounding: supported. Targets: CommunityMech:000477.

The complete native 79/79 and 199/199 reference results do not establish any experimental stock's species, assembly, abundance or ecological contribution.

### Preserved cross-kingdom scientific context

provenance: supported. Targets: CommunityMech:000477.

The guarded mapping change preserves every biological statement, current graph, source quote and old history event. Existing fungal exclusions and the Amesia limitation remain separate from bacterial correspondence.

### MAG affiliation remains genus-scoped

grounding: supported. Targets: CommunityMech:000353.

MAG003 and MAG013 remain distinct source entities in an enrichment, not two cultured isolates. The paper's MAG013 ANI and GTDB-Tk provenance do not become an exact assembly assignment through this mapping.

### Two genus populations with different denominators

grounding: supported. Targets: CommunityMech:000353.

Desulfosporosinus 32/32 and Acididesulfobacillus 3/3 support only their declared reference correspondences. The small three-genome denominator is retained explicitly.

### Source and historical carbon-flow limits preserved

provenance: supported. Targets: CommunityMech:000353.

Reinoculation days 32 and 86, pH conditions, PARTIAL carbon flux and unresolved transfer mechanisms remain unchanged. Native correspondence and gate success do not replace the historical scientific assessment.

### Alternative partners remain alternatives

grounding: supported. Targets: CommunityMech:000440.

Both descriptors retain genus-only identity and absent formal stocks. A database correspondence does not resolve the source's Methanosarcina-or-Methanothrix or e-pili-or-acetate alternatives.

### Reference majority is not ecological mechanism

grounding: supported. Targets: CommunityMech:000440.

The 301/301 and 94/117 populations are reproduced with the native genus route. Neither establishes experimental partner identity, a MAG assembly match or electron transfer.

### Abstract-only scope and original mechanisms preserved

provenance: supported. Targets: CommunityMech:000440.

Actual application and native provenance are bound without a full-text electrode or assembly audit. No operating condition, graph direction, source quote or historical limitation was rewritten.

### Temporal genus assemblages remain unresolved below genus

grounding: supported. Targets: CommunityMech:000447.

The source's multiple Brocadia species and earlier Kuenenia assemblage are preserved. No formal stock, particular species or experimental assembly is assigned.

### Reference denominators versus biological measurements

grounding: supported. Targets: CommunityMech:000447.

The 39/39 and 4/4 reference counts are separate from 44.7% source abundance, 71.5% transcriptional contribution and 68% positive associations. The small Kuenenia denominator is not experimental replication.

### Computational and historical boundaries remain intact

provenance: supported. Targets: CommunityMech:000447.

The guarded correction preserves the stage5 chain, all previous scientific text and the lack of measured exchange. Abstract-only source access is explicit; actual native gate success is a separate technical result.

### MAG genus affiliations do not identify species or virulence

grounding: supported. Targets: CommunityMech:000433.

Genus authority, absent formal stocks and source MAG notes remain unchanged. Reference relationships and secretion genes do not establish a species or demonstrate pathogenicity.

### Reference populations are separate from inoculum composition

grounding: supported. Targets: CommunityMech:000433.

Counts of 16/16, 17/17 and 5067/5375 are native genus correspondences, not the 64-MAG input denominator or source abundances of 45.96% and 9.73%. Legionella is explicitly non-unanimous.

### Historical scientific predicates survive bounded correction

provenance: supported. Targets: CommunityMech:000433.

Anoxic ammonia accumulation, delayed aerobic removal, aliases and culture/redox limits remain intact. The actual native application and appended provenance do not certify all scientific claims.

### Source isolates and unresolved canonical stock fields

grounding: supported. Targets: CommunityMech:000474.

Genus correspondence is compatible with source isolates sp2 and sp17 while leaving the exact formal-stock omission explicitly unresolved under issue 2872. No species or assembly assignment is introduced.

### Non-unanimous Vallitalea reference population

grounding: supported. Targets: CommunityMech:000474.

The native 14/16 and 8/8 populations are reference evidence, not experimental stock genomes or measured exchange. The two-genus Vallitalea split remains visible.

### Bounded mapping preserves separate assay and mechanism limits

provenance: supported. Targets: CommunityMech:000474.

The actual transition preserves source quotes, topology, old history and acetate/current/substrate distinctions. Strict batch133 admission must remain disjoint from other completed targets, and no scientific issue is closed.

### Five source-local stocks retain genus-only scope

grounding: supported. Targets: CommunityMech:000403.

L11, L29, L75, L44 and L115 remain distinct SynLAV stocks. Rhodococcus and Gordonia authority-label qualifiers remain unchanged. No stock is assigned a species, exact assembly or source-phylum error.

### Five different reference denominators and non-unanimous majorities

grounding: supported. Targets: CommunityMech:000403.

The complete native populations of 859/860, 17956/25706, 449/610, 514/514 and 450/453 remain explicit. The separate L115 exact-ID row is not promoted to a stock-specific species match; reference majorities do not establish experimental phenotype or persistence.

### Prior full science and separate supplement remain immutable

provenance: supported. Targets: CommunityMech:000403.

The 72-hour individual 100 mg/L screen stays separate from 100 mg/kg pots, equal optical density from viable counts, and three LAV-ASVs from persistence of every stock. The ten-day Methods versus two-week Results discrepancy, source-attributed phylum quotes, prior review and historical cache provenance remain unchanged.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| 000415-schema | .temp/gtdb-code006-20261115/genus-nine-415-run-schema-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000415-strict | .temp/gtdb-code006-20261115/genus-nine-415-run-strict-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000415-gtdb | .temp/gtdb-code006-20261115/genus-nine-415-run-gtdb-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000415-domain | .temp/gtdb-code006-20261115/genus-nine-415-run-domain-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000415-scalars | .temp/gtdb-code006-20261115/genus-nine-415-run-scalars-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000415-history | .temp/gtdb-code006-20261115/genus-nine-415-run-history-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000415-new-history | .temp/gtdb-code006-20261115/genus-nine-415-run-new-history-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000415-terms | .temp/gtdb-code006-20261115/genus-nine-415-run-terms-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000415-paper | https://pubmed.ncbi.nlm.nih.gov/41745484/; Retained community characterization and Methods 3.1-3.2/3.4; exact bound primary_contexts | supports | The selected bacterial genera describe enrichment fractions without formal stock identities. The methylotroph composition and culture inoculum are distinct quantities. |
| 000415-database | reports/gtdb-code006-20261115/genus-nine-415-source-evidence-001.json; occurrences[taxonomy_index=2,3,4,5], full native_result and authority rows | supports | Leptolyngbya 13/24, Methylotuvimicrobium 8/8, Methylophaga 45/45 and Methylonatrum 1/1 are reference-genus populations. The first is a narrow majority, and the last rests on one reference genome. |
| 000415-application | .temp/gtdb-code006-20261115/genus-nine-415-applied-m5-001/receipt.json; Actual accepted before/after and complete source input binding | supports | The guarded transition adds only four declared blocks/statuses and two native inline events, preserving six descriptors, two eukaryotic exclusions and all biology. |
| 000415-prior | reports/causal_graph_review/decisions/20261021-stage5-review-remediation.yaml; CommunityMech:000415, original 3e009885 to d3174165 chain; original batch4 remains unchanged | context_only | The historical source and biological limitations remain in force, including functional potential versus measured expression/exchange and the absence of a closed carbon balance. |
| 000477-schema | .temp/gtdb-code006-20261115/genus-nine-477-run-schema-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000477-strict | .temp/gtdb-code006-20261115/genus-nine-477-run-strict-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000477-gtdb | .temp/gtdb-code006-20261115/genus-nine-477-run-gtdb-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000477-domain | .temp/gtdb-code006-20261115/genus-nine-477-run-domain-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000477-scalars | .temp/gtdb-code006-20261115/genus-nine-477-run-scalars-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000477-history | .temp/gtdb-code006-20261115/genus-nine-477-run-history-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000477-new-history | .temp/gtdb-code006-20261115/genus-nine-477-run-new-history-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000477-terms | .temp/gtdb-code006-20261115/genus-nine-477-run-terms-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000477-paper | https://pubmed.ncbi.nlm.nih.gov/41882811/; Bound retained main-text consortium roster and stock contexts | supports | The 19 experimental stocks comprise 13 bacteria and six fungi, summarized by six taxonomy descriptors. Sphingopyxis represents two stocks and Cupriavidus three; neither descriptor is one newly identified stock. |
| 000477-database | reports/gtdb-code006-20261115/genus-nine-477-source-evidence-001.json; occurrences[taxonomy_index=2,3] | supports | Sphingopyxis 79/79 and Cupriavidus 199/199 support genus-reference correspondence only, not identity of the multiple experimental stocks summarized by each descriptor. |
| 000477-application | .temp/gtdb-code006-20261115/genus-nine-477-applied-m5-001/receipt.json; Actual accepted before/after and source bindings | supports | Two declared blocks/statuses and two native events changed. Other status-key ordering is semantically unchanged; the existing Bacillus/Devosia blocks, fungal exclusions and Amesia note remain intact. |
| 000477-prior | reports/causal_graph_review/decisions/20261020-stage2-fifteen-records-batch133.yaml; CommunityMech:000477 and immutable scientific decisions | context_only | The historical experimental and graph boundaries remain unchanged. Later strict admission must compose with other independently accepted batch133 targets without replacing their proofs. |
| 000353-schema | .temp/gtdb-code006-20261115/genus-nine-353-run-schema-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000353-strict | .temp/gtdb-code006-20261115/genus-nine-353-run-strict-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000353-gtdb | .temp/gtdb-code006-20261115/genus-nine-353-run-gtdb-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000353-domain | .temp/gtdb-code006-20261115/genus-nine-353-run-domain-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000353-scalars | .temp/gtdb-code006-20261115/genus-nine-353-run-scalars-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000353-history | .temp/gtdb-code006-20261115/genus-nine-353-run-history-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000353-new-history | .temp/gtdb-code006-20261115/genus-nine-353-run-new-history-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000353-terms | .temp/gtdb-code006-20261115/genus-nine-353-run-terms-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000353-paper | https://pubmed.ncbi.nlm.nih.gov/42029028/; Bound main-text day-160 enrichment, MAG affiliation and metabolic-potential passages | supports | MAG003 and MAG013 retain their Desulfosporosinus and Acididesulfobacillus genus affiliations. The source's 96% ANI result for MAG013 is separate from this crosswalk correspondence. |
| 000353-database | reports/gtdb-code006-20261115/genus-nine-353-source-evidence-001.json; occurrences[taxonomy_index=0,1] | supports | The native genus populations are 32/32 and 3/3. They do not identify an experimental MAG assembly or add a species assignment. |
| 000353-application | .temp/gtdb-code006-20261115/genus-nine-353-applied-m5-001/receipt.json; Actual two-block/status and two-event transition | supports | The accepted application preserves all MAG identifiers, evidence, cultivation conditions and biological claims outside the declared GTDB fields. |
| 000353-prior | reports/causal_graph_review/decisions/20261006-urls-amd-proteome-batch52.yaml; CommunityMech:000353 historical needs_research and exact predecessor | context_only | The historical carbon-flow limitations remain unresolved, including both MAGs' glycerol-to-acetate potential, residual acetate and minor acidogens. |
| 000440-schema | .temp/gtdb-code006-20261115/genus-nine-440-run-schema-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000440-strict | .temp/gtdb-code006-20261115/genus-nine-440-run-strict-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000440-gtdb | .temp/gtdb-code006-20261115/genus-nine-440-run-gtdb-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000440-domain | .temp/gtdb-code006-20261115/genus-nine-440-run-domain-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000440-scalars | .temp/gtdb-code006-20261115/genus-nine-440-run-scalars-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000440-history | .temp/gtdb-code006-20261115/genus-nine-440-run-history-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000440-new-history | .temp/gtdb-code006-20261115/genus-nine-440-run-new-history-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000440-terms | .temp/gtdb-code006-20261115/genus-nine-440-run-terms-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000440-paper | https://pubmed.ncbi.nlm.nih.gov/38865893/; Retained abstract, non-electrostimulated microbiota syntrophy sentence; exact literal newline preserved | supports | Methanosarcina or Methanothrix are alternative proposed acetoclastic partners, with e-pili or acetate mechanisms. The abstract does not establish both as confirmed exchanging stocks. |
| 000440-database | reports/gtdb-code006-20261115/genus-nine-440-source-evidence-001.json; occurrences[taxonomy_index=1,2] | supports | Methanosarcina 301/301 and Methanothrix 94/117 are genus-reference results. The latter population spans three GTDB genera and is not unanimous. |
| 000440-application | .temp/gtdb-code006-20261115/genus-nine-440-applied-m5-001/receipt.json; Actual accepted transition and source inputs | supports | Two declared blocks/statuses and two native events changed; all six entries and unselected Bacteria-domain, Methanobacterium and unresolved Desulfoprunum states remain intact. |
| 000440-prior | reports/causal_graph_review/decisions/20261006-three-records-batch37.yaml; CommunityMech:000440; old scientific and direction constraints | context_only | The HYPOTHESIZED graph, 800 mV versus control distinction, anode/cathode MAG labels and missing operating conditions remain unchanged. The separate 455 successor is not affected. |
| 000447-schema | .temp/gtdb-code006-20261115/genus-nine-447-run-schema-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000447-strict | .temp/gtdb-code006-20261115/genus-nine-447-run-strict-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000447-gtdb | .temp/gtdb-code006-20261115/genus-nine-447-run-gtdb-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000447-domain | .temp/gtdb-code006-20261115/genus-nine-447-run-domain-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000447-scalars | .temp/gtdb-code006-20261115/genus-nine-447-run-scalars-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000447-history | .temp/gtdb-code006-20261115/genus-nine-447-run-history-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000447-new-history | .temp/gtdb-code006-20261115/genus-nine-447-run-new-history-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000447-terms | .temp/gtdb-code006-20261115/genus-nine-447-run-terms-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000447-paper | https://pubmed.ncbi.nlm.nih.gov/42323145/; Retained primary abstract: temporal succession, multispecies Brocadia assemblage and model findings | supports | Earlier Kuenenia acclimation and later multispecies Brocadia dominance are temporal observations, not a defined two-isolate SynCom. |
| 000447-database | reports/gtdb-code006-20261115/genus-nine-447-source-evidence-001.json; occurrences[taxonomy_index=0,1] | supports | Brocadia 39/39 and Kuenenia 4/4 are reference-genus populations. Candidatus source names and absent stock fields remain unchanged. |
| 000447-application | .temp/gtdb-code006-20261115/genus-nine-447-applied-m5-001/receipt.json; Actual accepted two-block/status and two-event transition | supports | The application preserves temporal culture context, all source evidence and the computational interaction outside declared GTDB fields. |
| 000447-prior | reports/causal_graph_review/decisions/20261021-stage5-review-remediation.yaml; CommunityMech:000447, 227362963f to 0ea86ed4 chain and immutable original batch8 disposition | context_only | SMETANA auxotrophy and low/high-nitrogen model comparisons remain computational, without measured interspecies flux or newly certified assembly identities. |
| 000433-schema | .temp/gtdb-code006-20261115/genus-nine-433-run-schema-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000433-strict | .temp/gtdb-code006-20261115/genus-nine-433-run-strict-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000433-gtdb | .temp/gtdb-code006-20261115/genus-nine-433-run-gtdb-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000433-domain | .temp/gtdb-code006-20261115/genus-nine-433-run-domain-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000433-scalars | .temp/gtdb-code006-20261115/genus-nine-433-run-scalars-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000433-history | .temp/gtdb-code006-20261115/genus-nine-433-run-history-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000433-new-history | .temp/gtdb-code006-20261115/genus-nine-433-run-new-history-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000433-terms | .temp/gtdb-code006-20261115/genus-nine-433-run-terms-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000433-paper | https://pubmed.ncbi.nlm.nih.gov/41457319/; Bound inoculum MAG Results and Legionella phylogenetic/gene-content passages | supports | Nitrosospira, Nitrobacter and Legionella are genus-level MAG descriptors within starting material yielding 64 MAGs, not a three-strain inoculum. |
| 000433-database | reports/gtdb-code006-20261115/genus-nine-433-source-evidence-001.json; occurrences[taxonomy_index=0,1,2] | supports | Native genus populations are 16/16, 17/17 and 5067/5375. Legionella spans seven reference genera; no particular study MAG or pathogenicity is assigned. |
| 000433-application | .temp/gtdb-code006-20261115/genus-nine-433-applied-m5-001/receipt.json; Actual accepted three-block/status and two-event transition | supports | The accepted application preserves all MAG notes, culture conditions, evidence, biological graph and prior history outside declared GTDB fields. |
| 000433-prior | reports/causal_graph_review/decisions/20261007-four-records-batch78.yaml; CommunityMech:000433 scientific disposition and historical exact-hash/event facts | context_only | The historical needs_research status, PARTIAL guild handoff, aerobic/anoxic differences and gene-expression limits remain unchanged. The separate 176 c2s5 chain is preserved. |
| 000474-schema | .temp/gtdb-code006-20261115/genus-nine-474-run-schema-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000474-strict | .temp/gtdb-code006-20261115/genus-nine-474-run-strict-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000474-gtdb | .temp/gtdb-code006-20261115/genus-nine-474-run-gtdb-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000474-domain | .temp/gtdb-code006-20261115/genus-nine-474-run-domain-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000474-scalars | .temp/gtdb-code006-20261115/genus-nine-474-run-scalars-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000474-history | .temp/gtdb-code006-20261115/genus-nine-474-run-history-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000474-new-history | .temp/gtdb-code006-20261115/genus-nine-474-run-new-history-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000474-terms | .temp/gtdb-code006-20261115/genus-nine-474-run-terms-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000474-paper | https://pubmed.ncbi.nlm.nih.gov/42297039/; Bound isolation, partial-16S, reconstructed coculture and cultured-isolate passages | supports | The source names Vallitalea sp2 and Trichloromonas sp17, distinct from the sediment enrichment. Their omitted canonical formal stock fields remain a separate finding under issue 2872. |
| 000474-database | reports/gtdb-code006-20261115/genus-nine-474-source-evidence-001.json; occurrences[taxonomy_index=0,1] | supports | Vallitalea 14/16 across two reference genera and Trichloromonas 8/8 support genus correspondence only; partial 16S does not identify exact assemblies. |
| 000474-application | .temp/gtdb-code006-20261115/genus-nine-474-applied-m5-001/receipt.json; Actual accepted two-block/status and two-event transition | supports | The guarded correction preserves both null stock fields and every scientific claim outside the declared mapping fields. It does not silently repair or retire the separate stock finding. |
| 000474-prior | reports/causal_graph_review/decisions/20261020-stage2-fifteen-records-batch133.yaml; CommunityMech:000474 original decisions and current graph/source boundaries | context_only | Sediment enrichment, isolate coculture and separate current/substrate assays remain distinct. Initial acetate amendment is not evidence of chitin-derived transfer or completed reciprocal mechanism. |
| 000403-schema | .temp/gtdb-code006-20261115/genus-nine-403-run-schema-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000403-strict | .temp/gtdb-code006-20261115/genus-nine-403-run-strict-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000403-gtdb | .temp/gtdb-code006-20261115/genus-nine-403-run-gtdb-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000403-domain | .temp/gtdb-code006-20261115/genus-nine-403-run-domain-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000403-scalars | .temp/gtdb-code006-20261115/genus-nine-403-run-scalars-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000403-history | .temp/gtdb-code006-20261115/genus-nine-403-run-history-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000403-new-history | .temp/gtdb-code006-20261115/genus-nine-403-run-new-history-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000403-terms | .temp/gtdb-code006-20261115/genus-nine-403-run-terms-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000403-paper | https://pubmed.ncbi.nlm.nih.gov/42482240/; Selected main-text screen, inoculum, pot and targeted-ASV passages plus separately retained Table S2 stock rows | supports | Table S2 separately identifies L11, L29, L75, L44 and L115. Source phylum errors remain attributed quotations rather than authority labels; supplement text is not merged into the article cache. |
| 000403-database | reports/gtdb-code006-20261115/genus-nine-403-source-evidence-001.json; occurrences[taxonomy_index=0,1,2,3,4], full native result and exact current authority labels | supports | Flavobacterium 859/860, Pseudomonas 17956/25706, Sphingomonas 449/610, Rhodococcus 514/514 and Gordonia 450/453 support genus-reference correspondence for five distinct source stocks, without exact species or assembly assignment. |
| 000403-application | .temp/gtdb-code006-20261115/genus-nine-403-applied-m5-001/receipt.json; Actual accepted five-block/status and two-event transition | supports | The guarded application preserves all stock names, exact current authority labels, source evidence, biological conditions and old history outside the declared GTDB fields. |
| 000403-prior | reviews/structured/20261021T192924Z-choysum-synlav-record/review.yaml; Immutable prior full scientific review 8bc00677 and original batch15 chain | context_only | Issues 2535, 1311, 2534 and 1996 remain separate. The prior review's source-routing, timing, persistence and biological limitations are not retired by a genus correspondence diagnostic. |

## Limits And Additional Notes

- Partial technical diagnostic with scientific_review:false. Completion of these declared checks is not whole-record scientific approval, source-snippet validation, generated-site integration, final corpus QC or campaign completion.
- Every support/total count concerns the named-binomial reference population in crosswalk 761d5537, not the study's stocks, assemblies, experimental replicates or community abundance. Existing taxon labels, strain fields, source notes and scientific uncertainty remain unchanged.
- Leptolyngbya 13/24 is a narrow majority spanning six reference genera. Methanothrix 94/117, Legionella 5067/5375, Vallitalea 14/16 and the non-unanimous Choysum populations remain explicitly qualified; no majority vote resolves exact stock identity or mechanism.
- Primary coverage is limited to the source contexts and locators recorded for each target. Records 440 and 447 use retained abstracts; the other records use selected retained main-text passages, with Choysum Table S2 kept as a separate supplement. No new complete-paper, image, sequence or assembly review was performed.
- The whale-fall sp2/sp17 formal stock omissions remain separately owned by issue 2872. Choysum's prior full review and issues 2535, 1311, 2534 and 1996 remain unchanged. No historical scientific finding or GitHub issue is closed by this diagnostic.
- Native reporting ran locally at 0e826fcf, source binding at 4c0046c6, and staging and actual M5 application/checks at e83c687c56beb7160be20a0db2439dab92cfdb67. The M5 native gate receipts record Python 3.13.2. Post-application checks are not a clean-tree run. Crosswalk file mtime is not a release identifier; the local NCBI authority observation is stat-bound rather than a full database checksum.
- Source-binding attempt 001 refused a literal newline mismatch in record 440 under issue 2878. Its failed evidence is preserved separately. Corrected attempt 002 passed a fresh 410 source-binding canary followed by the full source-only binding before candidate staging.
- Native term validation is reported literally; its output does not establish an assertion denominator. Strict successor admission, historical caller composition and final integrated QC remain separate downstream checks. A complete immutable input checkpoint is required before any historical caller adaptation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261115T090205Z-eight-record-genus-reference-diagnostic
kind: batch
repository: CultureBotAI/CommunityMech
title: 'Eight source-scoped records: 22 genus-reference correspondences'
started_at: '2026-11-15T09:02:03.738836Z'
finished_at: '2026-11-15T09:02:05.624143Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Parent independently read the primary-source contexts, complete
    source configurations and all eight candidate diffs with exact external hashes
    before application. The shared reporter, binder, guarded engine, check runner
    and diagnostic builder were independently reviewed. The same application and persistence
    path was verified end to end on record 410 before these eight units. This remains
    self-review of a bounded technical correction.
skill: curate-yaml-record
completion: completed
verdict: pass_with_limitations
scientific_review: false
summary: Eight whole records receive 22 declared genus-reference blocks and matching
  statuses, with 16 actual native inline events and one append-only sidecar per record.
  Source stock identities or their absence, all unselected taxonomy, biological claims,
  quotes, experimental distinctions and historical scientific dispositions remain
  unchanged. Reference-genome correspondence is separate from study-organism identity
  and scientific support.
source:
  git_revision: e83c687c56beb7160be20a0db2439dab92cfdb67
  state: working_tree
  inputs:
  - path: .temp/gtdb-code006-20261115/genus-nine-353-applied-m5-001/before.yaml
    sha256: 123c3e9e5a107b28346350c70a739cda2a27079917779f2d91d4797157c5f5af
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-353-applied-m5-001/receipt.json
    sha256: 6ecc66f1ee3da3fbe06192cd25666c162b9a23c16c0b0d47933473f2c7024fbb
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-353-candidate-001/Hualgayoc_Acidic_Sulfate_Reducing_AMD_Consortium.yaml
    sha256: 99115a41c2c32e4ead8941e8cce89838944047e7f17221295bd73bfab63c8c13
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-353-candidate-001/receipt.json
    sha256: deb6159fdc8318c432c76fcbe3a9f060816e11457d108f7081c31a7ff3bdc6db
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-353-check-config-001.json
    sha256: 81292969144127f7ffab4771e985696cefea40096824107759a416d8033a6bb7
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-353-run-domain-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-353-run-domain-001/native.log
    sha256: 5ea2ca40540bcd054bd3e4b7b20a62b51e0334761a1552fc16587e3856e97964
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-353-run-domain-001/receipt.json
    sha256: 77688a0c5c2dec373223e4c6f001fe01f20cccc7721631f4e5cff9a5be405b1b
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-353-run-domain-001/start.json
    sha256: 793536083e4cac17520906a09adc8b32b5480a52997c0a4468592f02573358ce
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-353-run-gtdb-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-353-run-gtdb-001/native.log
    sha256: 669de58e9a8b8d4d06a12696536169910459ae0691fdac604462ef9361652f4c
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-353-run-gtdb-001/receipt.json
    sha256: 1f068160521c84f4f7b2ef224b2c65af22e5cdb3af4a6029703b8a3c7e3a9c86
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-353-run-gtdb-001/start.json
    sha256: b01b81cfb136672cd4f26c5fccd886285bcf059eb56b3acd0b8478bb64a2fb6c
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-353-run-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-353-run-history-001/native.log
    sha256: 700b44227c4cf01270ac26f16b308622de0b26f48d71aec49cdfaaab87620f0a
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-353-run-history-001/receipt.json
    sha256: dc53f3426b2a66f95074a9a3f8db56dbee5fad7951caf3dfc7eedb81f44c34cd
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-353-run-history-001/start.json
    sha256: 0d28560152cc8f031d549729182f329aff7cd809a098e1b01c3a272b16a77746
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-353-run-new-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-353-run-new-history-001/native.log
    sha256: 435afd1bfb13334d1faed3c77cd3a9d72ee05d2f7e854ef299ffa6b5d738585a
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-353-run-new-history-001/receipt.json
    sha256: b51e0b548e74a79d2f4f993b26cb42aadd6d8051d866166b330f888395e1dc78
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-353-run-new-history-001/start.json
    sha256: d9b4fc98da2e005ce16425e8469083f047540b9ac515736128744498b1a13764
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-353-run-scalars-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-353-run-scalars-001/native.log
    sha256: 6b060a610cf37a01fbae5e030aff862b8b061121d81bc6b3681ffe6db5b49682
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-353-run-scalars-001/receipt.json
    sha256: 2691e1e275a617f409f87131ddca70c1dc8b63a019b673bf33c30100b2f299e9
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-353-run-scalars-001/start.json
    sha256: 75fe4872c89574e3a0ada5d5569579bb94b83d68d3416a391c6fc516b25ce64d
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-353-run-schema-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-353-run-schema-001/native.log
    sha256: 42ed18d0a9219187dd8dd04064d04e38a2bb60418af30332a3140691e245125a
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-353-run-schema-001/receipt.json
    sha256: f5ef13da3483c7961ae2b9be8b319a79657ec6136863ca0c5947f60918287275
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-353-run-schema-001/start.json
    sha256: 0773686465ab5bf773567b67a586dc2618dc887aa4784eafcc13158b9585d94d
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-353-run-strict-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-353-run-strict-001/native.log
    sha256: 336b52dd1cd4b8bd64df1efca41f70f0f8d0a02cda6be606042494dfa1785489
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-353-run-strict-001/receipt.json
    sha256: 89b12fc219751ceec24219277fc9e58eba6db227804cb5ea8314eebf33675aaf
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-353-run-strict-001/start.json
    sha256: fe01c34c64eb17903a57c5d2970cc60d74ef3257ac5a8c10e7509e491924c44f
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-353-run-strict-001/strict.tsv
    sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-353-run-terms-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-353-run-terms-001/native.log
    sha256: f899f18f30f08fe51d6b967838dcd53c2962a06c93f929a0172e69d6e4b8ee5e
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-353-run-terms-001/receipt.json
    sha256: ab6ae896b78ef1d891eb8ccabae2c443cd504c1aae6b699e42fefb51216f7175
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-353-run-terms-001/start.json
    sha256: c66c288c368ad7e2a3e32950df937932b27daff856efc53c88bd464a5db224ed
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-403-applied-m5-001/before.yaml
    sha256: 23c898adcb069d4f4f36cc49783674e02fa33a814b11cdc8a3a7ed7f84f74239
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-403-applied-m5-001/receipt.json
    sha256: 5a10c1f293997c2949aac60ccef13a904b21a281cf4558fd61d05a712ac2cfe6
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-403-candidate-001/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom.yaml
    sha256: 57f34a82b45bc938d82175cd25bda54f53f981fc49f1a24b6d30f67094ac82a3
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-403-candidate-001/receipt.json
    sha256: 9b51ec71b6fd74385220b0489d170e90e88af5a39c3d222d81970228abaa7d8c
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-403-check-config-001.json
    sha256: b051d7b7c987ee8a66b6887170f74d2cb110da81159a98eba74db3cedc0343ec
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-403-run-domain-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-403-run-domain-001/native.log
    sha256: 6200c347f5a9d2cd7840f5bf64bc9e6ba63f397d8fa654bfd6a823ad47ca392c
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-403-run-domain-001/receipt.json
    sha256: 862027bae3734dd5907980418056a07521967c672fc1613d3905c0f69485407c
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-403-run-domain-001/start.json
    sha256: 319a7dc3128ab674ca8c643bb4b45cf81b0f34e42731ea15ac6222a46adc385a
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-403-run-gtdb-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-403-run-gtdb-001/native.log
    sha256: 103c498467fc95a8e3e92b3ca13d1cb0f4473c9e68e3b6ec86e95c3029a4340a
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-403-run-gtdb-001/receipt.json
    sha256: 09399fbaaff56960c68e489429c117267001573e8e025a56ba73d153070a2225
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-403-run-gtdb-001/start.json
    sha256: b7c1f957c22ec7f9bebaed7196c75e2f73fd4701d539ef7b8d09c6195078ee87
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-403-run-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-403-run-history-001/native.log
    sha256: 700b44227c4cf01270ac26f16b308622de0b26f48d71aec49cdfaaab87620f0a
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-403-run-history-001/receipt.json
    sha256: 72b4832865b4ef320654c61068459f6d4874c1388a62fb0411ef6a01c21d52e4
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-403-run-history-001/start.json
    sha256: 5b51c5050f1d0419ca4b241eade22477f5d2f6c283c765905dcdcd31fb602794
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-403-run-new-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-403-run-new-history-001/native.log
    sha256: 7eedb813467412238d47da8763f0137181358b43ebe3a176e9e2675be9ef5ea0
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-403-run-new-history-001/receipt.json
    sha256: 93728f6cde03d7f6682c024ca7afb388977cb2a624d67e555948600d2965009f
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-403-run-new-history-001/start.json
    sha256: 432a1e5a0f4219325b325abfc8ff0ca19e7d74b1241cc6f0d4d4b1c989bd41e0
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-403-run-scalars-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-403-run-scalars-001/native.log
    sha256: 299f47fa82fae071e37a7362d9221c8ff340e4835e935b1e4160cb200d812b66
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-403-run-scalars-001/receipt.json
    sha256: 8e858ea305f48b67da46bcb4024fb4098617ef9ea7c384618d1298542d13c539
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-403-run-scalars-001/start.json
    sha256: cacc82cca6888bc604203b896bc930c4165ad1f178aedd002c24d9eb15ebc35e
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-403-run-schema-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-403-run-schema-001/native.log
    sha256: 2c371290c5f9a12baf68f8161e17da84f9347e1efa92dceeffa402f8784317a4
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-403-run-schema-001/receipt.json
    sha256: 68bdfa5ab910554e306e0ebeb60c45d7e5dd2e42e8122b11a337fa5c8a82a581
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-403-run-schema-001/start.json
    sha256: 1ac9d368aac9e7f9cdf68ce24e14d08475c8ae267e0704445c14512812ab8d2e
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-403-run-strict-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-403-run-strict-001/native.log
    sha256: 507eb374a610bac371b170c2e20d7676422240070ac515c1d10417663d398fe4
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-403-run-strict-001/receipt.json
    sha256: 25a1b4810605938936d07127244cc06b2eb411d1d55a3db5abcf3cbde5d068f9
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-403-run-strict-001/start.json
    sha256: da5416193f6bf937c6d790b12b3454c8e2ec228973dbc18a7ae72da9c3e7e5b8
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-403-run-strict-001/strict.tsv
    sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-403-run-terms-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-403-run-terms-001/native.log
    sha256: fe6e26b365d68c9b62d32c4d001960b3ec597f98834457a84fc4aba5d4edf61a
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-403-run-terms-001/receipt.json
    sha256: b28d1d31169f51a292cf2e3f9a49a12ef50c2af1fee7fe91f3c0785f753e6dc9
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-403-run-terms-001/start.json
    sha256: 086a6634342cbe6476d32ff65f676d016034173bafb0b4dc44f701f62d072d2c
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-415-applied-m5-001/before.yaml
    sha256: d317416542deab471a12785f688c23d08ed5a7eea2894dbde489f40c0df80806
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-415-applied-m5-001/receipt.json
    sha256: 141d1285d44c84123e3e5ddc78a776e0bf61760f01967bd41a29b050f678fd57
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-415-candidate-001/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
    sha256: e950e47008afc7f4371fedefb6f5e75a506dc656e73f282ecd557db1bf10c16d
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-415-candidate-001/receipt.json
    sha256: 3ed4337544783a6e964fcabfd3dfb4e2cc37f0b107a04fee58c6206e243f0775
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-415-check-config-001.json
    sha256: d9be35a2975e2d1944d5796a1fe8410182029e841282df516a1983372886ed63
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-415-run-domain-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-415-run-domain-001/native.log
    sha256: dad14d97aacfbd69afdcfef45d86f142e0a811083a33f9892348621099341526
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-415-run-domain-001/receipt.json
    sha256: 066f62edcc61163b5619614802c806b51a7ffac4c8e36188151dc4bce540165f
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-415-run-domain-001/start.json
    sha256: 0a5214bec90b11f1a3af6a180503bc5230dd3a16bafb94fccf91e3ffe29a14d6
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-415-run-gtdb-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-415-run-gtdb-001/native.log
    sha256: 47a6fe59b28c924fa1fb29889f297f567bc77be55f679ec0e6784fcf55216356
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-415-run-gtdb-001/receipt.json
    sha256: 35b817449b4b1a14da728c841d5a41ad94d530b64b367eb353551e11746ccff1
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-415-run-gtdb-001/start.json
    sha256: 3d4a53bbf81741d297e53a8142075cd3b9399b6837737b5ca7c2c6248c84c708
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-415-run-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-415-run-history-001/native.log
    sha256: 700b44227c4cf01270ac26f16b308622de0b26f48d71aec49cdfaaab87620f0a
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-415-run-history-001/receipt.json
    sha256: 12a38460efdfc07c1a6881a0634325b65c49f57105825eafd499e3d88d677653
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-415-run-history-001/start.json
    sha256: caa3def2b8c362402598a91b06f3666d6ad5ea83c4f941340e39651bcedd1f1f
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-415-run-new-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-415-run-new-history-001/native.log
    sha256: 2a0083c39ce745f6970af13ee45b406e67af9b10f288ed7753ea35ca9a9cca28
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-415-run-new-history-001/receipt.json
    sha256: 4708ce1683b7208913f280ac040fd18e487facd7ea4cbc318101ea7ec1ae4d0d
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-415-run-new-history-001/start.json
    sha256: 8d935490905e443555c9de382717ac82d8df2e947f84760ad0bfbe028f7aa8e0
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-415-run-scalars-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-415-run-scalars-001/native.log
    sha256: fb12248c71c6c0cf224782253735a90c1b705ab2bc27af676ec9dd6e5722adc4
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-415-run-scalars-001/receipt.json
    sha256: 9ddf5a5c69990b769634d9fa999d9f88f2bde2035d1edd8f3ec46437554bfdf8
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-415-run-scalars-001/start.json
    sha256: ea9293ac43b4b9a40d7da9cf31db299c2990c08222cf474412c8c57ecb1f899b
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-415-run-schema-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-415-run-schema-001/native.log
    sha256: 9a81f9b8767777c39303d0bcd243a8a63be3ab18a7e84853164030925fbb1efe
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-415-run-schema-001/receipt.json
    sha256: 21154d10c2bf1d06a83f757d75667a32635c85d4d849af57b6469edac791828e
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-415-run-schema-001/start.json
    sha256: 2fdf7e2c5e26355e6baa20a40fcdf46b316e0238c47983f6ab9abd705c414bf8
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-415-run-strict-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-415-run-strict-001/native.log
    sha256: d4d4358a7531b0437992fcb492110f924c30145bc2c80eb56cbedaad87097856
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-415-run-strict-001/receipt.json
    sha256: a5ad989c7c0c4c6f4e50f139099561c4d42a5b6ddfd4cfcd749dcfb15f72e85f
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-415-run-strict-001/start.json
    sha256: 25f12466b14ce4be7bea5f733684d4870fa7a828440d8aabec254817a1cf5b04
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-415-run-strict-001/strict.tsv
    sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-415-run-terms-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-415-run-terms-001/native.log
    sha256: f3514d6769019b1f81fe4d39f6d97f9a722543e9404a324254d474e7cffafe6c
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-415-run-terms-001/receipt.json
    sha256: b2e6eb74dca80a1ecb4b40bf74550c1cd2e83f531aa627fd433adfc7ddee3c27
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-415-run-terms-001/start.json
    sha256: 379e700b4e069b3caedece94320e6f453acde571c88355c4c330a8d85bf43f9a
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-433-applied-m5-001/before.yaml
    sha256: 61a0b16fc00db138fa35884e8f9f170bda3b2cc9092008a9d5098b3600ad920a
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-433-applied-m5-001/receipt.json
    sha256: d442707388523e63775ed524b9fd7bd59f8134bb4bc1f45e4735847531626b67
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-433-candidate-001/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium.yaml
    sha256: 9cc17693e2d6431cb291cd9713d8c5ac68cbc3d45fa815621cf7ab3d46c59ed3
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-433-candidate-001/receipt.json
    sha256: 8e877f70054f995fbd62393217ba41a5bc41c33aeb28a2881d19472d8f685609
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-433-check-config-001.json
    sha256: dde7cc5f632992d9908f457a3d11fa3e6a83b753f206b3bd45a8f8f1e68e3bed
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-433-run-domain-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-433-run-domain-001/native.log
    sha256: 6a630403f7d53f60eacdaddff451ed28c5f1e0ad1088fa57f81c1ea6ce86edeb
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-433-run-domain-001/receipt.json
    sha256: 3866178773e66335424a855163fa4194f07f5ac73fc8075a52b013457b7d0d6e
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-433-run-domain-001/start.json
    sha256: b5b87849527717aabf783d3e88a9827ad284fc714228d84d083f989b99a8e350
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-433-run-gtdb-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-433-run-gtdb-001/native.log
    sha256: ddb9e71610e5e321ce99b54dbccc5eb8ab1aa02ca0567fb1a82e71bd7f784bd8
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-433-run-gtdb-001/receipt.json
    sha256: 83e42dd924ec09f9e271b4ed7a250e1d736fa4238e18f0009fb09e2d9b139779
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-433-run-gtdb-001/start.json
    sha256: 388298d962358b264a9cd7a018851cb3559fa966f442f1445f6695e865435cb3
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-433-run-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-433-run-history-001/native.log
    sha256: 700b44227c4cf01270ac26f16b308622de0b26f48d71aec49cdfaaab87620f0a
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-433-run-history-001/receipt.json
    sha256: afcca8f315e0b4908625fcad863e4514ffbf0e3109b308a78894cccaa655f656
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-433-run-history-001/start.json
    sha256: 8b90c9166b5fbf376dd3f7802275c4eef2c06784469895112174045d38504c79
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-433-run-new-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-433-run-new-history-001/native.log
    sha256: 444d3c5f429e265ccb3d9dccc5f9b2a4acce48716931f6df4ce236f29c9fc1fa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-433-run-new-history-001/receipt.json
    sha256: 8f67ccad7492dc3a4d1eb0cc9b9a21534dc188e59e4eaa2c586e1cedb814d6d8
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-433-run-new-history-001/start.json
    sha256: 935c48b145764d4a1949107b675fbbd0f23544dcd70f1d6b7a1b9e8c0cd6f69e
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-433-run-scalars-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-433-run-scalars-001/native.log
    sha256: 77cdf1a732dee81a7616dff6c82df1fcd27440ce83040eb961163473802e5016
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-433-run-scalars-001/receipt.json
    sha256: e180ce2217fbd6c98a4a65a559b7107daaa26251f137bb728c3a54ff65df4bd6
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-433-run-scalars-001/start.json
    sha256: cf1ad015b0d312dffb32b7c0f5c607d697acd28db6d37e3c21095d4405aef6f7
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-433-run-schema-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-433-run-schema-001/native.log
    sha256: 1609e641d40b4260f85a0cf409f8149efc15ede75e42b6c1088714f58983f866
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-433-run-schema-001/receipt.json
    sha256: 105c5017c837a8bc8ad7e219815fde240ef86d85e1912879e0bc57dc802aa7c3
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-433-run-schema-001/start.json
    sha256: 6855451f0ebb5d0867b97f1b66f1449fd11e468b21b30a793a422cd3d3b9c641
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-433-run-strict-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-433-run-strict-001/native.log
    sha256: b7a7fea2e273af52d74de44b682e9c84ea866b5298ba072d268f9a7610bfb492
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-433-run-strict-001/receipt.json
    sha256: 204e98103460dc62c66eb1cfe922b6f4eee35abd3319eeb362a5ecfd798c3da5
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-433-run-strict-001/start.json
    sha256: 8d6c20ab2107e7b79184478b0f717df32b1004fedb92b2fb1fbda18ee84aa4e1
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-433-run-strict-001/strict.tsv
    sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-433-run-terms-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-433-run-terms-001/native.log
    sha256: 89c7ef54879e2a19ea2fc258e3d384abc4dc10408eb703f5afbe24dc2af8c070
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-433-run-terms-001/receipt.json
    sha256: 1bbff5393fdc36fa72a67489e801609ee39bb475e884be7a34b833dc3fc8d4ac
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-433-run-terms-001/start.json
    sha256: a10d02fa92e0a2c126d3caa1ca6a04d120a2c213e518da227f7809c160efcd71
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-440-applied-m5-001/before.yaml
    sha256: 6d55992d0ce9ba8a4398c071862cc167ca334085174ed5c7f04aed80829588c2
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-440-applied-m5-001/receipt.json
    sha256: 8117d971a3735d5c404b6a2b656311b0caf05280ae0b8f8e311968aff913406d
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-440-candidate-001/Electrostimulated_Toluene_Methanogenic_Microbiota.yaml
    sha256: a033d28d488388bfbf5f802f652ce4cf3673b10e743cae49431ae4449a13c937
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-440-candidate-001/receipt.json
    sha256: 17a7e2f1279239a940a7e583b905ef16f2018489399a74615e854d4fb32fdcb1
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-440-check-config-001.json
    sha256: fc733f33be9e6a175e62d1710cd2a26ddcea74f2870fd1b37a44f6f1acb7ac36
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-440-run-domain-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-440-run-domain-001/native.log
    sha256: a8506c55c1ba975aea25d3223f1f64a6949296b84fdf297aa0dbe33b9820e5fb
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-440-run-domain-001/receipt.json
    sha256: 2cafd68e3cc891217c117d0e8b4063ebf8f4804c583597b539e8c53f9dfb1cc7
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-440-run-domain-001/start.json
    sha256: db048ec268dbc968a4260e21f073987ea26259a2c15dfbb561ed9df737b59429
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-440-run-gtdb-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-440-run-gtdb-001/native.log
    sha256: 38cccc9f470a531b659dd67e4e297ccd8ae6e23f97b7e2c285d65bb13b01fc81
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-440-run-gtdb-001/receipt.json
    sha256: 97412a123d2d76a7bf32f917affa2a36e81d6c1aedd254cf45fbcffdb0f95de0
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-440-run-gtdb-001/start.json
    sha256: a37da5ee504accec824ff1b948a9cd6f07801b788de4c738a488d2a4c3a7f0ff
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-440-run-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-440-run-history-001/native.log
    sha256: 700b44227c4cf01270ac26f16b308622de0b26f48d71aec49cdfaaab87620f0a
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-440-run-history-001/receipt.json
    sha256: 43e36579c4e9d88ae39560f258b8bf4b007ad8664227d9f341e64472031817b6
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-440-run-history-001/start.json
    sha256: 020a780a87d3662e8cf7bb346c400d6cb4e788eb1b47de11d6b649a8ec1d46f9
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-440-run-new-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-440-run-new-history-001/native.log
    sha256: 9696fae6019c042afad7e50e8ad062dbb88ddec5ff50f95331f36ee091d5760c
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-440-run-new-history-001/receipt.json
    sha256: 75ea085bd8c0548bc8abec19d492ef7a08ca6646ee1913b443f503b92e1ee13c
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-440-run-new-history-001/start.json
    sha256: 0cb41cdfc2aa50f06c3a1e3dd3e8799d14e9882a065728056fd8d3bb73d5edc6
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-440-run-scalars-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-440-run-scalars-001/native.log
    sha256: 5b23531ad6f12b4848306ecdd278ffa0da22fbd2d5068d64aa4df3d936833c19
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-440-run-scalars-001/receipt.json
    sha256: 71f6a1bf0fd9703f059bfb33c8e1f28aa47287f8165b2d8ad09d07043ee8e725
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-440-run-scalars-001/start.json
    sha256: 58e296e2c17b50ffff141212ba8e0c45d0b64f00d80b3bdd03f91ddcd51cba28
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-440-run-schema-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-440-run-schema-001/native.log
    sha256: c5d8b50f5ef5e240806fd6dc57b2ddd5187bc1bc6b77f5bfefc1351a5e3ae839
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-440-run-schema-001/receipt.json
    sha256: 5138e2804a71f1d863f532ca5685ce2128afc21fa204c7f9adfc2b40ae37e28e
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-440-run-schema-001/start.json
    sha256: ae904caa216a6511081f42deb6e545acaf7fd53c634dbcee0a7d76b474ed347a
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-440-run-strict-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-440-run-strict-001/native.log
    sha256: 38bedb6c98039bd7eb240ef34ee23eded0cbb533f8724ee0e63b47b30fd0df9a
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-440-run-strict-001/receipt.json
    sha256: dd97e2d08f625fd7111b3b9f06b02b6183edae27254d05d88b708659597b1570
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-440-run-strict-001/start.json
    sha256: b91f42de423d3a222e75f6a179b0e055f3c06282ff91ba59443407bcfa914554
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-440-run-strict-001/strict.tsv
    sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-440-run-terms-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-440-run-terms-001/native.log
    sha256: 3bd305b0cf1249216f7daabc45b58d01c017b780e9df8fc50e48d56cbac8fde7
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-440-run-terms-001/receipt.json
    sha256: 05f60b3aa647a4a6cdc2701043ba2d14fe23bf9cd80adb4916ae55d5f412a397
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-440-run-terms-001/start.json
    sha256: aed8a812b884206eeef807aba8ecc089111f6e4b1dd79ae0958a3421b0e420b1
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-447-applied-m5-001/before.yaml
    sha256: 0ea86ed4c4587ff6d6fcc424c9bf2a27163154962b8430576b2a6fd4bfb1b36c
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-447-applied-m5-001/receipt.json
    sha256: 4bef56656c67da7ff735d04f164348b6119f84bb43f1cedb6b1beffcc5269083
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-447-candidate-001/Brocadia_Low_Nitrogen_Anammox_Consortium.yaml
    sha256: a552ad2051d22297dd4ebb32accac9a226a45035827fb61982a1b0ccceadb9cb
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-447-candidate-001/receipt.json
    sha256: ecdeecaae4e8dd5ca479ca131f72393e7117429f041196a18cd4e6733f159ad7
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-447-check-config-001.json
    sha256: e98af895d5e35fc06ef68256e48a46b8db7025ff32843402d054b5657ab8621d
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-447-run-domain-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-447-run-domain-001/native.log
    sha256: 28dc57db914a55f46c49908c2bfe0a05fb05dc7882d7f9394b6b30f721931a8b
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-447-run-domain-001/receipt.json
    sha256: cf553a2e115b5f34a5d315cd181faf8fe86d182d50a5782cb0720f78ef406b58
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-447-run-domain-001/start.json
    sha256: d8264e1498d2d12c519475f1e199ffffa088912c4bfab8b23fafed44edd1f7f1
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-447-run-gtdb-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-447-run-gtdb-001/native.log
    sha256: 5d81fa81f60a6157c02568712bba0e7a36adacbec8a1a00eb383ad031638be21
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-447-run-gtdb-001/receipt.json
    sha256: a1698ad192387e4f715de776b4445ba30bf63dd273ba54633149e09eff632751
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-447-run-gtdb-001/start.json
    sha256: d6bee2bf6791e9ab59d2ea59ba071aeb5f953eed5b3aadd153265494aef37208
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-447-run-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-447-run-history-001/native.log
    sha256: 700b44227c4cf01270ac26f16b308622de0b26f48d71aec49cdfaaab87620f0a
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-447-run-history-001/receipt.json
    sha256: a09826b14f62a87874d37bcacbfea4e03b81720d0068492d19b2a86109fa8ebf
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-447-run-history-001/start.json
    sha256: 3fedab3c2f1021cee256352f63ab48537e54394498f59da152749e774eb0a62a
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-447-run-new-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-447-run-new-history-001/native.log
    sha256: c8a34a36e7cdf2b6bbe538901dd26b14208ac03dcb958d294273a8ef87ef5fe4
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-447-run-new-history-001/receipt.json
    sha256: 9f1510ab5dce9a5b4ff92fe18541ecb16a9c30ac2c6078817d5a2226ef1709dc
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-447-run-new-history-001/start.json
    sha256: 734839171f8543342eabc704aa30916a93693e56286dc7be93963f86e39f6555
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-447-run-scalars-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-447-run-scalars-001/native.log
    sha256: a276bb0795ff00901a4818bc12d08060df213f0cd579bdc8fbed58809faf440a
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-447-run-scalars-001/receipt.json
    sha256: 59564cebcc95aa88de417eb8cb8e57ead72c8f30b66a68480902a40d2c42977b
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-447-run-scalars-001/start.json
    sha256: a69888433633ef52ac77d26da28c1d682eb82b646016073b1d4f27cd08f48a46
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-447-run-schema-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-447-run-schema-001/native.log
    sha256: d7f4aa5ee08a1b9e603175aaf018d330b668c22c128dd6d21a722f410a759b12
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-447-run-schema-001/receipt.json
    sha256: b79497b2e1f5025ced28a0cc3a711f8bbc2b4306cd58e1a87f1e22c80c7cc0f4
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-447-run-schema-001/start.json
    sha256: 95ed367fc049597cd036a710392f26d81b6d237f478eb5c6f8a329407fe863de
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-447-run-strict-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-447-run-strict-001/native.log
    sha256: a89ac91a74941b3416fb28086d90ef4c0b658f7fd33f77fae26eb2f9403fabb9
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-447-run-strict-001/receipt.json
    sha256: 27f81d1959a302eaa2fbd0114e609563fc6c401bbc04d1784423b7bad2e860b3
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-447-run-strict-001/start.json
    sha256: 42df9d4b81db261220312e275c1d3eba425e484a8a06d61e28d3669be8351b9d
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-447-run-strict-001/strict.tsv
    sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-447-run-terms-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-447-run-terms-001/native.log
    sha256: fb91c97d632b1b34da5e7da2535fc852c2afa6d6cc3ab8029edfe946c21efd2a
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-447-run-terms-001/receipt.json
    sha256: f4dbe54989153ffef36dc1d98a26a5ee07ff6bbc1c48562e8bc996a89da242a1
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-447-run-terms-001/start.json
    sha256: ebefc37f5c8e6e8e93ba056b9ad72633e58c62b96b75a333fa9cf6da426b2d8f
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-474-applied-m5-001/before.yaml
    sha256: afddcb4da0903a9eb3ba3859641c9cbb60e3b90742bc6bc7a928e38da1c86885
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-474-applied-m5-001/receipt.json
    sha256: ee3ea76c83a6c8db170840dbe5675b34a556a7024b00e57e0242a8fc17c99b85
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-474-candidate-001/Whale_Fall_Vallitalea_Trichloromonas_Chitin_EET_Consortium.yaml
    sha256: b401dae6d9444065e95db02659dd85573da42649c03d6686e3f85bccc2f98aa7
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-474-candidate-001/receipt.json
    sha256: 31d1297ceb36bcb52954da3405146a6c915f0c7f7a16d5f413b96157225d4577
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-474-check-config-001.json
    sha256: adaf70bc0f84899d041d8b30c865a2fcb72079061fe9bdf415240bec1ff06b8f
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-474-run-domain-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-474-run-domain-001/native.log
    sha256: 67329faa3cd603454619814405d4b457b77acd1452f982cb4117b54fc33993a0
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-474-run-domain-001/receipt.json
    sha256: e7adde4f6b242f1a6d38605e169b6a9f378af3c6de468b9a293ec6520c0e11dd
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-474-run-domain-001/start.json
    sha256: ab8e6ebedaf0278fefed0e63c80252330b84e24f6d80c5883cacd888d6d45f5b
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-474-run-gtdb-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-474-run-gtdb-001/native.log
    sha256: e90d5371a27067c1a15dd5baf4d3d798988fdc577d8f564706c69cd94d3aac7b
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-474-run-gtdb-001/receipt.json
    sha256: cf8752f51a7915fe10a3505a44e062ea1a85e247e351c851debb74add91a105a
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-474-run-gtdb-001/start.json
    sha256: 2ce43e1ce0100da36e109df40e11805abd0733b042260eed947b896b1fd6835f
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-474-run-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-474-run-history-001/native.log
    sha256: 700b44227c4cf01270ac26f16b308622de0b26f48d71aec49cdfaaab87620f0a
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-474-run-history-001/receipt.json
    sha256: db5ac934430eae031d7874f50ad7818af2742b6d2b13760fce2df2fe96da45c1
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-474-run-history-001/start.json
    sha256: 34107ef34b53de8bca1a5e1843491671e7cab8308975781e223d2e9eaf38ff2a
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-474-run-new-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-474-run-new-history-001/native.log
    sha256: fa1f7b8e6b8190cb6b7617b502ae1d774ded7596b47a3e76de997f9e8d1281a9
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-474-run-new-history-001/receipt.json
    sha256: 1b9f918733f6576c85455bc2c6dad792d2575ea73d8e4dbf23a9adb385b7d04e
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-474-run-new-history-001/start.json
    sha256: 609403d17d5460d53b862ab689d9616a4b382aa7eb8d446b9a2f21aefb0504f4
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-474-run-scalars-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-474-run-scalars-001/native.log
    sha256: 5c2c775ca0d2c465fc99f7fd49be5070c1775cd9081e940fe5591681c218f5ca
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-474-run-scalars-001/receipt.json
    sha256: 538e645940ad032ec238902171d9f05b772b8a6841c54f17a0e63c613246cf93
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-474-run-scalars-001/start.json
    sha256: 87ce2b89bd150db7ab93819e570c8aaa5a581a6a63f964b5323f09b8a9f35528
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-474-run-schema-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-474-run-schema-001/native.log
    sha256: 51c778a2b8a903fdc0f5034e79a85c0bac9baa103c79309e0fb8b075980357a4
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-474-run-schema-001/receipt.json
    sha256: 176184297147c02cdd2e74d9cd64890d55332484f4d27ec27d09ee81dbff54a5
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-474-run-schema-001/start.json
    sha256: 65801ed6676b3712bdd5e55c4a9c813593a584085cf1d15b4315e2eb714119b1
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-474-run-strict-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-474-run-strict-001/native.log
    sha256: e2fb90f99a956a2aef738265e8a53318fa7e023b94ae5c404021f61b65dd24d7
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-474-run-strict-001/receipt.json
    sha256: d66cd7ccc8a670581ebb6aa8c8de2dba1a5a3cf6717d2e9981486cd991f0ea40
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-474-run-strict-001/start.json
    sha256: 1c2ad3be657d509ebe34b4f9b52fdba9a0fbda754fdb5520eb98901d600e8ab7
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-474-run-strict-001/strict.tsv
    sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-474-run-terms-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-474-run-terms-001/native.log
    sha256: 7f128aaa0ea5f03d87b71178669ac783011702918797d8162f45b8fb73d33b42
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-474-run-terms-001/receipt.json
    sha256: 7cd9554b053b7ac8ef89b8cec262e7be70935eadbdefed5b7ee0a280471189a8
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-474-run-terms-001/start.json
    sha256: f1cfee2543ce275e471b8b46e0d93c7f3eb0c01a125ce77cf9f59b3a0d704619
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-477-applied-m5-001/before.yaml
    sha256: 2647853142ba6426234854ef5ec1c925ce72086f7e3fc480a4949b7d34fdf549
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-477-applied-m5-001/receipt.json
    sha256: 1b97e5b5dbec6ef2b1779581b2be259ab847bb67c655e99c283b5b214a0dd419
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-477-candidate-001/Cucumber_Low_Phosphorus_Cross_Kingdom_Biocontrol_SynCom.yaml
    sha256: 5185491b5bf337064029dbb746a22015c68785964b73069c47da456b751e3e97
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-477-candidate-001/receipt.json
    sha256: ed5b71fad689746d6b5b971b8b33699aa6ed4e82cec3cb12dc706abbb9aed04a
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-477-check-config-001.json
    sha256: 079dd7bbd544fe4c15e595cbfa19eb444aeed960c18adcda34142139aeaf80e0
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-477-run-domain-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-477-run-domain-001/native.log
    sha256: a18b3d73c09719fcca52c385be6a5f105d84cafcb79ca9ff0dabe3bfd18a937f
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-477-run-domain-001/receipt.json
    sha256: a3d1ecc20c98f0deb3af07f24a8f2060c093d2ada2f2b296eaf71e56e7c8b2a1
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-477-run-domain-001/start.json
    sha256: e4dc69fd37a05f489d466442f376fc3b1fbe225a1cc224786c981bfa137d663f
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-477-run-gtdb-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-477-run-gtdb-001/native.log
    sha256: 38dda47074e8ac467adb5c186f9b3b1749f786add49f998bbdd89dcfc4ad5ba6
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-477-run-gtdb-001/receipt.json
    sha256: 8fd8badfca054681553b9b984fc4330a7456d9924ad6edbe670333db72e272b6
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-477-run-gtdb-001/start.json
    sha256: c093127dd60505a00d44c8e59681cb0fced8d94710b2db1b8629b08304001e18
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-477-run-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-477-run-history-001/native.log
    sha256: 700b44227c4cf01270ac26f16b308622de0b26f48d71aec49cdfaaab87620f0a
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-477-run-history-001/receipt.json
    sha256: 4632d97665272cbe7a85cfd580bb69789d59a0542f2135b14aad53cd35d43f30
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-477-run-history-001/start.json
    sha256: 4b8494cff666fc289a9c5bdd470934b159fe501e26b6271156da818897a832e0
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-477-run-new-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-477-run-new-history-001/native.log
    sha256: e33969e4cc0827ae27e277c5cf3b633608583e70f55b888d4ed36bbb1b09f0c1
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-477-run-new-history-001/receipt.json
    sha256: 5d180095f48d678337d1119e9051f2e4f816a2d21f4b29216cb68c2f1b09216f
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-477-run-new-history-001/start.json
    sha256: aa9f41c8938d1edc7cf4adbbae292ba3575a5284cdb42dd75a6e80a49fcd2b14
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-477-run-scalars-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-477-run-scalars-001/native.log
    sha256: a6b36b2ae9cc3c52c5384ffbbea002735912b77f6e576de26172a197a3c0b30b
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-477-run-scalars-001/receipt.json
    sha256: 4f4a5d6abf6605a13b78d485339ec96402576c509547c9220af8fd0f0fb00911
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-477-run-scalars-001/start.json
    sha256: cd832c13aef97a3388188e42ade7f529c2d2a1e91cdb18584002d9da565367ba
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-477-run-schema-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-477-run-schema-001/native.log
    sha256: 4c1c9d9a96e986932cf1a033777332c962738b32e1ee9ee6cf150f9810b0bfb6
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-477-run-schema-001/receipt.json
    sha256: 0c5e3b7c8225270fadb28a0d932b468151c03dd010f78f6ebff3b8ac46b1ae90
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-477-run-schema-001/start.json
    sha256: 801faeb48f00bd04eb0f0de1f3c8e6ae38915a1d6bcc6ee0edff775f5d359035
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-477-run-strict-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-477-run-strict-001/native.log
    sha256: a6d15d7f491ca7f5d3decdd6a6c1da7d7d1c066de2c0804313d6e080be9e7078
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-477-run-strict-001/receipt.json
    sha256: 724adc3e6e9791d3d678f4de2f4420b6c7a11183a2a636ce37c978c7ed56fadc
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-477-run-strict-001/start.json
    sha256: 1ec7be2d283add7397d328716042413ada6ca1634ef3177044fba468813a30fc
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-477-run-strict-001/strict.tsv
    sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-477-run-terms-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-477-run-terms-001/native.log
    sha256: 7da39c830567c4f238e67d43b2bd87ec0d5b8cd5231ede54897e3b67c50d06c4
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-477-run-terms-001/receipt.json
    sha256: 9a27ec1e0cf733267386fb56f38f12f0faeb9d97b096c78d35a00e51e3999d58
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-477-run-terms-001/start.json
    sha256: d8afff1d88c672fecf8dc735fa26d2fbd704a12f20c4f3b006a9cecff9b73034
    role: context
  - path: .temp/gtdb-code006-20261115/genus-nine-route-plan-001.json
    sha256: 567d7ce8b44e1c5d295495b1a1f7ed7be3845e7e0b371eb46eaee6f770c1102e
    role: context
  - path: .temp/gtdb-code006-20261115/kg-microbe/data/raw/NCBI2GTDB.tsv.gz
    sha256: 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd
    role: context
  - path: .temp/phase2-schema-20261115/genus-nine-bind-batch-002.log
    sha256: 41677e89a93937b1e5dec2fe1928366c855d5dbf1f535758fa8b485d44a0d464
    role: context
  - path: .temp/phase2-schema-20261115/genus-nine-route-batch-001.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/phase2-schema-20261115/genus-nine-route-batch-001.json
    sha256: 4e0765208d8634b662e61f0343831d2b41ab76dadc6d01eb4e4b5bed56098638
    role: context
  - path: .temp/phase2-schema-20261115/genus-nine-route-batch-001.log
    sha256: 3370f86c1a9d40ff6358331d70e305a992afbc31e0602ec717aab1f2f4b2a299
    role: context
  - path: history/records/Algal_Methanotroph_Biogas_Valorization_Coculture/2026-09-22T021817Z-codex-f1f2c6.yaml
    sha256: 9bfc08ee8935ee656496cef83e96ea5fc7ee6ade7edaa4cb863f561e24fd6f43
    role: context
  - path: history/records/Algal_Methanotroph_Biogas_Valorization_Coculture/2026-09-22T022344Z-codex-42bb96.yaml
    sha256: 87094b42b79ea0b6824dbbba9a93238c5fe8ddceb4c92ff75a9fd87ecce4f9cc
    role: context
  - path: history/records/Algal_Methanotroph_Biogas_Valorization_Coculture/2026-09-22T023024Z-codex-7b6bb4.yaml
    sha256: 5144011707902c422b278db5147111dd9a9fbe2ad4bd9ca817e0557407bc5e7b
    role: context
  - path: history/records/Algal_Methanotroph_Biogas_Valorization_Coculture/2026-10-05T084241Z-codex-0a0de5.yaml
    sha256: 986118826596e140971dbae607a5d01293023f3f0120eb6752a3f8e6740584b1
    role: context
  - path: history/records/Algal_Methanotroph_Biogas_Valorization_Coculture/2026-10-21T190000Z-claude-2048.yaml
    sha256: 6daeecaecb30693d966d470d6d1324726d1bcc32d45e232157cc27b68d0c4b46
    role: context
  - path: history/records/Algal_Methanotroph_Biogas_Valorization_Coculture/2026-11-15T085030Z-codex-c54710.yaml
    sha256: e89a7b6409b9ba534f7b59d591f5dfae739b25a67fb40d2acfa6f946c08c627c
    role: context
  - path: history/records/Brocadia_Low_Nitrogen_Anammox_Consortium/2026-09-27T071843Z-claude-code-a3a0aa.yaml
    sha256: fc186aa974700cfdfa206c64bc62ff9c6261c3e05626bbd929561ba22c261806
    role: context
  - path: history/records/Brocadia_Low_Nitrogen_Anammox_Consortium/2026-09-27T072435Z-claude-code-2c4140.yaml
    sha256: e2a99f489164c6a4a059b72ba7a13b99ca01e4a44c648bd6d5f4aeb813b0cb15
    role: context
  - path: history/records/Brocadia_Low_Nitrogen_Anammox_Consortium/2026-10-21T190000Z-claude-2048.yaml
    sha256: 435184b82102b203b723627e232772ed8475744fd7b04437a5a1b75c5516a700
    role: context
  - path: history/records/Brocadia_Low_Nitrogen_Anammox_Consortium/2026-11-15T085643Z-codex-72a66c.yaml
    sha256: 592626c9bfeab5f12aa6081add26a732825d1be43d346400c661f8c24036ad38
    role: context
  - path: history/records/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom/2026-09-21T054056Z-claude-code-d1929b.yaml
    sha256: bfe0c4a8683af8a835881bcb76e598c773adf8dada113c1e323387239fb22109
    role: context
  - path: history/records/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom/2026-09-21T054819Z-claude-code-522281.yaml
    sha256: 42c071099ed7ae6f26a9825156b803c0a87822be9671573da9cc8ed618d35d4f
    role: context
  - path: history/records/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom/2026-09-21T061445Z-claude-code-e2a79e.yaml
    sha256: 0e857f378600a62f5967e2cf83666aa8929887b372d07da6314cee9de7c5b02b
    role: context
  - path: history/records/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom/2026-10-05T215546Z-codex-e8e755.yaml
    sha256: 8f8f622532922fa917977260eb6f2a22e072d3526613e533e7911cc9e0719bf6
    role: context
  - path: history/records/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom/2026-11-15T090101Z-codex-c5b11d.yaml
    sha256: 4969f87e559b5aa896893db9509aa185528150aaa71f0520693445499dbc4905
    role: context
  - path: history/records/Cucumber_Low_Phosphorus_Cross_Kingdom_Biocontrol_SynCom/2026-10-19T053000Z-antigravity-6b18.yaml
    sha256: e1c4253fcc5f2df84d8d34bc871d997bd9bb4f92bd164f1d4f622e8947d5d986
    role: context
  - path: history/records/Cucumber_Low_Phosphorus_Cross_Kingdom_Biocontrol_SynCom/2026-10-20T041800Z-antigravity-264785.yaml
    sha256: c8faa30668d21b9adb7b0d314a8d34a4b1f4ed9d3a521be429d9b1825f8d1b7d
    role: context
  - path: history/records/Cucumber_Low_Phosphorus_Cross_Kingdom_Biocontrol_SynCom/2026-11-15T085202Z-codex-ea17c3.yaml
    sha256: 56e923be77fa21a37379dc5b8c0993d4be136e69cfd231e489343b1dff4da699
    role: context
  - path: history/records/Electrostimulated_Toluene_Methanogenic_Microbiota/2026-09-26T183856Z-codex-ac96a5.yaml
    sha256: 67340f14e32a481e41a8ccb47e0fb51024b15e3d30b53a2e3a8bec24e03ed585
    role: context
  - path: history/records/Electrostimulated_Toluene_Methanogenic_Microbiota/2026-10-06T084910Z-codex-af5821.yaml
    sha256: 5f275019e1a0c960f5096cedc0ebed94e9a20247ac68a2654715a69bb03c0eda
    role: context
  - path: history/records/Electrostimulated_Toluene_Methanogenic_Microbiota/2026-11-15T085514Z-codex-6b318a.yaml
    sha256: 8ad00c2adf1ebb9bad7ac56ca30fc5764a9428da7d7ae7cba665717717495433
    role: context
  - path: history/records/Hualgayoc_Acidic_Sulfate_Reducing_AMD_Consortium/2026-10-06T153824Z-codex-bb95e3.yaml
    sha256: 608f4d15f69adbe849197a8963b0771165513b4b9cc338c81a9710898e1aa7e3
    role: context
  - path: history/records/Hualgayoc_Acidic_Sulfate_Reducing_AMD_Consortium/2026-11-15T085323Z-codex-c560ea.yaml
    sha256: 315c2ff40da56e298a01cf6694c22410e2a5fdb4bee18ca4baffdce5c080f3fc
    role: context
  - path: history/records/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium/2026-09-26T072714Z-codex-433.yaml
    sha256: 02246591af5a866e4d30d108b5ad2c83b04578f7a18fcfa23216b5136baf7a5c
    role: context
  - path: history/records/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium/2026-09-26T073006Z-codex-1083.yaml
    sha256: 4ad37ddaf3f9bbbb08373e0e3a53e613cf926d41c5e196c78d09e3896f56fa81
    role: context
  - path: history/records/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium/2026-10-07T044213Z-codex-ac464a.yaml
    sha256: ad0fb52f747bdfd3141faff3c3291821458436db27ab0bfd71fc65a6f5a736d8
    role: context
  - path: history/records/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium/2026-11-15T085813Z-codex-981495.yaml
    sha256: 06209e01ee4efc215a59f0496148c09a0d7d4745de30de31497a6c395891f4ba
    role: context
  - path: history/records/Whale_Fall_Vallitalea_Trichloromonas_Chitin_EET_Consortium/2026-10-19T053000Z-antigravity-84ac.yaml
    sha256: d4ff3d882b20a1c55b3e577bb70c7210adf5d1b22699efaaec97b8750d7ada74
    role: context
  - path: history/records/Whale_Fall_Vallitalea_Trichloromonas_Chitin_EET_Consortium/2026-10-20T041800Z-antigravity-afddcb.yaml
    sha256: 48a9d6c06cf1cd30f1fd4995ff384e51d43f799d4326f81b3dcc5eb9c205d3bc
    role: context
  - path: history/records/Whale_Fall_Vallitalea_Trichloromonas_Chitin_EET_Consortium/2026-11-15T085939Z-codex-6f9205.yaml
    sha256: 1c65d4a95bb7b025fb63d2c99f60dece86a56dbe30f1a98c0f80cb9a343c0b89
    role: context
  - path: justfile
    sha256: 40369611ad4531582e420df0e9ff22109e4b18adf03b34d86b54200b280f2d0f
    role: context
  - path: kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
    sha256: e950e47008afc7f4371fedefb6f5e75a506dc656e73f282ecd557db1bf10c16d
    role: target
  - path: kb/communities/Brocadia_Low_Nitrogen_Anammox_Consortium.yaml
    sha256: a552ad2051d22297dd4ebb32accac9a226a45035827fb61982a1b0ccceadb9cb
    role: target
  - path: kb/communities/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom.yaml
    sha256: 57f34a82b45bc938d82175cd25bda54f53f981fc49f1a24b6d30f67094ac82a3
    role: target
  - path: kb/communities/Cucumber_Low_Phosphorus_Cross_Kingdom_Biocontrol_SynCom.yaml
    sha256: 5185491b5bf337064029dbb746a22015c68785964b73069c47da456b751e3e97
    role: target
  - path: kb/communities/Electrostimulated_Toluene_Methanogenic_Microbiota.yaml
    sha256: a033d28d488388bfbf5f802f652ce4cf3673b10e743cae49431ae4449a13c937
    role: target
  - path: kb/communities/Hualgayoc_Acidic_Sulfate_Reducing_AMD_Consortium.yaml
    sha256: 99115a41c2c32e4ead8941e8cce89838944047e7f17221295bd73bfab63c8c13
    role: target
  - path: kb/communities/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium.yaml
    sha256: 9cc17693e2d6431cb291cd9713d8c5ac68cbc3d45fa815621cf7ab3d46c59ed3
    role: target
  - path: kb/communities/Whale_Fall_Vallitalea_Trichloromonas_Chitin_EET_Consortium.yaml
    sha256: b401dae6d9444065e95db02659dd85573da42649c03d6686e3f85bccc2f98aa7
    role: target
  - path: pyproject.toml
    sha256: be952f0f137f85fed66bda0908f12014f1797a2dd229b44d832afc0c00471655
    role: context
  - path: references_cache/PMID_38865893.txt
    sha256: e801f5d665ea8d807869572afb4ac348fa92b31d007b7819fd9c79b38723300b
    role: context
  - path: references_cache/PMID_41457319.txt
    sha256: 904d315f9949e5ef5780954efbfad8bb6f542e6cd5e291248b83eb0eec9c2e8e
    role: context
  - path: references_cache/PMID_41745484.txt
    sha256: ad543c6e92b26ff25763f25f499719f0075bdfe85af9d006b20ae5865f50b9ae
    role: context
  - path: references_cache/PMID_41882811.txt
    sha256: dec747f6c57b4d919b7935ef153e012c999d4798a19dcd2aae2e5d91fead4ac6
    role: context
  - path: references_cache/PMID_42029028.txt
    sha256: 47cde42470db1b13f2cf75cf5f3131dda202cc1ce1dd9b736ee9789dc4fe6937
    role: context
  - path: references_cache/PMID_42297039.txt
    sha256: 5c1f67ef420c1aff46bc86678763c725f728a20688c094a776373a8a214e8989
    role: context
  - path: references_cache/PMID_42323145.txt
    sha256: dae56a2cb0f7223e87c5c6069c6437f02cfb7a7dc09c09135c30273626dfb018
    role: context
  - path: references_cache/PMID_42482240.supplement.md
    sha256: 45614f71bd112451ce0a5bb4b11f201c4e80278cb56c2cc591d5fc9bd0fcc726
    role: context
  - path: references_cache/PMID_42482240.txt
    sha256: fa818b4fb415527b08960aeb8aa118fef46555bc01b18126eb99b66dbae61210
    role: context
  - path: reports/causal_graph_review/decisions/20261005-three-records-batch15.yaml
    sha256: 9a91951bf6002151122053f4d0ad0c13ada0c7b4f61bff989a612268c9750dc0
    role: context
  - path: reports/causal_graph_review/decisions/20261005-twelve-records-batch4.yaml
    sha256: e21a355f676730e8e7e6de6ea663017c9b09e05a824ff383a272ab9f1399fd70
    role: context
  - path: reports/causal_graph_review/decisions/20261006-three-records-batch37.yaml
    sha256: 363b8d16d8cedae28dbbc6a5699ae9dd2de614364c305e68631891531a32e74e
    role: context
  - path: reports/causal_graph_review/decisions/20261006-urls-amd-proteome-batch52.yaml
    sha256: dca1ccadf55067fc169f67a18b738ba22b195153590515fa4563c183900d02e5
    role: context
  - path: reports/causal_graph_review/decisions/20261007-four-records-batch78.yaml
    sha256: 5803b1826d23abd55d08addeb735915efbe4906b77096584338e28c200415ea2
    role: context
  - path: reports/causal_graph_review/decisions/20261020-stage2-fifteen-records-batch133.yaml
    sha256: e9ded35a2333f9994869573f9f952b3af3191ab55528813a7f2c03639a362d3f
    role: context
  - path: reports/causal_graph_review/decisions/20261021-stage5-review-remediation.yaml
    sha256: efe4b6b56ae2ad5cb78452493088e5c046f10602461d581920791b19f9178119
    role: context
  - path: reports/gtdb-code006-20261115/genus-nine-353-source-evidence-001.json
    sha256: d40b7df7e6e526904941aa14b2a773243dec946824cd3024d1a1ec5b2c8c1724
    role: context
  - path: reports/gtdb-code006-20261115/genus-nine-403-source-evidence-001.json
    sha256: d2aec53507d77ebf258c4157e04ec20f1577729837bb6bdb33b875f8302782ae
    role: context
  - path: reports/gtdb-code006-20261115/genus-nine-415-source-evidence-001.json
    sha256: aeb82fee0c71b823fd6ccff46cb4f49b6e3ecf2ff82f3cc1170987bd2e999f3a
    role: context
  - path: reports/gtdb-code006-20261115/genus-nine-433-source-evidence-001.json
    sha256: 01a04674345c1d41919ac56bb0f1264ce06b19f1d7fd6f2855ef9d2d06c9ac10
    role: context
  - path: reports/gtdb-code006-20261115/genus-nine-440-source-evidence-001.json
    sha256: 656d51ef03e9be7a801f959595d0913d52aec26a007272723edc3cc618badf81
    role: context
  - path: reports/gtdb-code006-20261115/genus-nine-447-source-evidence-001.json
    sha256: 12f15674cbb36183cb9f9ab20e09eb1dca45e8baa59bca40a6ff87f0c18b480f
    role: context
  - path: reports/gtdb-code006-20261115/genus-nine-474-source-evidence-001.json
    sha256: fa87a47c551349320a6f0df00f5b9fb84fd91526d42634019f8d59099935e8a1
    role: context
  - path: reports/gtdb-code006-20261115/genus-nine-477-source-evidence-001.json
    sha256: f906428246fc66d36142c33b8f617dfead864bfa1c5be5aeb681fd6d9e104ea5
    role: context
  - path: reports/gtdb-code006-20261115/genus-nine-authored-source-context-002.json
    sha256: ad72f2e1c04d03efbb025502464840e3452cab8c18d948423db00a62c0fa7243
    role: context
  - path: reports/gtdb-code006-20261115/genus-nine-eight-review-config-001.json
    sha256: 0cbfef26a3c8c11ed466c8fc77d12580d5b111c4d52764abe351a44c1a916cba
    role: context
  - path: reports/gtdb-code006-20261115/genus-nine-source-config-002.json
    sha256: 4de351549bfc5b6784461ce183eae2797953d3676204805122b29740ff2c2cc7
    role: context
  - path: reports/phase2-completion-20261115/genus-additional-three-source-context-001.yaml
    sha256: 3bf0ae45e8220568174f48c057d89559ab5e713a04217eb0edad2ce31ac5c257
    role: context
  - path: reports/phase2-completion-20261115/genus-enrichment-three-source-context-001.yaml
    sha256: 600978eb459f6ec2531f52c0f19e3383d830802a2719d714aa8c2d4605c1c6a8
    role: context
  - path: reports/phase2-completion-20261115/genus-plant-three-source-context-001.yaml
    sha256: e203d26b442f07cb044a57e04c04448d8064338a7048528041b9520947cf691a
    role: context
  - path: reports/phase2-completion-20261115/higher-rank-enrichment-three-source-context-001.yaml
    sha256: 0265a09b58e8e6b7b93948a37bdd2030753b6863b2ed1c006131437d5056ff91
    role: context
  - path: reviews/structured/20261021T192924Z-choysum-synlav-record/review.yaml
    sha256: 8bc00677f77589ef843099ed024a48ab5f00d960ed199958168e51554f1ce850
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/adhoc/bind_gtdb_batch_source_context_20261115.py
    sha256: 6cdeb82122c130cd5b2e7e73bbe66bc5123fc951892f9f87edb589fb4929aac3
    role: context
  - path: scripts/adhoc/build_gtdb_batch_diagnostic_20261115.py
    sha256: c6bf0d09dc3d01797ab5d956a4f7458a9a153a8704508f50e656729e4ee1b860
    role: context
  - path: scripts/adhoc/check_gtdb_batch_unit_20261115.py
    sha256: 723047d1ec66fa752d6cedddbb6d399b18fa7f5b7a0e27fc435c76abfeb10493
    role: context
  - path: scripts/adhoc/compose_gtdb_source_config_20261115.jq
    sha256: 45f228d7cbd89ac7b39ff0f470d6a7602e822b866133d2f9a1b462ce38f9d5a5
    role: context
  - path: scripts/adhoc/export_m5_technical_evidence_20261114.py
    sha256: a0f43f617e8921443e660d262d28713f40b4c23770b684203c37b65330cc4a5d
    role: context
  - path: scripts/adhoc/gtdb_batch_curation_20261115.py
    sha256: 867e974e9c55325fb1b7e32f81dcf6b7a65b6720941fd303040f5570e46ba232
    role: context
  - path: scripts/adhoc/report_gtdb_batch_routes_20261115.py
    sha256: 2d4732edafccba24741b728b9e672ca7fada5e50d8220162a9ccf3c5d8d875ef
    role: context
  - path: scripts/gtdb_ground.py
    sha256: 0fc1ba926a56e5be85cdf064db0cf56452aeeee93f15b0ced98e8f11b5296175
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: src/communitymech/__init__.py
    sha256: c003d906fef500e765c59c8f15ee821054e26c43e59a1be70dbc23c33f8aae66
    role: context
  - path: src/communitymech/curate/__init__.py
    sha256: a591b57cbf73ef2ddb0da6d0b7be0dd784258115ae20cf4883f6f379bcad9324
    role: context
  - path: src/communitymech/curate/curation_event.py
    sha256: 58ebdb58ac39d7a319156ec735db9ef2e9afb4c7350613039ad9dc49d65a5afc
    role: context
  - path: src/communitymech/ontology_adapters.py
    sha256: 7e0a621831b28ac0f718a29c22af8052f93e006012fff77e11d92849e4852c45
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: c6f6e4a5cf42e450cf55d8fcb12817591c736198e24bcd217142b4f86712b4c3
    role: context
  - path: src/communitymech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
    role: context
  - path: src/communitymech/schema/mech_shared.yaml
    sha256: cf32864df1626201128e9311054b075bfc4ad3d8345491ac144122a5d5e67d11
    role: context
  - path: src/communitymech/validation/write_validated.py
    sha256: d19dd3b1e46856b4de67ecc17fc856aaa1034a9a97259cab3bbd54c3891fb019
    role: context
  - path: src/communitymech/validators/__init__.py
    sha256: 975d33a39c8e7173d25aa0de711f25a19158228ecfd837908c829b3f9f14cf93
    role: context
  - path: src/communitymech/validators/ncbi_domain.py
    sha256: b1e7ffc3c35c237e36c2c19fab42f1d42a14161397de9c5e726ed85897f1e262
    role: context
  - path: tests/test_causal_review_batch133.py
    sha256: fd5fac287e359fe33a2032910c0a462db10ae95458537864bf9110b5a1e9ab67
    role: context
  - path: tests/test_causal_review_batch15.py
    sha256: 89c823b38000ed9b77422c1d98475837f48b65d76c0a424f79397b7c15282117
    role: context
  - path: tests/test_causal_review_batch37.py
    sha256: 32a5c6e26cef35f69230655f0823d25c66f537667a0487feba32f83ce82284b5
    role: context
  - path: tests/test_causal_review_batch52.py
    sha256: d095dafc310dab3c7a40c0dc5bcd4d03946675d6ff848902deec1641065fd217
    role: context
  - path: tests/test_causal_review_batch78.py
    sha256: baf1b529b17cbf11902166edd55e87badbf66dfe7d80a80957262b8c6ab1ba79
    role: context
  - path: tests/test_participating_taxa.py
    sha256: 0bad0a41fa227759454f6cb84cd72586b654cd8600ff3efd83b1892d93724c8d
    role: context
  - path: uv.lock
    sha256: 712838f8fa3d68fbd818ac8162f3f1e2f2637db1da1a8ebfaba0ef759690f3b4
    role: context
targets:
- target_id: CommunityMech:000415
  path: kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
  selector: taxonomy[2:6].taxon_term.gtdb_classification; gtdb_grounding_status
  label: Four enrichment-community genus descriptors without named stocks
  kind: maintained
  ownership_note: CommunityMech owns this record; only declared GTDB correspondence/status
    and actual provenance are assessed.
- target_id: CommunityMech:000477
  path: kb/communities/Cucumber_Low_Phosphorus_Cross_Kingdom_Biocontrol_SynCom.yaml
  selector: taxonomy[2:4].taxon_term.gtdb_classification; gtdb_grounding_status
  label: Two genus summaries within the 19-stock cross-kingdom consortium
  kind: maintained
  ownership_note: CommunityMech owns this record; only declared GTDB correspondence/status
    and actual provenance are assessed.
- target_id: CommunityMech:000353
  path: kb/communities/Hualgayoc_Acidic_Sulfate_Reducing_AMD_Consortium.yaml
  selector: taxonomy[0:2].taxon_term.gtdb_classification; gtdb_grounding_status
  label: MAG003 and MAG013 genus-reference correspondences
  kind: maintained
  ownership_note: CommunityMech owns this record; only declared GTDB correspondence/status
    and actual provenance are assessed.
- target_id: CommunityMech:000440
  path: kb/communities/Electrostimulated_Toluene_Methanogenic_Microbiota.yaml
  selector: taxonomy[1:3].taxon_term.gtdb_classification; gtdb_grounding_status
  label: Alternative acetoclastic partner genus correspondences
  kind: maintained
  ownership_note: CommunityMech owns this record; only declared GTDB correspondence/status
    and actual provenance are assessed.
- target_id: CommunityMech:000447
  path: kb/communities/Brocadia_Low_Nitrogen_Anammox_Consortium.yaml
  selector: taxonomy[0:2].taxon_term.gtdb_classification; gtdb_grounding_status
  label: Temporal Brocadia and Kuenenia assemblage descriptors
  kind: maintained
  ownership_note: CommunityMech owns this record; only declared GTDB correspondence/status
    and actual provenance are assessed.
- target_id: CommunityMech:000433
  path: kb/communities/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium.yaml
  selector: taxonomy[0:3].taxon_term.gtdb_classification; gtdb_grounding_status
  label: Three genus-level MAG descriptors in a wastewater enrichment
  kind: maintained
  ownership_note: CommunityMech owns this record; only declared GTDB correspondence/status
    and actual provenance are assessed.
- target_id: CommunityMech:000474
  path: kb/communities/Whale_Fall_Vallitalea_Trichloromonas_Chitin_EET_Consortium.yaml
  selector: taxonomy[0:2].taxon_term.gtdb_classification; gtdb_grounding_status
  label: Vallitalea and Trichloromonas genus correspondence with stock omissions retained
  kind: maintained
  ownership_note: CommunityMech owns this record; only declared GTDB correspondence/status
    and actual provenance are assessed.
- target_id: CommunityMech:000403
  path: kb/communities/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom.yaml
  selector: taxonomy[0:5].taxon_term.gtdb_classification; gtdb_grounding_status
  label: Five distinct SynLAV stocks with genus-reference correspondence
  kind: maintained
  ownership_note: CommunityMech owns this record; only declared GTDB correspondence/status
    and actual provenance are assessed.
scope:
  description: Only the declared GTDB correspondence/status fields and actual application,
    history and native-check provenance for records 415, 477, 353, 440, 447, 433,
    474 and 403. Each target has explicit source, population and preservation assessments.
    This partial diagnostic does not reassess every scientific claim.
  selection: The eight remaining whole-record units in the independently source-prepared
    nine-record batch, after record 410 completed its separately saved and verified
    canary. The reviewed population here is exactly eight records; 410 and other campaign
    records are excluded.
  coverage: partial
  population_size: 8
  reviewed_target_ids:
  - CommunityMech:000415
  - CommunityMech:000477
  - CommunityMech:000353
  - CommunityMech:000440
  - CommunityMech:000447
  - CommunityMech:000433
  - CommunityMech:000474
  - CommunityMech:000403
  exclusions:
  - target: Other scientific claims and records
    reason: Existing biology is preserved, not newly certified by this database diagnostic.
checks:
- check_id: 000415-schema
  name: validate
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000415
  command: just --verbose --no-dotenv --color never validate kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000415-schema
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000415-strict
  name: validate-strict
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000415
  command: just --verbose --no-dotenv --color never validate-strict kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
    --out .temp/gtdb-code006-20261115/genus-nine-415-run-strict-001/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000415-strict
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000415-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000415
  command: just --verbose --no-dotenv --color never validate-gtdb kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000415-gtdb
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000415-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000415
  command: just --verbose --no-dotenv --color never validate-gtdb-domain kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000415-domain
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000415-scalars
  name: validate-scalars
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000415
  command: just --verbose --no-dotenv --color never validate-scalars kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000415-scalars
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000415-history
  name: validate-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000415
  command: just --verbose --no-dotenv --color never validate-history history/records/Algal_Methanotroph_Biogas_Valorization_Coculture
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000415-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000415-new-history
  name: new-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000415
  command: just --verbose --no-dotenv --color never new-history --kind record --slug
    Algal_Methanotroph_Biogas_Valorization_Coculture --target-root kb/communities
    --event EDIT --outcome changed --sections taxonomy,curation_history --actor-name
    codex --model gpt-6 --agent-tool codex --issue https://github.com/CultureBotAI/CommunityMech/issues/2848
    --summary 'Add four bounded genus-reference correspondences for the algal-methanotroph
    enrichment' --details 'Only four reviewed GTDB blocks/statuses and two native
    inline events changed. Preserve all six source descriptors, both eukaryotic exclusions,
    unknown stock identities, biological claims, quotations and old history. Leptolyngbya
    13/24 is a narrow majority in a reference population spanning six GTDB genera,
    not study abundance; the other populations are 8/8, 45/45 and 1/1. Keep culture
    inoculum distinct from community composition, main-assay versus enrichment salt,
    functional potential versus expression or exchange, and absent closed carbon balance.
    This is a partial database correspondence diagnostic, scientific_review:false,
    on frozen M5 e83c687c after the verified 410 canary. Actual apply receipt .temp/gtdb-code006-20261115/genus-nine-415-applied-m5-001/receipt.json
    sha256:141d1285d44c84123e3e5ddc78a776e0bf61760f01967bd41a29b050f678fd57.'
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000415-new-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000415-terms
  name: validate-terms
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000415
  command: just --verbose --no-dotenv --color never validate-terms kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000415-terms
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000477-schema
  name: validate
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000477
  command: just --verbose --no-dotenv --color never validate kb/communities/Cucumber_Low_Phosphorus_Cross_Kingdom_Biocontrol_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000477-schema
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000477-strict
  name: validate-strict
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000477
  command: just --verbose --no-dotenv --color never validate-strict kb/communities/Cucumber_Low_Phosphorus_Cross_Kingdom_Biocontrol_SynCom.yaml
    --out .temp/gtdb-code006-20261115/genus-nine-477-run-strict-001/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000477-strict
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000477-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000477
  command: just --verbose --no-dotenv --color never validate-gtdb kb/communities/Cucumber_Low_Phosphorus_Cross_Kingdom_Biocontrol_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000477-gtdb
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000477-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000477
  command: just --verbose --no-dotenv --color never validate-gtdb-domain kb/communities/Cucumber_Low_Phosphorus_Cross_Kingdom_Biocontrol_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000477-domain
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000477-scalars
  name: validate-scalars
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000477
  command: just --verbose --no-dotenv --color never validate-scalars kb/communities/Cucumber_Low_Phosphorus_Cross_Kingdom_Biocontrol_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000477-scalars
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000477-history
  name: validate-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000477
  command: just --verbose --no-dotenv --color never validate-history history/records/Cucumber_Low_Phosphorus_Cross_Kingdom_Biocontrol_SynCom
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000477-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000477-new-history
  name: new-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000477
  command: just --verbose --no-dotenv --color never new-history --kind record --slug
    Cucumber_Low_Phosphorus_Cross_Kingdom_Biocontrol_SynCom --target-root kb/communities
    --event EDIT --outcome changed --sections taxonomy,curation_history --actor-name
    codex --model gpt-6 --agent-tool codex --issue https://github.com/CultureBotAI/CommunityMech/issues/2848
    --summary 'Add bounded Sphingopyxis and Cupriavidus reference correspondences'
    --details 'Only two reviewed genus blocks/statuses and two native inline events
    changed; other status-key movement is semantically unchanged. Preserve 19 source
    stocks represented by six genus descriptors, including two Sphingopyxis and three
    Cupriavidus stocks, with no new stock genome or species assignment. Reference
    populations 79/79 and 199/199 are not stock counts. Existing Bacillus/Devosia
    mappings, fungal exclusions, Amesia source wording, all biology and old history
    remain intact. Low-P discovery, reconstruction, metabolite supplementation, high-P
    disease tests and pair-specific interaction limits remain distinct. Partial technical
    correspondence only, scientific_review:false, on frozen M5 e83c687c. Actual apply
    receipt .temp/gtdb-code006-20261115/genus-nine-477-applied-m5-001/receipt.json
    sha256:1b97e5b5dbec6ef2b1779581b2be259ab847bb67c655e99c283b5b214a0dd419.'
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000477-new-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000477-terms
  name: validate-terms
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000477
  command: just --verbose --no-dotenv --color never validate-terms kb/communities/Cucumber_Low_Phosphorus_Cross_Kingdom_Biocontrol_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000477-terms
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000353-schema
  name: validate
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000353
  command: just --verbose --no-dotenv --color never validate kb/communities/Hualgayoc_Acidic_Sulfate_Reducing_AMD_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000353-schema
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000353-strict
  name: validate-strict
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000353
  command: just --verbose --no-dotenv --color never validate-strict kb/communities/Hualgayoc_Acidic_Sulfate_Reducing_AMD_Consortium.yaml
    --out .temp/gtdb-code006-20261115/genus-nine-353-run-strict-001/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000353-strict
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000353-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000353
  command: just --verbose --no-dotenv --color never validate-gtdb kb/communities/Hualgayoc_Acidic_Sulfate_Reducing_AMD_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000353-gtdb
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000353-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000353
  command: just --verbose --no-dotenv --color never validate-gtdb-domain kb/communities/Hualgayoc_Acidic_Sulfate_Reducing_AMD_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000353-domain
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000353-scalars
  name: validate-scalars
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000353
  command: just --verbose --no-dotenv --color never validate-scalars kb/communities/Hualgayoc_Acidic_Sulfate_Reducing_AMD_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000353-scalars
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000353-history
  name: validate-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000353
  command: just --verbose --no-dotenv --color never validate-history history/records/Hualgayoc_Acidic_Sulfate_Reducing_AMD_Consortium
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000353-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000353-new-history
  name: new-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000353
  command: just --verbose --no-dotenv --color never new-history --kind record --slug
    Hualgayoc_Acidic_Sulfate_Reducing_AMD_Consortium --target-root kb/communities
    --event EDIT --outcome changed --sections taxonomy,curation_history --actor-name
    codex --model gpt-6 --agent-tool codex --issue https://github.com/CultureBotAI/CommunityMech/issues/2848
    --summary 'Add two genus-reference correspondences while preserving MAG-specific
    uncertainty' --details 'Only Desulfosporosinus MAG003 and Acididesulfobacillus
    MAG013 genus-reference blocks/statuses and two native events changed. The 32/32
    and 3/3 reference populations are not the study MAGs or isolate counts; the day-160
    enrichment remains distinct from a defined two-isolate SynCom. Preserve source
    species uncertainty, the separate reported ANI result, glycerol-to-acetate potential
    for both MAGs, PARTIAL flux, residual acetate, minor acidogens, reinoculation
    and pH limits. All quotations, biology and old history remain exact. Partial technical
    diagnostic, scientific_review:false, on frozen M5 e83c687c. Actual apply receipt
    .temp/gtdb-code006-20261115/genus-nine-353-applied-m5-001/receipt.json sha256:6ecc66f1ee3da3fbe06192cd25666c162b9a23c16c0b0d47933473f2c7024fbb.'
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000353-new-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000353-terms
  name: validate-terms
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000353
  command: just --verbose --no-dotenv --color never validate-terms kb/communities/Hualgayoc_Acidic_Sulfate_Reducing_AMD_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000353-terms
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000440-schema
  name: validate
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000440
  command: just --verbose --no-dotenv --color never validate kb/communities/Electrostimulated_Toluene_Methanogenic_Microbiota.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000440-schema
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000440-strict
  name: validate-strict
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000440
  command: just --verbose --no-dotenv --color never validate-strict kb/communities/Electrostimulated_Toluene_Methanogenic_Microbiota.yaml
    --out .temp/gtdb-code006-20261115/genus-nine-440-run-strict-001/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000440-strict
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000440-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000440
  command: just --verbose --no-dotenv --color never validate-gtdb kb/communities/Electrostimulated_Toluene_Methanogenic_Microbiota.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000440-gtdb
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000440-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000440
  command: just --verbose --no-dotenv --color never validate-gtdb-domain kb/communities/Electrostimulated_Toluene_Methanogenic_Microbiota.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000440-domain
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000440-scalars
  name: validate-scalars
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000440
  command: just --verbose --no-dotenv --color never validate-scalars kb/communities/Electrostimulated_Toluene_Methanogenic_Microbiota.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000440-scalars
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000440-history
  name: validate-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000440
  command: just --verbose --no-dotenv --color never validate-history history/records/Electrostimulated_Toluene_Methanogenic_Microbiota
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000440-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000440-new-history
  name: new-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000440
  command: just --verbose --no-dotenv --color never new-history --kind record --slug
    Electrostimulated_Toluene_Methanogenic_Microbiota --target-root kb/communities
    --event EDIT --outcome changed --sections taxonomy,curation_history --actor-name
    codex --model gpt-6 --agent-tool codex --issue https://github.com/CultureBotAI/CommunityMech/issues/2848
    --summary 'Add two alternative methanogen genus-reference correspondences' --details
    'Only Methanosarcina and Methanothrix reference blocks/statuses plus two native
    events changed. The 301/301 and 94/117 reference populations do not identify study
    MAGs or prove simultaneous partner membership. Preserve the source alternative-partner
    wording, 800 mV/control distinction, electron-sharing versus acetate alternatives,
    hypothesized graph and missing operating conditions. Existing Bacteria-domain
    and Methanobacterium mappings and unresolved Desulfoprunum remain unchanged, as
    do all scientific claims, quotations and old history. Abstract-only source scope
    and partial scientific_review:false diagnostic remain explicit; frozen M5 e83c687c.
    Actual apply receipt .temp/gtdb-code006-20261115/genus-nine-440-applied-m5-001/receipt.json
    sha256:8117d971a3735d5c404b6a2b656311b0caf05280ae0b8f8e311968aff913406d.'
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000440-new-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000440-terms
  name: validate-terms
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000440
  command: just --verbose --no-dotenv --color never validate-terms kb/communities/Electrostimulated_Toluene_Methanogenic_Microbiota.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000440-terms
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000447-schema
  name: validate
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000447
  command: just --verbose --no-dotenv --color never validate kb/communities/Brocadia_Low_Nitrogen_Anammox_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000447-schema
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000447-strict
  name: validate-strict
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000447
  command: just --verbose --no-dotenv --color never validate-strict kb/communities/Brocadia_Low_Nitrogen_Anammox_Consortium.yaml
    --out .temp/gtdb-code006-20261115/genus-nine-447-run-strict-001/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000447-strict
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000447-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000447
  command: just --verbose --no-dotenv --color never validate-gtdb kb/communities/Brocadia_Low_Nitrogen_Anammox_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000447-gtdb
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000447-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000447
  command: just --verbose --no-dotenv --color never validate-gtdb-domain kb/communities/Brocadia_Low_Nitrogen_Anammox_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000447-domain
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000447-scalars
  name: validate-scalars
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000447
  command: just --verbose --no-dotenv --color never validate-scalars kb/communities/Brocadia_Low_Nitrogen_Anammox_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000447-scalars
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000447-history
  name: validate-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000447
  command: just --verbose --no-dotenv --color never validate-history history/records/Brocadia_Low_Nitrogen_Anammox_Consortium
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000447-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000447-new-history
  name: new-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000447
  command: just --verbose --no-dotenv --color never new-history --kind record --slug
    Brocadia_Low_Nitrogen_Anammox_Consortium --target-root kb/communities --event
    EDIT --outcome changed --sections taxonomy,curation_history --actor-name codex
    --model gpt-6 --agent-tool codex --issue https://github.com/CultureBotAI/CommunityMech/issues/2848
    --summary 'Add Brocadia and Kuenenia reference correspondences without resolving
    species or flux' --details 'Only two approved genus blocks/statuses and two native
    events changed. Reference populations 39/39 and 4/4 are separate from temporal
    culture abundance and transcription measurements; neither identifies the unspecified
    Brocadia assemblage species or study MAGs. Preserve earlier Kuenenia versus later
    Brocadia succession, computational SMETANA auxotrophy, low/high-nitrogen comparison
    and absence of measured interspecies flux. The stage5 history chain, all participants,
    source quotes and biology remain unchanged. Abstract-only source coverage; partial
    scientific_review:false diagnostic on frozen M5 e83c687c. Actual apply receipt
    .temp/gtdb-code006-20261115/genus-nine-447-applied-m5-001/receipt.json sha256:4bef56656c67da7ff735d04f164348b6119f84bb43f1cedb6b1beffcc5269083.'
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000447-new-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000447-terms
  name: validate-terms
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000447
  command: just --verbose --no-dotenv --color never validate-terms kb/communities/Brocadia_Low_Nitrogen_Anammox_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000447-terms
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000433-schema
  name: validate
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000433
  command: just --verbose --no-dotenv --color never validate kb/communities/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000433-schema
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000433-strict
  name: validate-strict
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000433
  command: just --verbose --no-dotenv --color never validate-strict kb/communities/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium.yaml
    --out .temp/gtdb-code006-20261115/genus-nine-433-run-strict-001/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000433-strict
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000433-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000433
  command: just --verbose --no-dotenv --color never validate-gtdb kb/communities/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000433-gtdb
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000433-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000433
  command: just --verbose --no-dotenv --color never validate-gtdb-domain kb/communities/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000433-domain
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000433-scalars
  name: validate-scalars
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000433
  command: just --verbose --no-dotenv --color never validate-scalars kb/communities/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000433-scalars
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000433-history
  name: validate-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000433
  command: just --verbose --no-dotenv --color never validate-history history/records/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000433-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000433-new-history
  name: new-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000433
  command: just --verbose --no-dotenv --color never new-history --kind record --slug
    Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium --target-root kb/communities
    --event EDIT --outcome changed --sections taxonomy,curation_history --actor-name
    codex --model gpt-6 --agent-tool codex --issue https://github.com/CultureBotAI/CommunityMech/issues/2848
    --summary 'Add three bounded nitrifier-enrichment genus-reference correspondences'
    --details 'Only Nitrosospira, Nitrobacter and Legionella reference blocks/statuses
    and two native events changed. Their 16/16, 17/17 and 5067/5375 reference populations
    do not identify exact study MAG assemblies or certify pathogenicity. Preserve
    the 64-MAG starting enrichment, source abundances, PARTIAL guild handoff, anoxic
    ammonia accumulation, delayed aerobic removal, source aliases and culture/redox/expression
    limits. Current graph, quotations, old history and historical needs_research remain
    intact. Partial technical diagnostic, scientific_review:false, on frozen M5 e83c687c.
    Actual apply receipt .temp/gtdb-code006-20261115/genus-nine-433-applied-m5-001/receipt.json
    sha256:d442707388523e63775ed524b9fd7bd59f8134bb4bc1f45e4735847531626b67.'
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000433-new-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000433-terms
  name: validate-terms
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000433
  command: just --verbose --no-dotenv --color never validate-terms kb/communities/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000433-terms
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000474-schema
  name: validate
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000474
  command: just --verbose --no-dotenv --color never validate kb/communities/Whale_Fall_Vallitalea_Trichloromonas_Chitin_EET_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000474-schema
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000474-strict
  name: validate-strict
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000474
  command: just --verbose --no-dotenv --color never validate-strict kb/communities/Whale_Fall_Vallitalea_Trichloromonas_Chitin_EET_Consortium.yaml
    --out .temp/gtdb-code006-20261115/genus-nine-474-run-strict-001/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000474-strict
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000474-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000474
  command: just --verbose --no-dotenv --color never validate-gtdb kb/communities/Whale_Fall_Vallitalea_Trichloromonas_Chitin_EET_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000474-gtdb
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000474-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000474
  command: just --verbose --no-dotenv --color never validate-gtdb-domain kb/communities/Whale_Fall_Vallitalea_Trichloromonas_Chitin_EET_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000474-domain
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000474-scalars
  name: validate-scalars
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000474
  command: just --verbose --no-dotenv --color never validate-scalars kb/communities/Whale_Fall_Vallitalea_Trichloromonas_Chitin_EET_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000474-scalars
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000474-history
  name: validate-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000474
  command: just --verbose --no-dotenv --color never validate-history history/records/Whale_Fall_Vallitalea_Trichloromonas_Chitin_EET_Consortium
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000474-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000474-new-history
  name: new-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000474
  command: just --verbose --no-dotenv --color never new-history --kind record --slug
    Whale_Fall_Vallitalea_Trichloromonas_Chitin_EET_Consortium --target-root kb/communities
    --event EDIT --outcome changed --sections taxonomy,curation_history --actor-name
    codex --model gpt-6 --agent-tool codex --issue https://github.com/CultureBotAI/CommunityMech/issues/2848
    --summary 'Add two bounded whale-fall isolate genus-reference correspondences'
    --details 'Only Vallitalea and Trichloromonas reference blocks/statuses and two
    native events changed. Reference populations 14/16 and 8/8 are not isolate genomes;
    source partial-16S identification does not establish assemblies. Canonical null
    stock fields remain unchanged despite source sp2/sp17 designations, retained under
    issue 2872. Preserve sediment enrichment versus defined coculture, separate substrate/current
    assays and acetate amendment versus chitin-derived transfer. All biological statements,
    quotations and old history are unchanged; no new reciprocal-benefit certification.
    Partial scientific_review:false diagnostic on frozen M5 e83c687c. Actual apply
    receipt .temp/gtdb-code006-20261115/genus-nine-474-applied-m5-001/receipt.json
    sha256:ee3ea76c83a6c8db170840dbe5675b34a556a7024b00e57e0242a8fc17c99b85.'
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000474-new-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000474-terms
  name: validate-terms
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000474
  command: just --verbose --no-dotenv --color never validate-terms kb/communities/Whale_Fall_Vallitalea_Trichloromonas_Chitin_EET_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000474-terms
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000403-schema
  name: validate
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000403
  command: just --verbose --no-dotenv --color never validate kb/communities/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000403-schema
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000403-strict
  name: validate-strict
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000403
  command: just --verbose --no-dotenv --color never validate-strict kb/communities/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom.yaml
    --out .temp/gtdb-code006-20261115/genus-nine-403-run-strict-001/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000403-strict
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000403-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000403
  command: just --verbose --no-dotenv --color never validate-gtdb kb/communities/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000403-gtdb
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000403-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000403
  command: just --verbose --no-dotenv --color never validate-gtdb-domain kb/communities/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000403-domain
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000403-scalars
  name: validate-scalars
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000403
  command: just --verbose --no-dotenv --color never validate-scalars kb/communities/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000403-scalars
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000403-history
  name: validate-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000403
  command: just --verbose --no-dotenv --color never validate-history history/records/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000403-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000403-new-history
  name: new-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000403
  command: just --verbose --no-dotenv --color never new-history --kind record --slug
    Choysum_SynLAV_DEHP_Rhizobacterial_SynCom --target-root kb/communities --event
    EDIT --outcome changed --sections taxonomy,curation_history --actor-name codex
    --model gpt-6 --agent-tool codex --issue https://github.com/CultureBotAI/CommunityMech/issues/2848
    --summary 'Add five source-scoped SynLAV genus-reference correspondences' --details
    'Only five approved genus-reference blocks/statuses and two native events changed.
    Keep L11, L29, L75, L44 and L115 distinct, bound separately to main text and Table
    S2; no exact species or stock-genome inference. Reference fractions 859/860, 17956/25706,
    449/610, 514/514 and 450/453 are not abundance or persistence measurements. Preserve
    source-attributed phylum errors as quotations, individual screens versus pots,
    equal OD versus viable counts, ASV detection limits and the ten-day versus two-week
    discrepancy. Prior full review and issues 2535/1311/2534/1996 remain unresolved;
    all biology and old history remain exact. Partial scientific_review:false diagnostic
    on frozen M5 e83c687c. Actual apply receipt .temp/gtdb-code006-20261115/genus-nine-403-applied-m5-001/receipt.json
    sha256:5a10c1f293997c2949aac60ccef13a904b21a281cf4558fd61d05a712ac2cfe6.'
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000403-new-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000403-terms
  name: validate-terms
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000403
  command: just --verbose --no-dotenv --color never validate-terms kb/communities/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000403-terms
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
evidence:
- evidence_id: 000415-schema
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-415-run-schema-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000415-strict
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-415-run-strict-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000415-gtdb
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-415-run-gtdb-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000415-domain
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-415-run-domain-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000415-scalars
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-415-run-scalars-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000415-history
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-415-run-history-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000415-new-history
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-415-run-new-history-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000415-terms
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-415-run-terms-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000415-paper
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/41745484/
  locator: Retained community characterization and Methods 3.1-3.2/3.4; exact bound
    primary_contexts
  support: supports
  summary: The selected bacterial genera describe enrichment fractions without formal
    stock identities. The methylotroph composition and culture inoculum are distinct
    quantities.
  accessed_at: '2026-11-15T09:02:03.738836Z'
- evidence_id: 000415-database
  kind: database
  reference: reports/gtdb-code006-20261115/genus-nine-415-source-evidence-001.json
  locator: occurrences[taxonomy_index=2,3,4,5], full native_result and authority rows
  support: supports
  summary: Leptolyngbya 13/24, Methylotuvimicrobium 8/8, Methylophaga 45/45 and Methylonatrum
    1/1 are reference-genus populations. The first is a narrow majority, and the last
    rests on one reference genome.
  accessed_at: '2026-11-15T09:02:03.738836Z'
- evidence_id: 000415-application
  kind: record_content
  reference: .temp/gtdb-code006-20261115/genus-nine-415-applied-m5-001/receipt.json
  locator: Actual accepted before/after and complete source input binding
  support: supports
  summary: The guarded transition adds only four declared blocks/statuses and two
    native inline events, preserving six descriptors, two eukaryotic exclusions and
    all biology.
  accessed_at: '2026-11-15T09:02:03.738836Z'
- evidence_id: 000415-prior
  kind: prior_review
  reference: reports/causal_graph_review/decisions/20261021-stage5-review-remediation.yaml
  locator: CommunityMech:000415, original 3e009885 to d3174165 chain; original batch4
    remains unchanged
  support: context_only
  summary: The historical source and biological limitations remain in force, including
    functional potential versus measured expression/exchange and the absence of a
    closed carbon balance.
  accessed_at: '2026-11-15T09:02:03.738836Z'
- evidence_id: 000477-schema
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-477-run-schema-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000477-strict
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-477-run-strict-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000477-gtdb
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-477-run-gtdb-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000477-domain
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-477-run-domain-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000477-scalars
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-477-run-scalars-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000477-history
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-477-run-history-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000477-new-history
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-477-run-new-history-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000477-terms
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-477-run-terms-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000477-paper
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/41882811/
  locator: Bound retained main-text consortium roster and stock contexts
  support: supports
  summary: The 19 experimental stocks comprise 13 bacteria and six fungi, summarized
    by six taxonomy descriptors. Sphingopyxis represents two stocks and Cupriavidus
    three; neither descriptor is one newly identified stock.
  accessed_at: '2026-11-15T09:02:03.738836Z'
- evidence_id: 000477-database
  kind: database
  reference: reports/gtdb-code006-20261115/genus-nine-477-source-evidence-001.json
  locator: occurrences[taxonomy_index=2,3]
  support: supports
  summary: Sphingopyxis 79/79 and Cupriavidus 199/199 support genus-reference correspondence
    only, not identity of the multiple experimental stocks summarized by each descriptor.
  accessed_at: '2026-11-15T09:02:03.738836Z'
- evidence_id: 000477-application
  kind: record_content
  reference: .temp/gtdb-code006-20261115/genus-nine-477-applied-m5-001/receipt.json
  locator: Actual accepted before/after and source bindings
  support: supports
  summary: Two declared blocks/statuses and two native events changed. Other status-key
    ordering is semantically unchanged; the existing Bacillus/Devosia blocks, fungal
    exclusions and Amesia note remain intact.
  accessed_at: '2026-11-15T09:02:03.738836Z'
- evidence_id: 000477-prior
  kind: prior_review
  reference: reports/causal_graph_review/decisions/20261020-stage2-fifteen-records-batch133.yaml
  locator: CommunityMech:000477 and immutable scientific decisions
  support: context_only
  summary: The historical experimental and graph boundaries remain unchanged. Later
    strict admission must compose with other independently accepted batch133 targets
    without replacing their proofs.
  accessed_at: '2026-11-15T09:02:03.738836Z'
- evidence_id: 000353-schema
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-353-run-schema-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000353-strict
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-353-run-strict-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000353-gtdb
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-353-run-gtdb-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000353-domain
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-353-run-domain-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000353-scalars
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-353-run-scalars-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000353-history
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-353-run-history-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000353-new-history
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-353-run-new-history-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000353-terms
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-353-run-terms-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000353-paper
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/42029028/
  locator: Bound main-text day-160 enrichment, MAG affiliation and metabolic-potential
    passages
  support: supports
  summary: MAG003 and MAG013 retain their Desulfosporosinus and Acididesulfobacillus
    genus affiliations. The source's 96% ANI result for MAG013 is separate from this
    crosswalk correspondence.
  accessed_at: '2026-11-15T09:02:03.738836Z'
- evidence_id: 000353-database
  kind: database
  reference: reports/gtdb-code006-20261115/genus-nine-353-source-evidence-001.json
  locator: occurrences[taxonomy_index=0,1]
  support: supports
  summary: The native genus populations are 32/32 and 3/3. They do not identify an
    experimental MAG assembly or add a species assignment.
  accessed_at: '2026-11-15T09:02:03.738836Z'
- evidence_id: 000353-application
  kind: record_content
  reference: .temp/gtdb-code006-20261115/genus-nine-353-applied-m5-001/receipt.json
  locator: Actual two-block/status and two-event transition
  support: supports
  summary: The accepted application preserves all MAG identifiers, evidence, cultivation
    conditions and biological claims outside the declared GTDB fields.
  accessed_at: '2026-11-15T09:02:03.738836Z'
- evidence_id: 000353-prior
  kind: prior_review
  reference: reports/causal_graph_review/decisions/20261006-urls-amd-proteome-batch52.yaml
  locator: CommunityMech:000353 historical needs_research and exact predecessor
  support: context_only
  summary: The historical carbon-flow limitations remain unresolved, including both
    MAGs' glycerol-to-acetate potential, residual acetate and minor acidogens.
  accessed_at: '2026-11-15T09:02:03.738836Z'
- evidence_id: 000440-schema
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-440-run-schema-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000440-strict
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-440-run-strict-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000440-gtdb
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-440-run-gtdb-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000440-domain
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-440-run-domain-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000440-scalars
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-440-run-scalars-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000440-history
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-440-run-history-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000440-new-history
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-440-run-new-history-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000440-terms
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-440-run-terms-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000440-paper
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/38865893/
  locator: Retained abstract, non-electrostimulated microbiota syntrophy sentence;
    exact literal newline preserved
  support: supports
  summary: Methanosarcina or Methanothrix are alternative proposed acetoclastic partners,
    with e-pili or acetate mechanisms. The abstract does not establish both as confirmed
    exchanging stocks.
  accessed_at: '2026-11-15T09:02:03.738836Z'
- evidence_id: 000440-database
  kind: database
  reference: reports/gtdb-code006-20261115/genus-nine-440-source-evidence-001.json
  locator: occurrences[taxonomy_index=1,2]
  support: supports
  summary: Methanosarcina 301/301 and Methanothrix 94/117 are genus-reference results.
    The latter population spans three GTDB genera and is not unanimous.
  accessed_at: '2026-11-15T09:02:03.738836Z'
- evidence_id: 000440-application
  kind: record_content
  reference: .temp/gtdb-code006-20261115/genus-nine-440-applied-m5-001/receipt.json
  locator: Actual accepted transition and source inputs
  support: supports
  summary: Two declared blocks/statuses and two native events changed; all six entries
    and unselected Bacteria-domain, Methanobacterium and unresolved Desulfoprunum
    states remain intact.
  accessed_at: '2026-11-15T09:02:03.738836Z'
- evidence_id: 000440-prior
  kind: prior_review
  reference: reports/causal_graph_review/decisions/20261006-three-records-batch37.yaml
  locator: CommunityMech:000440; old scientific and direction constraints
  support: context_only
  summary: The HYPOTHESIZED graph, 800 mV versus control distinction, anode/cathode
    MAG labels and missing operating conditions remain unchanged. The separate 455
    successor is not affected.
  accessed_at: '2026-11-15T09:02:03.738836Z'
- evidence_id: 000447-schema
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-447-run-schema-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000447-strict
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-447-run-strict-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000447-gtdb
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-447-run-gtdb-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000447-domain
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-447-run-domain-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000447-scalars
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-447-run-scalars-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000447-history
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-447-run-history-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000447-new-history
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-447-run-new-history-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000447-terms
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-447-run-terms-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000447-paper
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/42323145/
  locator: 'Retained primary abstract: temporal succession, multispecies Brocadia
    assemblage and model findings'
  support: supports
  summary: Earlier Kuenenia acclimation and later multispecies Brocadia dominance
    are temporal observations, not a defined two-isolate SynCom.
  accessed_at: '2026-11-15T09:02:03.738836Z'
- evidence_id: 000447-database
  kind: database
  reference: reports/gtdb-code006-20261115/genus-nine-447-source-evidence-001.json
  locator: occurrences[taxonomy_index=0,1]
  support: supports
  summary: Brocadia 39/39 and Kuenenia 4/4 are reference-genus populations. Candidatus
    source names and absent stock fields remain unchanged.
  accessed_at: '2026-11-15T09:02:03.738836Z'
- evidence_id: 000447-application
  kind: record_content
  reference: .temp/gtdb-code006-20261115/genus-nine-447-applied-m5-001/receipt.json
  locator: Actual accepted two-block/status and two-event transition
  support: supports
  summary: The application preserves temporal culture context, all source evidence
    and the computational interaction outside declared GTDB fields.
  accessed_at: '2026-11-15T09:02:03.738836Z'
- evidence_id: 000447-prior
  kind: prior_review
  reference: reports/causal_graph_review/decisions/20261021-stage5-review-remediation.yaml
  locator: CommunityMech:000447, 227362963f to 0ea86ed4 chain and immutable original
    batch8 disposition
  support: context_only
  summary: SMETANA auxotrophy and low/high-nitrogen model comparisons remain computational,
    without measured interspecies flux or newly certified assembly identities.
  accessed_at: '2026-11-15T09:02:03.738836Z'
- evidence_id: 000433-schema
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-433-run-schema-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000433-strict
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-433-run-strict-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000433-gtdb
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-433-run-gtdb-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000433-domain
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-433-run-domain-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000433-scalars
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-433-run-scalars-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000433-history
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-433-run-history-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000433-new-history
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-433-run-new-history-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000433-terms
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-433-run-terms-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000433-paper
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/41457319/
  locator: Bound inoculum MAG Results and Legionella phylogenetic/gene-content passages
  support: supports
  summary: Nitrosospira, Nitrobacter and Legionella are genus-level MAG descriptors
    within starting material yielding 64 MAGs, not a three-strain inoculum.
  accessed_at: '2026-11-15T09:02:03.738836Z'
- evidence_id: 000433-database
  kind: database
  reference: reports/gtdb-code006-20261115/genus-nine-433-source-evidence-001.json
  locator: occurrences[taxonomy_index=0,1,2]
  support: supports
  summary: Native genus populations are 16/16, 17/17 and 5067/5375. Legionella spans
    seven reference genera; no particular study MAG or pathogenicity is assigned.
  accessed_at: '2026-11-15T09:02:03.738836Z'
- evidence_id: 000433-application
  kind: record_content
  reference: .temp/gtdb-code006-20261115/genus-nine-433-applied-m5-001/receipt.json
  locator: Actual accepted three-block/status and two-event transition
  support: supports
  summary: The accepted application preserves all MAG notes, culture conditions, evidence,
    biological graph and prior history outside declared GTDB fields.
  accessed_at: '2026-11-15T09:02:03.738836Z'
- evidence_id: 000433-prior
  kind: prior_review
  reference: reports/causal_graph_review/decisions/20261007-four-records-batch78.yaml
  locator: CommunityMech:000433 scientific disposition and historical exact-hash/event
    facts
  support: context_only
  summary: The historical needs_research status, PARTIAL guild handoff, aerobic/anoxic
    differences and gene-expression limits remain unchanged. The separate 176 c2s5
    chain is preserved.
  accessed_at: '2026-11-15T09:02:03.738836Z'
- evidence_id: 000474-schema
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-474-run-schema-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000474-strict
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-474-run-strict-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000474-gtdb
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-474-run-gtdb-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000474-domain
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-474-run-domain-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000474-scalars
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-474-run-scalars-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000474-history
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-474-run-history-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000474-new-history
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-474-run-new-history-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000474-terms
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-474-run-terms-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000474-paper
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/42297039/
  locator: Bound isolation, partial-16S, reconstructed coculture and cultured-isolate
    passages
  support: supports
  summary: The source names Vallitalea sp2 and Trichloromonas sp17, distinct from
    the sediment enrichment. Their omitted canonical formal stock fields remain a
    separate finding under issue 2872.
  accessed_at: '2026-11-15T09:02:03.738836Z'
- evidence_id: 000474-database
  kind: database
  reference: reports/gtdb-code006-20261115/genus-nine-474-source-evidence-001.json
  locator: occurrences[taxonomy_index=0,1]
  support: supports
  summary: Vallitalea 14/16 across two reference genera and Trichloromonas 8/8 support
    genus correspondence only; partial 16S does not identify exact assemblies.
  accessed_at: '2026-11-15T09:02:03.738836Z'
- evidence_id: 000474-application
  kind: record_content
  reference: .temp/gtdb-code006-20261115/genus-nine-474-applied-m5-001/receipt.json
  locator: Actual accepted two-block/status and two-event transition
  support: supports
  summary: The guarded correction preserves both null stock fields and every scientific
    claim outside the declared mapping fields. It does not silently repair or retire
    the separate stock finding.
  accessed_at: '2026-11-15T09:02:03.738836Z'
- evidence_id: 000474-prior
  kind: prior_review
  reference: reports/causal_graph_review/decisions/20261020-stage2-fifteen-records-batch133.yaml
  locator: CommunityMech:000474 original decisions and current graph/source boundaries
  support: context_only
  summary: Sediment enrichment, isolate coculture and separate current/substrate assays
    remain distinct. Initial acetate amendment is not evidence of chitin-derived transfer
    or completed reciprocal mechanism.
  accessed_at: '2026-11-15T09:02:03.738836Z'
- evidence_id: 000403-schema
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-403-run-schema-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000403-strict
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-403-run-strict-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000403-gtdb
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-403-run-gtdb-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000403-domain
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-403-run-domain-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000403-scalars
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-403-run-scalars-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000403-history
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-403-run-history-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000403-new-history
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-403-run-new-history-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000403-terms
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-nine-403-run-terms-001/native.log
  accessed_at: '2026-11-15T09:02:03.738836Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000403-paper
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/42482240/
  locator: Selected main-text screen, inoculum, pot and targeted-ASV passages plus
    separately retained Table S2 stock rows
  support: supports
  summary: Table S2 separately identifies L11, L29, L75, L44 and L115. Source phylum
    errors remain attributed quotations rather than authority labels; supplement text
    is not merged into the article cache.
  accessed_at: '2026-11-15T09:02:03.738836Z'
- evidence_id: 000403-database
  kind: database
  reference: reports/gtdb-code006-20261115/genus-nine-403-source-evidence-001.json
  locator: occurrences[taxonomy_index=0,1,2,3,4], full native result and exact current
    authority labels
  support: supports
  summary: Flavobacterium 859/860, Pseudomonas 17956/25706, Sphingomonas 449/610,
    Rhodococcus 514/514 and Gordonia 450/453 support genus-reference correspondence
    for five distinct source stocks, without exact species or assembly assignment.
  accessed_at: '2026-11-15T09:02:03.738836Z'
- evidence_id: 000403-application
  kind: record_content
  reference: .temp/gtdb-code006-20261115/genus-nine-403-applied-m5-001/receipt.json
  locator: Actual accepted five-block/status and two-event transition
  support: supports
  summary: The guarded application preserves all stock names, exact current authority
    labels, source evidence, biological conditions and old history outside the declared
    GTDB fields.
  accessed_at: '2026-11-15T09:02:03.738836Z'
- evidence_id: 000403-prior
  kind: prior_review
  reference: reviews/structured/20261021T192924Z-choysum-synlav-record/review.yaml
  locator: Immutable prior full scientific review 8bc00677 and original batch15 chain
  support: context_only
  summary: Issues 2535, 1311, 2534 and 1996 remain separate. The prior review's source-routing,
    timing, persistence and biological limitations are not retired by a genus correspondence
    diagnostic.
  accessed_at: '2026-11-15T09:02:03.738836Z'
assessments:
- assessment_id: 000415-identity
  area: grounding
  topic: Enrichment descriptors are not named experimental isolates
  outcome: supported
  target_ids:
  - CommunityMech:000415
  evidence_ids:
  - 000415-paper
  - 000415-database
  - 000415-terms
  summary: All six source descriptors and both eukaryotic exclusions remain intact.
    The four selected bacterial genera retain absent stock/species identity; no genome
    or strain is inferred.
- assessment_id: 000415-population
  area: grounding
  topic: Narrow majority and small reference populations
  outcome: supported
  target_ids:
  - CommunityMech:000415
  evidence_ids:
  - 000415-database
  - 000415-gtdb
  - 000415-domain
  summary: The 13/24 Leptolyngbya majority across six reference genera is explicitly
    limited, not unanimous. Counts of 8/8, 45/45 and 1/1 do not measure community
    abundance or verify study genomes. The source's 50:40 methylotroph composition
    remains distinct from the 50:50 culture inoculum.
- assessment_id: 000415-provenance
  area: provenance
  topic: Bounded actual correction preserves historical science
  outcome: supported
  target_ids:
  - CommunityMech:000415
  evidence_ids:
  - 000415-application
  - 000415-prior
  - 000415-schema
  - 000415-strict
  - 000415-scalars
  - 000415-new-history
  - 000415-history
  summary: Only the approved mapping/status fields and native provenance changed.
    Main-assay 6% versus enrichment 3% salt, metagenomic potential, carbon-balance
    limits, quotes and the stage5 chain remain unchanged.
- assessment_id: 000477-identity
  area: grounding
  topic: Stock roster versus genus descriptors
  outcome: supported
  target_ids:
  - CommunityMech:000477
  evidence_ids:
  - 000477-paper
  - 000477-database
  - 000477-terms
  summary: The 19-stock roster is not collapsed into six organisms. The two selected
    genus descriptors retain their absent formal stock fields and source-specific
    multiple-stock scope.
- assessment_id: 000477-population
  area: grounding
  topic: Reference genus correspondence without stock-genome inference
  outcome: supported
  target_ids:
  - CommunityMech:000477
  evidence_ids:
  - 000477-database
  - 000477-gtdb
  - 000477-domain
  summary: The complete native 79/79 and 199/199 reference results do not establish
    any experimental stock's species, assembly, abundance or ecological contribution.
- assessment_id: 000477-provenance
  area: provenance
  topic: Preserved cross-kingdom scientific context
  outcome: supported
  target_ids:
  - CommunityMech:000477
  evidence_ids:
  - 000477-application
  - 000477-prior
  - 000477-schema
  - 000477-strict
  - 000477-scalars
  - 000477-new-history
  - 000477-history
  summary: The guarded mapping change preserves every biological statement, current
    graph, source quote and old history event. Existing fungal exclusions and the
    Amesia limitation remain separate from bacterial correspondence.
- assessment_id: 000353-identity
  area: grounding
  topic: MAG affiliation remains genus-scoped
  outcome: supported
  target_ids:
  - CommunityMech:000353
  evidence_ids:
  - 000353-paper
  - 000353-database
  - 000353-terms
  summary: MAG003 and MAG013 remain distinct source entities in an enrichment, not
    two cultured isolates. The paper's MAG013 ANI and GTDB-Tk provenance do not become
    an exact assembly assignment through this mapping.
- assessment_id: 000353-population
  area: grounding
  topic: Two genus populations with different denominators
  outcome: supported
  target_ids:
  - CommunityMech:000353
  evidence_ids:
  - 000353-database
  - 000353-gtdb
  - 000353-domain
  summary: Desulfosporosinus 32/32 and Acididesulfobacillus 3/3 support only their
    declared reference correspondences. The small three-genome denominator is retained
    explicitly.
- assessment_id: 000353-provenance
  area: provenance
  topic: Source and historical carbon-flow limits preserved
  outcome: supported
  target_ids:
  - CommunityMech:000353
  evidence_ids:
  - 000353-application
  - 000353-prior
  - 000353-schema
  - 000353-strict
  - 000353-scalars
  - 000353-new-history
  - 000353-history
  summary: Reinoculation days 32 and 86, pH conditions, PARTIAL carbon flux and unresolved
    transfer mechanisms remain unchanged. Native correspondence and gate success do
    not replace the historical scientific assessment.
- assessment_id: 000440-identity
  area: grounding
  topic: Alternative partners remain alternatives
  outcome: supported
  target_ids:
  - CommunityMech:000440
  evidence_ids:
  - 000440-paper
  - 000440-database
  - 000440-terms
  summary: Both descriptors retain genus-only identity and absent formal stocks. A
    database correspondence does not resolve the source's Methanosarcina-or-Methanothrix
    or e-pili-or-acetate alternatives.
- assessment_id: 000440-population
  area: grounding
  topic: Reference majority is not ecological mechanism
  outcome: supported
  target_ids:
  - CommunityMech:000440
  evidence_ids:
  - 000440-database
  - 000440-gtdb
  - 000440-domain
  summary: The 301/301 and 94/117 populations are reproduced with the native genus
    route. Neither establishes experimental partner identity, a MAG assembly match
    or electron transfer.
- assessment_id: 000440-provenance
  area: provenance
  topic: Abstract-only scope and original mechanisms preserved
  outcome: supported
  target_ids:
  - CommunityMech:000440
  evidence_ids:
  - 000440-application
  - 000440-prior
  - 000440-schema
  - 000440-strict
  - 000440-scalars
  - 000440-new-history
  - 000440-history
  summary: Actual application and native provenance are bound without a full-text
    electrode or assembly audit. No operating condition, graph direction, source quote
    or historical limitation was rewritten.
- assessment_id: 000447-identity
  area: grounding
  topic: Temporal genus assemblages remain unresolved below genus
  outcome: supported
  target_ids:
  - CommunityMech:000447
  evidence_ids:
  - 000447-paper
  - 000447-database
  - 000447-terms
  summary: The source's multiple Brocadia species and earlier Kuenenia assemblage
    are preserved. No formal stock, particular species or experimental assembly is
    assigned.
- assessment_id: 000447-population
  area: grounding
  topic: Reference denominators versus biological measurements
  outcome: supported
  target_ids:
  - CommunityMech:000447
  evidence_ids:
  - 000447-database
  - 000447-gtdb
  - 000447-domain
  summary: The 39/39 and 4/4 reference counts are separate from 44.7% source abundance,
    71.5% transcriptional contribution and 68% positive associations. The small Kuenenia
    denominator is not experimental replication.
- assessment_id: 000447-provenance
  area: provenance
  topic: Computational and historical boundaries remain intact
  outcome: supported
  target_ids:
  - CommunityMech:000447
  evidence_ids:
  - 000447-application
  - 000447-prior
  - 000447-schema
  - 000447-strict
  - 000447-scalars
  - 000447-new-history
  - 000447-history
  summary: The guarded correction preserves the stage5 chain, all previous scientific
    text and the lack of measured exchange. Abstract-only source access is explicit;
    actual native gate success is a separate technical result.
- assessment_id: 000433-identity
  area: grounding
  topic: MAG genus affiliations do not identify species or virulence
  outcome: supported
  target_ids:
  - CommunityMech:000433
  evidence_ids:
  - 000433-paper
  - 000433-database
  - 000433-terms
  summary: Genus authority, absent formal stocks and source MAG notes remain unchanged.
    Reference relationships and secretion genes do not establish a species or demonstrate
    pathogenicity.
- assessment_id: 000433-population
  area: grounding
  topic: Reference populations are separate from inoculum composition
  outcome: supported
  target_ids:
  - CommunityMech:000433
  evidence_ids:
  - 000433-database
  - 000433-gtdb
  - 000433-domain
  summary: Counts of 16/16, 17/17 and 5067/5375 are native genus correspondences,
    not the 64-MAG input denominator or source abundances of 45.96% and 9.73%. Legionella
    is explicitly non-unanimous.
- assessment_id: 000433-provenance
  area: provenance
  topic: Historical scientific predicates survive bounded correction
  outcome: supported
  target_ids:
  - CommunityMech:000433
  evidence_ids:
  - 000433-application
  - 000433-prior
  - 000433-schema
  - 000433-strict
  - 000433-scalars
  - 000433-new-history
  - 000433-history
  summary: Anoxic ammonia accumulation, delayed aerobic removal, aliases and culture/redox
    limits remain intact. The actual native application and appended provenance do
    not certify all scientific claims.
- assessment_id: 000474-identity
  area: grounding
  topic: Source isolates and unresolved canonical stock fields
  outcome: supported
  target_ids:
  - CommunityMech:000474
  evidence_ids:
  - 000474-paper
  - 000474-database
  - 000474-terms
  summary: Genus correspondence is compatible with source isolates sp2 and sp17 while
    leaving the exact formal-stock omission explicitly unresolved under issue 2872.
    No species or assembly assignment is introduced.
- assessment_id: 000474-population
  area: grounding
  topic: Non-unanimous Vallitalea reference population
  outcome: supported
  target_ids:
  - CommunityMech:000474
  evidence_ids:
  - 000474-database
  - 000474-gtdb
  - 000474-domain
  summary: The native 14/16 and 8/8 populations are reference evidence, not experimental
    stock genomes or measured exchange. The two-genus Vallitalea split remains visible.
- assessment_id: 000474-provenance
  area: provenance
  topic: Bounded mapping preserves separate assay and mechanism limits
  outcome: supported
  target_ids:
  - CommunityMech:000474
  evidence_ids:
  - 000474-application
  - 000474-prior
  - 000474-schema
  - 000474-strict
  - 000474-scalars
  - 000474-new-history
  - 000474-history
  summary: The actual transition preserves source quotes, topology, old history and
    acetate/current/substrate distinctions. Strict batch133 admission must remain
    disjoint from other completed targets, and no scientific issue is closed.
- assessment_id: 000403-identity
  area: grounding
  topic: Five source-local stocks retain genus-only scope
  outcome: supported
  target_ids:
  - CommunityMech:000403
  evidence_ids:
  - 000403-paper
  - 000403-database
  - 000403-terms
  summary: L11, L29, L75, L44 and L115 remain distinct SynLAV stocks. Rhodococcus
    and Gordonia authority-label qualifiers remain unchanged. No stock is assigned
    a species, exact assembly or source-phylum error.
- assessment_id: 000403-population
  area: grounding
  topic: Five different reference denominators and non-unanimous majorities
  outcome: supported
  target_ids:
  - CommunityMech:000403
  evidence_ids:
  - 000403-database
  - 000403-gtdb
  - 000403-domain
  summary: The complete native populations of 859/860, 17956/25706, 449/610, 514/514
    and 450/453 remain explicit. The separate L115 exact-ID row is not promoted to
    a stock-specific species match; reference majorities do not establish experimental
    phenotype or persistence.
- assessment_id: 000403-provenance
  area: provenance
  topic: Prior full science and separate supplement remain immutable
  outcome: supported
  target_ids:
  - CommunityMech:000403
  evidence_ids:
  - 000403-application
  - 000403-prior
  - 000403-schema
  - 000403-strict
  - 000403-scalars
  - 000403-new-history
  - 000403-history
  summary: The 72-hour individual 100 mg/L screen stays separate from 100 mg/kg pots,
    equal optical density from viable counts, and three LAV-ASVs from persistence
    of every stock. The ten-day Methods versus two-week Results discrepancy, source-attributed
    phylum quotes, prior review and historical cache provenance remain unchanged.
findings: []
actions: []
limitations:
- Partial technical diagnostic with scientific_review:false. Completion of these declared
  checks is not whole-record scientific approval, source-snippet validation, generated-site
  integration, final corpus QC or campaign completion.
- Every support/total count concerns the named-binomial reference population in crosswalk
  761d5537, not the study's stocks, assemblies, experimental replicates or community
  abundance. Existing taxon labels, strain fields, source notes and scientific uncertainty
  remain unchanged.
- Leptolyngbya 13/24 is a narrow majority spanning six reference genera. Methanothrix
  94/117, Legionella 5067/5375, Vallitalea 14/16 and the non-unanimous Choysum populations
  remain explicitly qualified; no majority vote resolves exact stock identity or mechanism.
- Primary coverage is limited to the source contexts and locators recorded for each
  target. Records 440 and 447 use retained abstracts; the other records use selected
  retained main-text passages, with Choysum Table S2 kept as a separate supplement.
  No new complete-paper, image, sequence or assembly review was performed.
- The whale-fall sp2/sp17 formal stock omissions remain separately owned by issue
  2872. Choysum's prior full review and issues 2535, 1311, 2534 and 1996 remain unchanged.
  No historical scientific finding or GitHub issue is closed by this diagnostic.
- Native reporting ran locally at 0e826fcf, source binding at 4c0046c6, and staging
  and actual M5 application/checks at e83c687c56beb7160be20a0db2439dab92cfdb67. The
  M5 native gate receipts record Python 3.13.2. Post-application checks are not a
  clean-tree run. Crosswalk file mtime is not a release identifier; the local NCBI
  authority observation is stat-bound rather than a full database checksum.
- Source-binding attempt 001 refused a literal newline mismatch in record 440 under
  issue 2878. Its failed evidence is preserved separately. Corrected attempt 002 passed
  a fresh 410 source-binding canary followed by the full source-only binding before
  candidate staging.
- Native term validation is reported literally; its output does not establish an assertion
  denominator. Strict successor admission, historical caller composition and final
  integrated QC remain separate downstream checks. A complete immutable input checkpoint
  is required before any historical caller adaptation.
links:
- https://github.com/CultureBotAI/CommunityMech/issues/2848
- https://github.com/CultureBotAI/CommunityMech/issues/2878
- https://github.com/CultureBotAI/CommunityMech/issues/2872
- https://github.com/CultureBotAI/CommunityMech/issues/2535
- https://github.com/CultureBotAI/CommunityMech/issues/1311
- https://github.com/CultureBotAI/CommunityMech/issues/2534
- https://github.com/CultureBotAI/CommunityMech/issues/1996
- https://github.com/CultureBotAI/CommunityMech/pull/2853
```
