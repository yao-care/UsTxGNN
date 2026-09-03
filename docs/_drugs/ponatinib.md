---
layout: default
title: Ponatinib
parent: 僅模型預測 (L5)
nav_order: 1064
evidence_level: L5
indication_count: 2
---

# Ponatinib
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

# Ponatinib: From Unspecified Original Indication to Fibromatosis, Gingival

## One-Sentence Summary

> Ponatinib's original approved indication and mechanism of action are not available in the current evidence pack (data gaps DG001/DG002).
> The TxGNN model predicts it may be effective for **Fibromatosis, Gingival**,
> but currently **no clinical trials or published literature** support this specific prediction — evidence rests solely on the model score.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (data gap) |
| Predicted New Indication | Fibromatosis, Gingival |
| TxGNN Prediction Score | 99.04% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on the information provided, ponatinib's original approved indication(s) and MOA are recorded as data gaps in this evidence pack (DG001 — TFDA labeling/warnings, DG002 — MOA), so a mechanistic rationale linking any original indication to gingival fibromatosis cannot be constructed from the available data.

Without MOA or original-indication data, this prediction currently rests entirely on the TxGNN knowledge-graph score (99.04%, rank 20,750). No independent clinical or mechanistic evidence in the pack corroborates a biological link between ponatinib and gingival fibromatosis at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Additional Predicted Indication (Rank 2, for context)

A second candidate — **Liposarcoma** (TxGNN score 99.00%, rank 21,454) — has one supporting literature reference, though it has not yet undergone tier/relevance classification:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29132397](https://pubmed.ncbi.nlm.nih.gov/29132397/) | 2017 | Preclinical (RNAi/drug screening) | J Hematol Oncol | Kinase profiling in liposarcoma identified druggable kinase targets, supporting a rationale for kinase-inhibitor repurposing in this understudied cancer |

No clinical trials are currently registered for this indication either.

---

## US Market Information

No license/authorization records are available — Taiwan regulatory status is "Not Marketed" with 0 total licenses on file.

---

## Safety Considerations

Please refer to the package insert for safety information. Detailed TFDA warnings and contraindications could not be retrieved for this evidence pack (data gap DG001, severity: Blocking).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The lead prediction (gingival fibromatosis) has no supporting clinical trials or literature, and a Blocking-severity safety data gap (TFDA warnings/contraindications) prevents even an initial safety screen. Evidence is currently model-score-only (L5).

**To proceed, the following is needed:**
- TFDA/FDA label PDF (warnings, contraindications) to clear the Blocking safety gap (DG001)
- Confirmed mechanism of action via DrugBank API (DG002)
- Original approved indication(s) for ponatinib, to establish a mechanistic bridge to the predicted indication
- Targeted literature/clinical-trial search specifically for ponatinib and gingival fibromatosis
- If pursuing the liposarcoma signal instead, formal tier/relevance classification of PMID 29132397 and a search for corroborating trials
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

