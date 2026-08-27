---
layout: default
title: Lubiprostone
parent: 僅模型預測 (L5)
nav_order: 875
evidence_level: L5
indication_count: 10
---

# Lubiprostone
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

# Lubiprostone: From an Unspecified Original Indication to Predicted Alopecia

## One-Sentence Summary

> Lubiprostone (DrugBank ID: DB01046) is a chloride-channel/EP4-receptor active compound whose original approved indication is not documented in the current evidence pack.
> The TxGNN model predicts it may be effective for **Alopecia**, with a prediction score of **99.93%**, but currently **no supporting clinical trials or literature**, and the evidence pack's own mechanistic review finds no known biological pathway linking lubiprostone to hair growth.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (data gap — see DG002) |
| Predicted New Indication | Alopecia |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed, structured mechanism-of-action data for lubiprostone is marked as a data gap (DG002, High severity) in this evidence pack. However, the rationale attached to the predicted indications does describe lubiprostone's known pharmacology: it is a prostaglandin E1 (PGE1) derivative that activates the intestinal epithelial ClC-2 chloride channel and the EP4 receptor, promoting intestinal fluid secretion — a mechanism associated with gastrointestinal motility/secretion, though the specific original indication itself is not recorded in this pack.

The predicted new indication, alopecia, involves hair follicle growth regulation. The evidence pack's own mechanistic assessment explicitly states that this pathway is **not** shared with lubiprostone's known activity: hair growth effects seen with other prostaglandin analogs (e.g., bimatoprost, latanoprost) act through the FP receptor subtype, not EP4, and lubiprostone has minimal systemic absorption, limiting any plausible action outside the gut. The rationale text characterizes this specifically as "a high TxGNN score prediction without mechanistic support."

Given this explicit absence of mechanistic plausibility, combined with zero clinical trials and zero literature for this drug-disease pair, this candidate represents a pure statistical/embedding-similarity association from the model (Evidence Level L5) rather than a biologically grounded hypothesis. The same pattern (high score, no mechanism, no evidence) recurs across the other top-ranked predictions for this drug (hypotrichosis, alopecia areata, etc.), reinforcing that this is likely a model-embedding cluster effect rather than a genuine signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Lubiprostone currently has no recorded authorizations in this evidence pack (0 licenses; market status: not marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The alopecia prediction has no clinical trial or literature support, and the evidence pack's own rationale explicitly finds no mechanistic link between lubiprostone's known ClC-2/EP4 activity and hair follicle biology. Evidence level is L5 (model prediction only), and the drug currently has no market presence to leverage for rapid evaluation.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001, Blocking — required before any safety pre-assessment, S1)
- Confirmed original indication and mechanism-of-action data for lubiprostone (DG002, High)
- Preclinical or mechanistic studies specifically testing lubiprostone in dermatology/hair-growth models, given the current absence of any such link
- Re-evaluation of lower-ranked predictions in this candidate set (e.g., pulmonary hypertension, rank 5) which carry a weaker but non-zero mechanistic rationale (shared prostaglandin-receptor pathway family) and one loosely related trial record, should this drug be revisited
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

