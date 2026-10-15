# Reference CLI Coverage Correction

This is a reporting/provenance correction for the recurrence tracked in
[#1469](https://github.com/CultureBotAI/CommunityMech/issues/1469), not a new
scientific review. `linkml-reference-validator` 0.1.7 labels the number of
reported issues as `Total checks`. A zero is not evidence of a no-op.

The real CLI was invoked through Typer's `CliRunner`, with source-network
lookup forbidden and unchanged source bytes in isolated temporary caches.
Native DOI filename casing is used only in that fixture; this is not a fix
for the separately tracked Linux cache-casing problem. A trace wrapping the
unmodified excerpt method records each field actually checked.

| Record | Checked excerpts | Omitted Discussion excerpts | Control / mutation / restoration exits |
| --- | ---: | ---: | --- |
| Phormidium | 21 | 2 | 0 / 1 / 0 |
| Alseth | 27 | 1 | 0 / 1 / 0 |
| PHA | 24 | 0 | 0 / 1 / 0 |

The mutation replaces one graph excerpt with fabricated text. Additional
Discussion mutations still exit 0 for Phormidium and Alseth, preserving the
known #476 gap rather than falsely claiming it is fixed. Lexical acceptance
does not establish scientific support.

Receipts retain exact outputs, dependency versions, paths and input hashes:
[Phormidium](final-phormidium-cli.json), [Alseth](alseth-cli.json),
[PHA](final-pha-cli.json), and the [failing pre-fix reporting tests](before-regression.json).
The [post-fix tests](after-regression.json) pass all 48 selected cases;
[lint](lint.json) and the [maintained explained command](explained-cli.json) pass.
Run `probe.py --record <stem> --output <new-path>` with the repository Python
environment to reproduce the controls; it refuses to overwrite receipts.

The before review ([YAML](../../reviews/structured/20261015T030500Z-reference-cli-coverage-before/review.yaml),
[Markdown](../../reviews/structured/20261015T030500Z-reference-cli-coverage-before/review.md))
records the recurrence. Its successor ([YAML](../../reviews/structured/20261015T031006Z-reference-cli-coverage-after/review.yaml),
[Markdown](../../reviews/structured/20261015T031006Z-reference-cli-coverage-after/review.md))
resolves the scoped finding and corrects the interpretation without editing
either historical bundle or their original command receipts.
The current index is maintained and now carries the correction prominently.
The explained command labels the counter `Reported validation issues` and
states its coverage limit; the raw command and its exit status are unchanged.

The batch132 `reference-cli` failed disposition is withdrawn in this narrow
reporting scope: that CLI run passed its native excerpt checks. Its two
Discussion excerpts were checked separately, not by the CLI. Batch130's
zero-check/no-coverage wording is likewise corrected, without altering any
scientific verdict, open graph findings, or the historical run output.
Supplement-only failures remain failures under #1996; no cache fallback,
source union, matching waiver or schema change is introduced.

An [ignored/hidden-inclusive candidate search](candidate-statements.json) covers
YAML and Markdown under `reviews/structured` and `reports/causal_graph_review`.
It includes earlier corrected statements, correct negations, and unrelated
zero-structural-defect statements. Matches are leads, not automatic findings.
The earlier batch31-41 correction remains in the current index. This change
assesses the newer batch130/132 recurrence; it does not claim to re-audit every
historical PR comment or close all of #1469's historical publication work.
