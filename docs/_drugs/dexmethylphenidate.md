---
layout: default
title: Dexmethylphenidate
parent: Model Prediction Only (L5)
nav_order: 595
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Dexmethylphenidate: predicted new indication Specific developmental disorder (evidence level L5). Approved use: Attention deficit hyperactivity disorder (including the inattentive t…"
monitor_inn: "DEXMETHYLPHENIDATE"
predicted_indications: ["specific developmental disorder", "faciodigitogenital syndrome", "chondromyxoid fibroma", "multiple system atrophy", "variably protease-sensitive prionopathy", "manic bipolar affective disorder", "trichotillomania", "cerebellar ataxia", "autosomal dominant cerebellar ataxia", "postural orthostatic tachycardia syndrome"]
---

# Dexmethylphenidate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Dexmethylphenidate: From Attention Deficit Hyperactivity Disorder to Specific Developmental Disorder
{: .text-alpha }

## One-Sentence Summary

Dexmethylphenidate was originally used to treat attention deficit hyperactivity disorder (ADHD).
The TxGNN model predicts it may be effective for **specific developmental disorder**,
but **no clinical trials** and **no publications** currently support this prediction. It rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Attention deficit hyperactivity disorder (including the inattentive type) |
| Predicted New Indication | Specific developmental disorder |
| TxGNN Prediction Score | 99.9997% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (all 9 authorizations cancelled) |
| Number of NDAs | 9 (1 NDA and 8 ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, dexmethylphenidate is a central nervous system stimulant that is understood to raise synaptic dopamine and norepinephrine levels by blocking their reuptake. Its efficacy in ADHD is established, but this mechanism cannot be verified from the data compiled for this report.

ADHD is itself a neurodevelopmental condition, so the high score probably reflects closeness between disease classes in the knowledge graph rather than a new therapeutic mechanism. Specific developmental disorders (such as learning or language difficulties) often occur together with ADHD, which may explain the association. This is an interpretation, and no study was supplied to confirm it.

The other top predictions are weaker still. Faciodigitogenital syndrome, chondromyxoid fibroma and variably protease-sensitive prionopathy have no plausible link to this drug mechanism, and their high scores are likely graph artifacts. Multiple system atrophy and postural orthostatic tachycardia syndrome are speculatively linked through catecholamine pathways, but a stimulant could worsen blood pressure or heart rate in both. Manic bipolar affective disorder has two review papers, but they cover treating ADHD within bipolar patients, not treating mania. Stimulants may in fact precipitate mania.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was found for the top predicted indication (specific developmental disorder). The only literature in the compiled data concerns a lower-ranked prediction, manic bipolar affective disorder, and is indirect:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26364896](https://pubmed.ncbi.nlm.nih.gov/26364896/) | 2015 | Review | Expert Opin Pharmacother | Stimulants and atomoxetine in adults with comorbid ADHD and bipolar disorder; effective for ADHD, but use in bipolar disorder has not been extensively studied and may be problematic |
| [17667893](https://pubmed.ncbi.nlm.nih.gov/17667893/) | 2007 | Review | CNS Spectrums | Diagnosis and treatment of adult ADHD with comorbidities such as depression, anxiety and substance use |

## US Market Information

All nine authorizations are cancelled. No approved indication text is available for them.

| Authorization Number | Product Name | Dosage Form | Status |
|---------|------|------|-----------|
| NDA021802 | Focalin (Sandoz Inc) | Extended-release capsule | Cancelled |
| ANDA215523 | Dexmethylphenidate Hydrochloride (Camber) | Extended-release capsule | Cancelled |
| ANDA213813 | Dexmethylphenidate Hydrochloride (Granules) | Extended-release capsule | Cancelled |
| ANDA210279 | Dexmethylphenidate Hydrochloride (Lannett) | Extended-release capsule | Cancelled |
| ANDA212631 | Dexmethylphenidate Hydrochloride (Ascend) | Tablet | Cancelled |

Four further authorizations (extended-release capsule from Par Health; tablets from Bryant Ranch Prepack, Lupin and Sun Pharmaceutical) are also cancelled.

## Safety Considerations

- **Conditions flagged in the knowledge graph as contraindicated** (from drug-disease graph edges, not package insert text):
  - Cardiovascular: hypertension, coronary artery disease, myocardial infarction, stroke and cerebrovascular disorders, cardiomyopathy including hypertrophic cardiomyopathy
  - Psychiatric: bipolar disorder, psychotic disorders including schizoaffective disorder, substance abuse and dependence
  - Neurological and eye: epilepsy, glaucoma, vision disorders
  - Blood: thrombocytopenia, anemia, leukopenia, hemoglobinopathy
- **Drug Interactions**: 38 interactions are recorded; 20 are listed in the compiled data.
  - **Major**: bupropion, iohexol, iopamidol, methylene blue, topical cocaine
  - **Moderate**: sympathomimetics (epinephrine, ephedrine, pseudoephedrine, phenylephrine, isometheptene) and beta-agonists (formoterol, salbutamol); also promethazine, lindane, ioflupane I-123 and bowel-preparation agents (picosulfuric acid, sodium sulfate, polyethylene glycol with electrolytes)
  - **Minor**: warfarin, dicoumarol
- **Prediction-specific concerns**: for the manic bipolar disorder, multiple system atrophy and POTS predictions, stimulant effects could worsen the condition (mood destabilization, blood pressure or heart rate instability).

Please refer to the package insert for warnings and contraindications, which were not available in the compiled data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score only (L5), with no trials or literature, and the score may reflect disease-class proximity to ADHD rather than a true new indication. All US authorizations are also cancelled, and the knowledge graph flags several relevant safety conditions.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) to assess the mechanistic link
- FDA package insert warnings and contraindications for formal safety screening
- A literature and trial search specific to specific developmental disorder, and a clear definition of which conditions that term covers
- Clarification of why the drug is no longer marketed in the US (cancelled authorizations)
- Review of the other top predictions, which are likely artifacts or safety-limited, only if a clear rationale emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

