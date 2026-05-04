---
layout: default
title: Aconitum Napellus Whole Eupatorium Perfoliatum Flo
parent: 僅模型預測 (L5)
nav_order: 140
evidence_level: L5
indication_count: 0
---

# Aconitum Napellus Whole Eupatorium Perfoliatum Flo
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

# Multi-Ingredient Homeopathic Formula: Insufficient Data for Drug Repurposing Evaluation

## One-Sentence Summary

This submission contains a nine-ingredient homeopathic combination formula (including *Aconitum napellus*, *Gelsemium sempervirens*, *Pulsatilla vulgaris*, *Strychnos nux-vomica*, and five other botanical/mineral components), which is consistent with classical homeopathic cold and flu preparations.
The TxGNN model returned **no predicted indications** for this compound, and the formula holds **no US regulatory approvals**.
With critical data gaps across MOA, safety, and predictive evidence, this candidate **cannot proceed to repurposing evaluation** at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (no regulatory record found) |
| Predicted New Indication | None — TxGNN returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — Model prediction only; in this case, no predictions exist |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why Is This Prediction Reasonable?

No TxGNN predictions were generated for this formula, so a mechanistic plausibility analysis is not applicable.

From a compositional standpoint, this nine-ingredient formula is a classical homeopathic complex. The components — *Aconitum napellus* (sudden-onset fever), *Eupatorium perfoliatum* (influenza-type myalgia), *Ferrum phosphoricum* (early-stage inflammation), *Gelsemium sempervirens* (flu weakness and chills), *Mercurius solubilis* (catarrhal conditions), *Allium cepa* (onion, rhinitis), *Kali bichromicum* (potassium dichromate, sinusitis), *Pulsatilla vulgaris* (mucosal catarrh), and *Strychnos nux-vomica* seed (digestive and catarrhal symptoms) — are individually associated in homeopathic practice with upper respiratory tract complaints and influenza-like illness.

However, homeopathic preparations operate at ultra-dilute concentrations and lack conventional pharmacological mechanism-of-action data. Neither DrugBank pharmacology records nor peer-reviewed MOA literature were retrieved. Without a mechanistic basis that TxGNN can encode as graph relationships, the model has no pathway through which to generate repurposing candidates. This is the most likely explanation for the empty prediction output.

---

## Safety Considerations

No safety data (warnings, contraindications, or drug interactions) were retrieved for this formula through any queried source (TFDA, DrugBank DDI, standard DDI databases). This is expected for an unregistered homeopathic combination with no DrugBank ID assigned.

> Please consult primary literature and regulatory pharmacovigilance databases before any clinical use. Note that several raw botanical components in this formula carry intrinsic toxicity concerns at non-homeopathic doses: *Strychnos nux-vomica* seed contains strychnine; *Aconitum napellus* contains cardiotoxic aconitine; and potassium dichromate is a Cr(VI) compound with known genotoxic and carcinogenic properties. Homeopathic dilutions are presumed to eliminate pharmacological activity, but safety data specific to this formulation have not been verified.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model produced zero predictions for this formula, no US regulatory license exists, and all three critical data categories — original indication, mechanism of action, and safety profile — are absent. There is no evidentiary basis on which to initiate a repurposing program.

**To proceed, the following is needed:**

- **Identify or confirm the proprietary brand name** of this homeopathic formula to locate any existing regulatory filings (e.g., FDA OTC Homeopathic Drug, or equivalent registrations in other markets)
- **Establish a DrugBank ID** (currently null) or an equivalent structured identifier so that TxGNN can locate the node in the knowledge graph
- **Resolve MOA data gap (DG002)**: Query DrugBank and primary literature for pharmacological characterisation of each active component at non-homeopathic concentrations
- **Resolve safety data gap (DG001)**: Obtain the product package insert (if any) to populate warnings and contraindications
- **Re-run TxGNN** after the DrugBank mapping is established; if the formula cannot be mapped as a single entity, consider evaluating each active ingredient individually and aggregating predictions
- **Assess regulatory pathway**: Homeopathic combination products face specific regulatory constraints (e.g., FDA Homeopathic Drug Products guidance); a repurposing strategy must account for these before any submission planning
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

