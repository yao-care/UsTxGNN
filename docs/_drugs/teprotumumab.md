---
layout: default
title: Teprotumumab
parent: Model Prediction Only (L5)
nav_order: 1210
evidence_level: L5
indication_count: 10
monitor_inn: "TEPROTUMUMAB"
predicted_indications: ["monosomy X", "esophageal varices with bleeding", "esophageal varices without bleeding", "mixed gonadal dysgenesis", "mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies", "Turner syndrome due to structural X chromosome anomalies", "mosaic monosomy X", "sex chromosome disorder of sex development", "varicose disease", "X chromosome number anomaly"]
last_modified_at: 2026-10-14
description: "Teprotumumab: predicted new indication Monosomy X (evidence level L5). Approved use: Endocrine exophthalmos"
---

# Teprotumumab
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

## Teprotumumab: From Endocrine Exophthalmos to Monosomy X
{: .text-alpha }

## One-Sentence Summary

Teprotumumab is an IGF-1R inhibitory monoclonal antibody, originally used to treat endocrine exophthalmos (thyroid eye disease).
The TxGNN model predicts it may be effective for **monosomy X** (Turner syndrome), but **0 clinical trials** and **0 publications** currently support this direction. The prediction is computational only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Endocrine exophthalmos |
| Predicted New Indication | Monosomy X |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| US Market Status | Cancelled only |
| Number of NDAs | 1 (BLA761143, status: cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Teprotumumab is a monoclonal antibody that inhibits the insulin-like growth factor 1 receptor (IGF-1R). Detailed mechanism of action data is not available in the data compiled for this report, so this description relies on its known drug class.

The link to monosomy X (Turner syndrome) is weak. Turner syndrome involves growth impairment and gonadal dysgenesis, and the IGF-1 axis is relevant to growth. However, blocking IGF-1R would be expected to oppose, rather than support, growth. No direct mechanistic link is established.

The high TxGNN score (0.998) most likely reflects computational associations within the knowledge graph. The other top predictions are closely related entities (mosaic monosomy X, Turner syndrome due to structural X chromosome anomalies, X chromosome number anomaly, sex chromosome disorder of sex development, mixed gonadal dysgenesis). These appear to be correlated predictions from a single cluster rather than independent signals. The remaining predictions, such as esophageal varices and varicose disease, also lack any plausible mechanistic rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761143 | TEPEZZA | Injection, powder, lyophilized, for solution | Not listed (status: cancelled; manufacturer: Horizon Therapeutics USA, Inc.) |

---

## Safety Considerations

**Drug Interactions**: The interaction screen found 45 interactions in total. The 20 shown in the data are all **Moderate** severity and involve glucose-lowering agents:
- Insulin human
- Metformin, pioglitazone
- Sulfonylureas and related agents (glimepiride, glipizide, glyburide, chlorpropamide, acetohexamide)
- DPP-4 inhibitors (alogliptin, saxagliptin, linagliptin)
- SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin)
- GLP-1 receptor agonists (albiglutide, dulaglutide, exenatide, semaglutide)
- Acarbose

This pattern suggests a possible effect on blood glucose control, so close glucose monitoring would be needed in patients on antidiabetic therapy.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no clinical trials or literature (Evidence Level L5). No plausible mechanistic link exists, and IGF-1R blockade would be expected to work against growth in Turner syndrome. The US license is also listed as cancelled.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking data gap for safety screening)
- Detailed mechanism of action data
- A credible mechanistic hypothesis connecting IGF-1R inhibition to monosomy X, supported by preclinical evidence
- Clarification of the current US regulatory and marketing status
- Review of whether any of the other predicted indications has a stronger rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

