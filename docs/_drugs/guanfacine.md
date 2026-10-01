---
layout: default
title: Guanfacine
parent: Model Prediction Only (L5)
nav_order: 764
evidence_level: L5
indication_count: 7
---

# Guanfacine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Guanfacine: From ADHD to Faciodigitogenital Syndrome

## One-Sentence Summary

Guanfacine is an alpha-2A adrenergic agonist. The extended-release form is marketed in the US for attention-deficit/hyperactivity disorder (ADHD).
The TxGNN model predicts it may be effective for **faciodigitogenital syndrome**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ADHD (extended-release tablets; the license records contain no indication text, so this comes from the pack's rationale notes) |
| Predicted New Indication | Faciodigitogenital syndrome |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the sample listed below is all ANDA generics) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known information, guanfacine is a selective alpha-2A adrenergic agonist, and its efficacy in ADHD is established. Mechanistically, it may be applicable to faciodigitogenital syndrome only through a speculative link.

The syndrome is reported to include ADHD-like behavioral features. If those features drive the model's score, guanfacine's action on attention and impulsivity could be relevant. No documented mechanism or study connects guanfacine to the syndrome's core features. The high score should be treated as a hypothesis, not as support for efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA217269 | GUANFACINE (Alembic Pharmaceuticals Inc.) | Extended-release tablet | — |
| ANDA205689 | Guanfacine (Bryant Ranch Prepack) | Extended-release tablet | — |
| ANDA201408 | Guanfacine (REMEDYREPACK INC.) | Extended-release tablet | — |
| ANDA217269 | GUANFACINE (Golden State Medical Supply, Inc.) | Extended-release tablet | — |
| ANDA201408 | Guanfacine (Proficient Rx LP) | Extended-release tablet | — |

Oral routes are available for both extended-release and standard tablets.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trials, no literature, and no documented mechanism, so it is a model output only (L5). It should not drive development decisions in its current form.

**To proceed, the following is needed:**
- A targeted literature search on faciodigitogenital syndrome, to check whether any pharmacological or behavioral-treatment evidence exists.
- Mechanism of action data for guanfacine, and a mechanistic link to the syndrome.
- Package insert warnings and contraindications for the safety screen.
- Consider prioritizing the lower-ranked **Tourette syndrome** prediction (rank 7, score 99.27%). It has L1 evidence, with two completed guanfacine trials (NCT00004376, Phase 3; NCT01547000, Phase 4), and could proceed with guardrails. Both trials are small (n=34-35), and use would be off-label.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

