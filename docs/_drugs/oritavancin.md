---
layout: default
title: Oritavancin
parent: Model Prediction Only (L5)
nav_order: 995
evidence_level: L5
indication_count: 3
monitor_inn: "ORITAVANCIN"
predicted_indications: ["Bacteroidaceae infectious disease", "ophthalmic herpes zoster", "Mycoplasma pneumoniae pneumonia"]
last_modified_at: 2026-10-14
description: "Oritavancin: predicted new indication Bacteroidaceae infectious disease (evidence level L5). Approved use: Skin disease caused by infection"
---

# Oritavancin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Oritavancin: From Skin Infection to Bacteroidaceae Infectious Disease

## One-Sentence Summary

Oritavancin is a lipoglycopeptide antibacterial, originally used to treat skin disease caused by infection.
The TxGNN model predicts it may be effective for **Bacteroidaceae infectious disease**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Skin disease caused by infection |
| Predicted New Indication | Bacteroidaceae infectious disease |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L5 |
| US Market Status | Cancelled only |
| Number of NDAs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, oritavancin is a lipoglycopeptide that inhibits bacterial cell wall synthesis (transglycosylation and transpeptidation) and disrupts membrane integrity. Its activity is mainly against Gram-positive bacteria, which is consistent with its use in skin infections.

The link to the predicted indication is weak. Bacteroidaceae are Gram-negative anaerobes with an outer membrane that glycopeptides generally cannot penetrate. The high TxGNN score (99.48%) is therefore not supported by known pharmacology. It may reflect a graph-based association, such as shared infection-related nodes, rather than real activity.

Two other top-ranked predictions are also doubtful, which suggests the model's scores for this drug should be read with caution:
- **Ophthalmic herpes zoster (score 99.03%)**: caused by a virus, and oritavancin has no known antiviral activity.
- **Mycoplasma pneumoniae pneumonia (score 99.01%)**: Mycoplasma lacks a cell wall, so cell-wall-targeting agents are intrinsically inactive.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA214155 | Kimyrsa | Lyophilized powder for injection solution | Not available (status: cancelled) |
| NDA206334 | Orbactiv | Lyophilized powder for injection solution | Not available (status: cancelled) |

Both authorizations are held by Melinta Therapeutics, LLC and are currently listed as cancelled.

## Safety Considerations

- **Drug Interactions**: 38 interactions were identified in total. The first 20 retrieved include one Major interaction and mostly Moderate ones.
  - **Major**: Heparin
  - **Moderate (examples)**: Warfarin, Ticagrelor, Cobicistat, Fostamatinib, Hydrocodone, Ethinylestradiol, Abemaciclib, Acalabrutinib, Alpelisib, Brigatinib, Cabozantinib, Crizotinib
  - **Minor**: Bortezomib

  Several of these involve anticoagulants or antiplatelet agents (heparin, warfarin, ticagrelor), so coagulation monitoring deserves attention.

Please refer to the package insert for warnings and contraindications, as these were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trial or literature support (Evidence Level L5). Known pharmacology also argues against it: glycopeptides are poorly active against Gram-negative anaerobes because of the outer membrane. Both US authorizations are cancelled, and safety label data are missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the FDA
- Detailed mechanism of action data (MOA)
- In vitro susceptibility data for oritavancin against Bacteroidaceae (e.g., Bacteroides species)
- Review of why the model gives high scores to mechanistically implausible indications (viral and cell-wall-deficient pathogens)
- Clarification of the reasons for the authorization cancellations and of the current US availability
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

