---
layout: default
title: Nebivolol
parent: 僅模型預測 (L5)
nav_order: 958
evidence_level: L5
indication_count: 5
---

# Nebivolol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Nebivolol: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Nebivolol is a β1-selective adrenergic receptor blocker generally used to treat hypertension. The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**, with a prediction score of **99.42%**, but currently **no clinical trials and no published literature** directly support this specific indication.

*Note: the evidence pack's structured `original_indications` and license fields were empty for this drug; "Hypertension" is used here based on Nebivolol's well-established pharmacological class and is consistent with the blood-pressure-lowering rationale referenced throughout this evidence pack.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured DrugBank record for Nebivolol. Based on known pharmacological information, Nebivolol is a β1-selective adrenergic receptor blocker that also promotes endothelial nitric oxide (NO)-mediated vasodilation. Its efficacy in essential hypertension is well established, and mechanistically it could plausibly extend to malignant hypertensive renal disease, since this condition results from severe, uncontrolled systemic hypertension that causes acute renal vascular injury.

However, the relationship between the two conditions is only partial. Malignant hypertensive renal disease is typically an acute, emergent presentation requiring rapid, titratable blood pressure control with intravenous agents such as nicardipine or labetalol. Nebivolol is an oral, long-acting formulation not designed for acute titration, meaning it does not fit the standard treatment profile for this population even though its underlying pharmacology (systemic antihypertensive effect) is directionally relevant.

Overall, the mechanistic link here is class-level (beta-blockers lower blood pressure generally) rather than disease-specific. No data in this evidence pack demonstrates a targeted effect of Nebivolol on malignant hypertensive renal disease pathophysiology beyond its general antihypertensive action.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

No license records currently available — Nebivolol is not marketed in this jurisdiction (0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level for this candidate is L5 — a model prediction with no supporting clinical trials or literature. The mechanistic rationale is class-level (general antihypertensive effect) rather than disease-specific, and a blocking data gap exists for regulatory safety labeling (warnings/contraindications).

**To proceed, the following is needed:**
- TFDA/FDA label warnings and contraindications (currently a blocking data gap)
- Confirmed mechanism of action data from DrugBank or primary literature
- Preclinical or clinical evidence specific to malignant hypertensive renal disease (not just general hypertension)
- Clarification of route compatibility, since acute management of this condition typically requires titratable IV agents rather than an oral long-acting beta-blocker
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

