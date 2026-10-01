---
layout: default
title: Hydroquinone
parent: Model Prediction Only (L5)
nav_order: 778
evidence_level: L5
indication_count: 4
---

# Hydroquinone
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

# Hydroquinone: From Hyperpigmentation to Seborrheic Keratosis

## One-Sentence Summary

Hydroquinone is a topical skin-lightening agent. The available data do not state its approved indication, but its US products and related trials point to hyperpigmentation such as melasma. The TxGNN model predicts it may help with **seborrheic keratosis**, but there are **0 clinical trials** and only **2 indirect publications** for this indication, so the evidence is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperpigmentation (e.g., melasma), inferred from product use and related trials. The license records do not state an approved indication. |
| Predicted New Indication | Seborrheic keratosis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 (indirect literature and mechanistic inference only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 19 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the Evidence Pack. Hydroquinone is generally understood to inhibit tyrosinase and reduce melanin synthesis. This link is inferred, not confirmed by the input data.

Some seborrheic keratoses, including dermatosis papulosa nigra (DPN), are dark, pigmented lesions. DPN is histologically very similar to seborrheic keratosis. A depigmenting agent could therefore plausibly lighten their color.

The benefit would probably be cosmetic only. Hydroquinone would not be expected to treat the keratinocyte proliferation that defines the lesion. The high TxGNN score is a model prediction, not proof of clinical benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for seborrheic keratosis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33046430](https://pubmed.ncbi.nlm.nih.gov/33046430/) | 2021 | Prospective observational study | J Plast Reconstr Aesthet Surg | A combination treatment algorithm for facial pigmentary disorders in Asian patients. It addresses multiple pigmentary conditions at once and is only indirectly related to seborrheic keratosis. |
| [17373158](https://pubmed.ncbi.nlm.nih.gov/17373158/) | 2007 | Review | J Drugs Dermatol | Treatment options for dermatosis papulosa nigra, a condition histologically close to seborrheic keratosis. Patients mainly seek removal for cosmetic reasons, and the abstract does not show hydroquinone as an established treatment. |

---

## US Market Information

The Evidence Pack lists 19 authorizations. The main ones are below. Their approved indication text is blank in the records, so that column is omitted.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| Not listed | Hydroquinone | Cream | Westminster Pharmaceuticals, LLC |
| Not listed | Hydroquinone 4% | Cream | Akron Pharma Inc |
| Not listed | ZO Skin Health Pigment Control Creme Hydroquinone | Emulsion | ZO Skin Health, Inc. |
| Not listed | Hydroquinone 4% | Cream | SOHM, Inc. |
| Not listed | ZO Skin Health Pigment Control Plus Blending Creme Hydroquinone | Emulsion | ZO Skin Health, Inc. |

Marketed forms include cream, gel, solution, lotion, liquid and emulsion. The cream and gel are topical.

---

## Safety Considerations

Please refer to the package insert for safety information.

Skin irritation is a concern for topical hydroquinone, particularly at mucosal or mucosal-adjacent sites.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but there are no clinical trials for seborrheic keratosis, and the two publications are indirect (one general pigmentary-disorder study, one DPN review). The mechanistic link is plausible only for the pigmentation of some lesions and would not treat the underlying growth.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Confirmed mechanism-of-action data from DrugBank
- Direct evidence of hydroquinone use in seborrheic keratosis or DPN, such as a small pilot or split-lesion study
- Confirmation of the approved indication text for the US products
- A clear clinical goal (cosmetic lightening versus lesion treatment) and a route compatibility assessment

Results are for research reference only and do not constitute medical advice. Repurposing candidates require clinical validation before any use.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

