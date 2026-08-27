---
layout: default
title: Labetalol
parent: 僅模型預測 (L5)
nav_order: 827
evidence_level: L5
indication_count: 4
---

# Labetalol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Labetalol: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Labetalol is a combined alpha-1/non-selective beta-adrenergic blocker, a drug class established for treating hypertension, including hypertensive emergencies. The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension**, with **no clinical trials** and **2 case-report publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (based on known pharmacology; no formal Taiwan license text available — drug not marketed in Taiwan) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L4 |
| US Market Status | ✗ Not Marketed (Taiwan) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacology, labetalol is a combined alpha-1 and non-selective beta-adrenergic receptor blocker, a drug class widely used for hypertension and, notably, as one of the standard intravenous agents for hypertensive emergencies. Its blood-pressure-lowering efficacy in general hypertension is well established.

Malignant renovascular hypertension is fundamentally a severe subtype of hypertension involving renal vasculature. Because the predicted indication shares the same underlying pathophysiology (systemic hypertension) as labetalol's established use, the mechanistic link is a direct extension of an already-confirmed pharmacological action rather than a novel mechanism hypothesis — labetalol's alpha/beta blockade lowers systemic blood pressure, which is the core therapeutic goal in malignant renovascular hypertension as well.

This mechanistic reasonableness is supported qualitatively rather than by high-tier clinical evidence: the only literature identified are two older case reports describing labetalol's use in controlling malignant hypertension, not dedicated trials in the renovascular subtype.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7242419](https://pubmed.ncbi.nlm.nih.gov/7242419/) | 1981 | Case report | The Medical Journal of Australia | Case of malignant hypertension with renal arteritis/aneurysms; minoxidil plus labetalol used for initial blood pressure control |
| [15113447](https://pubmed.ncbi.nlm.nih.gov/15113447/) | 2004 | Case report | BMC Nephrology | Hyponatremic hypertensive syndrome in an 18-month-old presenting as malignant (renovascular) hypertension |

---

## US Market Information

Currently no marketing authorizations recorded (0 licenses; drug not marketed in Taiwan)

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale is sound — labetalol is an established treatment for hypertensive emergencies and malignant hypertension broadly — but direct evidence specific to the renovascular subtype is limited to two decades-old case reports with no clinical trials, placing this at Evidence Level L4.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (currently a Blocking data gap — required before safety (S1) evaluation)
- Formal mechanism of action (MOA) documentation from DrugBank
- Taiwan market authorization status confirmation (currently unmarketed, 0 licenses)
- Dedicated clinical evidence in malignant renovascular hypertension, or at minimum contemporary case series, to move beyond L4
- Route compatibility and similarity-to-original-indication analysis (currently marked "pending" in the evidence pack)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

