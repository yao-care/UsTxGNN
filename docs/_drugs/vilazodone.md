---
layout: default
title: Vilazodone
parent: Model Prediction Only (L5)
nav_order: 1290
evidence_level: L5
indication_count: 7
monitor_inn: "VILAZODONE"
predicted_indications: ["neurotic disorder", "obsessive-compulsive disorder", "agoraphobia", "benign paroxysmal torticollis of infancy", "Keppen-Lubinsky syndrome", "Ohdo syndrome and variants", "schizoid personality disorder"]
last_modified_at: 2026-10-23
description: "Vilazodone: predicted new indication Neurotic disorder (evidence level L5). Approved use: Major depressive disorder"
---

# Vilazodone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Vilazodone: From Major Depressive Disorder to Neurotic Disorder
{: .text-alpha }

## One-Sentence Summary

Vilazodone is a serotonergic antidepressant, with relations recorded in the knowledge graph for unipolar depression, major depressive disorder and anxiety disorder.
The TxGNN model predicts it may be effective for **neurotic disorder**, its top-ranked new indication.
There are currently **0 clinical trials** and **0 publications** that directly study this disease, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major depressive disorder (relation recorded in the knowledge graph; the US licence records compiled for this report contain no indication text) |
| Predicted New Indication | Neurotic disorder |
| TxGNN Prediction Score | 0.9975 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 6) |
| Number of NDAs | at least 6 |
| Number of approvals | At least 6 (1 NDA and 5 ANDAs; the list may be partial) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, vilazodone combines serotonin reuptake inhibition with 5-HT1A partial agonism.

Neurotic disorder is a broad, legacy category that overlaps with anxiety-spectrum conditions. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. No study cited here addresses neurotic disorder directly.

### Other Predicted Indications (for reference)

| Rank | Predicted Disease | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Obsessive-compulsive disorder | 0.9972 | L5 | Only class-level reviews of serotonergic antidepressants; no vilazodone-specific study and no study directly on vilazodone in this disease |
| 3 | Agoraphobia | 0.9968 | L5 | Plausible anxiety-spectrum rationale; no trials or literature |
| 4 | Benign paroxysmal torticollis of infancy | 0.9964 | L5 | No clear mechanistic link; pediatric safety concern |
| 5 | Keppen-Lubinsky syndrome | 0.9954 | L5 | Ultra-rare; likely a network-proximity artifact |
| 6 | Ohdo syndrome and variants | 0.9952 | L5 | No identifiable mechanistic link |
| 7 | Schizoid personality disorder | 0.9951 | L5 | Core features are not clearly serotonergic targets |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for neurotic disorder.

For the second-ranked prediction (obsessive-compulsive disorder), only indirect reviews were found, for example [24766145](https://pubmed.ncbi.nlm.nih.gov/24766145/) (2014, Expert Opin Pharmacother), a review of double-blind studies of serotonergic antidepressants in OCD. They offer class-level support only and do not study vilazodone.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022567 | VIIBRYD (Allergan, Inc.) | Tablet | Not stated in the compiled records |
| ANDA208200 | Vilazodone hydrochloride (Cipla USA Inc.) | Film-coated tablet | Not stated in the compiled records |
| ANDA208212 | Vilazodone Hydrochloride (Teva Pharmaceuticals, Inc.) | Film-coated tablet | Not stated in the compiled records |
| ANDA208202 | Vilazodone Hydrochloride (Alembic Pharmaceuticals Limited) | Film-coated tablet | Not stated in the compiled records |
| ANDA208228 | Vilazodone hydrochloride (Northstar Rx LLC) | Tablet | Not stated in the compiled records |

These are the first 5 of 6 listed records. The total is "at least 6", and the list may be partial.

## Safety Considerations

- **Relations recorded in the knowledge graph as contraindications** (not label text): epilepsy, bipolar disorder, major affective disorder, blood coagulation disease, neuroleptic malignant syndrome, inappropriate ADH syndrome, nephrogenic syndrome of inappropriate antidiuresis, serotonin syndrome.
- **Drug Interactions**: 100 interactions were found. Major-level ones among those listed include:
  - Bupropion
  - Lorcaserin
  - Clarithromycin
  - Diethylpropion
  - Dolasetron
  - Palonosetron
  - Phentermine

  Moderate-level ones include pioglitazone, aprepitant, morphine, acetylsalicylic acid, dexamethasone, chlorpropamide, glimepiride and several insulins. Many of the serotonergic and QT-related combinations call for caution.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for neurotic disorder has a high model score but no supporting clinical trials or publications (L5). The category is broad and largely overlaps with indications already recorded for vilazodone, so the score probably does not reflect a new therapeutic opportunity.

**To proceed, the following is needed:**
- Official package insert warnings and contraindications, which are currently missing and block safety screening
- Mechanism of action data from DrugBank
- A clearer, narrower definition of the target condition (for example, specific anxiety or obsessive-compulsive disorders)
- Disease-specific clinical or literature evidence, such as vilazodone trials in anxiety-spectrum or obsessive-compulsive disorders
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

