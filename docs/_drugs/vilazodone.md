---
layout: default
title: Vilazodone
parent: 僅模型預測 (L5)
nav_order: 1290
evidence_level: L5
indication_count: 10
---

# Vilazodone
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

# Vilazodone: From Major Depressive Disorder to Dysthymic Disorder

## One-Sentence Summary

> Vilazodone is a serotonergic antidepressant (SSRI + 5-HT1A partial agonist) — per literature within this evidence pack, it was approved by the US FDA in 2011 for Major Depressive Disorder (MDD) in adults; structured original-indication data is not recorded for this candidate.
> The TxGNN model's top-ranked prediction suggests possible efficacy for **Dysthymic Disorder** (persistent depressive disorder),
> but this specific candidate is currently supported by **mechanism reasoning only — no dedicated clinical trials or publications** are attached to it in this evidence pack.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in structured data (Data Gap); literature in this evidence pack indicates Major Depressive Disorder (MDD), US FDA approval 2011 |
| Predicted New Indication | Dysthymic Disorder |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L4 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Taiwan Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Structured mechanism-of-action data is marked as a Data Gap for this drug. However, several literature entries included elsewhere in this evidence pack (e.g. PMID [24195711](https://pubmed.ncbi.nlm.nih.gov/24195711/), [21951984](https://pubmed.ncbi.nlm.nih.gov/21951984/), [24940527](https://pubmed.ncbi.nlm.nih.gov/24940527/)) consistently describe vilazodone as a combined selective serotonin reuptake inhibitor (SSRI) and 5-HT1A receptor partial agonist, originally developed and FDA-approved for Major Depressive Disorder (MDD) in adults.

Dysthymic disorder (persistent depressive disorder) shares serotonergic pathophysiology with MDD, and SSRIs are commonly used across chronic depressive subtypes in clinical practice. Mechanistically, extending vilazodone's action to dysthymia is biologically plausible. That said, for this specific candidate the evidence pack records **no dedicated clinical trials and no literature** — the prediction is model-inferred only (evidence level L4, decision stage S1, recommendation "Research Question").

**Important caveat:** among the other candidates in this evidence pack, "neurotic depression" (rank 3) and "melancholia" (rank 4) score similarly high and are backed by substantial literature (up to 20 papers, including the pivotal FDA-approval review PMID 21951984) and, for melancholia, one completed Phase 4 trial. However, the evidence pack's own rationale flags these as likely **overlapping with vilazodone's already-approved MDD indication** — i.e., a duplicate-detection artifact caused by the missing `original_indications` field — rather than a genuinely novel repurposing signal. This distinction matters: the strongest evidence in this pack largely reflects vilazodone's known use, not a new therapeutic direction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Vilazodone currently has no approved license records in Taiwan (市場狀態：未上市 / Not Marketed; total licenses: 0). No NDA or product data is available for this candidate.

---

## Safety Considerations

Please refer to the package insert for safety information.

**Note:** TFDA label warnings and contraindications are currently missing and flagged as a **Blocking** data gap in this evidence pack — this must be resolved before the candidate can enter the S1 safety pre-assessment stage. No drug-drug interaction (DDI) records were found (query status: not found).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Dysthymic Disorder) is supported only by model inference (L4, TxGNN score 99.79%) with no dedicated trials or literature. Combined with a Blocking data gap in Taiwan label/safety information and the drug's current unmarketed status in Taiwan (0 licenses), there is insufficient evidence to advance this candidate at this time.

**To proceed, the following is needed:**
- TFDA label data (warnings, contraindications) — Blocking gap, required for S1 safety pre-assessment
- Structured mechanism-of-action and original-indication records at the drug level (currently Data Gaps)
- Dedicated clinical trials or literature evaluating vilazodone specifically in dysthymic disorder / persistent depressive disorder
- Clarification of Taiwan market/import pathway, given zero current licenses
- Reconciliation of whether "neurotic depression" / "melancholia" predictions represent a genuine repurposing signal or a duplicate-detection artifact from the missing original-indication field
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

