---
layout: default
title: Levodopa
parent: Model Prediction Only (L5)
nav_order: 854
evidence_level: L5
indication_count: 1
monitor_inn: "LEVODOPA"
predicted_indications: ["Rasmussen subacute encephalitis"]
last_modified_at: 2026-10-14
description: "Levodopa: predicted new indication Rasmussen subacute encephalitis (evidence level L5). Approved use: Parkinson disease and related parkinsonian syndromes"
---

# Levodopa
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Levodopa: From Parkinson Disease to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Levodopa is a dopamine precursor, originally used to treat Parkinson disease and related parkinsonian syndromes.
The TxGNN model predicts it may be effective for **Rasmussen subacute encephalitis**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction. The prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson disease and related parkinsonian syndromes |
| Predicted New Indication | Rasmussen subacute encephalitis |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (all listed authorizations are cancelled) |
| Number of NDAs | 12 (listed authorizations, including NDAs and ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, levodopa is a dopamine precursor that acts on dopaminergic signaling in the nigrostriatal pathway. Its efficacy in Parkinson disease and related parkinsonian syndromes is established.

Rasmussen encephalitis is a rare, chronic, unilateral inflammatory brain disease. It is thought to be driven by T-cell-mediated (cytotoxic CD8+) neuroinflammation with astrocyte and neuronal loss. It presents with intractable focal seizures, progressive hemiparesis and cognitive decline. **No direct mechanistic link between the two has been established.**

Possible indirect overlap is limited to dopaminergic modulation of neuroinflammation, or to the treatment of secondary movement abnormalities such as hemiparkinsonism or dystonia. This is speculative and unsupported by data. The high score (0.99) is likely driven by network proximity to the parkinsonism-related original indications (for example, hemiparkinsonism-hemiatrophy syndrome). It should not be read as clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

The data compiled for this report list 12 authorizations, all with cancelled status and no approved indication text. The main ones are shown below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA209184 | Inbrija | Capsule | Not stated |
| NDA203312 | RYTARY | Capsule, extended release | Not stated |
| ANDA077828 | Carbidopa and Levodopa | Tablet, extended release | Not stated |
| ANDA078690 | Carbidopa and Levodopa | Tablet, orally disintegrating | Not stated |
| ANDA214092 | Carbidopa and Levodopa | Tablet | Not stated |

## Safety Considerations

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for label safety information.

- **Disease-level contraindication signals (knowledge graph, not label text)**: The knowledge graph links levodopa to contraindications in several categories:
  - Cardiovascular: myocardial infarction, coronary thrombosis, sudden cardiac arrest, heart conduction disease, orthostatic hypotension, postural orthostatic tachycardia syndrome, multiple system atrophy
  - Psychiatric: psychotic disorder, schizophreniform disorder, schizoaffective disorder, mental disorder, anxiety disorder, neurotic disorder, dysthymic disorder
  - Glaucoma: open-angle and angle-closure glaucoma
  - Gastrointestinal and hepatic: peptic ulcer disease, gastric ulcer, liver disease, gallbladder disease, diarrheal disease
  - Other: epilepsy, drug-induced dyskinesia, kidney disease, diabetes mellitus, diabetic ketoacidosis, melanoma, hemoglobinopathy

  Epilepsy is particularly relevant here, because seizures are a core feature of Rasmussen encephalitis.
- **Drug Interactions** (100 interactions found; examples from the first 20 records returned):
  - Moderate: epinephrine, ephedrine, bupropion, metronidazole, pyridoxine, iron, metoclopramide, and anticholinergics (atropine, hyoscyamine, methscopolamine, glycopyrronium, dicyclomine, clidinium, mepenzolate)
  - Minor: antacids (aluminum hydroxide, calcium carbonate, magaldrate, magnesium carbonate, magnesium hydroxide, magnesium oxide)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score (L5). There are no registered clinical trials or publications, no established mechanistic link, and no mechanism-of-action data. Levodopa also carries a knowledge-graph contraindication signal for epilepsy, the main manifestation of Rasmussen encephalitis. In addition, all 12 listed US authorizations are cancelled.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data for levodopa
- A literature and trial search on dopaminergic therapy in Rasmussen encephalitis, and on neuroinflammation more broadly
- Preclinical or mechanistic studies supporting a link to T-cell-mediated neuroinflammation
- Route and formulation compatibility assessment for the new indication
- Clarification of the current US market and regulatory status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

