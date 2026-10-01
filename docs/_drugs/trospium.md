---
layout: default
title: Trospium
parent: Model Prediction Only (L5)
nav_order: 1270
evidence_level: L5
indication_count: 10
---

# Trospium
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Trospium: From Overactive Bladder to Irritable Bowel Syndrome

## One-Sentence Summary

Trospium is an antimuscarinic drug marketed in the US as an oral tablet and extended-release capsule. The pack's notes describe it as an overactive bladder drug, but the license records do not state an indication.
The TxGNN model predicts it may be effective for **irritable bowel syndrome (IBS)**, but **0 clinical trials** and **1 publication** (not about IBS) support this, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the license data; overactive bladder per the pack's rationale notes |
| Predicted New Indication | Irritable bowel syndrome |
| TxGNN Prediction Score | 98.04% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the listed licenses are ANDA generics) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, trospium is an antimuscarinic. It is a quaternary amine with minimal central nervous system penetration, and it is used for overactive bladder. It may be mechanistically applicable to IBS through peripheral blockade of muscarinic receptors on smooth muscle.

The reasoning is class-level: antimuscarinics reduce gut smooth-muscle spasm, which could ease the cramping and pain of IBS. This is plausible but unproven for trospium.

The only publication linked to this prediction (PMID 33890538) studies antimuscarinic use in older adults with dementia and overactive bladder. It says nothing about IBS. The very high TxGNN score (0.98) is therefore a prediction, not a finding supported by data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33890538](https://pubmed.ncbi.nlm.nih.gov/33890538/) | 2021 | Cohort | Current Medical Research and Opinion | Examined the incidence and predictors of antimuscarinic use among older adults with dementia and overactive bladder. It is not an IBS study. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA091573 | TROSPIUM CHLORIDE (Bryant Ranch Prepack) | Tablet, film coated | Not stated in the data |
| ANDA206472 | Trospium Chloride (Macleods Pharmaceuticals) | Tablet | Not stated in the data |
| ANDA091289 | Trospium Chloride (Golden State Medical Supply) | Capsule, extended release | Not stated in the data |

The pack lists 20 licenses in total but details only five records. Three of those are repeat entries of ANDA091573, which are merged into one row above.

## Safety Considerations

- **Contraindications (from the pack's rationale notes, not the safety fields)**: Trospium labeling lists uncontrolled narrow-angle glaucoma as a contraindication. Antimuscarinics can raise intraocular pressure.
- **Other concern noted in the pack**: Trospium may worsen tachycardia.

Please refer to the package insert for full warnings, contraindications, and drug interaction information. No drug interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The IBS prediction rests only on the model score and a class-level mechanistic argument. There are no IBS-specific trials or studies, and the single linked paper concerns overactive bladder.

**To proceed, the following is needed:**
- The package insert warnings and contraindications, which are currently blocking the safety screening.
- Detailed mechanism of action data, for example from DrugBank.
- IBS-specific evidence for trospium or close antimuscarinic analogues, such as clinical trials or observational studies.
- A check of the other predictions in this pack:
  - **Neurogenic bladder** has the strongest mechanistic fit (shared detrusor overactivity), but it has no evidence in the pack. Its ontology term is marked "obsolete" and should be remapped to a current term.
  - **Insomnia** trials in the pack are false-positive matches: they study the xanomeline-trospium combination (KarXT) in schizophrenia, not sleep.
  - **Glaucoma** predictions are potentially counter-therapeutic and should not be pursued.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

