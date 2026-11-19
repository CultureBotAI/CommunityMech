# Five-record integration checkpoint

The integration branch now includes the independently reviewed PPCP420,
MWF001443, GENIA352, HAMBI423 and Wetland471 changes. The record evidence is
combined at `acb0d4b95c4b4ec7e3b2837ee2bcb611a5de08d6`; Wetland's final
production admission is added at
`0286c0da1c05668c992c52262068677531cd658a`.

| Reviewed leaf | Integration | Evidence and retained limits |
| --- | --- | --- |
| PPCP420 `3997d822`, draft PR2921 | `170a414a` | [Outcome](../gtdb-ppcp420-domain-20261115/README.md): bacterial reference correspondences and affirmative fungal-domain evidence; 81-input saved assessment and complete 83-file checkpoint |
| MWF001443 `ff35f71c`, draft PR2917 | `280ceccf` | [Outcome](../gtdb-genia-hambi-mwf-20261115/mwf443-outcome-001.md): two reference blocks, complete alternative sets and retained stock/causal limits; 89-input assessment and complete 91-file checkpoints |
| GENIA352/HAMBI423 `9c851e74`, draft PR2917 | `acb0d4b9` | [Outcome](../gtdb-genia-hambi-mwf-20261115/genia-hambi-outcome-001.md): 127-input assessment, complete 129-file checkpoints and 54 public artifacts; existing C6 dependency was already integrated and was not duplicated |
| Wetland471 identity `38f11cfa`, draft PR2906 | `faad27a2` | [Identity outcome](../gtdb-wetland-identity-20261115/identity-outcome-001.md): source identity correction and retained roster/graph findings; maintained intermediate record SHA256 `b3234d5f041636195f4c9867aaccd0df802d22ff5f2fbc28b904868ee02b901a` |
| Wetland471 mapping `42b893a0`, draft PR2919 | `e18480ad` | [Mapping outcome](../gtdb-wetland-mapping-20261115/mapping-outcome-002.md): 84-input assessment, complete 86-file checkpoint and 27 public mapping artifacts; exact missing identity-log recovery retained under issue2922 |
| Wetland471 production admission `d976d7c6`, draft PR2923 | `0286c0da` | [Admission outcome](../gtdb-wetland-mapping-20261115/production-admission-001.md): original record → maintained identity intermediate → actual mapping proof, with current biological assertions and other batch133 admissions preserved |

All record applications and immutable assessments retain their actual frozen M5
execution revisions. Cherry-picking their public evidence does not rebind those
receipts to the integration revision. The new taxonomy diagnostics remain
partial with `scientific_review: false`; Wetland's identity assessment retains
its `needs_curation` findings. Reference genome populations do not identify
experimental stock genomes. Wetland's measured 16-reference comparison applies
to its identity intermediate, not a new comparison of the final mapped record.

The following checks ran on clean integration revisions. Unique recorder
triplets are retained in `.temp/phase2-schema-20261115/`; all reported logs were
read after completion. These are overlapping focused suites, not a summed count
of distinct tests or a full-corpus QC run.

| Revision / recorder | Actual result | Raw log SHA256 |
| --- | --- | --- |
| `acb0d4b9` / `integration-genia-hambi-mwf-proof-001` | 51 passed, 425 deselected, 12 warnings; 40.88s | `08798cc1860d959b67fd979cd32816b2b0f299367a38eab363a4c368172f06db` |
| `acb0d4b9` / `integration-ppcp-wetland-callers-001` | 94 passed, 14 warnings; 61.51s | `c3ce170c60977bb65c10c67022ca29b1fbaf490a660cad0a7f963fc7156ab633` |
| `acb0d4b9` / `integration-five-record-lint-001` | Black 788 files, Ruff and mypy 52 sources passed | `d0c5ad3d9da98cf166d32c79f73ac17043159661bb9b845a2fda191c0a0ad236` |
| `0286c0da` / `integration-wetland-production-001` | 9 passed, 14 warnings; 37.79s; production admission, batch133 and fetch controls | `fbfaec269f307f6b9bead4b9accbc4578c815dee9756c7f9c7eb7ee3a2954b51` |

The independently reviewed production leaf also passed native lint over 790
files and mypy over 52 sources. Its exact source changes were cherry-picked
without conflicts; the final clean integration suite above exercised them
together. No native curation helper, schema, reference-matching rule or
scientific threshold was relaxed.

A fresh captured-input inventory at `acb0d4b9` reports 104 changed and 22
unchanged records among the historical 126 assignments. The retained JSON is
`.temp/phase2-schema-20261115/assignment-progress-acb0d4b9-001.json`, SHA256
`df985c82bfc4681507a84d8df382a65bc9e162762637a8e9606cbbf4330664c7`.
This compares record bytes only. Changes are not scientific approvals, and
pending worktrees are excluded. The later production admission changes no
canonical record.

Full combined M5 QC, regenerated products, separate measured reference
validation and explicit scientific finding dispositions remain required.
Later aggregate gates remain not run until actually completed. Pending
private-input transfers retain their automatic-approval refusals and have not
been retried through another route. The all-record scientific campaign has not
resumed. This checkpoint does not claim Phase2 completion or authorize a merge.
