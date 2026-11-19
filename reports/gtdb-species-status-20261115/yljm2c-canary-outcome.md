# YL-JM2C shared-engine canary

The isolated M5 execution persisted the accepted CommunityMech:000554 correction, passed all eight scoped native commands, and saved a complete diagnostic assessment within its explicitly partial scope. The [native YAML](../../reviews/structured/20261115T063325Z-yljm2c-species-reference-diagnostic/review.yaml) and [derived Markdown](../../reviews/structured/20261115T063325Z-yljm2c-species-reference-diagnostic/review.md) retain `scientific_review: false`. This canary verifies the shared stage/application/check/review persistence path; it does not complete a full scientific review or corpus QC.

Actual M5 application and gate revision was `c86a898df4c5206efc683da9394d3eb68d06661b`, under frozen Python 3.13.2. Private staging used local Python 3.13.12 at `61d0e0a91d7135f2521faf5c15f4f48fc3b2c070`. The additive review builder was published in `3ad0b7e0946a9be80b58875dfee22e8011cd47f1` and copied without changing M5 HEAD; its exact bytes are inspected inputs. These identities remain distinct from later integration revisions.

The [actual application receipt](yljm2c-001-apply.raw.json), SHA256 `4158807ea699f981ed96fdb3e966878f95df84ea1c0b1682d9541305646e56d9`, connects original SHA256 `e70a8434bd8db3852302899814f08a19d97c0e9d73a6636cb7715295642fdf59` to current SHA256 `dd333d36e5ed9169cf2ddda11bc5d53466dc838895bfee5a8d71336f9c360673`. The only canonical changes are one native GTDB block, UNRESOLVED → GROUNDED status, and two appended native events. The [new native sidecar](../../history/records/Rhizorhabdus_Wittichii_YL_JM2C_BDE47_Dioxygenase_Isolate_Baseline/2026-11-15T062832Z-codex-867208.yaml) records this bounded correction. Existing biological claims, stock identity, source quotations and the open RwTfdB structural-determinants discussion remain unchanged.

The [source proof](yljm2c-source-evidence-001.json) binds primary PMID42364169, the NCBI species descriptor 160791, and row 7583 of the pinned crosswalk. The native route is `ncbi_id`, with seven reference genomes and a reported majority fraction of 0.86. It is a species-reference correspondence: no membership of the study stock YL-JM2C among those seven genomes, exact numerator, formal nomenclatural event, or stock genome accession is inferred. PRJNA1397584 is a BioProject. The primary source's ANI-based study-stock interpretation and the crosswalk population are assessed separately.

| Native command | Actual result | Retained output |
| --- | --- | --- |
| validate | Passed, exit 0 | [schema](yljm2c-001-schema.log.txt) |
| validate-strict | One file, zero errors, exit 0 | [strict](yljm2c-001-strict.log.txt) |
| validate-gtdb | One file, zero incoherent/malformed/conflicting blocks, exit 0 | [GTDB](yljm2c-001-gtdb.log.txt) |
| validate-gtdb-domain | One file, zero contradictory lineages, exit 0 | [domain](yljm2c-001-domain.log.txt) |
| validate-scalars | One file, zero truncated scalars, exit 0 | [scalars](yljm2c-001-scalars.log.txt) |
| new-history | One sidecar persisted, exit 0 | [history creation](yljm2c-001-new-history.log.txt) |
| validate-history | No issues, exit 0 | [history validation](yljm2c-001-history.log.txt) |
| validate-terms | Validation passed, exit 0 | [terms](yljm2c-001-terms.log.txt) |

The [retained-input audit](yljm2c-retained-inputs-audit-001.json) verifies 69 inputs totaling 4,898,360 bytes, native review validation and exact Markdown reproduction. Saved YAML is 28,024 bytes, SHA256 `ade47990493f73b974fdd588ec5bf0e194de44f4bef9dc9793c48b6ae466bef3`; Markdown is 37,511 bytes, SHA256 `d53f9f2c73a3a1e709a9a69d06bf23648476ee6a5fdb1f8391a33771d7577edc`. A private immutable input namespace is retained on M5 and mirrored locally: 71 files totaling 4,963,895 bytes, manifest SHA256 `83aee6caa3c01d5da8aa524bc3e58f00a0ded8307070f71f5bcb5ad0a7043737`. Native snapshot verification passed before later helper evolution.

The [public export receipt](yljm2c-export-audit-001.json) records the captured implementation and configuration hashes. All [27 artifact hashes](yljm2c-public-files.sha256) match their [persisted files](yljm2c-public-files-verified.log.txt). The [successor manifest](yljm2c-001-successor.json) explicitly links each gate's public receipt/log/exit to the original raw paths and hashes inspected by the saved review. Export/capture controls passed 28 tests; native gate and source evidence remain the basis for the assessment.

Independent outcome review removed an unbound release label from this narrative under the source-provenance issue [#2849](https://github.com/CultureBotAI/CommunityMech/issues/2849). This package identifies crosswalk bytes by SHA256; it does not bind upstream release metadata. The executed source proof, application and saved review were unchanged.

Strict historical-successor admission and combined generated-page rendering remain integration tasks. This canary does not automatically approve another route, close issues, or certify the remaining assigned records. New status-only or higher-rank routes require their own accepted source plans and real canaries before batch execution.
