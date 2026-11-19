---
layout: default
title: Golodirsen
parent: Model Prediction Only (L5)
nav_order: 759
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-12
monitor_inn: "GOLODIRSEN"
predicted_indications: ["distal myopathy, Welander type", "nebulin-related early-onset distal myopathy", "X-linked myopathy with postural muscle atrophy"]
description: "Golodirsen: predicted new indication Distal myopathy, Welander type (evidence level L5). In the US: 1 FDA application (1 active)"
---

# Golodirsen
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

## Golodirsen: Distal myopathy, Welander type
{: .text-alpha }

## One-Sentence Summary

Golodirsen was originally used to treat Duchenne muscular dystrophy (DMD) in patients whose disease is amenable to exon 53 skipping.
The TxGNN model predicts it may be effective for **distal myopathy, Welander type**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Distal myopathy, Welander type |
| TxGNN Prediction Score | 0.9911 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 1 of 1) |
| Number of FDA Applications | 1 (active: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for golodirsen: "Golodirsen is designed to bind to exon 53 of dystrophin pre-mRNA resulting in exclusion of this exon during mRNA processing in patients with genetic mutations that are amenable to exon 53 skipping. Exon 53 skipping is intended to allow for production of an internally truncated dystrophin protein in patients with genetic mutations that are amenable to exon 53 skipping." ([DailyMed: Vyondys 53 (golodirsen) prescribing information, Sarepta Therapeutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=35c227d1-5b24-44b0-b5d3-f0f6b1c46bd5), label version 2025-03-13; accessed 2026-11-19.) Based on known pharmacology, golodirsen is an antisense phosphorodiamidate morpholino oligomer that causes exon 53 skipping in DMD pre-mRNA, allowing production of a shortened but partly functional dystrophin protein.

Welander distal myopathy is linked to a founder variant in TIA1, a gene involved in RNA binding and stress granule biology. This is not a dystrophin defect, and it is not an exon 53-skippable lesion. No mechanistic link beyond the high prediction score has been established. The score most likely reflects network proximity between muscle diseases rather than a shared pathogenic mechanism.

The other top predictions are also weak. Each lacks trials and literature:

- **Nebulin-related early-onset distal myopathy** (score 0.9907): caused by NEB variants affecting thin filament function, with no exon 53 target.
- **X-linked myopathy with postural muscle atrophy** (score 0.9902): linked to VMA21 and autophagy dysfunction, with no plausible basis for golodirsen.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA211970 | Vyondys 53 | Injection | Not listed in the compiled data (status: valid; manufacturer: Sarepta Therapeutics, Inc.) |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or literature (evidence level L5), and the mechanism of golodirsen, which is specific to dystrophin exon 53 skipping, does not apply to the TIA1-related Welander distal myopathy.

<!-- review:begin us-lic-20261031-golodirsen-1 -->

> **Review correction (2026-10-31)**: Originally stated: "The prediction has no supporting clinical trials or literature (evidence level L5), and the mechanism of golodirsen, which is specific to dystrophin exon 53 skipping, does not apply to the TIA1-related Welander distal myopathy. In addition, the only US license is cancelled, and the package insert safety data has not been obtained." Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-10-31). The FDA data list 1 FDA application or NDC listing for this drug, 1 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261031-golodirsen-1 -->

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (currently a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Any preclinical or mechanistic evidence showing that an exon 53-skipping oligomer could affect TIA1-related pathology
- Confirmation of the current US marketing status of Vyondys 53

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-10-31 | Removed: "In addition, the only US license is cancelled, and the package insert safety data has not been obtained" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-19 | "Detailed mechanism of action data is not available in the compiled data" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Vyondys 53 (golodirsen) prescribing information, Sarepta Therapeutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=35c227d1-5b24-44b0-b5d3-f0f6b1c46bd5) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

