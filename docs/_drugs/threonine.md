---
layout: default
title: Threonine
parent: 僅模型預測 (L5)
nav_order: 1224
evidence_level: L5
indication_count: 1
---

# Threonine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Threonine: From Essential Amino Acid to Gastroparesis

## One-Sentence Summary

Threonine is an essential amino acid without an approved therapeutic indication in the current dataset; it is not currently marketed in Taiwan and has no known original mechanism of action.
The TxGNN model predicts a possible link to **Gastroparesis**, but this is supported only by a model score with **no clinical trials** and **a single mechanistic paper** whose relevance appears to be a keyword false-positive.
Evidence is currently insufficient to support any repurposing action.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication on record (Threonine is an essential amino acid / nutritional substance, not a registered drug with a labeled indication) |
| Predicted New Indication | Gastroparesis |
| TxGNN Prediction Score | 99.32% |
| Evidence Level | L5 (model prediction only) |
| Market Status | Not marketed (未上市) — 0 authorizations on file |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (`original_moa: [Data Gap]`). Threonine is an essential amino acid rather than a conventional pharmacological agent, and no therapeutic indication is on record for it, so there is no established original-indication → new-indication pharmacological rationale to evaluate.

More importantly, the single supporting literature record raises a significant concern about relevance rather than confirming it. The paper (PMID 28627597) studies apoptosis and PI3K-AKT-mTOR / AMPK-mTOR signaling in a rat model of diabetic gastroparesis. AKT is a **serine/threonine kinase**, and the term "threonine" in this context very likely refers to a phosphorylation residue on the kinase substrate — not to therapeutic use of threonine as an amino acid. This is consistent with the model's own rationale field, which explicitly flags this as a likely **keyword false-positive** rather than a genuine mechanistic link. There is no evidence in the pack of threonine supplementation being studied as an intervention for gastroparesis.

Given this, the high TxGNN score (99.32%) should not be interpreted as strong biological plausibility — it reflects a graph-level prediction unsupported by corroborating clinical or mechanistic evidence specific to threonine as a drug candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28627597](https://pubmed.ncbi.nlm.nih.gov/28627597/) | 2017 | Mechanistic/Basic Research | Molecular Medicine Reports | Examined gastric smooth muscle cell apoptosis and PI3K-AKT-mTOR / AMPK-mTOR signaling in a rat model of diabetic gastroparesis; "threonine" here refers to a kinase phosphorylation residue (AKT is a serine/threonine kinase), not to threonine as a therapeutic agent — likely a keyword mismatch rather than genuine supporting evidence |

---

## Market Information

No approved authorizations are on file. The drug is currently **not marketed** (未上市), with 0 total licenses recorded.

---

## Safety Considerations

Please refer to the package insert for safety information. Note: label warnings/contraindications data (TFDA) and full DDI data are currently unavailable and flagged as a **Blocking** data gap (DG001), meaning a formal safety review (S1 stage) cannot proceed until this is resolved.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L5 (model prediction only) — there are no clinical trials and only one piece of literature, which itself appears to be a false-positive keyword match (threonine amino acid vs. threonine/serine kinase phosphorylation site) rather than genuine mechanistic support. Combined with the complete absence of safety data, there is no basis to advance this candidate beyond the prediction stage.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain TFDA label warnings/contraindications before any safety review can begin
- Resolve DG002 (High): obtain confirmed mechanism of action data from DrugBank
- Independent literature review to confirm whether any genuine evidence exists for threonine (the amino acid) in gastroparesis, distinct from unrelated kinase-signaling studies
- If no genuine mechanistic or clinical support is found, this candidate should be deprioritized/closed rather than advanced further
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

