---
layout: default
title: Tazarotene
parent: Model Prediction Only (L5)
nav_order: 1202
evidence_level: L5
indication_count: 3
---

# Tazarotene
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Tazarotene: From Marketed Topical Retinoid to Seborrheic Dermatitis

## One-Sentence Summary

Tazarotene is a topical retinoid marketed in the US as creams and gels.
The TxGNN model predicts it may be effective for **seborrheic dermatitis**, but this rests on the model prediction alone.
There are **0 relevant clinical trials** and **0 publications** for this indication. The one trial retrieved studies acne vulgaris.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Seborrheic dermatitis |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 authorizations (NDA and ANDA combined) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Tazarotene is a topical retinoid prodrug. Its active form, tazarotenic acid, selectively activates the retinoic acid receptors RAR-beta and RAR-gamma. This normalizes keratinocyte differentiation and has antiproliferative and anti-inflammatory effects. These actions could plausibly help the scaling and inflammation seen in seborrheic dermatitis.

The link is indirect and speculative, though. Seborrheic dermatitis is driven mainly by Malassezia-associated inflammation and skin barrier dysfunction, which retinoid activity does not directly address. The very high TxGNN score (0.998) is a model output, not clinical evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06281782](https://clinicaltrials.gov/study/NCT06281782) | N/A | Unknown | 40 | Platelet-rich plasma plus topical retinoids vs topical retinoids alone in acne vulgaris. |

This trial is graded **C (weak relevance)**. It studies acne vulgaris, not seborrheic dermatitis, and gives no efficacy or safety data for the predicted indication. It was likely matched through retinoid and dermatology keywords.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA021184 | TAZORAC | Cream | Almirall, LLC |
| ANDA217075 | Tazarotene | Cream | Bryant Ranch Prepack |
| ANDA217075 | Tazarotene | Cream | Padagis Israel Pharmaceuticals Ltd |
| ANDA213079 | Tazarotene | Gel | Bryant Ranch Prepack |
| ANDA213079 | Tazarotene | Gel | Padagis Israel Pharmaceuticals Ltd |

Lotion and foam forms are also listed among the marketed dosage forms.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical evidence (L5). The only trial found concerns acne, and the mechanistic link to seborrheic dermatitis is indirect. A high model score alone does not justify moving forward.

**To proceed, the following is needed:**
- Obtain the package insert warnings and contraindications, which are currently missing and block safety screening.
- Search for direct clinical or preclinical studies of topical retinoids, including tazarotene, in seborrheic dermatitis.
- Assess the tolerability of tazarotene on seborrheic dermatitis sites such as the face and scalp. Route and formulation compatibility is still pending.

**Note on other predictions:** The rank 2 prediction, **seborrheic keratosis** (score 99.51%, L3), has more supporting material. It has one systematic review of topical treatments and one 2004 comparative study that includes tazarotene. However, neither has been confirmed to show that tazarotene works. The rank 3 prediction, vulvar inverted follicular keratosis (99.38%), has no trials or publications and is also L5 / Hold. Seborrheic keratosis may be the better candidate for a first research question.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

