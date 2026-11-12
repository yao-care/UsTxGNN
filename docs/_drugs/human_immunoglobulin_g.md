---
layout: default
title: Human Immunoglobulin G
parent: Model Prediction Only (L5)
nav_order: 773
evidence_level: L5
indication_count: 3
monitor_inn: "HUMAN IMMUNOGLOBULIN G"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "drug-induced osteoporosis"]
last_modified_at: 2026-11-12
description: "Human Immunoglobulin G: predicted new indication Severe nonproliferative diabetic retinopathy (evidence level L5). Approved use: Not recorded in the local data"
---

# Human Immunoglobulin G
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

## Human Immunoglobulin G: Severe nonproliferative diabetic retinopathy
{: .text-alpha }

## One-Sentence Summary

Human immunoglobulin G (IgG) is a plasma-derived biologic sold in the US as several immune globulin products, but the data compiled for this report do not include approved indication text.
The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**, a computational prediction only.
Currently there are **0 clinical trials** and **0 publications** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 0.9975 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 17 of 17) |
| Number of FDA Applications | 17 (active: 17) |
| Recommended Decision | Hold |

Two other predictions were also generated: diabetic retinopathy (0.9963) and drug-induced osteoporosis (0.9937). Both are also L5 with a recommendation of Hold.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on general knowledge, IVIG is thought to act through Fc-receptor blockade, complement inhibition, and broad anti-inflammatory effects. Low-grade inflammation contributes to diabetic retinopathy, so an immunomodulatory link is plausible. This link is unverified and cannot be confirmed from the compiled data.

The original indication is not recorded in the compiled data, so a direct comparison with the new indication is not possible. The established treatments for diabetic retinopathy are intravitreal anti-VEGF agents and laser photocoagulation. A systemic plasma-derived product has no clear rationale against them.

The related prediction "diabetic retinopathy" largely overlaps with the severe nonproliferative form, and its score is highly correlated. It should not be counted as independent support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

The drug is marketed in the US, and no approved indication text was available.

<!-- review:begin us-lic-20261106-human_immunoglobulin_g-2 -->

> **Review correction (2026-11-06)**: Originally stated: "The drug is marketed in the US with 11 valid licenses, and no approved indication text was available." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 17 FDA applications or NDC listings for this drug, 17 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-human_immunoglobulin_g-2 -->

| Authorization Number | Product Name | Dosage Form | Status |
|---------|------|------|-----------|
| BLA125822 | QIVIGY | Injection, solution | Valid |
| BLA125668 | Cutaquig | Solution | Valid |
| BLA125350 | Hizentra | Liquid | Valid |
| BLA125201 | Privigen | Liquid | Valid |
| BLA125062 | Octagam Immune Globulin (Human) | Solution | Valid |

## Safety Considerations

Please refer to the package insert for safety information.

<!-- review:begin us-lic-20261106-human_immunoglobulin_g-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Six further cancelled licenses are not shown: Gamunex-C, Alyglo, Flebogamma, Panzyga, GAMMAGARD Liquid, and Gammaplex." Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 17 FDA applications or NDC listings for this drug, 17 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-human_immunoglobulin_g-1 -->

Systemic immune globulin products carry general risks such as thrombosis and renal injury. These were noted in the rationale review but are not backed by label data in the compiled data. No drug interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a TxGNN model (deep learning) score, with no clinical trials, no literature, and no confirmed mechanism. The drug is marketed in the US, and the safety data are incomplete, so the review cannot proceed to safety screening.

<!-- review:begin us-lic-20261106-human_immunoglobulin_g-3 -->

> **Review correction (2026-11-06)**: Originally stated: "The drug is marketed in the US with 11 valid licenses, and the safety data are incomplete, so the review cannot proceed to safety screening." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 17 FDA applications or NDC listings for this drug, 17 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-human_immunoglobulin_g-3 -->

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap)
- Mechanism of action data from DrugBank
- Original approved indication information
- A literature and trial search for IVIG or immunoglobulin in diabetic retinopathy
- Preclinical or mechanistic evidence for an immunomodulatory role in retinopathy
- Route and formulation compatibility assessment (systemic versus intravitreal delivery)
- A risk-benefit justification against standard care (anti-VEGF, laser), including thrombosis, renal injury, cost, and supply

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "Six further cancelled licenses are not shown: Gamunex-C, Alyglo, Flebogamma, Panzyga, GAMMAGARD Liquid, and Gammaplex" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "with 11 valid licenses" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "with 11 valid licenses" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

