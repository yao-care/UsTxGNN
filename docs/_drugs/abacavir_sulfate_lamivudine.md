---
layout: default
title: Abacavir Sulfate Lamivudine
parent: Model Prediction Only (L5)
nav_order: 38
evidence_level: L5
indication_count: 0
noindex: true
sitemap: false
last_modified_at: 2026-11-12
predicted_indications: []
---

# Abacavir Sulfate Lamivudine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **0** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Abacavir Sulfate + Lamivudine: Antiretroviral Combination — No Repurposing Predictions Available
{: .text-alpha }

---

## One-Sentence Summary

Abacavir Sulfate + Lamivudine is a well-established dual nucleoside reverse transcriptase inhibitor (NRTI) combination used globally for HIV-1 infection treatment (marketed as Epzicom/Kivexa in the US/EU).
However, the TxGNN pipeline returned **no predicted repurposing indications** for this candidate.
As a result, this report documents the data gaps and provides a decision recommendation based on available evidence.

<!-- review:begin us-lic-20261105-abacavir_sulfate_lamivudine-1 -->

> **Review correction (2026-11-05)**: Originally stated: "However, **this drug combination is not registered in the Taiwan TFDA database**, and the TxGNN pipeline returned **no predicted repurposing indications** for this candidate." Removed: leftover template text about Taiwan's TFDA, which does not apply to this US page. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261105-abacavir_sulfate_lamivudine-1 -->

---

## Quick Overview

| Item | Content |
|------|---------|
| Predicted New Indication | No prediction available |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (model prediction only — but no prediction generated) |
| Recommended Decision | **Hold** |

---

## Why No Prediction Was Generated

The TxGNN pipeline requires a valid DrugBank ID and a mapped drug node in the knowledge graph to generate repurposing predictions. For this candidate, the following issues were identified:

- **DrugBank ID is null**: The combination "ABACAVIR SULFATE; LAMIVUDINE" was not successfully mapped to a DrugBank entry, preventing knowledge graph traversal. Each component (Abacavir: DB01048; Lamivudine: DB00709) has individual DrugBank records, but the combination query failed.
- **DDI data not found**: No drug-drug interaction data was retrievable under this combined query string.

<!-- review:begin us-lic-20261105-abacavir_sulfate_lamivudine-2 -->

> **Review correction (2026-11-05)**: Originally stated: "Each component (Abacavir: DB01048; Lamivudine: DB00709) has individual DrugBank records, but the combination query failed. / **No Taiwan TFDA registration**: TFDA query returned 0 results (query ID 1), meaning this combination is not approved or registered in Taiwan's drug database." Removed: leftover template text about Taiwan's TFDA, which does not apply to this US page. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261105-abacavir_sulfate_lamivudine-2 -->

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on known pharmacological information, Abacavir + Lamivudine belongs to the NRTI class, inhibiting HIV reverse transcriptase to suppress viral replication. Its efficacy in HIV-1 infection is well-established globally, though mechanistic applicability to other conditions (e.g., hepatitis B, for Lamivudine alone) would require separate TxGNN evaluation per individual component.

---

## Clinical Trial Evidence

Currently no related clinical trials registered under this combined drug query via the TxGNN pipeline.

*Note: Extensive clinical trial data exists for the individual components (Abacavir, Lamivudine) and the combination in HIV treatment, but these are not surfaced here due to the absence of TxGNN predictions.*

---

## Literature Evidence

Currently no related literature available via the TxGNN pipeline for this candidate.

---

## Taiwan Market Information

No license records exist.

<!-- review:begin us-lic-20261105-abacavir_sulfate_lamivudine-3 -->

> **Review correction (2026-11-05)**: Originally stated: "This combination is **not registered** in the Taiwan TFDA database. No license records exist." Removed: leftover template text about Taiwan's TFDA, which does not apply to this US page. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261105-abacavir_sulfate_lamivudine-3 -->

| Item | Detail |
|------|--------|
| Query Result | 0 records found |
| US Market Status | Marketed (active FDA-approved applications: 5 of 11) |
| Number of FDA Applications | 11 (active: 5) |

*For reference: Abacavir + Lamivudine is marketed internationally as Epzicom (US, GlaxoSmithKline) and Kivexa (EU), approved for HIV-1 infection in adults and pediatric patients. These approvals are outside the scope of this Taiwan-focused Evidence Pack.*

---

## Safety Considerations

All safety data for this candidate returned as unavailable in the current Evidence Pack. Please refer to the package insert (Epzicom/Kivexa SmPC) for safety information.

Key known clinical warnings (from published prescribing information, not from this Evidence Pack):
- **Black Box Warning**: Hypersensitivity reactions to Abacavir (HLA-B\*5701 screening required before initiation); Lactic acidosis and severe hepatomegaly with steatosis.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline was unable to generate any repurposing predictions for this drug combination due to a failed DrugBank ID mapping. Without a valid prediction, there is no repurposing hypothesis to evaluate.

<!-- review:begin us-lic-20261105-abacavir_sulfate_lamivudine-4 -->

> **Review correction (2026-11-05)**: Originally stated: "The TxGNN pipeline was unable to generate any repurposing predictions for this drug combination due to a failed DrugBank ID mapping and the absence of Taiwan TFDA registration data." Removed: leftover template text about Taiwan's TFDA, which does not apply to this US page. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261105-abacavir_sulfate_lamivudine-4 -->

**To proceed, the following is needed:**

- **Re-query by individual component**: Run TxGNN separately for Abacavir (DB01048) and Lamivudine (DB00709) to retrieve individual repurposing predictions, then assess combination feasibility.
- **Resolve DrugBank mapping**: The combined query string "ABACAVIR SULFATE; LAMIVUDINE" failed mapping. Submit individual INN names to DrugBank API to retrieve DrugBank IDs.
- **Populate MOA data**: Query DrugBank API for mechanism of action entries for each component to enable mechanistic plausibility analysis.
- **Re-run TxGNN pipeline**: After resolving the above gaps, re-run the full prediction pipeline and generate a new Evidence Pack with valid `predicted_indications`.

<!-- review:begin us-lic-20261105-abacavir_sulfate_lamivudine-5 -->

> **Review correction (2026-11-05)**: Originally stated: "Submit individual INN names to DrugBank API to retrieve DrugBank IDs. / **Confirm Taiwan regulatory status**: Verify whether any generics or branded combinations are pending TFDA registration." Removed: leftover template text about Taiwan's TFDA, which does not apply to this US page. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261105-abacavir_sulfate_lamivudine-5 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "**this drug combination is not registered in the Taiwan TFDA database**, and" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-05 | Removed: "**No Taiwan TFDA registration**: TFDA query returned 0 results (query ID 1), meaning this combination is not approved or registered in Taiwa" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-05 | Removed: "This combination is **not registered** in the Taiwan TFDA database" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-05 | Removed: "and the absence of Taiwan TFDA registration data" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-05 | Removed: "**Confirm Taiwan regulatory status**: Verify whether any generics or branded combinations are pending TFDA registration" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

