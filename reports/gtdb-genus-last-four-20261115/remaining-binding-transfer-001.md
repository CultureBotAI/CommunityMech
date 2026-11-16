# Remaining genus binding inputs

After the complete 441 canary was published as
`4f46bb640e0a5ceec646df90527bdfa881a20e12`, the already reviewed 389, 381 and
482 binding receipts, logs and exits were copied into the same isolated M5
worktree. These nine metadata files total 584,179 bytes. The original eight-file
approval and its retained denial remain documented separately; this transfer
used the normal bounded review path for the new metadata.

The first non-writing plan failed at sandbox hostname resolution, before any
copy (`genus-last-four-remaining-transfer-plan-001`, raw
`eed52aaac1c90772d8e0fc6372ad63bdd3e3d19b83cbc6be1cb273c953a08e12`).
The explicit network-enabled plan passed. A single 983-byte 389 receipt was then
copied using the maintained recorder and `rsync --ignore-existing`; its remote
size and hash were verified before the eight-file remainder. The remainder had
its own successful non-writing plan. No automatic approval rejection or
overwrite occurred.

The canary list is
`.temp/gtdb-genus-last-four-20261115/remaining-bindings-transfer-canary-001.files`
(`af37766f489c765db224e083bc0cbe02c6857deacb81269cbe305e2620dfdc44`);
the remaining list has the same prefix and `remaining-001.files` suffix
(`ca8b5a84b5161864fa6be5285d4b4b372ee7ae43547cdf3262d4e9360737e834`).
The local and M5 SHA-256 listings for all nine files are byte-identical:
`9d641d46aa46b4db9df464c45cf1ecbdb02a05d141c4eee36ab9240cfe6c6e55`.
Their recorder names are
`genus-last-four-remaining-input-hashes-{local,m5}-001` under
`.temp/phase2-schema-20261115/`.

The separate 381 supplement did not require an upload. The retained M5 source
`/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/references_cache/PMID_42549325.supplement.md`
was verified and copied locally on M5, without overwrite, into the already
declared private destination
`.temp/gtdb-genus-last-four-20261115/prymnesium381-supplement-retained-001.md`.
Source and destination both hash to
`4b30395e5db1c46bfb2f87a8737c55f825dfb80394485a5315736b006ec9f50e`
and the destination is 2,995,412 bytes. The retained verification log is
`genus-last-four-381-existing-source-verify-001`, raw
`e2152d8fbce53955b08bcf6be2dae163bcd7a7bb43de846c1c65af30eb186570`.
No acquisition, extraction or source-text upload was performed.

The M5 execution branch remains `review/gtdb-genus-last-four-20261115` at
`308081a8cf3f82472c542db87e135a5b96da61be`. The original whole-route binding
retains its pre-application 441 bytes; each remaining unit's explicit input list
excludes that unrelated canonical record. No full binder rerun was used to
replace the historical evidence. These input operations establish staging
readiness only; actual candidates, application, gates, saved diagnostics and
strict successor proofs have separate acceptance boundaries.
