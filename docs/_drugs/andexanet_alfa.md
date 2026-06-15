---
layout: default
title: Andexanet Alfa
parent: 僅模型預測 (L5)
nav_order: 349
evidence_level: L5
indication_count: 4
---

# Andexanet Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Andexanet Alfa: Evaluation Pending — Insufficient Evidence Pack Data

## One-Sentence Summary

Andexanet alfa (DB14562) is a biological reversal agent for Factor Xa inhibitors currently **not marketed in Taiwan**.
The TxGNN model returned **no predicted new indications** for this drug in the current evidence pack, and critical data items — including mechanism of action, safety warnings, and contraindications — are missing.
Without TxGNN predictions or supporting evidence, a standard repurposing evaluation **cannot be completed at this time**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No TFDA authorization records found |
| Predicted New Indication | None — TxGNN returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (model prediction only; currently no predictions available) |
| US Market Status | Not marketed in Taiwan (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN prediction is available for andexanet alfa in this evidence pack, so a mechanistic rationale for a new indication cannot be constructed.

Currently, detailed mechanism of action data is not available in the supplied evidence pack. Based on publicly known information, andexanet alfa is a recombinant modified human Factor Xa decoy protein designed to reverse anticoagulation caused by direct Factor Xa inhibitors (e.g., apixaban, rivaroxaban). Its original approved use in the United States (Andexxa®, approved 2018) is for life-threatening or uncontrolled bleeding in patients receiving Factor Xa inhibitor therapy — a highly specific, acute-care indication with no obvious mechanistic extension to other disease categories without further analysis.

Until TxGNN predictions are generated and MOA data is retrieved from DrugBank, the repurposing rationale for this candidate remains undetermined.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for predicted new indications (no TxGNN predictions available).

---

## Literature Evidence

Currently no related literature available for predicted new indications (no TxGNN predictions available).

---

## US Market Information

No TFDA authorization records found for andexanet alfa. The drug is not marketed in Taiwan.

---

## Safety Considerations

Please refer to the package insert for safety information.

> All safety fields — key warnings, contraindications, and drug-drug interactions — returned no data in this evidence pack. The TFDA package insert (仿單) has not yet been retrieved; this is classified as a **Blocking** data gap (DG001) that must be resolved before any safety evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence pack is structurally incomplete — andexanet alfa has zero TxGNN predicted indications, zero TFDA regulatory records, and all safety fields are empty. There is no evaluable repurposing signal at this stage.

**To proceed, the following is needed:**

- **[Blocking — DG001]** Retrieve the TFDA package insert PDF and extract warnings and contraindications before any safety evaluation
- **[High — DG002]** Query the DrugBank API for mechanism of action (MOA) data to enable mechanistic plausibility analysis
- **Confirm TxGNN pipeline execution**: Verify whether andexanet alfa is present in the knowledge graph node list (`data/external/drugbank_vocab.csv`) — its status as a large recombinant protein may cause it to be excluded from the standard small-molecule prediction pipeline
- **Check US/EU regulatory data**: Andexxa® (FDA-approved) and Ondexxya® (EMA-approved) package inserts are publicly available and should be used to populate original indication, warnings, and contraindication fields if TFDA data remains unavailable
- **Re-run evidence collection**: Once TxGNN predictions are obtained, trigger ClinicalTrials.gov and PubMed collectors for the predicted indication(s) to populate the evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

