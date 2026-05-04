---
layout: default
title: Acetaminophen
parent: 僅模型預測 (L5)
nav_order: 92
evidence_level: L5
indication_count: 1
---

# Acetaminophen
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

# Acetaminophen: Evidence Pack Incomplete — Repurposing Evaluation on Hold

## One-Sentence Summary

Acetaminophen (paracetamol, DB00316) is one of the most widely used analgesic and antipyretic agents globally, available in virtually every major market.
The current Evidence Pack contains **no TxGNN predicted indications** for this drug, and the Taiwan regulatory query returned zero records — almost certainly a data retrieval issue rather than true market absence.
A full repurposing evaluation cannot be completed until these critical gaps are resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in current Evidence Pack |
| Predicted New Indication | None — TxGNN returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A (no predictions to evaluate) |
| Taiwan Market Status | 未上市（資料品質疑慮，見下方說明） |
| Number of Licenses | 0 |
| Recommended Decision | **Hold** |

> **⚠️ Note on Taiwan Market Status**: Acetaminophen is a foundational OTC and prescription drug distributed throughout Taiwan under dozens of brand names (e.g., Panadol, Tylenol, and extensive generics). A TFDA query returning 0 results is almost certainly a search parameter mismatch — the TFDA database may index this drug under **"Paracetamol"**、**「乙醯氨酚」**、**「乙醯胺酚」** or individual brand names. This must be re-queried before any regulatory conclusion is drawn.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack is missing two blocking inputs — TxGNN predicted indications and Taiwan regulatory records — making it impossible to evaluate any repurposing hypothesis, conduct a mechanism analysis, or complete a safety pre-screen. No evaluation sections can be populated in good faith.

**To proceed, the following is needed:**

- **Re-run TFDA query** using alternative search terms: `Paracetamol`、`乙醯氨酚`、`乙醯胺酚`、`普拿疼` (brand), and wildcard on ingredient field
- **Resolve TxGNN output gap**: Confirm whether the prediction pipeline produced candidates for DB00316; if the model returned no results, document the reason (e.g., drug not present in KG, below score threshold, or pipeline error)
- **Retrieve MOA from DrugBank API** (DB00316) to support future mechanism analysis
- **Download TFDA package insert PDF** and extract warnings, contraindications, and special population precautions to clear DG001 (Blocking severity)
- **Re-run Evidence Pack generation** after above gaps are resolved before proceeding to repurposing evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

