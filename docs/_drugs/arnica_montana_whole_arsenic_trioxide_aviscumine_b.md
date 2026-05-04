---
layout: default
title: Arnica Montana Whole Arsenic Trioxide Aviscumine B
parent: 僅模型預測 (L5)
nav_order: 373
evidence_level: L5
indication_count: 0
---

# Arnica Montana Whole Arsenic Trioxide Aviscumine B
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

# Multi-Component Compound (Arnica Montana + 9 Others): Insufficient Data for Repurposing Evaluation

## One-Sentence Summary

This candidate consists of a 10-ingredient complex mixture (including Arnica Montana, Arsenic Trioxide, Aviscumine, and others) with no approved indications on record in Taiwan or the United States.
The TxGNN model was **unable to generate any repurposing predictions** for this compound, as it could not be matched to a single DrugBank entity.
Without a recognized drug identity or baseline indication, no evidence-based evaluation can be completed at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | None on record |
| Predicted New Indication | No prediction generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (Model prediction only — and none was generated) |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Was Generated

This submission contains **10 distinct chemical or botanical ingredients** listed as a single drug string:

> ARNICA MONTANA WHOLE · ARSENIC TRIOXIDE · AVISCUMINE · BARIUM IODIDE · CLAVICEPS PURPUREA SCLEROTIUM · OYSTER SHELL CALCIUM CARBONATE (CRUDE) · PHOSPHORUS · SILVER NITRATE · SOLANUM NIGRUM TOP · TOBACCO LEAF

The TxGNN pipeline is designed to evaluate **individual drug entities** mapped to DrugBank IDs. Because this submission could not be resolved to any single DrugBank entry (`drugbank_id: null`), the knowledge graph traversal and deep learning prediction steps both returned empty results.

Notably, several components *individually* have known pharmacological profiles — for example, **Arsenic Trioxide** is an established antineoplastic agent used in Acute Promyelocytic Leukemia (APL), and **Aviscumine** (mistletoe lectin) has been investigated as an immunotherapy adjuvant. However, the combination as a whole remains uncharacterized in standard drug databases.

The ingredient profile (Phosphorus, Arsenic Trioxide, Silver Nitrate, botanical extracts) is consistent with **homeopathic or complex traditional medicine formulations**, which typically fall outside the scope of conventional repurposing pipelines.

---

## Safety Considerations

No safety data is currently available for this compound as a combined entity. Individual components carry significant standalone risks:

- **Arsenic Trioxide**: Known QT-prolongation risk, hepatotoxicity, and hematological toxicity; requires cardiac monitoring
- **Silver Nitrate**: Corrosive at high concentrations; argyria risk with chronic exposure
- **Claviceps Purpurea (Ergot)**: Vasoconstrictive alkaloids; contraindicated in vascular disease and pregnancy
- **Tobacco Leaf**: Nicotine-containing; cardiovascular and addiction risk

Please refer to individual component package inserts for component-level safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The compound cannot be evaluated through standard TxGNN repurposing methodology because it is a multi-ingredient mixture without a unified DrugBank identity, no approved indications, and no regulatory registrations. Proceeding would require fundamental disambiguation of the compound's identity and intended use.

**To proceed, the following is needed:**

1. **Clarify compound identity** — Determine whether this is a registered formulation (e.g., a homeopathic product with a specific product code) or an experimental combination; provide the intended product name or registration number
2. **Decompose into individual agents** — If repurposing evaluation is desired, submit each active ingredient (especially Arsenic Trioxide and Aviscumine) as separate pipeline candidates with their individual DrugBank IDs
3. **Establish a primary indication** — Document the intended or historical therapeutic use of this combination to anchor the repurposing comparison
4. **Resolve MOA data gaps** — Obtain mechanism-of-action data (DG002) and package insert warnings (DG001) for at minimum the pharmacologically active components
5. **Regulatory feasibility check** — Confirm whether the combination formula has any registration pathway under Taiwan FDA or US FDA before investing further in evidence collection
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

