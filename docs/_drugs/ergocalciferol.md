---
layout: default
title: Ergocalciferol
parent: Model Prediction Only (L5)
nav_order: 667
evidence_level: L5
indication_count: 10
---

# Ergocalciferol
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

# Ergocalciferol: From Vitamin D Deficiency to Familial Isolated Hypoparathyroidism (Impaired PTH Secretion)

## One-Sentence Summary

Ergocalciferol (vitamin D2) is a marketed vitamin D supplement. The US license records in this data set leave the approved-indication text blank.
The TxGNN model predicts it may be effective for **familial isolated hypoparathyroidism due to impaired PTH secretion**.
This prediction has **0 clinical trials** and **0 publications** behind it, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US license records (indication text is blank). Ergocalciferol is generally used as a vitamin D2 supplement for vitamin D deficiency and rickets. |
| Predicted New Indication | Familial isolated hypoparathyroidism due to impaired PTH secretion |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacology, ergocalciferol is a native vitamin D precursor. It must be activated in the liver and kidney before it acts on calcium and phosphate handling.

In hypoparathyroidism, low PTH causes hypocalcemia, and vitamin D analogs are used to manage that. This gives the prediction some biological plausibility.

There is an important caveat. The kidney's conversion of vitamin D to its active form depends on PTH, and PTH secretion is impaired in this condition. Clinicians therefore usually choose active metabolites such as calcitriol or alfacalcidol over native ergocalciferol. The high score may reflect a broad link between "vitamin D" and "calcium disorders" in the knowledge graph rather than evidence that ergocalciferol works here.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

The indication text is blank in all listed records. Only the first 5 of the 20 authorizations are shown.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA090455 | VITAMIN D (REMEDYREPACK INC.) | Capsule | Not stated in record |
| ANDA040833 | Ergocalciferol (Chartwell RX, LLC) | Capsule | Not stated in record |
| ANDA080704 | Ergocalciferol (PD-Rx Pharmaceuticals, Inc.) | Capsule, liquid filled | Not stated in record |
| ANDA080704 | Ergocalciferol (Bryant Ranch Prepack) | Capsule, liquid filled | Not stated in record |
| ANDA080704 | Ergocalciferol (Bryant Ranch Prepack) | Capsule, liquid filled | Not stated in record |

All listed products are oral capsules.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no trials or publications, so it stays at evidence level L5. Mechanistically, active vitamin D metabolites are the usual choice when PTH-dependent activation is impaired. A blocking gap also remains: the package insert warnings and contraindications have not been retrieved.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data (MOA)
- Evidence that native ergocalciferol has any role in this condition compared with calcitriol or alfacalcidol
- Consideration of other candidates from the same run, which have more supporting evidence. Renal osteodystrophy is the most advanced (evidence L3, stage S2, with two registered trials and comparative studies including ergocalciferol vs calcitriol in children). Hypophosphatemic rickets and vitamin D-dependent rickets also have supporting literature.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

