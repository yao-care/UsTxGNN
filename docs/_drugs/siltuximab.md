---
layout: default
title: Siltuximab
parent: 僅模型預測 (L5)
nav_order: 1161
evidence_level: L5
indication_count: 8
---

# Siltuximab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Siltuximab: From No Registered Indication to Extracutaneous Mastocytoma (Predicted)

## One-Sentence Summary

> Siltuximab does not currently hold a marketing license or documented approved indication in this jurisdiction, and it is known pharmacologically as a chimeric anti-IL-6 monoclonal antibody.
> The TxGNN model predicts it may be effective for **Extracutaneous Mastocytoma**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications**, making it a model-only hypothesis at this stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — drug is not marketed in this jurisdiction; no license/indication text on file |
| Predicted New Indication | Extracutaneous Mastocytoma |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L5 |
| Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on information contained in this evidence pack, siltuximab is a chimeric (human-murine) anti-interleukin-6 (IL-6) monoclonal antibody administered by intravenous infusion.

The model's own rationale notes that IL-6 expression has occasionally been observed in mastocytoma lesions in association with local inflammatory activity. However, there is no direct evidence that IL-6 acts as a key driver pathway for tumor growth in extracutaneous mastocytoma — the mechanistic link is described as weak and inferential rather than established. This prediction should therefore be treated as a hypothesis-generating signal from the knowledge graph rather than a mechanistically validated candidate.

It is also worth noting that among the eight indications TxGNN predicted for siltuximab, **Kaposi's sarcoma** (rank 5) carries comparatively stronger mechanistic plausibility — IL-6 is implicated in HHV-8-driven pathology and in HHV-8-associated multicentric Castleman's disease, which frequently co-occurs with Kaposi's sarcoma — and reached evidence level L4 with at least indirect literature support. This may be a more productive direction for follow-up than the top-ranked mastocytoma prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Market Information

This drug is **not currently marketed** in this jurisdiction. No license records, product names, dosage forms, or approved indication text are on file.

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: TFDA warning/contraindication data and drug interaction data are currently unavailable and are flagged as a blocking data gap (DG001) — this must be resolved before any safety pre-assessment (S1) can proceed for this drug.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (extracutaneous mastocytoma) has no clinical trial or literature support and rests on an explicitly weak, inferential mechanistic link (L5 — model prediction only). Combined with the absence of local market authorization and missing safety labeling data, there is insufficient basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA (or equivalent local regulator) package insert — warnings and contraindications (blocking gap, DG001)
- Confirmed mechanism of action data from DrugBank or primary literature (DG002)
- Preclinical or case-level evidence directly evaluating IL-6 blockade in mastocytoma
- Consider evaluating the rank-5 candidate (Kaposi's sarcoma), which currently has a stronger mechanistic rationale (HHV-8/IL-6 axis) and reached evidence level L4, as a higher-priority research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

