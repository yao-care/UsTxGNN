---
layout: default
title: Arnica Montana Root Graphite Hypericum Perforatum 
parent: 僅模型預測 (L5)
nav_order: 368
evidence_level: L5
indication_count: 0
---

# Arnica Montana Root Graphite Hypericum Perforatum 
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

# Multi-Component Homeopathic Preparation (Arnica/Hypericum Complex): Insufficient Data for Drug Repurposing Evaluation

## One-Sentence Summary

This candidate is a multi-component homeopathic/botanical preparation containing eight active ingredients (including Arnica Montana, Hypericum Perforatum, and Ruta Graveolens), with recognized traditional use for musculoskeletal and nerve pain relief.
However, the TxGNN model returned **no predicted indications** for this combination — likely because the complex multi-ingredient formula and the absence of a DrugBank ID prevented the model from mapping the drug to the knowledge graph.
Without any model output, clinical evidence, or regulatory reference, a formal repurposing assessment **cannot be completed at this time**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not established (no regulatory licenses on record) |
| Predicted New Indication | No TxGNN predictions generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — Model prediction only (prediction absent; no supporting studies identified) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Was Generated

This preparation is an eight-ingredient homeopathic/botanical complex. Several structural issues prevented TxGNN from producing a meaningful output:

1. **No DrugBank ID**: TxGNN relies on DrugBank identifiers to anchor drugs within the knowledge graph. This multi-ingredient formula has no single DrugBank node, making graph traversal impossible without decomposing it into individual components.

2. **No mapped original indication**: The regulatory record is empty (0 licenses), so there is no approved indication from which to reason by analogy. Without a seed indication, TxGNN's disease–drug link prediction cannot be initialized.

3. **Homeopathic/botanical classification**: Conventional biomedical knowledge graphs (including the TxGNN KG built from DrugBank, OMIM, and DisGeNET) have limited coverage of homeopathic preparations and botanical extracts at the sub-ingredient level.

**What is known from traditional/ethnopharmacological context:**
- *Arnica Montana* is traditionally used for bruising, muscle soreness, and post-traumatic swelling.
- *Hypericum Perforatum* (St. John's Wort) is associated with neuropathic pain relief and mild-to-moderate depression.
- *Ruta Graveolens* has historical use in eye strain and rheumatic conditions.
- *Rhododendron Tomentosum* is used in folk medicine for joint pain.
- *Magnesium Sulfate* has established clinical roles in muscle relaxation and neuroprotection.

Taken together, this combination profile is consistent with a musculoskeletal/neuropathic pain application, but this inference is based on traditional use — **not TxGNN output** — and cannot be treated as a model-supported prediction.

---

## US Market Information

No regulatory licenses were found in the US for this drug combination.

---

## Safety Considerations

Please refer to the package insert for safety information. No DDI data, key warnings, or contraindication records were retrieved for this preparation.

> **Note on Hypericum Perforatum**: Although specific DDI data was not returned for this combination, Hypericum Perforatum (St. John's Wort) is a well-documented CYP3A4/P-gp inducer with clinically significant interactions with anticoagulants, antiretrovirals, oral contraceptives, and transplant immunosuppressants. If this ingredient is present in clinically active concentrations, drug interaction screening is recommended before any clinical application.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline produced no output for this candidate due to the absence of a DrugBank ID and regulatory anchor data. The eight-ingredient homeopathic formula cannot be evaluated as a single entity within the current knowledge graph framework, and traditional use signals alone do not meet the minimum evidence threshold for a repurposing recommendation.

**To proceed, the following is needed:**

- **Decompose the formula**: Run individual TxGNN predictions for each of the eight components (e.g., Hypericum Perforatum, Arnica Montana) using their respective DrugBank IDs, then aggregate results.
- **Establish an intended indication**: Clarify the intended therapeutic use (e.g., musculoskeletal pain, neuropathic pain) to enable targeted evidence review.
- **Obtain safety documentation**: Retrieve the full package insert or equivalent label to populate key warnings, contraindications, and drug interactions — currently all are flagged as data gaps.
- **Assess regulatory pathway**: Confirm whether this product is being evaluated as a botanical drug (FDA Botanical Drug Guidance), homeopathic product (OTC monograph), or conventional combination drug, as the evidence standards differ substantially.
- **Literature screen on key actives**: Conduct a targeted PubMed/ClinicalTrials.gov search on Hypericum Perforatum and Arnica Montana for the intended new indication, as these two components have the strongest existing evidence base.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

