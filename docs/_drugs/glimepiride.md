---
layout: default
title: Glimepiride
parent: Model Prediction Only (L5)
nav_order: 753
evidence_level: L5
indication_count: 9
---

# Glimepiride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Glimepiride: From Type 2 Diabetes to Classic Stiff Person Syndrome

## One-Sentence Summary

Glimepiride is a sulfonylurea oral antidiabetic drug. The pack does not give its original indication text, so this comes from general drug knowledge.
The TxGNN model predicts it may be effective for **classic stiff person syndrome**, but **0 clinical trials** and **0 publications** currently support this direction.
The prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (general knowledge; the license records contain no indication text) |
| Predicted New Indication | Classic stiff person syndrome |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, glimepiride is a sulfonylurea that closes pancreatic beta-cell KATP channels and stimulates insulin release. Its efficacy in diabetes is established, but no mechanism has been shown to apply to stiff person syndrome.

Stiff person syndrome is an autoimmune disorder of GABAergic neurotransmission, typically involving anti-GAD65 antibodies. Glimepiride has no known action on that pathway. The high score most likely reflects knowledge-graph proximity: GAD autoimmunity frequently co-occurs with diabetes, so the two sit close together in the graph. It probably does not reflect a therapeutic effect.

The same caution applies to the other predictions in this pack, such as focal stiff limb syndrome, the lipodystrophy cluster and pancreatic agenesis. Their scores are nearly identical, which suggests a shared graph-neighborhood artifact rather than an indication-specific signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA202112 | Glimepiride | Tablet | A-S Medication Solutions |
| ANDA077091 | Glimepiride | Tablet | Dr. Reddy's Laboratories Limited; NuCare Pharmaceuticals, Inc. |
| ANDA202759 | Glimepiride | Tablet | Aurobindo Pharma Limited |

The pack lists 20 licenses in total, and the table shows only the 5 records provided (one duplicate merged). All products are oral tablets.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no literature and no plausible mechanism. It appears to come from graph proximity through diabetes and GAD autoimmunity. Evidence is at the model-prediction-only level (L5).

**To proceed, the following is needed:**
- Mechanism of action data from DrugBank, and an assessment of any link to GABAergic or GAD65-mediated pathology
- The FDA package insert (warnings and contraindications), which is required for safety screening
- A targeted literature search for glimepiride or sulfonylureas in stiff person syndrome
- A check of the model output for an artifact caused by the diabetes and GAD-autoimmunity association
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

