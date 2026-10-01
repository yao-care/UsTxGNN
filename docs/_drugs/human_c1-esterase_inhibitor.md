---
layout: default
title: Human C1-Esterase Inhibitor
parent: Model Prediction Only (L5)
nav_order: 772
evidence_level: L5
indication_count: 4
---

# Human C1-Esterase Inhibitor
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# HUMAN C1-ESTERASE INHIBITOR: From a Marketed C1-INH Product to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Human C1-esterase inhibitor (C1-INH) is a plasma-derived protein marketed in the US as the injectable product Cinryze.
The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**, but **no clinical trials and no publications** currently support this specific prediction.
This is a model-only prediction (L5).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied record |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (BLA125267) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. C1-INH is a regulator of the complement system and the plasma kallikrein-kinin contact system. On that basis, a plausible but unverified link is that it could dampen complement activation and contact-system signalling. Both pathways are implicated in retinal vascular permeability and inflammation in diabetic retinopathy.

This link is inferred and is not supported by the supplied data. The record lists no original indication and no MOA, so the relationship between the original and predicted indications cannot be assessed. The high TxGNN score reflects knowledge-graph patterns, not tested biology.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for severe nonproliferative diabetic retinopathy.

Note: one indirect item exists for the broader indication *diabetic retinopathy* (rank 3 prediction): [26989329](https://pubmed.ncbi.nlm.nih.gov/26989329/) (2016, *Mediators of Inflammation*), a genetic association study of complement pathway genes (SERPING1 and C5) in 570 patients with type 2 diabetes. It supports complement-mediated inflammation as a disease mechanism, but it did not test C1-INH and is indirect evidence only.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125267 | Cinryze (Takeda Pharmaceuticals America, Inc.) | Injection, powder, lyophilized, for solution | Not listed in the supplied record |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no trials or publications for this indication, and the mechanism, original indication and safety data are all missing from the record.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank, to test the complement and kallikrein-kinin hypothesis
- Preclinical or biomarker work, such as complement activation in vitreous or serum of diabetic retinopathy patients, before any clinical consideration
- Assessment of route compatibility: Cinryze is an intravenous injectable, and the route required for retinal disease is not yet defined

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

