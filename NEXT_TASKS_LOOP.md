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

**#290, #358, #314 and #306 are done** (PRs #361, #362, #364, #368). **Start
with #352a** — seven records have no published page, one `just gen-html` away.

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
| #356 | Does the ECM entry mean nutrients *from* the host or *to* it? |
| #363 | Measure the real `/goal` ceiling, and decide whether it counts chars or bytes |
| #367 | Should `fetch_pubmed_abstract` return MEDLINE only, or normalise a `.md`? |
| #365 | Which NCBI id the two *Bosea* entries should carry — the current one is a plant |
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

- **#347 and #356 both edit `SPRUCE_Peatland_Warming_Community.yaml`.** One PR, or
  strictly serial.
- **#366 before any grounding backfill.** `gtdb_ground.py` is batch-sensitive —
  the same taxon can resolve differently per-record versus whole-KB — so a
  backfill run now would bake in whichever batch it happened to use.
- **#314 is done, so #294's backfill has correct data under it.**

## Never loop these

- Anything needing full text the repo cannot fetch (**#183**, and the blocked
  half of **#259**).
- Anything editing sibling repos (**#30** touches cross-Mech linking; the loop is
  scoped to this repo and must only report divergence).
