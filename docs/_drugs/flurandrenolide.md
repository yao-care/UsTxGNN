---
layout: default
title: Flurandrenolide
parent: 僅模型預測 (L5)
nav_order: 726
evidence_level: L5
indication_count: 10
---

# Flurandrenolide
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

# Flurandrenolide: From No Documented Indication to Vulvar Inverted Follicular Keratosis

## One-Sentence Summary

Flurandrenolide currently has no recorded approved indications, no US/Taiwan marketing licenses, and no verified mechanism-of-action data in this evidence pack. The TxGNN model's top-ranked prediction is **Vulvar Inverted Follicular Keratosis** (score **99.71%**), but this is supported by **0 clinical trials** and **0 publications**, and the model's own rationale states the mechanism does not plausibly fit this lesion type.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented (no approved indications on record; drug not currently marketed) |
| Predicted New Indication | Vulvar Inverted Follicular Keratosis |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for flurandrenolide is a confirmed data gap in this evidence pack. However, the model's own rationale text for other candidates in this list characterizes flurandrenolide as a **mid-potency topical corticosteroid with anti-inflammatory and immunomodulatory activity** — this is embedded evidence-pack context, not an external claim.

For the top-ranked prediction itself, this mechanism does not hold up: vulvar inverted follicular keratosis is a benign follicular epithelial proliferative lesion (tumor-like), not an inflammatory or immune-mediated condition. The pack's own repurposing rationale is explicit that a topical corticosteroid's anti-inflammatory mechanism has **no direct relevance** to this pathology, and no clinical or literature evidence exists to support it. This is why the associated decision stage is S0 with a "Hold" recommendation, despite the high raw TxGNN score.

By contrast, several lower-ranked but mechanistically stronger candidates appear in the same prediction set: lichen planus pigmentosus, hypertrophic lichen planus, annular atrophic lichen planus, lichen planus pemphigoides, alopecia areata, and alopecia mucinosa are all T-cell/immune-mediated inflammatory dermatoses for which topical or intralesional corticosteroids are an established treatment **class**. These are flagged as decision stage S1 ("Research Question") rather than S0, reflecting stronger class-effect biological plausibility — though still with zero drug-specific trial or literature evidence for flurandrenolide by name. A high TxGNN score alone does not guarantee mechanistic fit; in this case the rank-1 prediction is the weakest of the ten candidates on mechanistic grounds.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Flurandrenolide currently has no marketing authorizations on record (0 licenses; market status: Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: label warnings/contraindications and DDI data are both marked as data gaps in this evidence pack — see Conclusion for remediation.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (vulvar inverted follicular keratosis) has no clinical, literature, or credible mechanistic support — evidence level L5 with an explicit mechanistic mismatch noted in the model's own rationale. In addition, a **Blocking** data gap (TFDA label warnings/contraindications, DG001) prevents this candidate from even entering a preliminary S1 safety screen.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain TFDA label warnings/contraindications
- Resolve DG002 (High): confirm mechanism of action via DrugBank API
- If pursuing repurposing further, re-scope toward the lichen planus–spectrum candidates (ranks 2–4) or alopecia areata (rank 5), which carry stronger class-effect mechanistic rationale, and commission a targeted literature/trial search specific to flurandrenolide (not just the corticosteroid class) in those indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

