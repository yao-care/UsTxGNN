---
layout: default
title: Trandolapril
parent: 僅模型預測 (L5)
nav_order: 1247
evidence_level: L5
indication_count: 6
---

# Trandolapril
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

# Trandolapril: From Hypertension (ACE Inhibitor Class) to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Trandolapril is an ACE inhibitor; the exact regulatory-approved original indication is not available in this dataset, but its pharmacological class is classically used for hypertension. The TxGNN model predicts potential efficacy in **Malignant Hypertensive Renal Disease**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — the evidence rests solely on the model's prediction score (99.92%).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in available regulatory data (drug class: ACE inhibitor, typically indicated for hypertension) |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap). Based on the information present in this evidence pack, trandolapril is classified as an **ACE inhibitor (ACEi)**. Pharmacologically, ACE inhibitors are a standard class of therapy for malignant hypertension complicated by renal disease, acting through inhibition of angiotensin II–mediated elevation of intraglomerular pressure, which provides both blood-pressure lowering and renal-protective effects.

Malignant hypertensive renal disease and standard hypertension (the presumed original indication of this drug class) share the same underlying pathophysiology — excessive RAAS (renin-angiotensin-aldosterone system) activation — which makes this prediction a reasonable **class-effect extrapolation** rather than a novel mechanistic hypothesis. However, because the original approved indication for this specific product could not be confirmed from the regulatory dataset, it remains unclear whether this represents genuine "repurposing" or simply an existing, unregistered use of the drug class.

It should also be noted that no clinical trial or literature evidence in this dataset directly supports this specific indication — the mechanistic rationale is inferred from drug-class knowledge alone, not from trial or publication data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## US Market Information

Trandolapril is currently **未上市 (not marketed)** in this dataset's jurisdiction, with 0 registered licenses. No authorization records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** TFDA labeling data (key warnings and contraindications) is flagged as a **Blocking** data gap (DG001) in this evidence pack, meaning a proper safety (S1) evaluation cannot yet be completed for this drug.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is supported only by a TxGNN model score (Evidence Level L5) — no clinical trials or literature evidence exist for malignant hypertensive renal disease specifically. In addition, a **Blocking** data gap (TFDA warnings/contraindications unavailable) prevents even a preliminary safety assessment, so this candidate cannot proceed past a research hypothesis at this time.

**To proceed, the following is needed:**
- TFDA label data (key warnings, contraindications) to complete initial safety screening (DG001)
- Confirmed mechanism of action (MOA) from DrugBank or equivalent source (DG002)
- Confirmed original approved indication(s) for trandolapril in this jurisdiction
- Any available renal-function or hypertensive-crisis population data (given ACE inhibitors carry known risks in renal impairment and renal artery stenosis — see related candidate "malignant renovascular hypertension," which was independently flagged Hold due to this risk)
- Prospective or observational clinical evidence specific to malignant hypertensive renal disease before advancing beyond the research-question stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

