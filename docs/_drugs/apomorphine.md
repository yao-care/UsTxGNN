---
layout: default
title: Apomorphine
parent: Model Prediction Only (L5)
nav_order: 393
evidence_level: L5
indication_count: 10
---

# Apomorphine
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

# Apomorphine: From Parkinson's Disease to Polymicrogyria, Perisylvian, with Cerebellar Hypoplasia and Arthrogryposis

## One-Sentence Summary

Apomorphine is a dopamine agonist marketed in the US as injectable products. The evidence pack does not list its approved indication; these products are generally known for Parkinson's disease, but that was not verified here.
The TxGNN model predicts it may be effective for **polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis**, an ultra-rare congenital malformation.
There are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the data provided (see note above) |
| Predicted New Indication | Polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 3 (2 NDAs and 1 ANDA) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Apomorphine is a directly acting dopamine receptor agonist (D1/D2). It is a symptomatic treatment that stimulates dopamine receptors and does not modify disease.

No mechanistic link to this prediction was identified. Perisylvian polymicrogyria with cerebellar hypoplasia and arthrogryposis is a structural congenital malformation of brain development. A symptomatic dopamine agonist has no plausible disease-modifying role in it. The high score (rank 6,785 in the model's overall ranking) reflects a knowledge-graph association only, not biological or clinical support.

Among the other nine predictions, only two came with retrieved literature or trials:
- **Schizophrenia (rank 5, score 99.69%)**: The evidence is indirect and mostly historical (1975–2003). Apomorphine has been used mainly as a probe of dopamine function. Under the dopamine hypothesis, a dopamine agonist is more likely to aggravate psychosis than treat it, so the direction of effect is questionable.
- **Retinal dystrophy (rank 3)**: The 15 retrieved papers are general reviews and case reports on congenital eye and orbital disorders. None mention apomorphine.

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
| NDA 214056 | ONAPGO | Injection, solution | Not listed in the data provided |
| NDA 021264 | APOKYN | Injection | Not listed in the data provided |
| ANDA 212025 | Apomorphine hydrochloride (TruPharma) | Injection | Not listed in the data provided |

All three products are injectables.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the queried data.

One class-level concern arises from the evidence pack: as a dopamine agonist, apomorphine may worsen psychotic symptoms, which matters for any psychiatric repurposing hypothesis.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no trials, no relevant literature, and no plausible mechanism for a symptomatic dopamine agonist in a structural congenital brain malformation.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the FDA label, which are currently missing and block safety screening
- Mechanism of action data from DrugBank
- A biological rationale linking dopamine receptor agonism to this malformation
- A drug-level literature search that names apomorphine explicitly
- If a psychiatric direction is pursued, a resolution of the psychosis-aggravation risk before any therapeutic hypothesis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

