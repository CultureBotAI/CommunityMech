"""Guard current interaction semantics without erasing prior review evidence."""

import hashlib
import re
import subprocess
from copy import deepcopy
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261007-five-records-batch91.yaml"
SCHEMA_PATH = "src/communitymech/schema/communitymech.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in rows]


def assert_primary_artifact_hashes(ledger, root=ROOT):
    for path, digest in ledger["primary_artifacts"].items():
        if path.startswith("/"):
            continue
        if path == SCHEMA_PATH:
            # The schema is a historical review input, not a frozen live file (#1984).
            base = ledger["base_commit"]
            assert re.fullmatch(r"[0-9a-f]{40}", base), "Expected an immutable review base"
            tree = subprocess.check_output(
                ["git", "-C", str(root), "rev-parse", f"{base}^{{tree}}"], text=True
            ).strip()
            assert tree == ledger["base_tree"], "Historical review tree mismatch"
            content = subprocess.check_output(["git", "-C", str(root), "show", f"{base}:{path}"])
        else:
            content = (root / path).read_bytes()
        assert hashlib.sha256(content).hexdigest() == digest, path


def test_ufmp_preserves_hypothesized_cross_feeding_without_obligacy_requirement():
    ledger, _, docs = records()
    definition = yaml.safe_load((ROOT / "src/communitymech/schema/communitymech.yaml").read_text())[
        "enums"
    ]["InteractionTypeEnum"]["permissible_values"]["SYNTROPHY"]["description"]
    assert ledger["schema_definition"] == definition
    assert "Obligacy is not asserted." in definition
    transfer = docs[2]["ecological_interactions"][2]
    assert transfer["interaction_type"] == "CROSS_FEEDING"
    assert transfer["description"].startswith("HYPOTHESIZED:")
    assert "does not require obligacy" in transfer["description"]
    assert "product-removal feedback" in transfer["description"]
    assert len(transfer["evidence"]) == 2
    assert all(
        e["supports"] == "PARTIAL" and e["evidence_source"] == "COMPUTATIONAL"
        for e in transfer["evidence"]
    )


def test_digestion_keeps_positive_results_but_does_not_restore_unresolved_syntrophy():
    _, _, docs = records()
    staged, transfer, selection = docs[3]["ecological_interactions"]
    assert "22%" in staged["description"] and "8%" in staged["description"]
    assert "interaction_type" not in transfer and "interaction_type" not in selection
    assert "unresolved feedback mechanism, not unproven obligacy" in transfer["description"]
    assert "does not establish transcription" in transfer["description"]


def test_pleuromutilin_endpoint_is_not_a_feedback_mechanism():
    _, _, docs = records()
    doc = docs[4]
    endpoint, products = doc["ecological_interactions"]
    assert "91.97%" in endpoint["description"]
    assert "SYNTROPHY does not require obligacy" in endpoint["description"]
    assert all("interaction_type" not in n and "downstream" not in n for n in [endpoint, products])
    assert "engineering_design" not in doc
    assert "workflow remains in the record description" in doc["discussions"][-1]["rationale"]
    assert "no new structure is added" in doc["discussions"][-1]["rationale"]


def test_mfc_and_crystal_geyser_reviews_do_not_force_unnecessary_record_changes():
    _, rows, docs = records()
    for row, doc in zip(rows[:2], docs[:2], strict=True):
        assert row["outcome"] == "unchanged" and row["allowed_changed_fields"] == []
        assert row["original_sha256"] == row["record_sha256"]
        assert row["curation_events_added"] == 0 and row["history_files"] == []
        assert any(
            n.get("interaction_type") == "CROSS_FEEDING" for n in doc["ecological_interactions"]
        )


def test_existing_nodes_arrows_and_participant_assignments_remain_covered():
    _, rows, docs = records()
    assert sum(len(r["node_decisions"]) for r in rows) == 14
    assert sum(len(r["edges_after"]) for r in rows) == 7
    for row, doc in zip(rows, docs, strict=True):
        assert row["edges_before"] == row["edges_after"]
        assert not row["removed_node_decisions"] and not row["removed_edge_decisions"]
        assert {r["node"] for r in row["node_decisions"]} == {
            n["name"] for n in doc["ecological_interactions"]
        }
    assert [len(n["participating_taxa"]) for n in docs[2]["ecological_interactions"]] == [6, 3, 5]


def test_current_hashes_extend_the_immutable_prior_review_chain():
    _, rows, _ = records()
    for row in rows:
        link = row["supersedes_review"]
        prior = yaml.safe_load((ROOT / link["review_file"]).read_text())
        old = next(r for r in prior["records"] if r["path"] == row["path"])
        assert old["id"] == row["id"]
        assert old["record_sha256"] == link["record_sha256"] == row["original_sha256"]
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]


def test_unchanged_coverage_history_and_unfinished_research_are_explicit():
    ledger, rows, docs = records()
    assert not ledger["independent_approval"] and ledger["issues"] == [1744]
    assert ledger["unresolved_research_issues"] == [1715]
    assert rows[4]["status"] == "needs_research"
    assert [r["curation_events_added"] for r in rows] == [0, 0, 1, 1, 1]
    assert sum(len(r["history_files"]) for r in rows) == 3
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert ledger["edison"]["dry_runs"] == []
    for row, doc in zip(rows[2:], docs[2:], strict=True):
        assert doc["curation_history"][-1]["llm_assisted"]
        assert doc["curation_history"][-1]["action"] == "REVIEW_INTERACTION_SEMANTICS"
        assert (ROOT / row["history_files"][0]).is_file()


def test_unrelated_lookup_is_excluded_and_all_target_quotes_have_primary_matches():
    ledger, _, _ = records()
    assert ledger["excluded_source_lookup"]["pmid"] == "33125214"
    assert ledger["excluded_source_lookup"]["excluded_from_target_evidence"]
    assert len(ledger["source_access"]) == 6
    assert all(r["reference"] != "PMID:33125214" for r in ledger["source_access"])
    assert ledger["primary_graph_snippet_count"] == len(ledger["snippet_checks"]) == 23
    assert len(ledger["discussion_snippet_checks"]) == 2
    assert all(
        p["independent_primary_match"] and p["cache_matched"]
        for p in ledger["snippet_checks"] + ledger["discussion_snippet_checks"]
    )
    assert ledger["cache_changes"] == []
    assert_primary_artifact_hashes(ledger)


@pytest.fixture
def artifact_repository(tmp_path):
    contents = {
        SCHEMA_PATH: b"name: historical_schema\n",
        "references_cache/fixture.txt": b"Original evidence text.\n",
    }
    for path, content in contents.items():
        target = tmp_path / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
    for args in (
        ["init"],
        ["config", "user.name", "Provenance fixture"],
        ["config", "user.email", "fixture@example.invalid"],
        ["add", *contents],
        ["commit", "-m", "Historical review inputs"],
    ):
        subprocess.run(["git", "-C", str(tmp_path), *args], check=True, capture_output=True)
    return tmp_path, {
        "base_commit": subprocess.check_output(
            ["git", "-C", str(tmp_path), "rev-parse", "HEAD"], text=True
        ).strip(),
        "base_tree": subprocess.check_output(
            ["git", "-C", str(tmp_path), "rev-parse", "HEAD^{tree}"], text=True
        ).strip(),
        "primary_artifacts": {
            path: hashlib.sha256(content).hexdigest() for path, content in contents.items()
        },
    }


def test_historical_schema_guard_allows_current_schema_evolution(artifact_repository):
    root, ledger = artifact_repository
    assert_primary_artifact_hashes(ledger, root)
    schema = root / SCHEMA_PATH
    original = schema.read_bytes()
    schema.write_bytes(original + b"description: Later compatible extension\n")
    assert schema.read_bytes() != original
    assert_primary_artifact_hashes(ledger, root)


@pytest.mark.parametrize("path", [SCHEMA_PATH, "references_cache/fixture.txt"])
def test_primary_artifact_guard_detects_corrupt_hashes(artifact_repository, path):
    root, ledger = artifact_repository
    assert_primary_artifact_hashes(ledger, root)
    altered = deepcopy(ledger)
    altered["primary_artifacts"][path] = "0" * 64
    assert altered["primary_artifacts"][path] != ledger["primary_artifacts"][path]
    with pytest.raises(AssertionError, match=re.escape(path)):
        assert_primary_artifact_hashes(altered, root)
    assert_primary_artifact_hashes(ledger, root)


def test_primary_artifact_guard_detects_changed_current_evidence(artifact_repository):
    root, ledger = artifact_repository
    assert_primary_artifact_hashes(ledger, root)
    evidence = root / "references_cache/fixture.txt"
    original = evidence.read_bytes()
    evidence.write_bytes(b"Changed evidence.\n")
    assert evidence.read_bytes() != original
    with pytest.raises(AssertionError, match="references_cache/fixture.txt"):
        assert_primary_artifact_hashes(ledger, root)
    evidence.write_bytes(original)
    assert_primary_artifact_hashes(ledger, root)


@pytest.mark.parametrize("field", ["base_commit", "base_tree"])
def test_historical_schema_guard_fails_closed_on_missing_provenance(artifact_repository, field):
    root, ledger = artifact_repository
    assert_primary_artifact_hashes(ledger, root)
    altered = deepcopy(ledger)
    altered[field] = "0" * 40
    assert altered[field] != ledger[field]
    with pytest.raises((AssertionError, subprocess.CalledProcessError)):
        assert_primary_artifact_hashes(altered, root)
    assert_primary_artifact_hashes(ledger, root)
