---
layout: default
title: 2 3 7 8-Tetrachlorodibenzo-P-Dioxin Aconitum Napel
parent: 僅模型預測 (L5)
nav_order: 20
evidence_level: L5
indication_count: 0
---

# 2 3 7 8-Tetrachlorodibenzo-P-Dioxin Aconitum Napel
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

# Multi-Substance Complex (TW-UNKNOWN-multi): Insufficient Data for Repurposing Evaluation

## One-Sentence Summary

This entry corresponds to a multi-substance identifier comprising 23 components — ranging from homeopathic botanicals (e.g., Arnica montana, Apis mellifera, Calendula) to industrial chemicals (e.g., benzene, dioxin, hydrogen cyanide) — that could not be resolved to a single drug entity.
No original indication, no regulatory approval in Taiwan, and **no TxGNN-predicted indications** were returned.
The evidence base is effectively **empty (L5)**, and this entry cannot be meaningfully evaluated for drug repurposing at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | None on record |
| Predicted New Indication | None |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (model prediction only — no prediction generated) |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Is Available

The drug INN field contains a semicolon-delimited list of 23 heterogeneous substances:

| # | Substance | Category |
|---|-----------|----------|
| 1 | 2,3,7,8-Tetrachlorodibenzo-p-dioxin (TCDD) | Industrial toxin / Environmental contaminant |
| 2 | Aconitum napellus whole | Toxic botanical / Homeopathic ingredient |
| 3 | Ammonium cation | Inorganic ion |
| 4 | Apis mellifera | Homeopathic ingredient (bee venom) |
| 5 | Arnica montana whole | Homeopathic botanical |
| 6 | Arsenic trioxide | Approved anticancer agent (AML) |
| 7 | Benzene | Industrial carcinogen |
| 8 | Calendula officinalis flowering top | Homeopathic botanical |
| 9 | Chlorine | Industrial chemical / Toxin |
| 10 | Chloroform | Industrial solvent / Hepatotoxin |
| 11 | Dieffenbachia seguine whole | Toxic plant |
| 12 | Fenson | Obsolete acaricide / Pesticide |
| 13 | Fluorine | Reactive element |
| 14 | Hydrogen cyanide | Highly toxic gas |
| 15 | Methane | Combustible gas |
| 16 | Nitric acid | Strong acid |
| 17 | Onion | Food / Homeopathic ingredient |
| 18 | Phosfolan | Organophosphate pesticide |
| 19 | Potassium cyanide | Highly toxic salt |
| 20 | Propane | Combustible gas |
| 21 | Sulfur | Mineral / Homeopathic ingredient |
| 22 | Sulfuric acid | Strong acid |
| 23 | Veratrum album root | Toxic botanical |

This mixture of industrial chemicals, environmental toxins, pesticides, and homeopathic botanicals does not correspond to any identifiable single drug entity. The TxGNN pipeline requires a resolvable DrugBank ID to generate knowledge-graph embeddings; since `drugbank_id` is null and the INN string could not be mapped, **no prediction was produced**.

The most plausible data pipeline issue is that multiple FDA product ingredient lists were concatenated without deduplication, generating a meaningless compound key. The candidate ID `TW-UNKNOWN-multi` supports this hypothesis.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This entry does not represent a real drug candidate. It is a pipeline artifact — a concatenated multi-ingredient string that failed to resolve to any single pharmacological entity — and cannot be assessed for repurposing potential.

**To proceed, the following is needed:**

- **Deduplication and parsing**: Split the concatenated INN string at the source and create one candidate record per distinct active ingredient.
- **Identity resolution**: Re-run DrugBank mapping on each individual substance (e.g., Arsenic trioxide → DB01169, which has known oncology use and may be a legitimate repurposing candidate).
- **Data provenance audit**: Investigate why `TW-UNKNOWN-multi` was generated — likely a bug in the Taiwan FDA data ingestion step where a multi-ingredient product's ingredient list was flattened into the INN field.
- **Exclusion of non-drug substances**: Industrial chemicals (benzene, TCDD, HCN), gases (methane, propane), and strong acids (sulfuric acid, nitric acid) should be excluded from the repurposing pipeline entirely, as they have no therapeutic application.
- **Homeopathic ingredient handling**: Substances such as Arnica montana, Calendula officinalis, and Apis mellifera may require a dedicated homeopathic product pipeline with separate evaluation criteria.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

