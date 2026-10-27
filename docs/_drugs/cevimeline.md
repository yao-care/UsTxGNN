---
layout: default
title: Cevimeline
parent: Model Prediction Only (L5)
nav_order: 517
evidence_level: L5
indication_count: 4
monitor_inn: "CEVIMELINE"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature"]
last_modified_at: 2026-10-14
description: "Cevimeline: predicted new indication Hypertrichosis (evidence level L5). Approved use: Not stated in the US licence data compiled for this report (generally…"
---

# Cevimeline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Cevimeline: From Xerostomia in Sjögren's Syndrome to Hypertrichosis
{: .text-alpha }

## One-Sentence Summary

Cevimeline is an oral muscarinic agonist that stimulates saliva production. It has been used for dry mouth in Sjögren's syndrome, although the US licence data compiled for this report contain no approved-indication text.
The TxGNN model predicts it may be effective for **hypertrichosis**, but **no clinical trials and no publications** currently support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US licence data compiled for this report (generally known use: dry mouth in Sjögren's syndrome) |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licences) |
| Number of NDAs | 8 (all cancelled; 1 NDA and 7 ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Based on general pharmacology, cevimeline is a muscarinic M1/M3 receptor agonist that increases exocrine gland secretion. Its efficacy in dry mouth is the basis of its original use.

No plausible mechanistic link between muscarinic agonism and hair follicle cycling or hypertrichosis is established in the available data. The high score (0.993) is a graph-based prediction only, and no trial or publication backs it. Because the original mechanism data are missing, the prediction cannot be cross-checked against them.

The other top predictions are similarly weak:
- **Ambras type hypertrichosis universalis congenita** (99.08%): a rare genetic disorder tied to chromosome 8q22 rearrangements affecting TRPS1 regulation. A drug is unlikely to correct this defect, and the prediction probably reflects network proximity to the broader hypertrichosis node.
- **Malformation syndrome with odontal and/or periodontal component** (99.07%): increased salivation could at best give symptomatic oral relief, without addressing the developmental defect.
- **Syndrome with a Dandy-Walker malformation as major feature** (99.06%): cevimeline's peripheral action has no recognized way to modify cerebellar development. This looks like a graph-level artifact.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

All eight US authorisations are oral capsules and all are listed as cancelled. The approved-indication text is not available in the compiled data.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020989 | cevimeline hydrochloride (Cosette Pharmaceuticals) | Capsule | Not available |
| ANDA216682 | Cevimeline hydrochloride (Bryant Ranch Prepack) | Capsule | Not available |
| ANDA215056 | Cevimeline hydrochloride (Aurobindo Pharma) | Capsule | Not available |
| ANDA091591 | Cevimeline hydrochloride (Hikma Pharmaceuticals USA) | Capsule | Not available |
| ANDA204746 | Cevimeline hydrochloride (Lupin Pharmaceuticals) | Capsule | Not available |

## Safety Considerations

Label warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for safety information.

- **Disease contraindications from the knowledge graph** (derived from the TxGNN knowledge graph, not from label text): asthma (including intrinsic and allergic asthma), bronchitis, myocardial infarction and coronary thrombosis, sudden cardiac arrest, heart conduction disease, angle-closure glaucoma, iritis, nephrolithiasis, cholelithiasis and cholecystitis, cholangitis (including sclerosing forms), hemoglobinopathy, acute urate nephropathy, and night-blindness disorders.
- **Drug Interactions**: 100 interactions were found; the first 20 reviewed are mostly moderate.
  - Anticholinergics (likely pharmacodynamic opposition): atropine (including ophthalmic), hyoscyamine, glycopyrronium (including topical), clidinium, dicyclomine, mepenzolate, methscopolamine.
  - Other moderate interactions: bupropion, aprepitant, lorcaserin, fenfluramine, dexfenfluramine, cimetidine, clarithromycin, clotrimazole, eliglustat, glycerol phenylbutyrate.
  - Minor: dexamethasone.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph-based model score. There are no clinical trials or publications, no plausible mechanistic link, and no currently valid US marketing authorisation. The evidence level is L5.

**To proceed, the following is needed:**
- Label warnings and contraindications from the FDA package insert (a blocking gap for safety screening)
- Mechanism of action data for cevimeline
- Preclinical evidence that muscarinic signalling affects hair follicle biology
- Route and formulation compatibility assessment for the proposed indication
- A review of the knowledge-graph contraindications (cardiopulmonary, glaucoma, biliary and renal) against the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

