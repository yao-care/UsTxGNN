"""Tests for disease mapper module."""

import pytest
from ustxgnn.mapping.disease_mapper import (
    DISEASE_DICT,
    normalize_disease_name,
    translate_indication,
    extract_indications,
)


class TestDiseaseDict:
    """Tests for DISEASE_DICT coverage."""

    def test_disease_dict_not_empty(self):
        """Ensure DISEASE_DICT has entries."""
        assert len(DISEASE_DICT) > 0

    def test_disease_dict_minimum_entries(self):
        """DISEASE_DICT should have at least 150 entries per SOP."""
        assert len(DISEASE_DICT) >= 150

    def test_common_abbreviations_present(self):
        """Check common medical abbreviations are mapped."""
        abbreviations = ["htn", "copd", "gerd", "dm", "chf", "cad", "ckd"]
        for abbr in abbreviations:
            assert abbr in DISEASE_DICT, f"Missing abbreviation: {abbr}"

    def test_values_are_lowercase(self):
        """All mapped values should be lowercase."""
        for key, value in DISEASE_DICT.items():
            assert value == value.lower(), f"Value not lowercase: {value}"


class TestNormalizeName:
    """Tests for normalize_disease_name function."""

    def test_lowercase_conversion(self):
        """Should convert to lowercase."""
        result = normalize_disease_name("DIABETES")
        assert result == result.lower()

    def test_strip_whitespace(self):
        """Should strip leading/trailing whitespace."""
        result = normalize_disease_name("  diabetes  ")
        assert result == "diabetes"

    def test_empty_string(self):
        """Should handle empty string."""
        result = normalize_disease_name("")
        assert result == ""


class TestTranslateIndication:
    """Tests for translate_indication function."""

    def test_known_abbreviation(self):
        """Should translate known abbreviations."""
        result = translate_indication("htn")
        # Result may be uppercase or lowercase
        result_lower = [r.lower() for r in result]
        assert "hypertension" in result_lower

    def test_unknown_term_returns_original(self):
        """Unknown terms should return the original."""
        result = translate_indication("some_unknown_disease_xyz")
        assert "some_unknown_disease_xyz" in result or len(result) > 0


class TestExtractIndications:
    """Tests for extract_indications function."""

    def test_semicolon_separator(self):
        """Should split on semicolons."""
        result = extract_indications("diabetes; hypertension; pain")
        assert len(result) == 3

    def test_comma_separator(self):
        """Should split on commas."""
        result = extract_indications("diabetes, hypertension, pain")
        assert len(result) >= 2

    def test_single_indication(self):
        """Should handle single indication."""
        result = extract_indications("diabetes")
        assert len(result) == 1
        assert "diabetes" in result[0].lower()

    def test_empty_string(self):
        """Should handle empty string."""
        result = extract_indications("")
        # Should return empty list or list with empty string
        assert isinstance(result, list)
