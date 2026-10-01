---
layout: default
title: Tamsulosin
parent: Model Prediction Only (L5)
nav_order: 1199
evidence_level: L5
indication_count: 10
---

# Tamsulosin
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

# Tamsulosin: From Lower Urinary Tract Symptoms to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Tamsulosin is an alpha-1A/1D adrenoceptor antagonist used for lower urinary tract symptoms.
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**, but **no clinical trials and no publications** support this prediction. It is a model-only signal with no identified pharmacological rationale.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Lower urinary tract symptoms (taken from the prediction rationale; the US license records list no indication text) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.996% (rank 246) |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (all listed licenses are generic ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Tamsulosin is an alpha-1A/1D adrenoceptor antagonist, and its established use is symptomatic treatment of lower urinary tract symptoms.

**No plausible link was identified between the two conditions.** Ambras syndrome is a rare congenital disorder tied to chromosome 8q22 rearrangements that affect regulation of *TRPS1*. Alpha-1 adrenergic blockade has no established role in this pathway or in hair-growth regulation.

The high score most likely reflects proximity in the knowledge graph to related hair phenotypes, not a pharmacological signal. The other top predictions follow the same pattern. They include hypertrichosis, hair shaft abnormalities, hypotrichosis, alopecia, and Dandy-Walker malformation syndromes, and none has a mechanistic rationale or supporting evidence. Hypotrichosis simplex of the scalp is the phenotypic opposite of hypertrichosis, yet it also ranks high, which suggests the graph signal is not specific.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

The license records do not include approved indication text, so that column is omitted. The first five of 20 listed licenses are shown.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA202433 | Tamsulosin Hydrochloride | Capsule | Cardinal Health 107, LLC |
| ANDA207405 | Tamsulosin Hydrochloride | Capsule | Chartwell RX, LLC |
| ANDA202433 | Tamsulosin Hydrochloride | Capsule | Northwind Health Company, LLC |
| ANDA202433 | Tamsulosin Hydrochloride | Capsule | Aurobindo Pharma Limited |
| ANDA090931 | Tamsulosin Hydrochloride | Capsule | Proficient Rx LP |

The only route of administration listed is oral (capsule).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the graph model score. There are no trials or publications, and no mechanistic link between alpha-1A/1D blockade and Ambras syndrome. The 20 publications retrieved for another predicted indication (periodontal malformation syndrome, rank 3) concern periodontitis in general and do not mention tamsulosin, so they do not raise the evidence level.

**To proceed, the following is needed:**
- Any tamsulosin-specific mechanistic or preclinical evidence for hair-follicle or *TRPS1*-related biology
- Mechanism of action data from DrugBank
- FDA package insert warnings and contraindications, which are currently missing and block safety screening
- Pharmacoepidemiology data on hair outcomes in tamsulosin users, if the hair-related predictions are to be pursued
- Route compatibility and similarity-to-original assessments, which are still pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

