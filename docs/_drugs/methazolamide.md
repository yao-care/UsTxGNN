---
layout: default
title: Methazolamide
parent: 僅模型預測 (L5)
nav_order: 906
evidence_level: L5
indication_count: 3
---

# Methazolamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Methazolamide: From Carbonic Anhydrase Inhibitor to Primary Hereditary Glaucoma

## One-Sentence Summary

Methazolamide (DrugBank DB00703) is a carbonic anhydrase inhibitor; its original indication record is not available in this database and the drug is not currently marketed in Taiwan. The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma**, but this specific evidence pack currently contains **0 clinical trials** and **0 publications** directly supporting the pairing — the high score reflects the drug's known pharmacological class rather than confirmed new evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in database (drug not marketed in Taiwan; DrugBank original-indication field is empty) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 (no clinical trials or literature retrieved for this drug–disease pair) |
| Taiwan Market Status | ✗ 未上市 (Not marketed) |
| License Count | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not on file for this record (`original_moa: [Data Gap]`). Based on known pharmacology, methazolamide belongs to the **carbonic anhydrase inhibitor (CAI)** class, alongside acetazolamide and dorzolamide. In several markets, methazolamide itself is already approved for glaucoma — CAIs lower intraocular pressure by inhibiting carbonic anhydrase in the ciliary body, reducing aqueous humor production. This is a well-established, mechanistically direct route to treating glaucoma, not a novel or speculative pathway.

Given this, the TxGNN prediction most plausibly reflects the model rediscovering an already-known pharmacological use of the drug class, rather than surfacing new evidence. The empty `original_indications` field in this dataset is more likely a local data-collection gap than evidence that methazolamide has no established ocular indication.

Because no clinical trials or publications specific to methazolamide + primary hereditary glaucoma were retrieved in this search cycle, this prediction should be treated as **mechanistically credible but currently evidence-thin** within this evidence pack, and would benefit from a broader literature search (e.g., including historical glaucoma-specific terms not captured by the current disease-name query).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

Methazolamide has 0 registered licenses and is not currently marketed in Taiwan, so no product/authorization details are available.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are all currently unavailable — TFDA label data is flagged as a **Blocking** data gap, DG001.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score (99.83%) and known CAI-class mechanism make this a plausible signal, but no clinical trial or literature evidence specific to methazolamide in glaucoma exists in this evidence pack, and safety/labeling data is completely unavailable — a Blocking-severity gap that prevents even an initial safety screen (S1).

**To proceed, the following is needed:**
- TFDA/regulatory package insert (warnings, contraindications) — DG001, Blocking
- DrugBank-sourced mechanism of action and original indication confirmation — DG002
- A widened literature/clinical-trial search using glaucoma-specific synonyms, since methazolamide's established ocular use suggests the current 0-result query may be missing existing evidence
- Note: two other TxGNN candidates for this drug (congestive heart failure — 6 supporting papers, preclinical/review only; acute pulmonary heart disease — no evidence, recommendation Hold) exist in this evidence pack but are outside the scope of this single-indication report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

