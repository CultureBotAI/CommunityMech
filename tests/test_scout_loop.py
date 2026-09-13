import importlib.util
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "scout_loop.py"


def load_scout_loop():
    spec = importlib.util.spec_from_file_location("_scout_loop_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_loop_uses_the_scout_default_record_roots(tmp_path, monkeypatch):
    scout_loop = load_scout_loop()

    def build_dedup_index():
        return {
            "cited_pmids": set(),
            "cited_dois": set(),
            "name_token_sets": [],
        }

    monkeypatch.setattr(scout_loop.sc, "build_dedup_index", build_dedup_index)
    monkeypatch.setattr(scout_loop.sc, "query_epmc", lambda *args: [])
    monkeypatch.setattr(scout_loop.sc, "backfill_missing_dois", lambda *args: 0)

    result = scout_loop.main(
        [
            "--since",
            "2026",
            "--limit",
            "1",
            "--dry-streak",
            "1",
            "--out-dir",
            str(tmp_path),
        ]
    )

    assert result == 0
    assert (tmp_path / "scout-loop.md").exists()
    assert (tmp_path / "scout-loop-queue.json").exists()
