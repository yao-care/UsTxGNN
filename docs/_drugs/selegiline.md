---
layout: default
title: Selegiline
parent: Model Prediction Only (L5)
nav_order: 1150
evidence_level: L5
indication_count: 4
---

# Selegiline
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

# Selegiline: From Parkinson's Disease and Depression to Perisylvian Polymicrogyria with Cerebellar Hypoplasia and Arthrogryposis

## One-Sentence Summary

Selegiline is a monoamine oxidase B (MAO-B) inhibitor, published literature describes it as approved for Parkinson's disease (oral) and major depressive disorder (transdermal patch).
The TxGNN model predicts it may be effective for **polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis**, a rare neurodevelopmental malformation syndrome.
This prediction has **0 clinical trials** and **0 publications** behind it, so it is a model output only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease (oral) and major depressive disorder (transdermal), per published literature; US label indication text was not available in the data |
| Predicted New Indication | Polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis |
| TxGNN Prediction Score | 99.15% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 17 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank for this record. Published literature describes selegiline as an irreversible, selective MAO-B inhibitor. At oral doses of 20 mg/day or more it also inhibits MAO-A. This raises dopamine and other monoamines, which explains its use in Parkinson's disease and depression.

The data do not support a mechanistic link to this predicted condition. Perisylvian polymicrogyria with cerebellar hypoplasia and arthrogryposis is a rare developmental malformation syndrome. MAO-B inhibition has no established relevance to its pathogenesis. The score is high (99.15%, model rank 18,550), but it is a computational prediction with no supporting studies. The similarity between the original and predicted indications has not been assessed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| NDA021336 | EMSAM (Viatris Specialty LLC) | Patch |
| ANDA074672 | Selegiline Hydrochloride (A2A Integrated Pharmaceuticals) | Tablet |
| ANDA206803 | Selegiline Hydrochloride (Rising Pharma Holdings, Inc.) | Capsule |
| ANDA074871 | Selegiline Hydrochloride (A-S Medication Solutions) | Tablet |

There are 17 licenses in total, and 4 distinct ones are shown above. Other available forms include orally disintegrating tablets. Approved indication text was not provided in the data.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on the TxGNN model score. There are no trials or literature, and no biological link between MAO-B inhibition and this malformation syndrome.

**To proceed, the following is needed:**
- Evidence of a plausible mechanism, or any drug-specific study for this condition
- Package insert warnings and contraindications, which are currently a blocking data gap
- Mechanism of action data from DrugBank
- Route and formulation compatibility assessment

**Note on other predictions:** The second-ranked prediction, **schizophrenia** (score 99.14%), has much stronger support. It has one completed trial (NCT00456976, 70 inpatients, selegiline augmentation for negative symptoms) and several randomized add-on studies, including PMID 15677608 and PMID 17972359. It is graded L2 with a "Research Question" recommendation. If a candidate is to be advanced, it should be evaluated separately from this one.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

