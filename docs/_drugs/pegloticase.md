---
layout: default
title: Pegloticase
parent: 僅模型預測 (L5)
nav_order: 1022
evidence_level: L5
indication_count: 1
---

# Pegloticase
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Pegloticase: From Chronic Refractory Gout to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

> Pegloticase (DrugBank DB09208) is a PEGylated uricase enzyme; publicly known information indicates it is used elsewhere for chronic refractory gout, though this evidence pack contains no documented original indication.
> The TxGNN model predicts it may be effective for **Severe Nonproliferative Diabetic Retinopathy**,
> with a high prediction score (**99.18%**) but currently **no clinical trials and no published literature** supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (`original_indications` empty) |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L5 (model prediction only, no clinical trials or literature) |
| Taiwan Market Status | Not Marketed |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). Publicly, pegloticase is known as a PEGylated recombinant uricase enzyme that converts uric acid to allantoin, and its use elsewhere has focused on lowering serum uric acid in chronic refractory gout — but this specific claim is not confirmed within the data provided here.

No mechanistic, clinical, or literature evidence in this pack links uric acid metabolism to diabetic retinopathy pathology. The TxGNN score reflects a graph-based association only (e.g., shared metabolic or comorbidity nodes in the knowledge graph) and should be treated as a hypothesis, not a validated mechanistic rationale, until independent literature or trial evidence becomes available.

Given the combination of missing MOA data and zero supporting evidence, this prediction currently rests entirely on the model score and requires further validation before any mechanistic narrative can be responsibly written.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Pegloticase has **0 licenses on record and is not currently marketed in Taiwan** (`market_status: 未上市`). No product, dosage form, or approved indication data is available.

---

## Safety Considerations

Please refer to the package insert for safety information. TFDA warnings/contraindications data is currently a **Blocking** data gap (DG001) — this must be resolved before any safety-related decision can be made.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is supported only by a TxGNN model score, with no clinical trials, no literature, no confirmed mechanism of action, and no Taiwan market presence. Evidence is at the lowest tier (L5) and insufficient to justify further evaluation at this time.

**To proceed, the following is needed:**
- TFDA package insert data (warnings/contraindications) — currently blocking (DG001)
- Confirmed mechanism of action from DrugBank or other authoritative source (DG002)
- Targeted literature/clinical trial search for any link between uric acid metabolism and diabetic retinopathy
- Route compatibility assessment — pegloticase is administered by IV infusion; suitability for an ophthalmic indication (severe NPDR) has not been evaluated (`route_compatibility.status: pending`)
- Confirmation of the drug's actual original indication, since it is not documented in this evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

