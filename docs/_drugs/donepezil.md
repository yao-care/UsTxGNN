---
layout: default
title: Donepezil
parent: Model Prediction Only (L5)
nav_order: 621
evidence_level: L5
indication_count: 8
---

# Donepezil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Donepezil: From Alzheimer's Disease to Psychogenic Movement Disorders

## One-Sentence Summary

Donepezil is a reversible acetylcholinesterase inhibitor, widely used to treat Alzheimer's-type dementia.
The TxGNN model predicts it may be effective for **psychogenic movement disorders**, but the prediction currently has **0 clinical trials** and **0 publications** behind it. It is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Alzheimer's disease (from the literature in the Evidence Pack; the US label text was not provided) |
| Predicted New Indication | Psychogenic movement disorders |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 licenses (all ANDA generics) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for donepezil is not available in the source record. Based on known information, donepezil is a reversible acetylcholinesterase inhibitor that raises cholinergic tone. Its efficacy in Alzheimer's disease is established, but no mechanistic rationale is documented for functional or psychogenic movement disorders.

The link between the original and new indication is weak. Psychogenic (functional) movement disorders are not primarily driven by a cholinergic deficit. Any benefit would therefore be speculative and unsupported by data. The high TxGNN score (99.23%) reflects a network-level association in the knowledge graph, not clinical validation.

Two related predictions from the same run have more support:
- **Chronic tic disorder** (rank 2, evidence level L3): a small pediatric open-label study, a case report, and mouse studies support a cholinergic-modulation hypothesis.
- **Tardive dyskinesia**: the evidence is indirect and mixed, and it includes reports of donepezil-induced movement adverse effects.

If the goal is to advance a candidate, chronic tic disorder is the better research question than psychogenic movement disorders.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA203034 | Donepezil (Camber Pharmaceuticals) | Tablet | Not listed in source data |
| ANDA203907 | Donepezil Hydrochloride (Golden State Medical Supply) | Film-coated tablet | Not listed in source data |
| ANDA202782 | Donepezil Hydrochloride (Lupin Pharmaceuticals) | Tablet | Not listed in source data |
| ANDA203656 | Donepezil Hydrochloride (Unichem Pharmaceuticals) | Film-coated tablet | Not listed in source data |

Available oral forms include tablets, film-coated tablets, and orally disintegrating tablets. ANDA203907 appeared twice in the source data and is shown once.

## Safety Considerations

- **Movement-related adverse effects**: A 2025 systematic review (PMID 40224553) examined movement disorders associated with acetylcholinesterase inhibitors, including donepezil. Cholinergic excess can worsen parkinsonism and tremor. This is directly relevant to any movement-disorder use.

Please refer to the package insert for warnings, contraindications, and drug interaction information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no trials or publications. There is also no documented mechanistic rationale, and known movement-related adverse effects of cholinesterase inhibitors argue for caution.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- A literature search specific to psychogenic or functional movement disorders
- Consideration of prioritizing chronic tic disorder (rank 2) for further evaluation

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

