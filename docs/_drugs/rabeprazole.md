---
layout: default
title: Rabeprazole
parent: Model Prediction Only (L5)
nav_order: 1103
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Rabeprazole: predicted new indication Smouldering systemic mastocytosis (evidence level L5). Approved use: Peptic ulcer disease, gastroesophageal reflux disease…"
---

# Rabeprazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Rabeprazole: From Peptic Ulcer and Acid-Related Disease to Smouldering Systemic Mastocytosis

## One-Sentence Summary

Rabeprazole is a proton pump inhibitor originally used for acid-related conditions such as peptic ulcer disease, gastroesophageal reflux disease, and Zollinger-Ellison syndrome.
The TxGNN model predicts it may be effective for **Smouldering systemic mastocytosis**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peptic ulcer disease, gastroesophageal reflux disease, and related acid-related conditions (no approved indication text is available in the US license records) |
| Predicted New Indication | Smouldering systemic mastocytosis |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (all licenses cancelled) |
| Number of NDAs | 7 (1 NDA and 6 ANDAs, all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, rabeprazole is a proton pump inhibitor, its efficacy in acid-related disease is established, and the knowledge graph already links it to systemic mastocytosis and mastocytosis.

The most plausible link is symptomatic. Mast cell mediators such as histamine can drive gastric acid hypersecretion and peptic disease, and acid suppression helps control these problems. This is symptom control, not activity against the underlying clonal mast cell proliferation.

The prediction therefore most likely reflects closeness to the existing mastocytosis indications in the knowledge graph rather than a new mechanism. A second prediction, lymphoadenopathic mastocytosis with eosinophilia (score 99.35%), follows the same reasoning and has no supporting trials or literature either.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020973 | Aciphex (Waylis Therapeutics LLC) | Delayed-release tablet | Not available; license cancelled |
| ANDA090678 | Rabeprazole Sodium (Lannett Company) | Delayed-release tablet | Not available; license cancelled |
| ANDA208644 | Rabeprazole Sodium (RemedyRepack) | Delayed-release tablet | Not available; license cancelled |
| ANDA204237 | Rabeprazole Sodium (Advanced Rx of Tennessee) | Delayed-release tablet | Not available; license cancelled |
| ANDA205761 | Rabeprazole Sodium (Direct Rx) | Delayed-release tablet | Not available; license cancelled |

Two further cancelled ANDAs (ANDA202376, Torrent; ANDA204179, Amneal) are also on record, making 7 in total.

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text)**: liver disease, gallbladder disease, osteoporosis, postmenopausal osteoporosis, and bone fracture. These come from knowledge-graph relationships and should be checked against the package insert.
- **Drug Interactions**: 100 interactions were found. Examples in the first 20 reviewed:
  - **Major**: acalabrutinib, atazanavir
  - **Moderate**: amikacin, amphotericin B (several formulations), amphetamine, apalutamide, aprepitant, armodafinil, bosutinib, thiazide diuretics (bendroflumethiazide, benzthiazide)
  - **Minor**: acetylsalicylic acid, axitinib

  Because the full list was not reviewed, check the complete interaction list before any development step.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a high model score. There are no registered trials or publications, the likely benefit is symptomatic acid suppression rather than disease modification, and all US licenses are cancelled.

**To proceed, the following is needed:**
- The FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data for rabeprazole
- A literature and trial search on proton pump inhibitors in mastocytosis to test whether any evidence exists beyond symptom control
- A clear definition of the target outcome (symptom control versus disease modification) and a check of route compatibility
- A review of the full drug interaction list, especially the major interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

