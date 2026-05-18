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

### 1. Validate the community knowledge base

```bash
find kb/communities -name "*.yaml" -print0 \
  | xargs -0 .venv/bin/linkml-validate \
      -s src/communitymech/schema/communitymech.yaml \
      -C MicrobialCommunity \
      2>&1 | tee /tmp/cme_validate.out > /dev/null
grep -c "^\[ERROR\]" /tmp/cme_validate.out
```

### 2. Validate the isolate records

Isolates use a different class — find the right one in the schema first if needed:

```bash
# Identify the isolate root class
grep -B1 "tree_root: true\|^  Isolate" src/communitymech/schema/communitymech.yaml | head -20

# Then validate (adjust -C to match)
find data/isolates -name "*.yaml" -print0 \
  | xargs -0 .venv/bin/linkml-validate \
      -s src/communitymech/schema/communitymech.yaml \
      -C IsolateRecord \
      2>&1 | tee /tmp/cme_isolates_validate.out > /dev/null
grep -c "^\[ERROR\]" /tmp/cme_isolates_validate.out
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

```bash
# Naive datetimes
grep -rnE 'datetime\.now\(\)\.isoformat\b' \
  src/ scripts/ --include='*.py' | grep -v "timezone"

# yaml.dump that drops collection metadata (CommunityMech keys: communities/isolates)
grep -rnE 'yaml\.dump\(\s*\{\s*["\047](communities|isolates)["\047]\s*:' \
  src/ scripts/ --include='*.py'

# Direct writes to kb/communities/ that skip the curator
grep -rnE 'open\([^)]*kb/communities/[^)]*["\047][wa][bt]?["\047]' \
  scripts/ src/ --include='*.py'
```

### 5. Re-validate after fixes

```bash
find kb/communities -name "*.yaml" -print0 \
  | xargs -0 .venv/bin/linkml-validate \
      -s src/communitymech/schema/communitymech.yaml \
      -C MicrobialCommunity \
      2>&1 | grep -c "^\[ERROR\]"
# target: 0
```

## CommunityMech-specific state (as of 2026-05-17 pass)

| Surface | Records | Errors |
|---|---:|---:|
| `kb/communities/*.yaml` | 261 | 0 (clean) |
| `data/isolates/**/*.yaml` | _(re-run step 2 to populate)_ | _(unknown until run)_ |

The community knowledge base passes cleanly under `linkml-validate -C MicrobialCommunity`. If you add new classes/slots to `src/communitymech/schema/communitymech.yaml`, re-run this skill before committing.

## Pointers

- Schema: `src/communitymech/schema/communitymech.yaml`
- Curation source: `src/communitymech/curation/` (if present); otherwise direct edits via `kb/communities/<name>.yaml`
- Related skills: `review-communities` (manual review pass), `generate-schema-artifacts` (regenerate dataclasses)
- Cross-Mech framework + new-Mech bootstrap template: [claw/.claude/skills/schema-gap-analysis](https://github.com/CultureBotAI/culturebotai-claw/blob/main/.claude/skills/schema-gap-analysis/skill.md)
