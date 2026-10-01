---
layout: default
title: Vilazodone
parent: Model Prediction Only (L5)
nav_order: 1290
evidence_level: L5
indication_count: 10
---

# Vilazodone
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

# Vilazodone: From Major Depressive Disorder to Dysthymic Disorder

## One-Sentence Summary

Vilazodone is an antidepressant originally used to treat major depressive disorder.
The TxGNN model predicts it may be effective for **dysthymic disorder (persistent depressive disorder)**,
but there are currently **0 clinical trials** and **0 publications** specific to this indication, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major depressive disorder (the US license records in the dataset carry no indication text; this is taken from the mechanistic notes) |
| Predicted New Indication | Dysthymic disorder |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the listed licenses are generic ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Vilazodone is an SSRI and a 5-HT1A partial agonist. It is approved in the US for major depressive disorder. Detailed mechanism of action data is not available from DrugBank in this dataset. The description above comes from the rationale notes and the retrieved literature.

Dysthymic disorder, now called persistent depressive disorder, is a chronic, lower-grade form of depression. It is biologically adjacent to major depressive disorder, and serotonergic antidepressants are widely used across the depressive spectrum. This is why the model scores the link so highly.

This is a model prediction only. No trial or publication in the dataset tests vilazodone in dysthymic disorder, and the similarity to the original indication has not yet been assessed. The score therefore shows graph-level plausibility, not demonstrated efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

The dataset lists 20 licenses in total. The five main ones are shown below. None of them carries approved-indication text in the dataset.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA208200 | Vilazodone hydrochloride (Cipla USA Inc.) | Film-coated tablet | — |
| ANDA208212 | Vilazodone Hydrochloride (Teva Pharmaceuticals, Inc.) | Film-coated tablet | — |
| ANDA208202 | Vilazodone Hydrochloride (Alembic Pharmaceuticals Limited) | Film-coated tablet | — |
| ANDA208228 | Vilazodone hydrochloride (Northstar Rx LLC) | Tablet | — |
| ANDA208228 | Vilazodone hydrochloride (Apotex Corp.) | Tablet | — |

All listed products are oral formulations.

---

## Safety Considerations

Please refer to the package insert for safety information. The dataset has no warnings, contraindications, or drug interaction records for vilazodone.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score (L5). There are no trials or publications for dysthymic disorder, and the safety data are missing. Among the other predicted indications, neurotic depression and melancholia have indirect literature, but these mostly overlap with the already-approved major depressive disorder. They are better treated as terminology or subtype questions than as distinct repurposing signals.

**To proceed, the following is needed:**
- Safety data: US package insert warnings and contraindications, which currently block the S1 safety screening
- Mechanism of action data from DrugBank to support the mechanistic-link analysis
- A targeted search for vilazodone studies in persistent depressive disorder or dysthymia, including trial registries and publications
- A similarity assessment between dysthymic disorder and major depressive disorder, using diagnostic criteria and clinical endpoints

---

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

