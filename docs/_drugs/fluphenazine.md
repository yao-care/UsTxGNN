---
layout: default
title: Fluphenazine
parent: Model Prediction Only (L5)
nav_order: 725
evidence_level: L5
indication_count: 10
monitor_inn: "FLUPHENAZINE"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "syndromic myopia", "myopia X-linked", "hydranencephaly (disease)", "congenital disorder of glycosylation with defective fucosylation", "myopia 26, X-linked, female-limited", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "atypical glycine encephalopathy", "manic bipolar affective disorder"]
last_modified_at: 2026-10-14
description: "Fluphenazine: predicted new indication Retinal dystrophy with or without extraocular anomalies (evidence level L5). Approved use: Schizophrenia, psychotic disorder, schizoaffective disorder…"
---

# Fluphenazine
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

## Fluphenazine: From Schizophrenia and Psychotic Disorders to Retinal Dystrophy
{: .text-alpha }

## One-Sentence Summary

Fluphenazine is a phenothiazine antipsychotic, originally used to treat schizophrenia and related psychotic disorders.
The TxGNN model predicts it may be effective for **retinal dystrophy with or without extraocular anomalies**,
but **0 clinical trials** and **0 publications** currently support this direction. It is a network-based prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia, psychotic disorder, schizoaffective disorder, schizophreniform disorder, mental disorder |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | ✗ Cancelled only (no active authorizations) |
| Number of NDAs | 13 (all cancelled; ANDA generic applications) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Fluphenazine is known as a phenothiazine dopamine D2 receptor antagonist, and its efficacy in schizophrenia and other psychotic disorders is well established.

**The prediction is not mechanistically supported.** No known pathway connects D2 antagonism to inherited retinal dystrophies, which are genetically driven degenerative conditions. The high TxGNN score (99.99%) reflects network-based similarity in the knowledge graph, not biological or clinical evidence. Phenothiazines are also associated with retinal toxicity (pigmentary retinopathy) at high doses, which argues against this use.

The related predictions for syndromic myopia, X-linked myopia and several congenital neurological or metabolic disorders show the same pattern: no mechanism and no evidence. Of the ten predictions reviewed, only **manic bipolar affective disorder** (rank 10) is biologically plausible, because D2 antagonism underlies antipsychotic efficacy in mania.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

All 13 authorizations are generic applications (ANDA) with cancelled status, and none is currently valid. Five examples:

| Authorization Number | Product Name | Dosage Form | Manufacturer | Status |
|---------|------|------|------|------|
| ANDA218173 | Fluphenazine Hydrochloride | Film-coated tablet | Alembic Pharmaceuticals Inc. | Cancelled |
| ANDA213647 | Fluphenazine Hydrochloride | Film-coated tablet | Amneal Pharmaceuticals NY LLC | Cancelled |
| ANDA218055 | Fluphenazine Hydrochloride | Tablet | Aurobindo Pharma Limited | Cancelled |
| ANDA089556 | Fluphenazine Hydrochloride | Solution for injection | Fresenius Kabi USA, LLC | Cancelled |
| ANDA040146 | Fluphenazine Hydrochloride | Elixir | PAI Holdings, LLC dba PAI Pharma | Cancelled |

Dosage forms across all authorizations: oral tablets (plain and film-coated), injectable solution and oral elixir.

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for label safety information.

- **Contraindications from the knowledge graph (not label text):** The TxGNN knowledge graph links fluphenazine to contraindications in the following groups:
  - Cardiovascular and conduction: long QT syndrome (including familial), torsades de pointes, sudden cardiac arrest, heart conduction disease, myocardial infarction, coronary thrombosis, orthostatic hypotension, postural orthostatic tachycardia syndrome.
  - Blood disorders: neutropenia, agranulocytosis, leukopenia, thrombocytopenia, anemia (including macrocytic), hemoglobinopathy.
  - Neurological: epilepsy, basal ganglia disease, multiple system atrophy, focal hand dystonia, blepharospasm.
  - Other: liver disease, gallbladder disease, hyperglycemia, obesity disorder, benign prostatic hyperplasia, female breast carcinoma, substance abuse/dependence.
- **Drug Interactions:** The query returned 100 interactions in total. The 20 shown include:
  - **Major:** bupropion, morphine.
  - **Moderate:** antidiabetic agents (acarbose, metformin, pioglitazone, alogliptin, albiglutide), corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone), anticholinergics (atropine, hyoscyamine, loperamide), famotidine, epinephrine, amphotericin B and lorcaserin.
  - **Minor:** ascorbic acid.
- **Ocular safety:** Phenothiazines can cause pigmentary retinopathy, which is directly relevant to any retinal indication.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph-based score. No clinical trials or literature support it, no mechanism links D2 antagonism to retinal dystrophy, and phenothiazine retinal toxicity argues against the use. All US authorizations are also cancelled.

**To proceed, the following is needed:**
- Mechanistic evidence, or preclinical data, showing a plausible effect in retinal dystrophy models
- Package insert warnings and contraindications, and detailed MOA data
- An assessment of retinal toxicity risk at therapeutic doses
- Consideration of redirecting effort to **manic bipolar affective disorder** (rank 10). It is the only prediction with a plausible mechanism and literature, namely long-acting injectable antipsychotic reviews. Its evidence is indirect (L4), no trials are registered, and the cancelled US market status limits practical development.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

