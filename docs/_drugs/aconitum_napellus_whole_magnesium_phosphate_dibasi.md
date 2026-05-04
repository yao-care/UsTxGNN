---
layout: default
title: Aconitum Napellus Whole Magnesium Phosphate Dibasi
parent: 僅模型預測 (L5)
nav_order: 142
evidence_level: L5
indication_count: 0
---

# Aconitum Napellus Whole Magnesium Phosphate Dibasi
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

# Multi-Component Botanical Formula (Aconitum / Viscum / Toxicodendron): Insufficient Data for Repurposing Analysis

## One-Sentence Summary

This candidate is a six-component botanical/homeopathic combination containing *Aconitum napellus*, *Magnesium phosphate*, *Pseudognaphalium obtusifolium*, *Rhododendron tomentosum*, *Toxicodendron pubescens*, and *Viscum album*.
The TxGNN pipeline returned **no predicted indications** for this compound, most likely because the multi-ingredient string could not be resolved to any DrugBank entry or knowledge-graph node.
Without a DrugBank ID, MOA data, or regulatory approval in any surveyed market, no repurposing analysis can be performed at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | None on record |
| Predicted New Indication | None (TxGNN returned no candidates) |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — model prediction only, no actual studies linked to this combined entity |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN prediction is available for this candidate; therefore, a mechanism-based rationale cannot be constructed from the evidence pack.

For context, the six named components suggest a **homeopathic or phytotherapy combination**:

- **Aconitum napellus** and **Toxicodendron pubescens** are classic homeopathic source materials used in highly diluted preparations (historically associated with pain and inflammatory conditions).
- **Viscum album** (European mistletoe) has a published oncology literature under the trade name Iscador / Helixor, typically used as an immunomodulatory adjunct.
- **Rhododendron tomentosum** and **Pseudognaphalium obtusifolium** are traditional herbal ingredients with limited modern pharmacological characterisation.
- **Magnesium phosphate** is a homeopathic mineral (Schüssler salt no. 7) associated with muscle cramps and neuralgia.

Because TxGNN's knowledge graph operates on individual DrugBank-mapped molecules, it cannot score combinations of botanical extracts that lack a unified identifier. The pipeline failure is structural, not a negative prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this combined entity.

---

## Literature Evidence

Currently no related literature available for this combined entity.

---

## US Market Information

No US (FDA) authorisations found for this multi-component formula.

---

## Safety Considerations

All safety fields returned no data for this candidate. Given that two of the six ingredients — *Aconitum napellus* and *Toxicodendron pubescens* — are derived from acutely toxic plants, the following general cautions apply even before formal package insert review:

- **Aconitum napellus**: source of aconitine; cardiotoxic and neurotoxic at non-homeopathic doses. Narrow therapeutic index.
- **Toxicodendron pubescens**: source of urushiol; potent contact allergen; systemic sensitisation risk.
- **Viscum album**: lectins and viscotoxins present; immunostimulant activity may interact with immunosuppressants.

Please refer to the respective component package inserts and homeopathic pharmacopoeia monographs before any clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The multi-ingredient botanical string could not be resolved to a DrugBank node, so TxGNN produced zero predictions and no evidence linkage is possible. The candidate therefore cannot clear the minimum threshold for repurposing evaluation.

**To proceed, the following is needed:**

1. **Identifier resolution** — Determine whether a single DrugBank ID or a compound-level FHIR identifier can represent this combination (e.g., if the product is a known marketed homeopathic brand such as a Boiron or Heel product, obtain its mapped ID).
2. **MOA data per ingredient** — Query DrugBank individually for each of the six components (especially Viscum album lectin, aconitine, and urushiol) to support a component-level mechanism analysis.
3. **Regulatory status clarification** — Confirm whether any US, EU, or Asia-Pacific homeopathic product licence exists for this exact formula, to populate the safety and indication fields.
4. **Safety review** — Download and parse the full prescribing information or homeopathic product dossier before re-entering the TxGNN pipeline (blocking gap DG001).
5. **Re-run TxGNN per component** — If the combination cannot be unified, run individual predictions for the pharmacologically active ingredients (Viscum album extract, Aconitum alkaloids) and aggregate results.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

