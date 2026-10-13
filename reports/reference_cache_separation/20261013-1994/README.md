# Issue 1994 Source Separation

This is a source-provenance repair, not a new scientific review. Canonical
community, isolate and taxon YAML is unchanged. No article text was fetched,
no publication PDF was added, and no validator fallback or waiver was added.

## Receipt

- `manifest.json`: exact before/after SHA-256 hashes, byte boundaries, sidecar
  dispositions and reviewed payload offsets for the 11 article caches.
- `before-inputs.json`: the review helper's pre-edit source inspection at
  `77ecab85bca112fde83ec221f5f4149666e01a78`.
- `targets.json`: the exact source cohort and maintained owners.
- `snippet-audit.json`: all 284 affected snippet occurrences in 11 records,
  field paths, snippet hashes, article/supplement line locations and native
  before/after findings. Canonical YAML roots were searched recursively,
  including hidden/ignored files; this is not a whole-record science audit.
- `audit.py`: the offline receipt generator. It must run against the historical
  mixed-cache baseline, not the repaired corpus.
- `verify.py` and `verification.json`: reproduce final byte preservation against
  the historical Git objects, confirm all 11 curated records are unchanged,
  and scan article caches including ignored files for remaining mixed sections.

Eight appended sections were byte-identical to existing sidecars. Choysum's
sidecar differs only in its retrieval header; the source body is identical.
Nasal SynCom's appended Table S2 is contained in its larger Tables S1-S4 sidecar.
All ten existing sidecars are retained unchanged. The missing Lupinus sidecar
is extracted byte-for-byte from its article suffix. Every article prefix is
preserved except for one separator newline immediately before the removed
append marker. This explicit `0a` normalization avoids a new blank line at EOF;
the receipt retains both the original prefix hash and the final article hash.

## Validation Boundary

The pinned native validator (0.1.7) returned zero failures before separation
and 79 article-only failures afterward. All 79 have whitespace/case-normalized
verbatim matches at the recorded separate-supplement locations and pass the
native matcher when that supplement is explicitly selected for the diagnostic.
That diagnostic is **not** a normal CLI pass. The failures remain visible and
are tracked in [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996).
Do not concatenate sources or introduce an automatic union/fallback.

Of the remaining 205 occurrences, 203 match article text with whitespace/case
folding. Two existing snippets need native punctuation normalization: `Lut`
versus `(Lut)` in PMID:42604006, and the Unicode hyphen in `co-inoculated` in
PMID:42099455. They are not literal whitespace-only matches and were not edited.
Lexical matching does not establish that a scientific claim is supported.

## Reproduction

Use a separate historical worktree and the pinned validation environment.
The generator writes diagnostics only to the chosen output directory and
disables network source lookup. Temporary article fixtures use the native
fetcher's normalized filename casing; no repository cache is renamed.

```bash
git worktree add --detach /tmp/communitymech-1994-before 77ecab85bca112fde83ec221f5f4149666e01a78
.venv/bin/python reports/reference_cache_separation/20261013-1994/audit.py \
  --repo-root /tmp/communitymech-1994-before --output-dir /tmp/communitymech-1994-audit
```

The repair command is deliberately hash-bound and refuses changed or already
separated inputs. It plans the entire batch before any write and never
overwrites an existing sidecar:

```bash
.venv/bin/python scripts/separate_legacy_supplements.py \
  reports/reference_cache_separation/20261013-1994/manifest.json
# Add --apply only in the reviewed mixed-cache worktree.
```

On the repaired worktree, run the final byte checks with:

```bash
.venv/bin/python reports/reference_cache_separation/20261013-1994/verify.py
```

The new corpus gate first failed on all 11 original mixed caches. Synthetic
tests exercise clean control, applied mutation, immediate restoration,
byte preservation and conflict refusal. The structured before/after reviews
under `reviews/structured/` are the assessed record; these JSON diagnostics
alone are not a completed scientific review or a record-level status change.
