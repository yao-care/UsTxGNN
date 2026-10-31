---
layout: default
title: Finasteride
parent: Model Prediction Only (L5)
nav_order: 708
evidence_level: L5
indication_count: 6
monitor_inn: "FINASTERIDE"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial isolated trichomegaly"]
last_modified_at: 2026-10-31
description: "Finasteride: predicted new indication Ambras type hypertrichosis universalis congenita (evidence level L4). Approved use: Benign prostatic hyperplasia"
---

# Finasteride
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

## Finasteride: From Benign Prostatic Hyperplasia to Ambras type hypertrichosis universalis congenita
{: .text-alpha }

## One-Sentence Summary

Finasteride was originally used to treat benign prostatic hyperplasia.
The TxGNN model (deep learning) predicts it may be effective for **Ambras type hypertrichosis universalis congenita**, but this is a model prediction with **0 clinical trials** and only **4 indirect publications** (narrative reviews and a methods paper) behind it. The evidence is weak and does not directly show that finasteride works for this condition.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign prostatic hyperplasia |
| Predicted New Indication | Hypertrichosis (rank 2 of 6 predictions; the top-ranked prediction, Ambras type hypertrichosis universalis congenita, has no evidence at all) |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 10) |
| Number of FDA Applications | at least 10 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, finasteride inhibits type II 5-alpha-reductase and lowers dihydrotestosterone (DHT). That is how it shrinks the prostate in benign prostatic hyperplasia, and it is also why it is used for male pattern hair loss.

The link to hypertrichosis is weak. Hypertrichosis is increased hair growth in non-androgen-dependent areas, so lowering DHT would not be expected to treat it. The retrieved publications discuss hair disorders broadly, including androgenetic alopecia, hirsutism and hypertrichosis. They mention finasteride for male pattern hair loss and laser-assisted hair removal for hypertrichosis and hirsutism, but none shows finasteride working for hypertrichosis. The very high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The other predictions fare no better:
- **Ambras type hypertrichosis universalis congenita** (score 0.9999): a genetic developmental disorder not driven by androgens, with no trials or literature.
- **Malformation syndrome with odontal/periodontal component, Dandy-Walker malformation syndrome, isolated genetic hair shaft abnormality, familial isolated trichomegaly**: no plausible mechanism and no evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12942187](https://pubmed.ncbi.nlm.nih.gov/12942187/) | 2003 | Review | Der Hautarzt | Overview of new hair disease therapies: finasteride for male pattern hair loss and laser-assisted hair removal for hypertrichosis and hirsutism |
| [12223963](https://pubmed.ncbi.nlm.nih.gov/12223963/) | 2002 | Review | Ann Dermatol Venereol | Investigation and treatment of adult hirsutism and hypertrichosis; hypertrichosis is non-androgen-dependent and often iatrogenic or metabolic |
| [10330884](https://pubmed.ncbi.nlm.nih.gov/10330884/) | 1999 | Review | Ther Umsch | Treatment options for androgenetic alopecia and hirsutism; emotional impact of cosmetic hair problems |
| [12444520](https://pubmed.ncbi.nlm.nih.gov/12444520/) | 2002 | Methods paper | Der Hautarzt | TrichoScan digital hair analysis tool; not a drug study |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA078341 | Finasteride (Aurobindo Pharma) | Film-coated tablet | Not listed (valid) |
| NDA020788 | PROPECIA (Organon) | Film-coated tablet | Not listed (valid) |
| ANDA204304 | Finasteride (Proficient Rx) | Film-coated tablet | Not listed (valid) |
| ANDA090121 | Finasteride (Proficient Rx) | Film-coated tablet | Not listed (valid) |
| ANDA090060 | Finasteride (NuCare Pharmaceuticals) | Film-coated tablet | Not listed (valid) |

All 10 licenses compiled for this report are valid; the table shows the first 5.

## Safety Considerations

- **Disease associations from the knowledge graph (not label text)**: liver disease and gallbladder disease are listed as contraindication-related conditions.
- **Drug Interactions**: 100 potential interactions were found in the DDInter database, but none has a severity level assigned. Examples include calcitriol, doxycycline, clotrimazole, famotidine, acetylsalicylic acid, bupropion, omeprazole, metformin, and morphine.

Please refer to the package insert for full warnings and contraindications, which are not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but there are no clinical trials, and the four publications are indirect reviews and a methods paper. Hypertrichosis is not androgen-driven, so finasteride's DHT-lowering action has no clear mechanistic link to it. The drug is marketed in the US, with 10 valid licenses.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Direct clinical or preclinical evidence of finasteride in hypertrichosis
- A reassessment of whether hirsutism, an androgen-dependent condition, would be a more plausible target than hypertrichosis
- Clarification of the US regulatory pathway for this new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

