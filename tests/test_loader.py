"""Tests for FDA data loader module."""

import pytest
from pathlib import Path
import pandas as pd

from ustxgnn.data.loader import (
    load_field_config,
    load_fda_drugs,
    filter_active_drugs,
)


class TestFieldConfig:
    """Tests for field configuration loading."""

    def test_load_field_config(self):
        """Should load field config successfully."""
        config = load_field_config()
        assert isinstance(config, dict)

    def test_config_has_country_code(self):
        """Config should have country code."""
        config = load_field_config()
        assert "country_code" in config
        assert config["country_code"] == "US"

    def test_config_has_field_mapping(self):
        """Config should have field mapping."""
        config = load_field_config()
        assert "field_mapping" in config
        assert isinstance(config["field_mapping"], dict)

    def test_config_has_required_fields(self):
        """Config should have required field mappings."""
        config = load_field_config()
        required_fields = ["license_id", "brand_name_local", "ingredients"]
        for field in required_fields:
            assert field in config["field_mapping"], f"Missing field: {field}"


class TestLoadFdaDrugs:
    """Tests for FDA drugs data loading."""

    def test_load_fda_drugs_returns_dataframe(self):
        """Should return a DataFrame."""
        try:
            df = load_fda_drugs()
            assert isinstance(df, pd.DataFrame)
        except FileNotFoundError:
            pytest.skip("FDA data file not available")

    def test_fda_drugs_not_empty(self):
        """Loaded data should not be empty."""
        try:
            df = load_fda_drugs()
            assert len(df) > 0
        except FileNotFoundError:
            pytest.skip("FDA data file not available")

    def test_fda_drugs_has_expected_columns(self):
        """DataFrame should have expected columns based on config."""
        try:
            df = load_fda_drugs()
            config = load_field_config()

            # Check at least some mapped fields exist
            field_mapping = config["field_mapping"]
            found_fields = 0
            for standard_name, actual_name in field_mapping.items():
                if actual_name in df.columns:
                    found_fields += 1

            assert found_fields > 0, "No mapped fields found in DataFrame"
        except FileNotFoundError:
            pytest.skip("FDA data file not available")


class TestFilterActiveDrugs:
    """Tests for active drug filtering."""

    def test_filter_active_drugs_returns_dataframe(self):
        """Should return a DataFrame."""
        try:
            df = load_fda_drugs()
            active = filter_active_drugs(df)
            assert isinstance(active, pd.DataFrame)
        except FileNotFoundError:
            pytest.skip("FDA data file not available")

    def test_filter_active_drugs_not_larger_than_input(self):
        """Filtered data should not be larger than input."""
        try:
            df = load_fda_drugs()
            active = filter_active_drugs(df)
            assert len(active) <= len(df)
        except FileNotFoundError:
            pytest.skip("FDA data file not available")

    def test_filter_active_drugs_removes_withdrawn(self):
        """Should filter out withdrawn drugs."""
        try:
            df = load_fda_drugs()
            config = load_field_config()
            withdrawn_statuses = config.get("withdrawn_statuses", [])

            if withdrawn_statuses:
                active = filter_active_drugs(df)
                status_field = config["field_mapping"].get("status", "")

                if status_field and status_field in active.columns:
                    for status in withdrawn_statuses:
                        assert status not in active[status_field].values
        except FileNotFoundError:
            pytest.skip("FDA data file not available")
