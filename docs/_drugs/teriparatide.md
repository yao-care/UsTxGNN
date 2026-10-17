---
layout: default
title: Teriparatide
parent: Model Prediction Only (L5)
nav_order: 1215
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Teriparatide: predicted new indication Duodenal ulcer (evidence level L5). Approved use: Postmenopausal osteoporosis / osteoporosis"
monitor_inn: "Teriparatide"
predicted_indications: ["duodenal ulcer (disease)", "non-syndromic esophageal malformation", "duodenal obstruction", "duodenogastric reflux", "esophageal disease", "Worth syndrome", "autosomal dominant neovascular inflammatory vitreoretinopathy", "succinyl-CoA:3-ketoacid CoA transferase deficiency", "amenorrhea (disease)"]
---

# Teriparatide
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

# Teriparatide: From Postmenopausal Osteoporosis to Duodenal Ulcer

## One-Sentence Summary

Teriparatide is a parathyroid hormone fragment (PTH 1-34) originally used to treat osteoporosis in patients at high risk of fracture.
The TxGNN model predicts it may be effective for **duodenal ulcer**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so it is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Postmenopausal osteoporosis / osteoporosis (from the knowledge graph; no approved-indication text is listed in the US license records) |
| Predicted New Indication | Duodenal ulcer |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no active listings) |
| Number of NDAs | 6 authorizations (3 NDAs and 3 ANDAs), all cancelled |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Teriparatide is a synthetic peptide that mimics the first 34 amino acids of human parathyroid hormone. Pharmacology data show it binds the PTH1 receptor (and also the PTH2 receptor). Its established role is anabolic: it stimulates bone formation in osteoporosis. A detailed mechanism-of-action record is not available for this report, so the description above rests on the receptor data and its known clinical use.

The data compiled for this report do not show a plausible mechanistic link between PTH receptor signaling in bone and duodenal ulcer healing. The very high TxGNN score (99.86%, model rank 32) reflects network-based computational similarity, not biological or clinical validation. Neither trials nor literature were found to support it, and the similarity between the original and predicted indications has not been assessed. This prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

All six US authorizations are cancelled, and none is currently active.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA211097 | Teriparatide | Injection, solution | Apotex Corp. |
| NDA216490 | Yorvipath | Injection, solution | Ascendis Pharma, Endocrinology, Inc. |
| NDA021318 | Teriparatide | Injection, solution | Prasco Laboratories |
| NDA211939 | Teriparatide | Injection, solution | Alvogen, Inc. |
| ANDA213641 | Teriparatide | Injection | Amphastar Pharmaceuticals, Inc. |
| ANDA208569 | Teriparatide | Injection, solution | Teva Pharmaceuticals USA, Inc. |

## Safety Considerations

Label-based warnings and contraindications were not available for this report; please refer to the package insert.

- **Knowledge-graph contraindication signals** (from drug-disease contraindication links, not label text): hypotensive disorder, hypercalcemia, nephrocalcinosis, phosphorus metabolism disease, bone osteosarcoma, bone Paget disease, juvenile Paget disease, osteomalacia, rickets, urolithiasis, renal osteodystrophy, osteitis fibrosa, and hyperparathyroidism.
- **Drug interactions** (8 records in total, 6 drug-drug and 2 receptor-target records):
  - Moderate: topical calcitriol, topical calcipotriol, digoxin, digitoxin
  - Minor: hydrochlorothiazide, furosemide

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The duodenal ulcer prediction rests only on a model score, with no clinical trials, no literature, and no plausible mechanistic link. All US authorizations are also cancelled, which adds an access barrier.

**To proceed, the following is needed:**
- A mechanistic rationale connecting PTH1R signaling to duodenal ulcer biology, and preclinical evidence to test it
- A targeted literature and trial search specific to teriparatide and duodenal ulcer
- Label-based warnings and contraindications from the FDA package insert, and detailed mechanism-of-action data
- A review of whether other predictions for this drug deserve priority. Among the other predicted indications, **pregnancy-associated osteoporosis** (score 99.55%) has by far the strongest support: about 20 publications, including teriparatide-specific cohort studies, reviews and meta-analyses. It is an extension of the existing osteoporosis use (evidence level L3), though no randomized trial exists and use during pregnancy or lactation is limited. Bone density in functional hypothalamic amenorrhea has indirect support only.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

