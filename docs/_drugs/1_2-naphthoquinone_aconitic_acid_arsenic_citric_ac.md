---
layout: default
title: 1 2-Naphthoquinone Aconitic Acid Arsenic Citric Ac
parent: 僅模型預測 (L5)
nav_order: 14
evidence_level: L5
indication_count: 0
---

# 1 2-Naphthoquinone Aconitic Acid Arsenic Citric Ac
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

# Multi-Component Metabolic Mixture: Insufficient Data for Repurposing Evaluation

## One-Sentence Summary

This candidate is a complex 20-ingredient mixture — including Krebs cycle intermediates, trace minerals, plant extracts (ginkgo), and porcine organ extracts (lung, colon, pancreas) — with no registered indication or regulatory approval in Taiwan or the US.
The TxGNN model returned **no predicted indications**, likely because this multi-component formulation could not be mapped to a single DrugBank entity.
Without predictions, regulatory records, or safety data, a full repurposing evaluation cannot proceed at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | None on record |
| Predicted New Indication | No TxGNN prediction generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (no studies; no predictions) |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Was Generated

This entry is not a single drug but a **20-component formulation** containing:

- **Krebs cycle organic acids**: citric acid, malic acid, fumaric acid, succinic acid, pyruvic acid, aconitic acid, oxogluric acid (α-ketoglutaric acid)
- **Trace elements and minerals**: arsenic, copper, manganese, phosphorus, tin, germanium sesquioxide, oyster shell calcium carbonate
- **Porcine organ extracts**: Sus scrofa colon, lung, and pancreas
- **Plant extract**: Ginkgo
- **Synthetic/semi-synthetic compounds**: 1,2-naphthoquinone, sodium diethyl oxalacetate

The TxGNN model is designed to evaluate **single drug entities** mapped via DrugBank IDs. Because this formulation has no DrugBank ID and its constituent ingredients lack a unified pharmacological profile, the model could not produce a repurposing prediction. Additionally, no original indication or approved use was found in either the Taiwan or US regulatory database.

This pattern is typical of **compounded preparations or traditional medicine products** that exist outside standard regulatory pathways, making automated repurposing analysis structurally infeasible without first decomposing the formulation into its individual components.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note**: Several ingredients in this formulation warrant independent safety review before any clinical use:
> - **Arsenic**: narrow therapeutic index; recognized carcinogen at chronic low doses
> - **Germanium sesquioxide**: associated with nephrotoxicity in case reports
> - **Tin**: systemic toxicity risk at elevated exposure
> - **1,2-Naphthoquinone**: reactive oxidant with potential cytotoxicity

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN predictions were generated, no regulatory approvals exist, and no safety profile has been established for this formulation as a whole. The complexity of the 20-component mixture prevents standard drug repurposing evaluation.

**To proceed, the following is needed:**

- **Formulation decomposition**: Evaluate each of the 20 ingredients individually through the TxGNN pipeline to identify which components may carry repurposing potential
- **Identity clarification**: Determine whether this mixture corresponds to a named traditional medicine product (e.g., a glandular/organotherapy preparation) and locate its regulatory history
- **Safety audit**: Conduct independent toxicology review for arsenic, germanium sesquioxide, tin, and 1,2-naphthoquinone components before any human exposure study is considered
- **MOA documentation**: Map individual ingredient mechanisms to assess whether any coherent combined pharmacological activity can be proposed
- **DrugBank linkage**: Attempt to link each active ingredient to a DrugBank entry to enable component-level TxGNN scoring
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

