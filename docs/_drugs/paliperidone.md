---
layout: default
title: Paliperidone
parent: Model Prediction Only (L5)
nav_order: 1010
evidence_level: L5
indication_count: 10
---

# Paliperidone
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

# Paliperidone: From Schizophrenia to Retinal Dystrophy (With or Without Extraocular Anomalies)

## One-Sentence Summary

Paliperidone is an atypical antipsychotic originally used to treat schizophrenia and related psychotic disorders.
The TxGNN model predicts it may be effective for **retinal dystrophy with or without extraocular anomalies**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia, schizoaffective disorder, schizophreniform disorder, psychotic disorder, mental disorder |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (all 12 authorizations are cancelled) |
| Number of NDAs | 12 authorizations in total (3 NDAs and 9 ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Paliperidone is known to be the active metabolite of risperidone (9-hydroxyrisperidone) and acts as a dopamine D2 and serotonin 5-HT2A antagonist. Its efficacy in schizophrenia and related psychotic disorders is established.

No plausible link between this receptor pharmacology and inherited retinal dystrophy has been shown. Retinal dystrophies are mostly monogenic degenerative conditions of the retina. The very high TxGNN score (0.999) most likely reflects similarity within the knowledge graph rather than a biologically validated mechanism. No trial or publication was found to support the connection, and the similarity between the original and predicted indications could not be assessed.

For this reason the prediction should be treated as a computational hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

All 12 authorizations are cancelled. The table lists five of them, and approved indication text was not available for any of them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022264 | INVEGA SUSTENNA | Injection | Not specified |
| NDA207946 | INVEGA TRINZA | Injection, suspension, extended release | Not specified |
| NDA216352 | Erzofri extended-release | Injection | Not specified |
| ANDA203802 | Paliperidone | Tablet, film coated, extended release | Not specified |
| ANDA204707 | Paliperidone | Tablet, extended release | Not specified |

Available dosage forms include extended-release oral tablets and extended-release injectables.

## Safety Considerations

- **Conditions flagged in the knowledge graph (not label text):** The knowledge graph links paliperidone to the following conditions as contraindications or cautions:
  - Cardiovascular: long QT syndrome (including familial), torsades de pointes, orthostatic hypotension, postural orthostatic tachycardia syndrome, hypotensive disorder, myocardial infarction, coronary thrombosis.
  - Metabolic: diabetes mellitus, diabetic ketoacidosis, hyperglycemia, hyperlipidemia (including familial), obesity disorder, potassium deficiency disease.
  - Neurological: epilepsy, basal ganglia disease, multiple system atrophy, focal hand dystonia, blepharospasm.
  - Haematological: neutropenia, agranulocytosis, hemoglobinopathy.
  - Gastrointestinal: Crohn disease, inflammatory bowel disease.
  - Other: impaired renal function disease, female breast carcinoma.
- **Drug Interactions:** 100 interactions were recorded. The two classified as **Major** are:
  - Bupropion
  - Morphine

  Notable Moderate interactions include:
  - Antidiabetic agents (metformin, pioglitazone, alogliptin, canagliflozin, chlorpropamide, acarbose, albiglutide)
  - Anticholinergic agents (atropine, hyoscyamine, glycopyrronium)
  - Epinephrine
  - Hydrocortisone
  - Famotidine
  - Loperamide
  - Amphotericin B
  - Lorcaserin
  - Bisacodyl

Please refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no clinical trials or publications and no demonstrated mechanism linking paliperidone to retinal dystrophy. All US authorizations are also cancelled.

The only predicted indication in this dataset with any supporting activity is **treatment-refractory schizophrenia** (rank 10, L3, score 99.80%). It has three Phase 4 trials and two reviews. These appear to be comparator, adjunctive-strategy, or exploratory designs rather than paliperidone-specific efficacy evidence, and clozapine remains the standard for that population. This is essentially an extension of the existing schizophrenia indication and would be better treated as a separate research question than as true repurposing.

**To proceed, the following is needed:**
- Mechanism of action data and a biological rationale connecting dopaminergic or serotonergic antagonism to retinal degeneration
- Preclinical evidence (for example, retinal disease models) before any clinical consideration
- Package insert warnings and contraindications to complete the safety review
- Verification of the cancelled market status and its effect on development feasibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

