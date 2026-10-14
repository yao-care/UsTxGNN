---
layout: default
title: Flurandrenolide
parent: Model Prediction Only (L5)
nav_order: 726
evidence_level: L5
indication_count: 10
---

# Flurandrenolide
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

# Flurandrenolide: From Inflammatory Skin Conditions to Vulvar Inverted Follicular Keratosis

## One-Sentence Summary

Flurandrenolide is a topical corticosteroid, originally used for inflammatory and eczematous skin conditions such as atopic dermatitis, contact dermatitis, seborrheic dermatitis and lichen disease.
The TxGNN model predicts it may be effective for **vulvar inverted follicular keratosis**, but currently there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Inflammatory skin diseases, including atopic eczema, contact dermatitis, seborrheic dermatitis, granuloma annulare, neurodermatitis, lichen disease, lupus erythematosus (discoid/chronic cutaneous) and primary cutaneous T-cell lymphoma (the US approved-indication text was not available) |
| Predicted New Indication | Vulvar inverted follicular keratosis |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid authorization) |
| Number of NDAs | 3 (all cancelled; includes 1 ANDA) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, flurandrenolide is a topical corticosteroid. Its use in inflammatory and eczematous skin diseases is established, and mechanistically a glucocorticoid anti-inflammatory effect may be applicable to some inflammatory skin conditions.

The high score for vulvar inverted follicular keratosis most likely comes from graph proximity to seborrheic keratosis, a related benign keratinocytic lesion that appears among the drug's original indications. However, inverted follicular keratosis is typically treated by excision, and there is no evidence that a corticosteroid is effective. The link is a computational prediction only. The vulvar location also raises a concern about skin atrophy with potent topical steroids.

**Other predicted indications (all L5, all Hold):**

| Rank | Predicted Indication | Score | Comment |
|---|---|---|---|
| 2 | Lichen planus pigmentosus | 99.66% | Inflammatory lichenoid condition, but mainly pigmentary; steroid response is variable |
| 3 | Hypertrophic lichen planus | 99.66% | Potent topical steroids are standard therapy for this class; most mechanistically credible candidate, but no drug-specific evidence |
| 4 | Annular atrophic lichen planus | 99.66% | Plausible mechanism, but the atrophic phenotype makes prolonged potent steroid use a concern |
| 5 | Alopecia areata | 99.62% | Autoimmune; steroids are used as a class, evidence for topical use is modest |
| 6 | Primary cutaneous B-cell lymphoma | 99.61% | Based on proximity to T-cell lymphoma; any benefit would likely be symptomatic only |
| 7 | Alopecia mucinosa | 99.60% | Must be distinguished from lymphoma-associated forms before any consideration |
| 8 | Telogen effluvium | 99.60% | No clear mechanistic rationale; likely a graph artifact |
| 9 | Lichen planus pemphigoides | 99.56% | Systemic steroids are the mainstay; topical may help localized disease |
| 10 | Hereditary hypotrichosis with recurrent skin vesicles | 99.53% | Genetic disorder; no clear rationale |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA016455 | CORDRAN (Almirall, LLC) | Tape | Not available (cancelled) |
| NDA012806 | CORDRAN (INA Pharmaceutics, Inc) | Cream | Not available (cancelled) |
| ANDA207133 | Flurandrenolide (Bryant Ranch Prepack) | Lotion | Not available (cancelled) |

All three authorizations are cancelled, so there is currently no valid US-marketed product.

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease relationships, not label text): adrenocortical insufficiency, Addison disease, skin atrophy, telangiectasis, capillary disease, hereditary hemorrhagic telangiectasia, peripheral vascular disease, intermittent vascular claudication, and peripheral arterial disease.
- **Site-specific concern**: potent topical steroids on vulvar skin and in atrophic lichenoid conditions raise the risk of skin atrophy.
- **Drug interactions**: no interaction records were found.

Please refer to the package insert for further safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for vulvar inverted follicular keratosis has no supporting clinical trials or literature (L5). The condition is normally managed by excision, and the vulvar site raises skin atrophy concerns. All US authorizations are cancelled, and label safety data are missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- A drug-specific literature and trial search for the top indication
- A clinical rationale review against standard care (excision)
- Consideration of hypertrophic lichen planus as the more mechanistically credible candidate, which still needs a drug-specific evidence review
- Route and formulation compatibility assessment, since no currently valid US product exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

