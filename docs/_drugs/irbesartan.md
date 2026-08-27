---
layout: default
title: Irbesartan
parent: 僅模型預測 (L5)
nav_order: 809
evidence_level: L5
indication_count: 4
---

# Irbesartan
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

# Irbesartan: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Irbesartan (DrugBank DB01029) is an angiotensin II receptor blocker (ARB) whose established indication is hypertension (this evidence pack does not carry a confirmed Taiwan/US regulatory filing for it — see Data Gaps below).
The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension**, but currently **no clinical trials and no literature** directly support this specific indication — the prediction rests on mechanistic plausibility (RAAS inhibition) alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack's Taiwan regulatory data (drug shows as unmarketed, 0 licenses); per general ARB-class pharmacology: hypertension |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 (model prediction only, no clinical trial or literature support) |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

*Note: two closely related predictions score nearly identically — "malignant hypertensive renal disease" (rank 2, score 99.31%) is mechanistically the same pathology (renal sequela of malignant hypertension) and carries the same evidence gap. "Pulmonary hypertension owing to lung disease/hypoxia" (rank 3) and "pulmonary hypertension with unclear multifactorial mechanism" (rank 4) score similarly (~99.25%) but ARB is not a standard mechanistic fit for WHO Group 3/5 pulmonary hypertension, and the 20 PubMed hits returned for rank 3 are generic hypoxia/oncology biology papers unrelated to irbesartan or pulmonary hypertension treatment — they do not constitute supporting evidence.*

---

## Why is This Prediction Reasonable?

Detailed, source-verified mechanism-of-action data is not available in this evidence pack (`original_moa` is flagged as a High-severity data gap). Based on general pharmacological classification, irbesartan is an angiotensin II receptor blocker (ARB) that inhibits the renin-angiotensin-aldosterone system (RAAS), and its efficacy in essential hypertension is well established as a drug class.

Malignant renovascular hypertension arises from renal artery stenosis driving pathological RAAS overactivation, which produces both severe hypertension and progressive renal injury. Mechanistically, ARB-mediated RAAS blockade is a direct pharmacological counter to this pathway, which is consistent with the very high TxGNN score (0.993) for both this indication and its closely related renal-disease counterpart.

However, this mechanistic plausibility has not been corroborated by any indication-specific clinical trial or publication in this evidence pack — the searches returned zero results for both malignant renovascular hypertension and malignant hypertensive renal disease across ClinicalTrials.gov, ICTRP, and PubMed. The prediction should therefore be read as a model-driven hypothesis grounded in class pharmacology, not as an evidence-backed repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(TFDA warnings and contraindications are flagged as a Blocking data gap — S1 safety screening cannot proceed until this is obtained.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is high, and the RAAS-inhibition mechanism is biologically plausible for malignant renovascular hypertension, but there is zero clinical trial or literature evidence directly supporting this indication, and the drug's Taiwan/US market status, MOA, and safety data (warnings/contraindications) are all unconfirmed or missing from this evidence pack.

**To proceed, the following is needed:**
- TFDA package insert (warnings and contraindications) — currently a Blocking gap preventing safety screening
- Confirmed original MOA and approved indication data from DrugBank/regulatory source — currently a High-severity gap
- Indication-specific literature/trial search for irbesartan in renovascular or malignant hypertension (current pulmonary-hypertension literature hits are not relevant and should not be cited as support)
- Confirmation of actual Taiwan/US marketing and license status, since this evidence pack currently shows the drug as unmarketed with zero licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

