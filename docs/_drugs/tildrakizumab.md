---
layout: default
title: Tildrakizumab
parent: Model Prediction Only (L5)
nav_order: 1228
evidence_level: L5
indication_count: 4
monitor_inn: "TILDRAKIZUMAB"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "diabetic cataract", "drug-induced osteoporosis"]
last_modified_at: 2026-10-30
description: "Tildrakizumab: predicted new indication Severe nonproliferative diabetic retinopathy (evidence level L5). Approved use: Not listed in the compiled data (known clinical use: moderate-to-seve…"
---

# Tildrakizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Tildrakizumab: From Plaque Psoriasis to Severe Nonproliferative Diabetic Retinopathy
{: .text-alpha }

## One-Sentence Summary

Tildrakizumab is an anti-IL-23 p19 monoclonal antibody marketed in the US as ILUMYA. The indication text was not captured in the data compiled for this report, but the drug is known as a treatment for plaque psoriasis.
The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the compiled data (known clinical use: moderate-to-severe plaque psoriasis) |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 0.9963 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of FDA Applications | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on its drug class, tildrakizumab is an anti-IL-23 p19 monoclonal antibody, so it blocks the IL-23/IL-17 inflammatory axis, which is the basis of its use in psoriasis.

The proposed link is that chronic low-grade inflammation, including IL-23/IL-17 signaling, may contribute to retinal microvascular damage in diabetic retinopathy. This link is speculative. It rests only on the TxGNN score and has no supporting trial or publication, and it cannot be validated from the supplied data.

Other predicted indications show the same pattern of high scores without supporting evidence:

| Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|
| Diabetic retinopathy | 0.9953 | L5 | Same inflammatory rationale. Anti-VEGF, laser and corticosteroids set a high bar, and a systemic anti-IL-23 antibody would first need preclinical ocular evidence. |
| Diabetic cataract | 0.9921 | L5 | Driven mainly by hyperglycemia-related osmotic and oxidative lens stress. The link to IL-23 blockade is weak, and surgery is the definitive treatment. |
| Drug-induced osteoporosis | 0.9920 | L5 | IL-23/IL-17 is implicated in bone remodeling, but the direction of effect is unestablished. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761067 (cancelled) | ILUMYA (Sun Pharmaceutical Industries, Inc.) | Injection, solution | Not listed in the compiled data |

## Safety Considerations

- **Drug Interactions**: 78 interactions were identified. The most important ones from the compiled sample are:
  - **Major**: adalimumab, baricitinib, certolizumab pegol, cladribine. These mostly reflect additive immunosuppression.
  - **Moderate**: roflumilast, tacrolimus, azathioprine, cyclosporine, alefacept, alemtuzumab, anakinra, canakinumab, denosumab, and several vaccines (live cholera, anthrax, tetanus toxoid).
  - **Minor**: zinc salts (sulfate, acetate, gluconate, chloride).

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All four predictions are supported only by model scores (L5), with no registered trials or publications. The mechanistic link to diabetic retinopathy is speculative. In addition, the only US license is recorded as cancelled, and the package insert safety data has not been obtained.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications, which is a blocking gap for safety screening
- Mechanism of action data from DrugBank, to support mechanistic-link analysis
- Preclinical evidence of IL-23/IL-17 involvement in retinal disease (ocular models)
- A literature and trial search specific to diabetic retinopathy and IL-23 blockade
- Clarification of the route of administration, since a systemic antibody may not suit an ocular indication, and of the regulatory implications of the cancelled license status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

