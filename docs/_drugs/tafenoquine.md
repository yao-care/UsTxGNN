---
layout: default
title: Tafenoquine
parent: Model Prediction Only (L5)
nav_order: 1193
evidence_level: L5
indication_count: 1
monitor_inn: "TAFENOQUINE"
predicted_indications: ["Smouldering systemic mastocytosis"]
last_modified_at: 2026-11-12
description: "Tafenoquine: predicted new indication Smouldering systemic mastocytosis (evidence level L5). Approved use: Not recorded in the local data"
---

# Tafenoquine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Tafenoquine: Smouldering systemic mastocytosis
{: .text-alpha }

## One-Sentence Summary

Tafenoquine is an antimalarial drug, originally used to treat and prevent malaria.
The TxGNN model predicts it may be effective for **Smouldering Systemic Mastocytosis**,
but **no clinical trials and no publications** currently support this direction, so the prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Smouldering systemic mastocytosis |
| TxGNN Prediction Score | 0.9905 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 2 of 2; OTC monograph / unapproved listings: 1) |
| Number of FDA Applications | 2 (active: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, tafenoquine is an 8-aminoquinoline antimalarial, and its efficacy in malaria has been established. Any mechanistic link to smouldering systemic mastocytosis cannot be established from the data compiled for this report.

The TxGNN score is very high (0.9905), but it comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Possible links to mast cell disease, such as effects on KIT-driven mast cell proliferation, oxidative stress, or lysosomal pathways, are speculative and not supported by any evidence gathered here. Malaria and smouldering systemic mastocytosis are also biologically very different diseases (a parasitic infection versus a clonal mast cell neoplasm), so the relationship between the original and new indication is not apparent.

Mechanistic validation, such as in vitro mast cell assays and KIT D816V models, would be required before any further consideration.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| NDA210607 | ARAKODA | 60 DEGREES PHARMS | Tablet; oral | Valid |
| NDA210795 | KRINTAFEL | GLAXOSMITHKLINE | Tablet; oral | Valid |
| NDC 71475-258 | Kodatef | 60 Degrees Pharmaceuticals, INC | Tablet, film coated | NDC listing, no FDA application (unapproved drug for use in drug shortage) |

<!-- licenses:end -->

## Cytotoxicity

Not applicable. Tafenoquine is not an antineoplastic drug, and the predicted indication is a neoplasm for which no supporting evidence exists. This section is therefore omitted from the assessment.

## Safety Considerations

- **Drug Interactions**: 21 interacting drugs were identified (all from the DDInter database).
  - **Major (5)**: Nitrous acid, Dofetilide, Prilocaine, Typhoid vaccine (live), and one further entry in the same category as listed in the interaction data.
  - **Moderate (16)**: including Metformin, Clofarabine, Dalfampridine, Guanfacine, Dapsone (systemic and topical), and several local anaesthetics (lidocaine, benzocaine, tetracaine, cocaine, proparacaine, oxybuprocaine, cinchocaine in topical, ophthalmic, or nasal forms).

Please refer to the package insert for warnings and contraindications, as these were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score (Evidence Level L5), with no clinical trials, no literature, no mechanism of action data, and no clear biological connection between malaria and smouldering systemic mastocytosis. In addition, label safety data are missing.

<!-- review:begin us-lic-20261106-tafenoquine-1 -->

> **Review correction (2026-11-06)**: Originally stated: "In addition, no US license for tafenoquine is currently valid, and label safety data are missing." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 2 FDA applications or NDC listings for this drug, 2 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-tafenoquine-1 -->

**To proceed, the following is needed:**
- Mechanism of action data for tafenoquine, and an analysis of any plausible link to mast cell biology
- Preclinical validation (in vitro mast cell assays, KIT D816V models)
- FDA package insert warnings and contraindications for a formal safety screening
- A literature and trial search specific to tafenoquine and mastocytosis
- Clarification of the regulatory and commercial status
- Review of the major drug interactions for relevance to the target patient population

<!-- review:begin us-lic-20261106-tafenoquine-2 -->

> **Review correction (2026-11-06)**: Originally stated: "Clarification of the regulatory and commercial status of the cancelled NDAs" Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 2 FDA applications or NDC listings for this drug, 2 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-tafenoquine-2 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "no US license for tafenoquine is currently valid, and" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "of the cancelled NDAs" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

