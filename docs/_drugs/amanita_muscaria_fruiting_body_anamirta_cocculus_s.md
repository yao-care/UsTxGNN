---
layout: default
title: Amanita Muscaria Fruiting Body Anamirta Cocculus S
parent: 僅模型預測 (L5)
nav_order: 304
evidence_level: L5
indication_count: 0
---

# Amanita Muscaria Fruiting Body Anamirta Cocculus S
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

# Multi-Component Homeopathic Mixture: No Repurposing Candidate Identified

## One-Sentence Summary

This Evidence Pack describes a ten-component mixture — including Amanita muscaria, Arsenic trioxide, Conium maculatum, Kerosene, Phosphorus, and Tobacco leaf — that resembles a classical homeopathic formulation.
The TxGNN model returned **no predicted new indications** for this compound, and the drug is **not currently marketed** in the United States under any NDA.
Due to the complete absence of predictions, regulatory records, and safety data, no repurposing assessment can be completed at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (no approved indications on record) |
| Predicted New Indication | None (TxGNN returned no candidates) |
| TxGNN Prediction Score | — |
| Evidence Level | L5 — model prediction only; in this case, no prediction was generated |
| US Market Status | Not marketed (0 NDAs) |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Was Generated

The TxGNN knowledge-graph model requires a valid DrugBank identifier to anchor a drug within the biomedical knowledge graph. This compound has **no DrugBank ID**, which means the model cannot establish the network embeddings needed to score disease associations.

In addition, the formulation is a heterogeneous ten-component mixture. The individual components span radically different pharmacological classes:

| Component | Known Pharmacological Class |
|-----------|----------------------------|
| Arsenic trioxide | Cytotoxic / APL chemotherapy agent (FDA-approved as Trisenox) |
| Amanita muscaria fruiting body | Muscarinic/GABA-A agonist (ibotenic acid, muscimol); toxic |
| Conium maculatum flowering top | Toxic piperidine alkaloids (coniine); no therapeutic use |
| Anamirta cocculus seed | GABA-A antagonist (picrotoxin); toxic |
| Phosphorus | Elemental phosphorus; highly toxic |
| Kerosene | Petroleum distillate; no recognised therapeutic use |
| Leonurus cardiaca whole | Traditional cardiotonic herb |
| Pulsatilla vulgaris whole | Classical homeopathic remedy |
| Theridion curassavicum | Classical homeopathic nosode (from spider) |
| Tobacco leaf | Nicotinic receptor agonist; carcinogen |

The combination pattern is consistent with a **classical homeopathic polypharmacy preparation**, in which individual ingredients are typically used at extreme dilutions. At conventional pharmaceutical doses, several components (arsenic trioxide, coniine, picrotoxin, phosphorus, kerosene) are acutely toxic. This further complicates any standard repurposing analysis.

---

## Safety Considerations

Several individual components carry significant standalone toxicity concerns worth flagging, even in the absence of package-insert data for the combined product:

- **Arsenic trioxide**: Known carcinogen and QTc-prolonging agent; requires cardiac monitoring when used therapeutically.
- **Conium maculatum**: Source of coniine, a neuromuscular blocking alkaloid responsible for Socrates' death; no safe therapeutic dose window is established.
- **Amanita muscaria**: Contains muscimol and ibotenic acid; causes cholinergic and GABAergic toxicity.
- **Phosphorus (elemental)**: Hepatotoxic and caustic; formerly used as a homeopathic remedy but abandoned in conventional medicine.
- **Kerosene**: Aspiration risk; pulmonary toxicity; not a recognised pharmaceutical excipient.

Please refer to the relevant safety data sheets (SDS) and any available package insert if this product is being evaluated for clinical or regulatory purposes.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline produced zero repurposing candidates because the compound lacks a DrugBank ID and has no approved indication record to anchor the prediction. The multi-component, likely homeopathic nature of the formulation, combined with the presence of acutely toxic ingredients at conventional doses, makes a standard drug-repurposing pathway inappropriate without substantial additional information.

**To proceed, the following is needed:**

- **Clarify the product identity**: Confirm whether this is a homeopathic dilution (e.g., 6C, 30C) or a conventional pharmaceutical. If homeopathic, the regulatory and safety framework differs entirely from standard drug repurposing.
- **Obtain a DrugBank ID**: If one of the single active ingredients (e.g., arsenic trioxide) is the intended subject of repurposing, re-submit with that ingredient alone as the `inn` field. Arsenic trioxide (DrugBank: DB01169) already has an approved oncology indication and active repurposing literature.
- **Separate component-level analysis**: Each of the ten ingredients should be evaluated individually for repurposing potential rather than as a combined entity.
- **Regulatory clarification**: Determine whether this product falls under homeopathic OTC exemptions or requires a full NDA pathway in the target market, as this governs the applicable evidence standard.
- **Safety data retrieval**: Pull the official prescribing information or SDS for any component before proceeding to an S1 safety screen.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

