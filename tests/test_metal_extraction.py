"""Tests for the metal/REE keyword-matching extractor.

These cases exist because the original implementation used plain
substring matching against short element symbols (`ti`, `au`), which
falsely produced TITANIUM in 56/67 metals_present-annotated community
YAMLs (matched inside `characteristic`, `kinetic`, etc.) and GOLD in
unrelated communities (`Australia`, `author`). The fix anchors keyword
matches on non-alphanumeric boundaries.
"""

from communitymech.metal_extraction import keyword_in_text


class TestKeywordInText:
    def test_short_symbol_does_not_match_inside_word(self):
        assert not keyword_in_text("ti", "characteristic kinetic activity")
        assert not keyword_in_text("ti", "antibiotic resistance")
        assert not keyword_in_text("au", "australia author")
        assert not keyword_in_text("au", "haustoria autotroph")
        assert not keyword_in_text("pd", "phosphodiesterase")

    def test_short_symbol_matches_standalone(self):
        assert keyword_in_text("ti", "ti is a 4+ cation")
        assert keyword_in_text("au", "au is a noble metal")

    def test_chemical_form_matches(self):
        assert keyword_in_text("ti4+", "Ti4+ in solution")
        assert keyword_in_text("au3+", "au3+ recovered by biosorption")
        assert keyword_in_text("co(ii)", "Co(II) measured at 50 mg/L")

    def test_full_name_matches(self):
        assert keyword_in_text("titanium", "Titanium nanoparticles formed")
        assert keyword_in_text("gold", "gold extraction from PCBs")

    def test_full_name_does_not_match_substring(self):
        assert not keyword_in_text("iron", "environmental")
        assert not keyword_in_text("lead", "leadership")
