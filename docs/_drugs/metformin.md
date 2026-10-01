---
layout: default
title: Metformin
parent: Model Prediction Only (L5)
nav_order: 905
evidence_level: L5
indication_count: 5
---

# Metformin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Metformin: From Type 2 Diabetes to Classic Stiff Person Syndrome

## One-Sentence Summary

Metformin is a widely marketed oral glucose-lowering drug. The US license records in the data carry no indication text, so "Type 2 diabetes" here is general drug knowledge rather than data from the pack.
The TxGNN model predicts it may be effective for **classic stiff person syndrome**.
There are currently **0 clinical trials** and **0 publications** supporting this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Classic stiff person syndrome |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the sampled licenses are ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Metformin is a long-established antidiabetic, and its mechanistic link to stiff person syndrome has not been documented or verified.

A speculative link is metformin's AMPK-mediated immunomodulation. Stiff person syndrome is an autoimmune condition, typically associated with anti-GAD65 antibodies. This idea is a hypothesis only.

The TxGNN score of 0.994 is a model output, not clinical evidence. The closely related "focal stiff limb syndrome" received the identical score (0.9945). This suggests the prediction comes from a shared knowledge-graph neighborhood (disease-class similarity) rather than independent drug-specific evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|------|
| ANDA201991 | METFORMIN HYDROCHLORIDE | Tablet, extended release | Northwind Health Company, LLC |
| ANDA077078 | METFORMIN HYDROCHLORIDE | Tablet, extended release | Zydus Lifesciences Limited |
| ANDA211052 | METFORMIN HYDROCHLORIDE | Tablet, extended release | Epic Pharma, LLC |
| ANDA209674 | Metformin | Tablet, extended release | Ingenus Pharmaceuticals, LLC |
| ANDA202917 | Metformin Hydrochloride | Tablet, film coated, extended release | Sun Pharmaceutical Industries, Inc. |

Approved indication text was not provided for these licenses. All listed products are oral formulations.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature (L5, model prediction only). The mechanism is undocumented, and the identical score for a neighboring disease points to class-level similarity rather than drug-specific signal. The same pattern applies to the other four predicted indications (focal stiff limb syndrome, opsismodysplasia, thiamine-responsive dysfunction syndrome, drug-induced localized lipodystrophy), which are also L5 with no evidence.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (e.g., from DrugBank) to test the AMPK/immunomodulation hypothesis
- A literature and trial search for metformin in stiff person syndrome, including preclinical or case-level evidence
- Route compatibility and similarity-to-original-indication assessment (both currently pending)

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

