---
layout: default
title: Anakinra
parent: 僅模型預測 (L5)
nav_order: 337
evidence_level: L5
indication_count: 10
---

# Anakinra
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

# Anakinra: From Rheumatoid Arthritis to Extracutaneous Mastocytoma

## One-Sentence Summary

Anakinra is a recombinant human interleukin-1 receptor antagonist (IL-1Ra), used in major markets outside Taiwan for rheumatoid arthritis and several hereditary autoinflammatory diseases.
The TxGNN model assigns its highest score to **Extracutaneous Mastocytoma** (rank 1, score **99.93%**), yet **no clinical trials or publications** have been identified for this specific indication.
The evidence level is **L5** (model prediction only), and the recommended decision is **Hold**; notably, stronger mechanistic and clinical evidence exists for other top-10 predicted indications, particularly pyogenic autoinflammatory syndrome (rank 9, L3, Proceed with Guardrails).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Rheumatoid arthritis (not marketed per regulatory records in this evidence pack) |
| Predicted New Indication | Extracutaneous Mastocytoma |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Market Status | ✗ Not marketed (per regulatory records) |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on publicly known information, Anakinra competitively blocks both IL-1α and IL-1β from binding to the IL-1 type I receptor (IL-1RI), thereby suppressing downstream pro-inflammatory signaling — including NF-κB activation, prostaglandin synthesis, and cytokine cascades. This broad blockade of the IL-1 axis underpins its efficacy across a wide spectrum of inflammatory diseases.

Extracutaneous mastocytoma is an extremely rare, benign, localized mast cell tumor arising outside the skin. Mast cells are known secretors of IL-1β, and theoretically IL-1Ra could dampen mast cell–driven local inflammation. However, the dominant pathology of extracutaneous mastocytoma is clonal mast cell proliferation rather than a primary IL-1-mediated inflammatory cascade. The role of IL-1 as a disease driver in this entity has not been established, making the mechanistic connection indirect and speculative.

Context across the full top-10 prediction list is important: stronger mechanistic links and actual clinical evidence exist further down the ranked list. Pyogenic autoinflammatory syndrome (PAPA/PAPASH, rank 9) is directly driven by PSTPIP1 mutations that hyper-activate the IL-1β inflammasome — a textbook target for anakinra — and is supported by a systematic review plus multiple case series (L3 evidence, Proceed with Guardrails). Autosomal recessive familial Mediterranean fever (rank 3) is similarly an IL-1-pathway–driven monogenic disease with strong mechanistic rationale. The top-ranked prediction's high TxGNN score likely reflects graph-level topological proximity rather than established clinical relevance for extracutaneous mastocytoma specifically.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Anakinra in Extracutaneous Mastocytoma.

---

## Literature Evidence

Currently no related literature available for Anakinra in Extracutaneous Mastocytoma.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a near-perfect TxGNN prediction score (99.93%), extracutaneous mastocytoma is an extremely rare benign tumor with no clinical trials, no supporting publications, and no established IL-1 pathway involvement — making this a model-only prediction with insufficient biological or clinical grounding to advance.

**To proceed, the following is needed:**

- Preclinical data (in vitro or animal models) establishing IL-1β's causal role in extracutaneous mastocytoma
- Complete mechanism of action documentation retrieved from DrugBank API or official package insert
- Safety profile (key warnings, contraindications) extracted from the regulatory package insert to enable S1 safety screening
- Evaluation of whether repurposing resources would be better directed toward higher-evidence indications already in the top-10 list, specifically:
  - **Pyogenic autoinflammatory syndrome** (rank 9, L3, Systematic Review available — Proceed with Guardrails)
  - **Autosomal recessive familial Mediterranean fever** (rank 3, strong mechanistic link; likely a data collection gap rather than true absence of evidence)
  - **Aggressive systemic mastocytosis** (rank 4, L4, case-level literature on IL-1 inhibition in related mast cell–activation conditions)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

