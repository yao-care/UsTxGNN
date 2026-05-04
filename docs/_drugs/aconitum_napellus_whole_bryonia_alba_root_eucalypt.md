---
layout: default
title: Aconitum Napellus Whole Bryonia Alba Root Eucalypt
parent: 僅模型預測 (L5)
nav_order: 135
evidence_level: L5
indication_count: 0
---

# Aconitum Napellus Whole Bryonia Alba Root Eucalypt
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

# Homeopathic Multi-Component Combination (Aconitum/Bryonia/Pelargonium): TxGNN Prediction Unavailable

## One-Sentence Summary

This submission contains a complex 8-component homeopathic botanical combination — including *Aconitum napellus*, *Bryonia alba*, *Pelargonium sidoides*, and *Gelsemium sempervirens* — classically associated with influenza-like illness and upper respiratory tract infections.
The TxGNN model was **unable to generate any repurposing predictions** for this candidate, most likely because the combination lacks a standard DrugBank identifier required for knowledge graph traversal.
As a result, **no evidence-based repurposing direction can be established** at this time, and the overall assessment is classified as **Hold** pending structural data remediation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not established (no regulatory approvals on record) |
| Predicted New Indication | Not available — TxGNN returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — model prediction unavailable; no supporting studies for the combination |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN prediction was generated for this candidate, so a standard mechanism-to-indication inference cannot be made.

The 8 components are all well-known homeopathic materia medica ingredients. Based on their classical indications and the limited conventional pharmacology available:

- **Pelargonium sidoides** (EPs 7630 extract) is the most evidence-backed component, with multiple randomised controlled trials supporting its use in **acute bronchitis and upper respiratory tract infections**. It appears to act via immunomodulatory and direct antiviral mechanisms.
- **Eupatorium perfoliatum**, **Gelsemium sempervirens**, and **Aconitum napellus** are traditionally indicated for **influenza-like illness** (fever, myalgia, chills, fatigue).
- **Bryonia alba** and **Phosphorus** target cough and lower respiratory symptoms.
- **Eucalyptus globulus** is associated with mucolytic and mild antimicrobial activity in the upper airways.
- **Ipecac** (in sub-emetic homeopathic dose) is traditionally used for nausea and spasmodic cough.

As a combination, the product profile is most consistent with **acute respiratory infections / influenza-like illness (ILI)**, but this inference is based on component-level knowledge, not on TxGNN graph scoring. No repurposing direction beyond this original cluster can be formally proposed without a valid drug node in the knowledge graph.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this multi-component combination as a single entity.

> **Note:** Individual components have been investigated separately. Pelargonium sidoides (EPs 7630) has the strongest trial base (acute bronchitis, URTI). Searches against the combination as a whole returned no matching NCT records.

---

## Literature Evidence

Currently no related literature available for this combination as a unified drug entity.

> Individual component literature (particularly for Pelargonium sidoides) exists but is not attributable to the combination product without a consolidated DrugBank or CAS identifier.

---

## Safety Considerations

Please refer to the package insert for safety information.

> All safety fields (key warnings, contraindications, drug-drug interactions) returned no data for this combination. Because several components carry known pharmacological risks in non-homeopathic doses — notably **Aconitum napellus** (cardiotoxic alkaloids), **Gelsemium sempervirens** (strychnine-related alkaloids), and **Ipecac** (emetine cardiotoxicity) — a formal toxicology review is strongly recommended before any clinical development proceeds.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline requires a resolvable DrugBank ID to anchor the drug node in the knowledge graph; because this combination carries no DrugBank identifier and no original indication record, the model returned zero predictions. Without at least one prediction, there is no repurposing hypothesis to evaluate.

**To proceed, the following is needed:**

1. **Assign a DrugBank ID or decompose into individual components** — Run TxGNN separately for each of the 8 components (especially Pelargonium sidoides DB09228 and others with known IDs) and aggregate predictions at the combination level.
2. **Establish original indication** — Document the traditional or regulatory indication for this combination in at least one jurisdiction (e.g., Germany's Commission E monograph, EMA HMPC opinion, or published homeopathic pharmacopoeia entry).
3. **Safety review** — Given the presence of *Aconitum*, *Gelsemium*, and *Ipecac*, obtain a formal toxicology assessment covering dose-dependent risks before any repurposing direction is pursued.
4. **Obtain package insert / SPC** — Required to satisfy the blocking data gap (DG001) and enable S1 safety evaluation.
5. **MOA mapping** — Query DrugBank for each individual component to populate the mechanism-of-action field (DG002) and support future knowledge graph traversal.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

