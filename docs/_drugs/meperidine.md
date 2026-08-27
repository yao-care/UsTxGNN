---
layout: default
title: Meperidine
parent: 僅模型預測 (L5)
nav_order: 897
evidence_level: L5
indication_count: 2
---

# Meperidine
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

# Meperidine: From Pain Management to Tourette Syndrome

## One-Sentence Summary

Meperidine (pethidine, DrugBank DB00454) is an opioid analgesic historically used for moderate-to-severe pain. The TxGNN model predicts potential efficacy for **Tourette Syndrome**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it reflects a knowledge-graph statistical association only, with no direct mechanistic or clinical evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from licensing data; based on known pharmacology, meperidine is an opioid analgesic used for moderate-to-severe pain |
| Predicted New Indication | Tourette Syndrome |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Taiwan Market Status | Not marketed (未上市) |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

*A second candidate, trichotillomania (score 99.39%, rank 13973), was also flagged with identical L5 evidence and a Hold recommendation — see note below.*

---

## Why is This Prediction Reasonable?

Detailed original mechanism-of-action data (DrugBank MOA field) is not available for this record. However, based on known pharmacology, meperidine is a mu-opioid receptor agonist that also has anticholinergic, local-anesthetic (sodium-channel blocking), NMDA-antagonist, and monoamine-reuptake-inhibiting activity.

For **Tourette syndrome**, the tic-related dysregulation of basal ganglia dopamine has led some researchers to propose an "endogenous opioid hypothesis" — but that hypothesis has primarily been tested with opioid **antagonists** (e.g., naltrexone), not agonists. Meperidine acts in the opposite pharmacological direction, so there is no mechanistic basis for expecting it to improve tic symptoms.

For **trichotillomania**, the prevailing pharmacological hypothesis similarly implicates opioid **antagonists** as reducing impulsive hair-pulling behavior by blocking opioid signaling in reward/impulse circuits. Meperidine, as an opioid agonist, runs counter to this hypothesis and could theoretically worsen rather than improve impulsive behavior.

In both cases, the high TxGNN score (>99%) reflects knowledge-graph relationship strength, not causal or mechanistic evidence, and the mechanistic direction available in the evidence pack argues against — rather than for — plausibility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Meperidine currently holds no TFDA licenses and is not marketed in Taiwan (0 licenses on record).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both predicted indications (Tourette syndrome and trichotillomania) have zero clinical trial and literature support (L5, model prediction only), and the available mechanistic rationale suggests meperidine's opioid-agonist activity runs counter to the opioid-antagonist hypotheses proposed for these conditions. The drug is also unmarketed in Taiwan with no TFDA safety data on file.

**To proceed, the following is needed:**
- Confirmed DrugBank/TFDA mechanism-of-action and labeling data (currently blocking per data gap DG001/DG002)
- Preclinical or case-level evidence testing meperidine specifically (not opioid antagonists) in tic or impulse-control disorders
- TFDA warnings/contraindications data before any safety evaluation (S1) can begin
- Reassessment if independent mechanistic or trial evidence emerges, given the current agonist-vs-antagonist directional conflict
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

