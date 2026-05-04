---
layout: default
title: 1 4-Naphthoquinone Aconitic Acid - Anhydrous Citri
parent: 僅模型預測 (L5)
nav_order: 17
evidence_level: L5
indication_count: 0
---

# 1 4-Naphthoquinone Aconitic Acid - Anhydrous Citri
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

# Multi-Component Formula (20 Ingredients): Insufficient Data for Repurposing Evaluation

## One-Sentence Summary

This entry describes a complex multi-component mixture comprising 20 ingredients—including organic acids, animal-derived substances, minerals, and botanical extracts—with no established approved indication on record.
The TxGNN model returned **no predicted indications** for this candidate, and the US/Taiwan regulatory database shows **no approved licenses**.
Without an original indication or a model prediction target, a standard drug repurposing evaluation cannot be completed at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | None on record |
| Predicted New Indication | None (TxGNN returned no predictions) |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — Model prediction only (and none returned) |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No repurposing prediction is available for this candidate. The TxGNN knowledge-graph and deep-learning models require a recognized drug node (typically identified by a DrugBank ID) to generate disease associations. This entry has no DrugBank ID and no single active pharmaceutical ingredient (API) that the model can anchor to.

The candidate is a heterogeneous mixture of 20 substances spanning organic acids (citric acid, fumaric acid, malic acid, succinic acid, pyruvic acid, oxoglutaric acid, aconitic acid), redox-active compounds (1,4-naphthoquinone, arsenic, sulfur, phosphorus), trace elements (manganese, germanium sesquioxide), animal-derived materials (Bos taurus bile, Sus scrofa gallbladder, pork liver, thyroid), and botanical ingredients (Ginkgo, Lycopodium clavatum spore). This composition resembles classical metabolic/mitochondrial support formulas or complex homeopathic preparations, but no pharmacological mechanism of action data is available to confirm this.

Until individual components are mapped to DrugBank entries and a dominant API is identified, the relationship between this formula and any target indication cannot be assessed mechanistically.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

This drug has no approved licenses in the US regulatory database. No authorization records are available to display.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note on arsenic content**: This formula lists arsenic as an ingredient. In any future evaluation, arsenic speciation (organic vs. inorganic) and concentration must be clarified, as inorganic arsenic carries significant toxicity concerns (carcinogenicity, peripheral neuropathy, QTc prolongation). Regulatory thresholds for arsenic in medicinal products vary by jurisdiction and must be verified before any clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate lacks the foundational data (DrugBank ID, original approved indication, and TxGNN prediction output) required to conduct a drug repurposing evaluation; proceeding without resolving these gaps would produce unreliable conclusions.

**To proceed, the following is needed:**

- **Identify the primary active ingredient**: Determine which of the 20 components is the pharmacologically dominant API; multi-ingredient formulas typically cannot be evaluated as a single entity in TxGNN.
- **Obtain DrugBank ID(s)**: Map each clinically relevant component to its DrugBank entry so TxGNN can generate disease predictions.
- **Clarify product identity**: Confirm whether this is a homeopathic preparation, a nutraceutical blend, or a registered drug product, as the regulatory pathway and evidence standards differ significantly.
- **Resolve arsenic safety data (Blocking — DG001)**: Retrieve the full product monograph or package insert to characterize arsenic form, dose, and safety profile before any safety screening can proceed.
- **Obtain MOA data (High — DG002)**: Query DrugBank and primary literature for mechanistic data on the key components.
- **Resubmit to TxGNN pipeline**: After DrugBank mapping is complete, rerun the KG and DL prediction modules to generate candidate indications.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

