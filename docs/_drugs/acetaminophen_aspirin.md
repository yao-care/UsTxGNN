---
layout: default
title: Acetaminophen Aspirin
parent: 僅模型預測 (L5)
nav_order: 93
evidence_level: L5
indication_count: 0
---

# Acetaminophen Aspirin
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

# Acetaminophen + Aspirin: Analgesic/Antipyretic Combination — Repurposing Evaluation Pending

## One-Sentence Summary

Acetaminophen and Aspirin is a well-established analgesic and antipyretic combination widely used for pain and fever management worldwide. However, the TxGNN model did not generate any new indication predictions for this combination drug entry, and the combination product has no registration records in the current regulatory database. This report documents the current data status and outlines the remediation steps required before a formal repurposing evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No regulatory registration found |
| Predicted New Indication | No TxGNN predictions generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — model prediction stage not reached; data gaps blocking evaluation |
| Market Status | Not marketed (0 licenses on record) |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Acetaminophen (paracetamol) is a centrally-acting analgesic and antipyretic agent, while Aspirin (acetylsalicylic acid) is a non-selective COX inhibitor with analgesic, anti-inflammatory, antipyretic, and antiplatelet properties. As individual drugs, both have decades of well-documented clinical use and are among the most widely marketed OTC analgesics globally.

The combination product returned zero results from the regulatory database query, suggesting it is not registered as a fixed-dose combination under this exact naming string in the current market. Notably, the DrugBank query returned 1 result, indicating that component-level data exists but was not successfully mapped into this Evidence Pack — likely because the combined string `"ACETAMINOPHEN; ASPIRIN"` did not match a single DrugBank entity.

Because no TxGNN repurposing predictions were generated for this entry, a formal comparison between original and predicted indications cannot be performed. The evaluation is blocked at the data preparation stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered in this Evidence Pack.

---

## Literature Evidence

Currently no related literature available in this Evidence Pack.

---

## Market Information

This combination product has no registration records in the current regulatory database query. Individual components (acetaminophen and aspirin) are widely available as separate products in most markets, but their status as a fixed-dose combination under this exact entry could not be confirmed.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: Safety data was not retrievable for this drug entry. Known class-level concerns for this combination include GI irritation (aspirin), hepatotoxicity risk at high acetaminophen doses, and potential interactions with anticoagulants. These should be formally sourced from the prescribing information before any clinical use assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This Evidence Pack contains multiple blocking data gaps — no TxGNN predictions were generated, no regulatory license records exist for the combination product, and both MOA and safety data are absent. A meaningful repurposing evaluation cannot proceed in its current state.

**To proceed, the following is needed:**

- **Resolve the TxGNN mapping failure**: Re-query using individual DrugBank IDs — Acetaminophen (DB00316) and Aspirin (DB00945) — separately, as the combined string likely caused the entity mapping to fail
- **Clarify the evaluation scope**: Determine whether the intended target is the fixed-dose combination or each component independently; separate reports may be more appropriate
- **Source safety data**: Obtain the package insert (仿單/prescribing information) for each component to populate warnings, contraindications, and drug interactions
- **Retrieve MOA from DrugBank**: The DrugBank query returned 1 result — extract MOA, drug categories, and toxicity data from that record
- **Verify regulatory status**: Confirm whether this combination product is marketed under a different brand name or trade name that may explain the zero-result regulatory query
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

