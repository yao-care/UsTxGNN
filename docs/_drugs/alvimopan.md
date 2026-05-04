---
layout: default
title: Alvimopan
parent: 僅模型預測 (L5)
nav_order: 300
evidence_level: L5
indication_count: 0
---

# Alvimopan
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

# Alvimopan: Evaluation Report — No TxGNN Predictions Available

## One-Sentence Summary

Alvimopan is a peripherally acting μ-opioid receptor antagonist, approved in the United States for accelerating gastrointestinal recovery following bowel resection surgery, but not currently marketed in Taiwan.
The current Evidence Pack contains **no TxGNN repurposing predictions** for this drug, and critical inputs — including mechanism of action and safety data — remain unpopulated.
A full repurposing assessment cannot be completed until these data gaps are resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | GI recovery post-bowel resection (US-approved; not marketed in Taiwan) |
| Predicted New Indication | Not available |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 — Pending: TxGNN pipeline has not yet been executed for this drug |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Taiwan Licenses | 0 |
| Recommended Decision | **Hold** |

---

## Why Assessment Cannot Proceed

The Evidence Pack for Alvimopan (DB06274) is currently in an early-collection state. Three critical data layers are absent:

**1. No repurposing predictions generated.** The `predicted_indications` array is empty, meaning the TxGNN pipeline (knowledge-graph and deep-learning prediction steps) has not yet been run for this drug. Without a ranked list of candidate indications, there is no target to evaluate.

**2. Mechanism of action unavailable.** The `original_moa` field is unpopulated. Alvimopan's known pharmacology — peripheral μ-opioid receptor antagonism — is directly relevant to any mechanistic plausibility analysis of new indications, particularly in GI motility disorders, opioid-induced constipation, or bowel recovery contexts. Retrieval from the DrugBank API is flagged as a high-severity remediation task (DG002).

**3. Safety data absent.** All warning and contraindication fields returned `[Data Gap]`, and the DDI query returned no results. This prevents the mandatory S1 safety screen from being completed (DG001, classified as Blocking severity).

---

## Taiwan Market Information

Alvimopan has no Taiwan FDA (TFDA) licenses on record. The drug is not marketed in Taiwan, and no dosage forms or approved indications exist in the local registry.

For reference, Alvimopan is marketed in the United States under the brand name **Entereg** (originally Adolor/GlaxoSmithKline, later acquired by Cubist/Merck), indicated for short-term in-hospital use to accelerate upper and lower GI recovery after partial large or small bowel resection with primary anastomosis.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: DG001 is classified as **Blocking** severity. The TFDA package insert PDF must be retrieved and parsed before any safety-related evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack lacks both repurposing prediction output and the safety data required for the S1 screen. Proceeding with evaluation in this state would produce an unreliable assessment with no factual basis for a Go or Proceed-with-Guardrails recommendation.

**To proceed, the following is needed:**

- **[Blocking]** Retrieve TFDA package insert PDF and extract key warnings and contraindications (DG001)
- **[High]** Query DrugBank API for Alvimopan mechanism of action, pharmacodynamics, and toxicity data (DG002)
- **[Required]** Execute the TxGNN knowledge-graph and deep-learning prediction pipeline for DB06274 to populate `predicted_indications`
- **[Optional]** Re-run the DDI query against an updated interaction database to confirm the zero-interaction result is genuine rather than a lookup failure
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

