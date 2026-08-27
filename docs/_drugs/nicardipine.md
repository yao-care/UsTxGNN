---
layout: default
title: Nicardipine
parent: 僅模型預測 (L5)
nav_order: 963
evidence_level: L5
indication_count: 5
---

# Nicardipine
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

# Nicardipine: From Hypertension to Pulmonary Hypertension with Unclear Multifactorial Mechanism

## One-Sentence Summary

Nicardipine is a dihydropyridine calcium channel blocker (CCB); its original approved indication is not on file in the current evidence pack (the product is not currently marketed in Taiwan, and no license text is available). The TxGNN model predicts it may be effective for **pulmonary hypertension with unclear multifactorial mechanism**, but this direction is currently supported by **no clinical trials** and **no literature** — only the TxGNN prediction score.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented — no TFDA license record on file; based on known pharmacology, nicardipine is a dihydropyridine CCB used for hypertension |
| Predicted New Indication | Pulmonary hypertension with unclear multifactorial mechanism |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this candidate. Based on known information, nicardipine belongs to the dihydropyridine calcium channel blocker (CCB) class, acting by blocking L-type calcium channels in vascular smooth muscle to produce systemic vasodilation — the mechanism underlying its established use in hypertension.

For this particular predicted indication, the underlying disease pathology is itself described as "unclear/multifactorial," meaning there is no defined pathological pathway to which nicardipine's vasodilatory mechanism can be mapped. Without a clear disease mechanism to anchor against, it is not currently possible to construct a coherent pharmacological rationale linking the drug's known CCB activity to therapeutic benefit in this specific form of pulmonary hypertension.

Notably, other candidates generated for this drug (e.g., malignant renovascular hypertension, malignant hypertensive renal disease) represent more straightforward class-effect extensions of nicardipine's known antihypertensive activity, but even these lack any dedicated trial or literature evidence in the current pack. This top-ranked candidate, despite having the highest TxGNN score among the five, has the weakest mechanistic anchoring of the group.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a TxGNN model score, with zero supporting clinical trials or literature, an unclear disease mechanism to validate against, and no accessible TFDA warnings, contraindications, or drug interaction data — the safety data gap (DG001) is flagged as Blocking, meaning this candidate cannot yet clear even initial safety screening.

**To proceed, the following is needed:**
- TFDA package insert (warnings/precautions and contraindications) to clear the blocking safety data gap (DG001)
- Confirmed mechanism of action data for nicardipine (DG002)
- Literature or trial evidence specific to nicardipine in this pulmonary hypertension subtype (current literature hits for the related rank-2 candidate are background hypoxia biology, not drug-specific)
- A clearer pathophysiological definition of the target disease to support a mechanistic rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

