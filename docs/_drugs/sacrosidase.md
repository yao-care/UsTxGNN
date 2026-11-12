---
layout: default
title: Sacrosidase
parent: Model Prediction Only (L5)
nav_order: 1142
evidence_level: L5
indication_count: 2
monitor_inn: "SACROSIDASE"
predicted_indications: ["cystinosis", "familial apolipoprotein C-II deficiency"]
last_modified_at: 2026-11-12
description: "Sacrosidase: predicted new indication Cystinosis (evidence level L5). Approved use: Congenital sucrase-isomaltase deficiency"
---

# Sacrosidase
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

## Sacrosidase: From Congenital Sucrase-Isomaltase Deficiency to Cystinosis
{: .text-alpha }

## One-Sentence Summary

Sacrosidase is an orally administered yeast-derived sucrase enzyme, originally used to treat congenital sucrase-isomaltase deficiency.
The TxGNN model predicts it may be effective for **Cystinosis**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on computation alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Congenital sucrase-isomaltase deficiency |
| Predicted New Indication | Cystinosis |
| TxGNN Prediction Score | 0.9944 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 1 of 1) |
| Number of FDA Applications | 1 (active: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, sacrosidase is an oral enzyme replacement that hydrolyzes dietary sucrose in the gastrointestinal lumen and is not systemically absorbed. Its efficacy in congenital sucrase-isomaltase deficiency rests on this local digestive action.

Cystinosis is a lysosomal storage disorder caused by CTNS mutations. These impair the cystinosin transporter and lead to cystine accumulation inside lysosomes. The standard of care is cysteamine, which depletes cystine. A luminal digestive enzyme has no plausible effect on lysosomal cystine transport, so **no credible mechanistic link was identified**.

The high score (0.9944) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, such as both being "inherited metabolic disorders," not biological evidence. It should be treated as a computational hypothesis only.

*Another prediction from the same analysis:* familial apolipoprotein C-II deficiency (score 0.9905) also lacks any mechanistic link, clinical trials or literature. It involves a defect in lipoprotein lipase activation, which a gut-luminal sucrase does not influence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA 020772 | Sucraid (QOL Medical, LLC) | Solution | Status: valid |

## Safety Considerations

Please refer to the package insert for safety information.

No drug-drug interaction records were found in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trial or literature support (L5), and no plausible mechanism links a non-absorbed gut enzyme to lysosomal cystine transport.

<!-- review:begin us-lic-20261031-sacrosidase-1 -->

> **Review correction (2026-10-31)**: Originally stated: "The prediction has no clinical trial or literature support (L5), and no plausible mechanism links a non-absorbed gut enzyme to lysosomal cystine transport. The only US license is cancelled, so there is also no commercial basis for development." Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-10-31). The FDA data list 1 FDA application or NDC listing for this drug, 1 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261031-sacrosidase-1 -->

**To proceed, the following is needed:**
- Mechanism of action data (e.g., from DrugBank) to allow a proper mechanistic assessment
- Package insert warnings and contraindications from the FDA, which are required before any safety screening
- Preclinical evidence of any systemic or lysosomal effect of sacrosidase relevant to cystinosis

<!-- review:begin us-lic-20261031-sacrosidase-2 -->

> **Review correction (2026-10-31)**: Originally stated: "Preclinical evidence of any systemic or lysosomal effect of sacrosidase relevant to cystinosis / Clarification of the regulatory and supply status, given that the only US license is cancelled" Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-10-31). The FDA data list 1 FDA application or NDC listing for this drug, 1 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261031-sacrosidase-2 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-10-31 | Removed: "The only US license is cancelled, so there is also no commercial basis for development" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-10-31 | Removed: "Clarification of the regulatory and supply status, given that the only US license is cancelled" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

