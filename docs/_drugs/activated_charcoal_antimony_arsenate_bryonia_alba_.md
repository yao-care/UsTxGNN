---
layout: default
title: Activated Charcoal Antimony Arsenate Bryonia Alba 
parent: 僅模型預測 (L5)
nav_order: 183
evidence_level: L5
indication_count: 0
---

# Activated Charcoal Antimony Arsenate Bryonia Alba 
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

# 多成分製劑 (Multi-Component Preparation): 評估報告

## One-Sentence Summary

This submission contains a complex multi-component preparation composed of 21 heterogeneous ingredients—including herbal extracts, minerals, microorganisms, and gases—that does not match any single registered pharmaceutical entity.
The TxGNN model was **unable to generate repurposing predictions** for this compound due to the absence of a DrugBank identifier and the non-standard nature of the formulation.
There is currently **no clinical trial evidence, no supporting literature, and no regulatory authorization** in any examined market.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (no regulatory registration found) |
| Predicted New Indication | None — TxGNN pipeline returned no candidates |
| TxGNN Prediction Score | N/A |
| Evidence Level | Below L5 (no predictions, no studies, no registration) |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

No TxGNN repurposing prediction was generated for this submission. The pipeline requires a valid DrugBank ID (`drugbank_id: null`) to anchor the compound within the knowledge graph; without it, neither knowledge-graph traversal nor deep-learning scoring could be performed.

The submitted "INN" field is not a single international nonproprietary name but a concatenated list of 21 discrete substances spanning at least five pharmacological categories: adsorption agents (activated charcoal), inorganic minerals (copper, tin, phosphorus, potassium chloride), botanical extracts (Bryonia alba, Chelidonium majus, Gelsemium sempervirens, Ipecac, Polygala senega, Pratia purpurascens, Veratrum viride), biological/microbial antigens (Haemophilus influenzae type B, Mycoplasma pneumoniae, Streptococcus pneumoniae), and other materials (camphor, oxygen, quinine hydrochloride, antimony arsenate, Sus scrofa lung). The combination profile is consistent with a **homeopathic or naturopathic complex remedy**, for which standard pharmacokinetic and mechanistic data are generally unavailable.

Without an established mechanism of action, a registered indication, or a drug-disease relationship node in the TxGNN knowledge graph, the repurposing hypothesis cannot be mechanistically justified at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

No regulatory authorizations were found. This preparation is not registered in Taiwan; US NDA/ANDA records were not queried separately due to the absence of a standard drug identifier.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Because the formulation includes several potentially bioactive components—including **quinine hydrochloride** (risk of QT prolongation and cinchonism), **camphor** (risk of seizures at high doses), **ipecac** (emetogenic, cardiotoxic at high doses), and **antimony arsenate** (heavy metal toxicity)—a full ingredient-level safety review is strongly recommended before any clinical or research application is considered.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This submission cannot be meaningfully evaluated by the TxGNN drug repurposing pipeline because the input does not correspond to a single, identifiable pharmaceutical entity—it is a multi-ingredient mixture lacking a DrugBank ID, a registered indication, or any retrievable mechanistic profile. No repurposing prediction was produced, and no supporting evidence exists.

**To proceed, the following is needed:**

- **Clarify the submission intent:** Determine whether this is a homeopathic complex, a compounded formulation, a research mixture, or a data entry error that concatenated multiple drug names into a single record.
- **Decompose the formulation:** If repurposing analysis is desired, each bioactive component (e.g., quinine, activated charcoal, ipecac) should be submitted individually as a separate Evidence Pack with its own INN and DrugBank ID.
- **Obtain regulatory documentation:** If the combination product is registered in any jurisdiction, retrieve the package insert or product monograph to establish the approved indication and safety profile.
- **Resolve DrugBank mapping:** Run each ingredient through the DrugBank normalization pipeline (`drugbank_mapper.py`) to obtain valid identifiers before re-submitting to TxGNN.
- **Address data gaps DG001 and DG002:** Retrieve TFDA package insert warnings/contraindications and mechanism of action data for each identifiable component.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

