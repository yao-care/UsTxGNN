---
layout: default
title: Carvedilol
parent: 僅模型預測 (L5)
nav_order: 502
evidence_level: L5
indication_count: 5
---

# Carvedilol
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

以下是根據 Evidence Pack 產生的完整評估報告：

---

# Carvedilol: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Carvedilol is a non-selective beta/alpha-1 adrenergic receptor blocker used internationally for hypertension and heart failure, though it currently holds no approved licenses in Taiwan.
The TxGNN model predicts it may be effective for **Malignant Hypertensive Renal Disease**,
with **no clinical trials** and **no publications** directly supporting this direction at present.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Taiwan; internationally used for hypertension and heart failure |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Carvedilol is a dual-mechanism adrenergic blocker: its alpha-1 blockade reduces peripheral vascular resistance directly, while its beta-1 blockade suppresses renin secretion from juxtaglomerular cells and reduces cardiac output. Together, these actions address the core haemodynamic drivers of malignant hypertensive renal disease—sustained high perfusion pressure that causes fibrinoid necrosis of glomerular capillaries and rapid loss of kidney function. Additionally, carvedilol has documented antioxidant properties (free radical scavenging) that are not shared by pure beta-blockers, providing a potential secondary benefit in mitigating oxidative injury to the renal microvasculature.

Malignant hypertensive renal disease and the drug's primary cardiovascular indications share the same target system: blood pressure reduction and end-organ protection. This mechanistic overlap is the basis for TxGNN's high prediction score (rank 11,079 out of all disease nodes), and is biologically plausible even in the absence of direct clinical evidence.

However, a critical clinical caveat must be noted: malignant hypertension is an acute emergency typically managed with intravenous agents such as sodium nitroprusside or labetalol. The role of oral carvedilol in the acute phase has not been established, and it is more likely to be relevant as a maintenance or secondary-prevention agent. This distinction limits immediate clinical translatability and warrants careful study design before any trial is proposed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Market Information

Carvedilol currently holds **no approved licenses in Taiwan** (market status: Not Marketed, 0 registered products). No market information table can be generated from the available data.

> **Note for verification:** Carvedilol is approved under multiple brand names (e.g., Coreg) in international markets for heart failure and hypertension. The Taiwan regulatory data in this Evidence Pack shows zero registrations; this should be confirmed against the current TFDA database before drawing regulatory conclusions.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Both the TFDA package insert data and the DrugBank MOA/warning fields are currently unavailable (Data Gaps DG001 and DG002). This is a **Blocking** gap that prevents formal safety pre-screening. Resolution is required before any clinical application proceeds.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic case for carvedilol in malignant hypertensive renal disease is biologically coherent—dual adrenergic blockade plus antioxidant activity directly targets the haemodynamic and oxidative pathways underlying hypertensive nephropathy—but there are currently no clinical trials, no direct supporting literature, and no Taiwan regulatory data to anchor the assessment. Evidence is at L4 (mechanism-based reasoning only), which is insufficient to advance to an actionable development stage.

**To proceed, the following is needed:**

- **Safety data (Blocking):** Obtain the TFDA/package insert for key warnings and contraindications (DG001) before any safety assessment can begin
- **MOA data (High priority):** Retrieve complete mechanism-of-action profile from DrugBank API (DG002) to formalise the mechanistic rationale
- **Targeted literature search:** Re-query PubMed and EMBASE with combined terms (carvedilol AND hypertensive nephropathy / hypertensive renal crisis / malignant hypertension) to identify any indirect evidence not captured by the current search
- **Preclinical evidence review:** Survey animal model studies of carvedilol in hypertensive kidney injury to establish L4 evidence formally
- **Clinical positioning clarification:** Define whether the target use case is acute-phase management (likely not suitable for oral carvedilol) or maintenance/secondary-prevention after acute stabilisation — this determination shapes trial design
- **Comparative landscape:** Assess existing standard-of-care agents (ACE inhibitors, ARBs, CCBs) to identify unmet need or niche where carvedilol offers a differentiated benefit (e.g., patients with ACEi/ARB contraindications due to bilateral renal artery stenosis)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

