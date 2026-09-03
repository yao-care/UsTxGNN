---
layout: default
title: Olopatadine
parent: 僅模型預測 (L5)
nav_order: 989
evidence_level: L5
indication_count: 1
---

# Olopatadine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Olopatadine: From Allergic Conjunctivitis to Rosacea Conjunctivitis

## One-Sentence Summary

> Olopatadine is an antihistamine/mast cell stabilizer with known clinical use in allergic conjunctivitis, though no formal indication record is available in this evidence pack.
> The TxGNN model predicts a possible association with **Rosacea Conjunctivitis**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded (drug not marketed in the US/Taiwan); known clinical use is allergic conjunctivitis per mechanistic rationale |
| Predicted New Indication | Rosacea Conjunctivitis |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L5 (model prediction only, no clinical trials or literature) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available for olopatadine. Based on known information, olopatadine is an antihistamine/mast cell stabilizer class drug, with established clinical use in allergic conjunctivitis. Its efficacy in that setting is well documented in general clinical practice, though no formal Taiwan/US indication record exists in this evidence pack.

"Rosacea conjunctivitis" is not a standard, single clinical entity — it appears to be a knowledge-graph label that may correspond to ocular manifestations of rosacea (ocular rosacea), a condition with overlapping features to allergic/inflammatory conjunctivitis. The mechanistic link here is based purely on drug-disease embedding similarity within the TxGNN model, without corroborating MOA data or original-indication confirmation. Given the absence of both original indication data and MOA detail, the biological rationale for this specific prediction cannot be independently verified at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is evidence level L5 — supported only by the TxGNN model score, with zero clinical trials or literature backing it, and a Blocking-severity data gap on TFDA safety labeling. There is insufficient basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA/FDA package insert data (warnings, contraindications) — currently a Blocking gap
- Confirmed original indication and MOA from DrugBank or regulatory source
- Clarification of "rosacea conjunctivitis" as a clinical entity (e.g., confirm whether it maps to ocular rosacea)
- Literature or preclinical evidence establishing a mechanistic link between olopatadine and rosacea-associated conjunctivitis
- At minimum, observational or case-level evidence before moving beyond S0/Hold
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

