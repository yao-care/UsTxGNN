---
layout: default
title: Phenol
parent: Model Prediction Only (L5)
nav_order: 1038
evidence_level: L5
indication_count: 8
---

# Phenol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Phenol: From Sore Throat Relief to Acrodermatitis Chronica Atrophicans

## One-Sentence Summary

Phenol is an old antiseptic and topical agent. Its US products include sore throat sprays and homeopathic pellets, and no approved indication text is on file.
The TxGNN model predicts it may be effective for **acrodermatitis chronica atrophicans**, but **0 clinical trials** and **0 publications** support this prediction.
It is a model-only prediction with no mechanistic link identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the regulatory data (product names such as "Sore Throat" spray suggest oral/throat use) |
| Predicted New Indication | Acrodermatitis chronica atrophicans |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for phenol. Its known general actions are protein denaturation, keratolysis, antisepsis and neurolysis. These support local antiseptic, analgesic and chemical-peel uses.

Acrodermatitis chronica atrophicans is a late, chronic atrophic skin condition caused by *Borrelia* infection. None of phenol's known actions address this process. The 99.95% score is a knowledge-graph model output only. No trial, publication or mechanistic argument supports it, so the prediction is **not** considered credible at this stage.

Among the other predicted indications, **acne keloid** (rank 5, score 99.94%) is the only one with a plausible, indirect rationale. Topical phenol chemical peels are used for acne scars and skin resurfacing, and a scar-remodeling or keratolytic rationale is conceivable. However, the literature found concerns acne scars and wrinkles, not acne keloid itself. It is best treated as a research question, not a treatment recommendation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

The approved indication text is not provided for any of the listed products.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| M022 | CVS Sore Throat | Spray | CVS Pharmacy, Inc. |
| M022 | Chloraseptic Sore Throat Menthol | Spray | Prestige Brands Holdings, Inc. |
| M022 | Rugby | Spray | Rugby Laboratories |
| Not listed | Carbolicum acidum | Pellet | Boiron |
| Not listed | Acidum Carbolicum | Pellet | Hahnemann Laboratories, Inc. |

The record lists 20 authorizations in total; the table shows 5 of them.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no supporting trials or literature, and phenol has no known mechanism relevant to *Borrelia*-driven atrophic skin disease. Basic safety and mechanism data are also missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- For any dermatologic direction, a targeted literature review, with acne keloid as the first candidate to investigate
- Route and dosage-form compatibility assessment against the predicted indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

