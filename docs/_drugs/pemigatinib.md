---
layout: default
title: Pemigatinib
parent: 僅模型預測 (L5)
nav_order: 1026
evidence_level: L5
indication_count: 10
---

# Pemigatinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Pemigatinib: From an Undocumented Original Indication to Multiple Endocrine Neoplasia

## One-Sentence Summary

> This evidence pack contains no record of Pemigatinib's original approved indication or mechanism of action (both flagged as data gaps), though supporting rationale text identifies it as an FGFR1–3 tyrosine kinase inhibitor used in oncology.
> The TxGNN model's top-ranked prediction is **Multiple Endocrine Neoplasia**, but this is supported by **0 clinical trials** and **0 publications**, and the model's own mechanistic rationale flags the signal as likely knowledge-graph noise.
> Given a Blocking data gap on regulatory safety information and essentially no independent evidence, this candidate is **not ready to advance**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (no license/indication data available) |
| Predicted New Indication | Multiple Endocrine Neoplasia |
| TxGNN Prediction Score | 99.71% (model rank 7826) |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (flagged as a High-severity data gap). Based on contextual information embedded in the model's own rationale text, Pemigatinib is referenced as a small-molecule FGFR1–3 tyrosine kinase inhibitor used in an oncology setting — this is inferred, not confirmed by structured MOA data, and should be independently verified.

For the top-ranked prediction itself, the picture is not favorable. The model's own repurposing rationale states that Multiple Endocrine Neoplasia (MEN1/MEN2) is driven primarily by menin loss-of-function or RET oncogenic mutations, and that "no clear direct relationship" exists with FGFR1/2/3 signaling. The rationale explicitly attributes the high TxGNN score to likely **co-occurrence noise between tumor-associated genes in the knowledge graph**, rather than a genuine pharmacological signal.

Interestingly, among the 10 candidates reviewed, rank 3 (**HER2 positive breast carcinoma**) has a somewhat stronger — though still weak — mechanistic story: FGFR signaling is a documented crosstalk pathway and resistance mechanism in anti-HER2 therapy, and it is the only candidate reaching evidence level L4 in this pack. However, its single supporting citation is a general 2021 review of FDA-approved kinase inhibitors, not indication-specific evidence. Several other candidates (infectious bovine rhinotracheitis, malignant catarrh) are veterinary diseases with no relevance to human therapeutics and should be treated as knowledge-graph artifacts.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Cytotoxicity

Structured DrugBank category and toxicity data are not present in this evidence pack. Contextual rationale text identifies Pemigatinib as a small-molecule FGFR1–3 tyrosine kinase inhibitor (targeted therapy), but this classification should be confirmed via DrugBank before use. Please refer to the package insert warnings and precautions once TFDA/FDA labeling data is obtained (see Conclusion, DG001).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Multiple Endocrine Neoplasia) has no clinical trial or literature support (L5) and the model's own rationale casts doubt on its mechanistic validity, likely reflecting knowledge-graph co-occurrence noise. This is compounded by a Blocking data gap on TFDA warnings/contraindications, which prevents even a baseline safety assessment.

**To proceed, the following is needed:**
- Resolve DG001: obtain TFDA/FDA label warnings and contraindications for Pemigatinib
- Resolve DG002: confirm mechanism of action and DrugBank drug categories via DrugBank API
- Confirm the original approved indication(s), which are currently missing from this evidence pack
- If pursued further, prioritize **HER2 positive breast carcinoma** (rank 3, L4) as a research question over the top-ranked MEN prediction, and seek indication-specific preclinical or clinical evidence rather than general kinase-inhibitor reviews
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

