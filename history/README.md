# Curation history

Append-only provenance for curation sessions. One record per session per target,
written once and **never edited afterwards**. Corrections go in a new record that
references the old one in its `details`.

```
history/<kind-dir>/<slug>/<TIMESTAMP>-<actor>-<shortid>.yaml
```

## Why this exists

Nothing else in the repo records *which model, using which tool, changed what,
why, and under which issue*. Git tells you a commit happened; it does not tell you
that a membership claim was checked against a cached abstract, or which deep-research
provider produced an interaction edge, or that a review deliberately changed nothing.

That gap matters more as autonomous agents start doing the changing. See
`culturebotai-claw/docs/AUTONOMOUS_LOOPS.md`.

## Why the layout looks like that

The directory-per-slug plus unguessable `shortid` is the whole design. Two agents
curating the same community concurrently cannot write the same file, so this layer
has **no merge-conflict surface**. A single shared changelog would conflict on every
parallel PR; this never does.

## Writing a record

Do not hand-write the filename or the timestamp — scaffold it:

```bash
just new-history --kind record --slug Anammox_Granule_Metabolic_Interaction_Community \
  --target-root kb/communities \
  --event EDIT --outcome changed \
  --sections members,interactions \
  --summary "Ground two unmapped members to NCBITaxon" \
  --model claude-opus-5 --agent-tool claude-code \
  --issue https://github.com/CultureBotAI/CommunityMech/issues/<n> \
  --details "What was done, what evidence was used, how it was validated."
```

Community records live flat under `kb/communities/`, so `--slug` is the record's
filename stem and `--target-root kb/communities` resolves the target path to
`kb/communities/<slug>.yaml`.

Omit `--details` and you get a TODO placeholder to edit before committing —
`just validate-history` **fails** while it is still there, so an unfilled record
cannot slip through. The command prints the record path as its final stdout line,
so scripts can capture it.

`--kind record` and `--kind schema` can derive the target path from `--slug` plus
`--target-root`. Every other kind needs an explicit `--path`, because only those
two are reliably `.yaml`.

Then validate and stage:

```bash
just validate-history history/records/Anammox_Granule_Metabolic_Interaction_Community/<file>.yaml
git add history/
```

## The vocabulary

`event`: `CREATE` · `EDIT` · `REVIEW` · `AUDIT` · `GENERAL`

`outcome`: `changed` · `no_change` · `needs_followup` · `blocked`

Outcome is **orthogonal** to event on purpose. A `REVIEW` that found nothing is
`no_change` — a real result worth recording, because it says something was
checked. An `EDIT` that hit a wall is `blocked`, and `details` must say what the
wall was so the next session does not rediscover it.

`kind`: `record` · `schema` · `mapping` · `report` · `infrastructure` · `other`
(`other` requires an explicit `--path`).

## How strictly this is enforced

Deliberately split:

- **Presence is advisory.** CI warns when a community record changes without a
  matching history record. It does not block. A hard gate on provenance blocks
  legitimate work at inconvenient moments and trains people to route around it.
- **Validity is not.** If you write a record it must be schema-valid, and
  `just validate-history` fails like any other validation error.

## Where the schema lives

Authority and consumer copies are separate on purpose:

- **Canonical**:
  `culturebotai-claw/src/kg_microbe_governance/artifacts/schema/history.yaml`.
- **Vendored here**: `src/communitymech/schema/history.yaml`, byte-identical.

Check that identity rather than trusting this file — with a claw checkout:

```bash
diff "${CLAW_SRC:-../../culturebotai-claw/src}/kg_microbe_governance/artifacts/schema/history.yaml" \
     src/communitymech/schema/history.yaml && echo "in sync"
```

(The `../../` default is not a typo: this clone is nested one level deeper than a
plain sibling checkout, which is why every claw-reaching recipe in the justfile
defaults `CLAW_SRC` to `../../culturebotai-claw/src`.)

Writing the md5 into this prose instead would go stale the first time the schema
gains a field and nobody updates the hash — a confident false negative. A runnable
command cannot decay that way.

The vendored copy exists so validation has **no dependency on a claw checkout**.
`just
validate-history` and the `curation-history` workflow both use the local copy and
work with no claw checkout at all.

Only `just new-history` needs claw, via `CLAW_SRC`. That is a dev-time scaffolder,
and anyone writing curation records has claw checked out.

Changing the schema means changing claw's canonical
`src/kg_microbe_governance/artifacts/schema/history.yaml`, updating its artifact
manifest, merging a reviewed claw commit, and coordinating that immutable pin
across the five Mechs. The unfiltered `vendored-sync` workflow verifies this
copy byte-for-byte against the public pinned manifest on every PR and main push.
