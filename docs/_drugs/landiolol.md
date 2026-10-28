---
layout: default
title: Landiolol
parent: Model Prediction Only (L5)
nav_order: 833
evidence_level: L5
indication_count: 6
monitor_inn: "LANDIOLOL"
predicted_indications: ["lingual-facial-buccal dyskinesia", "chronic tic disorder", "psychogenic movement disorders", "extrapyramidal and movement disease", "benign shuddering attacks", "primary orthostatic tremor"]
last_modified_at: 2026-10-14
description: "Landiolol: predicted new indication Lingual-facial-buccal dyskinesia (evidence level L5). Approved use: Supraventricular tachycardia (atrial fibrillation and atrial flutter)…"
---

# Landiolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Landiolol: From Supraventricular Tachycardia to Lingual-Facial-Buccal Dyskinesia
{: .text-alpha }

## One-Sentence Summary

Landiolol is an ultra-short-acting, highly beta-1-selective adrenergic blocker given intravenously, used for supraventricular tachycardia (atrial fibrillation and atrial flutter).
The TxGNN model predicts it may be effective for **lingual-facial-buccal dyskinesia**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction is model-only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Supraventricular tachycardia (atrial fibrillation and atrial flutter), based on pharmacology data; the approved indication text is not listed in the US license record |
| Predicted New Indication | Lingual-facial-buccal dyskinesia |
| TxGNN Prediction Score | 0.9911 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of NDAs | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Landiolol selectively blocks the beta-1 adrenergic receptor (about 250-fold selectivity over beta-2) and has a very short half-life. Currently, detailed mechanism of action data is not available in the compiled data, so no mechanistic validation is possible.

The link to orofacial dyskinesia comes purely from the TxGNN model (deep learning) prediction. Other beta-blockers, such as propranolol, have been used for some drug-induced movement disorders (for example akathisia). However, propranolol is non-selective and enters the brain, whereas landiolol is beta-1 selective, acts mainly in the periphery, and has minimal CNS penetration. There is no evidence that it would affect orofacial dyskinesia, so the prediction is probably a class-level association rather than a true landiolol-specific mechanism.

**Other predicted indications (all L5, all Hold):**

| Rank | Predicted Indication | TxGNN Score | Comment |
|------|------|------|------|
| 2 | Chronic tic disorder | 0.9908 | Tics involve cortico-striatal-thalamo-cortical and dopaminergic circuits; peripheral beta-1 blockade has no established rationale |
| 3 | Psychogenic movement disorders | 0.9905 | Managed mainly with physiotherapy and CBT; an IV-only drug is poorly suited to a chronic condition |
| 4 | Extrapyramidal and movement disease | 0.9904 | Broad category; score likely reflects beta-blocker class association |
| 5 | Benign shuddering attacks | 0.9904 | Rare, self-limiting pediatric condition; unfavorable benefit-risk for an IV beta-blocker |
| 6 | Primary orthostatic tremor | 0.9900 | Usually treated with clonazepam, gabapentin or primidone; beta-blockers are generally ineffective |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA217202 | RAPIBLYK (AOP Orphan Pharmaceuticals GmbH) | Injection, powder, lyophilized, for solution | Not listed in the license record (status: valid) |

## Safety Considerations

- **Drug Interactions**: No drug-drug interactions were identified. The interaction query returned only pharmacological target data: landiolol acts on the beta-1 adrenoceptor (ADRB1) and the beta-2 adrenoceptor (ADRB2), with about 250-fold selectivity for beta-1.
- **Route of administration**: Landiolol is an intravenous drug used in critical care settings, which limits its suitability for chronic movement disorders.

Please refer to the package insert for warnings and contraindications, as these were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score (L5). There are no clinical trials or publications, the mechanism is not validated, and landiolol's beta-1 selectivity, minimal CNS penetration, ultra-short half-life and IV-only use make it a poor fit for chronic movement disorders. The US license record also shows only a cancelled status.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data (for example from DrugBank)
- Preclinical or clinical evidence that beta-1-selective blockade affects orofacial dyskinesia or other movement disorders
- Assessment of route compatibility, since only an IV formulation exists
- Clarification of the current US marketing status of RAPIBLYK
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

