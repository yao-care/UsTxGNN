---
layout: default
title: Silodosin
parent: 僅模型預測 (L5)
nav_order: 1160
evidence_level: L5
indication_count: 6
---

# Silodosin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Silodosin: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Silodosin is a highly selective alpha-1A adrenergic receptor antagonist used to treat benign prostatic hyperplasia (BPH) by relaxing prostatic and bladder-neck smooth muscle. The TxGNN model predicts a possible link to **Ambras type hypertrichosis universalis congenita**, a rare congenital hair-overgrowth syndrome, but this prediction is currently supported by **0 clinical trials** and **0 publications**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign Prostatic Hyperplasia (BPH) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.99% (global rank 418) |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data (DrugBank MOA field) is currently unavailable for this drug. Based on the pharmacological information available in this evidence pack, silodosin is a highly selective alpha-1A adrenergic receptor antagonist, used clinically to relax smooth muscle in the prostate and bladder neck for BPH symptom relief.

There is no known pharmacological or physiological pathway connecting alpha-1A adrenergic antagonism to Ambras type hypertrichosis, a rare genetic disorder typically associated with 8q chromosomal rearrangements affecting hair follicle development. No mechanistic, clinical, or literature evidence in this evidence pack supports a causal or therapeutic relationship between the two conditions.

Given the absence of any supporting trials or publications, and the biological implausibility of the mechanism, this prediction is most consistent with knowledge-graph embedding noise rather than a genuine pharmacological signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Taiwan Market Information

No license records are currently available — silodosin is listed as not marketed (未上市) in Taiwan, with 0 registered licenses in this evidence pack.

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA warning/contraindication data and DDI data were both flagged as data gaps in this evidence pack — TFDA label warnings/contraindications is a **Blocking** gap that prevents any S1 safety pre-assessment.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN similarity score, the predicted indication has no supporting clinical trials, no supporting literature, and no plausible mechanistic link to the drug's known pharmacology. This pattern also holds for the other top-ranked candidates in this evidence pack (hypertrichosis, odontal/periodontal malformation syndrome — literature matched appears to be an entity-mismatch on unrelated periodontitis research, Dandy-Walker malformation, genetic hair shaft abnormality, familial trichomegaly), none of which show credible mechanistic or evidentiary support. This indication should not proceed past S0 without independent validation.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — currently a Blocking data gap
- Confirmed DrugBank MOA record for silodosin
- Preclinical or mechanistic studies specifically linking alpha-1A adrenergic antagonism to hair follicle/hypertrichosis biology
- Re-validation of the TxGNN prediction to rule out knowledge-graph embedding artifacts, given the biological implausibility and complete absence of corroborating evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

