# Loop-ready backlog

Which open issues suit an autonomous `/goal` run with
[`prompts/backlog-loop.goal.md`](prompts/backlog-loop.goal.md), and which do not.

`NEXT_TASKS.md` is the full backlog and stays the source of truth for *what* is
deferred. This file answers a narrower question: *what can be handed to a loop
that will not stop to ask?* Reconciled 2026-08-03. Every claim was re-measured
against `main`, not copied from the issue — including where the two disagree.

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

| # | Item | Size | Done when | Verified against `main` |
|---|---|---|---|---|
| 1 | **#290** `just install` fails | XS | `just install` exits 0 | `uv sync --group dev` → *"Group `dev` is not defined"*; deps are under `[project.optional-dependencies]` |
| 2 | **#314** taxon ungrounded after an id edit | S | `gtdb_classification` present; a test pins `ncbi_source_id == term.id` | `Mesorhizobium_Synechococcus_…`: `NCBITaxon:1125` is the one taxon of four with no grounding |
| 3 | **#306** snippet checks pick a cache file arbitrarily | M | resolution is deterministic, pinned by a test | **62** stems carry both `.md` and `.txt`; 63 folding case, 63 with any two extensions |
| 4 | **#352a** seven records have no published page | XS | `just gen-html`; every record has a page | 312 records, **305** pages — 7 missing, not just SPRUCE |

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
- **#295 — one snippet cited at two supports levels.** Looks mechanical and is
  not: the issue asks for `PARTIAL` *or* dropping the citation, and names the
  curator who made #262's call as the decider. Brief it to reuse that reasoning.
  It is also not a clean pair — the `SUPPORT` occurrence is 150 chars and
  truncated mid-word against the other two at 188, so the fix has to repair a
  truncation as well as reconcile the level.
- **#350 — isolates are gated for schema only.** All **4 of 4** fail
  `linkml-term-validator --labels`, but the failures are mostly wrong *id*, not
  wrong label (`CHEBI:30319` recorded as `dicyanoaurate(1-)`; `ENVO:00000072` as
  `mine tailing`; `GO:0055114`/`GO:0055065` obsolete). Choosing the right id per
  term is triage, not transcription — `id-label-correspondence` prescribes
  `validate_ncbitaxon_ids.py` and `term_fix_apply.py` for it, but choosing per
  term still needs a call. The other branch — documenting the roots as
  schema-only — is mechanical, so the brief must name which branch to take.
- **#277 — four dangling `[[wiki-links]]`.** Looks like doc hygiene, but the issue
  offers three mutually exclusive remedies (inline the substance, point at a
  committed doc, or drop the links) and the substance lives in a memory directory
  the issue records as absent. "No dangling links" is satisfiable by deletion,
  which throws away what the issue calls load-bearing. Brief which remedy.
- **#270 — interaction type encoded by colour alone**, nine categories. Fully
  specified, and the CVD-simulation harness from #268 already exists to verify a
  redundant encoding. Frontend, self-contained.
- **#352b — a second coarse SPRUCE record (`000135`) already exists.** Only the
  *report* is loop-able; whether to merge the two records is a curator call.

## Queued — mechanical, but blocked

**#358 — guard the goal prompt's size limit.** Mechanical, but
it asserts a limit on a file [PR #357](https://github.com/CultureBotAI/CommunityMech/pull/357)
is still changing — on `main` the prompt is 3987 chars / 4015 bytes (13 spare),
and #357 takes it to 3995 / 4021. Note 4015 bytes is *already over* 4000, so if
the ceiling counts bytes rather than characters the file has been over all along;
that is the open question #358 exists to settle. Do it once #357 lands.

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
| #325 | Backfill `curation_history` to the other 310 of 312, or drop the slot? |
| #355 | Is interaction 1 `COMMENSALISM`/`CROSS_FEEDING` rather than `MUTUALISM`? |
| #356 | Does the ECM entry mean nutrients *from* the host or *to* it? |
| #182 | Which best-effort ontology remaps to accept |
| #199 | Which dataviz findings to act on |

**#319 is decided but heavy.** Hosts and antagonists become taxonomy members; the
`NCBITaxon:2` aggregate placeholders lose their participant slot instead. The
decision is [recorded on the issue](https://github.com/CultureBotAI/CommunityMech/issues/319#issuecomment-5173848793)
— the issue body still reads "unresolved", so cite the comment, not the body.

Measured over all 1127 participant slots, counting a participant as absent only
when its id appears nowhere in that record's `taxonomy`: **10 host/antagonist
slots across 8 records** to add, **13 placeholder slots across 8 records** to
drop, and **4 name variants** of existing members to reconcile. That reproduces
the 23 in the issue body; an earlier draft here said 13 and 14, which came from
the *auditor's* looser rule and counted members whose name merely differs. The 10
each need a grounded term and a snippet, so this is a focused session, not a
loop.

## Ordering and dependencies

- **#358 waits for [#357](https://github.com/CultureBotAI/CommunityMech/pull/357)
  to merge** — it asserts a limit on the file that PR is still changing.
- **#347, #355, #356 all edit `SPRUCE_Peatland_Warming_Community.yaml`.** One PR,
  or strictly serial; the loop's one-PR-in-flight rule handles this if they are
  not queued together.
- **#314 before #294.** #314 is the data fix; #294 is the schema that would
  describe it. Doing the data first keeps the enum backfill honest.
- **#352a cannot close #352** — that issue also carries the duplicate-SPRUCE
  question (#352b), which is a curator call. Expect the loop's "issue closed"
  finish condition not to fire; split the issue first, or accept a partial.
- **#290 retires a gotcha** in `prompts/backlog-loop.goal.md`. Whoever fixes it
  updates the prompt in the same PR — the prompt's own header says so.

## Never loop these

- Anything needing full text the repo cannot fetch (**#183**, and the blocked
  half of **#259**).
- Anything editing sibling repos (**#30** touches cross-Mech linking; the loop is
  scoped to this repo and must only report divergence).
