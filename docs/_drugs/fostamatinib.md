---
layout: default
title: Fostamatinib
parent: 僅模型預測 (L5)
nav_order: 740
evidence_level: L5
indication_count: 2
---

# Fostamatinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Fostamatinib: From Chronic Immune Thrombocytopenia (ITP) to Autosomal Thrombocytopenia with Normal Platelets

## One-Sentence Summary

Fostamatinib is a Syk (spleen tyrosine kinase) inhibitor approved for chronic immune thrombocytopenia (ITP), where it blocks FcγR-mediated destruction of antibody-coated platelets.
The TxGNN model predicts it may be effective for **Autosomal Thrombocytopenia with Normal Platelets**, a hereditary, non-immune platelet disorder,
but this prediction is currently supported by **no clinical trials** and **no published literature** — the connection appears to be a knowledge-graph artifact based on shared "thrombocytopenia" terminology rather than a validated mechanistic link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Immune Thrombocytopenia (ITP) |
| Predicted New Indication | Autosomal Thrombocytopenia with Normal Platelets |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Fostamatinib is a Syk inhibitor. Its approved mechanism in chronic ITP is to block FcγR signaling in macrophages, preventing the phagocytic destruction of platelets that have been coated with autoantibodies — an **immune-mediated** mechanism.

Autosomal thrombocytopenia with normal platelets is a hereditary condition typically caused by genetic mutations affecting platelet production or function, not by antibody-mediated platelet clearance. There is no established biological pathway linking Syk inhibition to correction of an inherited platelet-production defect.

Given this mismatch, the high TxGNN score most likely reflects a surface-level semantic association (both conditions contain "thrombocytopenia") rather than a genuine shared mechanism. This prediction should be treated as a hypothesis-generation signal only, not as mechanistically validated.

*Note: A second, lower-ranked prediction (non-syndromic esophageal malformation, score 99.05%) was also generated but shows no plausible biological link to Syk inhibition — Syk is expressed almost exclusively in hematopoietic/immune cells and has no known role in esophageal embryogenesis. This candidate is not pursued further.*

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trial or literature support (L5, evidence-only from the model), and the proposed mechanistic link is biologically implausible — ITP's immune-mediated pathway does not map onto a hereditary, non-immune platelet disorder. In addition, a Blocking data gap (missing TFDA label/warnings) prevents even an initial safety assessment.

**To proceed, the following is needed:**
- TFDA/FDA label data — key warnings and contraindications (currently unavailable, Blocking gap)
- Confirmed detailed mechanism of action data beyond the general Syk-inhibitor class description
- Preclinical or mechanistic studies specifically testing Syk inhibition in hereditary thrombocytopenia models
- Drug interaction (DDI) data (current query returned no results)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

