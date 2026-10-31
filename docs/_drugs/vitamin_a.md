---
layout: default
title: Vitamin A
parent: Model Prediction Only (L5)
nav_order: 1295
evidence_level: L5
indication_count: 10
monitor_inn: "VITAMIN A"
predicted_indications: ["congenital prothrombin deficiency", "biotin metabolic disease", "non-syndromic esophageal malformation", "injury", "cell proliferation disorder", "florid cemento-osseous dysplasia", "perinatal disease", "segmental odontomaxillary dysplasia", "disease by subcellular system affected", "radiation or chemically induced disorder"]
last_modified_at: 2026-10-31
description: "Vitamin A: predicted new indication Congenital prothrombin deficiency (evidence level L5). Approved use: Vitamin deficiency disorder / vitamin A deficiency"
---

# Vitamin A
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Vitamin A: From Vitamin A Deficiency to Congenital Prothrombin Deficiency
{: .text-alpha }

## One-Sentence Summary

Vitamin A is a fat-soluble vitamin, originally used to treat vitamin deficiency disorders, particularly vitamin A deficiency.
The TxGNN model predicts it may be effective for **congenital prothrombin deficiency**, but **no clinical trials and no publications** currently support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vitamin deficiency disorder / vitamin A deficiency |
| Predicted New Indication | Congenital prothrombin deficiency |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 4) |
| Number of FDA Applications | at least 4 |
| Recommended Decision | Hold |

*Note: The original indication is not listed in the TxGNN model's output. The US authorization records compiled for this report contain no approved-indication text.*

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, vitamin A (retinol) is an essential nutrient. Its role in correcting vitamin A deficiency is well established, and its active metabolites act through retinoic acid signaling to support vision, epithelial differentiation, and immune function.

The mechanistic link to the predicted indication is weak. Prothrombin (factor II) synthesis depends on vitamin K, not vitamin A, and congenital prothrombin deficiency is an inherited disorder of the gene encoding prothrombin. No established role for vitamin A in this pathway was identified. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

The drug is marketed in the US, and all four US authorizations on record are valid.

| Authorization Number | Product Name | Dosage Form | Status |
|---------|------|------|-----------|
| NDA006823 | AQUASOL A | Injection, solution | Valid |
| M016 | SKINEEZ | Cloth | Valid |
| Not available | Tri-Vite Drops with Fluoride | Solution | Cancelled |
| 505G(a)(3) | NOAVIA Retinol Moisturizer | Cream | Valid |

## Safety Considerations

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for label safety information.

- **Disease associations flagged in the knowledge graph** (not label text): Kidney disease, liver disease, gallbladder disease, peptic ulcer disease, sarcoidosis, hypercalcemia, nephrocalcinosis, nephrolithiasis, primary hyperoxaluria, hereditary hemochromatosis and other iron metabolism disorders, Wilson disease, sickle cell anemia, hemolytic anemia, inflammatory bowel disease and ulcerative colitis, hypervitaminosis, and others.
- **Drug Interactions** (68 interactions recorded; main ones):
  - **Major:** Retinoids (isotretinoin, acitretin, tretinoin) and tetracycline-class antibiotics (doxycycline, tetracycline, minocycline, demeclocycline, oxytetracycline, omadacycline, eravacycline, sarecycline).
  - **Moderate:** Bile acid sequestrants (cholestyramine, colesevelam, colestipol), sevelamer, bexarotene, and selpercatinib.
  - **Minor:** Orlistat.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for congenital prothrombin deficiency has no supporting trials or literature, and its biological rationale conflicts with known biology, since prothrombin synthesis is vitamin K-dependent. In addition, the drug is marketed in the US with four valid authorizations.

**To proceed, the following is needed:**
- Mechanistic evidence for any role of vitamin A in prothrombin expression or function.
- Mechanism of action data and package insert safety information.
- A review of the other predicted indications. In this dataset, **perinatal disease** (score 0.9963) has the most substantial support. Cochrane systematic reviews of RCTs suggest vitamin A supplementation in very-low-birth-weight infants may reduce death or bronchopulmonary dysplasia. Its benefit is modest and practicality is limited by the route and supply. It is a better candidate for further research than the top-ranked prediction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

