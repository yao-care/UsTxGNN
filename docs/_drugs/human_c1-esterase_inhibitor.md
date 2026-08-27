---
layout: default
title: Human C1-Esterase Inhibitor
parent: 僅模型預測 (L5)
nav_order: 772
evidence_level: L5
indication_count: 4
---

# Human C1-Esterase Inhibitor
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

# Human C1-Esterase Inhibitor: From Hereditary Angioedema to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

> Human C1-esterase inhibitor (C1-INH, DrugBank DB06404) is a plasma-derived serine protease inhibitor clinically known for treating hereditary angioedema (HAE) by regulating the complement, contact-activation, and coagulation cascades — though this original-indication detail is not captured in the current evidence pack.
> The TxGNN model predicts it may be effective for **Severe Nonproliferative Diabetic Retinopathy**,
> but this specific prediction currently has **0 clinical trials** and **0 publications** supporting it — it is a pure knowledge-graph-embedding signal with no direct or indirect literature backing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in evidence pack (no Taiwan license/MOA data returned; C1-INH is clinically established for hereditary angioedema, per general pharmacological knowledge — not verified against this evidence pack) |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L5 |
| Market Status (Taiwan) | 未上市 (Not marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this drug in the evidence pack (Data Gap DG002, severity High). Based on what evidence *is* present in the accompanying repurposing rationale, human C1-esterase inhibitor (C1-INH/SERPING1) is a serine protease inhibitor that primarily suppresses the classical complement pathway (C1r, C1s) and the lectin pathway (MASP1/2), and also acts on the contact-activation system (kallikrein, activated Factor XII).

Severe nonproliferative diabetic retinopathy is a late-stage subtype of diabetic retinopathy (DR), a disease with documented complement-pathway involvement — C1q deposition, local inflammation, and microvascular thrombosis. Theoretically, C1-INH's inhibition of complement activation could plausibly attenuate this inflammatory and microvascular injury process. Notably, a related TxGNN prediction in the same evidence pack (rank 3, plain "diabetic retinopathy," score 99.25%) is supported by one genetic-association study linking complement pathway genes (SERPING1, C5) to DR susceptibility — this offers indirect mechanistic plausibility for the complement–DR link in general.

However, for the specific candidate evaluated here (severe nonproliferative DR), **no clinical trial or literature evidence exists at all**. The mechanistic link is explicitly flagged in the source data as theoretical only, and the high TxGNN score may reflect shared complement-related graph nodes rather than a validated pharmacological relationship. This prediction should be read as hypothesis-generating, not evidence-supported.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA warnings/contraindications are a Blocking data gap (DG001) — this must be resolved before any S1 safety review can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate sits at evidence level L5 (model prediction only) — there are zero clinical trials and zero publications directly supporting C1-INH use in severe nonproliferative diabetic retinopathy. The mechanistic rationale is inferred by analogy to a related, still weakly-supported prediction (plain diabetic retinopathy, backed only by a Tier 3 genetic-association study, not an interventional study of C1-INH itself). The drug is also not currently marketed in Taiwan (0 NDAs).

**To proceed, the following is needed:**
- Resolve Blocking data gap DG001: TFDA label warnings/contraindications (required before any safety review)
- Resolve High-priority data gap DG002: confirmed mechanism of action from DrugBank
- Original approved indication(s) for this drug, to properly assess similarity to the new indication
- At minimum, preclinical or mechanistic studies directly testing C1-INH in a diabetic retinopathy model, before this moves beyond a research question
- Continued monitoring of the related "diabetic retinopathy" (non-severe-specific) prediction, which has marginally stronger — though still indirect — literature support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

