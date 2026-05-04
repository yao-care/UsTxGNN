---
layout: default
title: Aluminum Oxide Arsenic Trioxide Calomel Chelidoniu
parent: 僅模型預測 (L5)
nav_order: 276
evidence_level: L5
indication_count: 0
---

# Aluminum Oxide Arsenic Trioxide Calomel Chelidoniu
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

# Multi-Ingredient Heavy Metal Complex: No Repurposing Indication Identified

## One-Sentence Summary

This entry represents a 13-ingredient mixture containing multiple toxic heavy metals and botanical substances — a profile consistent with a homeopathic or traditional compound preparation. The TxGNN pipeline returned **no predicted repurposing indications**, and the product has no US market authorization. No supporting clinical trial or literature evidence was retrieved.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indications on record |
| Predicted New Indication | None — TxGNN returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | Below L5 (no model predictions, no studies) |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

There are no predicted indications to evaluate. The compound is a 13-ingredient mixture whose composition raises immediate concern: **arsenic trioxide** (a cytotoxic oncology drug regulated under strict protocols), **calomel** (mercurous chloride), **mercuric iodide**, and **Mercurius Solubilis** (a homeopathic mercury preparation), **lead** and **lead iodide** (neurotoxins with no established safe exposure level), and **silver nitrate** (a caustic agent). The presence of botanical entries — *Chelidonium majus*, *Solidago virgaurea* flowering top — and the Latin naming convention of "Mercurius Solubilis" strongly suggests this is a **homeopathic formulation**, not a conventional pharmaceutical entity.

Currently, no mechanism of action data is available. The product lacks a DrugBank ID, carries no TFDA or US approval records, and cannot be matched to a single pharmacologically characterized compound. Standard TxGNN drug repurposing pipelines operate on single-entity drugs mapped to the DrugBank knowledge graph; a 13-ingredient homeopathic mixture, particularly one without a DrugBank ID, is outside the model's intended input domain.

The absence of any TxGNN output is therefore **expected and appropriate**, not a data pipeline error.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

No US market authorizations exist for this product.

---

## Safety Considerations

Several ingredients in this mixture carry well-established serious toxicity profiles:

- **Arsenic trioxide**: Human carcinogen; FDA-approved only for acute promyelocytic leukemia under a restricted Risk Evaluation and Mitigation Strategy (REMS). Causes QT prolongation, peripheral neuropathy, and hepatotoxicity.
- **Calomel (Mercurous chloride)** and **Mercuric iodide**: Mercury-containing compounds. Chronic exposure causes nephrotoxicity, neurotoxicity, and acrodynia. The cumulative mercury burden from three mercury-containing ingredients (calomel, mercuric iodide, Mercurius Solubilis) in a single formulation is a significant concern.
- **Lead** and **Lead iodide**: No safe level of lead exposure exists according to WHO and US CDC. Lead causes irreversible neurodevelopmental damage, nephropathy, and anaemia.
- **Silver nitrate**: Caustic and oxidising agent; systemic absorption causes argyria (permanent skin/tissue discolouration) and can impair renal function.

Please refer to individual component package inserts and current regulatory guidance for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model produced no repurposing predictions for this entry, and the formulation contains multiple substances of serious and well-documented toxicological concern. There is no viable path to a repurposing evaluation as currently submitted.

**To proceed, the following is needed:**

- **Clarify regulatory context**: Confirm whether this is a homeopathic product. If so, standard drug repurposing modelling does not apply, and the regulatory pathway (e.g., OTC homeopathic monograph, FDA Compliance Policy Guide) is fundamentally different from a conventional NDA.
- **Disaggregate and re-query**: If the intent is to evaluate a specific active ingredient — most likely **arsenic trioxide** (DrugBank: DB01169) — submit it as a standalone entry through the TxGNN pipeline.
- **Do not aggregate toxic ingredients**: Submitting lead, mercury compounds, and arsenic trioxide as a single drug entity bypasses the safety review mechanisms designed for each toxic component individually.
- **Obtain component-level safety data**: Each heavy-metal-containing ingredient requires its own toxicology review before any clinical evaluation is considered.
- **Regulatory opinion**: Seek a pre-submission meeting with FDA or equivalent authority to clarify the product's classification before investing further in any development or repurposing programme.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

