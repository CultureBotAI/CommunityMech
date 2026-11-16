"""Actual historical census controls for #2947, 2026-11-16.

Read the real Git corpus and prove exact count/rank/bucket failures with
restoration; current semantic zero cases remain separately exercised.
"""

import pytest
import test_is_reclassified_semantics as semantics


def test_actual_dated_git_census_matches_the_original_contract():
    blocks = semantics._historical_blocks()
    semantics._assert_historical_census(blocks)
    assert len(blocks) == 143


@pytest.mark.parametrize("mutation", ["omit", "extra", "zero_bucket", "rank"])
def test_historical_population_mutations_refuse_and_restore(mutation):
    original = semantics._historical_blocks()
    semantics._assert_historical_census(original)
    changed = list(original)
    if mutation == "omit":
        changed.pop()
    elif mutation == "extra":
        changed.append(("Agrobacterium deltae", "Agrobacterium leguminum", "GTDB:s__extra"))
    elif mutation == "zero_bucket":
        changed[0] = ("Escherichia coli K-12", "Escherichia coli", "GTDB:s__Escherichia_coli")
    else:
        index = next(i for i, row in enumerate(changed) if row[2].startswith("GTDB:g__"))
        label, gtdb, _ = changed[index]
        changed[index] = (label, gtdb, "GTDB:s__invented_species")
    assert tuple(changed) != original
    with pytest.raises(AssertionError):
        semantics._assert_historical_census(changed)
    semantics._assert_historical_census(original)
