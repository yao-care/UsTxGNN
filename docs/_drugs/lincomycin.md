---
layout: default
title: Lincomycin
parent: 僅模型預測 (L5)
nav_order: 862
evidence_level: L5
indication_count: 3
---

# Lincomycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Lincomycin: From Bacterial Infections (indication undocumented) to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Lincomycin is a lincosamide-class antibacterial agent; its original approved indication is not documented in this evidence pack, and the drug currently has no market authorization on record (0 licenses).
The TxGNN model predicts it may be effective for **Polyclonal Hyperviscosity Syndrome**,
but this direction is currently supported by **0 clinical trials** and **0 publications** — the score reflects knowledge-graph embedding similarity only, not clinical or mechanistic evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (no license records; MOA data unavailable) |
| Predicted New Indication | Polyclonal Hyperviscosity Syndrome |
| TxGNN Prediction Score | 99.14% |
| Evidence Level | L5 |
| Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Lincomycin. Based on known pharmacological classification, Lincomycin belongs to the lincosamide class of antibacterial agents; however, its original approved indication is not captured in this evidence pack (no license records exist — the drug is not currently marketed), which limits any structured comparison between an original and a new indication.

Polyclonal hyperviscosity syndrome is typically associated with plasma cell dyscrasias and immunoglobulin abnormalities — a disease mechanism unrelated to known antibacterial pharmacology. No mechanistic pathway linking Lincomycin to this condition can be established from the data available.

As the evidence pack itself notes: the TxGNN score (0.9914) is high, but this reflects knowledge-graph embedding similarity, not mechanistic, clinical, or literature evidence. With zero supporting clinical trials or publications, this prediction should be treated as an unvalidated computational hypothesis only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Market Information

Lincomycin is not currently marketed in the reference jurisdiction — no license/authorization records exist (0 NDAs on file), so no product/dosage-form details are available.

---

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA label warnings/contraindications data is currently a blocking data gap (DG001) — this must be resolved before any safety pre-assessment (S1) can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a TxGNN embedding score (L5, decision stage S0) with zero clinical trials, zero literature, no established mechanism of action, and no market presence for the drug itself. There is no basis to advance beyond model prediction at this time.

**To proceed, the following is needed:**
- TFDA (or equivalent) package insert — warnings, contraindications (DG001, blocking)
- Verified mechanism of action data via DrugBank API (DG002)
- Documentation of Lincomycin's original approved indication(s)
- Any preclinical or mechanistic literature connecting lincosamide antibiotics to plasma-cell/immunoglobulin-related pathology, if it exists

**Note:** Two additional TxGNN-predicted indications for this drug (hyperamylasemia, congenital analbuminemia) were evaluated in the same evidence pack and show the same profile — L5 evidence, zero supporting trials/literature, Hold recommendation. Congenital analbuminemia in particular is a genetic disorder not amenable to pharmacological correction, which further weakens confidence in the underlying prediction set for this drug.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

