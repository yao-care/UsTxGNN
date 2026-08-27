---
layout: default
title: Halcinonide
parent: 僅模型預測 (L5)
nav_order: 766
evidence_level: L5
indication_count: 10
---

# Halcinonide
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

# Halcinonide: From Topical Corticosteroid Therapy to Annular Atrophic Lichen Planus

## One-Sentence Summary

Halcinonide is a high-potency synthetic glucocorticoid classified as a topical corticosteroid; a specific original indication is not recorded in this evidence pack. The TxGNN model predicts it may be effective for **Annular Atrophic Lichen Planus**, but currently **no clinical trials** and **no published literature** support this specific prediction — it rests on model score and mechanistic class reasoning alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (drug is classified as a high-potency topical corticosteroid based on repurposing rationale text) |
| Predicted New Indication | Annular Atrophic Lichen Planus |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Market Status (Taiwan) | 未上市 (Not marketed) |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap in this pack). Based on the information that is available, halcinonide is classified as a high-potency (class II–III) synthetic glucocorticoid — a topical corticosteroid. Topical corticosteroids are the established standard treatment class across the various subtypes of lichen planus, which gives this prediction a degree of mechanistic plausibility at the drug-class level.

However, for annular atrophic lichen planus specifically, there is no direct literature or trial evidence supporting halcinonide's use in this subtype. The rationale supplied with this prediction explicitly notes the link is a class-level (same-disease-family) inference rather than drug-specific evidence — the prediction should be read as hypothesis-generating, not as evidence of clinical efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Taiwan Market Information

Halcinonide has no marketing authorizations recorded in Taiwan (`market_status: 未上市`, 0 licenses on file). No product/dosage-form data is available to summarize.

## Safety Considerations

Please refer to the package insert for safety information.

*Note: TFDA label warnings/contraindications are flagged as a **Blocking** data gap in this pack (item DG001) — this must be resolved before any safety screening (S1) can proceed for this candidate.*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score (L5, decision stage S0) — there are zero clinical trials and zero published literature specific to halcinonide in annular atrophic lichen planus, and the drug is not currently marketed in Taiwan.

**To proceed, the following is needed:**
- TFDA package insert data (warnings/contraindications) — currently a Blocking gap (DG001)
- Mechanism of action (MOA) detail from DrugBank — currently a High-severity gap (DG002)
- Disease-specific preclinical or case-level evidence for annular atrophic lichen planus before advancing past S0
- Consider evaluating **alopecia areata** (rank 6 in this same prediction set) as an alternate candidate — it has 1 supporting literature citation (PMID 915049) and has already reached decision stage S1 ("Research Question"), a stronger evidence position than the top-ranked indication in this report
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

