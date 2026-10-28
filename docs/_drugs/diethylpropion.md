---
layout: default
title: Diethylpropion
parent: Model Prediction Only (L5)
nav_order: 604
evidence_level: L5
indication_count: 4
monitor_inn: "DIETHYLPROPION"
predicted_indications: ["hypervitaminosis", "proximal 16p11.2 microdeletion syndrome", "obsolete hypertelorism (disease)", "frontorhiny"]
last_modified_at: 2026-10-28
description: "Diethylpropion: predicted new indication Hypervitaminosis (evidence level L5). Approved use: Not recorded in the local data"
---

# Diethylpropion
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Diethylpropion: Hypervitaminosis
{: .text-alpha }

## One-Sentence Summary

Diethylpropion is a sympathomimetic appetite suppressant (anorectic) originally used to treat obesity.
The TxGNN model predicts it may be effective for **hypervitaminosis**, but there are **0 clinical trials** and **0 publications** supporting this prediction.
The prediction is a model output only and has no credible mechanistic or clinical support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 3) |
| Number of NDAs | 3 (all cancelled; these are ANDA generic applications) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, diethylpropion is a sympathomimetic amine that suppresses appetite through catecholamine release, and it has been used for obesity.

Hypervitaminosis is a toxicity state caused by excess vitamin intake. No credible mechanistic link to an anorectic sympathomimetic has been identified. The very high TxGNN score (0.9999) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, and it should not be read as evidence of efficacy.

Other predictions generated for this drug show the same pattern:

- **Proximal 16p11.2 microdeletion syndrome** (score 0.9999): the only plausible link is indirect. This deletion is a known genetic cause of severe early-onset obesity, so diethylpropion might address the weight-related symptom, but not the underlying syndrome. Safety in patients with neurodevelopmental comorbidities is uncharacterized.
- **Obsolete hypertelorism (disease)** (score 0.9997): a craniofacial structural anomaly, with no plausible pharmacological correction. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.
- **Frontorhiny** (score 0.9996): a rare congenital craniofacial malformation, with no apparent mechanistic relationship.

All four predictions have L5 evidence and a Hold recommendation.

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
| ANDA091680 | Diethylpropion Hydrochloride ER (Chartwell RX, LLC.) | Extended-release tablet | Not listed (status: valid) |
| ANDA200177 | Diethylpropion (Chartwell RX, LLC.) | Tablet | Not listed (status: valid) |
| ANDA201212 | Diethylpropion Hydrochloride (Bryant Ranch Prepack) | Tablet | Not listed (status: valid) |

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (these come from drug-disease relationships in the graph, not from package insert text):
  - Cardiovascular: hypertension, hypertensive disorder, pulmonary hypertension, coronary artery disease, arteriosclerosis disorder, atherosclerosis, sudden cardiac arrest, heart conduction disease, heart valve disease
  - Metabolic and endocrine: type 1 diabetes mellitus (IDDM 1), type 2 diabetes mellitus, diabetes mellitus, diabetic ketoacidosis, hyperthyroidism, Graves disease, thyrotoxicosis
  - Neurological and psychiatric: epilepsy, drug psychosis
  - Substance use: substance abuse/dependence, substance-related disorder
  - Eye: glaucoma
- **Drug Interactions**: The interaction screening returned 100 interacting drugs. The main interactions are listed below.
  - **Major**: tramadol, fluvoxamine, bupropion, methylene blue, lorcaserin
  - **Moderate** (examples): other sympathomimetics and bronchodilators (phenylephrine, pseudoephedrine, epinephrine, salbutamol, formoterol, arformoterol, isometheptene); antidiabetic drugs (metformin, pioglitazone, alogliptin, acarbose, albiglutide); amitriptyline; amifampridine; ethanol

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no clinical trials, no literature, and no credible mechanistic link between an anorectic sympathomimetic and vitamin toxicity. In addition, this drug is marketed in the US with 3 valid licenses, and the knowledge graph flags many cardiovascular and metabolic contraindications.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- A credible biological rationale linking diethylpropion to hypervitaminosis, or a reassessment of whether other predictions (for example, the obesity-related phenotype of 16p11.2 microdeletion syndrome) are more worth pursuing
- Any supporting preclinical or clinical evidence, which is currently absent
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

