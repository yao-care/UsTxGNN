---
layout: default
title: Amanita Muscaria Fruiting Body Ammonium Carbonate 
parent: 僅模型預測 (L5)
nav_order: 317
evidence_level: L5
indication_count: 0
---

# Amanita Muscaria Fruiting Body Ammonium Carbonate 
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

# Multi-Component Homeopathic Formulation: Insufficient Data for Drug Repurposing Evaluation

## One-Sentence Summary

This submission contains a 19-component homeopathic formulation (including *Amanita muscaria*, arsenic triiodide, *Mephitis mephitis* anal gland fluid, and *Echinacea angustifolia*, among others) with no registered original indication and no DrugBank identifier on record.
The TxGNN model returned **no predicted new indications** for this compound, and the formulation has **no market authorization** in Taiwan.
Due to the complete absence of prediction outputs and critical data gaps, a meaningful drug repurposing assessment cannot be performed at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | None on record |
| Predicted New Indication | None (TxGNN returned no candidates) |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — Model prediction only (no predictions generated) |
| US Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN prediction was generated for this formulation, so a mechanistic rationale for any new indication cannot be constructed.

This product is a complex multi-ingredient mixture of 19 substances spanning fungi (*Amanita muscaria*, *Aspergillus niger*, *Claviceps purpurea*), botanical extracts (*Cinchona officinalis*, *Echinacea angustifolia*, *Phytolacca americana*, *Sanguinaria canadensis*, *Thuja occidentalis*), animal-derived materials (*Blatta orientalis*, *Mephitis mephitis* anal gland fluid), mineral and inorganic compounds (arsenic triiodide, antimony potassium tartrate, ammonium carbonate, potassium carbonate, sodium sulfate, sulfuric acid, phenol, iron), and common food ingredients (onion). This composition is consistent with a classical homeopathic preparation, where each ingredient is typically employed at extreme dilutions.

The TxGNN knowledge-graph model is optimized for single small-molecule entities with defined DrugBank identifiers. Because no DrugBank ID was resolved and no structured mechanistic profile is available, the model could not locate the compound in the knowledge graph and therefore produced no repurposing candidates. This is a methodological limitation, not a clinical judgment on the formulation itself.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

This formulation has no registered product licenses on file. No authorization table can be generated.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline produced zero predicted indications for this 19-component homeopathic mixture, and no regulatory authorization, original indication, mechanism of action, or safety data are currently available — making any repurposing evaluation impossible at this stage.

**To proceed, the following is needed:**

- **Clarify product identity**: Determine whether this formulation corresponds to a specific marketed homeopathic product (e.g., by brand name or NDC/NDA number) to enable targeted database queries.
- **Resolve DrugBank ID or active ingredient mapping**: Identify whether any single component can be evaluated independently through TxGNN (e.g., cinchonine/quinine from *Cinchona officinalis*, or sanguinarine from *Sanguinaria canadensis*).
- **Obtain original indication documentation**: Retrieve package insert, label, or monograph specifying the claimed therapeutic use.
- **Perform safety review per component**: Several ingredients carry significant toxicity concerns at non-homeopathic concentrations (arsenic triiodide, antimony potassium tartrate, phenol, sulfuric acid, *Amanita muscaria*); a component-level safety audit is required before any clinical evaluation.
- **Re-run TxGNN pipeline on individual active components**: If individual INN-level DrugBank IDs can be resolved for key ingredients, each can be submitted as a separate TxGNN query.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

