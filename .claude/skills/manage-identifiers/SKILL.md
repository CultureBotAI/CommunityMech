---
name: manage-identifiers
description: Use this skill to manage CommunityMech record identifiers — find the highest existing CommunityMech id, mint the next id, and insert new community records with correct id placement. Use when adding or importing community records, or reconciling id collisions.
category: workflow
requires_database: false
requires_internet: false
version: 1.1.0
---

# Identifier Management (CommunityMech)

## Overview

Maintain stable, sequential record identifiers for CommunityMech so records have persistent
references, link cleanly across repositories, and integrate into the knowledge graph. IDs
never change once assigned and are never reused.

CommunityMech is a **multi-file collection**: each community is its own YAML file under
`kb/communities/`, with an `id` of the form `CommunityMech:NNNNNN` (zero-padded 6-digit,
`000001`–`999999`). Finding the next ID means scanning the directory; adding a record means
writing a new file (no shared metadata to update).

> The same identifier infrastructure is shared with MediaIngredientMech (single-file
> collection) and CultureMech (multi-file + registry). Those collection types, their
> find/mint/add variants, and a copy-paste utility module are documented in the reference
> files below — use them when working cross-repo or setting up a new X-Mech repository.

## When to Use This Skill

- Adding a new community record (or importing a batch)
- Finding the next available ID before minting
- Running batch ID assignment
- Validating ID sequences (duplicates, gaps, format)
- Reconciling ID collisions

---

## Identifier Format

```
CommunityMech:NNNNNN
```

- `CommunityMech` — repository prefix
- `NNNNNN` — zero-padded 6-digit sequential number (`000001`–`999999`)

Zero-padding makes alphabetical sort == numerical sort. The `id` is stable, unique within
the repo, and works directly as an RDF subject/object.

---

## Core Workflow

**Records:** one YAML file per community under `kb/communities/`. Full code for every step —
including the single-file and registry variants — is in
[`reference/finding-highest-id.md`](reference/finding-highest-id.md) and
[`reference/minting-and-adding.md`](reference/minting-and-adding.md).

### 1. Find the highest existing ID (scan **every** id-bearing directory)

`kb/communities/` is not the whole id space. `data/isolates/` carries
`CommunityMech:` ids too, and scanning only the first is what let four ids get
used twice (#310, #346) — the isolates held ids that later records re-minted.

```bash
grep -rh 'id: CommunityMech:' kb/communities/ data/isolates/ | cut -d: -f3 | sort -n | tail -1
```

```python
highest = max(
    find_highest_id_multi_file(Path(d), 'CommunityMech')
    for d in ('kb/communities', 'data/isolates')
)
```

`tests/test_id_uniqueness.py` fails the build if a mint collides anyway, but it
is a backstop — mint from the full space in the first place.

### 2. Mint the next ID

```python
next_id = generate_xmech_id('CommunityMech', highest + 1)   # -> 'CommunityMech:000079'
# generate_xmech_id(prefix, n) == f"{prefix}:{n:06d}"
```

### 3. Add the record (new file)

```python
new_community = {
    'id': next_id,                 # ALWAYS the first field
    'name': 'New Community Name',
    'description': 'Description of the microbial community',
    'environment': 'Environmental context',
    'members': [],
    'metadata': {
        'created_date': datetime.now(timezone.utc).isoformat(),
        'curator': 'manual_addition',
    },
}
safe_name = new_community['name'].replace(' ', '_').replace('/', '_')   # sanitize for filesystem
output_path = Path('kb/communities') / f"{safe_name}.yaml"
with open(output_path, 'w') as f:
    yaml.dump(new_community, f, default_flow_style=False, sort_keys=False,
              allow_unicode=True, width=100)
```

Key points: `id` first; sanitized filename (no special chars); **`sort_keys=False`** to
preserve field order; each file is independent (no shared metadata to update).

### 4. Batch assignment

```bash
python scripts/add_community_ids.py
```

Sequential assignment in sorted order, writes the `id` as the first field, prints per-file
progress. (This simple version has no `--dry-run`.) MediaIngredientMech/CultureMech batch
scripts are covered in [`reference/minting-and-adding.md`](reference/minting-and-adding.md).

---

## Validation

Validate format, find duplicates, and find sequence gaps — full validators and fixes in
[`reference/validation.md`](reference/validation.md):

- **Format:** every `id` matches `^CommunityMech:\d{6}$`.
- **Duplicates:** no two files share an ID (breaks references).
- **Gaps:** sequence is contiguous (gaps are tolerable but avoid creating them).

---

## Best Practices

### DO
- **Validate after changes** with the validation functions.
- **Zero-pad** with `{number:06d}`; place `id` first in the YAML.
- **Preserve ID history** — never reuse a deleted ID.
- **Use the existing script** for batches; document manual additions in record metadata.

### DON'T
- **Don't assign IDs** without scanning for the highest first.
- **Don't reuse** IDs from deleted records (breaks cross-references).
- **Don't use `sort_keys=True`** when saving (breaks field order).
- **Don't force-overwrite** existing IDs unless absolutely necessary.
- **Don't create gaps intentionally**, and don't use non-standard formats.

---

## Reference Files

| File | Contents |
|------|----------|
| [`reference/finding-highest-id.md`](reference/finding-highest-id.md) | Finding the highest ID for all three collection types (multi-file scan, recursive, single-file, registry) |
| [`reference/minting-and-adding.md`](reference/minting-and-adding.md) | Generic mint function, full add-record workflows (1 single-file, 2 multi-file, 3 multi-file+registry), and all three batch-assignment scripts |
| [`reference/validation.md`](reference/validation.md) | ID-format validator, duplicate finder, gap finder, and common issues + fixes |
| [`reference/cross-repo.md`](reference/cross-repo.md) | Collection-type comparison, MediaIngredientMech/CultureMech quick references, integration with curators and KGX export, and the future-enhancements/decision-tree material |
| [`reference/utility-module.md`](reference/utility-module.md) | Copy-paste-ready `xmech_id_utils` module covering all collection types |
