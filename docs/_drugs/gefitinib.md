---
layout: default
title: Gefitinib
parent: Model Prediction Only (L5)
nav_order: 747
evidence_level: L5
indication_count: 10
---

# Gefitinib
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

# Gefitinib: From EGFR-Mutant Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Gefitinib is an oral EGFR tyrosine kinase inhibitor used for EGFR-mutant non-small cell lung cancer (NSCLC).
The TxGNN model predicts it may be effective for **gingival fibromatosis** with a very high score (99.89%), but there are **0 clinical trials** and **0 publications** supporting this specific link, so it is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | EGFR-mutant non-small cell lung cancer (the supplied license data has no indication text; this comes from the evidence pack's mechanism notes) |
| Predicted New Indication | Gingival fibromatosis |
| TxGNN Prediction Score | 99.89% (model rank 3,463) |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 5 licenses (1 NDA, 4 ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Gefitinib is known to inhibit the EGFR tyrosine kinase, and its efficacy in EGFR-mutant NSCLC is well established.

Gingival fibromatosis is a benign overgrowth of gum connective tissue. One could speculate that EGFR-driven fibroblast proliferation links the two, but **the supplied data does not support this**. No trial, paper, or mechanistic study connects gefitinib to this condition. The high score reflects the model's knowledge-graph patterns, not experimental validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

The supplied license records contain no approved-indication text.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA206995 | IRESSA | Tablet, coated | AstraZeneca Pharmaceuticals LP |
| ANDA211591 | Gefitinib | Tablet, coated | Ingenus Pharmaceuticals, LLC |
| ANDA211591 | Gefitinib | Tablet, coated | Qilu Pharmaceutical Co., Ltd. |
| ANDA212827 | Gefitinib | Tablet, film coated | Natco Pharma USA LLC |
| ANDA208913 | Gefitinib | Tablet, film coated | Teva Pharmaceuticals, Inc. |

All products are oral tablets.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (EGFR tyrosine kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Literature in the pack points to ECG/QT monitoring, respiratory symptoms (interstitial lung disease), and skin reactions; see Safety Considerations |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

The evidence pack has no package-insert warnings, contraindications, or drug-interaction records for gefitinib. The retrieved literature (from other predicted indications) does describe these gefitinib-related safety signals:

- **Interstitial lung disease**: reported with EGFR TKIs such as gefitinib (PMID [22076388](https://pubmed.ncbi.nlm.nih.gov/22076388/)).
- **QT prolongation**: shown in patch-clamp studies (PMID [34474028](https://pubmed.ncbi.nlm.nih.gov/34474028/)) and in a retrospective NSCLC cohort of 122 patients (PMID [37258113](https://pubmed.ncbi.nlm.nih.gov/37258113/)).
- **Skin toxicity**: acneiform eruption, paronychia, and xerosis are common with EGFR inhibitors (PMID [18931563](https://pubmed.ncbi.nlm.nih.gov/18931563/)).

Please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on the model score. There are no trials or publications, and benign gingival overgrowth has no established EGFR-dependent biology. Gefitinib's known toxicities (skin, lung, QT) also raise the bar for use in a non-life-threatening condition.

**To proceed, the following is needed:**
- Mechanistic evidence, for example EGFR pathway activity in gingival fibroblasts
- Preclinical data (cell or animal models) showing gefitinib effect on this condition
- Package insert warnings and contraindications (blocking data gap)
- Detailed mechanism of action data from DrugBank

**Note on other candidates in the pack:** Of the ten predictions, only *lung hilum carcinoma* (rank 5) has a biologically coherent rationale, but it is essentially an existing on-label NSCLC use and rests on a single case report. The rest are L4/L5 with no meaningful gefitinib-specific evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

