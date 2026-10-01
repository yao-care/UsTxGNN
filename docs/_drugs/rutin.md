---
layout: default
title: Rutin
parent: Model Prediction Only (L5)
nav_order: 1139
evidence_level: L5
indication_count: 8
---

# Rutin
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

# Rutin: From an Unspecified Original Indication to Breast Fibrocystic Disease

## One-Sentence Summary

Rutin is a plant flavonoid, and the provided US regulatory data does not state an approved indication for it.
The TxGNN model predicts it may be effective for **breast fibrocystic disease** (score 99.74%),
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so it is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the provided regulatory data |
| Predicted New Indication | Breast fibrocystic disease |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 4 license records (see the note under US Market Information) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Rutin is a flavonoid with reported antioxidant, anti-inflammatory and vascular-protective properties. These properties could plausibly bear on inflammation in benign breast tissue, but this link is speculative.

No original indication is documented in the provided data, so the relationship between an established use and the predicted one cannot be assessed. The score likely reflects proximity in the TxGNN knowledge graph rather than independent evidence.

Several other top predictions are closely related benign breast conditions:

- Apocrine adenosis of breast (99.64%) and blunt duct adenosis of breast (99.64%) have identical scores, which suggests a shared knowledge-graph neighborhood.
- Benign mammary dysplasia (99.42%) is essentially a synonym-level cluster with fibrocystic disease, so it does not add independent support.
- Lower-ranked predictions are vulvovaginal candidiasis, breast abscess, fat necrosis of breast and vaginitis. None has trial or supporting literature evidence, and established treatments exist for several of them.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for breast fibrocystic disease.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not assigned in data | Rutin (Professional Complementary Health Formulas) | Liquid | Not stated |
| NDA219685 | WAYRILZ (Genzyme Corporation) | Tablet, film coated | Not stated |
| NDA216059 | JAYPIRCA (Eli Lilly and Company), listed twice | Tablet, coated | Not stated |

**Note:** WAYRILZ and JAYPIRCA are branded products of other drugs. They may be mapping artifacts and should be checked before the "Marketed" status is relied on. Only the liquid Rutin product is clearly a rutin product, and it has no NDA number in the data.

---

## Safety Considerations

- **Drug Interactions**: No interaction records were found (query status: not found).

Please refer to the package insert for other safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical, preclinical or literature support for breast fibrocystic disease. The mechanism of action and original indication are unavailable, and the US license records are unreliable for rutin.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, currently a blocking gap for safety screening
- Mechanism of action data, for example from DrugBank
- Verification of which US products actually contain rutin, and their approved indications
- A literature and trial search specific to rutin in benign breast disease, to move beyond L5
- A route-of-administration compatibility check (currently pending)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

