---
layout: default
title: Dulaglutide
parent: 僅模型預測 (L5)
nav_order: 632
evidence_level: L5
indication_count: 10
---

# Dulaglutide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Dulaglutide: From Type 2 Diabetes Mellitus to Opsismodysplasia

## One-Sentence Summary

Dulaglutide is a GLP-1 receptor agonist; its established therapeutic class and mechanism (referenced throughout this evidence pack's own rationale text) point to type 2 diabetes mellitus as the original indication, though Taiwan-specific approval data is unavailable since the product is **not currently marketed in Taiwan**. The TxGNN model's top-ranked new-indication prediction is **Opsismodysplasia**, a rare skeletal dysplasia, but this candidate has **0 clinical trials**, **0 publications**, and — critically — the evidence pack's own mechanistic analysis flags it as a likely false positive with no known biological connection to the GLP-1 pathway.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus (inferred from drug-class context in the evidence; not confirmed by Taiwan regulatory data — no TW license exists) |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 97.05% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Taiwan Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on general drug-class knowledge, Dulaglutide is a GLP-1 receptor agonist, and its efficacy in type 2 diabetes has been established through insulin secretion and metabolic regulation pathways.

However, for this specific top-ranked candidate, the evidence pack's own repurposing rationale explicitly **does not support** a plausible mechanistic link: Opsismodysplasia is a rare skeletal dysplasia caused by *RSPRY1* mutations, with no known relationship to GLP-1 receptor signaling. The rationale text itself attributes the high TxGNN score to a likely **knowledge-graph artifact** — a common false-positive pattern where sparsely-connected rare-disease nodes receive inflated similarity scores due to structural proximity rather than genuine biological signal.

This pattern is not isolated to rank 1: across all 10 predicted indications in this evidence pack (stiff person syndrome, pancreatic agenesis, several lipodystrophy subtypes, autoimmune oophoritis, etc.), the mechanistic rationale consistently notes weak-to-absent biological plausibility, and every candidate carries a Hold recommendation at evidence level L5. This candidate set should be read as a low-confidence output requiring substantial independent validation before any further action.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Dulaglutide has 0 registered licenses in Taiwan and is not currently marketed (`未上市`). No product/authorization records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA warning/contraindication data for this drug is currently a Blocking-severity data gap — see Conclusion.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate lacks any clinical trial or literature support (L5, model-prediction-only), and the evidence pack's own mechanistic analysis identifies the top prediction as a probable false positive with no plausible biological link to the drug's known pathway. Separately, a Blocking-severity data gap (missing TFDA label warnings/contraindications) prevents this candidate from entering the S1 safety evaluation stage regardless of efficacy signal.

**To proceed, the following is needed:**
- TFDA label data (warnings, contraindications) — Blocking gap, required before any S1 safety review
- Confirmed mechanism of action (MOA) data via DrugBank — High-severity gap
- Independent mechanistic/preclinical validation, since the model's own rationale disputes plausibility for this candidate
- Consideration of whether lower-ranked or differently-sourced candidates (e.g., those with a coherent metabolic/endocrine link, such as thiamine-responsive dysfunction syndrome, which at least shares a diabetes-adjacent phenotype) merit closer review instead of the top-scored but mechanistically unsupported candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

