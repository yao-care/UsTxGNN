"""OpenFDA collector - fetches US FDA drug data via openFDA API."""

import requests
from typing import Any

from .base import BaseCollector, CollectorResult


class OpenFDACollector(BaseCollector):
    """Collector for US FDA drug data via openFDA API.

    Uses the openFDA API to search for drug labels, adverse events, and approvals.
    API docs: https://open.fda.gov/apis/
    """

    source_name = "openfda"
    BASE_URL = "https://api.fda.gov"

    def __init__(self, api_key: str | None = None, max_results: int = 50):
        """Initialize the collector.

        Args:
            api_key: Optional openFDA API key (increases rate limits)
            max_results: Maximum number of results to return per query
        """
        self.api_key = api_key
        self.max_results = max_results

    def search(self, drug: str, disease: str | None = None) -> CollectorResult:
        """Search for FDA drug label data.

        Args:
            drug: Drug name (generic or brand)
            disease: Disease/indication name (optional, used to filter results)

        Returns:
            CollectorResult with drug label data
        """
        query = {"drug": drug, "disease": disease}

        # Search in drug labels
        labels = self._search_drug_labels(drug, disease)
        adverse_events = self._search_adverse_events(drug)

        data = {
            "labels": labels,
            "adverse_events_summary": adverse_events,
        }

        return self._make_result(
            query=query,
            data=data,
            success=True,
        )

    def _search_drug_labels(
        self, drug: str, disease: str | None = None
    ) -> list[dict]:
        """Search FDA drug labels (SPL data).

        Args:
            drug: Drug name
            disease: Optional disease filter

        Returns:
            List of matching drug labels
        """
        url = f"{self.BASE_URL}/drug/label.json"

        # Build search query
        search_parts = [f'(openfda.generic_name:"{drug}" OR openfda.brand_name:"{drug}")']
        if disease:
            search_parts.append(f'indications_and_usage:"{disease}"')

        params = {
            "search": " AND ".join(search_parts),
            "limit": self.max_results,
        }

        if self.api_key:
            params["api_key"] = self.api_key

        try:
            response = requests.get(url, params=params, timeout=30)
            if response.status_code == 404:
                return []
            response.raise_for_status()
            data = response.json()

            return self._parse_labels(data.get("results", []))

        except requests.RequestException:
            return []

    def _parse_labels(self, results: list[dict]) -> list[dict]:
        """Parse drug label results.

        Args:
            results: Raw API results

        Returns:
            List of parsed label dictionaries
        """
        labels = []

        for result in results:
            openfda = result.get("openfda", {})

            label = {
                "brand_name": openfda.get("brand_name", ["N/A"])[0] if openfda.get("brand_name") else "N/A",
                "generic_name": openfda.get("generic_name", ["N/A"])[0] if openfda.get("generic_name") else "N/A",
                "manufacturer": openfda.get("manufacturer_name", ["N/A"])[0] if openfda.get("manufacturer_name") else "N/A",
                "application_number": openfda.get("application_number", ["N/A"])[0] if openfda.get("application_number") else "N/A",
                "product_type": openfda.get("product_type", ["N/A"])[0] if openfda.get("product_type") else "N/A",
                "route": openfda.get("route", ["N/A"])[0] if openfda.get("route") else "N/A",
                "substance_name": openfda.get("substance_name", []) if openfda.get("substance_name") else [],
                "rxcui": openfda.get("rxcui", []) if openfda.get("rxcui") else [],
                "indications_and_usage": self._truncate(result.get("indications_and_usage", [""])[0] if result.get("indications_and_usage") else "", 500),
                "dosage_and_administration": self._truncate(result.get("dosage_and_administration", [""])[0] if result.get("dosage_and_administration") else "", 300),
                "warnings": self._truncate(result.get("warnings", [""])[0] if result.get("warnings") else "", 300),
                "contraindications": self._truncate(result.get("contraindications", [""])[0] if result.get("contraindications") else "", 300),
                "drug_interactions": self._truncate(result.get("drug_interactions", [""])[0] if result.get("drug_interactions") else "", 300),
            }
            labels.append(label)

        return labels

    def _search_adverse_events(self, drug: str) -> dict:
        """Search FDA adverse event reports (FAERS).

        Args:
            drug: Drug name

        Returns:
            Summary of adverse events
        """
        url = f"{self.BASE_URL}/drug/event.json"

        params = {
            "search": f'patient.drug.openfda.generic_name:"{drug}"',
            "count": "patient.reaction.reactionmeddrapt.exact",
            "limit": 10,
        }

        if self.api_key:
            params["api_key"] = self.api_key

        try:
            response = requests.get(url, params=params, timeout=30)
            if response.status_code == 404:
                return {"total_reports": 0, "top_reactions": []}
            response.raise_for_status()
            data = response.json()

            results = data.get("results", [])
            return {
                "total_reports": sum(r.get("count", 0) for r in results),
                "top_reactions": [
                    {"reaction": r.get("term", ""), "count": r.get("count", 0)}
                    for r in results[:10]
                ],
            }

        except requests.RequestException:
            return {"total_reports": 0, "top_reactions": []}

    def get_drug_approvals(self, drug: str) -> list[dict]:
        """Get FDA drug approval history.

        Args:
            drug: Drug name

        Returns:
            List of approval records
        """
        url = f"{self.BASE_URL}/drug/drugsfda.json"

        params = {
            "search": f'openfda.generic_name:"{drug}" OR openfda.brand_name:"{drug}"',
            "limit": self.max_results,
        }

        if self.api_key:
            params["api_key"] = self.api_key

        try:
            response = requests.get(url, params=params, timeout=30)
            if response.status_code == 404:
                return []
            response.raise_for_status()
            data = response.json()

            approvals = []
            for result in data.get("results", []):
                products = result.get("products", [])
                submissions = result.get("submissions", [])

                for product in products:
                    approval = {
                        "application_number": result.get("application_number", ""),
                        "sponsor_name": result.get("sponsor_name", ""),
                        "brand_name": product.get("brand_name", ""),
                        "active_ingredients": [
                            ai.get("name", "") for ai in product.get("active_ingredients", [])
                        ],
                        "dosage_form": product.get("dosage_form", ""),
                        "route": product.get("route", ""),
                        "marketing_status": product.get("marketing_status", ""),
                    }

                    # Get the most recent submission
                    if submissions:
                        latest = sorted(
                            submissions,
                            key=lambda x: x.get("submission_status_date", ""),
                            reverse=True,
                        )[0]
                        approval["submission_type"] = latest.get("submission_type", "")
                        approval["submission_status"] = latest.get("submission_status", "")
                        approval["submission_date"] = latest.get("submission_status_date", "")

                    approvals.append(approval)

            return approvals

        except requests.RequestException:
            return []

    def search_by_indication(self, indication: str) -> list[dict]:
        """Search for drugs by indication.

        Args:
            indication: Disease or condition name

        Returns:
            List of drugs with this indication
        """
        url = f"{self.BASE_URL}/drug/label.json"

        params = {
            "search": f'indications_and_usage:"{indication}"',
            "limit": self.max_results,
        }

        if self.api_key:
            params["api_key"] = self.api_key

        try:
            response = requests.get(url, params=params, timeout=30)
            if response.status_code == 404:
                return []
            response.raise_for_status()
            data = response.json()

            drugs = []
            seen = set()

            for result in data.get("results", []):
                openfda = result.get("openfda", {})
                generic_name = openfda.get("generic_name", [""])[0] if openfda.get("generic_name") else ""

                if generic_name and generic_name.lower() not in seen:
                    seen.add(generic_name.lower())
                    drugs.append({
                        "generic_name": generic_name,
                        "brand_name": openfda.get("brand_name", [""])[0] if openfda.get("brand_name") else "",
                        "manufacturer": openfda.get("manufacturer_name", [""])[0] if openfda.get("manufacturer_name") else "",
                        "indication_excerpt": self._truncate(
                            result.get("indications_and_usage", [""])[0] if result.get("indications_and_usage") else "",
                            300
                        ),
                    })

            return drugs

        except requests.RequestException:
            return []

    @staticmethod
    def _truncate(text: str, max_length: int) -> str:
        """Truncate text to max length."""
        if len(text) <= max_length:
            return text
        return text[:max_length] + "..."
