"""
Network integrity auditor for microbial community YAML files.

Checks for:
1. NCBITaxon ID mismatches between taxonomy and interactions
2. Missing source_taxon or target_taxon in interactions
3. Interactions referencing taxa not in taxonomy section
4. Disconnected taxa (no interactions involving them)
"""

import json
import sys
from collections import defaultdict
from enum import Enum
from pathlib import Path

import yaml


class IssueType(str, Enum):
    """Types of network integrity issues."""

    ID_MISMATCH = "ID_MISMATCH"
    MISSING_SOURCE = "MISSING_SOURCE"
    UNKNOWN_SOURCE = "UNKNOWN_SOURCE"
    UNKNOWN_TARGET = "UNKNOWN_TARGET"
    NAME_MISMATCH = "NAME_MISMATCH"
    DANGLING_EDGE = "DANGLING_EDGE"
    DANGLING_ANCHOR = "DANGLING_ANCHOR"
    DISCONNECTED = "DISCONNECTED"
    UNREADABLE = "UNREADABLE"


# Severity per issue type, using the "error"/"warning" vocabulary already in
# `network/validators.py`.
#
# The split is between *the record contradicting itself* and *the record being
# incomplete*. Everything at error level names something that is not there: an
# interaction citing a taxon the record does not list, a causal edge or
# discussion anchor pointing at an interaction that does not exist, an id that
# disagrees with the taxonomy entry it refers to. Those are objectively broken
# and no amount of further curation makes them correct.
#
# `NAME_MISMATCH` and `DISCONNECTED` are different in kind. The first says the
# participant was matched by its ontology id because its name matched no entry:
# usually the paper's own shorthand, occasionally a name left behind by an edit,
# and the auditor cannot tell which — so it reports rather than resolving
# silently (#317), and does not gate on what is legitimate most of the time.
#
# The second is a curated member that no interaction yet mentions. Nothing is
# inconsistent — the record simply says less than it could, and for field and
# natural communities that is the normal state rather than a defect. It stays
# reported and stays out of the gate (#273).
SEVERITY: dict[str, str] = {
    "UNREADABLE": "error",
    "ID_MISMATCH": "error",
    "MISSING_SOURCE": "error",
    "UNKNOWN_SOURCE": "error",
    "UNKNOWN_TARGET": "error",
    "NAME_MISMATCH": "warning",
    "DANGLING_EDGE": "error",
    "DANGLING_ANCHOR": "error",
    "DISCONNECTED": "warning",
}

# Distinct exit codes, because CI has to tell three outcomes apart that a plain
# non-zero cannot: findings that should block, findings that should only be
# reported, and the auditor failing to run at all.
EXIT_CLEAN = 0
EXIT_WARNINGS = 1
EXIT_CRASH = 2
EXIT_ERRORS = 3


def _type_label(issue_type) -> str:
    """Render an issue type as its bare value, on every Python.

    ``IssueType`` is a ``str``-mixin enum, and the mixin's ``__format__``
    switched in Python 3.11 from emitting the *value* to emitting the qualified
    ``IssueType.NAME``. Interpolating a member directly therefore produced
    different report text under 3.10 (CI) than under 3.14 (a dev venv). Entries
    are occasionally plain strings, so fall back to the object itself.
    """
    return getattr(issue_type, "value", issue_type)


def severity_of(issue_type) -> str:
    """Severity for an issue type, defaulting to error for anything unmapped.

    A new `IssueType` added without a `SEVERITY` entry gates rather than passes
    silently — the safe direction for a check whose job is catching breakage.
    """
    return SEVERITY.get(_type_label(issue_type), "error")


class NetworkIntegrityAuditor:
    """Audit community YAML files for network data integrity issues."""

    def __init__(self, communities_dir: Path = Path("kb/communities")):
        self.communities_dir = Path(communities_dir)
        self.issues: dict[str, list[dict]] = defaultdict(list)

    def audit_all(self, check_only: bool = False, quiet: bool = False) -> dict[str, list[dict]]:
        """
        Audit all community YAML files.

        Args:
            check_only: If True, exit non-zero when issues are found (CI mode):
                EXIT_ERRORS if any error-severity issue exists, else
                EXIT_WARNINGS.
            quiet: Suppress the human-readable report. Needed by ``--json``,
                which otherwise emitted the report and the JSON to the same
                stdout, so ``audit-network --json > out.json`` produced a file
                that was not JSON (#273).

        Returns:
            Dictionary mapping community names to their issues
        """
        yaml_files = sorted(self.communities_dir.glob("*.yaml"))
        verbose = not (check_only or quiet)

        if verbose:
            print(f"\n🔍 Auditing {len(yaml_files)} communities for network integrity issues...\n")

        total_issues = 0
        communities_with_issues = 0

        for yaml_file in yaml_files:
            # One unreadable file must not abort the sweep. Before this, a single
            # malformed YAML propagated out of the loop, so the remaining records
            # went unaudited *and* no report was written — the audit produced
            # nothing precisely when something was wrong. Record it as a finding
            # against that record instead and carry on.
            try:
                issues = self.audit_community(yaml_file)
            except Exception as exc:
                issues = [
                    {
                        "type": IssueType.UNREADABLE,
                        "message": f"Could not audit this file: {' '.join(str(exc).split())}",
                    }
                ]
            if issues:
                self.issues[yaml_file.stem] = issues
                communities_with_issues += 1
                total_issues += len(issues)
                if verbose:
                    self.report_community_issues(yaml_file.stem, issues)

        # Catching per file keeps one bad record from ending the sweep, but it
        # would also turn a bug in this auditor into "every record is bad data".
        # Nothing legitimate makes *all* of them unreadable at once, so treat
        # that as a tool failure and let it out: the CLI turns it into exit 2
        # with no report, which the network-quality workflow reports as a crash
        # rather than as findings.
        unreadable = sum(
            1
            for community_issues in self.issues.values()
            if any(issue["type"] == IssueType.UNREADABLE for issue in community_issues)
        )
        if len(yaml_files) > 1 and unreadable == len(yaml_files):
            raise RuntimeError(
                f"every one of the {len(yaml_files)} community files failed to audit — "
                f"this is a failure of the auditor, not of the data"
            )

        if verbose:
            print(f"\n{'='*80}")
            print(f"Summary: {communities_with_issues}/{len(yaml_files)} communities have issues")
            print(f"Total issues found: {total_issues}")
            print(f"{'='*80}\n")

        # In check-only mode, exit non-zero when issues are found — but say
        # *which kind* through the exit code, so CI can gate on breakage while
        # still surfacing incompleteness (#273). A plain exit 1 could not
        # express that difference, which is why the workflow had to stay
        # reporting-only.
        if check_only and total_issues > 0:
            errors = self.count_by_severity()["error"]
            print(
                f"❌ Found {total_issues} network integrity issues "
                f"({errors} error, {total_issues - errors} warning)",
                file=sys.stderr,
            )
            sys.exit(EXIT_ERRORS if errors else EXIT_WARNINGS)

        return self.issues

    def count_by_severity(self) -> dict[str, int]:
        """Count findings by severity across every audited community."""
        counts = {"error": 0, "warning": 0}
        for community_issues in self.issues.values():
            for issue in community_issues:
                counts[severity_of(issue["type"])] += 1
        return counts

    def audit_community(self, yaml_path: Path) -> list[dict]:
        """
        Audit a single community file.

        Args:
            yaml_path: Path to community YAML file

        Returns:
            List of issue dictionaries
        """
        with open(yaml_path) as f:
            data = yaml.safe_load(f)

        issues = []

        # Build taxonomy lookup by preferred_term, plus a secondary index by
        # ontology id.
        taxonomy_by_term = {}
        taxonomy_keys_by_id: dict[str, list[str]] = defaultdict(list)
        for taxon in data.get("taxonomy") or []:
            term = taxon.get("taxon_term", {})
            preferred = term.get("preferred_term") or term.get("term", {}).get("label")
            taxon_id = term.get("term", {}).get("id")

            if preferred:
                taxonomy_by_term[preferred] = {
                    "id": taxon_id,
                    "label": term.get("term", {}).get("label"),
                    "taxon_data": taxon,  # Store full taxon data for context
                }
                if taxon_id:
                    taxonomy_keys_by_id[taxon_id].append(preferred)

        def resolve_member(name: str | None, taxon_id: str | None) -> tuple[str | None, bool]:
            """Match an interaction participant to its taxonomy entry.

            Returns the taxonomy key and whether the id fallback was what
            matched it — the caller reports the latter as NAME_MISMATCH, because
            the fallback cannot tell a paper's shorthand from a stale name and
            must not resolve either one silently (#317).

            Name first, because `preferred_term` is the only thing that separates
            two members sharing one ontology id: `Lotus_LjSC3` carries three
            distinct strains — LjNodule210/215/218 — all on NCBITaxon:68287,
            since NCBI has no strain-level term for them. Resolving by id would
            collapse the three onto whichever came first and report the other two
            as taking part in nothing.

            Only when the name matches no entry does the id decide, and only if
            exactly one entry carries it. That covers the other direction:
            `preferred_term` is free text preserving a paper's own name, so an
            interaction may say "ANME-1" where taxonomy says "ANME-1 (anaerobic
            methanotrophic archaea, clade 1)" for the same NCBITaxon:588814.
            Name-only matching reported all four such pairs as dangling
            references (#315). An id shared by several entries stays unresolved —
            the record genuinely does not say which member is meant.
            """
            if name and name in taxonomy_by_term:
                return name, False
            if taxon_id:
                candidates = taxonomy_keys_by_id.get(taxon_id, [])
                if len(candidates) == 1:
                    return candidates[0], True
            return None, False

        # Check each interaction
        interactions = data.get("ecological_interactions") or []

        # Track which taxa are connected, keyed by preferred_term like taxonomy_by_term
        connected_taxa: set[str] = set()

        for idx, interaction in enumerate(interactions):
            int_name = interaction.get("name", f"Interaction {idx+1}")
            scope = interaction.get("scope", "PAIRWISE")

            # A COMMUNITY_LEVEL interaction asserts a relationship holding across
            # the community rather than between a named pair, so every member
            # participates in it. Without this, such interactions contributed no
            # connections at all and every taxon in the 107 records that use them
            # exclusively counted as disconnected by construction (#304).
            if scope == "COMMUNITY_LEVEL":
                connected_taxa.update(taxonomy_by_term)

            # Check source_taxon (only required for PAIRWISE interactions)
            source = interaction.get("source_taxon")
            if not source:
                if scope != "COMMUNITY_LEVEL":
                    issues.append(
                        {
                            "type": IssueType.MISSING_SOURCE,
                            "interaction": int_name,
                            "interaction_index": idx,
                            "message": "Interaction has no source_taxon",
                        }
                    )
            else:
                source_term = source.get("preferred_term") or source.get("term", {}).get("label")
                source_id = source.get("term", {}).get("id")

                source_key, source_by_id = resolve_member(source_term, source_id)
                if source_key is None:
                    if scope != "COMMUNITY_LEVEL":
                        issues.append(
                            {
                                "type": IssueType.UNKNOWN_SOURCE,
                                "interaction": int_name,
                                "interaction_index": idx,
                                "taxon": source_term,
                                "message": (
                                    f"Source taxon '{source_term}' not found in " "taxonomy section"
                                ),
                            }
                        )
                else:
                    connected_taxa.add(source_key)
                    if source_by_id:
                        # Matched on the id alone. Report it: the same shape
                        # covers a paper's shorthand and a name stranded by an
                        # edit, and binding the second one silently is how a
                        # genuine dangling reference disappears (#317).
                        issues.append(
                            {
                                "type": IssueType.NAME_MISMATCH,
                                "interaction": int_name,
                                "interaction_index": idx,
                                "taxon": source_term,
                                "role": "source",
                                "resolved_to": source_key,
                                "message": (
                                    f"Source '{source_term}' matches no taxonomy entry by name; "
                                    f"resolved to '{source_key}' by source_id {source_id}"
                                ),
                            }
                        )
                    # Check ID mismatch
                    expected_id = taxonomy_by_term[source_key]["id"]
                    if source_id != expected_id:
                        issues.append(
                            {
                                "type": IssueType.ID_MISMATCH,
                                "interaction": int_name,
                                "interaction_index": idx,
                                "taxon": source_term,
                                "role": "source",
                                "expected_id": expected_id,
                                "actual_id": source_id,
                                "message": (
                                    f"Source '{source_term}' has ID {source_id}, "
                                    f"expected {expected_id}"
                                ),
                            }
                        )

            # Check target_taxon (optional but if present should be valid)
            target = interaction.get("target_taxon")
            if target:
                target_term = target.get("preferred_term") or target.get("term", {}).get("label")
                target_id = target.get("term", {}).get("id")

                target_key, target_by_id = resolve_member(target_term, target_id)
                if target_key is None:
                    if scope != "COMMUNITY_LEVEL":
                        issues.append(
                            {
                                "type": IssueType.UNKNOWN_TARGET,
                                "interaction": int_name,
                                "interaction_index": idx,
                                "taxon": target_term,
                                "message": (
                                    f"Target taxon '{target_term}' not found in " "taxonomy section"
                                ),
                            }
                        )
                else:
                    connected_taxa.add(target_key)
                    if target_by_id:
                        # Matched on the id alone. Report it: the same shape
                        # covers a paper's shorthand and a name stranded by an
                        # edit, and binding the second one silently is how a
                        # genuine dangling reference disappears (#317).
                        issues.append(
                            {
                                "type": IssueType.NAME_MISMATCH,
                                "interaction": int_name,
                                "interaction_index": idx,
                                "taxon": target_term,
                                "role": "target",
                                "resolved_to": target_key,
                                "message": (
                                    f"Target '{target_term}' matches no taxonomy entry by name; "
                                    f"resolved to '{target_key}' by target_id {target_id}"
                                ),
                            }
                        )
                    # Check ID mismatch
                    expected_id = taxonomy_by_term[target_key]["id"]
                    if target_id != expected_id:
                        issues.append(
                            {
                                "type": IssueType.ID_MISMATCH,
                                "interaction": int_name,
                                "interaction_index": idx,
                                "taxon": target_term,
                                "role": "target",
                                "expected_id": expected_id,
                                "actual_id": target_id,
                                "message": (
                                    f"Target '{target_term}' has ID {target_id}, "
                                    f"expected {expected_id}"
                                ),
                            }
                        )

        # Check causal-graph edges and discussion anchors. Both name an
        # interaction by its `name` string, so a rename or deletion elsewhere in
        # the record leaves a reference pointing at nothing and the causal graph
        # silently loses an arc — nothing else in the pipeline notices.
        #
        # These two detectors were written in PR #260 but only ever existed in
        # `scripts/audit_network_integrity.py`, a copy of this auditor that no
        # recipe or workflow ran (#313). They are ported here, and that script is
        # deleted, so the checks run in CI for the first time.
        interaction_names = {
            interaction.get("name") for interaction in interactions if interaction.get("name")
        }

        for idx, interaction in enumerate(interactions):
            int_name = interaction.get("name", f"Interaction {idx+1}")
            for edge in interaction.get("downstream") or []:
                target_name = edge.get("target")
                if target_name and target_name not in interaction_names:
                    issues.append(
                        {
                            "type": IssueType.DANGLING_EDGE,
                            "interaction": int_name,
                            "interaction_index": idx,
                            "target": target_name,
                            "message": (
                                f"downstream target '{target_name}' does not name any "
                                f"interaction in this record"
                            ),
                        }
                    )

        for discussion in data.get("discussions") or []:
            disc_id = discussion.get("discussion_id", "<no id>")
            for anchor in discussion.get("attaches_to") or []:
                prefix = "ecological_interactions#"
                if anchor.startswith(prefix):
                    anchor_name = anchor[len(prefix) :]
                    if anchor_name not in interaction_names:
                        issues.append(
                            {
                                "type": IssueType.DANGLING_ANCHOR,
                                "interaction": disc_id,
                                "target": anchor_name,
                                "message": (
                                    f"discussion '{disc_id}' attaches to '{anchor_name}', "
                                    f"which does not name any interaction in this record"
                                ),
                            }
                        )

        # Check for disconnected taxa: members that take part in no interaction
        # of any scope.
        #
        # There used to be an exemption here for taxa carrying abundance_level or
        # functional_role, standing in for "described as a member even without an
        # edge". With COMMUNITY_LEVEL interactions now crediting their members,
        # that proxy is unnecessary — and it was harmful. It exempted 931 of 1007
        # taxa, so the rule effectively reported "lacks metadata" rather than
        # "lacks interactions", and it rewarded filling those slots: removing a
        # fabricated abundance_level created findings (#304).
        all_taxa = set(taxonomy_by_term.keys())
        disconnected = all_taxa - connected_taxa

        if disconnected and interactions:  # Only flag if there ARE interactions
            for taxon in sorted(disconnected):
                taxon_data = taxonomy_by_term[taxon]["taxon_data"]
                issues.append(
                    {
                        "type": IssueType.DISCONNECTED,
                        "taxon": taxon,
                        "taxon_id": taxonomy_by_term[taxon]["id"],
                        "taxon_data": taxon_data,  # Include for context building
                        "message": f"Taxon '{taxon}' has no interactions",
                    }
                )

        return issues

    def report_community_issues(self, community_name: str, issues: list[dict]):
        """
        Print issues for a community.

        Args:
            community_name: Name of the community
            issues: List of issue dictionaries
        """
        print(f"\n{'─'*80}")
        print(f"📋 {community_name}")
        print(f"{'─'*80}")

        # Group by type
        by_type = defaultdict(list)
        for issue in issues:
            by_type[issue["type"]].append(issue)

        # Report each type
        for issue_type in [
            IssueType.UNREADABLE,
            IssueType.ID_MISMATCH,
            IssueType.MISSING_SOURCE,
            IssueType.UNKNOWN_SOURCE,
            IssueType.UNKNOWN_TARGET,
            IssueType.NAME_MISMATCH,
            IssueType.DANGLING_EDGE,
            IssueType.DANGLING_ANCHOR,
            IssueType.DISCONNECTED,
        ]:
            if issue_type in by_type:
                print(f"\n  {issue_type.value}:")
                for issue in by_type[issue_type]:
                    if issue_type == IssueType.ID_MISMATCH:
                        print(f"    • [{issue['interaction']}] {issue['role']}: {issue['taxon']}")
                        print(
                            f"      Expected: {issue['expected_id']}, Found: {issue['actual_id']}"
                        )
                    elif issue_type == IssueType.DISCONNECTED:
                        print(f"    • {issue['taxon']} ({issue['taxon_id']})")
                    elif issue_type == IssueType.UNREADABLE:
                        print(f"    • {issue['message']}")
                    else:
                        print(f"    • [{issue.get('interaction', 'N/A')}] {issue['message']}")

        print(f"\n  Total issues: {len(issues)}")

    def to_json(self) -> str:
        """
        Export issues as JSON for programmatic consumption.

        Returns:
            JSON string of all issues
        """
        return json.dumps(self.issues, indent=2, default=str)

    def write_report(self, output_path: Path = Path("network_integrity_audit.txt")):
        """
        Write detailed report to file.

        Args:
            output_path: Path to write report
        """
        with open(output_path, "w") as f:
            f.write("Network Integrity Audit Report\n")
            f.write("=" * 80 + "\n\n")

            # Severity is on every line, and counted per record and overall.
            # The workflow pastes this report into a pull request comment whose
            # heading comes from the *aggregate* outcome, so without a per-line
            # marker one gating DANGLING_EDGE and nineteen non-gating
            # DISCONNECTED looked identical and the curator had no way to find
            # the blocker (#321).
            totals = self.count_by_severity()
            f.write(
                f"{totals['error']} error, {totals['warning']} warning "
                f"across {len(self.issues)} records\n"
            )
            f.write("Only error-severity findings fail the build.\n")

            for community, community_issues in sorted(self.issues.items()):
                f.write(f"\n{community}\n")
                f.write("-" * 80 + "\n")
                for issue in community_issues:
                    severity = severity_of(issue["type"])
                    f.write(f"  [{severity}] {_type_label(issue['type'])}: {issue['message']}\n")
                    if issue["type"] == "ID_MISMATCH":
                        f.write(
                            f"    Expected: {issue['expected_id']}, Found: {issue['actual_id']}\n"
                        )
                errors = sum(1 for i in community_issues if severity_of(i["type"]) == "error")
                f.write(
                    f"\nTotal: {len(community_issues)} issues "
                    f"({errors} error, {len(community_issues) - errors} warning)\n"
                )

        # stderr, not stdout: with --json both would otherwise share the
        # stream and the confirmation line would corrupt the JSON.
        print(f"\n✅ Detailed report written to {output_path}\n", file=sys.stderr)

    def get_community_data(self, community_path: Path) -> dict:
        """
        Load community data from YAML file.

        Args:
            community_path: Path to community YAML file

        Returns:
            Community data dictionary
        """
        with open(community_path) as f:
            return yaml.safe_load(f)

    def get_taxonomy_lookup(self, community_data: dict) -> dict[str, dict]:
        """
        Build taxonomy lookup from community data.

        Args:
            community_data: Community data dictionary

        Returns:
            Dictionary mapping taxon names to their data
        """
        taxonomy_by_term = {}
        for taxon in community_data.get("taxonomy", []):
            term = taxon.get("taxon_term", {})
            preferred = term.get("preferred_term") or term.get("term", {}).get("label")

            if preferred:
                taxonomy_by_term[preferred] = {
                    "id": term.get("term", {}).get("id"),
                    "label": term.get("term", {}).get("label"),
                    "taxon_data": taxon,
                }

        return taxonomy_by_term
