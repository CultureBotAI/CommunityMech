# Claude Code task: one CommunityMech deep-research curation

Work from the CommunityMech repository root. Read `CLAUDE.md`, any applicable
`AGENTS.md`, `history/README.md`, the LinkML schema, and the target community
before editing.

## Mission

Select exactly one researchable microbial-community interaction question, use
the `claude_code` deep-research provider once, and curate supported findings into
one schema-compliant `MicrobialCommunity` YAML record.

The Markdown report under `research/communities/` is the raw research artifact.
It is not the schema-compliant deliverable. Accepted findings must be represented
in the canonical community YAML and pass validation.

## Constraints

- Use only `claude_code`. Do not spend Falcon/Edison, Cyberian, or other provider
  credits, and do not switch providers on failure. Run one new job at most.
- Skip any candidate with an equivalent existing Claude Code report.
- Do not read, print, modify, or commit credentials or `.env`.
- Do not change the schema or validators to fit generated prose.
- Do not infer an interaction from co-occurrence alone. Direction, exchanged
  metabolites, functional roles, and downstream effects each need direct or
  clearly attributable source support.
- Keep natural communities, enrichments, isolates, and engineered consortia
  distinct. Do not generalize a strain-pair experiment to an entire environment.
- Never invent NCBI/GTDB/ENVO/CHEBI/GO identifiers, taxonomic membership,
  causal direction, citations, or snippets.

## 1. Pick one question

Inspect:

- `reports/knowledge_gap_scan.json` and `.md`, if present
- records in `kb/communities/`
- any relevant reusable taxon records in `kb/taxa/`
- existing `research/communities/**/*claude_code*` reports

Choose one existing community with a meaningful missing or weakly evidenced
ecological mechanism. Prefer a target whose membership and environment are
already usable but whose interaction, metabolite exchange, perturbation response,
or downstream consequence is incomplete. State its ID, name, YAML path,
selection rationale, and one precise question before starting research:

> Which source-backed interactions among the members of **<community>** explain
> its observed function or stability, including direction, exchanged metabolites
> or processes, conditions, and measurable downstream effects?

Do not run `knowledge-gap-scan --apply` or modify data during selection.

## 2. Check provider fit and run one job

Run:

```bash
just deep-research-provider claude_code ecological_mechanism
```

If unavailable, stop and do not fall back. Otherwise run exactly once:

```bash
just research-community claude_code <community-id-slug-or-yaml-path>
```

Capture the printed report and citations paths. Verify that the report is
non-empty and that important claims resolve to traceable sources. Do not retry a
failed/inconclusive job or manufacture YAML to make the session appear complete.

## 3. Curate into MicrobialCommunity YAML

Use the schema and strong neighboring records as structural guides. Make the
smallest evidence-backed edit to the chosen file under `kb/communities/`.

- Put member evidence on the corresponding taxonomy/member assertion.
- Represent ecological interactions with supported source/target direction,
  interaction type, metabolites/processes, and downstream effects only when
  each is evidenced.
- Use stable PMID/DOI identifiers. Add short verbatim snippets and explanations
  at the exact assertion they support.
- Verify ontology labels and CURIEs from authoritative local/source data. Leave
  a field absent or explicitly uncertain rather than guessing.
- Do not overwrite correct curated membership, environment, GTDB grounding, or
  experimental design with broader report language.
- If the literature supports only a related community or condition, reject the
  claim or model the distinction allowed by the current schema; never blur it.

Create the required append-only history record with `just new-history` following
`history/README.md`. Mark the work as LLM-assisted and reference both the target
and Claude Code raw report. Never revise old history records.

## 4. Validate

Run:

```bash
just validate <target-yaml-path>
just validate-strict <target-yaml-path>
just validate-references-explained <target-yaml-path>
just validate-gtdb <target-yaml-path>
just validate-gtdb-domain <target-yaml-path>
just validate-history <new-history-path>
```

Run `just audit-snippets` as an additional corpus-aware check when evidence was
added. Fix data or the new history entry, not validation rules or baselines. Do
not call deep research again. Finish with `git diff --check` and review the
focused diff.

## Completion report

Return the chosen question/rationale, provider check, single research command,
raw report/citations paths, canonical YAML and history paths, accepted/rejected
claims, validation outcomes, and any taxonomic or mechanistic uncertainty.

