---
layout: default
title: Ammonia
parent: Model Prediction Only (L5)
nav_order: 330
evidence_level: L5
indication_count: 6
---

# Ammonia
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Ammonia: From Marketed Ammonia Products (No Labeled Indication on Record) to Acrodermatitis Chronica Atrophicans

## One-Sentence Summary

Ammonia is marketed in the US mainly as smelling salts and inhalants, but no approved indication text is on record.
The TxGNN model predicts it may be effective for **acrodermatitis chronica atrophicans**,
with **0 clinical trials** and **0 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded (all listed authorizations have empty indication text) |
| Predicted New Indication | Acrodermatitis chronica atrophicans |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available, and no original indication is recorded. Ammonia is sold as smelling salts and inhalants, and it is an endogenous metabolite that is toxic at elevated levels. A mechanistic link to the predicted disease cannot be established from the available data.

Acrodermatitis chronica atrophicans is a late-stage skin manifestation of Lyme borreliosis, which is an infection. No plausible role for ammonia is evident. The high score (0.997) most likely reflects the structure of the knowledge graph, not a drug-specific mechanism.

Ammonia is a known irritant and caustic agent for skin and airways. That argues for caution rather than benefit in a skin disease. The same score-only pattern applies to the five other predicted indications, which have the same evidence level (L5) and recommendation (Hold):
- neonatal dermatomyositis
- acne keloid
- secondary interstitial lung disease specific to childhood associated with a connective tissue disease
- amyopathic dermatomyositis
- familial hydroa vacciniforme

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M011 | UpSniff Smelling Salts | Powder | Not specified in record |
| M011 | SERYNTH SMELLING SALTS | Inhalant | Not specified in record |
| Not listed | Ammonium Causticum | Pellet | Not specified in record |
| Not listed | VYV Smelling Salts | Inhalant | Not specified in record |
| Not listed | Snap Labs Ammonia Inhalants | Inhalant | Not specified in record |

The table shows 5 of 20 authorizations. Other dosage forms on record include granule and gas.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a computational score. There are no trials, no publications, no mechanism data and no recorded original indication. Ammonia's irritant properties and the infectious nature of the predicted disease add to the doubt. The prediction is likely a knowledge-graph artifact.

**To proceed, the following is needed:**
- Mechanism of action data (MOA), for example from DrugBank
- FDA package insert warnings and contraindications, which are needed before any safety screening
- Any independent preclinical, clinical or literature evidence linking ammonia to the predicted disease
- Confirmation of the approved indication text for the listed products
- Route compatibility assessment, since inhalant, powder and pellet forms may not suit a dermatologic indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

