---
layout: default
title: Activated Charcoal Antimony Trisulfide Asafetida C
parent: 僅模型預測 (L5)
nav_order: 187
evidence_level: L5
indication_count: 0
---

# Activated Charcoal Antimony Trisulfide Asafetida C
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

# Multi-Ingredient Herbal Compound: TxGNN Repurposing Analysis Inconclusive

## One-Sentence Summary

This submission contains a seven-ingredient mixture (Activated Charcoal, Antimony Trisulfide, Asafetida, Chelidonium majus, Goldenseal, Nutmeg, and Ptelea trifoliata bark) with no established regulatory record in Taiwan or the US.
The TxGNN model was unable to generate repurposing predictions for this compound combination, as no DrugBank identifier could be resolved and no original indications were available to anchor the analysis.
Without a prediction target, evidence-level assessment and decision recommendation cannot be completed in the current cycle.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not established (no regulatory record found) |
| Predicted New Indication | No predictions generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — prerequisites not met |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Was Generated

The TxGNN model requires a resolvable DrugBank ID to position a drug within the knowledge graph and compute disease association scores. For this submission, three systemic barriers prevented prediction:

1. **Multi-ingredient mixture without a unified DrugBank entry.** The seven components span herbal botanicals (Chelidonium majus, Goldenseal, Asafetida, Ptelea trifoliata bark, Nutmeg), a mineral compound (Antimony Trisulfide), and a non-specific adsorbent (Activated Charcoal). This combination does not correspond to any single DrugBank node, and the pipeline returned `drugbank_id: null`.

2. **No original indication to establish a repurposing baseline.** TxGNN's repurposing logic anchors on a drug's known therapeutic context. Without an approved indication, the model cannot compute meaningful displacement scores toward new disease nodes.

3. **Regulatory absence.** The compound has zero TFDA licenses and is not marketed in Taiwan or the US. There is no approved labeling from which to infer therapeutic intent.

Currently, detailed mechanism of action data is not available. Based on known pharmacology at the component level, Activated Charcoal is an adsorption agent used in acute poisoning and GI decontamination; Goldenseal (berberine-containing) has antimicrobial and anti-inflammatory properties; Chelidonium majus is used in traditional medicine for liver and biliary complaints. However, these individual MOAs cannot be combined into a coherent multi-target profile without a formalized DrugBank or pharmacological model entry.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note on Antimony Trisulfide:** Antimony compounds as a class carry toxicity concerns (cardiac, hepatic, renal). If this compound proceeds to any regulatory pathway, specific safety data for the antimony-containing component should be prioritized.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline cannot generate a repurposing prediction without a resolvable DrugBank ID and at least one established indication. This is a structural data gap, not a marginal evidence gap — the evaluation cannot proceed in its current form.

**To proceed, the following is needed:**

- **DrugBank resolution:** Determine whether any of the seven ingredients individually holds a DrugBank entry, or whether the mixture exists as a combination product in any pharmacopeia. If so, re-run the pipeline against the primary active ingredient.
- **Indication clarification:** Obtain historical or traditional-use documentation to establish what condition this compound has been used to treat. This anchors the repurposing baseline.
- **Regulatory filing review:** Identify whether this mixture has ever held any approval (US, EU, Japan, or traditional medicine classification) that could provide a labeling reference.
- **Safety data for antimony component:** Antimony Trisulfide safety profile should be assessed independently before any further evaluation.
- **Component-level analysis (fallback):** If the mixture cannot be unified into a single DrugBank node, consider running TxGNN separately on each resolvable ingredient (e.g., Goldenseal → berberine, Nutmeg → myristicin) and aggregating predictions.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

