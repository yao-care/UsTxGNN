---
layout: default
title: Acorus Calamus Whole Citrullus Colocynthis Fruit P
parent: 僅模型預測 (L5)
nav_order: 143
evidence_level: L5
indication_count: 0
---

# Acorus Calamus Whole Citrullus Colocynthis Fruit P
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

# Multi-Ingredient Botanical Complex: Insufficient Data for Repurposing Analysis

## One-Sentence Summary

This entry represents a complex 10-ingredient botanical/herbal combination — including *Colchicum autumnale* bulb, Comfrey root, and Potassium iodide — that holds no US market authorization and carries no DrugBank identifier.
The TxGNN model was unable to generate any repurposing predictions for this combination, as the multi-component mixture cannot be mapped to a unified drug identity in the knowledge graph.
Without a matched DrugBank entry or approved indication, no evidence-supported new indication can be proposed at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indications on record |
| Predicted New Indication | No prediction generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | Below L5 — model prediction not generated |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Safety Considerations

Although structured safety data is unavailable for this combination as a whole, several individual ingredients carry well-documented regulatory concerns that warrant attention before any further evaluation:

- **Colchicum autumnale bulb** contains colchicine alkaloids with a narrow therapeutic index; overdose can be life-threatening.
- **Comfrey root** (*Symphytum officinale*) contains pyrrolizidine alkaloids (PAs), classified as hepatotoxic and potentially carcinogenic. Oral use is banned or severely restricted in multiple jurisdictions (US FDA, EU, Germany BfR).
- **Toxicodendron pubescens leaf** (poison oak) can cause severe contact dermatitis; systemic toxicity risk must be evaluated for any non-topical route.
- **Citrullus colocynthis** is a potent cathartic with reports of hemorrhagic colitis and renal toxicity.
- **Potassium iodide** has documented interactions with thyroid function and certain cardiac medications.

A formal ingredient-by-ingredient toxicological review and drug interaction screening is required before this combination can proceed to any efficacy evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This 10-ingredient botanical combination cannot be processed by the TxGNN model due to the absence of a unified DrugBank entry, and no original or predicted indication exists to anchor a repurposing hypothesis. Several individual ingredients have known serious safety signals that must be resolved before efficacy work can begin.

**To proceed, the following is needed:**

- **Identity resolution**: Determine whether this combination corresponds to a registered product (e.g., homeopathic, traditional medicine, or compounded formulation) and obtain a product-level identifier.
- **DrugBank mapping**: Attempt individual-ingredient DrugBank lookups for components with known drug activity (e.g., colchicine from *Colchicum autumnale*, potassium iodide), then evaluate whether a single active ingredient can serve as the repurposing anchor.
- **Safety pre-screen**: Conduct a formal PA (pyrrolizidine alkaloid) safety assessment for Comfrey root and a colchicine toxicity review before any clinical translation is considered.
- **Regulatory status clarification**: Confirm whether this combination is intended as a homeopathic product, herbal supplement, or conventional drug formulation, as the regulatory pathway and evidence standards differ significantly.
- **Re-run TxGNN**: Once a primary active ingredient is identified and mapped, resubmit as a single-ingredient query to obtain a prediction score and disease ranking.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

