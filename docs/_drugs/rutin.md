---
layout: default
title: Rutin
parent: Model Prediction Only (L5)
nav_order: 1139
evidence_level: L5
indication_count: 8
monitor_inn: "Rutin"
predicted_indications: ["breast fibrocystic disease", "apocrine adenosis of breast", "blunt duct adenosis of breast", "benign mammary dysplasia", "vulvovaginal candidiasis", "fat necrosis of breast", "breast abscess", "vaginitis (disease)"]
last_modified_at: 2026-10-30
description: "Rutin: predicted new indication Breast fibrocystic disease (evidence level L5). Approved use: Not recorded in the local data"
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Rutin: Breast fibrocystic disease
{: .text-alpha }

## One-Sentence Summary

Rutin is a flavonoid compound whose original indications are ascorbic acid deficiency and scurvy.
The TxGNN model predicts it may be effective for **breast fibrocystic disease**,
but currently there are **0 clinical trials** and **0 publications** supporting this prediction, so it remains a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Breast fibrocystic disease |
| TxGNN Prediction Score | 0.9974 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 3 of 3) |
| Number of FDA Applications | 3 (valid: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, rutin is a flavonoid with reported antioxidant and vascular-protective (capillary fragility) properties. This could plausibly relate to inflammation or microvascular changes in breast tissue, but this link is speculative.

The high TxGNN score is a computational prediction only. Several other benign breast conditions also appear among the top predictions (apocrine adenosis, blunt duct adenosis, benign mammary dysplasia, fat necrosis of breast). Their identical or near-identical scores may reflect similarities the TxGNN model (deep learning) learned between related diseases, not biological evidence or independent lines of evidence. No clinical trials or publications support any of them.

Other predicted indications include vulvovaginal candidiasis, breast abscess and vaginitis. Flavonoids have some reported in vitro antifungal and anti-inflammatory activity, but nothing in the data compiled for this report supports this for rutin specifically. The two publications retrieved for vaginitis concern plant extracts in rat models of polycystic ovarian syndrome, not rutin and not vaginitis, so they offer no meaningful support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA219685 | WAYRILZ | Tablet, film coated | Not specified (status: valid) |
| NDA216059 | JAYPIRCA | Tablet, coated | Not specified (status: valid) |
| Not available | Rutin (Professional Complementary Health Formulas) | Liquid | Not specified (status: cancelled) |

All three authorizations are valid, and no approved indication text is recorded for any of them.

## Safety Considerations

- **Knowledge-graph contraindication signals** (these come from the TxGNN knowledge graph, not from label text): sickle cell anemia, hereditary persistence of fetal hemoglobin, primary hyperoxaluria, hereditary hemochromatosis, hemosiderosis, iron metabolism disease, Wilson disease.

Please refer to the package insert for further safety information, including warnings and drug interactions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score (L5). There are no clinical trials or relevant publications, the mechanism of action is unavailable, and all US authorizations are valid. Label-based safety information is also missing, which blocks safety screening.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (download and parse the label)
- Mechanism of action data (for example, from DrugBank)
- Targeted literature search on rutin or quercetin-glycoside use in benign breast disease
- Preclinical or early clinical evidence for the predicted indication
- Route and formulation compatibility assessment for the predicted indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

