---
layout: default
title: Aconitum Napellus Whole Eucalyptus Globulus Leaf I
parent: 僅模型預測 (L5)
nav_order: 139
evidence_level: L5
indication_count: 0
---

# Aconitum Napellus Whole Eucalyptus Globulus Leaf I
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Aconitum Napellus / Eucalyptus Globulus / Ipecac: Insufficient Data for Repurposing Evaluation

## One-Sentence Summary

This submission involves a combination of three natural/herbal substances — **Aconitum napellus whole**, **Eucalyptus globulus leaf**, and **Ipecac** — for which no approved indication, no DrugBank identifier, and no TxGNN-predicted new indications are currently available.
The TxGNN model returned **zero repurposing candidates**, and the combination is **not marketed** in Taiwan.
Given the complete absence of regulatory, mechanistic, and predictive data, this candidate cannot proceed to formal evaluation at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not established (no regulatory record found) |
| Predicted New Indication | None (TxGNN returned no candidates) |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — Model prediction only; in this case, no prediction was generated |
| Market Status | Not marketed in Taiwan; US status unknown |
| Number of Approvals | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN repurposing prediction was generated for this combination, so a mechanistic rationale cannot be constructed at this time.

For background context: this combination appears consistent with a **homeopathic or phytotherapeutic preparation**. The three components are:

- **Aconitum napellus whole** — a highly toxic plant (contains aconitine, a cardiotoxic and neurotoxic alkaloid) used in highly diluted homeopathic formulations; known for its role in traditional medicine for pain, fever, and inflammation.
- **Eucalyptus globulus leaf** — contains 1,8-cineole (eucalyptol); used traditionally for respiratory conditions, as an expectorant and mild antiseptic.
- **Ipecac** (from *Carapichea ipecacuanha*) — contains emetine and cephaeline; historically used as an emetic for poison management, and in homeopathy for nausea.

Without a DrugBank ID, no knowledge-graph traversal is possible. The TxGNN model could not identify any disease node sufficiently connected to this compound combination to generate a candidate prediction.

Currently, detailed mechanism of action data is not available. Based on known pharmacognosy, this combination belongs to the herbal/homeopathic category, and its systemic applicability to any new indication cannot be assessed without further data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this combination.

---

## Literature Evidence

Currently no related literature available for this combination as a whole.

---

## Safety Considerations

> ⚠️ **Important safety notice**: Even in the absence of formal regulatory data, **Aconitum napellus** contains aconitine, which is highly toxic at non-homeopathic doses and has a narrow therapeutic index. Cardiotoxicity and neurotoxicity have been documented in case reports worldwide. Similarly, **Ipecac** (emetine) carries risk of cardiotoxicity with repeated or high-dose use.

Please refer to the relevant package inserts, pharmacopeial monographs, and local poison control guidelines for safety information on these substances.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model generated no repurposing predictions for this combination, no regulatory record exists in Taiwan, no DrugBank ID is available, and all safety data fields are currently unresolved. This candidate does not meet the minimum data threshold required for a repurposing evaluation.

**To proceed, the following is needed:**

- Clarify whether this is a **homeopathic preparation** (e.g., listing dilution ratios) or a conventional fixed-dose combination — this determines which regulatory pathway and evidence standards apply
- Obtain or assign a **DrugBank ID** for each active ingredient individually, enabling separate TxGNN traversals for *Aconitum napellus*, *Eucalyptus globulus*, and *Ipecac*
- Retrieve **mechanism of action (MOA)** data for each component from DrugBank or primary pharmacological literature
- Confirm **US/Taiwan regulatory status** for each individual component and for the combination product
- Conduct a targeted **literature review** for each active ingredient separately, particularly for Aconitum alkaloids and emetine in oncology or anti-inflammatory contexts
- Resolve the **DG001 (safety warnings)** and **DG002 (MOA)** data gaps identified in the Evidence Pack before re-submitting for evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

