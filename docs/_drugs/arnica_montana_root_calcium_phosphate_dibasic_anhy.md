---
layout: default
title: Arnica Montana Root Calcium Phosphate Dibasic Anhy
parent: 僅模型預測 (L5)
nav_order: 405
evidence_level: L5
indication_count: 0
---

# Arnica Montana Root Calcium Phosphate Dibasic Anhy
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

# Arnica/Calendula/Hypericum Multi-Ingredient Homeopathic Preparation: Insufficient Data for Repurposing Analysis

## One-Sentence Summary

This is a complex multi-ingredient homeopathic/botanical preparation containing eight components — including Arnica Montana Root, Calendula Officinalis, Comfrey Root, and Hypericum Perforatum — with classical uses in musculoskeletal and wound-healing applications.
However, the TxGNN model returned **no predicted new indications** for this compound, as it could not be matched to a DrugBank entry.
As a result, this evaluation is based on structural data only, with **no clinical trial or literature evidence** linked through the automated pipeline.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indications on record |
| Predicted New Indication | None (TxGNN mapping failed) |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — Model prediction unavailable; no supporting studies identified |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN prediction was generated for this compound. The pipeline failed to resolve a DrugBank ID for this multi-ingredient formulation, which prevented knowledge graph traversal and deep learning scoring.

The eight ingredients — Arnica Montana Root, Calcium Phosphate Dibasic Anhydrous, Calendula Officinalis Flowering Top, Comfrey Root (Symphytum), Hypericum Perforatum, Oryctolagus Cuniculus Spinal Cord (rabbit spinal cord, a homeopathic organo-preparation), Pulsatilla Vulgaris, and Ruta Graveolens Flowering Top — are individually associated in traditional and homeopathic medicine with inflammation, soft-tissue trauma, nerve pain, and musculoskeletal injury. Combination products of this profile (e.g., Traumeel, Zeel) have been used in integrative oncology supportive care and sports medicine.

Detailed mechanism of action data is not available in this Evidence Pack. Without a DrugBank ID and a resolved MOA, it is not possible to establish a mechanistic rationale for any specific new indication at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered via automated pipeline.

> **Note:** Manual searches on ClinicalTrials.gov using individual ingredient names (e.g., "Arnica Montana," "Traumeel," "Hypericum Perforatum") may yield relevant results and are recommended as a remediation step.

---

## Literature Evidence

Currently no related literature available via automated pipeline.

> **Note:** PubMed manual searches for individual components and combination product brand names are recommended to supplement this gap.

---

## Safety Considerations

Please refer to the package insert for safety information.

> No key warnings, contraindications, or drug interaction data were available in this Evidence Pack. All safety fields were flagged as data gaps. Given that several ingredients (e.g., Comfrey Root / Symphytum, Hypericum Perforatum) have known pharmacological activity and potential herb–drug interactions, a manual safety review is strongly recommended before any clinical use assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline could not generate any prediction because this multi-ingredient homeopathic formulation lacks a DrugBank ID, preventing knowledge graph and deep learning analysis. Without a predicted indication and without any linked evidence, there is no basis for a repurposing recommendation at this time.

**To proceed, the following is needed:**

- **Resolve DrugBank mapping:** Either identify the closest single active ingredient with an established DrugBank ID (e.g., Hypericum Perforatum → DB00456), or register this combination as a new DrugBank entry to enable graph traversal.
- **Define original indication:** Determine the clinical indication this preparation was historically used or registered for (e.g., musculoskeletal pain, post-surgical bruising), to provide context for repurposing direction.
- **Manual safety review:** Investigate herb–drug interactions for Hypericum Perforatum (a known CYP3A4 inducer) and pyrrolizidine alkaloid content in Comfrey Root (hepatotoxicity risk).
- **Manual literature scan:** Search PubMed and ClinicalTrials.gov using individual ingredient names and known brand equivalents (Traumeel, Zeel) for relevant efficacy and safety data.
- **Re-run TxGNN pipeline** after DrugBank ID is resolved to obtain a formal prediction score and evidence linkage.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

