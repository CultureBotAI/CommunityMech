# Cache inputs of the six saved scientific reviews

The [exact manifest](review-cache-input-manifest.json) contains **five distinct
cache paths and nine direct review/path occurrences** across all six saved
reviews. The [native input-row capture](review-cache-input-lines.txt) retains
the original file/line locations and adjacent saved hashes; the
[bundle manifest](review-cache-bundle-sha256.txt) pins all six reviewed YAML
files. No old review or source was changed.

| Review | Direct `references_cache/` inputs |
|---|---:|
| EcoFAB canary | 2 |
| LBNL Switchgrass | 2 |
| Yolo soil | 1 |
| Dopamine SynCom | 1 |
| LBNL environment addendum | 0 |
| Post-curation delta | 3 |

The environment addendum directly references retained primary XML under
`.temp/` and the earlier LBNL review. Both of that earlier review's cache paths
are included in the union. This is an exact inventory of named cache inputs,
not a transitive inventory of every research artifact.

The union is `PMID_36472419.txt`, `pmc_full_pmid_36472419.txt`,
`PMID_40920748.md`, `doi_10.1126_sciadv.adg7888.md`, and
`PMID_42660928.md`, all under `references_cache/`.

Each occurrence retains its saved SHA-256 independently. Baseline hashes were
read from Git commit `e9ae9dee132ab210c87f76460c5d6247af9ea99c` using
`git show <revision>:<path> | shasum -a 256`. The first source inventory used
native `rg -n -A 2 '^  - path: references_cache/'` over the six explicit YAML
paths; every match was inspected within its `source.inputs` block. The
environment addendum's full `source` block was inspected to confirm zero
direct cache entries. The manifest transcribes those native outputs; no new
helper or M5 source code was introduced.

Four historical occurrences differ from the C2 baseline because the three
article-cache headers were corrected before C2 and assessed by the saved
post-curation delta. These are preserved predecessor identities, not runtime
mutations. The final cache audit must intersect its actual changed paths with
all five union paths and compare actual bytes with the baseline hashes.
Report runtime overlap separately from those historical differences and from
the scientific review's conclusions. This manifest alone makes no final
runtime-overlap claim.
