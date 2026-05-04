---
layout: default
title: Acer Rubrum Pollen Acer Saccharum Pollen Agrostis 
parent: 僅模型預測 (L5)
nav_order: 75
evidence_level: L5
indication_count: 0
---

# Acer Rubrum Pollen Acer Saccharum Pollen Agrostis 
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

# Multi-Allergen Immunotherapy Extract Complex: Allergen Desensitization – No TxGNN Predictions Available

## One-Sentence Summary

This candidate is a complex multi-component allergen extract mixture comprising 69 botanical antigens — spanning tree pollens, grass pollens, weed pollens, and herbal botanicals — of the type used in subcutaneous allergen immunotherapy (SCIT) for allergic rhinitis and polysensitized allergic disease.
The TxGNN pipeline returned **no predicted new indications** for this candidate, most likely because the multi-ingredient string could not be resolved to a single DrugBank entity or knowledge-graph node.
Without a valid prediction, a formal repurposing evaluation cannot proceed at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Allergen immunotherapy / allergy desensitization (inferred from composition) |
| Predicted New Indication | None – TxGNN generated no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A – pipeline did not produce a candidate |
| US Market Status | Not marketed (no NDA records found) |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Was Generated

This candidate is not a single molecular entity but a **69-component allergen mixture** whose ingredients include:

- **Tree pollens** (22 species): Acer rubrum, Acer saccharum, Ailanthus altissima, Alnus rubra, Betula nigra, Carya tomentosa, Celtis occidentalis, Fagus grandifolia, Fraxinus americana, Juglans regia, Juniperus ashei/scopulorum/virginiana, Ligustrum vulgare, Liquidambar styraciflua, Morus alba, Picea pungens, Pinus strobus, Platanus occidentalis, Populus alba/deltoides/nigra/tremuloides, Pseudotsuga menziesii, Salix nigra, Ulmus americana/pumila
- **Grass pollens** (15 species): Agrostis gigantea, Anthoxanthum odoratum, Avena sativa, Bromus inermis, Dactylis glomerata, Festuca pratensis, Lolium multiflorum/perenne, Pascopyrum smithii, Phalaris arundinacea, Phleum pratense, Poa pratensis, Sorghum halepense, Triticum aestivum, Zea mays
- **Weed pollens** (21 species): Amaranthus retroflexus/spinosus/tuberculatus, Ambrosia acanthicarpa, Artemisia absinthium/ludoviciana/tridentata/vulgaris, Atriplex canescens/confertifolia, Bassia scoparia, Chenopodium album, Cyclachaena xanthifolia, Iva annua, Plantago lanceolata, Rumex acetosella, Salsola tragus, Sarcobatus vermiculatus, Solidago canadensis, Urtica dioica, Xanthium strumarium
- **Herbal botanical components** (5): Baptisia tinctoria root, Echinacea (unspecified), Fenugreek leaf, Goldenseal, Myrrh, Phytolacca americana root

The TxGNN knowledge graph is built around **single INN molecules mapped to DrugBank IDs**. A multi-ingredient string of this length cannot be resolved to any DrugBank node, so the KG traversal and DL scoring steps both returned null results. This is a **pipeline limitation**, not a signal that the product has no repurposing potential.

The five herbal components — especially Echinacea, Goldenseal (*Hydrastis canadensis*), and Phytolacca — have established immunomodulatory properties studied independently, but they were queried as part of the composite string and were not individually scored.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: No TFDA registration was found for this product combination. Standard allergen immunotherapy precautions apply: anaphylaxis risk with dose escalation, requirement for post-injection observation periods, and contraindication in patients on beta-blockers or with severe asthma.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline cannot process a 69-component allergen mixture as a single entity; without a resolvable DrugBank ID and a scored prediction, there is no repurposing hypothesis to evaluate.

**To proceed, the following is needed:**

1. **Decompose the mixture**: Re-submit each individual component (e.g., *Phleum pratense* pollen → DB01161, Echinacea → DB00584) as separate single-drug queries so TxGNN can score each independently.
2. **Identify the intended therapeutic entity**: Determine whether the repurposing question concerns the full allergen mix (immunotherapy application) or one of the herbal botanicals within it (e.g., Goldenseal/berberine, Echinacea polysaccharides).
3. **Resolve DrugBank mapping**: Manually map the components with known DrugBank IDs before re-running the KG prediction pipeline.
4. **Obtain regulatory data**: If any individual component has TFDA or FDA NDA registration, retrieve the package insert for MOA and safety data.
5. **Re-run pipeline per component**: After decomposition, generate individual Evidence Packs and aggregate findings into a coherent repurposing landscape for the botanicals of interest.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

