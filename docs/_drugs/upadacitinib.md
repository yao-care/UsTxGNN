---
layout: default
title: Upadacitinib
parent: Model Prediction Only (L5)
nav_order: 1276
evidence_level: L5
indication_count: 2
monitor_inn: "UPADACITINIB"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome"]
last_modified_at: 2026-11-12
description: "Upadacitinib: predicted new indication Colobomatous microphthalmia-rhizomelic dysplasia syndrome (evidence level L5). Approved use: Rheumatoid arthritis"
---

# Upadacitinib
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

## Upadacitinib: From Rheumatoid Arthritis to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome
{: .text-alpha }

## One-Sentence Summary

Upadacitinib is a selective JAK1 inhibitor, originally used to treat rheumatoid arthritis.
The TxGNN model predicts it may be effective for **colobomatous microphthalmia-rhizomelic dysplasia syndrome**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. The prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis |
| Predicted New Indication | Colobomatous microphthalmia-rhizomelic dysplasia syndrome |
| TxGNN Prediction Score | 0.9961 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 3 of 3) |
| Number of FDA Applications | 3 (active: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, upadacitinib is a selective JAK1 inhibitor, and its efficacy in rheumatoid arthritis is established through suppression of JAK-STAT-mediated cytokine signaling.

The predicted condition is a rare developmental disorder with eye and skeletal malformations. Disorders like this are generally not driven by JAK-STAT-mediated inflammation, so a plausible mechanistic link cannot be established from the available data. The high score (0.9961) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The prediction should be treated as a hypothesis-generating signal only.

A second prediction, brachydactyly-syndactyly syndrome (score 0.9958, also L5, also Hold), is a congenital limb malformation and has the same limitations: no trials, no literature, and no inflammatory component to target.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

<!-- review:begin us-lic-20261106-upadacitinib-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Both authorizations are listed as cancelled in the data compiled for this report." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 3 FDA applications or NDC listings for this drug, 3 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-upadacitinib-1 -->

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA211675 | Rinvoq (AbbVie Inc.) | Tablet, extended release | Not available |
| NDA218347 | Rinvoq (AbbVie Inc.) | Solution | Not available |

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 interacting drugs in total; the 20 reviewed here show the following pattern:
  - **Major**: Systemic and other corticosteroids (hydrocortisone, triamcinolone, dexamethasone, beclomethasone dipropionate, betamethasone, budesonide, prednisone, prednisolone, ophthalmic triamcinolone); clarithromycin; cobicistat; deferiprone; iobenguane (I-131).
  - **Moderate**: Aprepitant, cimetidine, miconazole, deferasirox.
  - **Minor**: Zinc sulfate, zinc acetate, zinc gluconate.
- JAK inhibitors as a class carry significant safety warnings (infections, thrombosis, malignancy, major adverse cardiovascular events). Please refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a high TxGNN model (deep learning) score. There are no clinical trials or publications, no plausible mechanistic link to JAK1 signaling. A benefit-risk case cannot be made for a congenital structural condition given the known JAK inhibitor safety profile.

<!-- review:begin us-lic-20261106-upadacitinib-2 -->

> **Review correction (2026-11-06)**: Originally stated: "There are no clinical trials or publications, no plausible mechanistic link to JAK1 signaling, and the product's US authorizations are cancelled." Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 3 FDA applications or NDC listings for this drug, 3 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-upadacitinib-2 -->

**To proceed, the following is needed:**
- Package insert warnings and contraindications (required before any safety screening)
- Mechanism of action data to assess whether any biological link exists
- Evidence of a JAK-STAT or inflammatory component in the predicted condition (e.g., preclinical or genetic studies)

<!-- review:begin us-lic-20261106-upadacitinib-3 -->

> **Review correction (2026-11-06)**: Originally stated: "Evidence of a JAK-STAT or inflammatory component in the predicted condition (e.g., preclinical or genetic studies) / Clarification of the cancelled US authorization status" Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 3 FDA applications or NDC listings for this drug, 3 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-upadacitinib-3 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "Both authorizations are listed as cancelled in the data compiled for this report" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "and the product's US authorizations are cancelled" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "Clarification of the cancelled US authorization status" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

