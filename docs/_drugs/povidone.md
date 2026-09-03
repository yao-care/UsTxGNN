---
layout: default
title: Povidone
parent: 僅模型預測 (L5)
nav_order: 1072
evidence_level: L5
indication_count: 1
---

# Povidone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Povidone: From Pharmaceutical Excipient to Congenital Ichthyosiform Erythroderma

## One-Sentence Summary

> Povidone (polyvinylpyrrolidone, PVP) is a pharmaceutical excipient used as a tablet binder, topical antiseptic base (e.g., povidone-iodine), and plasma volume expander, without a specific approved therapeutic indication of its own.
> The TxGNN model predicts a possible association with **Congenital Ichthyosiform Erythroderma**,
> but this prediction is currently supported only by a model score — **no clinical trials and no literature** are available.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indication on record (used as excipient / topical antiseptic base) |
| Predicted New Indication | Congenital Ichthyosiform Erythroderma |
| TxGNN Prediction Score | 99.11% (rank 19,302) |
| Evidence Level | L5 |
| Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for povidone. Based on known information, povidone is a pharmaceutical excipient/carrier polymer — used clinically as a tablet binder, as the base matrix in topical antiseptics (e.g., povidone-iodine), and as a plasma substitute. It does not have a well-defined pharmacological target of its own, so its "efficacy" in prior uses is functional (formulation/delivery) rather than therapeutic.

Congenital ichthyosiform erythroderma is a genetic keratinization disorder (e.g., involving *TGM1*, *ALOX12B* mutations) affecting epidermal differentiation. There is no established mechanism linking povidone's physicochemical properties (film-forming, moisture-retention, carrier function) to the keratinocyte differentiation pathways implicated in this disease. The high TxGNN score (0.99) most likely reflects an indirect graph association — for example, with topical povidone-iodine formulations used in dermatologic care — rather than a genuine pharmacological rationale. This prediction should be treated as a hypothesis-generating signal only, not as mechanistic evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Market Information

No marketed products or authorizations on record; povidone currently has no formal drug license entries in the dataset for this jurisdiction.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug interaction data are currently unavailable — see Data Gap DG001, classified as Blocking, which prevents safety pre-screening.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L5 (model prediction only) — there are no clinical trials, no literature, and no established mechanistic link supporting this indication. In addition, the drug is not currently marketed, and a Blocking data gap (TFDA label/warnings, DG001) prevents any safety pre-screening.

**To proceed, the following is needed:**
- TFDA package insert / warnings and contraindications (DG001, Blocking)
- Mechanism of action data from DrugBank (DG002, High)
- Preclinical or mechanistic studies linking povidone to keratinization pathways
- Any emerging clinical trial or literature evidence for this indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

