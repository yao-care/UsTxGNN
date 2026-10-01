---
layout: default
title: Piroxicam
parent: Model Prediction Only (L5)
nav_order: 1050
evidence_level: L5
indication_count: 10
---

# Piroxicam
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

# Piroxicam: From NSAID Use to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

## One-Sentence Summary

Piroxicam is a non-selective COX inhibitor (an NSAID) marketed in the United States as an oral capsule.
The TxGNN model predicts it may be effective for **colobomatous microphthalmia-rhizomelic dysplasia syndrome**, a rare developmental malformation syndrome.
There are **0 clinical trials** and **0 publications** supporting this prediction, so it is a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the provided data (NSAID, COX inhibitor) |
| Predicted New Indication | Colobomatous microphthalmia-rhizomelic dysplasia syndrome |
| TxGNN Prediction Score | 99.996% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (listed licenses are ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Based on known information, piroxicam is a non-selective COX-1/COX-2 inhibitor with a long half-life, and its role is to reduce prostaglandin-mediated inflammation and pain.

No plausible mechanistic link to this disease was identified. It is a rare congenital developmental malformation syndrome, and COX inhibition is not expected to change its course. The very high score (0.99996, rank 225) most likely reflects connectivity in the knowledge graph rather than a pharmacological rationale. Treat it as a hypothesis-generating signal only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA210347 | Piroxicam | Capsule | PD-Rx Pharmaceuticals, Inc. |
| ANDA210347 | Piroxicam | Capsule | AvKARE |
| ANDA074116 | Piroxicam | Capsule | Bryant Ranch Prepack |
| ANDA210347 | Piroxicam | Capsule | Strides Pharma Science Limited |

Approved indication text was not provided for these licenses. The only route of administration listed is oral.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature and no plausible mechanism. It sits at evidence level L5 (model prediction only). Pursuing it would need new preclinical or mechanistic support first.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking data gap for safety screening)
- Mechanism of action data from DrugBank
- A mechanistic or preclinical rationale linking COX inhibition to this syndrome

**Note on other candidates:**
Of the 10 predicted indications, only **juvenile idiopathic arthritis** (rank 10, score 99.93%) has supporting literature. It is rated L3 with a "Research Question" recommendation.
- The retrieved literature includes piroxicam-specific studies in juvenile arthritis: a randomized comparison with naproxen (PMID 2957205, 1987) and a double-blind crossover study against naproxen (PMID 3510686, 1986). It also includes two NSAID network meta-analyses (PMIDs 38680254 and 33632948).
- The evidence supports symptomatic use only, not disease modification. Study designs and outcomes are not fully available, and pediatric safety and dosing would need review.
- This candidate is worth evaluating separately from the rank-1 prediction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

