---
layout: default
title: Metyrapone
parent: 僅模型預測 (L5)
nav_order: 922
evidence_level: L5
indication_count: 10
---

# Metyrapone
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

# Metyrapone: From an Undocumented Original Indication to Exercise-Induced Malignant Hyperthermia

## One-Sentence Summary

Metyrapone (DrugBank DB01011) is not currently marketed in the covered jurisdiction, and its original approved indication and mechanism of action are not yet documented in this evidence pack.
The TxGNN model's top-ranked prediction is **Exercise-Induced Malignant Hyperthermia** (score 99.95%), but this specific prediction is supported by **0 clinical trials** and **0 publications** — the evidence pack's own rationale explicitly notes no mechanistic link to the drug's known pharmacology.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (no license/indication records; MOA also flagged as a data gap pending DrugBank lookup) |
| Predicted New Indication | Exercise-Induced Malignant Hyperthermia |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for metyrapone is currently a flagged data gap in this evidence pack (severity: High). However, the rationale text attached to a lower-ranked candidate in this same pack (familial periodic paralysis, rank 8) indicates metyrapone acts by inhibiting 11β-hydroxylase, blocking ACTH-stimulated glucocorticoid (not mineralocorticoid) synthesis.

For the top-ranked prediction — Exercise-Induced Malignant Hyperthermia — the evidence pack's own mechanistic assessment is explicit and cautionary: this condition is driven by RYR1 channelopathy, and the rationale states there is **no direct connection** between RYR1-mediated calcium channel dysfunction and 11β-hydroxylase inhibition, with **zero supporting trials and zero literature**. The same caveat applies to ranks 2–7 and 10, which form a cluster of RYR1/CACNA1S-related myopathies likely grouped together by TxGNN's embedding space rather than by a shared, verified biological pathway with metyrapone.

In short, the highest TxGNN score in this pack does not correspond to the strongest biological plausibility — the pack itself flags this as a likely graph-similarity artifact rather than a mechanistically grounded hit.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## US Market Information

Metyrapone currently has no marketing authorization on file (0 licenses; market status: Not Marketed). No NDA or product records are available in the evidence pack.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Exercise-Induced Malignant Hyperthermia) has no clinical trial or literature support, and the evidence pack's own rationale finds no plausible mechanistic overlap between metyrapone's known pharmacology and RYR1-driven channelopathies — the high TxGNN score likely reflects knowledge-graph embedding similarity rather than real biological signal.

**To proceed, the following is needed:**
- TFDA/FDA package insert (warnings, contraindications) — currently a Blocking data gap preventing any S1 safety review
- Confirmed mechanism of action via DrugBank API — currently a High-severity data gap
- Original approved indication and licensing history
- Separately worth noting: within this same evidence pack, a lower-ranked candidate — **familial periodic paralysis** (rank 8, score 99.40%, L3/S1, "Research Question") — has actual literature support (2 PMIDs, including a tier-2 prospective case series showing glucocorticoid-induced paralysis is blocked by ACTH + metyrapone) and a coherent mechanistic rationale. This candidate is currently better supported than the top TxGNN hit and may warrant its own evaluation track.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

