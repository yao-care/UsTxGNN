---
layout: default
title: Isotretinoin
parent: 僅模型預測 (L5)
nav_order: 817
evidence_level: L5
indication_count: 2
---

# Isotretinoin
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

# Isotretinoin: From Unrecorded Original Indication to Malignant Renovascular Hypertension

## One-Sentence Summary

Isotretinoin (DrugBank DB00982) is not currently marketed in this jurisdiction, and its original approved indication is not documented in the available evidence pack. The TxGNN model predicts a possible link to **Malignant Renovascular Hypertension** (score 99.01%), but this prediction is supported by **no clinical trials, no literature, and no mechanistic rationale** — it rests on the knowledge-graph signal alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (no licenses on file) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.01% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for isotretinoin in this evidence pack. Based on general pharmacology, isotretinoin (13-cis-retinoic acid) is a retinoic acid receptor (RAR) agonist whose established clinical use centers on sebaceous gland differentiation and keratinization — a dermatologic mechanism with no documented connection to renovascular or hypertensive-renal pathophysiology.

The repurposing rationale supplied with this candidate is explicit on this point: there is **no known pharmacological pathway** linking retinoic acid signaling to blood pressure regulation, the renin-angiotensin-aldosterone axis, or renal artery stenosis pathology. The mechanistic link is described as inferable only through indirect knowledge-graph connections, without direct biological evidence.

Notably, the second-ranked prediction ("malignant hypertensive renal disease") carries an almost identical TxGNN score (99.01%, adjacent rank), suggesting these two disease nodes are closely clustered in the knowledge graph rather than representing two independently validated signals. Combined with isotretinoin's known safety profile (teratogenicity, hepatotoxicity, neuropsychiatric effects, pseudotumor cerebri) — none of which relate favorably to a renal-hypertensive treatment goal — the biological plausibility of this prediction is low.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

No NDA or marketing authorization is on file for isotretinoin in this jurisdiction (market status: not marketed; total licenses: 0).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate is supported only by an L5 knowledge-graph signal, with no clinical trials, literature, or mechanistic pathway connecting isotretinoin to renovascular/hypertensive-renal disease. Two of the top predictions appear to be near-duplicate disease nodes, and the drug's known safety liabilities (teratogenicity, hepatotoxicity, neuropsychiatric risk) do not clearly favor this indication.

**To proceed, the following is needed:**
- TFDA (or equivalent regulatory) label — warnings/precautions and contraindications (blocking gap, DG001)
- Verified mechanism of action data from DrugBank (DG002)
- Preclinical or mechanistic studies establishing a biological rationale for retinoid activity in renovascular/renal-hypertensive disease
- Clarification of the original approved indication, since none is currently on file for this jurisdiction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

