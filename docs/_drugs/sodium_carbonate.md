---
layout: default
title: Sodium Carbonate
parent: Model Prediction Only (L5)
nav_order: 1168
evidence_level: L5
indication_count: 6
monitor_inn: "SODIUM CARBONATE"
predicted_indications: ["cauda equina syndrome", "anaphylaxis", "food-dependent exercise-induced anaphylaxis", "obsolete neurogenic bladder (disease)", "dry eye syndrome", "ventricular tachycardia"]
last_modified_at: 2026-10-14
description: "Sodium Carbonate: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: No approved indication text on record"
---

# Sodium Carbonate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Sodium Carbonate: From an Unspecified Original Indication to Cauda Equina Syndrome
{: .text-alpha }

## One-Sentence Summary

Sodium carbonate is an alkalinizing agent, and no approved indication is on record for it in the data compiled for this report. The TxGNN model's top-ranked prediction is **cauda equina syndrome**, but there are **0 clinical trials** and **0 publications** for this indication, so the prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication text on record |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 0.9980 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of NDAs | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Sodium carbonate is an alkalinizing, antacid-type agent. Because no original indication is recorded, its relationship to the predicted indication cannot be assessed.

Cauda equina syndrome is a compressive injury to the lumbosacral nerve roots, and it is managed surgically. Sodium carbonate has no known action on this condition. The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, and neither trials nor literature support it. On current information, no plausible mechanistic link can be identified.

### Other Predicted Indications

The model also ranked the following indications. None has enough support to change the decision.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Anaphylaxis | 0.9972 | L5 | One paper on sublingual epinephrine formulation (PMID 34600046). It does not test sodium carbonate as a treatment, and the link is indirect at best (formulation or pH adjustment). |
| 3 | Food-dependent exercise-induced anaphylaxis | 0.9963 | L5 | No mechanistic link and no studies. |
| 4 | Neurogenic bladder (obsolete ontology term) | 0.9962 | L5 | No mechanistic link. The disease term is obsolete, which lowers its value as a target. |
| 5 | Dry eye syndrome | 0.9958 | L5 | Only indirect evidence from an oral hygiene study in Sjögren's syndrome (PMID 27813150). No dry eye trials were found. |
| 6 | Ventricular tachycardia | 0.9918 | L5 | Sodium bicarbonate, a related compound, is used in some toxicologic arrhythmias. Sodium carbonate has no documented antiarrhythmic use and is a stronger alkali with irritant properties. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was found for the top-ranked indication, cauda equina syndrome. The table below lists the two papers retrieved for lower-ranked predictions.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27813150](https://pubmed.ncbi.nlm.nih.gov/27813150/) | 2017 | Clinical study (design unconfirmed) | Gerodontology | Explorative study of an alkaline spray (sodium bicarbonate and xylitol, Cariex®) combined with professional oral hygiene in patients with primary Sjögren's syndrome. The setting is oral, not ocular (dry eye syndrome, rank 5). |
| [34600046](https://pubmed.ncbi.nlm.nih.gov/34600046/) | 2021 | Preclinical/formulation study | European Journal of Pharmaceutical Sciences | Sublingual epinephrine stability and permeability, including the effect of modifying the sublingual pH, for anaphylaxis (rank 2). Sodium carbonate is not tested as a treatment. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not available | Natrum carbonicum (Boiron) | Pellet | No indication text on record (status: cancelled) |

## Safety Considerations

- **Related formulation note:** Sodium carbonate is a stronger alkali than sodium bicarbonate and has irritant and caustic properties, so systemic use raises safety concerns.

No drug interaction records were found. Please refer to the package insert for other safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All six predictions are supported only by the model score, with no clinical trials. The few papers retrieved are indirect, and no mechanistic link is identified for any indication. The only US license is cancelled and has no recorded indication, and package insert safety data are missing.

**To proceed, the following is needed:**
- Mechanism of action data for sodium carbonate
- Package insert warnings and contraindications, to allow safety screening
- A clearly documented original indication, to support similarity analysis
- Route-of-administration compatibility assessment for any candidate indication
- Direct clinical or preclinical evidence in a specific indication. Dry eye syndrome has the most indirect support so far, and the oral hygiene data would need to be confirmed and extended to the ocular setting.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

