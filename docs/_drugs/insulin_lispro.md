---
layout: default
title: Insulin Lispro
parent: 僅模型預測 (L5)
nav_order: 802
evidence_level: L5
indication_count: 9
---

# Insulin Lispro
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Insulin Lispro: From Diabetes Mellitus to Autoimmune Oophoritis

## One-Sentence Summary

Insulin lispro is a rapid-acting insulin analog used to treat diabetes mellitus. The TxGNN model predicts it may be relevant to **autoimmune oophoritis**, but this ranking is based on model score alone — **no clinical trials and no literature** currently support this specific pairing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetes mellitus (well-established use for insulin lispro; not sourced from this evidence pack, as no Taiwan license record exists) |
| Predicted New Indication | Autoimmune oophoritis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for insulin lispro in this evidence pack (flagged as a High-severity data gap). Based on general pharmacological knowledge, insulin lispro acts as an insulin receptor agonist, promoting glucose uptake and regulating metabolism — a mechanism with no established direct link to ovarian autoimmune processes.

The relationship between diabetes mellitus and autoimmune oophoritis appears to be one of **comorbidity, not shared treatment mechanism**: autoimmune oophoritis can co-occur with other autoimmune endocrine diseases, including type 1 diabetes, as part of polyglandular autoimmune syndromes. This means patients with autoimmune oophoritis may separately require insulin for a co-existing diabetes diagnosis — it does not imply insulin lispro treats the oophoritis itself.

Because the TxGNN score reflects a knowledge-graph association rather than a validated causal or therapeutic pathway, and because no clinical trials or literature exist for this specific drug-disease pair, this candidate should be interpreted as a hypothesis-generating signal only, not a therapeutic lead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L5 (model prediction only) with no clinical trials or literature support, and the proposed mechanistic link is an indirect disease comorbidity rather than a plausible treatment pathway. Combined with missing TFDA label/safety data (a blocking gap), this candidate cannot proceed to safety review.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001, blocking — required before any S1 safety screening)
- Insulin lispro mechanism of action data from DrugBank (DG002)
- A mechanistic or preclinical study directly linking insulin signaling to ovarian autoimmune pathology, rather than relying on diabetes comorbidity as a proxy
- Note: of the 9 candidates evaluated for this drug, only "pancreatic agenesis" (rank 7) returned literature, and that literature was a general diabetes-insulin review rather than disease-specific evidence; three lipodystrophy-related candidates were flagged as likely reflecting insulin's known *adverse* association with lipoatrophy rather than a therapeutic signal, and should not be pursued as indications.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

