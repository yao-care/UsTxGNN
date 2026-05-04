---
layout: default
title: Aconitum Napellus Whole Asclepias Tuberosa Floweri
parent: 僅模型預測 (L5)
nav_order: 130
evidence_level: L5
indication_count: 0
---

# Aconitum Napellus Whole Asclepias Tuberosa Floweri
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

# Aconitum Napellus Complex (Multi-Component Formula): Insufficient Data for Repurposing Prediction

---

## One-Sentence Summary

This submission concerns a 10-component botanical/homeopathic mixture (including *Aconitum napellus*, *Filipendula ulmaria*, *Pulsatilla montana*, and others) with no registered indications in Taiwan and no DrugBank identifier.
The TxGNN model was **unable to generate repurposing predictions** for this entry, most likely because multi-component complex formulas cannot be mapped to a single drug node in the knowledge graph.
As a result, **no clinical trial or literature evidence** was retrieved, and a formal repurposing assessment cannot be completed at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (no Taiwan registration) |
| Predicted New Indication | None (TxGNN returned no predictions) |
| TxGNN Prediction Score | N/A |
| Evidence Level | Below L5 — model produced no output |
| US Market Status | 未上市 (Not marketed) |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Was Generated

TxGNN operates on individual drug entities mapped to DrugBank IDs. This submission contains **10 distinct botanical/chemical components** listed as a single drug string, none of which could be resolved to a DrugBank ID as a unified entity. As a result:

1. **No knowledge graph node exists** for this multi-component formula, preventing any graph traversal or link-prediction step.
2. **MOA data is unavailable** — the mechanism of action for the combined formula has not been characterised.
3. Without a resolvable drug node, neither the KG-based nor the deep-learning branch of TxGNN can score candidate disease associations.

The individual ingredients suggest a traditional use profile oriented toward pain and inflammation (e.g., *Filipendula ulmaria* as a source of salicylates; *Aconitum napellus* for neuralgia; *Lithium benzoate* historically for gout), but this cannot be formalised into a prediction without decomposing the formula.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note**: Several individual ingredients in this formula carry well-known safety signals that warrant independent review before any clinical use:
> - *Aconitum napellus* (monkshood) is highly toxic; aconitine has a narrow therapeutic index.
> - *Euphorbia resinifera* resin (resiniferatoxin source) is a potent TRPV1 agonist.
> - *Rhododendron tomentosum* contains grayanotoxins.
>
> A component-level safety review is strongly recommended even if regulatory data for the combined formula is absent.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
TxGNN requires a single mappable drug entity (DrugBank ID) to generate repurposing candidates; this multi-component formula could not be resolved, leaving zero predictions and zero supporting evidence.

**To proceed, the following is needed:**

- **Decompose the formula**: Evaluate each of the 10 components individually through TxGNN to identify which ingredient(s) drive any therapeutic signal.
- **Identify the lead compound**: Determine whether one active ingredient (e.g., methyl salicylate from *Filipendula ulmaria*, or aconitine from *Aconitum napellus*) is the primary pharmacological agent and re-run prediction under that entity.
- **Obtain a DrugBank ID**: If the formula is marketed elsewhere under a single product name, locate the corresponding DrugBank or ChEMBL entry.
- **Component-level safety audit**: Given the toxicity profile of several ingredients (especially *Aconitum napellus* and *Euphorbia resinifera*), a preclinical safety assessment is prerequisite to any repurposing attempt.
- **Clarify regulatory identity**: Confirm whether this is a registered homeopathic preparation in any jurisdiction, which may provide indication language and safety precedent.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

