---
layout: default
title: Felodipine
parent: 僅模型預測 (L5)
nav_order: 696
evidence_level: L5
indication_count: 7
---

# Felodipine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Felodipine: From Hypertension to Pulmonary Hypertension with Unclear Multifactorial Mechanism

## One-Sentence Summary

Felodipine is a dihydropyridine calcium channel blocker (DHP-CCB) whose established clinical use is blood pressure control in hypertension. The TxGNN model's top-ranked prediction for this drug is **pulmonary hypertension with unclear multifactorial mechanism** (TxGNN score 99.91%), but **no clinical trials and no published literature currently support this specific prediction** — it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in US regulatory data (0 NDAs on file); pharmacologically a DHP calcium channel blocker used for hypertension |
| Predicted New Indication | Pulmonary hypertension with unclear multifactorial mechanism |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank query flagged as a High-severity data gap). Based on known information available elsewhere in this evidence pack, felodipine is a dihydropyridine calcium channel blocker (DHP-CCB) that acts as a systemic vasodilator; its efficacy in hypertension is well established, and mechanistically the same vasodilatory action could theoretically extend to pulmonary vascular resistance.

However, "pulmonary hypertension with unclear multifactorial mechanism" corresponds to WHO Group 5 PH, an etiologically heterogeneous category where systemic vasodilators are not standard therapy and — in some PH subtypes — can be harmful (e.g., unopposed systemic hypotension without corresponding pulmonary selectivity). No felodipine-specific trial or publication in this pack addresses this indication, so the mechanistic plausibility above is theoretical, not evidence-backed.

Notably, other TxGNN-predicted indications for felodipine in this same batch have direct, drug-specific supporting literature (see Conclusion), which is not the case for the top-ranked candidate presented here.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

Felodipine is currently **not marketed** in the United States under this evidence pack's records — 0 NDAs/licenses are on file.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN prediction score (99.91%), zero clinical trials and zero publications directly support felodipine's use in pulmonary hypertension with unclear multifactorial mechanism — this meets the L5 criterion (model prediction only, no actual studies), which does not warrant advancing past a Hold.

**To proceed, the following is needed:**
- Direct clinical or mechanistic evidence (in vitro, animal, or human) connecting felodipine to WHO Group 5 pulmonary hypertension specifically
- Felodipine MOA and DrugBank category data (currently a Blocking/High-severity data gap) to support mechanistic-link analysis
- TFDA/FDA label data (warnings, contraindications) before any S1 safety screening can proceed
- Confirmation of current US marketing status, since 0 NDAs are on file despite felodipine being a known marketed molecule elsewhere
- Consider redirecting evaluation effort toward this same batch's better-evidenced candidates — **chronic pulmonary heart disease** (3 felodipine-specific hemodynamic studies) and **Prinzmetal angina** (9 felodipine-specific trials, including head-to-head RCTs vs. nifedipine) — both already show direct drug-level evidence that this top-ranked candidate lacks
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

