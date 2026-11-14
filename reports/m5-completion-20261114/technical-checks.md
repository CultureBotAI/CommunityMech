# M5 technical checks

All logs, exact exits and hash receipts are retained in [technical-evidence](technical-evidence/README.md).
Separate diagnostics do not repair failed aggregates; skipped checks are not passes.
The original baseline is 76aa644cd6803ea2c9545d4c704276ede219d354; each receipt records its actual revision and source status.

| Run | Status | Exit | Native stage counts |
|---|---|---:|---|
| [baseline-bracket-reference](technical-evidence/baseline-bracket-reference.receipt.json) | FAILED | 1 | FAILED: 1 |
| [bracket-regression-before](technical-evidence/bracket-regression-before.receipt.json) | FAILED | 1 |  |
| [canary](technical-evidence/canary.receipt.json) | PASSED | 0 | PASSED: 1 |
| [diagnostic-validate-gtdb-all](technical-evidence/diagnostic-validate-gtdb-all.receipt.json) | PASSED | 0 | PASSED: 1 |
| [diagnostic-validate-scalars-idiomatic](technical-evidence/diagnostic-validate-scalars-idiomatic.receipt.json) | PASSED | 0 | PASSED: 1 |
| [diagnostic-validate-scalars](technical-evidence/diagnostic-validate-scalars.receipt.json) | PASSED | 0 | PASSED: 1 |
| [diagnostic-validate-strict](technical-evidence/diagnostic-validate-strict.receipt.json) | PASSED | 0 | PASSED: 1 |
| [diagnostic-validate-taxa](technical-evidence/diagnostic-validate-taxa.receipt.json) | PASSED | 0 | PASSED: 1 |
| [diagnostic-validate-terms-all](technical-evidence/diagnostic-validate-terms-all.receipt.json) | SUPERSEDED BASELINE; INTERRUPTED | 143 | FAILED: 1 |
| [diagnostic-validate-terms-taxa](technical-evidence/diagnostic-validate-terms-taxa.receipt.json) | PASSED | 0 | PASSED: 1 |
| [dopamine-syncom-domain](technical-evidence/dopamine-syncom-domain.receipt.json) | PASSED | 0 | PASSED: 1 |
| [dopamine-syncom-gtdb](technical-evidence/dopamine-syncom-gtdb.receipt.json) | PASSED | 0 | PASSED: 1 |
| [dopamine-syncom-history](technical-evidence/dopamine-syncom-history.receipt.json) | PASSED | 0 | PASSED: 1 |
| [dopamine-syncom-references](technical-evidence/dopamine-syncom-references.receipt.json) | PASSED | 0 | PASSED: 1 |
| [dopamine-syncom-schema](technical-evidence/dopamine-syncom-schema.receipt.json) | PASSED | 0 | PASSED: 1 |
| [dopamine-syncom-strict](technical-evidence/dopamine-syncom-strict.receipt.json) | PASSED | 0 | PASSED: 1 |
| [dopamine-syncom-terms](technical-evidence/dopamine-syncom-terms.receipt.json) | PASSED | 0 | PASSED: 1 |
| [ecofab-domain](technical-evidence/ecofab-domain.receipt.json) | PASSED | 0 | PASSED: 1 |
| [ecofab-gtdb](technical-evidence/ecofab-gtdb.receipt.json) | PASSED | 0 | PASSED: 1 |
| [ecofab-history-corrected](technical-evidence/ecofab-history-corrected.receipt.json) | PASSED | 0 | PASSED: 1 |
| [ecofab-history](technical-evidence/ecofab-history.receipt.json) | FAILED | 1 | FAILED: 1 |
| [ecofab-references](technical-evidence/ecofab-references.receipt.json) | PASSED | 0 | PASSED: 1 |
| [ecofab-schema](technical-evidence/ecofab-schema.receipt.json) | PASSED | 0 | PASSED: 1 |
| [ecofab-strict](technical-evidence/ecofab-strict.receipt.json) | PASSED | 0 | PASSED: 1 |
| [ecofab-terms](technical-evidence/ecofab-terms.receipt.json) | PASSED | 0 | PASSED: 1 |
| [final-environment-canary](technical-evidence/final-environment-canary.receipt.json) | PASSED | 0 |  |
| [final-frozen-install](technical-evidence/final-frozen-install.receipt.json) | PASSED | 0 |  |
| [final-plan-qc-references](technical-evidence/final-plan-qc-references.receipt.json) | PASSED | 0 | DRY RUN: 13 |
| [historical-bases-fetch](technical-evidence/historical-bases-fetch.receipt.json) | PASSED | 0 |  |
| [historical-case-canary](technical-evidence/historical-case-canary.receipt.json) | PASSED | 0 |  |
| [historical-cases-remaining](technical-evidence/historical-cases-remaining.receipt.json) | PASSED | 0 |  |
| [lbnl-domain](technical-evidence/lbnl-domain.receipt.json) | PASSED | 0 | PASSED: 1 |
| [lbnl-gtdb](technical-evidence/lbnl-gtdb.receipt.json) | PASSED | 0 | PASSED: 1 |
| [lbnl-history](technical-evidence/lbnl-history.receipt.json) | PASSED | 0 | PASSED: 1 |
| [lbnl-references](technical-evidence/lbnl-references.receipt.json) | PASSED | 0 | PASSED: 1 |
| [lbnl-schema](technical-evidence/lbnl-schema.receipt.json) | PASSED | 0 | PASSED: 1 |
| [lbnl-strict](technical-evidence/lbnl-strict.receipt.json) | PASSED | 0 | PASSED: 1 |
| [lbnl-terms](technical-evidence/lbnl-terms.receipt.json) | PASSED | 0 | PASSED: 1 |
| [local-bracket-install](technical-evidence/local-bracket-install.receipt.json) | PASSED | 0 |  |
| [local-bracket-lock](technical-evidence/local-bracket-lock.receipt.json) | PASSED | 0 |  |
| [local-bracket-native-after](technical-evidence/local-bracket-native-after.receipt.json) | PASSED | 0 | PASSED: 1 |
| [local-bracket-regression-canary](technical-evidence/local-bracket-regression-canary.receipt.json) | PASSED | 0 |  |
| [local-bracket-regressions](technical-evidence/local-bracket-regressions.receipt.json) | PASSED | 0 |  |
| [local-c2-helper-integration](technical-evidence/local-c2-helper-integration.receipt.json) | PASSED | 0 |  |
| [local-c2-lint](technical-evidence/local-c2-lint.receipt.json) | PASSED | 0 | PASSED: 1 |
| [local-cache-canary-references](technical-evidence/local-cache-canary-references.receipt.json) | PASSED | 0 | PASSED: 1 |
| [local-curation-audit-writers](technical-evidence/local-curation-audit-writers.receipt.json) | PASSED | 0 | PASSED: 1 |
| [local-curation-canary-history](technical-evidence/local-curation-canary-history.receipt.json) | PASSED | 0 | PASSED: 1 |
| [local-curation-canary-schema](technical-evidence/local-curation-canary-schema.receipt.json) | PASSED | 0 | PASSED: 1 |
| [local-curation-canary-strict](technical-evidence/local-curation-canary-strict.receipt.json) | PASSED | 0 | PASSED: 1 |
| [local-curation-gen-html](technical-evidence/local-curation-gen-html.receipt.json) | PASSED | 0 | PASSED: 1 |
| [local-curation-history-all](technical-evidence/local-curation-history-all.receipt.json) | PASSED | 0 | PASSED: 1 |
| [local-export-index-after](technical-evidence/local-export-index-after.receipt.json) | PASSED | 0 |  |
| [local-export-index-before](technical-evidence/local-export-index-before.receipt.json) | FAILED | 1 |  |
| [local-postcuration-gate-regression](technical-evidence/local-postcuration-gate-regression.receipt.json) | PASSED | 0 |  |
| [local-successor-before](technical-evidence/local-successor-before.receipt.json) | FAILED | 1 |  |
| [local-successor-canary](technical-evidence/local-successor-canary.receipt.json) | PASSED | 0 |  |
| [local-successor-regressions](technical-evidence/local-successor-regressions.receipt.json) | PASSED | 0 |  |
| [nested-just-canary](technical-evidence/nested-just-canary.receipt.json) | PASSED | 0 |  |
| [plan-qc-references](technical-evidence/plan-qc-references.receipt.json) | PASSED | 0 | DRY RUN: 13 |
| [plan-qc](technical-evidence/plan-qc.receipt.json) | PASSED | 0 | DRY RUN: 11 |
| [qc-references](technical-evidence/qc-references.receipt.json) | INVALID LAUNCHER; INTERRUPTED | 2 | PASSED: 1; FAILED: 1; NOT RUN: 11 |
| [qc](technical-evidence/qc.receipt.json) | FAILED | 1 | PASSED: 1; FAILED: 1; NOT RUN: 9 |
| [shared-network-quality](technical-evidence/shared-network-quality.receipt.json) | FAILED | 1 | FAILED: 1 |
| [shared-network](technical-evidence/shared-network.receipt.json) | FAILED | 1 | FAILED: 1 |
| [yolo-domain](technical-evidence/yolo-domain.receipt.json) | PASSED | 0 | PASSED: 1 |
| [yolo-gtdb](technical-evidence/yolo-gtdb.receipt.json) | PASSED | 0 | PASSED: 1 |
| [yolo-history](technical-evidence/yolo-history.receipt.json) | PASSED | 0 | PASSED: 1 |
| [yolo-references](technical-evidence/yolo-references.receipt.json) | PASSED | 0 | PASSED: 1 |
| [yolo-schema](technical-evidence/yolo-schema.receipt.json) | PASSED | 0 | PASSED: 1 |
| [yolo-strict](technical-evidence/yolo-strict.receipt.json) | PASSED | 0 | PASSED: 1 |
| [yolo-terms](technical-evidence/yolo-terms.receipt.json) | PASSED | 0 | PASSED: 1 |

## baseline-bracket-reference

[Native output](technical-evidence/baseline-bracket-reference.log.txt) · [Exact exit](technical-evidence/baseline-bracket-reference.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never validate-references kb/communities/Asgard_Wetland_Soil_Methanogenesis_Substrate_Community.yaml`


| Native recipe | Status |
|---|---|
| validate-references | FAILED |

## bracket-regression-before

[Native output](technical-evidence/bracket-regression-before.log.txt) · [Exact exit](technical-evidence/bracket-regression-before.exit.txt)

Command: `uv run pytest tests/test_no_new_bracketed_snippets.py::test_unchanged_asgard_nife_quote_matches_its_committed_article -q`

1 failed in 0.38s

## canary

[Native output](technical-evidence/canary.log.txt) · [Exact exit](technical-evidence/canary.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never validate-scalars kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml`


| Native recipe | Status |
|---|---|
| validate-scalars | PASSED |

## diagnostic-validate-gtdb-all

[Native output](technical-evidence/diagnostic-validate-gtdb-all.log.txt) · [Exact exit](technical-evidence/diagnostic-validate-gtdb-all.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never --no-deps validate-gtdb-all`


| Native recipe | Status |
|---|---|
| validate-gtdb-all | PASSED |

## diagnostic-validate-scalars-idiomatic

[Native output](technical-evidence/diagnostic-validate-scalars-idiomatic.log.txt) · [Exact exit](technical-evidence/diagnostic-validate-scalars-idiomatic.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never --no-deps validate-scalars-idiomatic`


| Native recipe | Status |
|---|---|
| validate-scalars-idiomatic | PASSED |

## diagnostic-validate-scalars

[Native output](technical-evidence/diagnostic-validate-scalars.log.txt) · [Exact exit](technical-evidence/diagnostic-validate-scalars.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never --no-deps validate-scalars`


| Native recipe | Status |
|---|---|
| validate-scalars | PASSED |

## diagnostic-validate-strict

[Native output](technical-evidence/diagnostic-validate-strict.log.txt) · [Exact exit](technical-evidence/diagnostic-validate-strict.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never --no-deps validate-strict`


| Native recipe | Status |
|---|---|
| validate-strict | PASSED |

## diagnostic-validate-taxa

[Native output](technical-evidence/diagnostic-validate-taxa.log.txt) · [Exact exit](technical-evidence/diagnostic-validate-taxa.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never --no-deps validate-taxa`


| Native recipe | Status |
|---|---|
| validate-taxa | PASSED |

## diagnostic-validate-terms-all

[Native output](technical-evidence/diagnostic-validate-terms-all.log.txt) · [Exact exit](technical-evidence/diagnostic-validate-terms-all.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never --no-deps validate-terms-all`

Superseded baseline; deliberately interrupted before final-revision validation. This is not a repository-failure conclusion.

| Native recipe | Status |
|---|---|
| validate-terms-all | FAILED |

## diagnostic-validate-terms-taxa

[Native output](technical-evidence/diagnostic-validate-terms-taxa.log.txt) · [Exact exit](technical-evidence/diagnostic-validate-terms-taxa.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never --no-deps validate-terms-taxa`


| Native recipe | Status |
|---|---|
| validate-terms-taxa | PASSED |

## dopamine-syncom-domain

[Native output](technical-evidence/dopamine-syncom-domain.log.txt) · [Exact exit](technical-evidence/dopamine-syncom-domain.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never validate-gtdb-domain kb/communities/Brachypodium_Natural_Variation_Dopamine_SynCom16.yaml`


| Native recipe | Status |
|---|---|
| validate-gtdb-domain | PASSED |

## dopamine-syncom-gtdb

[Native output](technical-evidence/dopamine-syncom-gtdb.log.txt) · [Exact exit](technical-evidence/dopamine-syncom-gtdb.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never validate-gtdb kb/communities/Brachypodium_Natural_Variation_Dopamine_SynCom16.yaml`


| Native recipe | Status |
|---|---|
| validate-gtdb | PASSED |

## dopamine-syncom-history

[Native output](technical-evidence/dopamine-syncom-history.log.txt) · [Exact exit](technical-evidence/dopamine-syncom-history.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never validate-history history/records/Brachypodium_Natural_Variation_Dopamine_SynCom16`


| Native recipe | Status |
|---|---|
| validate-history | PASSED |

## dopamine-syncom-references

[Native output](technical-evidence/dopamine-syncom-references.log.txt) · [Exact exit](technical-evidence/dopamine-syncom-references.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never validate-references-explained kb/communities/Brachypodium_Natural_Variation_Dopamine_SynCom16.yaml`


| Native recipe | Status |
|---|---|
| validate-references-explained | PASSED |

## dopamine-syncom-schema

[Native output](technical-evidence/dopamine-syncom-schema.log.txt) · [Exact exit](technical-evidence/dopamine-syncom-schema.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never validate kb/communities/Brachypodium_Natural_Variation_Dopamine_SynCom16.yaml`


| Native recipe | Status |
|---|---|
| validate | PASSED |

## dopamine-syncom-strict

[Native output](technical-evidence/dopamine-syncom-strict.log.txt) · [Exact exit](technical-evidence/dopamine-syncom-strict.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never validate-strict kb/communities/Brachypodium_Natural_Variation_Dopamine_SynCom16.yaml`


| Native recipe | Status |
|---|---|
| validate-strict | PASSED |

## dopamine-syncom-terms

[Native output](technical-evidence/dopamine-syncom-terms.log.txt) · [Exact exit](technical-evidence/dopamine-syncom-terms.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never validate-terms kb/communities/Brachypodium_Natural_Variation_Dopamine_SynCom16.yaml`


| Native recipe | Status |
|---|---|
| validate-terms | PASSED |

## ecofab-domain

[Native output](technical-evidence/ecofab-domain.log.txt) · [Exact exit](technical-evidence/ecofab-domain.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never validate-gtdb-domain kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml`


| Native recipe | Status |
|---|---|
| validate-gtdb-domain | PASSED |

## ecofab-gtdb

[Native output](technical-evidence/ecofab-gtdb.log.txt) · [Exact exit](technical-evidence/ecofab-gtdb.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never validate-gtdb kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml`


| Native recipe | Status |
|---|---|
| validate-gtdb | PASSED |

## ecofab-history-corrected

[Native output](technical-evidence/ecofab-history-corrected.log.txt) · [Exact exit](technical-evidence/ecofab-history-corrected.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never validate-history history/records/EcoFAB_Ring_Trial_SynCom17`


| Native recipe | Status |
|---|---|
| validate-history | PASSED |

## ecofab-history

[Native output](technical-evidence/ecofab-history.log.txt) · [Exact exit](technical-evidence/ecofab-history.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never validate-history kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml`


| Native recipe | Status |
|---|---|
| validate-history | FAILED |

## ecofab-references

[Native output](technical-evidence/ecofab-references.log.txt) · [Exact exit](technical-evidence/ecofab-references.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never validate-references-explained kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml`


| Native recipe | Status |
|---|---|
| validate-references-explained | PASSED |

## ecofab-schema

[Native output](technical-evidence/ecofab-schema.log.txt) · [Exact exit](technical-evidence/ecofab-schema.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never validate kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml`


| Native recipe | Status |
|---|---|
| validate | PASSED |

## ecofab-strict

[Native output](technical-evidence/ecofab-strict.log.txt) · [Exact exit](technical-evidence/ecofab-strict.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never validate-strict kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml --out .temp/m5-completion-20261114/ecofab-strict.tsv`


| Native recipe | Status |
|---|---|
| validate-strict | PASSED |

## ecofab-terms

[Native output](technical-evidence/ecofab-terms.log.txt) · [Exact exit](technical-evidence/ecofab-terms.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never validate-terms kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml`


| Native recipe | Status |
|---|---|
| validate-terms | PASSED |

## final-environment-canary

[Native output](technical-evidence/final-environment-canary.log.txt) · [Exact exit](technical-evidence/final-environment-canary.exit.txt)

Command: `uv run pytest tests/test_no_new_bracketed_snippets.py::test_unchanged_asgard_nife_quote_matches_its_committed_article -q`

1 passed in 0.39s

## final-frozen-install

[Native output](technical-evidence/final-frozen-install.log.txt) · [Exact exit](technical-evidence/final-frozen-install.exit.txt)

Command: `uv sync --frozen --extra dev --python <REPO>/.venv/bin/python`


## final-plan-qc-references

[Native output](technical-evidence/final-plan-qc-references.log.txt) · [Exact exit](technical-evidence/final-plan-qc-references.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never --dry-run qc-references`


```text
    echo "⚠️  SKIPPED, NOT PASSED: this check could not look anything up (#708)."
    echo "⚠️  SKIPPED, NOT PASSED: this check could not look anything up (#708)."
```

| Native recipe | Status |
|---|---|
| lint | DRY RUN |
| test | DRY RUN |
| validate-all | DRY RUN |
| validate-taxa | DRY RUN |
| validate-strict | DRY RUN |
| validate-gtdb-all | DRY RUN |
| validate-scalars | DRY RUN |
| validate-scalars-idiomatic | DRY RUN |
| validate-terms-all | DRY RUN |
| validate-terms-taxa | DRY RUN |
| qc | DRY RUN |
| validate-references-all | DRY RUN |
| qc-references | DRY RUN |

## historical-bases-fetch

[Native output](technical-evidence/historical-bases-fetch.log.txt) · [Exact exit](technical-evidence/historical-bases-fetch.exit.txt)

Command: `git fetch --no-tags origin b036e766f9fb3b085b8111e4d34e6587ae242bb0 9174d5c1ce9c92966a4d270b4109071d81aa25f5 ba082c3e8c3f34f78e3f9dc32b35f57cc303bc7f e5ce1f8d359d1690b8cc0bd03d43ff41056f1339 5fb1fb3d8fa26c4f424be17f7a380e3f9c0eaee6`


## historical-case-canary

[Native output](technical-evidence/historical-case-canary.log.txt) · [Exact exit](technical-evidence/historical-case-canary.exit.txt)

Command: `uv run pytest tests/test_causal_review_batch15.py::test_batch15_ledger_covers_every_node_and_retained_edge -q`

1 passed in 0.15s

## historical-cases-remaining

[Native output](technical-evidence/historical-cases-remaining.log.txt) · [Exact exit](technical-evidence/historical-cases-remaining.exit.txt)

Command: `uv run pytest tests/test_causal_review_batch48.py::test_every_original_node_and_arrow_has_a_hash_bound_decision tests/test_causal_review_batch64.py::test_batch64_historical_caches_and_current_canonical_participants tests/test_causal_review_batch92.py::test_provenance_does_not_disguise_selected_excerpts_as_independent_sources -q`

3 passed in 0.39s

## lbnl-domain

[Native output](technical-evidence/lbnl-domain.log.txt) · [Exact exit](technical-evidence/lbnl-domain.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never validate-gtdb-domain kb/communities/LBNL_Switchgrass_Soil_SynCom16.yaml`


| Native recipe | Status |
|---|---|
| validate-gtdb-domain | PASSED |

## lbnl-gtdb

[Native output](technical-evidence/lbnl-gtdb.log.txt) · [Exact exit](technical-evidence/lbnl-gtdb.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never validate-gtdb kb/communities/LBNL_Switchgrass_Soil_SynCom16.yaml`


| Native recipe | Status |
|---|---|
| validate-gtdb | PASSED |

## lbnl-history

[Native output](technical-evidence/lbnl-history.log.txt) · [Exact exit](technical-evidence/lbnl-history.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never validate-history history/records/LBNL_Switchgrass_Soil_SynCom16`


| Native recipe | Status |
|---|---|
| validate-history | PASSED |

## lbnl-references

[Native output](technical-evidence/lbnl-references.log.txt) · [Exact exit](technical-evidence/lbnl-references.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never validate-references-explained kb/communities/LBNL_Switchgrass_Soil_SynCom16.yaml`


| Native recipe | Status |
|---|---|
| validate-references-explained | PASSED |

## lbnl-schema

[Native output](technical-evidence/lbnl-schema.log.txt) · [Exact exit](technical-evidence/lbnl-schema.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never validate kb/communities/LBNL_Switchgrass_Soil_SynCom16.yaml`


| Native recipe | Status |
|---|---|
| validate | PASSED |

## lbnl-strict

[Native output](technical-evidence/lbnl-strict.log.txt) · [Exact exit](technical-evidence/lbnl-strict.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never validate-strict kb/communities/LBNL_Switchgrass_Soil_SynCom16.yaml --out .temp/m5-completion-20261114/lbnl-strict.tsv`


| Native recipe | Status |
|---|---|
| validate-strict | PASSED |

## lbnl-terms

[Native output](technical-evidence/lbnl-terms.log.txt) · [Exact exit](technical-evidence/lbnl-terms.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never validate-terms kb/communities/LBNL_Switchgrass_Soil_SynCom16.yaml`


| Native recipe | Status |
|---|---|
| validate-terms | PASSED |

## local-bracket-install

[Native output](technical-evidence/local-bracket-install.log.txt) · [Exact exit](technical-evidence/local-bracket-install.exit.txt)

Command: `uv sync --frozen --extra dev --python <REPO>/.venv/bin/python`


## local-bracket-lock

[Native output](technical-evidence/local-bracket-lock.log.txt) · [Exact exit](technical-evidence/local-bracket-lock.exit.txt)

Command: `uv lock --upgrade-package linkml-reference-validator==0.2.1 --python <REPO>/.venv/bin/python`


## local-bracket-native-after

[Native output](technical-evidence/local-bracket-native-after.log.txt) · [Exact exit](technical-evidence/local-bracket-native-after.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never validate-references kb/communities/Asgard_Wetland_Soil_Methanogenesis_Substrate_Community.yaml`


| Native recipe | Status |
|---|---|
| validate-references | PASSED |

## local-bracket-regression-canary

[Native output](technical-evidence/local-bracket-regression-canary.log.txt) · [Exact exit](technical-evidence/local-bracket-regression-canary.exit.txt)

Command: `uv run pytest tests/test_no_new_bracketed_snippets.py::test_unchanged_asgard_nife_quote_matches_its_committed_article -q`

1 passed in 0.93s

## local-bracket-regressions

[Native output](technical-evidence/local-bracket-regressions.log.txt) · [Exact exit](technical-evidence/local-bracket-regressions.exit.txt)

Command: `uv run pytest tests/test_no_new_bracketed_snippets.py tests/test_reference_validator_actually_validates.py tests/test_reference_error_annotation.py -q`

27 passed, 12 warnings in 71.55s (0:01:11)

## local-c2-helper-integration

[Native output](technical-evidence/local-c2-helper-integration.log.txt) · [Exact exit](technical-evidence/local-c2-helper-integration.exit.txt)

Command: `uv run pytest tests/test_m5_completion_evidence_export.py tests/test_m5_source_capture_guards.py tests/test_m5_postcuration_gates.py tests/test_m5_attempt_provenance.py tests/test_m5_review_successor.py -q`

53 passed in 11.20s

## local-c2-lint

[Native output](technical-evidence/local-c2-lint.log.txt) · [Exact exit](technical-evidence/local-c2-lint.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never lint`


| Native recipe | Status |
|---|---|
| lint | PASSED |

## local-cache-canary-references

[Native output](technical-evidence/local-cache-canary-references.log.txt) · [Exact exit](technical-evidence/local-cache-canary-references.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never validate-references-explained kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml`


| Native recipe | Status |
|---|---|
| validate-references-explained | PASSED |

## local-curation-audit-writers

[Native output](technical-evidence/local-curation-audit-writers.log.txt) · [Exact exit](technical-evidence/local-curation-audit-writers.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never audit-writers`


| Native recipe | Status |
|---|---|
| audit-writers | PASSED |

## local-curation-canary-history

[Native output](technical-evidence/local-curation-canary-history.log.txt) · [Exact exit](technical-evidence/local-curation-canary-history.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never validate-history history/records/EcoFAB_Ring_Trial_SynCom17`


| Native recipe | Status |
|---|---|
| validate-history | PASSED |

## local-curation-canary-schema

[Native output](technical-evidence/local-curation-canary-schema.log.txt) · [Exact exit](technical-evidence/local-curation-canary-schema.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never validate kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml`


| Native recipe | Status |
|---|---|
| validate | PASSED |

## local-curation-canary-strict

[Native output](technical-evidence/local-curation-canary-strict.log.txt) · [Exact exit](technical-evidence/local-curation-canary-strict.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never validate-strict kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml`


| Native recipe | Status |
|---|---|
| validate-strict | PASSED |

## local-curation-gen-html

[Native output](technical-evidence/local-curation-gen-html.log.txt) · [Exact exit](technical-evidence/local-curation-gen-html.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never gen-html`


| Native recipe | Status |
|---|---|
| gen-html | PASSED |

## local-curation-history-all

[Native output](technical-evidence/local-curation-history-all.log.txt) · [Exact exit](technical-evidence/local-curation-history-all.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never validate-history`


| Native recipe | Status |
|---|---|
| validate-history | PASSED |

## local-export-index-after

[Native output](technical-evidence/local-export-index-after.log.txt) · [Exact exit](technical-evidence/local-export-index-after.exit.txt)

Command: `uv run pytest tests/test_m5_completion_evidence_export.py -q`

3 passed in 0.11s

## local-export-index-before

[Native output](technical-evidence/local-export-index-before.log.txt) · [Exact exit](technical-evidence/local-export-index-before.exit.txt)

Command: `uv run pytest tests/test_m5_completion_evidence_export.py::test_filtered_export_preserves_previous_index_entries -q`

1 failed in 0.11s

## local-postcuration-gate-regression

[Native output](technical-evidence/local-postcuration-gate-regression.log.txt) · [Exact exit](technical-evidence/local-postcuration-gate-regression.exit.txt)

Command: `uv run pytest tests/test_m5_postcuration_gates.py -q`

10 passed in 0.21s

## local-successor-before

[Native output](technical-evidence/local-successor-before.log.txt) · [Exact exit](technical-evidence/local-successor-before.exit.txt)

Command: `uv run pytest tests/test_causal_review_batch36.py::test_batch36_canonical_participants_anchors_history_and_hashes -q`

1 failed in 0.50s

## local-successor-canary

[Native output](technical-evidence/local-successor-canary.log.txt) · [Exact exit](technical-evidence/local-successor-canary.exit.txt)

Command: `uv run pytest tests/test_causal_review_batch36.py::test_batch36_canonical_participants_anchors_history_and_hashes -q`

1 passed in 0.51s

## local-successor-regressions

[Native output](technical-evidence/local-successor-regressions.log.txt) · [Exact exit](technical-evidence/local-successor-regressions.exit.txt)

Command: `uv run pytest tests/test_causal_review_batch36.py tests/test_causal_review_batch141.py tests/test_m5_review_successor.py -q`

20 passed in 8.06s

## nested-just-canary

[Native output](technical-evidence/nested-just-canary.log.txt) · [Exact exit](technical-evidence/nested-just-canary.exit.txt)

Command: `uv run pytest tests/test_claude_guide_contract.py::test_every_documented_just_recipe_exists -q`

1 passed in 0.02s

## plan-qc-references

[Native output](technical-evidence/plan-qc-references.log.txt) · [Exact exit](technical-evidence/plan-qc-references.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never --dry-run qc-references`


```text
    echo "⚠️  SKIPPED, NOT PASSED: this check could not look anything up (#708)."
    echo "⚠️  SKIPPED, NOT PASSED: this check could not look anything up (#708)."
```

| Native recipe | Status |
|---|---|
| lint | DRY RUN |
| test | DRY RUN |
| validate-all | DRY RUN |
| validate-taxa | DRY RUN |
| validate-strict | DRY RUN |
| validate-gtdb-all | DRY RUN |
| validate-scalars | DRY RUN |
| validate-scalars-idiomatic | DRY RUN |
| validate-terms-all | DRY RUN |
| validate-terms-taxa | DRY RUN |
| qc | DRY RUN |
| validate-references-all | DRY RUN |
| qc-references | DRY RUN |

## plan-qc

[Native output](technical-evidence/plan-qc.log.txt) · [Exact exit](technical-evidence/plan-qc.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never --dry-run qc`


```text
    echo "⚠️  SKIPPED, NOT PASSED: this check could not look anything up (#708)."
    echo "⚠️  SKIPPED, NOT PASSED: this check could not look anything up (#708)."
```

| Native recipe | Status |
|---|---|
| lint | DRY RUN |
| test | DRY RUN |
| validate-all | DRY RUN |
| validate-taxa | DRY RUN |
| validate-strict | DRY RUN |
| validate-gtdb-all | DRY RUN |
| validate-scalars | DRY RUN |
| validate-scalars-idiomatic | DRY RUN |
| validate-terms-all | DRY RUN |
| validate-terms-taxa | DRY RUN |
| qc | DRY RUN |

## qc-references

[Native output](technical-evidence/qc-references.log.txt) · [Exact exit](technical-evidence/qc-references.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never qc-references`

= 3 failed, 2706 passed, 18 skipped, 8 deselected, 16 warnings in 228.67s (0:03:48) =
Invalid launcher environment; deliberately interrupted. This is not a repository-failure conclusion.

| Native recipe | Status |
|---|---|
| lint | PASSED |
| test | FAILED |
| validate-all | NOT RUN |
| validate-taxa | NOT RUN |
| validate-strict | NOT RUN |
| validate-gtdb-all | NOT RUN |
| validate-scalars | NOT RUN |
| validate-scalars-idiomatic | NOT RUN |
| validate-terms-all | NOT RUN |
| validate-terms-taxa | NOT RUN |
| qc | NOT RUN |
| validate-references-all | NOT RUN |
| qc-references | NOT RUN |

## qc

[Native output](technical-evidence/qc.log.txt) · [Exact exit](technical-evidence/qc.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never qc`

= 4 failed, 5390 passed, 102 skipped, 8 deselected, 18 warnings in 1002.02s (0:16:42) =

| Native recipe | Status |
|---|---|
| lint | PASSED |
| test | FAILED |
| validate-all | NOT RUN |
| validate-taxa | NOT RUN |
| validate-strict | NOT RUN |
| validate-gtdb-all | NOT RUN |
| validate-scalars | NOT RUN |
| validate-scalars-idiomatic | NOT RUN |
| validate-terms-all | NOT RUN |
| validate-terms-taxa | NOT RUN |
| qc | NOT RUN |

## shared-network-quality

[Native output](technical-evidence/shared-network-quality.log.txt) · [Exact exit](technical-evidence/shared-network-quality.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never check-network-quality`


| Native recipe | Status |
|---|---|
| check-network-quality | FAILED |

## shared-network

[Native output](technical-evidence/shared-network.log.txt) · [Exact exit](technical-evidence/shared-network.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never audit-network`


| Native recipe | Status |
|---|---|
| audit-network | FAILED |

## yolo-domain

[Native output](technical-evidence/yolo-domain.log.txt) · [Exact exit](technical-evidence/yolo-domain.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never validate-gtdb-domain kb/communities/Yolo_Silt_Loam_Soil_Dopamine_Amendment_Microcosm.yaml`


| Native recipe | Status |
|---|---|
| validate-gtdb-domain | PASSED |

## yolo-gtdb

[Native output](technical-evidence/yolo-gtdb.log.txt) · [Exact exit](technical-evidence/yolo-gtdb.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never validate-gtdb kb/communities/Yolo_Silt_Loam_Soil_Dopamine_Amendment_Microcosm.yaml`


| Native recipe | Status |
|---|---|
| validate-gtdb | PASSED |

## yolo-history

[Native output](technical-evidence/yolo-history.log.txt) · [Exact exit](technical-evidence/yolo-history.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never validate-history history/records/Yolo_Silt_Loam_Soil_Dopamine_Amendment_Microcosm`


| Native recipe | Status |
|---|---|
| validate-history | PASSED |

## yolo-references

[Native output](technical-evidence/yolo-references.log.txt) · [Exact exit](technical-evidence/yolo-references.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never validate-references-explained kb/communities/Yolo_Silt_Loam_Soil_Dopamine_Amendment_Microcosm.yaml`


| Native recipe | Status |
|---|---|
| validate-references-explained | PASSED |

## yolo-schema

[Native output](technical-evidence/yolo-schema.log.txt) · [Exact exit](technical-evidence/yolo-schema.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never validate kb/communities/Yolo_Silt_Loam_Soil_Dopamine_Amendment_Microcosm.yaml`


| Native recipe | Status |
|---|---|
| validate | PASSED |

## yolo-strict

[Native output](technical-evidence/yolo-strict.log.txt) · [Exact exit](technical-evidence/yolo-strict.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never validate-strict kb/communities/Yolo_Silt_Loam_Soil_Dopamine_Amendment_Microcosm.yaml`


| Native recipe | Status |
|---|---|
| validate-strict | PASSED |

## yolo-terms

[Native output](technical-evidence/yolo-terms.log.txt) · [Exact exit](technical-evidence/yolo-terms.exit.txt)

Command: `/opt/homebrew/bin/just --verbose --no-dotenv --color never validate-terms kb/communities/Yolo_Silt_Loam_Soil_Dopamine_Amendment_Microcosm.yaml`


| Native recipe | Status |
|---|---|
| validate-terms | PASSED |
