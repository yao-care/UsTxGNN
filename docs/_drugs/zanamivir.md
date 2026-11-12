---
layout: default
title: Zanamivir
parent: Model Prediction Only (L5)
nav_order: 1301
evidence_level: L5
indication_count: 2
monitor_inn: "ZANAMIVIR"
predicted_indications: ["pyelonephritis", "disorder of tyrosine metabolism"]
last_modified_at: 2026-11-12
description: "Zanamivir: predicted new indication Pyelonephritis (evidence level L5). Approved use: Influenza"
---

# Zanamivir
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

## Zanamivir: From Influenza to Pyelonephritis
{: .text-alpha }

## One-Sentence Summary

Zanamivir is a neuraminidase inhibitor, originally used to treat influenza.
The TxGNN model predicts it may be effective for **pyelonephritis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Influenza |
| Predicted New Indication | Pyelonephritis |
| TxGNN Prediction Score | 0.9984 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 1 of 1) |
| Number of FDA Applications | 1 (active: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Based on known information, zanamivir is a viral neuraminidase inhibitor, and its efficacy in influenza has been established.

A plausible mechanistic link to pyelonephritis is hard to find. Pyelonephritis is mostly caused by bacteria such as *E. coli*, not by viruses. Bacteria do produce neuraminidases (sialidases) that may contribute to virulence, but zanamivir has little established activity against them, so this idea is speculative.

Practical feasibility is also limited. Systemic exposure from the inhaled formulation is low, and an intravenous form is not widely marketed, which makes treating a urinary tract infection difficult. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| NDA021036 | RELENZA | GLAXOSMITHKLINE | Powder; inhalation | Valid |

<!-- licenses:end -->

## Safety Considerations

- **Disease associations flagged in the knowledge graph** (not label text): epilepsy, chronic obstructive pulmonary disease (including severe early-onset COPD), bronchial disease, and delirium.
- **Drug Interactions** (8 recorded):
  - Insulin human (inhalation, rapid acting): Moderate
  - Clarithromycin, loratadine, montelukast, ketotifen, fexofenadine, ibuprofen, diclofenac: severity level unknown

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a high model score. The score is likely a TxGNN model (deep learning) artifact.

<!-- review:begin us-lic-20261031-zanamivir-1 -->

> **Review correction (2026-10-31)**: Originally stated: "There are no clinical trials or literature, no plausible mechanism against bacterial pyelonephritis, and the only US license is cancelled. The score is likely a TxGNN model (deep learning) artifact." Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-10-31). The FDA data list 1 FDA application or NDC listing for this drug, 1 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261031-zanamivir-1 -->

**To proceed, the following is needed:**
- Detailed mechanism of action data, including any evidence of zanamivir activity against bacterial neuraminidases
- Preclinical evidence in relevant urinary tract infection models
- Package insert warnings and contraindications
- Pharmacokinetic data on urinary exposure and feasible routes of administration, since the inhaled form gives low systemic exposure
- A review of how the TxGNN model (deep learning) produced this prediction

---

**Note on the second prediction (disorder of tyrosine metabolism, score 0.9902):** This candidate is also at Evidence Level L5 with a Hold recommendation. The three retrieved publications all concern influenza neuraminidase inhibitors (oseltamivir resistance, an SPR inhibition assay, and an N294S neuraminidase mutation). None addresses tyrosine metabolism, and there is no apparent mechanistic link. This is most likely a prediction artifact.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-10-31 | Removed: "There are no clinical trials or literature, no plausible mechanism against bacterial pyelonephritis, and the only US license is cancelled" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

