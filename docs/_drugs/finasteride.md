---
layout: default
title: Finasteride
parent: Moderate Evidence (L3-L4)
nav_order: 708
evidence_level: L4
indication_count: 6
monitor_inn: "FINASTERIDE"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial isolated trichomegaly"]
---

# Finasteride
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **6** 
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

# Finasteride: From Benign Prostatic Hyperplasia to Hypertrichosis

## One-Sentence Summary

Finasteride was originally used to treat benign prostatic hyperplasia.
The TxGNN model predicts it may be effective for **Hypertrichosis**, but this is a graph-based prediction with **0 clinical trials** and only **4 indirect publications** (narrative reviews and a methods paper) behind it. The evidence is weak and does not directly show that finasteride works for this condition.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign prostatic hyperplasia |
| Predicted New Indication | Hypertrichosis (rank 2 of 6 predictions; the top-ranked prediction, Ambras type hypertrichosis universalis congenita, has no evidence at all) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 10 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, finasteride inhibits type II 5-alpha-reductase and lowers dihydrotestosterone (DHT). That is how it shrinks the prostate in benign prostatic hyperplasia, and it is also why it is used for male pattern hair loss.

The link to hypertrichosis is weak. Hypertrichosis is increased hair growth in non-androgen-dependent areas, so lowering DHT would not be expected to treat it. The retrieved publications discuss hair disorders broadly, including androgenetic alopecia, hirsutism and hypertrichosis. They mention finasteride for male pattern hair loss and laser-assisted hair removal for hypertrichosis and hirsutism, but none shows finasteride working for hypertrichosis. The very high TxGNN score most likely reflects shared hair-related associations in the knowledge graph rather than a real mechanistic connection.

The other predictions fare no better:
- **Ambras type hypertrichosis universalis congenita** (score 99.99%): a genetic developmental disorder not driven by androgens, with no trials or literature.
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
| ANDA078341 | Finasteride (Aurobindo Pharma) | Film-coated tablet | Not listed (cancelled) |
| NDA020788 | PROPECIA (Organon) | Film-coated tablet | Not listed (cancelled) |
| ANDA204304 | Finasteride (Proficient Rx) | Film-coated tablet | Not listed (cancelled) |
| ANDA090121 | Finasteride (Proficient Rx) | Film-coated tablet | Not listed (cancelled) |
| ANDA090060 | Finasteride (NuCare Pharmaceuticals) | Film-coated tablet | Not listed (cancelled) |

All 10 licenses compiled for this report are cancelled; the table shows the first 5.

## Safety Considerations

- **Disease associations from the knowledge graph (not label text)**: liver disease and gallbladder disease are listed as contraindication-related conditions.
- **Drug Interactions**: 100 potential interactions were found in the DDInter database, but none has a severity level assigned. Examples include calcitriol, doxycycline, clotrimazole, famotidine, acetylsalicylic acid, bupropion, omeprazole, metformin, and morphine.

Please refer to the package insert for full warnings and contraindications, which are not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but there are no clinical trials, and the four publications are indirect reviews and a methods paper. Hypertrichosis is not androgen-driven, so finasteride's DHT-lowering action has no clear mechanistic link to it. All US licenses are also cancelled.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Direct clinical or preclinical evidence of finasteride in hypertrichosis
- A reassessment of whether hirsutism, an androgen-dependent condition, would be a more plausible target than hypertrichosis
- Clarification of the US regulatory pathway, since no valid licenses remain
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

