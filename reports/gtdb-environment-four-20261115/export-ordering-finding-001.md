The first local TCP/Wheat public export refused before writing because the
historical callers had already been updated after the saved review audit and
export plan. The saved review correctly pins the original callers. The failure
names `tests/test_causal_review_batch122.py`; batch124 was also updated.

This is an execution-order error, not an exporter defect. Preserve the failed
receipt `environment-two-export-001` and its log SHA256
`feee7ba316c90856db2de553d70ab89d6d4057517570879a69283b91d083288b`.
An ignore-inclusive file search found no TCP/Wheat public export artifacts
after this refusal.

Recovery: use the exact reviewed export config on the original frozen M5
checkout, where the captured caller bytes remain unchanged; verify every
exported artifact before mirroring it locally. Do not weaken input verification,
rewrite the saved review, or overwrite the original input checkpoint. Future
units must finish the evidence export before editing captured historical callers.

Acceptance requires a successful original-checkout export, complete output hash
verification, and the unchanged saved pair and complete checkpoint. The new
caller changes require their own adversarial review and actual-proof controls.

Recorded 2026-11-15 for PR2902 and issue2848. This finding does not change any
scientific assessment or establish full QC completion.
