---
layout: default
title: Taliglucerase Alfa
parent: 僅模型預測 (L5)
nav_order: 1196
evidence_level: L5
indication_count: 5
---

# Taliglucerase Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Taliglucerase Alfa: From Gaucher Disease to Hurler Syndrome

## One-Sentence Summary

Taliglucerase alfa is a recombinant human glucocerebrosidase (GCase) enzyme replacement therapy, developed to treat Gaucher disease by supplementing the enzyme patients lack due to GBA gene deficiency. The TxGNN model's top prediction suggests possible effectiveness for **Hurler Syndrome** (MPS I), but this is currently supported by **0 clinical trials** and **0 publications**, and the underlying enzyme mechanism does not match the target disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gaucher disease (inferred from enzyme mechanism described in evidence pack; no formal license record available — drug not marketed in the US) |
| Predicted New Indication | Hurler Syndrome (MPS I) |
| TxGNN Prediction Score | 99.52% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is officially flagged as a data gap (DG002) in this evidence pack. However, the repurposing rationale confirms taliglucerase alfa is a recombinant glucocerebrosidase (GCase) used to supplement the enzyme deficient in Gaucher disease patients (GBA gene defect).

Hurler syndrome, in contrast, is caused by deficiency of **alpha-L-iduronidase (IDUA)**, an entirely different lysosomal enzyme with distinct substrate specificity. While both Gaucher disease and Hurler syndrome fall under the broad umbrella of lysosomal storage disorders, enzyme replacement therapies are substrate-specific — GCase cannot compensate for IDUA deficiency, and vice versa.

This strongly suggests the TxGNN prediction reflects a **disease-category clustering artifact** (both diseases embedding near "lysosomal storage disease" in the knowledge graph) rather than a biologically grounded mechanistic link. The same limitation applies to the other four candidates in this evidence pack (Scheie syndrome, benign adrenal adenoma, autosomal ichthyosis, and cholesteryl ester storage disease), none of which share a plausible enzymatic overlap with GCase — for cholesteryl ester storage disease in particular, an approved enzyme-specific therapy (sebelipase alfa, targeting LIPA) already exists and is not this drug. Given this pattern across all five ranked predictions, the evidence pack itself concludes there is no credible mechanistic basis to support repurposing at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Taliglucerase alfa currently has **no marketing authorization on record** in this evidence pack (`market_status: 未上市`, `total_licenses: 0`, no license entries). No NDA table can be populated at this time.

---

## Safety Considerations

Please refer to the package insert for safety information. Note that TFDA/FDA label warnings and contraindications (DG001) are flagged as a **Blocking** data gap in this evidence pack, meaning a formal safety pre-screen (S1) cannot proceed until this data is obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All five TxGNN-predicted indications (including the top-ranked Hurler syndrome) are supported only by model score with zero clinical trials or literature (Evidence Level L5), and mechanistic review indicates a substrate/enzyme-specificity mismatch that undermines biological plausibility. A blocking data gap in safety labeling (DG001) also prevents any formal safety evaluation at this time.

**To proceed, the following is needed:**
- TFDA/FDA package insert data (warnings, contraindications) — blocking gap DG001
- Confirmed mechanism of action detail from DrugBank — gap DG002
- Independent preclinical or mechanistic evidence specifically linking GCase activity to MPS I (Hurler/Scheie) pathophysiology, given the current enzyme-mismatch concern
- Re-evaluation of whether the TxGNN signal reflects true pharmacology or disease-category embedding proximity before allocating further review resources
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

