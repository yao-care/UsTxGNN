---
layout: default
title: Abacavir Sulfate Lamivudine
parent: 僅模型預測 (L5)
nav_order: 38
evidence_level: L5
indication_count: 0
---

# Abacavir Sulfate Lamivudine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Abacavir Sulfate + Lamivudine: Antiretroviral Combination — No Repurposing Predictions Available

---

## One-Sentence Summary

Abacavir Sulfate + Lamivudine is a well-established dual nucleoside reverse transcriptase inhibitor (NRTI) combination used globally for HIV-1 infection treatment (marketed as Epzicom/Kivexa in the US/EU).
However, **this drug combination is not registered in the Taiwan TFDA database**, and the TxGNN pipeline returned **no predicted repurposing indications** for this candidate.
As a result, this report documents the data gaps and provides a decision recommendation based on available evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (antiretroviral treatment) — *sourced from general medical knowledge; not in Taiwan TFDA* |
| Predicted New Indication | No prediction available |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (model prediction only — but no prediction generated) |
| Taiwan Market Status | ✗ Not marketed |
| Number of Approved Licenses (Taiwan) | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Was Generated

The TxGNN pipeline requires a valid DrugBank ID and a mapped drug node in the knowledge graph to generate repurposing predictions. For this candidate, the following issues were identified:

- **DrugBank ID is null**: The combination "ABACAVIR SULFATE; LAMIVUDINE" was not successfully mapped to a DrugBank entry, preventing knowledge graph traversal. Each component (Abacavir: DB01048; Lamivudine: DB00709) has individual DrugBank records, but the combination query failed.
- **No Taiwan TFDA registration**: TFDA query returned 0 results (query ID 1), meaning this combination is not approved or registered in Taiwan's drug database.
- **DDI data not found**: No drug-drug interaction data was retrievable under this combined query string.

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

This combination is **not registered** in the Taiwan TFDA database. No license records exist.

| Item | Detail |
|------|--------|
| TFDA Query Date | 2026-03-24 |
| Query Result | 0 records found |
| Market Status | Not marketed in Taiwan |

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
The TxGNN pipeline was unable to generate any repurposing predictions for this drug combination due to a failed DrugBank ID mapping and the absence of Taiwan TFDA registration data. Without a valid prediction, there is no repurposing hypothesis to evaluate.

**To proceed, the following is needed:**

- **Re-query by individual component**: Run TxGNN separately for Abacavir (DB01048) and Lamivudine (DB00709) to retrieve individual repurposing predictions, then assess combination feasibility.
- **Resolve DrugBank mapping**: The combined query string "ABACAVIR SULFATE; LAMIVUDINE" failed mapping. Submit individual INN names to DrugBank API to retrieve DrugBank IDs.
- **Confirm Taiwan regulatory status**: Verify whether any generics or branded combinations are pending TFDA registration.
- **Populate MOA data**: Query DrugBank API for mechanism of action entries for each component to enable mechanistic plausibility analysis.
- **Re-run TxGNN pipeline**: After resolving the above gaps, re-run the full prediction pipeline and generate a new Evidence Pack with valid `predicted_indications`.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

