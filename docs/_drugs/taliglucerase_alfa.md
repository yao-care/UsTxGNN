---
layout: default
title: Taliglucerase Alfa
parent: Model Prediction Only (L5)
nav_order: 1196
evidence_level: L5
indication_count: 5
monitor_inn: "TALIGLUCERASE ALFA"
predicted_indications: ["Hurler syndrome", "Scheie syndrome", "benign neoplasm of adrenal gland", "autosomal ichthyosis syndrome with fatal disease course", "cholesteryl ester storage disease"]
last_modified_at: 2026-10-28
description: "Taliglucerase Alfa: predicted new indication Hurler syndrome (evidence level L5). Approved use: Gaucher disease"
---

# Taliglucerase Alfa
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Taliglucerase Alfa: From Gaucher Disease to Hurler Syndrome
{: .text-alpha }

## One-Sentence Summary

Taliglucerase alfa is a recombinant plant-cell-expressed enzyme replacement therapy, originally used to treat Gaucher disease.
The TxGNN model predicts it may be effective for **Hurler syndrome**, but **no clinical trials and no publications** currently support this direction. The prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gaucher disease |
| Predicted New Indication | Hurler syndrome |
| TxGNN Prediction Score | 0.9952 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of NDAs | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, taliglucerase alfa is a recombinant glucocerebrosidase (beta-glucosidase) enzyme replacement therapy. Its efficacy in Gaucher disease comes from replacing the deficient enzyme that breaks down glucosylceramide.

Hurler syndrome (MPS I) is caused by a different enzyme deficiency: alpha-L-iduronidase. This leads to accumulation of glycosaminoglycans. Both conditions are lysosomal storage disorders treated by enzyme replacement, which likely explains the high TxGNN score.

The mechanistic support is weak, however. Glucocerebrosidase does not act on dermatan sulfate or heparan sulfate, so there is no direct enzymatic rationale. The link is limited to similarity at the disease-class level. An approved alpha-L-iduronidase therapy (laronidase) already exists for this condition.

**Other predictions in the model output (all L5, all Hold):**

| Rank | Predicted Indication | TxGNN Score | Assessment |
|------|------|------|------|
| 2 | Scheie syndrome | 0.9929 | Attenuated form of MPS I. Same reasoning and same limits as Hurler syndrome. |
| 3 | Benign neoplasm of adrenal gland | 0.9928 | The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Adrenal adenomas are reported in Gaucher patients, but this reflects co-occurrence, not a therapeutic target. |
| 4 | Autosomal ichthyosis syndrome with fatal disease course | 0.9924 | Speculative link through skin ceramide metabolism. The disease term is ambiguous, and systemic enzyme is unlikely to reach the epidermal barrier. |
| 5 | Cholesteryl ester storage disease | 0.9912 | Shared lysosomal pathology and liver/spleen involvement. Glucocerebrosidase does not act on cholesteryl esters, and sebelipase alfa is already approved. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA022458 (cancelled) | ELELYSO | Injection, powder, lyophilized, for solution | Not listed in the data compiled for this report |

The only US authorization is Pfizer's ELELYSO, and it has a cancelled status.

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug interaction data were available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN score, with no clinical trials or literature (Evidence Level L5). Glucocerebrosidase has no enzymatic activity against the substrates that accumulate in Hurler syndrome, and an approved targeted therapy (laronidase) already exists. The only US license is also cancelled.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data for taliglucerase alfa
- Preclinical evidence (for example, in vitro or animal studies) showing any activity against the glycosaminoglycan pathology of MPS I
- A comparison against laronidase to show a plausible advantage
- Clarification of the current US regulatory and supply status of the product
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

