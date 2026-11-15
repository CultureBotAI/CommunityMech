# BR1 exact-genome correction and scoped M5 canary

The BR1 record now identifies its GTDB species as `Microbacterium sp002812725`.
The exact NCBI assembly pair, strain, taxon and BioSample identify BR1; official
GTDB history explicitly supplies the R220 assignment. The correction replaces
the old `Microbacterium lacus` block and its one opening-description identifier.
It preserves the original NCBI stock, experimental claims, quotations, graph,
discussion and prior history. See the [source assessment](README.md) and
[frozen grounding proof](grounding-evidence-003.json).

The mapping is explicitly curated against a native crosswalk result of `None`.
That absence is not evidence for the chosen species: the separate exact-genome
authority chain supplies the support. No BR1 crosswalk majority or genome count
is claimed. The unrelated CJ77 row and GTDB species-cluster size are different
populations. `is_reclassified: true` retains its native label-difference meaning;
the note explicitly avoids claiming a formal species renaming.

The actual guarded application ran on M5 at
`56138e068c7b2d73d366fdcf9d6d95173cd599c6` with native Python 3.13.2. It consumed
the independently accepted candidate and staging receipt without restaging:

| Artifact | SHA-256 |
|---|---|
| Original record | `c0326c5cdaf678c922659c33dbe4fe1b5717be2bf79dab54d672f160574c0fe5` |
| Accepted and persisted record | `acdadd88a7f7e81eced8c1d229709ba94023dde7e7f72f3238f483685b4c2236` |
| Staging receipt | `809d1fc6884f93c51209e79aecb9ec54b82de3a907c2fce13aa02b8f6dc9408c` |
| Actual application receipt | `d1c902b14a80badaf1d3d84049200e800f3cc443cd58b261393b001c48e0321a` |
| Native history sidecar | `84d49b31a65a7efc90310d6a976fd7c784000b187029da7bb09688c549508c56` |

The [actual apply receipt](br1-apply-001.raw.json) is a byte-identical public
metadata copy. The [successor manifest](br1-successor-001.json) binds the source
proof, sidecar, saved review and exact permitted description substitution for the
separate batch144 lineage check. Historical reviews remain unchanged.
All 27 exported files match the frozen plan: [checksums](canary-public-files.sha256)
and [on-disk verification](canary-public-files-verified.log.txt).

All eight commands used the retained one-record launcher, with individual
plans, native logs, exits and input hashes:

| Native command | Result |
|---|---|
| `just validate` | Passed; no schema issues |
| `just validate-strict` | Passed; one file, zero errors; nonempty TSV verified |
| `just validate-gtdb` | Passed; zero incoherent blocks, malformed lineages or conflicts |
| `just validate-gtdb-domain` | Passed; zero contradictory lineages |
| `just validate-scalars` | Passed; zero truncated scalars |
| `just validate-terms` | Passed with labels checked |
| `just new-history` | Persisted exactly one new sidecar, with Codex attribution |
| `just validate-history` | Passed; no issues |

The immutable scoped diagnostic is saved as
[YAML](../../reviews/structured/20261115T053150Z-br1-gtdb-diagnostic/review.yaml)
and [derived Markdown](../../reviews/structured/20261115T053150Z-br1-gtdb-diagnostic/review.md).
Its 62 declared inputs and native Markdown derivation were verified. The YAML
SHA-256 is `2adc93fb4ea6d0386b873b1310c95c9121f997e3fcf5349961e1ca49ba50d214`;
the Markdown SHA-256 is `c8f69adc69d02aeed9068220f08465c3d09849018ac2f759fb274cb1adad8329`.
The accepted diagnostic builder was added without changing M5's execution HEAD;
its exact `2a21b29c48ff02641a812d98b5d177d9ce9981428b12b8a04b747ab3931c1b5f`
hash is one of those inputs.

This is a completed **scoped diagnostic**, with `scientific_review: false`,
partial record coverage and `pass_with_limitations`. It does not certify the
record's complete scientific content, claim-level references, corpus QC or
generated pages. Combined integration owns page regeneration and the strict
batch144 successor. Other work under [#2849](https://github.com/CultureBotAI/CommunityMech/issues/2849)
is separate.

The writer's 11 controls passed before application. After the independent
[#2858](https://github.com/CultureBotAI/CommunityMech/issues/2858) fixture-durability
finding, the controls use the byte-identical original from the historical base
already fetched by native CI. The combined 11 controls and seven writer-audit
tests passed locally, with 12 dependency deprecation warnings. These local tests
used Python 3.13.12; they are distinct from the actual M5 3.13.2 checks above.

Before public evidence publication, independent review found the exporter read
some files separately for verification and export
([#2860](https://github.com/CultureBotAI/CommunityMech/issues/2860)). The corrected
exporter captures the review and all inputs once, uses those bytes throughout,
and rechecks the entire snapshot before writing. Ten controls passed, including
source, log, exit, review, Markdown and schema changes that refuse publication,
followed by successful restoration. The original read-only plan remains retained;
no public artifact or saved review was overwritten.
