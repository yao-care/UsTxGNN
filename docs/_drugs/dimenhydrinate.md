---
layout: default
title: Dimenhydrinate
parent: Model Prediction Only (L5)
nav_order: 610
evidence_level: L5
indication_count: 2
monitor_inn: "DIMENHYDRINATE"
predicted_indications: ["allergic urticaria", "cold urticaria"]
last_modified_at: 2026-11-12
description: "Dimenhydrinate: predicted new indication Allergic urticaria (evidence level L5). Approved use: Not recorded in the local data"
---

# Dimenhydrinate
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

## Dimenhydrinate: Allergic urticaria
{: .text-alpha }

## One-Sentence Summary

Dimenhydrinate was originally used to treat motion sickness and vertigo of central nervous system origin.
The TxGNN model predicts it may be effective for **allergic urticaria**,
but currently there are **0 clinical trials** and only **1 publication** (a pharmacokinetic study, not an efficacy study) supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 0.9974 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 1 of 9; OTC monograph / unapproved listings: 33) |
| Number of FDA Applications | 9 (active: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, dimenhydrinate is a salt of diphenhydramine and 8-chlorotheophylline. Diphenhydramine is a first-generation H1 receptor antagonist, and its efficacy in motion sickness and vertigo is established.

H1 antagonism is a well-established way to relieve histamine-mediated urticaria symptoms, so the prediction is biologically plausible and consistent with the high TxGNN score. However, diphenhydramine itself is already used for allergic conditions. The signal therefore reflects the known activity of the active ingredient rather than a novel repurposing finding.

Practical value is also limited.

A second predicted indication, **cold urticaria** (score 0.9924, evidence level L5), rests on the same H1 antagonism reasoning. It has no clinical trials and no literature, so it is supported by model prediction alone and is also on Hold.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30779257](https://pubmed.ncbi.nlm.nih.gov/30779257/) | 2019 | Pharmacokinetic study (in dogs) | Veterinary Dermatology | Compared diphenhydramine after oral and intravenous dosing with oral dimenhydrinate, and its effect on histamine-induced wheal formation. Shows dimenhydrinate delivers diphenhydramine systemically, but does not evaluate efficacy in urticaria. |

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA040519 | DIMENHYDRINATE | FRESENIUS KABI USA | Injectable; injection | Valid |
| ANDA080615 | DIMENHYDRINATE | WATSON LABS TEVA | Injectable; injection | Discontinued in Drugs@FDA |
| ANDA080715 | DIMENHYDRINATE | ALRA | Liquid; oral | Discontinued in Drugs@FDA |
| ANDA080841 | DIMENHYDRINATE | HEATHER | Tablet; oral | Discontinued in Drugs@FDA |
| ANDA083531 | DIMENHYDRINATE | WATSON LABS | Injectable; injection | Discontinued in Drugs@FDA |

Showing 5 of 42 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

## Safety Considerations

- **Contraindications (associations learned by the TxGNN model (deep learning), not label text)**: The TxGNN model (deep learning) links dimenhydrinate with caution or contraindication in the following conditions, which may reflect similarities the model learned between related diseases, not biological evidence:
  - Cardiovascular: hypertension, hypotension, acute coronary syndrome, coronary artery disease, myocardial infarction, coronary thrombosis
  - Hepatic and gastrointestinal: liver disease, gallbladder disease, peptic ulcer disease, pyloric stenosis
  - Metabolic and endocrine: diabetes mellitus, diabetic ketoacidosis, hyperglycemia, hyperthyroidism (including Graves disease and thyrotoxicosis), gout, hypophosphatemia
  - Haematological: thrombocytopenia, blood coagulation disease, hemoglobinopathy
  - Eye: angle-closure glaucoma, ocular hypertension
  - Urinary: benign prostatic hyperplasia, bladder neck obstruction
  - Other: substance abuse/dependence
- **Drug Interactions**: 67 interactions were recorded. The two rated **Major** are:
  - Potassium citrate
  - Potassium chloride

  Many others are rated Moderate, mostly anticholinergic agents (e.g., atropine, scopolamine, hyoscyamine, dicyclomine, glycopyrronium, trospium) and opioids or other central nervous system and gastrointestinal-motility agents (e.g., morphine, opium, loperamide, metoclopramide, nabilone, eluxadoline, prucalopride).

Package insert warnings and contraindications were not available for this report; please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is biologically plausible through H1 antagonism, but no clinical trials exist for dimenhydrinate in urticaria, and the single publication is a pharmacokinetic study that does not assess efficacy. The signal mainly reflects the known activity of diphenhydramine.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (required for safety screening)
- Mechanism of action data
- Clinical efficacy data (trials or observational studies) for dimenhydrinate or diphenhydramine in allergic urticaria, and in cold urticaria
- Assessment of the added value over second-generation antihistamines, given the sedation and anticholinergic burden
- Clarification of route and formulation availability

<!-- review:begin us-lic-20261105-dimenhydrinate-1 -->

> **Review correction (2026-11-05)**: Originally stated: "Clarification of route and formulation availability, since the drug is currently marketed with 2 valid US authorizations" Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-05). The FDA data list 9 FDA applications or NDC listings for this drug, 1 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261105-dimenhydrinate-1 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "since the drug is currently marketed with 2 valid US authorizations" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

