# JMP134 canary outcome

The isolated M5 canary persisted the accepted correction to CommunityMech:000555 and passed all eight scoped native commands. Its [native review](../../reviews/structured/20261115T055930Z-jmp134-gtdb-diagnostic/review.yaml) and [derived Markdown](../../reviews/structured/20261115T055930Z-jmp134-gtdb-diagnostic/review.md) are complete within their partial scope, with `scientific_review: false`. This is an exact-stock database correspondence and application assessment; the existing biological claims were preserved.

Actual execution revision was `f95ad0d731bc53634336ae7b794a7b23aa96a3c0`, Python 3.13.2. Native private staging occurred earlier at `99e82a494d02201b72c8b85ed7c5e63f3390cdf0` under local Python 3.13.12. The additive diagnostic builder was published in `aae62e4c` and copied to M5 without changing its execution HEAD; its exact `faae6fb9` bytes are one of the 66 inspected inputs. None of these revisions is relabelled as a later integration revision.

The [byte-identical actual application receipt](jmp134-001-apply.raw.json), SHA256 `d6d0af2d04990111aca3e7dd6c7437c3243e1bdb6f33f5afcc91feb857e83010`, connects original record SHA256 `429964cbf945c41b2e89b57a072718158cf674e03786ef34b1ef96fe9247995e` to accepted current SHA256 `fede5211f0911d1a0543f1e19f8c53bf4c6dfc4ee306a6a3b8ee5d184ed7e786`. The only changes are the native GTDB block, GROUNDED status and two appended native inline events. A [new native sidecar](../../history/records/Cupriavidus_Necator_JMP134_24DBP_Hydroxylase_Isolate_Baseline/2026-11-15T055420Z-codex-edf3d2.yaml), SHA256 `4ce51b644bdab92f1ea7702ce4261045097c4a03280dc483d62aa8695637596a`, records the actual application.

| Native command | Actual result | Retained output |
| --- | --- | --- |
| validate | Passed, exit0 | [schema](jmp134-001-schema.log.txt) |
| validate-strict | One file, zero errors, exit0 | [strict](jmp134-001-strict.log.txt) |
| validate-gtdb | One file, zero incoherent/malformed/conflicting blocks, exit0 | [GTDB](jmp134-001-gtdb.log.txt) |
| validate-gtdb-domain | One file, zero contradictory lineages, exit0 | [domain](jmp134-001-domain.log.txt) |
| validate-scalars | One file, zero truncated scalars, exit0 | [scalars](jmp134-001-scalars.log.txt) |
| new-history | One new sidecar persisted, exit0 | [history creation](jmp134-001-new-history.log.txt) |
| validate-history | No issues, exit0 | [history validation](jmp134-001-history.log.txt) |
| validate-terms | Validation passed, exit0 | [terms](jmp134-001-terms.log.txt) |

The [source proof](jmp134-source-evidence-001.json) preserves the exact one-genome crosswalk row, native `ncbi_id` result, NCBI synonym query and primary-source locators. It does not infer other stocks, species-wide genome counts, a formal nomenclatural event or a genome accession. The original open tfdBI/tfdBII expression/flux question remains unchanged.

The saved YAML is 26,464 bytes, SHA256 `7355641ae0d308b57b533c877132a4f3953a03cab1b3c2aae3424076b6806d4f`; Markdown is 35,264 bytes, SHA256 `9486cbdc3ae569f4c2d466b446e079c39e7e2074a9b61d36082241791e6f6bf3`. The [retained-input audit](jmp134-retained-inputs-audit-001.json) verified all 66 inputs (4,838,169 bytes), native schema validation and exact Markdown derivation. The [public export receipt](jmp134-export-audit-001.json) binds exporter/auditor/redactor implementations and [all 27 artifact hashes](jmp134-public-files.sha256), verified against the [persisted outputs](jmp134-public-files-verified.log.txt). The [successor manifest](jmp134-001-successor.json) binds the exact actual receipt, source proof, sidecar and saved pair.

The application guard and writer classification passed 22 tests. Reusable evidence capture/export passed 27 controls, including four overlapping-input cases that first failed before the [#2860](https://github.com/CultureBotAI/CommunityMech/issues/2860) correction. [#2863](https://github.com/CultureBotAI/CommunityMech/issues/2863) added direct inspection of the actual applier bytes before the first saved review; the earlier unexecuted builder snapshot remains retained. The fixed 000555 successor passed 16 actual proof, semantic and mutation/restoration controls. These checks do not substitute for scientific evidence.

The shared batch147 caller and combined generated-page rendering remain integration tasks. The strict species guard supplies the original 68699871 bytes for the historical 000555 mutation sample; it grants no allowance to another changed record. Other assigned records, full corpus QC and the broader scientific campaign remain separate work. No issue is automatically closed by this canary.
