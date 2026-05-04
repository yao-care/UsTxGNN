---
layout: default
title: Activated Charcoal Antimony Trisulfide Bismuth Sub
parent: 僅模型預測 (L5)
nav_order: 188
evidence_level: L5
indication_count: 0
---

# Activated Charcoal Antimony Trisulfide Bismuth Sub
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

# Multi-Component Preparation (15 Ingredients): Insufficient Data for Repurposing Evaluation

## One-Sentence Summary

This submission contains a 15-ingredient multi-component preparation (including Activated Charcoal, Dopamine, Human Epidermal Growth Factor, Silver Nitrate, and various botanical/animal-derived substances) with no established regulatory indication and no DrugBank identifier.

The TxGNN model returned **no repurposing predictions** for this compound, and no clinical trials or literature evidence are available.

This evaluation cannot proceed beyond the data-gathering stage without first resolving the identity and regulatory status of this preparation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Unknown — no regulatory records found |
| Predicted New Indication | None — TxGNN returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (model prediction only — and even this is absent) |
| Market Status | Not marketed (0 authorizations) |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Is Available

The 15-ingredient formula contains a highly heterogeneous mix of pharmacological categories:

- **Gastrointestinal agents**: Activated Charcoal, Bismuth Subnitrate, Ipecac, Sus Scrofa Stomach
- **Cardiovascular**: Dopamine
- **Growth factors / Wound healing**: Human Epidermal Growth Factor
- **Antimicrobials**: Silver Nitrate, Oregano, Semecarpus Anacardium Juice
- **Botanicals / Traditional medicine**: Dioscorea Villosa Root, Momordica Balsamina Immature Fruit, Picea Mariana Resin, Robinia Pseudoacacia Bark
- **Heavy metals / Minerals**: Antimony Trisulfide, Bismuth Subnitrate, Silver Nitrate
- **Animal-derived**: Sus Scrofa Stomach, Sus Scrofa Sympathetic Nerve

This combination resembles a homeopathic or traditional compound preparation rather than a single chemical entity. TxGNN is trained on single-agent DrugBank entries; without a DrugBank ID, the model cannot map this preparation to a node in the knowledge graph, which explains the absence of any prediction output.

Without a recognized mechanism of action or disease target, any repurposing analysis would be speculative.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: Several ingredients in this preparation carry known individual safety concerns that warrant attention even in the absence of formal DDI data:
> - **Ipecac**: use has been largely discontinued due to risk of cardiomyopathy and aspiration
> - **Antimony Trisulfide**: antimony compounds are nephrotoxic and hepatotoxic at systemic exposure
> - **Silver Nitrate**: caustic; systemic absorption risk (argyria)
> - **Semecarpus Anacardium**: contains urushiol-related allergens; contact sensitizer

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This preparation could not be evaluated because TxGNN produced no predictions, no regulatory authorization exists in any jurisdiction, and the multi-ingredient heterogeneous composition cannot be matched to a DrugBank knowledge graph entry. There is no evidence base (clinical trials or literature) linking this specific combination to any new indication.

**To proceed, the following is needed:**

1. **Drug identity resolution** — Determine whether this preparation has a recognized brand name, a pharmacopoeial monograph, or a homeopathic registration number; submit a single INN or a structured multi-ingredient NDA filing number
2. **Regulatory status clarification** — If this is a homeopathic or traditional medicine, document under which regulatory category (e.g., TFDA 中藥、成藥, or homeopathic exemption) it would be reviewed
3. **DrugBank mapping** — Identify the primary active component(s) for individual DrugBank lookup, enabling TxGNN to generate predictions on the lead molecule(s)
4. **MOA documentation** — Provide a proposed mechanism of action for the preparation's intended therapeutic effect; this is required before any repurposing rationale can be constructed
5. **Safety review** — Obtain or reconstruct a package insert for each active ingredient; several components (Ipecac, Antimony Trisulfide, Silver Nitrate) have well-documented toxicity profiles that must be formally assessed before any repurposing study is initiated
6. **Re-submit as single-agent candidates** — If repurposing evaluation is the goal, consider splitting the preparation and submitting each pharmacologically active ingredient (e.g., Dopamine, Human Epidermal Growth Factor) as separate Evidence Pack entries
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

