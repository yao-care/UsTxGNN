---
layout: default
title: Difluprednate
parent: Model Prediction Only (L5)
nav_order: 607
evidence_level: L5
indication_count: 10
monitor_inn: "DIFLUPREDNATE"
predicted_indications: ["familial adrenal hypoplasia with absent pituitary luteinizing hormone", "seborrheic keratosis", "PAGOD syndrome", "vulvar inverted follicular keratosis", "adrenocortical insufficiency", "seborrheic dermatitis", "46,XY disorder of sex development", "necrobiosis lipoidica", "nephrotic syndrome", "iris disease"]
last_modified_at: 2026-10-30
description: "Difluprednate: predicted new indication Familial adrenal hypoplasia with absent pituitary luteinizing hormone (evidence level L5). Approved use: Not stated in the US license records compiled for this…"
---

# Difluprednate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Difluprednate: From Ocular Inflammation to Familial Adrenal Hypoplasia with Absent Pituitary Luteinizing Hormone
{: .text-alpha }

## One-Sentence Summary

Difluprednate is a potent corticosteroid, marketed as an ophthalmic emulsion (brand name Durezol) for eye inflammation and pain after surgery and for anterior uveitis.
The TxGNN model predicts it may be effective for **familial adrenal hypoplasia with absent pituitary luteinizing hormone**, but **no clinical trials and no publications** support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US license records compiled for this report. Pharmacology data describe approved use for eye pain and inflammation after ophthalmic surgery and for anterior uveitis. |
| Predicted New Indication | Familial adrenal hypoplasia with absent pituitary luteinizing hormone |
| TxGNN Prediction Score | 0.9996 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 7 of 8) |
| Number of FDA Applications | 8 (valid: 7) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. From pharmacology data, difluprednate is a glucocorticoid receptor (NR3C1) agonist with a reported binding affinity (Ki) of 0.78 nM. It is a prodrug that is converted to an active metabolite after application.

The predicted disease is a congenital genetic disorder (for example involving NR0B1/DAX-1) that causes adrenal and gonadotropin deficiency. Glucocorticoids are relevant to the cortisol deficiency in such conditions, so there is a class-level link. However, difluprednate is a potent topical ophthalmic and dermatologic steroid, not a systemic replacement agent. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. No clinical or literature support was found.

Other predictions in the top 10 follow a similar pattern. Adrenocortical insufficiency, nephrotic syndrome, seborrheic dermatitis and necrobiosis lipoidica have plausible class-level steroid rationales. Seborrheic keratosis, PAGOD syndrome and vulvar inverted follicular keratosis have little biological basis. The only prediction with any supporting item is iris disease (rank 10), which probably overlaps with the existing ocular use.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top-ranked prediction.

For reference, the only publication found among the top 10 predictions relates to rank 10 (iris disease):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21182429](https://pubmed.ncbi.nlm.nih.gov/21182429/) | 2011 | Preclinical (rabbit pharmacokinetics) | J Ocul Pharmacol Ther | Evaluated pharmacokinetic and pharmacodynamic features of difluprednate ophthalmic emulsion using a glucocorticoid receptor-binding bioassay. It supports ocular tissue exposure but is not clinical efficacy evidence. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022212 | DUREZOL (Sandoz Inc) | Emulsion | Not stated in the data (valid) |
| ANDA211776 | Difluprednate (Cipla USA Inc.) | Emulsion | Not stated in the data (valid) |
| ANDA219441 | Difluprednate (Leading Pharma, LLC) | Emulsion | Not stated in the data (valid) |
| ANDA213774 | Difluprednate (Alembic Pharmaceuticals Limited) | Emulsion | Not stated in the data (valid) |
| ANDA218191 | Difluprednate (Upsher-Smith Laboratories, LLC) | Emulsion | Not stated in the data (valid) |

Three more authorizations (Mylan, Amneal and Dr. Reddy's) are also cancelled, for a total of 8.

## Safety Considerations

- **Disease contraindications (from the knowledge graph, not label text)**: ocular hypertension, herpes simplex virus keratitis, ocular tuberculosis, and mycotic (fungal) corneal ulcer.
- **Drug Interactions**: No drug-drug interactions were identified. The only pharmacology entry is its target, the glucocorticoid receptor.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score (L5). There are no clinical trials or publications, and a potent topical ophthalmic steroid is not a suitable replacement therapy for a congenital adrenal and gonadotropin deficiency. The drug is marketed in the US, with all 8 of 8 licenses valid.

**To proceed, the following is needed:**
- FDA package insert warnings, contraindications and approved indications
- Detailed mechanism-of-action data
- Evidence that a systemic or otherwise suitable formulation is feasible for this condition
- Clinical or literature evidence for the predicted disease
- If the team wants to pursue other predictions, prioritize those with plausible class-level rationales (seborrheic dermatitis, adrenocortical insufficiency, nephrotic syndrome), and check the iris disease prediction against current ocular labeling, since it likely overlaps with the existing use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

