"""Exact-owner reuse must reject equal-count failures with changed evidence."""

import importlib.util
from copy import deepcopy
from pathlib import Path

import pytest

SOURCE = Path(__file__).parents[1] / "scripts/adhoc/reconcile_code006_reference_owners_20261115.py"
spec = importlib.util.spec_from_file_location("code006_reference_owners", SOURCE)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


@pytest.fixture
def evidence():
    source = {"kb/communities/a.yaml": b"id: A\n", "kb/communities/b.yaml": b"id: B\n"}
    observed, published, prior = [], [], []
    for path, raw in source.items():
        bad = path.endswith("a.yaml")
        item = {
            "path": "discussions[0].evidence[0].snippet",
            "reference": "PMID:1",
            "native_class": "SupportingReference",
            "status": "mismatched" if bad else "matched",
            "actually_compared": True,
            "cache": {
                "requested_path": "references_cache/PMID_1.txt",
                "sha256": "a" * 64,
                "content_type": "full_text",
            },
        }
        row = {"record": path, "assertions": [item], "native_issue_count": int(bad)}
        observed.append(row)
        published.append(
            {
                "record": path,
                "surfaces": 1,
                "compared": 1,
                "native_issues": int(bad),
                "status_counts": {item["status"]: 1},
                "native_classes": {},
            }
        )
        prior.append(
            {
                "record": path,
                "id": path,
                "record_sha256": m.digest(raw),
                "phase2_scope": True,
                "native_issues": int(bad),
                "failures": [m.failure(item)] if bad else [],
                "ownership": {"issues": [1996], "category": "Supplement routing"},
            }
        )
    counts = {
        "records_completed": 2,
        "snippet_surfaces": 2,
        "snippet_occurrences_compared": 2,
        "native_issues": 1,
    }
    summary = {
        "counts": counts,
        "status_counts": {"matched": 1, "mismatched": 1},
        "record_processing_complete": True,
        "assertion_coverage_complete": True,
        "native_exit_code": 1,
        "measurement_revision": "new",
        "records": published,
    }
    measured = {
        "measurement_valid": True,
        "counts": deepcopy(counts),
        "assertion_status_counts": deepcopy(summary["status_counts"]),
        "records": observed,
        "input_sha256": {path: m.digest(raw) for path, raw in source.items()},
    }
    return summary, measured, {"rows": prior, "measurement_revision": "old"}, source


def test_exact_current_occurrences_reuse_owners_and_keep_failure(evidence):
    summary, measured, prior, source = evidence
    result = m.reconcile(summary, measured, prior, source.__getitem__)
    assert result["exact_failure_tuple_reconciliation"] is True
    assert result["affected_records"] == result["native_exit_code"] == 1
    assert result["rows"][0]["ownership"]["issues"] == [1996]
    assert result["phase2"] == {
        "records": 2,
        "surfaces": 2,
        "compared": 2,
        "matched": 1,
        "native_issues": 1,
    }


@pytest.mark.parametrize(
    "key,value",
    [
        ("path", "discussions[1].evidence[0].snippet"),
        ("reference", "PMID:2"),
        ("native_class", "EvidenceItem"),
        ("cache_path", "references_cache/PMID_2.txt"),
        ("cache_sha256", "b" * 64),
        ("content_type", "abstract"),
    ],
)
def test_equal_counts_with_changed_occurrence_cannot_reuse_owner(evidence, key, value):
    summary, measured, prior, source = evidence
    item = measured["records"][0]["assertions"][0]
    if key in {"cache_path", "cache_sha256", "content_type"}:
        item["cache"][
            {"cache_path": "requested_path", "cache_sha256": "sha256"}.get(key, key)
        ] = value
    else:
        item[key] = value
    with pytest.raises(ValueError, match="occurrence or source binding"):
        m.reconcile(summary, measured, prior, source.__getitem__)


def test_changed_affected_record_bytes_refuse_even_when_tuples_match(evidence):
    summary, measured, prior, source = evidence
    source["kb/communities/a.yaml"] += b"notes: changed\n"
    with pytest.raises(ValueError, match="affected record bytes changed"):
        m.reconcile(summary, measured, prior, source.__getitem__)


def test_duplicate_rows_refuse(evidence):
    summary, measured, prior, source = evidence
    measured["records"].append(deepcopy(measured["records"][0]))
    with pytest.raises(ValueError, match="duplicate"):
        m.reconcile(summary, measured, prior, source.__getitem__)


def test_comparison_flag_is_not_a_truthy_counter(evidence):
    summary, measured, prior, source = evidence
    measured["records"][0]["assertions"][0]["actually_compared"] = 1
    with pytest.raises(ValueError, match="comparison flag"):
        m.reconcile(summary, measured, prior, source.__getitem__)


def test_raw_and_published_counts_must_reconcile(evidence):
    summary, measured, prior, source = evidence
    measured["counts"]["snippet_occurrences_compared"] = 1
    with pytest.raises(ValueError, match="aggregate counters"):
        m.reconcile(summary, measured, prior, source.__getitem__)
