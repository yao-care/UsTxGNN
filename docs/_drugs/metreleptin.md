---
layout: default
title: Metreleptin
parent: 僅模型預測 (L5)
nav_order: 920
evidence_level: L5
indication_count: 10
---

# Metreleptin
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

# Metreleptin: From Lipodystrophy to Familial Generalized Lentiginosis

## One-Sentence Summary

> Metreleptin is a recombinant leptin analog; general drug knowledge indicates it is used to treat **lipodystrophy** (this indication is not documented in the current evidence pack — see note below).
> The TxGNN model's top prediction is **Familial Generalized Lentiginosis**, but this candidate — along with all 9 others in the current pack — has **zero supporting clinical trials and zero literature**, and the model's own rationale states there is no known mechanistic overlap with metreleptin's leptin-receptor pathway.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (`taiwan_regulatory.licenses` and `drug.original_indications` are both empty; metreleptin is generally known as a lipodystrophy treatment, but this is not sourced from this pack) |
| Predicted New Indication | Familial Generalized Lentiginosis |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 (model prediction only, no clinical or literature support) |
| US Market Status | Not Marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (`original_moa: [Data Gap]`). Based on general drug knowledge, metreleptin is a recombinant human leptin analog acting as a leptin receptor agonist, historically used to correct leptin deficiency in lipodystrophy syndromes.

However, the evidence pack's own mechanistic rationale for the top-ranked candidate, Familial Generalized Lentiginosis, explicitly states that this disease is a synonym for LEOPARD syndrome (a PTPN11/RAF1-driven RASopathy) and has **no known mechanistic overlap** with leptin receptor signaling. The same disconnect applies to ranks 2 and 3 (Gastrocutaneous syndrome, Moynahan syndrome — both also LEOPARD syndrome synonyms).

Across all 10 candidates in this pack, the model's rationale field consistently flags weak or absent mechanistic linkage — the closest candidates are rank 8 (a rare syndrome with acanthosis-nigricans-like lesions, tenuously linked via leptin's general association with insulin resistance) and rank 9 (adrenal adenoma, via a loosely described leptin–HPA axis interaction). Notably, rank 4 (rhabdoid tumor) carries a theoretical **safety concern**, since exogenous leptin may promote tumor growth in some preclinical models. Given this, the high TxGNN scores (all ≈99.5–99.7%) should be interpreted as statistical/embedding-space proximity rather than biologically validated repurposing signals.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| — | — | — | Not marketed (`market_status: 未上市`, 0 licenses on record) |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are all unavailable in this evidence pack; DDI query returned `not_found`.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 predicted indications are Evidence Level L5 with zero clinical trials and zero literature support, and the top-ranked candidate's own mechanistic rationale states no known biological link to metreleptin's mode of action. Combined with the drug's non-marketed status in this jurisdiction and missing MOA/safety documentation, there is no basis to advance beyond model prediction at this time.

**To proceed, the following is needed:**
- TFDA label / package insert (warnings, contraindications) — flagged as **Blocking** data gap (DG001)
- Verified mechanism of action data from DrugBank — flagged as **High** severity data gap (DG002)
- Original indication documentation (none currently on file for this jurisdiction)
- If pursued, preclinical/mechanistic studies specifically testing leptin-pathway relevance for the higher-plausibility candidates (rank 8: acanthosis-nigricans-like syndrome; rank 9: adrenal adenoma), given the top 3 candidates are mechanistically unrelated per the model's own rationale
- Safety evaluation of leptin-pathway activation in oncologic contexts before any consideration of rank 4 (rhabdoid tumor)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

