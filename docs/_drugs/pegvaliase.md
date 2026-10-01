---
layout: default
title: Pegvaliase
parent: Model Prediction Only (L5)
nav_order: 1023
evidence_level: L5
indication_count: 3
---

# Pegvaliase
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Pegvaliase: From Phenylketonuria to Diabetic Retinopathy

## One-Sentence Summary

Pegvaliase is a PEGylated phenylalanine ammonia lyase that lowers blood phenylalanine in phenylketonuria (PKU).
The TxGNN model predicts it may be effective for **diabetic retinopathy**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The prediction rests on the knowledge-graph score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Phenylketonuria (PKU); the license records contain no indication text, so this comes from the prediction rationale |
| Predicted New Indication | Diabetic retinopathy |
| TxGNN Prediction Score | 99.17% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 3 (all three records share BLA761079) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Pegvaliase is an enzyme therapy that breaks down phenylalanine, and its use in PKU is the basis of its approval.

The supplied data does not support a mechanistic link between phenylalanine depletion and diabetic retinal microvascular disease. The score of 0.992 is a knowledge-graph association only, and the source record has no MOA or original-indication data to check it against. Any biological rationale would have to be built from the literature.

Two other predictions look like the same signal rather than independent evidence:
- **Severe nonproliferative diabetic retinopathy** (score 99.16%) is a more severe subtype of the same disease.
- **Diabetic cataract** (score 99.11%) probably comes from the same diabetic eye disease cluster. Pegvaliase has no known effect on the polyol pathway or lens opacity.

Pegvaliase is a systemic enzyme therapy with known immunogenicity and anaphylaxis risk. An ocular indication would need a strong rationale, and none is present.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761079 | Palynziq (BioMarin Pharmaceutical Inc.) | Injection, solution | Not provided in the supplied record |

The record lists this authorization three times, with identical product name and dosage form. The only route is injectable.

---

## Safety Considerations

Please refer to the package insert for safety information.

The prediction rationale notes immunogenicity and anaphylaxis risk for this systemic enzyme therapy. No drug interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L5: a model prediction with no trials, no literature and no supported mechanism. The safety data are also incomplete, which blocks progression past the initial screening stage (S0).

**To proceed, the following is needed:**
- The package insert for warnings and contraindications (blocking gap)
- Mechanism of action data, for example from DrugBank
- A literature review testing any link between phenylalanine metabolism and diabetic retinopathy
- A risk-benefit justification for a systemic, immunogenic enzyme therapy in an ocular indication
- An assessment of route compatibility with ocular use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

