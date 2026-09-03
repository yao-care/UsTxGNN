---
layout: default
title: Tildrakizumab
parent: 僅模型預測 (L5)
nav_order: 1228
evidence_level: L5
indication_count: 4
---

# Tildrakizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Tildrakizumab: From Plaque Psoriasis to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

> Tildrakizumab is an anti-IL-23p19 monoclonal antibody originally approved for plaque psoriasis.
> The TxGNN model predicts it may be effective for **Severe Nonproliferative Diabetic Retinopathy**,
> but currently **no clinical trials** and **no publications** support this direction — this is a model-only prediction (L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Plaque psoriasis (drawn from mechanism-of-action context; no formal license record on file) |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action data for Tildrakizumab is not available in the structured drug record. Based on the evidence gathered in this analysis, however, Tildrakizumab is known to be an anti-IL-23p19 monoclonal antibody that suppresses the Th17 inflammatory pathway, and it is approved for plaque psoriasis.

Because IL-23/Th17 signaling has a theoretical role in inflammatory microvascular pathology, TxGNN's knowledge graph links the drug to several diabetes-related complications — severe nonproliferative diabetic retinopathy, diabetic retinopathy, diabetic cataract, and drug-induced osteoporosis. Of these four, drug-induced osteoporosis has the most defensible biological rationale (Th17/IL-23 can drive RANKL-mediated osteoclast activation, an established osteoimmunology pathway), while the retinopathy and cataract predictions appear to rely on indirect "inflammation–vascular disease" node adjacency in the graph rather than drug-specific mechanistic evidence.

No pharmacokinetic data confirm whether a systemically administered monoclonal antibody achieves meaningful intraocular penetration, and no clinical trials or literature currently support any of these four indications. All four should be treated as hypothesis-generating signals only, not as evidence-backed repurposing candidates.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: internal data gap tracking flags TFDA label warnings/contraindications as a **Blocking** gap — this must be resolved before any safety review can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All four TxGNN-predicted indications (including the top-ranked severe nonproliferative diabetic retinopathy) are supported only by model score, with zero clinical trials or literature and no confirmed MOA/safety documentation. This does not meet the minimum evidence threshold to advance past S0.

**To proceed, the following is needed:**
- Formal TFDA/manufacturer label data — warnings, contraindications (Blocking gap, DG001)
- Confirmed mechanism-of-action documentation (DG002)
- Preclinical or mechanistic literature specifically linking IL-23 inhibition to diabetic retinopathy, diabetic cataract, and drug-induced osteoporosis
- Ocular pharmacokinetics/bioavailability assessment for systemic monoclonal antibody administration
- If evidence accrues, prioritize the drug-induced osteoporosis indication given its comparatively stronger osteoimmunology rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

