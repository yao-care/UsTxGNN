---
layout: default
title: Acer Negundo Pollen Acer Saccharum Pollen Agrostis
parent: 僅模型預測 (L5)
nav_order: 69
evidence_level: L5
indication_count: 0
---

# Acer Negundo Pollen Acer Saccharum Pollen Agrostis
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

# Multi-Component Allergen Extract (70-Pollen Mixture): Insufficient Data for Repurposing Analysis

## One-Sentence Summary

This entry represents a complex multi-component allergen immunotherapy mixture comprising 70+ aeroallergen extracts (tree, grass, and weed pollens plus botanical roots), classically used for allergic desensitization therapy.
The TxGNN pipeline returned **no predicted new indications** for this candidate, and the US regulatory search found **no approved NDA/BLA** on record.
As a result, no evidence-based repurposing analysis can be performed at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Product Type | Multi-component allergen immunotherapy extract (70 components) |
| Original Indication | Allergen desensitization / Allergic rhinitis (inferred from product composition) |
| Predicted New Indication | None — TxGNN returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (model prediction only — and none generated) |
| US Market Status | Not marketed (0 authorizations found) |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Was Generated

This entry is not a single molecular entity but a **heterogeneous mixture of 70+ allergenic source materials**, including:

- **Tree pollens** (Acer, Betula, Carya, Fagus, Fraxinus, Juglans, Juniperus, Liquidambar, Morus, Picea, Pinus, Platanus, Populus, Quercus, Salix, Ulmus, Broussonetia, Celtis, Ligustrum)
- **Grass pollens** (Agrostis, Anthoxanthum, Avena, Bromus, Cynodon, Dactylis, Festuca, Holcus, Koeleria, Lolium, Phalaris, Phleum, Sorghum, Triticum, Zea)
- **Weed pollens** (Ailanthus, Amaranthus spp., Ambrosia spp., Artemisia spp., Chenopodium spp., Plantago, Rumex spp., Solidago, Urtica, Xanthium)
- **Botanical roots/herbs** (Baptisia tinctoria root, Echinacea, Fenugreek leaf, Goldenseal, Myrrh, Phytolacca americana root)

The TxGNN knowledge graph operates on single DrugBank-indexed entities. Because this mixture has **no DrugBank ID** and is not a defined molecular entity, the model cannot generate a drug–disease prediction score. This is a **pipeline limitation**, not a clinical judgment.

---

## US Market Information

No US authorizations (NDA/BLA/ANDA) were retrieved for this product combination. Individual allergen extract components may be regulated as biological products under separate licenses; however, this specific 70-component mixture as a unit was not found in the regulatory database queried.

---

## Safety Considerations

Please refer to the package insert for safety information. For allergen immunotherapy products generally, key considerations include risk of systemic allergic reaction (anaphylaxis), required in-office administration with post-injection observation, and contraindication in patients with severe or unstable asthma.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This evidence pack does not represent a repurposable small-molecule drug — it is a multi-component allergen extract mixture that falls outside the TxGNN prediction framework. No predictions, regulatory data, or safety records were retrieved, making a standard repurposing evaluation impossible.

**To proceed, the following is needed:**

- **Identify the actual drug of interest**: Confirm whether the intended query target is one of the botanical components (e.g., Echinacea, Goldenseal) or the mixture as a whole; individual components may have standalone DrugBank entries
- **Resolve the pipeline ingestion error**: The candidate ID `TW-UNKNOWN-multi` and the concatenated multi-ingredient string suggest an upstream data parsing issue — the drug name field appears to have been populated with a full ingredient list rather than a single INN
- **Separate ingredients for individual analysis**: If the goal is to explore any individual pollen protein or botanical compound (e.g., berberine from Goldenseal, echinacoside from Echinacea), each should be submitted as a separate query with its own DrugBank ID
- **Obtain MOA data (DG002)**: Once the correct single-entity candidate is identified, retrieve mechanism of action from DrugBank
- **Obtain regulatory safety data (DG001)**: Retrieve package insert warnings and contraindications from the relevant regulatory authority
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

