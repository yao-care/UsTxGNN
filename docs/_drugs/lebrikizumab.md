---
layout: default
title: Lebrikizumab
parent: Model Prediction Only (L5)
nav_order: 841
evidence_level: L5
indication_count: 10
monitor_inn: "Lebrikizumab"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "drug-induced osteoporosis", "diabetic retinopathy", "primary release disorder of platelets", "dermatitis", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "neonatal dermatomyositis", "psoriasis", "HER2 positive breast carcinoma"]
---

# Lebrikizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Lebrikizumab: From Atopic Dermatitis to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Lebrikizumab is an injectable monoclonal antibody against interleukin-13 (IL-13). Published studies describe it as approved in the US for moderate-to-severe atopic dermatitis.
The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**.
This prediction currently has **0 clinical trials** and **0 publications** supporting it, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic dermatitis (taken from the published literature; the regulatory record compiled for this report has no indication text) |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 97.94% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | Cancelled only (see the caution in the market section) |
| Number of NDAs | 1 (BLA761306) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the regulatory data compiled for this report. The published literature describes lebrikizumab as a high-affinity IgG4 monoclonal antibody that binds IL-13. This prevents formation of the IL-4Rα/IL-13Rα1 receptor signaling complex, a central type 2 inflammatory pathway in atopic dermatitis.

The link to diabetic retinopathy is speculative. The only argument is that IL-13-related inflammation might contribute to retinal inflammation or vascular permeability. Atopic dermatitis is a skin disease driven by type 2 immunity, while diabetic retinopathy is mainly a microvascular complication of diabetes. No trial, publication, or mechanistic study in the compiled data connects the two. The high score should be read as a computational association, not as evidence of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761306 | EBGLYSS (Eli Lilly and Company) | Injection, solution | Not listed in the compiled data |

**Caution:** The compiled regulatory data shows this license as "cancelled" and lists no indication text. Recent publications and trial records describe lebrikizumab as FDA-approved for atopic dermatitis. This discrepancy is probably a data issue and should be checked against current FDA records before any decision relies on it.

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug interaction data were available in the compiled data. This gap is blocking for any further safety screening.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no clinical trials, no publications, and no plausible mechanistic support for retinal disease. Safety label data are also missing.

**To proceed, the following is needed:**
- A literature review of IL-13 biology in the retina and in diabetic retinopathy, followed by preclinical evidence if a rationale emerges
- Verification of the current FDA regulatory status and approved indication for EBGLYSS
- FDA package insert warnings and contraindications
- Mechanism of action data from DrugBank
- Assessment of route compatibility: an ophthalmic indication may need intravitreal delivery, but only a subcutaneous injectable is on record

**Note on other predictions:** Among the other top-10 predictions, "dermatitis" (rank 5) has substantial supporting evidence, including multiple completed Phase 3 trials. This is the drug's established atopic dermatitis indication, not a true repurposing opportunity. The remaining predictions have either no evidence or only indirect evidence, and none is recommended to proceed.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

