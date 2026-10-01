---
layout: default
title: Disopyramide
parent: Model Prediction Only (L5)
nav_order: 615
evidence_level: L5
indication_count: 10
---

# Disopyramide
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

# Disopyramide: From Antiarrhythmic Use to Tourette Syndrome

## One-Sentence Summary

Disopyramide is a class Ia antiarrhythmic drug that is currently marketed in the US.
The TxGNN model predicts it may be effective for **Tourette syndrome**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Antiarrhythmic (the approved indication text is not captured in the source data) |
| Predicted New Indication | Tourette syndrome |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 11 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, disopyramide is a sodium-channel-blocking class Ia antiarrhythmic with anticholinergic activity.

No plausible mechanistic link to Tourette syndrome has been identified. Sodium-channel blockade in cardiac tissue does not obviously connect to the neurological basis of tics. The very high TxGNN score is best read as a graph-based signal, not as pharmacological support.

The other top-ranked predictions are mostly neurodevelopmental or psychiatric conditions (ADHD, trichotillomania, developmental disorders). This suggests the model is clustering on graph-neighborhood similarity. Anticholinergic effects and QT-prolongation risk would also be concerns in these populations.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA018655 | Norpace CR | Capsule, extended release | Pfizer Laboratories Div Pfizer Inc |
| NDA017447 | Norpace | Capsule, gelatin coated | Pfizer Laboratories Div Pfizer Inc |
| ANDA070102 | Disopyramide Phosphate | Capsule | Teva Pharmaceuticals USA, Inc. |
| ANDA070173 | Disopyramide Phosphate | Capsule | Dr. Reddy's Laboratories Inc. |

All marketed forms are oral.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical or literature support and no identifiable mechanistic link. Disopyramide's anticholinergic and proarrhythmic liabilities make speculative use in a neurological or pediatric population hard to justify.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are required for safety screening
- Mechanism of action data, for example from DrugBank
- Approved indication text from the current labels
- Any preclinical or clinical signal linking sodium-channel blockade or anticholinergic activity to tic disorders

**Note on other predictions:** Multifocal atrial tachycardia (rank 9) is the only prediction with a mechanistically plausible link and one indirect paper. That paper (PMID 7418495) concerns lorcainide, not disopyramide, so it does not support the prediction. This is a candidate for further review, not for advancement.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

