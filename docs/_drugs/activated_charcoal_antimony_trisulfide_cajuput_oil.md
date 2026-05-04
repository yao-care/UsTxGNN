---
layout: default
title: Activated Charcoal Antimony Trisulfide Cajuput Oil
parent: 僅模型預測 (L5)
nav_order: 189
evidence_level: L5
indication_count: 0
---

# Activated Charcoal Antimony Trisulfide Cajuput Oil
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

# Activated Charcoal Compound (7-Component Mixture): No TxGNN Prediction Generated — Candidate Unresolvable

## One-Sentence Summary

This submission is a 7-component mixture — Activated Charcoal, Antimony Trisulfide, Cajuput Oil, Lycopodium Clavatum Spore, Pulsatilla Vulgaris, Silver Nitrate, and Strychnos Nux-Vomica Seed — with no US market approval and no original indication on record. The TxGNN pipeline was unable to generate any repurposing predictions for this candidate, as the combination could not be mapped to a DrugBank entity. No clinical or literature evidence is available to support evaluation at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available |
| Predicted New Indication | None generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — no prediction generated |
| US Market Status | Not marketed (0 NDAs) |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why This Candidate Cannot Be Evaluated

This submission presents a 7-component mixture combining conventional pharmaceutical substances (Activated Charcoal, Silver Nitrate, Cajuput Oil) with traditional/homeopathic ingredients (Lycopodium Clavatum Spore, Pulsatilla Vulgaris, Strychnos Nux-Vomica Seed, Antimony Trisulfide). The ingredient profile is characteristic of a homeopathic compounding formula, and several structural barriers prevent standard TxGNN evaluation:

**No DrugBank ID could be assigned.** The TxGNN knowledge graph pipeline requires each candidate to be anchored to a single DrugBank entity. A 7-component mixture with no unified registration cannot be resolved into a single node in the graph, so no prediction scores were produced.

**No original indication is on record.** Without a defined therapeutic use, there is no clinical anchor from which to extrapolate mechanism-based repurposing hypotheses. The TFDA query returned zero results, confirming this combination has never received a formal drug approval in any reviewed jurisdiction.

**Homeopathic formulations fall outside TxGNN's data assumptions.** Pulsatilla Vulgaris, Nux Vomica (Strychnos), and Lycopodium are classical homeopathic remedies used at highly diluted concentrations. Such preparations typically lack the pharmacokinetic profiles and receptor-level mechanism data required for knowledge graph traversal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note on Strychnos Nux-Vomica Seed:** This ingredient contains strychnine and brucine, which are potent alkaloids with a narrow therapeutic index and known CNS/neuromuscular toxicity. Even in compounded or homeopathic preparations, the presence of this ingredient warrants careful regulatory and safety review before any repurposing work is initiated.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline returned zero predicted indications because the candidate is a multi-component mixture that cannot be mapped to a DrugBank entity and has no recorded regulatory history. The minimum data requirements for a repurposing evaluation are not met.

**To proceed, the following is needed:**

- **Disaggregate the components:** Submit each active ingredient (e.g., Activated Charcoal, Silver Nitrate) separately as individual candidates to enable DrugBank mapping and TxGNN scoring
- **Clarify formulation intent:** Confirm whether this is a homeopathic preparation — if so, a different evaluation framework (outside TxGNN's scope) should be applied
- **Obtain a DrugBank ID:** Required for any candidate to enter the KG prediction pipeline
- **Establish the original approved indication:** Retrieve the package insert (仿單) or any historical regulatory filing from TFDA, EMA, or FDA to establish a baseline clinical use
- **Safety baseline:** Download and parse the package insert PDF to fill the DG001 (warnings/contraindications) and DG002 (MOA) data gaps before any further analysis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

