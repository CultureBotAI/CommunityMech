---
name: schema-gap-analysis
description: Find gaps between CommunityMech's LinkML schema, its YAML community/isolate instances, and the code that generates them. Uses linkml-validate as ground truth and reports along three axes (schema / instances / process). Copy-paste runnable.
category: quality
requires_database: false
requires_internet: false
version: 2.1.0
---

# Schema gap analysis (CommunityMech)

The conceptual framework — why three axes, error-class heuristics, common anti-patterns — lives once at the cross-Mech version in claw:
https://github.com/CultureBotAI/culturebotai-claw/blob/main/.claude/skills/schema-gap-analysis/skill.md

This file is the CommunityMech-specific operational version. Every command below runs as-is.

## Setup

LinkML lives in `.venv/`:

```bash
.venv/bin/linkml-validate --help   # smoke test

# If you hit `AttributeError: Format has no attribute 'JSON'`, pin runtime:
.venv/bin/python -m pip install "linkml-runtime>=1.9,<1.10"
```

## Procedure

CommunityMech has no top-level collection file; everything is per-record.

Both `kb/communities/*.yaml` and `data/isolates/**/*.yaml` validate against the **same** `MicrobialCommunity` class — per `data/isolates/README.md`, isolates are single-organism communities kept in the same schema for interoperability. The schema only declares one `tree_root: true` class (`MicrobialCommunity`); there is no `IsolateRecord`.

The pipelines below `tee` validator output to a log **and** to your terminal — if `linkml-validate` itself errors out (missing schema path, wrong class name, broken venv), you want to see the message immediately, not have it swallowed into a `0` error count. The `|| true` on `grep -c` keeps the exit status at 0 when there are no errors (`grep -c` exits 1 on zero matches, which would break `set -e` recipes).

### 1. Validate the community knowledge base

```bash
find kb/communities -name "*.yaml" -print0 \
  | xargs -0 .venv/bin/linkml-validate \
      -s src/communitymech/schema/communitymech.yaml \
      -C MicrobialCommunity \
      2>&1 | tee /tmp/cme_validate.out
ERRORS=$(grep -c "^\[ERROR\]" /tmp/cme_validate.out || true)
echo "kb/communities errors: $ERRORS"
```

### 2. Validate the isolate records

Same class as step 1 — `MicrobialCommunity`. Isolates differ from communities in cardinality (one member, not many), not in schema.

```bash
find data/isolates -name "*.yaml" -print0 \
  | xargs -0 .venv/bin/linkml-validate \
      -s src/communitymech/schema/communitymech.yaml \
      -C MicrobialCommunity \
      2>&1 | tee /tmp/cme_isolates_validate.out
ERRORS=$(grep -c "^\[ERROR\]" /tmp/cme_isolates_validate.out || true)
echo "data/isolates errors: $ERRORS"
```

### 3. Histogram the errors

```bash
for f in /tmp/cme_validate.out /tmp/cme_isolates_validate.out; do
  [ -s "$f" ] || continue
  echo "=== $f ==="
  grep -oE "Additional properties are not allowed \('[^']+'" "$f" | sort | uniq -c | sort -rn
  grep -oE "'[^']+' is a required property" "$f" | sort | uniq -c | sort -rn
  grep -oE "does not match '[^']+'" "$f" | sort | uniq -c | sort -rn
  grep -oE "is not a '[^']+'" "$f" | sort | uniq -c | sort -rn
done
```

### 4. Cross-check generator drift (Axis 3)

CommunityMech YAMLs are currently hand-curated — there are no programmatic writers in `src/` or `scripts/`. The greps below are forward-looking: they fire when someone adds an auto-writer that emits the wrong shape. As long as they print nothing, the corpus's "process axis" is clean by construction.

```bash
# Naive datetimes
grep -rnE 'datetime\.now\(\)\.isoformat\b' \
  src/ scripts/ --include='*.py' | grep -v "timezone"

# Any write to kb/communities/ or data/isolates/ that isn't via a curator helper.
# Covers `open(..., "w"/"a"/"x"...)`, `Path(...).open(...)`, and `Path.write_text(...)`.
grep -rnE '(open\([^)]*(kb/communities|data/isolates)|(kb/communities|data/isolates)[^)]*\.write_text\()' \
  scripts/ src/ --include='*.py'

# Any yaml.dump / yaml.safe_dump that writes to the community or isolate trees
grep -rnE 'yaml\.(safe_)?dump\([^)]*(kb/communities|data/isolates)' \
  scripts/ src/ --include='*.py'
```

### 5. Re-validate after fixes

```bash
find kb/communities data/isolates -name "*.yaml" -print0 \
  | xargs -0 .venv/bin/linkml-validate \
      -s src/communitymech/schema/communitymech.yaml \
      -C MicrobialCommunity \
      2>&1 | tee /tmp/cme_revalidate.out
ERRORS=$(grep -c "^\[ERROR\]" /tmp/cme_revalidate.out || true)
echo "total errors after fixes: $ERRORS"   # target: 0
```

## CommunityMech-specific state (as of 2026-05-17 pass)

| Surface | Records | Errors |
|---|---:|---:|
| `kb/communities/*.yaml` | 261 | 0 (clean) |
| `data/isolates/**/*.yaml` | 5 | 4 (`'id' is a required property`) |

The community knowledge base passes cleanly under `linkml-validate -C MicrobialCommunity`. The isolate tree shares the same class but 4 of 5 files are missing the required `id` slot — likely an instance-axis gap (just add the missing `id:` to each isolate YAML and re-run step 2). If you add new classes/slots to `src/communitymech/schema/communitymech.yaml`, re-run this skill before committing.

## Pointers

- Schema: `src/communitymech/schema/communitymech.yaml`
- Curation source: `src/communitymech/curation/` (if present); otherwise direct edits via `kb/communities/<name>.yaml`
- Related skills: `review-communities` (manual review pass), `generate-schema-artifacts` (regenerate dataclasses)
- Cross-Mech framework + new-Mech bootstrap template: [claw/.claude/skills/schema-gap-analysis](https://github.com/CultureBotAI/culturebotai-claw/blob/main/.claude/skills/schema-gap-analysis/skill.md)
