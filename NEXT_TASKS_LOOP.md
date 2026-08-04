# Loop-ready backlog

Which open issues suit an autonomous `/goal` run with
[`prompts/backlog-loop.goal.md`](prompts/backlog-loop.goal.md), and which do not.

`NEXT_TASKS.md` is the full backlog and stays the source of truth for *what* is
deferred. This file answers a narrower question: *what can be handed to a loop
that will not stop to ask?* Reconciled 2026-08-04. Every claim below was
re-measured against `main` on that date, not copied from the issue text.

## What makes an item loop-ready

1. **A machine-checkable definition of done** — a test, a gate, a command exit
   code. Not "reads better".
2. **No curation or schema decision.** The loop pauses for those by design, and
   an item that pauses on its first step wastes the run.
3. **Bounded blast radius**, so an adversarial review can actually cover it.
4. **A premise that survives measurement.** Half the issues in this repo have
   been wrong on inspection (#273, #276, #310, #346); the loop re-measures
   first, but an item whose premise is already verified starts a step ahead.

## Tier 1 — ready now

Ranked by value per unit of risk. Each has a verified premise and a green/red
finish condition.

| # | Item | Size | Done when | Verified 2026-08-04 |
|---|---|---|---|---|
| 1 | **#290** `just install` fails | XS | `just install` exits 0 | `uv sync --group dev` → *"Group `dev` is not defined"*; deps are under `[project.optional-dependencies]` |
| 2 | **#295** one snippet cited at two supports levels | S | the pair agrees, or the difference is explained | `Geobacter_Clostridium_…` cites the DIET snippet as both `PARTIAL` and `SUPPORT` |
| 3 | **#314** taxon ungrounded after an id edit | S | `gtdb_classification` present; a test pins `ncbi_source_id == term.id` | `Mesorhizobium_Synechococcus_…`: `NCBITaxon:1125` is the one taxon of four with no grounding |
| 4 | **#358** goal-prompt size unguarded | XS | a test asserts chars **and** bytes | 3995 chars / 4021 bytes, 5 chars of headroom, nothing guards it |
| 5 | **#350** isolates are gated for schema only | M | isolates pass term validation, or the roots are documented as schema-only | **4 of 4** isolates fail `linkml-term-validator --labels` today |
| 6 | **#306** snippet checks pick a cache file arbitrarily | M | resolution is deterministic, pinned by a test | **63** references have both `.md` and `.txt` in `references_cache/` |
| 7 | **#352a** SPRUCE has no published page | XS | `just gen-html`, page committed | 312 records, **305** pages |
| 8 | **#277** four `[[wiki-links]]` resolve to nothing | XS | no dangling links | 4 dangling: `chebi-mislabels-backlog`, `edison-auth-env-shadowing`, `ontology-term-cleanup`, `space-regolith-scouting-gap` |

**Start with #290.** It is one line, it exits 0 or it doesn't, and it retires a
gotcha the goal prompt currently has to carry. A clean first pass through the
whole loop on a trivial item is worth more than a big first win.

## Tier 2 — loop-able with a tighter brief

Mechanical enough to automate, but each needs an instruction that constrains
judgement, or the loop will invent something.

- **#347 — SPRUCE's 17 snippets are paraphrases, not quotes.** Both abstracts are
  cached, and "is this a verbatim substring" is machine-checkable, so the loop
  can do it. Brief it to *only* use exact substrings and to **delete** a claim it
  cannot source rather than reword one. Without that, the failure mode is
  fabricating support. Note `just validate-references-all` already fails on
  `main` (e.g. `Aalborg_East_…`), so this improves a red gate rather than
  greening it.
- **#270 — interaction type encoded by colour alone**, nine categories. Fully
  specified, and the CVD-simulation harness from #268 already exists to verify a
  redundant encoding. Frontend, self-contained.
- **#352b — a second coarse SPRUCE record (`000135`) already exists.** Only the
  *report* is loop-able; whether to merge the two records is a curator call.

## Tier 3 — needs a human decision first

Do not queue these. Each stops on the loop's first substantive step, and the
answer is not derivable from the repo.

| # | The decision that is actually needed |
|---|---|
| #294 | Approve or reject the `gtdb_grounding_status` enum (proposal §4.1) |
| #307 | Approve or reject the counter-selection block (§4.3) — design **with** #312 |
| #312 | Should a `COMMUNITY_LEVEL` interaction be able to name *which* members it concerns? |
| #301 | Mint METPO terms for biocontrol/antagonist and N-fixing symbiont, or reuse? |
| #297 | Is ROS detoxification a metabolite or a process in that record? |
| #292 | Two taxa carry an id for a different organism — correct, or keep withheld? |
| #325 | Backfill `curation_history` to 311 records, or drop the slot? |
| #355 | Is interaction 1 `COMMENSALISM`/`CROSS_FEEDING` rather than `MUTUALISM`? |
| #356 | Does the ECM entry mean nutrients *from* the host or *to* it? |
| #182 | Which best-effort ontology remaps to accept |
| #199 | Which dataviz findings to act on |

**#319 is decided but heavy.** Hosts and antagonists become taxonomy members (13
instances, 12 records) and the 14 `NCBITaxon:2` aggregate placeholders lose their
participant slot. The decision is made; the work is per-record evidence curation,
so it belongs in a focused session rather than an unattended loop.

## Ordering and dependencies

- **#358 waits for [#357](https://github.com/CultureBotAI/CommunityMech/pull/357)
  to merge** — it asserts a limit on the file that PR is still changing.
- **#347, #355, #356 all edit `SPRUCE_Peatland_Warming_Community.yaml`.** One PR,
  or strictly serial; the loop's one-PR-in-flight rule handles this if they are
  not queued together.
- **#314 before #294.** #314 is the data fix; #294 is the schema that would
  describe it. Doing the data first keeps the enum backfill honest.
- **#350 and #352a** both touch isolate/site generation but do not overlap.
- **#290 retires a gotcha** in `prompts/backlog-loop.goal.md`. Whoever fixes it
  updates the prompt in the same PR — the prompt's own header says so.

## Never loop these

- Anything needing full text the repo cannot fetch (**#183**, and the blocked
  half of **#259**).
- Anything editing sibling repos (**#30** touches cross-Mech linking; the loop is
  scoped to this repo and must only report divergence).
- **#359** is a note, not a task.
