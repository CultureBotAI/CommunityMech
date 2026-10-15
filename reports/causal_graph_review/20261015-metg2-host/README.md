# MetG2 Host-Scope Repair

This is a partial source-based self-review under [#1847](https://github.com/CultureBotAI/CommunityMech/issues/1847),
not independent approval or whole-record certification. The source population is
one target from 462 community/isolate records; all other canonical records are
unchanged.

- [Historical pre-fix YAML](../../../reviews/structured/20261015T043154Z-metg2-host-before/review.yaml)
  and [Markdown](../../../reviews/structured/20261015T043154Z-metg2-host-before/review.md).
- [Successor YAML](../../../reviews/structured/20261015T044333Z-metg2-host-after/review.yaml)
  and [Markdown](../../../reviews/structured/20261015T044333Z-metg2-host-after/review.md)
  resolve the scoped host/participant finding and explicitly carry the unresolved
  membership finding forward. Both observations retain their exact input commits
  under annotated `review-provenance/20261015-metg2-host-*` tags.
- [Decision ledger](../decisions/20261015-metg2-host.yaml) preserves all three
  node decisions, the retained hypothetical arrow and the prior review hash.
- [Source manifest](../sources/20261015-metg2-host/manifest.json) and raw NCBI XML
  distinguish genus from species, without claiming the experimental cultivar.
- `before-regression.json` reproduces the unsupported species grounding.
  The final regression receipts include control/mutation/restoration and native
  auditor participant-credit checks.
- `references.json` is the maintained CLI command. `explicit-excerpts.json`
  traces six native calls, tests a fabricated graph snippet and restoration,
  and separately checks all eight excerpts with the unchanged native matcher.
  The two Discussion omissions remain [#476](https://github.com/CultureBotAI/CommunityMech/issues/476).
- `preservation-final.json` verifies one changed canonical record, unchanged
  snippet/reference pairs, unchanged cache/schema/config and the exact baseline
  network warning set. The native network diagnostic exits 1 for 57 warnings,
  not a zero-warning pass. There are no structural defects.

Failed intermediate receipts remain intact. The mutation harness, participant
census, import/XML lint annotation and preservation-helper summary key were
corrected without relaxing validation. Old batch108 assertions use their exact
retained historical record; separate current-record tests check this successor.

The retained functional-gene aggregate is not newly certified as belonging to
every inoculant. Exact membership, strain spelling, experimental host and complete
Methods remain outstanding. No source snippets, caches, new graph topology or
provider submissions were added. Remote CI and protected queue results must be
verified separately; local receipts alone do not establish merge readiness.
