---
layout: default
title: Pilocarpine
parent: 僅模型預測 (L5)
nav_order: 1044
evidence_level: L5
indication_count: 1
---

# Pilocarpine
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

# Pilocarpine: From Unrecorded Original Indication to Primary Hereditary Glaucoma

## One-Sentence Summary

> No original indication or licensing data is on file for Pilocarpine (DrugBank DB01085) in this dataset, and the drug is currently not marketed in this jurisdiction.
> The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma**, with a prediction score of **99.83%**,
> but **no clinical trials or literature** currently support this direction — the signal is model-only at this stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No records available (no license or indication data on file) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.83% (rank 4905) |
| Evidence Level | L5 (model prediction only, no supporting trials/literature) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, no structured mechanism of action (MOA) data is on file for this drug. However, the model's own repurposing rationale draws on established pharmacology: Pilocarpine is a muscarinic (M3) receptor agonist acting on the ciliary muscle and iris sphincter. It induces miosis and increases aqueous humor outflow through the trabecular meshwork — the classic pharmacological mechanism for lowering intraocular pressure.

This mechanism maps directly onto glaucoma pathophysiology, where impaired aqueous humor drainage raises intraocular pressure. Notably, pilocarpine is historically a well-established miotic agent used in glaucoma management, so this "predicted new indication" largely reflects a long-standing, mechanistically mature use rather than a novel therapeutic hypothesis. That said, this dataset contains no original indication, license, or literature records to formally substantiate that history — it is asserted only through the model's mechanistic rationale field, not through verifiable regulatory or bibliographic evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but evidence level is L5 — no clinical trials, no literature, and no verified original-indication or MOA documentation exist in this dataset to corroborate the model's mechanistic rationale. A blocking data gap (missing TFDA/label warnings and contraindications) also prevents any safety pre-screening (S1).

**To proceed, the following is needed:**
- TFDA (or equivalent) label warnings and contraindications — currently blocking safety review
- Verified mechanism of action (MOA) documentation from DrugBank or equivalent source
- Confirmed original indication(s) and licensing history for this drug
- At least preliminary clinical or literature evidence directly linking pilocarpine to glaucoma treatment, to move the evidence level beyond L5
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

