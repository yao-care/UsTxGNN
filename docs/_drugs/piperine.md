---
layout: default
title: Piperine
parent: 僅模型預測 (L5)
nav_order: 1048
evidence_level: L5
indication_count: 2
---

# Piperine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Piperine: From No Approved Indication to Acne (Predicted)

## One-Sentence Summary

> Piperine (DrugBank DB12582) currently has no approved indication on record — it is not marketed and its original mechanism of action is undocumented in this dataset.
> The TxGNN model predicts it may be relevant to **Acne**, with a prediction score of **99.69%**,
> but this is currently supported by **0 clinical trials** and **0 publications** — a pure graph-embedding signal with no corroborating evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication recorded (compound not currently marketed) |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for piperine in this dataset. Based on general pharmacological knowledge, piperine is the primary bioactive alkaloid in black pepper (*Piper nigrum*), best characterized for its inhibition of CYP3A4 and P-glycoprotein, which increases the bioavailability of co-administered drugs. It has no established indication of its own in this evidence pack, and no clinical development pathway is documented.

The TxGNN score of 0.997 for acne reflects knowledge-graph embedding similarity, not a mechanism-driven signal — there is no supporting literature or trial evidence in this dataset to substantiate a causal link. Some external literature has explored piperine's anti-inflammatory and antimicrobial activity in vitro, which could theoretically intersect with acne pathophysiology (*P. acnes* colonization, follicular inflammation), but this connection is speculative and entirely unverified within the current evidence pack.

A second candidate, **amenorrhea**, was also predicted (score 99.39%, rank 13848) with the same lack of mechanistic or literature support. Neither prediction can currently be distinguished from graph-based noise without additional MOA and evidence data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## US Market Information

No marketing authorization found in the current dataset (0 licenses on record; product is not marketed).

---

## Safety Considerations

Please refer to the package insert for safety information. Note: safety review is currently **blocked** — TFDA label warnings/contraindications (DG001, Blocking severity) have not yet been retrieved, and no drug-drug interaction data is available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is based solely on TxGNN graph-embedding similarity (L5, decision stage S0), with no mechanism of action, no clinical trials, and no supporting literature. Safety review is also blocked pending TFDA label data, so this candidate cannot proceed to any clinical evaluation stage at this time.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain TFDA label warnings/contraindications to unblock S1 safety screening
- Resolve DG002 (High): retrieve piperine's mechanism of action via DrugBank API to assess mechanistic plausibility for acne
- Targeted literature search on piperine's activity in acne (anti-inflammatory/antimicrobial pathways) and amenorrhea (endocrine/steroidogenic pathways)
- Confirm whether piperine has any regulatory or marketed status in comparable jurisdictions, since it is currently unregistered in this dataset
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

