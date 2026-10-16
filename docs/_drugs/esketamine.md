---
layout: default
title: Esketamine
parent: Model Prediction Only (L5)
nav_order: 670
evidence_level: L5
indication_count: 2
monitor_inn: "ESKETAMINE"
predicted_indications: ["agoraphobia", "benign paroxysmal torticollis of infancy"]
last_modified_at: 2026-10-14
description: "Esketamine: predicted new indication Agoraphobia (evidence level L5). Approved use: Anxiety disorder, neurotic disorder, dysthymic disorder"
---

# Esketamine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Esketamine: From Anxiety Disorder to Agoraphobia

## One-Sentence Summary

Esketamine was originally associated with anxiety-spectrum conditions (anxiety disorder, neurotic disorder, dysthymic disorder) in the knowledge graph used for this analysis.
The TxGNN model predicts it may be effective for **agoraphobia**,
but **no clinical trials and no publications** were found to support this direction, so it is a model-derived signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anxiety disorder, neurotic disorder, dysthymic disorder (from the knowledge graph; no approved-indication text is available for the US license) |
| Predicted New Indication | Agoraphobia |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| US Market Status | Cancelled only |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for esketamine is not available in the data compiled for this report. From general pharmacology, esketamine is an NMDA receptor antagonist that modulates glutamatergic signaling. This background knowledge could not be confirmed from the supplied data.

Agoraphobia is usually classed with the anxiety disorders and often occurs together with panic disorder. Because esketamine's listed original indications (anxiety disorder, neurotic disorder) are close neighbors of agoraphobia, the prediction is biologically plausible on grounds of disease proximity.

This is an inference, not evidence. The high model score (0.996) reflects a pattern in the knowledge graph, not any demonstrated clinical benefit.

**Second predicted indication (for reference):** The model also predicted *benign paroxysmal torticollis of infancy* (score 99.49%). This is a rare, self-limiting pediatric disorder linked to channelopathy (often CACNA1A variants) and related to migraine. It has no evident connection to esketamine's glutamatergic action or its psychiatric indications, and it is likely a knowledge-graph artifact. It is rated L5 with a Hold recommendation and is not evaluated further here.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA211243 (cancelled) | Spravato (Janssen Pharmaceuticals Inc.) | Solution | Not available |

## Safety Considerations

- **Knowledge-graph contraindications** (from drug-disease relationships, not label text): vascular disease; arteriovenous hemangioma/malformation.
- **Drug Interactions**: 70 interactions were identified. Examples of **Major** interactions: diethylpropion, phentermine, fenfluramine, mazindol, caffeine. Examples of **Moderate** interactions: morphine (including liposomal), opium, loperamide, diphenoxylate, difenoxin, dronabinol, nabilone, metoclopramide, scopolamine, and several nasal corticosteroids/decongestants (beclomethasone, budesonide, triamcinolone, dexamethasone, ephedrine).

Please refer to the package insert for warnings and contraindications, as label-level data was not available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no registered trials or publications. The US license is cancelled, and label safety data and mechanism data are missing. The knowledge-graph contraindication with vascular disease and the many major interactions with stimulant-type drugs also call for caution.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Confirmed mechanism-of-action data (e.g., from DrugBank)
- A literature and trial search specific to esketamine in agoraphobia and panic-related disorders
- Clarification of the cancelled US license status and the approved indication
- Assessment of route compatibility, which is still pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

