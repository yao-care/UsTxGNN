---
layout: default
title: Allantoin
parent: 僅模型預測 (L5)
nav_order: 224
evidence_level: L5
indication_count: 8
---

# Allantoin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Allantoin: From Topical Wound Care to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Allantoin is a well-established OTC active ingredient widely used in topical wound-healing and skin barrier repair formulations, known for its keratolytic, cell-proliferating, and mild anti-inflammatory properties.
The TxGNN model predicts it may be effective for **Severe Nonproliferative Diabetic Retinopathy** as its top-ranked new indication,
with **0 clinical trials** and **0 publications** currently supporting this specific direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Topical wound healing and skin barrier repair (OTC) |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.56% |
| Evidence Level | L5 |
| US Market Status | Not approved (no NDA on file) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from the DrugBank query at this time. Based on published pharmaceutical literature, allantoin (5-ureidohydantoin, DB11100) is a naturally occurring purine metabolism byproduct also produced synthetically. Its documented pharmacological properties include promotion of fibroblast proliferation, keratolytic activity enabling skin desquamation and renewal, stimulation of granulation tissue formation, and non-specific anti-inflammatory effects. These properties have underpinned its longstanding use in OTC wound-healing creams, post-procedure skincare, mucous membrane products, and scar management formulations.

Severe nonproliferative diabetic retinopathy (SNPDR) is driven by oxidative stress, microvascular inflammation, pericyte loss, and progressive retinal ischemia. Allantoin's anti-inflammatory and antioxidant properties are theoretically relevant insofar as inflammatory pathways are shared between skin and retinal tissue. However, allantoin has no documented systemic administration history, no established ocular pharmacokinetics, and no published data on blood-retinal barrier penetration. Its entire evidence base is confined to topical/dermatological use.

The KG prediction signal most likely originates from shared "inflammation" and "oxidative stress" network nodes — a topology-based association rather than a direct mechanistic link. Extrapolating from peripheral anti-inflammatory activity to intraocular efficacy requires, at minimum, pharmacokinetic proof-of-concept that does not currently exist. This prediction is best interpreted as a hypothesis-generating signal rather than actionable evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Allantoin in severe nonproliferative diabetic retinopathy.

---

## Literature Evidence

Currently no related literature available for Allantoin in severe nonproliferative diabetic retinopathy.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** TFDA label (warnings, contraindications) and DDI data are currently unavailable (data gap). Safety screening (S1 stage) cannot be completed until the prescribing information is obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN prediction (severe nonproliferative diabetic retinopathy) is supported exclusively by knowledge graph topology with no clinical or preclinical corroboration (L5), and allantoin lacks any systemic or ocular pharmacology data necessary to evaluate feasibility.

**To proceed, the following is needed:**
- Retrieve MOA data from DrugBank API (DG002) to enable mechanistic analysis
- Obtain TFDA/FDA prescribing information to complete S1 safety screening (DG001 — Blocking)
- Commission ocular pharmacokinetic studies: blood-retinal barrier penetration, aqueous humor distribution, and systemic bioavailability after any proposed systemic route
- Consider pivoting analytical priority to higher-plausibility indications: **Acne Keloid** (Rank 4, Research Question) which has the strongest mechanistic alignment with allantoin's known fibroblast-modulating and keratolytic profile, and **Exanthem** (Rank 8, L4) which has 3 supporting trials using allantoin-containing formulations and warrants a component-isolation study design
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

