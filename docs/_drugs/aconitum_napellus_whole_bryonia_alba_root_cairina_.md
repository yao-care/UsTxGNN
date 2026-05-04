---
layout: default
title: Aconitum Napellus Whole Bryonia Alba Root Cairina 
parent: 僅模型預測 (L5)
nav_order: 134
evidence_level: L5
indication_count: 0
---

# Aconitum Napellus Whole Bryonia Alba Root Cairina 
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

# Homeopathic Influenza Combination (Multi-Ingredient): Insufficient Data for Repurposing Evaluation

## One-Sentence Summary

This product is a 15-ingredient homeopathic combination that appears formulated for influenza and flu-like symptoms, containing diluted influenza virus strains (A/Darwin/6/2021, B/Austria/1359417/2021, B/Phuket/3073/2013) alongside classical homeopathic botanicals (Gelsemium, Bryonia, Eupatorium, Aconitum).
The TxGNN model returned **no predicted new indications** for this candidate, likely because the multi-ingredient INN string could not be resolved to a single DrugBank node.
With **0 clinical trials**, **0 publications**, and **0 regulatory authorizations** identified in this pipeline run, the current evidence base is insufficient to evaluate repurposing potential.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not established (no regulatory authorizations found) |
| Predicted New Indication | None (TxGNN returned no predictions) |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — model prediction only; in this case, no predictions were generated |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Was Generated

This candidate is a homeopathic combination product composed of **15 distinct ingredients**, including:

- **Homeopathic influenza antigens**: Influenza A (A/Darwin/6/2021), Influenza B (B/Austria/1359417/2021 BVR-26, B/Phuket/3073/2013 BVR-1B), and generic Influenza A Whole — consistent with annual seasonal influenza formulations
- **Classic homeopathic flu botanicals**: *Eupatorium perfoliatum* (body aches, fever), *Gelsemium sempervirens* (weakness, headache), *Bryonia alba* (myalgia, dry cough), *Aconitum napellus* (sudden fever onset)
- **Cairina moschata* (Muscovy duck) heart/liver autolysate**: the hallmark ingredient of Oscillococcinum-class homeopathic products
- **Additional homeopathic constituents**: Ipecac, Phosphorus, Phytolacca americana, Sanguinaria canadensis, Lobaria pulmonaria, Strychnos nux-vomica

The TxGNN knowledge graph operates on individual drug–disease edges indexed by DrugBank ID. Because this candidate:
1. Has **no resolvable DrugBank ID** (the 15-component INN string did not map to any single node), and
2. Contains **homeopathic dilutions** not represented in conventional pharmacological databases,

the graph traversal produced zero candidate disease edges, and no prediction score could be computed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this multi-ingredient combination as a unified entity.

> **Note**: Individual components such as influenza virus antigens appear in vaccine trials, but those are not directly applicable to this homeopathic formulation.

---

## Literature Evidence

Currently no related literature available for this specific multi-ingredient combination as identified by the pipeline.

---

## US Market Information

No regulatory authorizations were identified in this pipeline run. This product is classified as **not marketed** in the United States under this ingredient profile.

> Oscillococcinum (Boiron), a related Cairina moschata–based homeopathic product, is marketed in the US as an OTC homeopathic remedy and is regulated under FDA's OTC homeopathic enforcement policy (2017 revised guidance), but it is a distinct product with a different formulation.

---

## Safety Considerations

Please refer to the package insert for safety information.

> No drug–drug interaction data, key warnings, or contraindications were returned by the pipeline. Given the homeopathic nature of the product (ultra-dilute ingredients), conventional pharmacokinetic DDI analysis is generally not applicable. However, some ingredients — notably *Aconitum napellus* and *Strychnos nux-vomica* — contain toxic alkaloids (aconitine, strychnine) at pharmacologically active concentrations in non-homeopathic preparations; their safety in this formulation depends entirely on the dilution factor specified in the monograph.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline could not process this candidate because the 15-ingredient INN string cannot be mapped to a single DrugBank node, which is a structural prerequisite for knowledge-graph–based repurposing prediction. Without a valid prediction score or evidence base, no repurposing direction can be evaluated at this time.

**To proceed, the following is needed:**

- **Decompose the combination**: Evaluate each of the 15 active ingredients independently through the TxGNN pipeline to identify individual repurposing signals
- **Resolve the primary active ingredient**: Determine which ingredient is considered the principal agent (likely the influenza virus antigens or Cairina moschata autolysate) and resubmit as a single-INN query
- **Clarify regulatory identity**: Confirm whether this formulation corresponds to a registered homeopathic OTC product (e.g., Oscillococcinum or equivalent) to enable proper literature and trial linkage
- **Obtain the product monograph**: Source the full ingredient dilution ratios (e.g., 200CK, 1X) to assess whether any components are present at pharmacologically active concentrations
- **Assess MOA plausibility**: For the influenza virus antigen components, literature on homeopathic immunomodulation should be reviewed separately from classical pharmacology models
- **Address Data Gap DG001 & DG002**: Retrieve package insert warnings/contraindications and mechanism-of-action documentation from relevant regulatory sources before any further pipeline evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

