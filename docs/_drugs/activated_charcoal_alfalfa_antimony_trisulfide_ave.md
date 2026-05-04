---
layout: default
title: Activated Charcoal Alfalfa Antimony Trisulfide Ave
parent: 僅模型預測 (L5)
nav_order: 162
evidence_level: L5
indication_count: 0
---

# Activated Charcoal Alfalfa Antimony Trisulfide Ave
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

# Multi-Component Compound (22 Ingredients): No Repurposing Prediction Available

## One-Sentence Summary

This formulation is a 22-ingredient combination of digestive enzymes, bitter botanicals, and traditional herbal/homeopathic components—including pancrelipase, pepsin, gentian, licorice, cascara, and nux vomica—with no registered original indication on record. The TxGNN model was unable to generate a repurposing prediction because the compound lacks a DrugBank ID and cannot be anchored in the knowledge graph. No clinical trial or literature evidence is currently linked to this formulation as a unified entity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Unknown (no registration found) |
| Predicted New Indication | None — model could not process |
| TxGNN Prediction Score | N/A |
| Evidence Level | Not Evaluable |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

No TxGNN repurposing prediction was generated for this compound. The TxGNN pipeline requires a DrugBank ID to locate a drug node within the knowledge graph and compute disease associations. Since this multi-component formulation has no DrugBank ID, the model cannot link it to any disease node, making score computation impossible.

Based on its ingredient profile, this appears to be a traditional gastrointestinal/hepatobiliary compound, likely of homeopathic or phytotherapeutic origin. Several components are hallmarks of classical homeopathic preparations: *Strychnos nux-vomica* seed (nux vomica), *Lycopodium clavatum* spore, Carbo Animalis (animal charcoal), Chelidonium Majus, and Berberis Vulgaris are all listed in the Homeopathic Pharmacopoeia of the United States (HPUS). The concurrent presence of pancrelipase, pepsin, and ox bile (*Bos taurus* bile) suggests a digestive enzyme supplement function, while gentian root, cascara (*Frangula purshiana* bark), star anise, and licorice are conventional bitter tonics and carminatives. Indole and skatole—volatile intestinal fermentation byproducts—also appear in homeopathic bowel preparations.

To enable a formal TxGNN repurposing analysis, the compound would need to be decomposed into individual ingredients for separate evaluation, or alternatively, a lead active component (e.g., berberine from *Berberis vulgaris*, or glycyrrhizin from *Glycyrrhiza glabra*) would need to be designated as the primary entity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this multi-component formulation as a unified entity.

---

## Literature Evidence

Currently no related literature available for this exact multi-component formulation.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note on Nux Vomica**: *Strychnos nux-vomica* seed contains strychnine, which is toxic at non-homeopathic doses. If this is a conventional (non-homeopathic) formulation, the concentration of nux vomica extract should be verified against safe upper limits before any clinical use evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline cannot evaluate this compound in its current form. Without a DrugBank ID, an original indication, or any predicted indication, there is no basis for a repurposing evaluation.

**To proceed, the following is needed:**

- **Clarify regulatory classification**: Determine whether this is a homeopathic preparation (HPUS-listed), a phytotherapeutic combination, or a conventional OTC digestive enzyme supplement — each follows a different regulatory and evidence pathway
- **Assign a DrugBank ID or decompose into individual ingredients**: Evaluate each of the 22 active components separately through TxGNN; leading candidates (berberine, glycyrrhizin, pancrelipase, pepsin) already have DrugBank entries
- **Identify the original registered indication**: Even an informal use case (e.g., dyspepsia, digestive insufficiency, liver support) is needed to anchor the repurposing analysis
- **Obtain complete safety data**: Retrieve the full package insert to document warnings, contraindications, and dosing limits — especially regarding nux vomica (strychnine content) and antimony trisulfide
- **Confirm US market status**: A TFDA query returned 0 results and DDI lookup was not found; an independent US FDA Orange Book search should confirm whether any NDA or ANDA exists under a brand name
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

