---
layout: default
title: Androctonus Australis Whole Calcium Fluoride Viscu
parent: 僅模型預測 (L5)
nav_order: 319
evidence_level: L5
indication_count: 0
---

# Androctonus Australis Whole Calcium Fluoride Viscu
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

# ANDROCTONUS AUSTRALIS WHOLE / CALCIUM FLUORIDE / VISCUM ALBUM WHOLE: No Baseline Indication — TxGNN Prediction Unavailable

## One-Sentence Summary

This submission comprises a three-component combination — *Androctonus australis* whole (North African scorpion extract), calcium fluoride, and *Viscum album* whole (mistletoe) — none of which carry an approved indication in the US market.
The TxGNN model returned **no predicted new indications** for this combination, and no supporting clinical trials or literature were identified.
With zero regulatory footprint and no model output, no repurposing evaluation can be completed at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indication on record |
| Predicted New Indication | None — TxGNN returned no candidates |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 (model prediction only — and none generated) |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why This Prediction Is Reasonable

No TxGNN predictions were generated for this compound combination, so a mechanistic repurposing rationale cannot be constructed.

For reference, the three components individually belong to complementary/anthroposophic medicine traditions:

- **Androctonus australis whole** is a scorpion venom preparation used in some homeopathic formulations; research into scorpion toxin–derived peptides for oncology and pain exists but remains preclinical.
- **Calcium fluoride** (Calcarea fluorica) is a Schüssler tissue salt used in homeopathic practice; no established pharmacological MOA is recognised in conventional medicine.
- **Viscum album whole** (mistletoe) is the best-studied of the three; its lectins (ML-I, ML-II, ML-III) have demonstrated immunomodulatory and cytotoxic activity in vitro, and it is used as adjuvant therapy in European integrative oncology (marketed as Iscador, Helixor, Lektinol). However, for this submission the components are listed together as a single undifferentiated entity without DrugBank mapping, preventing any structured graph-based prediction.

Until each active component is individually resolved to a DrugBank ID and linked to the TxGNN knowledge graph, model-based repurposing analysis cannot proceed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this specific combination.

---

## Literature Evidence

Currently no related literature available for this specific combination as a unified entity.

---

## US Market Information

This drug combination has no US market authorisations on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack contains no predicted indications, no regulatory history, no MOA data, and no safety information. The combination cannot be evaluated for repurposing potential until foundational data are obtained.

**To proceed, the following is needed:**

- **Component disambiguation**: Confirm whether this is a fixed-dose combination product or three separate entries. If a combination, obtain the product's brand name and formulation details.
- **DrugBank ID resolution**: Map each of the three components individually to DrugBank records so that the TxGNN knowledge graph can process them.
- **MOA data**: Retrieve mechanism-of-action data for each component (particularly *Viscum album* lectins, which have documented biological targets) via DrugBank API or literature review.
- **Indication clarification**: Determine the intended therapeutic area from the product's regulatory submission, prescribing information, or manufacturer documentation. *Viscum album*-based products are frequently used in oncology supportive care — confirming this would enable targeted evidence retrieval.
- **Safety package**: Download and parse the product's package insert (or equivalent regulatory document) to populate warnings, contraindications, and DDI fields.
- **TxGNN re-run**: Once DrugBank IDs are confirmed, re-submit individual components to the TxGNN pipeline to generate per-component predictions, then aggregate results at the combination level.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

