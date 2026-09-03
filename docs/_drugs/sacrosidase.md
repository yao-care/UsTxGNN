---
layout: default
title: Sacrosidase
parent: 僅模型預測 (L5)
nav_order: 1142
evidence_level: L5
indication_count: 2
---

# Sacrosidase
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

# Sacrosidase: From Unconfirmed Original Indication to Cystinosis

## One-Sentence Summary

> Sacrosidase's original approved indication is not documented in the current evidence pack, and its mechanism of action is also unavailable.
> The TxGNN model predicts a possible link to **Cystinosis**, but **no clinical trials** and **no literature** currently support this direction — the prediction is based purely on the model's statistical output.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no license/indication record in current data |
| Predicted New Indication | Cystinosis |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for sacrosidase is currently unavailable in this evidence pack, and no original indication record exists to compare against. Based on the evidence pack's own mechanistic assessment, sacrosidase is an orally administered sucrase-replacement enzyme that acts locally in the intestinal lumen to hydrolyze sucrose into glucose and fructose; it is not systemically absorbed.

Cystinosis, by contrast, is a systemic lysosomal storage disorder caused by defects in the CTNS gene (cystine transporter), leading to cystine accumulation across tissues. The evidence pack explicitly notes that there is **no shared enzymatic pathway and no lysosomal-related mechanism connecting the two** — the mechanistic rationale for this prediction does not hold up. A second candidate, familial apolipoprotein C-II deficiency (score 99.05%, also L5), shows the same pattern: no overlapping metabolic pathway or drug target with sacrosidase's local intestinal action.

Both predictions therefore appear to be purely data-driven associations from the TxGNN model, without a credible biological bridging hypothesis. This should be treated as a hypothesis-generating signal only, not as mechanistically supported repurposing evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Sacrosidase currently has no marketing authorization on record in this evidence pack (market status: not marketed; 0 licenses). No product/dosage form information is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (cystinosis) has zero clinical trial or literature support, an explicitly implausible mechanistic link per the evidence pack's own analysis, and the drug lacks basic regulatory and safety documentation (MOA, label warnings, contraindications are all missing). This falls well below the threshold for any active development action.

**To proceed, the following is needed:**
- Confirmed original approved indication and regulatory license history for sacrosidase
- Mechanism of action (MOA) data from DrugBank or primary literature
- Local regulatory label (warnings/contraindications) — currently a blocking data gap for any safety assessment
- Independent mechanistic or preclinical rationale connecting sucrase enzyme replacement to lysosomal cystine transport, if such a rationale exists
- Re-evaluation only if new clinical or literature evidence emerges for either candidate indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

