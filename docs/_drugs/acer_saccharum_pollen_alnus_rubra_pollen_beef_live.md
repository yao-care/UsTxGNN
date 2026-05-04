---
layout: default
title: Acer Saccharum Pollen Alnus Rubra Pollen Beef Live
parent: 僅模型預測 (L5)
nav_order: 79
evidence_level: L5
indication_count: 0
---

# Acer Saccharum Pollen Alnus Rubra Pollen Beef Live
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

# Multi-Allergen Extract Mixture: Evaluation Report

> **Notice:** This Evidence Pack contains no TxGNN predicted indications. This report documents the data status and provides recommendations for the next steps before a repurposing evaluation can be conducted.

---

## One-Sentence Summary

This candidate consists of an 18-component allergen/biological mixture — including multiple tree pollens, bovine-derived materials, corticotropin, and histamine dihydrochloride — which is characteristic of allergy immunotherapy or diagnostic scratch-test preparations.
The TxGNN model returned **no predicted indications** for this candidate, and the drug has **no registered licenses** in Taiwan.
Without a DrugBank ID or predicted indications, a full repurposing evaluation cannot be completed at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Drug Name (INN) | 18-component allergen mixture (pollen extracts, bovine materials, corticotropin, histamine dihydrochloride) |
| DrugBank ID | Not assigned |
| Original Indication | Not available |
| Predicted New Indication | No prediction generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (model prediction only) — effectively **not evaluable** |
| Taiwan Market Status | Not marketed (0 licenses) |
| Recommended Decision | **Hold** |

---

## Why This Case Cannot Be Evaluated Yet

This candidate is a complex multi-component mixture containing 18 distinct ingredients, including:

- **Tree pollens** (maple, red alder, birch, hazel, European beech, ash, Virginia juniper, London plane, white poplar, English oak, crack willow, elderflower, American elm)
- **Animal-derived biologicals** (beef liver, bovine adrenal gland)
- **Pharmacological reference substances** (corticotropin/ACTH, histamine dihydrochloride)

Mixtures of this type are typically found in **allergy immunotherapy preparations** (allergen desensitisation vaccines) or **allergen diagnostic panels** used for skin-prick testing. In either case, the "drug" is not a single molecular entity, and standard drug repurposing models like TxGNN — which operate on single-drug nodes in a biomedical knowledge graph — are not designed to process composite allergen extracts.

The absence of a DrugBank ID confirms that this mixture was not resolved to any node in the TxGNN knowledge graph, which explains why no predicted indications were generated.

---

## Data Gaps Blocking Evaluation

The following gaps must be resolved before evaluation can proceed:

| Gap ID | Item | Severity | Impact | Recommended Action |
|--------|------|----------|--------|--------------------|
| DG001 | Package insert warnings / contraindications | Blocking | Cannot complete safety pre-screen | Download PDF from TFDA website |
| DG002 | Mechanism of action (MOA) | High | Cannot perform mechanistic relevance analysis | Query DrugBank API for each active component individually |
| DG003 | DrugBank ID | Blocking | TxGNN cannot generate predictions without a graph node | Map each component separately; corticotropin (DB00741) and histamine (DB04660) are individually registered |
| DG004 | Original approved indication | High | Cannot establish repurposing baseline | Search TFDA / US FDA / EMA for each component or the combined product |

---

## Recommended Path Forward

Because this product is a multi-component mixture, standard single-drug repurposing analysis is not directly applicable. The recommended approach is to **decompose the mixture into evaluable components**:

1. **Corticotropin (ACTH)** — DrugBank ID DB00741 — has known indications (diagnostic testing, infantile spasms, MS relapse) and is amenable to TxGNN repurposing analysis on its own.
2. **Histamine dihydrochloride** — used as a positive control in allergy testing; limited repurposing relevance, but can be queried separately.
3. **Pollen and animal-derived allergen components** — these are not standard small-molecule drugs; they are biological extracts. Repurposing analysis is not applicable to these components.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model was unable to generate any repurposing predictions for this candidate because the drug is a multi-component allergen mixture without a single DrugBank knowledge-graph node. The Evidence Pack is effectively empty of actionable signals.

**To proceed, the following is needed:**

- **Decompose the mixture**: Run separate TxGNN evaluations for corticotropin (DB00741) and histamine dihydrochloride as individual drug candidates.
- **Clarify product class**: Confirm whether this is an allergen immunotherapy product or a diagnostic reagent, as this determines whether repurposing is conceptually relevant.
- **Resolve DG001–DG004**: Obtain package insert, MOA data, and original indication for each active component before re-submitting to the pipeline.
- **Do not re-run TxGNN** on the full 18-component INN string — the composite string will not resolve to a graph node.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

