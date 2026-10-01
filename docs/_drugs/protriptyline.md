---
layout: default
title: Protriptyline
parent: Model Prediction Only (L5)
nav_order: 1096
evidence_level: L5
indication_count: 5
---

# Protriptyline
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

# Protriptyline: From Depression to Attention Deficit Hyperactivity Disorder, Inattentive Type

## One-Sentence Summary

Protriptyline is a tricyclic antidepressant marketed in the United States as oral tablets.
The TxGNN model predicts it may be effective for **attention deficit hyperactivity disorder, inattentive type**, but this is a model prediction only, with **0 clinical trials** and **0 publications** directly supporting this specific subtype.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the source data (drug class: tricyclic antidepressant) |
| Predicted New Indication | Attention deficit hyperactivity disorder, inattentive type |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 4 records (2 unique ANDA numbers, all generics) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source data. Based on general drug-class knowledge, protriptyline is a tricyclic antidepressant that inhibits norepinephrine reuptake. This mechanism has not been confirmed from the data provided.

Noradrenergic modulation is an established strategy in ADHD treatment (for example atomoxetine, and tricyclics as second-line agents). That gives the prediction some pharmacological plausibility.

This link is inferred, not proven. No clinical trials or literature address the inattentive subtype specifically.

Other high-scoring predictions for this drug (rank 2 to 5) are a broad developmental disorder category, chondromyxoid fibroma, and faciodigitogenital syndrome. They have no plausible mechanistic link, and the high scores are likely model artifacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the inattentive subtype.

For the broader indication **attention deficit-hyperactivity disorder** (TxGNN rank 3, score 99.77%), there is one relevant publication:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8936915](https://pubmed.ncbi.nlm.nih.gov/8936915/) | 1996 | Cohort (naturalistic) | J Am Acad Child Adolesc Psychiatry | Naturalistic assessment of protriptyline in children and adolescents with ADHD. It is observational, uncontrolled and dated. |

Two other articles retrieved for this broader indication (PMIDs 19007502 and 22112053) are guanfacine urine assays that use protriptyline only as an internal standard. They are not relevant evidence.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA202220 | Protriptyline Hydrochloride | Tablet, film coated | Epic Pharma, LLC |
| ANDA090462 | Protriptyline Hydrochloride | Tablet, film coated | Sigmapharm Laboratories, LLC |

The source data lists each authorization twice, so only the two unique entries are shown. Approved indication text was not provided. The only route is oral.

## Safety Considerations

Please refer to the package insert for safety information.

For any pediatric ADHD use, the cardiovascular and anticholinergic safety of tricyclics would need careful evaluation.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for the inattentive subtype is model-only (L5), with no trials or literature and no confirmed mechanism data. The only related evidence is one 1996 uncontrolled study in general ADHD, so this candidate is at most a research question.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Confirmed mechanism of action data from DrugBank
- Approved indication text for the US labels
- Controlled clinical evidence in ADHD, plus a pediatric cardiovascular and anticholinergic safety assessment
- Evaluation of the broader ADHD indication (rank 3) as the more practical research direction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

