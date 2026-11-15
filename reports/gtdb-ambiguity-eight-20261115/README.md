# Eight-record ambiguity and correspondence batch

This branch prepares records 400, 499, 500 and 505–509 for the unchanged guarded
GTDB correction workflow. Its twenty selected occurrences cover four pesticide
and biofilm ambiguities plus sixteen hexamine correspondences. Record 505 is the
first application canary: one species-reference correspondence and one ambiguous
genus descriptor. Its [completed bounded canary checkpoint](505-canary-outcome-002.md)
now binds the actual M5 write, saved partial assessment, complete verified inputs
and passing historical controls. The [other seven completed applications](seven-record-outcome-001.md)
have their own saved partial assessment, complete checkpoint, 56 native checks
and 119 passing evidence controls. All eight bounded taxonomy corrections are
complete on this branch; full scientific approval is not claimed.

The source judgments come from the previously reviewed
[three-record plan](../phase2-completion-20261115/status-biofilm-pesticide-three-source-context-001.yaml)
and [hexamine plan successor](../phase2-completion-20261115/hexamine-five-source-context-002.yaml).
The latter changes only the YAML representation of the final completion-limit
scalar. Its malformed original remains intact. All stock identities, experimental
distinctions, reference-population limits and historical scientific blockers
remain in the copied judgments. These are partial technical preparations, not
new full-paper assessments.

Independent review found a separate capture race in the new preparation adapter
([#2879](https://github.com/CultureBotAI/CommunityMech/issues/2879)). The original
draft is preserved at `17760e55`; the repaired helper at `a5c0e6d8` parses and
hashes one captured byte sequence per input and rechecks every capture. Five
full-producer controls passed, including actual transient and persistent changes
to source judgments and route status, restored positives and an altered accepted
plan. The first actual preparation then refused the older plan's invalid YAML
before creating a config ([#2880](https://github.com/CultureBotAI/CommunityMech/issues/2880)).
The additive v2 helper binds both plan versions and the previously executed
helper. All ten controls across both helpers passed; Black and Ruff passed.
Neither the native binder nor any curation/validation policy changed.

The 505 native route canary ran at `3bdbc774`, persisted a nonempty report and
verified unchanged inputs. It preserves SRCHD05's exact-ID 18-reference-genome
correspondence and all three ordered genus alternatives for SRCHD06. After
verification, the same reporter captured all eight whole records. The corrected
505 preparation persisted its config and passed the native source binder before
the eight-record preparation and binding ran. The binders verify current local
NCBI labels/ranks and literal source anchors, with database identity recorded by
file stat rather than a content checksum. No genome placement of a study stock
is inferred.

| Retained native-recorder run | Result | Log SHA-256 |
|---|---|---|
| `ambiguity-eight-505-route-canary-001` | Exit 0; 54,542 bytes | `e0e7ee13562e2278a9aa3ec9d2180c22b631ce6089d5d62c7a979c0c123a78c6` |
| `ambiguity-eight-routes-001` | Exit 0; 529,840 bytes | `1ef40997cb36c77b71c13c5a3597e8622b54aa4638487dcb16ddf3a750bf681b` |
| `ambiguity-eight-capture-controls-001` | Exit 0; five tests | `ae5fba65d921fdac1d07df2d4c0621785efbaf2180961712ad6328bf7b56e222` |
| `ambiguity-eight-505-config-001` | Exit 1; malformed retained plan; no output | `b986325daa79e18a4d346336b1cf6507b6071c262e82d1d0761dcf8e6fe95635` |
| `ambiguity-eight-capture-controls-002` | Exit 0; ten tests | `4b08818924ebd60ded35d0879fdd3c76917acc70e7165c750d0228df5f006100` |
| `ambiguity-eight-505-source-binding-001` | Exit 0; 24,300 bytes | `e473b6dd243b3b1b0a60944d8f937190d2a552d44a73659377876e962f42442d` |
| `ambiguity-eight-source-binding-002` | Exit 0; 175,942 bytes | `efc851cec1476ecfd204bf5f6e0ce5e898a247a4b6feab62498039b777b2667f` |

Commands, exact revisions, working-tree disclosures, logs and exits remain under
`.temp/phase2-schema-20261115/`. The linked canary outcome records its reviewed
candidate, actual M5 application, eight native checks, immutable partial review,
complete verified checkpoint and actual strict historical proof. Batch 10/137/139 scientific predicates and
mutation controls must survive caller adaptation; old ledgers remain immutable.
