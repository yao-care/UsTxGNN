---
layout: default
title: Amifampridine
parent: Model Prediction Only (L5)
nav_order: 324
evidence_level: L5
indication_count: 2
monitor_inn: "AMIFAMPRIDINE"
predicted_indications: ["glaucoma", "acute intermittent porphyria"]
last_modified_at: 2026-11-12
description: "Amifampridine: predicted new indication Glaucoma (evidence level L5). Approved use: Lambert-Eaton myasthenic syndrome"
---

# Amifampridine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Amifampridine: From Lambert-Eaton Myasthenic Syndrome to Glaucoma
{: .text-alpha }

## One-Sentence Summary

Amifampridine (3,4-diaminopyridine) was originally used to treat Lambert-Eaton myasthenic syndrome (LEMS).
The TxGNN model predicts it may be effective for **glaucoma**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on computation alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Lambert-Eaton myasthenic syndrome |
| Predicted New Indication | Glaucoma |
| TxGNN Prediction Score | 0.9971 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 2 of 2) |
| Number of FDA Applications | 2 (active: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the data compiled for this report. Based on known pharmacology, amifampridine is a voltage-gated potassium channel blocker. It prolongs presynaptic depolarization, which increases calcium influx and acetylcholine release at the neuromuscular junction. This is how it relieves muscle weakness in LEMS.

A possible link to glaucoma is modulation of potassium channel activity or neuronal excitability in retinal ganglion cells. This link is **speculative**. Potassium channel blockade could also affect ocular tissues in unpredictable ways, including intraocular pressure, so even the direction of any effect is unknown. The high TxGNN score is a computational output only and is not backed by trials or publications.

A second prediction, **acute intermittent porphyria** (score 0.9932, also L5, Hold), was also generated. Amifampridine might theoretically ease the weakness of neurovisceral attacks, but it does not address the underlying heme biosynthesis defect. It also lowers the seizure threshold, which is a significant concern because seizures can occur during porphyric attacks and many anticonvulsants are restricted in this condition.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA217996 | AMIFAMPRIDINE PHOSPHATE | LUPIN | Tablet; oral | Valid |
| NDA208078 | FIRDAPSE | CATALYST PHARMS | Tablet; oral | Valid |

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 68 interactions were identified. The most clinically relevant listed are:
  - **Major**: Bupropion
  - **Moderate** (examples): corticosteroids (hydrocortisone, betamethasone, dexamethasone, prednisolone, prednisone); stimulants and anorectics (phentermine, diethylpropion, mazindol, sibutramine, fenfluramine, dexfenfluramine, ephedrine); opioids (morphine, opium); others (levofloxacin, metoclopramide, dronabinol, polyethylene glycol 3350 with electrolytes)
- For key warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The glaucoma prediction has a high model score but no clinical trials, no literature, and only a speculative mechanism (Evidence Level L5). The effect of potassium channel blockade on ocular tissue is unclear.

<!-- review:begin us-lic-20261106-amifampridine-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The effect of potassium channel blockade on ocular tissue is unclear. The only US authorization on record is also cancelled." Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 2 FDA applications or NDC listings for this drug, 2 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-amifampridine-1 -->

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are required for safety screening
- Detailed mechanism of action data
- Preclinical evidence (for example, effects on retinal ganglion cell excitability and intraocular pressure)
- Assessment of route compatibility, since the drug is currently available only as an oral tablet, and of similarity to the original indication
- A seizure-risk assessment if the porphyria prediction is pursued

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "The only US authorization on record is also cancelled" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

