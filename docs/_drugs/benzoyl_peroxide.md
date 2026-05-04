---
layout: default
title: Benzoyl Peroxide
parent: 僅模型預測 (L5)
nav_order: 408
evidence_level: L5
indication_count: 4
---

# Benzoyl Peroxide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

Using the `txgnn-pipeline` skill to confirm project context. Now generating the evaluation report based on the Evidence Pack.

---

# Benzoyl Peroxide: From Acne Vulgaris to Vulvar Inverted Follicular Keratosis

## One-Sentence Summary

Benzoyl Peroxide (BPO) is a well-established topical antimicrobial and keratolytic agent, widely recognized for its use in acne vulgaris treatment, though it holds no formal regulatory approval in Taiwan.
The TxGNN model predicts it may have activity in **Vulvar Inverted Follicular Keratosis**, achieving a prediction score of 99.92%.
However, **no clinical trials and no publications** currently support this direction — placing this candidate at the lowest possible evidence tier (L5, model prediction only).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Taiwan; recognized global use for acne vulgaris |
| Predicted New Indication | Vulvar Inverted Follicular Keratosis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 (Model prediction only, no actual studies) |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Benzoyl Peroxide acts primarily by releasing free radical oxygen upon contact with skin, which kills *Cutibacterium acnes* and exerts keratolytic activity to help clear blocked follicles. These properties underpin its well-validated efficacy in inflammatory acne vulgaris.

Inverted follicular keratosis (IFK) is a benign squamous tumor arising from the hair follicle infundibulum, presenting as a solitary papule or nodule. The pipeline's own mechanistic rationale describes only a speculative "epidermal-follicular shared pathway" — the idea that BPO's keratolytic action on follicular epithelium might be loosely relevant to a follicle-origin lesion. Critically, there are **no structural mechanistic papers** connecting BPO to IFK suppression or regression, and the "vulvar" anatomical qualifier adds a further layer of implausibility: no biological rationale supports why BPO would specifically act on vulvar IFK, a rare benign lesion that is typically managed surgically.

In short, the high TxGNN score likely reflects shared Knowledge Graph nodes in the "skin / follicular / keratosis" neighborhood, rather than any true pharmacological relationship. The prediction does not currently translate into a scientifically defensible hypothesis for clinical development.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate is backed solely by a TxGNN model prediction (L5) with zero supporting clinical or preclinical evidence, and the pipeline's own mechanistic review explicitly characterizes the mechanistic link as "extremely weak with no structural support." The specific vulvar anatomical target also raises unanswered tolerability questions that would need to be resolved before any further work is justified.

**To proceed, the following would be needed:**
- Retrieval of BPO's full mechanism of action data from DrugBank (currently a data gap)
- Taiwan / US regulatory label to identify approved indications, key warnings, and contraindications
- At least one peer-reviewed preclinical or mechanistic study connecting BPO activity to inverted follicular keratosis biology
- A safety assessment specifically addressing topical BPO application to vulvar mucosa (irritation, sensitization, mucosal absorption risks)
- Clarification of whether IFK at the vulvar site is expected to respond to topical keratolytic therapy at all, given that surgical excision is the standard of care
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

