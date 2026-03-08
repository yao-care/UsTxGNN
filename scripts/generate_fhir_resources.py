#!/usr/bin/env python3
"""生成 FHIR R4 資源

從預測結果生成 FHIR 格式的資源檔案。

使用方法:
    uv run python scripts/generate_fhir_resources.py

前置條件:
    已執行 run_kg_prediction.py

產生檔案:
    docs/fhir/metadata
    docs/fhir/MedicationKnowledge/*.json
    docs/fhir/ClinicalUseDefinition/*.json
"""

import json
import re
from datetime import datetime
from pathlib import Path

import pandas as pd


# US FDA configuration
BASE_URL = "https://ustxgnn.yao.care"

JURISDICTION = {
    "coding": [{
        "system": "urn:iso:std:iso:3166",
        "code": "US",
        "display": "United States of America"
    }]
}


def slugify(text: str) -> str:
    """Convert text to URL-safe slug"""
    if not text:
        return ""
    text = str(text).lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text[:100].strip("-")


def generate_capability_statement() -> dict:
    """Generate CapabilityStatement (metadata)"""
    return {
        "resourceType": "CapabilityStatement",
        "id": "ustxgnn-fhir-server",
        "url": f"{BASE_URL}/fhir/metadata",
        "version": "1.0.0",
        "name": "UsTxGNNFHIRServer",
        "status": "active",
        "date": datetime.now().strftime("%Y-%m-%d"),
        "publisher": "UsTxGNN Project",
        "description": "US FDA Drug Repurposing Predictions - FHIR R4 API",
        "kind": "instance",
        "fhirVersion": "4.0.1",
        "format": ["json"],
        "rest": [{
            "mode": "server",
            "resource": [
                {
                    "type": "MedicationKnowledge",
                    "interaction": [{"code": "read"}, {"code": "search-type"}]
                },
                {
                    "type": "ClinicalUseDefinition",
                    "interaction": [{"code": "read"}, {"code": "search-type"}]
                }
            ]
        }]
    }


def generate_medication_knowledge(
    drug_name: str,
    drugbank_id: str,
    evidence_level: str = "L5"
) -> dict:
    """Generate MedicationKnowledge resource"""
    slug = slugify(drug_name)
    return {
        "resourceType": "MedicationKnowledge",
        "id": slug,
        "status": "active",
        "code": {
            "coding": [
                {
                    "system": "https://www.drugbank.ca",
                    "code": drugbank_id,
                    "display": drug_name
                }
            ],
            "text": drug_name
        },
        "intendedJurisdiction": [JURISDICTION],
        "extension": [{
            "url": f"{BASE_URL}/fhir/StructureDefinition/evidence-level",
            "valueCode": evidence_level
        }]
    }


def generate_clinical_use_definition(
    drug_name: str,
    drugbank_id: str,
    indication: str,
    evidence_level: str = "L5"
) -> dict:
    """Generate ClinicalUseDefinition resource"""
    drug_slug = slugify(drug_name)
    indication_slug = slugify(indication)
    resource_id = f"{drug_slug}-{indication_slug}"[:100]

    return {
        "resourceType": "ClinicalUseDefinition",
        "id": resource_id,
        "type": "indication",
        "status": "active",
        "subject": [{"reference": f"MedicationKnowledge/{drug_slug}"}],
        "indication": {
            "diseaseSymptomProcedure": {
                "concept": {"text": indication}
            }
        },
        "extension": [
            {
                "url": f"{BASE_URL}/fhir/StructureDefinition/evidence-level",
                "valueCode": evidence_level
            },
            {
                "url": f"{BASE_URL}/fhir/StructureDefinition/source",
                "valueString": "TxGNN Knowledge Graph"
            }
        ]
    }


def main():
    print("=" * 60)
    print("Generate FHIR R4 Resources - US FDA")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent
    fhir_dir = base_dir / "docs" / "fhir"

    # Create directories
    (fhir_dir / "MedicationKnowledge").mkdir(parents=True, exist_ok=True)
    (fhir_dir / "ClinicalUseDefinition").mkdir(parents=True, exist_ok=True)

    # 1. Generate CapabilityStatement
    print("1. Generating CapabilityStatement...")
    metadata = generate_capability_statement()
    with open(fhir_dir / "metadata", "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    print(f"   Saved: {fhir_dir / 'metadata'}")

    # 2. Load prediction results
    print()
    print("2. Loading prediction results...")
    candidates_path = base_dir / "data" / "processed" / "repurposing_candidates.csv"

    if not candidates_path.exists():
        print(f"   Error: {candidates_path} not found")
        print("   Please run run_kg_prediction.py first")
        return

    candidates = pd.read_csv(candidates_path)
    print(f"   Loaded {len(candidates)} predictions")

    # 3. Generate MedicationKnowledge resources
    print()
    print("3. Generating MedicationKnowledge resources...")

    # Get unique drugs
    drugs = candidates[["NormalizedIngredient", "drugbank_id"]].drop_duplicates()
    drugs = drugs[drugs["drugbank_id"].notna()]

    med_count = 0
    for _, row in drugs.iterrows():
        drug_name = row["NormalizedIngredient"]
        drugbank_id = row["drugbank_id"]

        if not drug_name:
            continue

        resource = generate_medication_knowledge(drug_name, drugbank_id)
        slug = slugify(drug_name)
        filepath = fhir_dir / "MedicationKnowledge" / f"{slug}.json"

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(resource, f, indent=2, ensure_ascii=False)
        med_count += 1

    print(f"   Generated {med_count} MedicationKnowledge resources")

    # 4. Generate ClinicalUseDefinition resources
    print()
    print("4. Generating ClinicalUseDefinition resources...")

    cud_count = 0
    seen = set()

    for _, row in candidates.iterrows():
        drug_name = row.get("NormalizedIngredient", "")
        drugbank_id = row.get("drugbank_id", "")
        indication = row.get("PotentialIndication", "")

        if not drug_name or not indication:
            continue

        # Avoid duplicates
        key = (drug_name, indication)
        if key in seen:
            continue
        seen.add(key)

        resource = generate_clinical_use_definition(drug_name, drugbank_id, indication)
        drug_slug = slugify(drug_name)
        indication_slug = slugify(indication)
        filename = f"{drug_slug}-{indication_slug}.json"[:150]

        filepath = fhir_dir / "ClinicalUseDefinition" / filename

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(resource, f, indent=2, ensure_ascii=False)
        cud_count += 1

    print(f"   Generated {cud_count} ClinicalUseDefinition resources")

    # Summary
    print()
    print("=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"  CapabilityStatement: 1")
    print(f"  MedicationKnowledge: {med_count}")
    print(f"  ClinicalUseDefinition: {cud_count}")
    print(f"  Total FHIR resources: {1 + med_count + cud_count}")
    print()
    print(f"FHIR resources saved to: {fhir_dir}")
    print()
    print("Done!")


if __name__ == "__main__":
    main()
