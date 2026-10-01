---
layout: default
title: Insulin Lispro
parent: Model Prediction Only (L5)
nav_order: 802
evidence_level: L5
indication_count: 9
---

# Insulin Lispro
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

# Insulin Lispro: From Diabetes Mellitus to Autoimmune Oophoritis

## One-Sentence Summary

Insulin lispro is a rapid-acting insulin analog, marketed in the US as Humalog for glycemic control in diabetes. The TxGNN model predicts it may be relevant to **autoimmune oophoritis**, but **no clinical trials and no publications** currently support this prediction, and the supplied data show no mechanistic link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetes mellitus (general knowledge; the supplied license records contain no indication text) |
| Predicted New Indication | Autoimmune oophoritis |
| TxGNN Prediction Score | 99.78% (model rank 45) |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (BLA-licensed biologic) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Insulin lispro is a rapid-acting insulin analog, and its use in diabetes is well established. However, nothing in the supplied data supports its use in autoimmune oophoritis.

Insulin has no established role in ovarian autoimmunity. The high score is a knowledge-graph prediction only. It probably reflects autoimmune-disease co-annotation in the graph, not a real therapeutic relationship. Similarity to the original indication has not been assessed, and route compatibility is also pending.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| BLA020563 | HUMALOG | Injection, solution | A-S Medication Solutions |
| BLA021018 | Humalog | Injection, suspension | Eli Lilly and Company |
| BLA021017 | Humalog | Injection, suspension | Eli Lilly and Company |
| BLA020563 | Humalog | Injection, solution | Eli Lilly and Company |
| BLA020563 | Humalog | Injection, solution | Eli Lilly and Company |

Approved indication text is not included in the supplied license records.

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found for this drug.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score (L5). There are no trials or publications, and no plausible mechanism links insulin lispro to autoimmune oophoritis. It is most likely a graph artifact, so the candidate should not advance.

**To proceed, the following is needed:**
- Any disease-specific clinical or preclinical evidence for insulin in autoimmune oophoritis
- A mechanism of action (MOA) dataset from DrugBank to support mechanistic analysis
- FDA package insert warnings and contraindications for safety screening
- If the goal is a more actionable candidate, review the lower-ranked predictions. Pancreatic agenesis (score 99.09%, L4) is mechanistically direct, but it is likely already standard care and the supplied literature does not address it.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

