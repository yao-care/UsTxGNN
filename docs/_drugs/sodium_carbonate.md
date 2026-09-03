---
layout: default
title: Sodium Carbonate
parent: 僅模型預測 (L5)
nav_order: 1168
evidence_level: L5
indication_count: 6
---

# Sodium Carbonate
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

# Sodium Carbonate: From Undocumented Original Indication to Cauda Equina Syndrome (Model Prediction Only)

## One-Sentence Summary

> Sodium Carbonate (DrugBank DB09460) has no documented original indication or mechanism of action in this Evidence Pack, and it is not currently marketed in Taiwan or the US.
> The TxGNN model predicts a possible association with **Cauda Equina Syndrome**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure graph-embedding signal with no biological rationale.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in available data |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Sodium Carbonate, and no original indication is recorded in this Evidence Pack. Based on general pharmacological knowledge, sodium carbonate is an inorganic alkalizing/pH-adjusting agent, typically used as an excipient or buffering agent rather than as a standalone therapeutic.

For the top-ranked prediction — Cauda Equina Syndrome, a neurosurgical emergency caused by nerve root compression — the Evidence Pack explicitly states there is **no known biological connection** between an alkalizing agent and this condition's pathophysiology. The 99.80% TxGNN score reflects graph-embedding similarity only, not a validated pharmacological hypothesis.

It is worth noting that several lower-ranked candidates (e.g., ventricular tachycardia, anaphylaxis) have plausible **class-effect** rationale, since the related compound sodium bicarbonate has established use in alkalinizing therapy for sodium-channel-blocker toxicity and as a buffering excipient in epinephrine formulations. However, these are indirect extrapolations from a related compound, not direct evidence for sodium carbonate itself, and are not the top-ranked prediction in this pack.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Sodium Carbonate is currently **not marketed** in Taiwan or the US per this Evidence Pack, with 0 recorded authorizations/licenses. No product-level market information is available.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug interaction data are currently available for this compound, and TFDA label data (DG001) has not yet been retrieved.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is an L5 (prediction-only) candidate with no mechanism of action, no original indication, no clinical trials, and no literature support. The top-ranked predicted indication (cauda equina syndrome) has no biologically plausible link to the drug's known pharmacology, and the drug is not currently marketed in Taiwan or the US.

**To proceed, the following is needed:**
- TFDA label / package insert (warnings, contraindications) — currently blocking (DG001)
- Confirmed mechanism of action from DrugBank or primary literature (DG002)
- Original indication(s), if any, to establish a baseline pharmacological rationale
- Preclinical or mechanistic evidence specifically linking sodium carbonate (not sodium bicarbonate) to any of the predicted indications before advancing past S0
- If class-effect extrapolation from sodium bicarbonate is to be pursued, a formal review of the two compounds' PK/PD equivalence for the intended route of administration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

