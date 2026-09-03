---
layout: default
title: Spironolactone
parent: 僅模型預測 (L5)
nav_order: 1180
evidence_level: L5
indication_count: 2
---

# Spironolactone
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

# Spironolactone: From Established Uses to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

> Spironolactone is a well-established mineralocorticoid receptor antagonist; however, the evidence pack does not contain its approved indication text or mechanism-of-action data.
> The TxGNN model predicts potential efficacy for **Hypotrichosis Simplex of the Scalp**,
> but this prediction is supported by **no clinical trials** and **no published literature** — score alone drives the ranking.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (no approved indication text provided; drug is not currently marketed under any license in this dataset) |
| Predicted New Indication | Hypotrichosis Simplex of the Scalp |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L5 |
| US Market Status | Not Marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for spironolactone in this evidence pack. Based on the rationale accompanying the prediction, spironolactone is known to act as a mineralocorticoid receptor antagonist with weak antiandrogen activity, and is used clinically as an adjunct in androgenetic alopecia — a hormonally-driven, acquired form of hair loss.

Hypotrichosis simplex of the scalp, however, is a distinct, genetically inherited follicular developmental disorder (commonly associated with *APCDD1* or *CDH3* mutations) that is **not androgen-dependent**. There is no established mechanistic pathway connecting spironolactone's antimineralocorticoid/antiandrogen activity to this congenital condition. The high TxGNN score is most plausibly explained by lexical/semantic overlap between "hypotrichosis" and "alopecia" in the knowledge graph, rather than genuine biological plausibility.

The second-ranked prediction in this pack, *congenital hypotrichosis milia* (score 99.04%), shows the same pattern — a rare congenital syndrome with no known link to mineralocorticoid or androgen pathways, and likewise unsupported by any trial or literature evidence. This reinforces the interpretation that both predictions are likely artifacts of disease-name similarity rather than mechanistically grounded repurposing candidates.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

No marketing authorizations are recorded for this drug in the current dataset (0 licenses, market status: Not Marketed). Regulatory/label data would need to be sourced separately (see Data Gap DG001).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate rests entirely on an L5 model score with no clinical trial or literature corroboration, and the underlying mechanistic rationale argues *against* biological plausibility (an androgen/mineralocorticoid-pathway drug proposed for a non-hormonal, congenital follicular disorder). Combined with the absence of any Taiwan/US market authorization and missing safety label data (DG001, Blocking), this candidate does not meet the bar to advance past S0.

**To proceed, the following is needed:**
- TFDA/FDA package insert (warnings, contraindications) — required to clear the S1 safety gate (DG001)
- Confirmed mechanism-of-action documentation from DrugBank or primary literature (DG002)
- Independent literature or preclinical search specifically on spironolactone in hereditary hypotrichosis syndromes, to confirm or refute the suspected knowledge-graph name-similarity artifact
- If mechanistic plausibility cannot be established, recommend deprioritizing this candidate in favor of higher-ranked, mechanistically coherent TxGNN predictions for this drug
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

