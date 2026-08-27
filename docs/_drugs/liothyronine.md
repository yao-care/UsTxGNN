---
layout: default
title: Liothyronine
parent: 僅模型預測 (L5)
nav_order: 863
evidence_level: L5
indication_count: 10
---

# Liothyronine
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

# Liothyronine: From Hypothyroidism to Renal Hypodysplasia/Aplasia

## One-Sentence Summary

Liothyronine (T3, DB00279) is a synthetic thyroid hormone; the Evidence Pack does not record its original approved indication (data gap), but it is pharmacologically known as thyroid hormone replacement/suppressive therapy. The TxGNN model predicts it may be effective for **Renal Hypodysplasia/Aplasia**, but this is currently a **pure knowledge-graph prediction with zero supporting clinical trials or literature**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in Evidence Pack (no licenses on file; drug is a synthetic thyroid hormone, clinically known for thyroid hormone replacement) |
| Predicted New Indication | Renal Hypodysplasia/Aplasia |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, liothyronine is a synthetic form of triiodothyronine (T3) used in thyroid hormone replacement/suppressive therapy; its efficacy in thyroid hormone deficiency states has been established, but no formal original-indication record exists in this Evidence Pack (flagged as a High-severity data gap, DG002).

The repurposing rationale for this candidate notes that thyroid hormone receptors are expressed during renal development, and animal models show associations between thyroid dysfunction and renal developmental defects. This offers a plausible biological explanation for the high TxGNN score, but it remains a pure knowledge-graph co-occurrence inference — there is no clinical or case-level evidence that T3 supplementation can treat this congenital structural kidney disease.

Given renal hypodysplasia/aplasia is a structural/developmental malformation rather than a hormone-deficiency disorder, mechanistic plausibility alone does not establish therapeutic applicability, and no trial or observational data currently bridges this gap.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has evidence level L5 (model prediction only) — no clinical trials, no literature, and no case reports support liothyronine for renal hypodysplasia/aplasia. In addition, a Blocking-severity data gap (DG001: TFDA label warnings/contraindications) prevents even an initial safety screen (S1).

**To proceed, the following is needed:**
- TFDA label/package insert data (warnings, contraindications) — currently blocking (DG001)
- Confirmed mechanism of action and original indication documentation (DG002)
- Preclinical or clinical evidence specifically linking T3 therapy to renal hypodysplasia/aplasia outcomes
- Note: a separate candidate in this same Evidence Pack — **nodular goiter** (rank 3, evidence level L2, "Proceed with Guardrails") — is backed by 2 clinical trials and 20 literature records and reflects an already-established use of thyroid hormone suppressive therapy; it may warrant prioritization over this top-ranked but evidence-free candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

