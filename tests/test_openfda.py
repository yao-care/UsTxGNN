"""Tests for OpenFDA collector module."""

import pytest
from unittest.mock import patch, MagicMock

from ustxgnn.collectors.openfda import OpenFDACollector
from ustxgnn.collectors.base import CollectorResult


class TestOpenFDACollector:
    """Tests for OpenFDACollector class."""

    def test_init_default(self):
        """Should initialize with default values."""
        collector = OpenFDACollector()
        assert collector.api_key is None
        assert collector.max_results == 50
        assert collector.source_name == "openfda"

    def test_init_with_params(self):
        """Should initialize with custom parameters."""
        collector = OpenFDACollector(api_key="test_key", max_results=100)
        assert collector.api_key == "test_key"
        assert collector.max_results == 100

    def test_search_returns_collector_result(self):
        """Search should return a CollectorResult."""
        collector = OpenFDACollector()

        with patch("requests.get") as mock_get:
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_response.json.return_value = {"results": []}
            mock_get.return_value = mock_response

            result = collector.search("aspirin")

            assert isinstance(result, CollectorResult)
            assert result.source == "openfda"
            assert result.query["drug"] == "aspirin"

    def test_search_with_disease(self):
        """Search should accept disease parameter."""
        collector = OpenFDACollector()

        with patch("requests.get") as mock_get:
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_response.json.return_value = {"results": []}
            mock_get.return_value = mock_response

            result = collector.search("aspirin", "pain")

            assert result.query["disease"] == "pain"

    def test_search_handles_404(self):
        """Search should handle 404 responses gracefully."""
        collector = OpenFDACollector()

        with patch("requests.get") as mock_get:
            mock_response = MagicMock()
            mock_response.status_code = 404
            mock_get.return_value = mock_response

            result = collector.search("nonexistent_drug_xyz")

            assert result.success is True
            assert result.data["labels"] == []

    def test_truncate_method(self):
        """Truncate method should limit text length."""
        short_text = "short"
        long_text = "a" * 100

        assert OpenFDACollector._truncate(short_text, 50) == short_text
        assert len(OpenFDACollector._truncate(long_text, 50)) == 53  # 50 + "..."

    def test_parse_labels_empty(self):
        """Should handle empty results."""
        collector = OpenFDACollector()
        result = collector._parse_labels([])
        assert result == []

    def test_parse_labels_with_data(self):
        """Should parse label data correctly."""
        collector = OpenFDACollector()
        sample_data = [
            {
                "openfda": {
                    "brand_name": ["Aspirin"],
                    "generic_name": ["aspirin"],
                    "manufacturer_name": ["Test Pharma"],
                },
                "indications_and_usage": ["For pain relief."],
            }
        ]

        result = collector._parse_labels(sample_data)

        assert len(result) == 1
        assert result[0]["brand_name"] == "Aspirin"
        assert result[0]["generic_name"] == "aspirin"


class TestOpenFDACollectorIntegration:
    """Integration tests for OpenFDA API (requires network)."""

    @pytest.mark.integration
    def test_real_search_aspirin(self):
        """Test real API call for aspirin (integration test)."""
        collector = OpenFDACollector(max_results=5)
        result = collector.search("aspirin")

        assert result.success is True
        assert "labels" in result.data
        # Aspirin should have results
        if result.data["labels"]:
            assert result.data["labels"][0]["generic_name"].lower() in ["aspirin", "n/a"]

    @pytest.mark.integration
    def test_real_adverse_events(self):
        """Test real adverse events search (integration test)."""
        collector = OpenFDACollector()
        result = collector._search_adverse_events("metformin")

        assert isinstance(result, dict)
        assert "total_reports" in result
        assert "top_reactions" in result
