---
layout: default
title: Meclizine
parent: Model Prediction Only (L5)
nav_order: 893
evidence_level: L5
indication_count: 6
monitor_inn: "MECLIZINE"
predicted_indications: ["allergic urticaria", "common cold", "nasal cavity disease", "pharyngitis", "acute laryngopharyngitis", "cold urticaria"]
last_modified_at: 2026-10-28
description: "Meclizine: predicted new indication Allergic urticaria (evidence level L5). Approved use: Central nervous system origin vertigo"
---

# Meclizine
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

## Meclizine: From Vertigo and Motion Sickness to Allergic Urticaria
{: .text-alpha }

## One-Sentence Summary

Meclizine is a first-generation antihistamine originally used to treat vertigo of central nervous system origin and motion sickness.
The TxGNN model predicts it may be effective for **allergic urticaria**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score and drug-class reasoning alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Central nervous system origin vertigo; motion sickness |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 0.9967 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 7) |
| Number of NDAs | 7 licenses listed (all cancelled) |
| Recommended Decision | Hold |

Other predicted indications, all also at L5 with a Hold recommendation:

| Rank | Predicted Indication | TxGNN Score |
|------|------|------|
| 2 | Common cold | 0.9949 |
| 3 | Nasal cavity disease | 0.9948 |
| 4 | Pharyngitis | 0.9945 |
| 5 | Acute laryngopharyngitis | 0.9937 |
| 6 | Cold urticaria | 0.9922 |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. Based on known information, meclizine is a first-generation H1-antihistamine with anticholinergic activity. Its efficacy in vertigo and motion sickness is established, and mechanistically, histamine-receptor blockade may be applicable to histamine-mediated conditions such as allergic urticaria.

The link between the original and new indications is indirect. Vertigo and motion sickness are treated mainly through central antihistaminic and anticholinergic effects, whereas urticaria is driven by histamine release in the skin. Both share the H1-receptor pathway, which is why the prediction is biologically plausible. However, this reasoning comes from drug class and the model prediction, not from drug-specific evidence.

There are also practical concerns. Established H1-antihistamines already exist for urticaria, including newer non-sedating agents that are generally preferred, so the added value of meclizine is unclear. For respiratory-tract predictions (common cold, pharyngitis, laryngopharyngitis, nasal cavity disease), any benefit would be symptomatic only, such as drying of secretions, and would not address the underlying cause.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

All seven licenses in the data compiled for this report are cancelled. No approved indication text is recorded for any of them.

| Authorization Number | Product Name | Dosage Form | Status |
|---------|------|------|-----------|
| M009 | Dramamine Less Drowsy Meclizine Hydrochloride | Tablet | Valid |
| NDA010721 | Meclizine Hydrochloride | Tablet | Valid |
| ANDA213957 | Meclizine Hydrochloride | Tablet | Valid |
| part336 | Motion Sickness Relief | Chewable tablet | Valid |
| ANDA201451 | Meclizine Hydrochloride | Tablet | Valid |

Two further cancelled licenses are not shown: M002 (Motion Sickness Relief, film-coated tablet) and ANDA040659 (Meclizine Hydrochloride, tablet). All available forms are oral.

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: benign prostatic hyperplasia, angle-closure glaucoma, pyloric stenosis, and bladder neck obstruction. These are consistent with the drug's anticholinergic activity.
- **Drug Interactions**: 100 interactions were identified. The ones listed below are the most notable.
  - **Major**: potassium citrate and potassium chloride.
  - **Moderate**: anticholinergics (hyoscyamine, atropine, glycopyrronium, dicyclomine, trospium, clidinium, mepenzolate, methscopolamine), opioids (morphine, opium, loperamide), and others including metoclopramide, nabilone, eliglustat, eluxadoline, and glycerol phenylbutyrate. Additive anticholinergic and sedative effects are the main concern.

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for complete safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction (score 0.9967) is supported only by class-level reasoning, with no clinical trials or publications for meclizine in this indication. The drug is marketed in the US with 7 valid licenses, and effective alternatives already exist for urticaria.

**To proceed, the following is needed:**
- Literature and trial searches specific to meclizine in urticaria (and the other predicted indications)
- Mechanism of action data to support the mechanistic link
- Package insert warnings and contraindications for formal safety screening
- A comparison against established non-sedating antihistamines to show added value
- Assessment of the current US market and regulatory pathway, given that the drug is marketed with 7 valid licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

