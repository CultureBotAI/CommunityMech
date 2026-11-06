# Cycle 4 Stage 6 — Infrastructure Validation Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `4`
- **Stage**: `6` (`infrastructure`)
- **Revision**: `1`
- **Source Revision**: `fb5cbe66b8e19daed26b32ab96316af75c3ec961`
- **Frozen Scope Timestamp**: `2026-11-01T01:43:10Z`
- **Frozen `INFRA_TASKS.md` SHA-256**: `ea5df4865a121d43a16f45577c248f285e5e2a81e094ef8e6a7043a209f8069f`

## 1. Frozen Scope & Workflow Profile Verification

- **Frozen `INFRA_TASKS.md` / `infra_snapshot.md` SHA-256**:
  - `INFRA_TASKS.md`: `ea5df4865a121d43a16f45577c248f285e5e2a81e094ef8e6a7043a209f8069f`
  - `reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-06/revision-0001/infra_snapshot.md`: `ea5df4865a121d43a16f45577c248f285e5e2a81e094ef8e6a7043a209f8069f`
  - Status of all 4 tasks (`communitymech-infra-0001` [`#2055`], `communitymech-infra-0002` [`#2056`], `communitymech-infra-0003` [`#2057`], `communitymech-infra-0004` [`#2063`]): `resolved` (`0` open/note/deferred tasks at freeze cutoff `2026-11-01T01:43:10Z`).
- **Workflow Profile Validation (`workflow/mech-workflow.yaml`)**:
  - Command:
    ```bash
    PYTHONPATH="/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/src" \
      "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/python" -c '
    from pathlib import Path
    from kg_microbe_workflows import load_effective_workflow
    root = Path("/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech")
    wf = load_effective_workflow(root, root / "workflow/mech-workflow.yaml")
    print("Workflow profile valid:", wf.profile.id, "stages:", len(wf.stages))
    '
    ```
  - Result: `Workflow profile valid: communitymech stages: 6` (exit `0`).

## 2. Stage 6 Infrastructure & Corpus-Invariant Regression Suite

- **Commands**:
  ```bash
  ./.venv/bin/pytest -o cache_dir=/tmp/pytest_cache \
    tests/test_stage6_infrastructure.py \
    tests/test_community_level_connectivity_credit.py \
    tests/test_causal_review_batch109.py \
    tests/test_participating_taxa.py \
    tests/test_okeke_participant_census.py \
    tests/test_gtdb_coherence_validator.py \
    tests/test_is_reclassified_semantics.py \
    tests/test_transwell_participants.py \
    tests/test_record_review_contract.py -v

  UV_NO_SYNC=1 ./.venv/bin/pytest -o cache_dir=/tmp/pytest_cache \
    tests/test_record_review_contract.py \
    tests/test_gtdb_coherence_validator.py \
    -k "linkml or validate_strict or test_review_skill or test_every_saved or test_shared_saver" -v
  ```
- **Results**:
  - `138 passed, 1 skipped` across `139` collected items (`0` failures):
    - `tests/test_stage6_infrastructure.py`: `4 passed` (`test_infra_0001_downstream_edge_contract_and_decision_provenance`, `test_infra_0002_build_sequence_map_projects_commontaxon_genes`, `test_infra_0003_audit_completeness_and_seatbelt_safe_root`, `test_infra_0004_corpus_count_decoupling_preserves_invariants`).
    - `tests/test_community_level_connectivity_credit.py`: `6 passed`.
    - `tests/test_causal_review_batch109.py`: `12 passed`.
    - `tests/test_participating_taxa.py`: `9 passed`.
    - `tests/test_okeke_participant_census.py`: `1 passed`.
    - `tests/test_gtdb_coherence_validator.py`: `56 passed, 1 skipped` (only `test_prokaryote_only_catches_a_eukaryote_carrying_a_gtdb_block` skipped when local OAK NCBITaxon SQLite is absent).
    - `tests/test_is_reclassified_semantics.py`: `18 passed`.
    - `tests/test_transwell_participants.py`: `28 passed`.
    - `tests/test_record_review_contract.py`: `4 passed`.

## 3. Repository Quality Gates

- **Strict Corpus Validation (`scripts/validate_strict.py`)**:
  - Command: `PYTHONPATH=src ./.venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv`
  - Result: `files scanned: 490`, `files with ERROR: 0`, `total ERROR rows: 0` (`481` community records in `kb/communities/*.yaml` + `9` isolate records in `data/isolates/*.yaml`).
- **Ecological Network Audit (`communitymech audit-network --check-only`)**:
  - Command: `./.venv/bin/communitymech audit-network --check-only`
  - Result: `0 error, 44 warning` across `490` community/isolate records (unchanged baseline).
- **Linting, Formatting, and Static Typing (`ruff`, `black`, `mypy`)**:
  - Command: `./.venv/bin/ruff check --no-cache src/ tests/ scripts/ && ./.venv/bin/black --check src/ tests/ scripts/ && ./.venv/bin/mypy --cache-dir=/tmp/mypy_cache src/`
  - Result:
    - `ruff`: `All checks passed!`
    - `black`: `All done! 409 files would be left unchanged.`
    - `mypy`: `Success: no issues found in 49 source files`
