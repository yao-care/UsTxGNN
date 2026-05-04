---
layout: default
title: Activated Charcoal American Ginseng Aviscumine Gal
parent: 僅模型預測 (L5)
nav_order: 172
evidence_level: L5
indication_count: 0
---

# Activated Charcoal American Ginseng Aviscumine Gal
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# ACTIVATED CHARCOAL / AMERICAN GINSENG / AVISCUMINE / GALIUM APARINE / GERMANIUM / SELENIUM / UBIDECARENONE: Insufficient Evidence for Repurposing Evaluation

## One-Sentence Summary

This candidate is a seven-component mixture—combining activated charcoal, American ginseng, aviscumine (mistletoe lectin), Galium aparine, germanium, selenium, and ubidecarenone (CoQ10)—none of which are individually or collectively registered in the Taiwanese market.
The TxGNN model returned **no predicted indications** for this combination, and neither clinical trial evidence nor published literature was retrieved to support any repurposing direction.
As a result, a full evidence-based evaluation cannot be completed at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not established (no regulatory filings found) |
| Predicted New Indication | None — TxGNN returned no candidates |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (model prediction only — and none was generated) |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN prediction was generated for this candidate, so there is no predicted indication to evaluate for mechanistic plausibility.

The combination contains components with heterogeneous pharmacological profiles: activated charcoal is primarily an adsorbent used in acute poisoning; ubidecarenone (CoQ10) is a mitochondrial cofactor; selenium is a trace element antioxidant; American ginseng and Galium aparine are botanical extracts; aviscumine is a recombinant mistletoe lectin with reported immunomodulatory and cytotoxic activity; and germanium (as an organic compound) has been investigated peripherally for immune effects. Because each component has a distinct mechanism and the combination has no established clinical indication, the TxGNN knowledge graph cannot anchor this mixture to a disease node—resulting in zero candidates.

Currently, detailed mechanism of action data is not available for this combination as a whole. Without a unified MOA, regulatory anchor, or at least one predicted indication, mechanistic applicability to any new indication cannot be assessed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model produced no repurposing candidates for this seven-component mixture, and the combination holds no regulatory approvals in any queried jurisdiction. Without a predicted indication, there is no hypothesis to test.

**To proceed, the following is needed:**

- **Decompose the query**: Run TxGNN separately for each individual active ingredient (e.g., aviscumine, ubidecarenone, selenium) rather than as a concatenated string; the pipeline likely failed to map the compound string to any single DrugBank node.
- **Establish a lead component**: Identify which ingredient (most likely aviscumine or ubidecarenone, both of which have DrugBank entries) is the primary therapeutic candidate and re-run the Evidence Pack for that single INN.
- **Clarify the product identity**: Determine whether this combination is a finished pharmaceutical product, a compounded formulation, or a dietary supplement, as this determines which regulatory and safety frameworks apply.
- **MOA data**: Once a lead component is identified, retrieve mechanism of action from DrugBank API (remediation already flagged as DG002).
- **Safety baseline**: Download the relevant package insert or regulatory monograph to address DG001 before any safety screening is attempted.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

