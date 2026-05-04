---
layout: default
title: Aconitum Napellus Whole Fagopyrum Esculentum Whole
parent: 僅模型預測 (L5)
nav_order: 141
evidence_level: L5
indication_count: 0
---

# Aconitum Napellus Whole Fagopyrum Esculentum Whole
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

# Complex Multi-Ingredient Homeopathic Formula: Insufficient Data for Repurposing Evaluation

## One-Sentence Summary

This product is a complex multi-ingredient formula composed of 15 botanical, homeopathic, and viral antigen components — including *Aconitum napellus*, multiple human herpesvirus antigens (HSV-1/2, VZV, EBV, CMV), and *Glycyrrhiza glabra* — with no registered indication on record.
The TxGNN model **could not generate any repurposing prediction** for this compound, as no DrugBank ID could be matched for the mixture.
There is **no clinical trial or publication evidence** linked to this formulation through the current pipeline.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Unknown — no licensed indication on record |
| Predicted New Indication | None — TxGNN returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (model prediction only — in this case, no prediction was generated) |
| US Market Status | Not marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN repurposing prediction was generated for this compound. The pipeline requires a valid DrugBank ID to anchor a candidate within the TxGNN knowledge graph; because this multi-ingredient formula lacks a DrugBank mapping, the model returned an empty result set.

The formula appears to be a **homeopathic combination product**. Its ingredients follow a classic homeopathic paradigm: *Aconitum napellus* (acute inflammatory states), *Ranunculus bulbosus* and *Toxicodendron pubescens* (dermatological and neuralgic symptoms), *Sepia officinalis* (hormonal/visceral complaints), and *Solanum dulcamara* (cold/damp aggravation). The inclusion of attenuated human herpesvirus antigens (HSV-1, HSV-2, VZV, EBV, CMV) and adenovirus antigen suggests the product may target viral or post-viral symptom complexes.

Because homeopathic combination products are formulated at ultra-dilute concentrations, conventional pharmacological mechanism-of-action analysis and knowledge-graph-based drug repurposing methods are not applicable without further characterisation of the active fractions. A repurposing evaluation would require reformulating the research question around individual bioactive components (e.g., glycyrrhizin from *Glycyrrhiza glabra*) rather than the mixture as a whole.

---

## Safety Considerations

No safety data — including warnings, contraindications, or drug-drug interactions — were retrievable through the current pipeline for this formula. Individual ingredients carry known safety considerations that should be reviewed before any clinical application:

- **Aconitum napellus** contains aconitine alkaloids, which are cardiotoxic and neurotoxic at pharmacological doses.
- **Toxicodendron pubescens** contains urushiol, a potent contact allergen.
- **Sodium hypochlorite** is an oxidising agent with mucosal irritation potential.

> Please refer to the product's package insert and individual ingredient monographs for full safety information before any clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline could not evaluate this candidate because the multi-ingredient homeopathic formula has no DrugBank ID and no existing licensed indication, leaving the model without an entry point into the knowledge graph. Without a prediction, no repurposing hypothesis can be assessed.

**To proceed, the following is needed:**

- Identify whether any single active component (e.g., glycyrrhizin, aconite alkaloids) can be isolated as the primary repurposing candidate and mapped to a DrugBank node
- Clarify the regulatory classification of this product in its country of origin (homeopathic drug vs. biological vs. combination drug)
- Obtain the original manufacturer's package insert to establish approved indications and safety profile
- If the antiviral antigen components are of primary interest, redirect the evaluation to the individual herpesvirus antigens or consider an immunological mechanism pathway separately from the botanical components
- Re-run the TxGNN pipeline against each decomposed active ingredient before attempting a combined evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

