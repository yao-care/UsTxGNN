---
layout: default
title: Phenazopyridine
parent: 僅模型預測 (L5)
nav_order: 1036
evidence_level: L5
indication_count: 1
---

# Phenazopyridine
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

# Phenazopyridine: From Unknown Original Indication to Bronchitis

## One-Sentence Summary

> Phenazopyridine's original indication data is currently unavailable (Data Gap), though it is known as a urinary tract analgesic azo dye compound.
> The TxGNN model predicts it may be effective for **Bronchitis**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-only signal with no corroborating evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (Data Gap) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L5 |
| US Market Status | 未上市 (Not marketed in Taiwan) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, phenazopyridine is an azo dye compound that, after renal excretion, produces a local analgesic effect on the urinary tract mucosa. Its original approved indication is not recorded in this evidence pack, which limits our ability to fully assess the reasonableness of this new prediction.

There is no known pharmacological pathway connecting phenazopyridine's urinary tract mucosal analgesic action to respiratory tract inflammation or bronchitis. No receptor-binding, anti-inflammatory, or airway-related pharmacology data support this link. The high TxGNN score (99.23%) reflects knowledge-graph embedding similarity only, not mechanistic or clinical evidence — the model has ranked this candidate at position 16,929, and the rationale explicitly notes the absence of supporting pharmacological rationale.

Given the complete absence of clinical trials, literature, or mechanistic support, this prediction should be treated as an exploratory signal only, requiring substantial further validation before any clinical consideration.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## US Market Information

Phenazopyridine is not currently marketed in Taiwan (0 licenses on record). No product authorization data is available for this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has no clinical trial or literature evidence, no confirmed original indication, and no verified mechanism of action — evidence level is L5 (model prediction only), which is insufficient to proceed to safety or clinical evaluation.

**To proceed, the following is needed:**
- TFDA package insert warnings/contraindications (currently blocking, per DG001)
- Confirmed mechanism of action data via DrugBank API query (per DG002)
- Confirmed original approved indication(s) for phenazopyridine
- Independent literature or preclinical search specifically evaluating phenazopyridine in respiratory/bronchial conditions, to determine whether any biological plausibility exists beyond the knowledge-graph signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

