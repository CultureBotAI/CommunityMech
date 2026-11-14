# Durable technical evidence

Each receipt preserves the original native-log SHA-256 and the published derivative SHA-256.
Absolute home paths, email addresses and credential-shaped values are replaced where present.
Raw logs remain in both review checkouts. Failed/interrupted attempts are retained.
Separate diagnostics do not change an aggregate failure or its NOT RUN stages.

| Run | Status | Exit | Log | Receipt |
|---|---|---:|---|---|
| baseline-bracket-reference | FAILED | 1 | [baseline-bracket-reference.log.txt](baseline-bracket-reference.log.txt) | [JSON](baseline-bracket-reference.receipt.json) |
| bracket-regression-before | FAILED | 1 | [bracket-regression-before.log.txt](bracket-regression-before.log.txt) | [JSON](bracket-regression-before.receipt.json) |
| canary | PASSED | 0 | [canary.log.txt](canary.log.txt) | [JSON](canary.receipt.json) |
| diagnostic-validate-gtdb-all | PASSED | 0 | [diagnostic-validate-gtdb-all.log.txt](diagnostic-validate-gtdb-all.log.txt) | [JSON](diagnostic-validate-gtdb-all.receipt.json) |
| diagnostic-validate-scalars-idiomatic | PASSED | 0 | [diagnostic-validate-scalars-idiomatic.log.txt](diagnostic-validate-scalars-idiomatic.log.txt) | [JSON](diagnostic-validate-scalars-idiomatic.receipt.json) |
| diagnostic-validate-scalars | PASSED | 0 | [diagnostic-validate-scalars.log.txt](diagnostic-validate-scalars.log.txt) | [JSON](diagnostic-validate-scalars.receipt.json) |
| diagnostic-validate-strict | PASSED | 0 | [diagnostic-validate-strict.log.txt](diagnostic-validate-strict.log.txt) | [JSON](diagnostic-validate-strict.receipt.json) |
| diagnostic-validate-taxa | PASSED | 0 | [diagnostic-validate-taxa.log.txt](diagnostic-validate-taxa.log.txt) | [JSON](diagnostic-validate-taxa.receipt.json) |
| diagnostic-validate-terms-taxa | PASSED | 0 | [diagnostic-validate-terms-taxa.log.txt](diagnostic-validate-terms-taxa.log.txt) | [JSON](diagnostic-validate-terms-taxa.receipt.json) |
| dopamine-syncom-domain | PASSED | 0 | [dopamine-syncom-domain.log.txt](dopamine-syncom-domain.log.txt) | [JSON](dopamine-syncom-domain.receipt.json) |
| dopamine-syncom-gtdb | PASSED | 0 | [dopamine-syncom-gtdb.log.txt](dopamine-syncom-gtdb.log.txt) | [JSON](dopamine-syncom-gtdb.receipt.json) |
| dopamine-syncom-history | PASSED | 0 | [dopamine-syncom-history.log.txt](dopamine-syncom-history.log.txt) | [JSON](dopamine-syncom-history.receipt.json) |
| dopamine-syncom-references | PASSED | 0 | [dopamine-syncom-references.log.txt](dopamine-syncom-references.log.txt) | [JSON](dopamine-syncom-references.receipt.json) |
| dopamine-syncom-schema | PASSED | 0 | [dopamine-syncom-schema.log.txt](dopamine-syncom-schema.log.txt) | [JSON](dopamine-syncom-schema.receipt.json) |
| dopamine-syncom-strict | PASSED | 0 | [dopamine-syncom-strict.log.txt](dopamine-syncom-strict.log.txt) | [JSON](dopamine-syncom-strict.receipt.json) |
| dopamine-syncom-terms | PASSED | 0 | [dopamine-syncom-terms.log.txt](dopamine-syncom-terms.log.txt) | [JSON](dopamine-syncom-terms.receipt.json) |
| ecofab-domain | PASSED | 0 | [ecofab-domain.log.txt](ecofab-domain.log.txt) | [JSON](ecofab-domain.receipt.json) |
| ecofab-gtdb | PASSED | 0 | [ecofab-gtdb.log.txt](ecofab-gtdb.log.txt) | [JSON](ecofab-gtdb.receipt.json) |
| ecofab-history-corrected | PASSED | 0 | [ecofab-history-corrected.log.txt](ecofab-history-corrected.log.txt) | [JSON](ecofab-history-corrected.receipt.json) |
| ecofab-history | FAILED | 1 | [ecofab-history.log.txt](ecofab-history.log.txt) | [JSON](ecofab-history.receipt.json) |
| ecofab-references | PASSED | 0 | [ecofab-references.log.txt](ecofab-references.log.txt) | [JSON](ecofab-references.receipt.json) |
| ecofab-schema | PASSED | 0 | [ecofab-schema.log.txt](ecofab-schema.log.txt) | [JSON](ecofab-schema.receipt.json) |
| ecofab-strict | PASSED | 0 | [ecofab-strict.log.txt](ecofab-strict.log.txt) | [JSON](ecofab-strict.receipt.json) |
| ecofab-terms | PASSED | 0 | [ecofab-terms.log.txt](ecofab-terms.log.txt) | [JSON](ecofab-terms.receipt.json) |
| historical-bases-fetch | PASSED | 0 | [historical-bases-fetch.log.txt](historical-bases-fetch.log.txt) | [JSON](historical-bases-fetch.receipt.json) |
| historical-case-canary | PASSED | 0 | [historical-case-canary.log.txt](historical-case-canary.log.txt) | [JSON](historical-case-canary.receipt.json) |
| historical-cases-remaining | PASSED | 0 | [historical-cases-remaining.log.txt](historical-cases-remaining.log.txt) | [JSON](historical-cases-remaining.receipt.json) |
| lbnl-domain | PASSED | 0 | [lbnl-domain.log.txt](lbnl-domain.log.txt) | [JSON](lbnl-domain.receipt.json) |
| lbnl-gtdb | PASSED | 0 | [lbnl-gtdb.log.txt](lbnl-gtdb.log.txt) | [JSON](lbnl-gtdb.receipt.json) |
| lbnl-history | PASSED | 0 | [lbnl-history.log.txt](lbnl-history.log.txt) | [JSON](lbnl-history.receipt.json) |
| lbnl-references | PASSED | 0 | [lbnl-references.log.txt](lbnl-references.log.txt) | [JSON](lbnl-references.receipt.json) |
| lbnl-schema | PASSED | 0 | [lbnl-schema.log.txt](lbnl-schema.log.txt) | [JSON](lbnl-schema.receipt.json) |
| lbnl-strict | PASSED | 0 | [lbnl-strict.log.txt](lbnl-strict.log.txt) | [JSON](lbnl-strict.receipt.json) |
| lbnl-terms | PASSED | 0 | [lbnl-terms.log.txt](lbnl-terms.log.txt) | [JSON](lbnl-terms.receipt.json) |
| local-bracket-install | PASSED | 0 | [local-bracket-install.log.txt](local-bracket-install.log.txt) | [JSON](local-bracket-install.receipt.json) |
| local-bracket-lock | PASSED | 0 | [local-bracket-lock.log.txt](local-bracket-lock.log.txt) | [JSON](local-bracket-lock.receipt.json) |
| local-bracket-native-after | PASSED | 0 | [local-bracket-native-after.log.txt](local-bracket-native-after.log.txt) | [JSON](local-bracket-native-after.receipt.json) |
| local-bracket-regression-canary | PASSED | 0 | [local-bracket-regression-canary.log.txt](local-bracket-regression-canary.log.txt) | [JSON](local-bracket-regression-canary.receipt.json) |
| local-bracket-regressions | PASSED | 0 | [local-bracket-regressions.log.txt](local-bracket-regressions.log.txt) | [JSON](local-bracket-regressions.receipt.json) |
| local-cache-canary-references | PASSED | 0 | [local-cache-canary-references.log.txt](local-cache-canary-references.log.txt) | [JSON](local-cache-canary-references.receipt.json) |
| local-curation-canary-history | PASSED | 0 | [local-curation-canary-history.log.txt](local-curation-canary-history.log.txt) | [JSON](local-curation-canary-history.receipt.json) |
| local-curation-canary-schema | PASSED | 0 | [local-curation-canary-schema.log.txt](local-curation-canary-schema.log.txt) | [JSON](local-curation-canary-schema.receipt.json) |
| local-curation-canary-strict | PASSED | 0 | [local-curation-canary-strict.log.txt](local-curation-canary-strict.log.txt) | [JSON](local-curation-canary-strict.receipt.json) |
| nested-just-canary | PASSED | 0 | [nested-just-canary.log.txt](nested-just-canary.log.txt) | [JSON](nested-just-canary.receipt.json) |
| plan-qc-references | PASSED | 0 | [plan-qc-references.log.txt](plan-qc-references.log.txt) | [JSON](plan-qc-references.receipt.json) |
| plan-qc | PASSED | 0 | [plan-qc.log.txt](plan-qc.log.txt) | [JSON](plan-qc.receipt.json) |
| qc-references | INVALID LAUNCHER; INTERRUPTED | 2 | [qc-references.log.txt](qc-references.log.txt) | [JSON](qc-references.receipt.json) |
| qc | FAILED | 1 | [qc.log.txt](qc.log.txt) | [JSON](qc.receipt.json) |
| shared-network-quality | FAILED | 1 | [shared-network-quality.log.txt](shared-network-quality.log.txt) | [JSON](shared-network-quality.receipt.json) |
| shared-network | FAILED | 1 | [shared-network.log.txt](shared-network.log.txt) | [JSON](shared-network.receipt.json) |
| yolo-domain | PASSED | 0 | [yolo-domain.log.txt](yolo-domain.log.txt) | [JSON](yolo-domain.receipt.json) |
| yolo-gtdb | PASSED | 0 | [yolo-gtdb.log.txt](yolo-gtdb.log.txt) | [JSON](yolo-gtdb.receipt.json) |
| yolo-history | PASSED | 0 | [yolo-history.log.txt](yolo-history.log.txt) | [JSON](yolo-history.receipt.json) |
| yolo-references | PASSED | 0 | [yolo-references.log.txt](yolo-references.log.txt) | [JSON](yolo-references.receipt.json) |
| yolo-schema | PASSED | 0 | [yolo-schema.log.txt](yolo-schema.log.txt) | [JSON](yolo-schema.receipt.json) |
| yolo-strict | PASSED | 0 | [yolo-strict.log.txt](yolo-strict.log.txt) | [JSON](yolo-strict.receipt.json) |
| yolo-terms | PASSED | 0 | [yolo-terms.log.txt](yolo-terms.log.txt) | [JSON](yolo-terms.receipt.json) |
