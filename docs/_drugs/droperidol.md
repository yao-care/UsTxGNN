---
layout: default
title: Droperidol
parent: Model Prediction Only (L5)
nav_order: 630
evidence_level: L5
indication_count: 10
monitor_inn: "DROPERIDOL"
predicted_indications: ["Tourette syndrome", "trichotillomania", "manic bipolar affective disorder", "attention deficit hyperactivity disorder, inattentive type", "nephrogenic syndrome of inappropriate antidiuresis", "attention deficit-hyperactivity disorder", "headache disorder", "common cold", "hypertrichosis (disease)", "specific developmental disorder"]
last_modified_at: 2026-10-30
description: "Droperidol: predicted new indication Tourette syndrome (evidence level L5). Approved use: Not recorded in the local data"
---

# Droperidol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Droperidol: Tourette syndrome
{: .text-alpha }

## One-Sentence Summary

Droperidol is a butyrophenone dopamine D2 antagonist that has been sold in the US as an injectable solution. The TxGNN model predicts it may be effective for **Tourette syndrome**, but **no clinical trials and no publications** were found for this prediction, so it rests on a computational score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Tourette syndrome |
| TxGNN Prediction Score | 0.9989 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 2 of 2) |
| Number of FDA Applications | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Droperidol is known to be a butyrophenone neuroleptic that blocks dopamine D2 receptors. This is the same class as haloperidol, an established treatment for Tourette syndrome.

Tourette syndrome is a tic disorder in which dopamine D2 blockade is a recognized treatment approach. The mechanistic rationale is therefore plausible. However, droperidol is an injectable, mainly sedating agent. Tourette syndrome usually needs long-term oral treatment, and no study of droperidol in this condition was retrieved. The high TxGNN score should be read as a hypothesis, not as evidence of benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA208197 (Hikma Pharmaceuticals USA Inc.) | Droperidol | Injection, solution | Not listed; status cancelled |
| ANDA072123 (American Regent, Inc.) | Droperidol | Injection, solution | Not listed; status cancelled |

Only injectable solutions are on record. No oral formulation appears in the data.

---

## Safety Considerations

Package-insert warnings and contraindications were not available for this report. The items below come from other sources and should be read in that light.

- **Knowledge-graph contraindication signals** (from drug-disease edges in the TxGNN knowledge graph, not from label text). These include cardiac and rhythm conditions: long QT syndrome (including the familial form), torsades de pointes, hypertension, orthostatic hypotension, and postural orthostatic tachycardia syndrome. They also include neurological conditions (basal ganglia disease, focal hand dystonia, blepharospasm, multiple system atrophy), respiratory conditions (COPD, respiratory failure), liver, kidney and gallbladder disease, potassium deficiency, and pheochromocytoma.
- **Drug interactions**: 100 interactions were recorded. Those rated **Major** among the 20 retrieved include:
  - hydrocortisone
  - morphine
  - naloxone
  - clarithromycin
  - dolasetron
  - amphotericin B (conventional, lipid complex, cholesteryl sulfate and liposomal forms)
  - picosulfuric acid
  - polyethylene glycol 3350 with electrolytes

  Moderate interactions include famotidine, epinephrine, loperamide, bisacodyl, dronabinol and castor oil.
- **Cardiac risk**: the literature collected for other predicted indications raises QT prolongation and case reports of respiratory distress as concerns. This is relevant to any long-term or repeated use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Tourette syndrome prediction has a very high model score and a plausible D2-antagonist rationale. The QT-related safety profile and the injectable-only formulation do not fit chronic tic management.

**To proceed, the following is needed:**
- A literature and trial search specific to droperidol in tic disorders, plus a comparison against established D2 antagonists such as haloperidol
- Mechanism-of-action data and the FDA package insert warnings and contraindications
- A route and formulation assessment, since only injectable forms are on record and chronic use would likely need an oral option
- A cardiac safety plan (QT/ECG monitoring)

**Note on other predicted indications:** among the other predictions in the data, **headache disorder** (rank 7) has the most support. It has one registered trial (NCT01406860, terminated with 19 participants), a randomized placebo-controlled trial of droperidol in acute migraine (PMID 12552051), and several reviews. It reaches evidence level L3. If the aim is to prioritize droperidol repurposing candidates, that indication merits a dedicated evaluation, with QT-risk guardrails and a check of the market status.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

