---
layout: default
title: Triamterene
parent: 僅模型預測 (L5)
nav_order: 1258
evidence_level: L5
indication_count: 6
---

# Triamterene
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

# Triamterene: From Potassium-Sparing Diuretic Use to Malignant Hypertensive Renal Disease

## One-Sentence Summary

> Triamterene is a potassium-sparing diuretic (ENaC blocker); this evidence pack contains no confirmed original indication, TFDA license, or MOA record.
> The TxGNN model ranks **Malignant Hypertensive Renal Disease** as its top prediction with a **99.89%** score, but **0 clinical trials** and **0 publications** support it —
> and the mechanistic rationale itself flags this as a **hyperkalemia risk signal**, not a therapeutic opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file (no TFDA/regulatory license data provided; commonly known as a potassium-sparing diuretic for edema/hypertension) |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 (model prediction only, no clinical/literature support) |
| US Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data is not formally on file (`original_moa: [Data Gap]`). Based on the rationale text provided with this prediction, triamterene is a **potassium-sparing diuretic that blocks the epithelial sodium channel (ENaC)**, producing a mild antihypertensive/diuretic effect by reducing sodium reabsorption in the distal nephron.

However, this mechanism does **not** support its use in malignant hypertensive renal disease. Patients with this condition typically have impaired renal function and activated renin-angiotensin-aldosterone signaling, both of which sharply increase the risk of **hyperkalemia** when a potassium-sparing agent is used — especially in combination with ACEI/ARB therapy, which is standard of care in this population. The TxGNN prediction pack itself characterizes this link as "risk rather than efficacy," and no clinical trial or literature evidence exists to counter that assessment.

The next-ranked prediction (rank 2, malignant renovascular hypertension) shares the identical score and the same safety concern. Ranks 3–5 (pulmonary hypertension variants, Braddock syndrome) have no plausible mechanistic link and no supporting evidence at all — these appear to be prediction noise. The one indication with any literature backing is **chronic pulmonary heart disease** (rank 6, L4, "Research Question" status), supported by decades-old, non-triamterene-specific diuretic studies used for volume overload in cor pulmonale — a supportive rather than disease-modifying role.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

No marketing authorizations are on file for this evidence pack (`total_licenses: 0`, `market_status: 未上市`). Triamterene is not currently marketed under the jurisdiction covered by this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA warnings/contraindications and DDI data are flagged as a **Blocking** data gap — see Conclusion.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Malignant Hypertensive Renal Disease) has zero clinical or literature support, and its own mechanistic rationale identifies a **hyperkalemia risk** rather than a therapeutic benefit — this is not a viable repurposing candidate. The only prediction with any evidence base (chronic pulmonary heart disease, L4) rests on generic, decades-old diuretic-combination studies rather than triamterene-specific efficacy data, and stops at "Research Question" status.

**To proceed, the following is needed:**
- TFDA-equivalent warnings/contraindications and full prescribing information (DG001, **Blocking** — required before any S1 safety evaluation)
- Verified mechanism of action from DrugBank (DG002, currently missing)
- If pursuing chronic pulmonary heart disease as a low-priority research question: triamterene-specific (not general diuretic-class) trial or cohort data in cor pulmonale/right heart failure populations
- Renal function and serum potassium risk assessment before considering any hypertensive-renal-disease indication further
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

