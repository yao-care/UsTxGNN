---
layout: default
title: Teriparatide
parent: Model Prediction Only (L5)
nav_order: 1215
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
monitor_inn: "Teriparatide"
predicted_indications: ["duodenal ulcer (disease)", "non-syndromic esophageal malformation", "duodenal obstruction", "duodenogastric reflux", "esophageal disease", "Worth syndrome", "autosomal dominant neovascular inflammatory vitreoretinopathy", "succinyl-CoA:3-ketoacid CoA transferase deficiency", "amenorrhea (disease)"]
description: "Teriparatide: predicted new indication Duodenal ulcer (disease) (evidence level L5). Approved use: Not recorded in the local data"
---

# Teriparatide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Teriparatide: Duodenal ulcer (disease)
{: .text-alpha }

## One-Sentence Summary

Teriparatide is a parathyroid hormone fragment (PTH 1-34) originally used to treat osteoporosis in patients at high risk of fracture.
The TxGNN model predicts it may be effective for **duodenal ulcer**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so it is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Duodenal ulcer (disease) |
| TxGNN Prediction Score | 0.9986 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 6 of 6) |
| Number of NDAs | 6 (valid: 6) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Teriparatide is a synthetic peptide that mimics the first 34 amino acids of human parathyroid hormone. Pharmacology data show it binds the PTH1 receptor (and also the PTH2 receptor). Its established role is anabolic: it stimulates bone formation in osteoporosis. A detailed mechanism-of-action record is not available for this report, so the description above rests on the receptor data and its known clinical use.

The data compiled for this report do not show a plausible mechanistic link between PTH receptor signaling in bone and duodenal ulcer healing. The very high TxGNN score (0.9986, model rank 32) reflects network-based computational similarity, not biological or clinical validation. Neither trials nor literature were found to support it, and the similarity between the original and predicted indications has not been assessed. This prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

All six US authorizations are currently valid, and the drug is marketed.

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
The duodenal ulcer prediction rests only on a model score from the TxGNN model (deep learning), with no clinical trials, no literature, and no plausible mechanistic link. The drug is marketed in the US, with all six authorizations valid.

**To proceed, the following is needed:**
- A mechanistic rationale connecting PTH1R signaling to duodenal ulcer biology, and preclinical evidence to test it
- A targeted literature and trial search specific to teriparatide and duodenal ulcer
- Label-based warnings and contraindications from the FDA package insert, and detailed mechanism-of-action data
- A review of whether other predictions for this drug deserve priority. Bone density in functional hypothalamic amenorrhea has indirect support only.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

