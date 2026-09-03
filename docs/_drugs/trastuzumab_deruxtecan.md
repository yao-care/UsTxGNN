---
layout: default
title: Trastuzumab Deruxtecan
parent: 僅模型預測 (L5)
nav_order: 1251
evidence_level: L5
indication_count: 1
---

# Trastuzumab Deruxtecan
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

# Trastuzumab Deruxtecan: From Undocumented Original Indication to Drug-Induced Osteoporosis

## One-Sentence Summary

> The original approved indication for trastuzumab deruxtecan is not documented in the current evidence pack.
> The TxGNN model predicts a possible association with **Drug-Induced Osteoporosis**,
> but this signal is currently supported by **0 clinical trials** and **0 publications** — it is a pure computational prediction with no corroborating real-world evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in current dataset |
| Predicted New Indication | Drug-Induced Osteoporosis |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on the information present in the evidence pack, trastuzumab deruxtecan is identified as a HER2-targeted antibody-drug conjugate (ADC), but no original indication record exists in this dataset for comparison against the predicted new indication.

The evidence pack's own mechanistic assessment is notably skeptical of this prediction: there is no known biological pathway linking HER2 signaling to bone metabolism regulation (the RANKL/OPG axis), and no established connection between HER2-targeted therapy and drug-induced osteoporosis. The assessment explicitly flags this association as likely arising from embedding-level noise in the TxGNN knowledge graph rather than reflecting genuine biological plausibility.

Given the absence of an original indication for comparison, the absence of MOA detail, and the explicit noise-signal caveat in the source rationale, this prediction should be treated as exploratory only and not as a basis for further pharmacological reasoning at this stage.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## US Market Information

This drug currently has **no market authorization records** (market status: Not Marketed; total licenses: 0). No NDA/product information is available in the evidence pack.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (HER2-directed antibody-drug conjugate) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Cytotoxic-payload-bearing ADC; handling per institutional hazardous drug protocols is expected, pending confirmation from official labeling |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction carries only L5 evidence (model output with no supporting clinical trials or literature), the drug has no market authorization on record, and the source rationale itself identifies the mechanistic link as likely noise. Combined with blocking data gaps in safety labeling (TFDA/label warnings and contraindications), this candidate cannot proceed past initial screening (S0).

**To proceed, the following is needed:**
- Original approved indication(s) for trastuzumab deruxtecan (currently missing)
- Confirmed mechanism of action detail from DrugBank or official labeling
- TFDA/FDA label warnings, contraindications, and drug interaction data (currently blocking data gap)
- Independent mechanistic or preclinical evidence linking HER2-ADC therapy to bone metabolism/osteoporosis before any further evaluation is warranted
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

