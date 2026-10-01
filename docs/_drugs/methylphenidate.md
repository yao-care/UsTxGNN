---
layout: default
title: Methylphenidate
parent: Model Prediction Only (L5)
nav_order: 916
evidence_level: L5
indication_count: 4
---

# Methylphenidate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Methylphenidate: From ADHD to Faciodigitogenital Syndrome

## One-Sentence Summary

Methylphenidate is a marketed dopamine/norepinephrine reuptake inhibitor, used mainly for ADHD (the label text is not in the data provided).
The TxGNN model predicts it may be effective for **faciodigitogenital syndrome** (Aarskog-Scott syndrome) with a very high score, but there are **0 clinical trials** and **0 publications** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ADHD (inferred from the evidence pack; approved indication text is not available in the licence records) |
| Predicted New Indication | Faciodigitogenital syndrome |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Methylphenidate blocks dopamine and norepinephrine transporters, which enhances catecholaminergic signalling in the brain. This is the basis of its use in ADHD.

Faciodigitogenital syndrome is an X-linked developmental disorder caused by *FGD1* mutations. No plausible mechanistic link was identified between transporter inhibition and this pathology. The very high score most likely reflects knowledge-graph topology, such as shared neurodevelopmental or ADHD-like phenotype nodes. It probably does not reflect a real pharmacological relationship. The prediction is therefore treated as a model artefact until independent evidence appears.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA091601 | Methylphenidate Hydrochloride | Solution | Cranbury Pharmaceuticals, LLC |
| ANDA203583 | Methylphenidate Hydrochloride | Extended-release capsule | SpecGx LLC |
| ANDA075629 | Methylphenidate Hydrochloride | Extended-release tablet | SpecGx LLC |
| NDA021259 | Methylphenidate Hydrochloride CD | Extended-release capsule | Lannett Company, Inc. |

The records provided do not include approved indication text. Other listed forms include tablets, capsules and film-coated extended-release tablets.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a high model score. It has no mechanistic rationale, trials or publications, so it stays at L5 (model prediction only) and should not advance.

**To proceed, the following is needed:**
- Independent biological evidence linking catecholamine reuptake inhibition to *FGD1*-related pathology
- Any clinical or preclinical study in Aarskog-Scott syndrome
- FDA package insert warnings and contraindications
- Formal MOA data from DrugBank

**Other candidates in this pack:** the third-ranked prediction, *specific developmental disorder*, has more support. It is L2, based on a completed Phase 2 placebo-controlled trial in childhood apraxia of speech (NCT05185583, n=18, no results provided). It is more worth pursuing than this top-ranked prediction.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

