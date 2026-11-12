---
layout: default
title: Mometasone
parent: Model Prediction Only (L5)
nav_order: 941
evidence_level: L5
indication_count: 1
monitor_inn: "MOMETASONE"
predicted_indications: ["primary cutaneous T-cell lymphoma"]
last_modified_at: 2026-11-12
description: "Mometasone: predicted new indication Primary cutaneous T-cell lymphoma (evidence level L5). Approved use: Not stated in the US license records"
---

# Mometasone
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

## Mometasone: From Allergic Rhinitis and Related Airway Conditions to Primary Cutaneous T-Cell Lymphoma
{: .text-alpha }

## One-Sentence Summary

Mometasone is a corticosteroid used intranasally for allergic rhinitis, nasal polyposis and asthma, and topically for allergic skin disorders.
The TxGNN model predicts it may be effective for **primary cutaneous T-cell lymphoma**,
but there are currently **0 registered clinical trials** and only **2 case reports** in the literature, so the evidence is very limited.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US license records; pharmacology data list intranasal use for allergic rhinitis, nasal polyposis and asthma, and topical use for allergic skin disorders |
| Predicted New Indication | Primary cutaneous T-cell lymphoma |
| TxGNN Prediction Score | 0.9936 |
| Evidence Level | L5 (model prediction only; the only literature is two case reports, which does not meet L3 criteria) |
| US Market Status | Marketed (active FDA-approved applications: 20 of 35) |
| Number of FDA Applications | 35 (active: 20) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available for mometasone in the data compiled for this report. Based on known pharmacology, mometasone is a synthetic corticosteroid that binds the glucocorticoid receptor (NR3C1). It is a medium-to-high potency agent and has been used for inflammatory conditions of the airways and skin.

Topical corticosteroids are an established skin-directed therapy for early-stage mycosis fungoides, the most common form of primary cutaneous T-cell lymphoma. Through glucocorticoid receptor signalling, they exert anti-inflammatory and pro-apoptotic effects on both malignant and reactive T cells. This gives a plausible class-level mechanistic link between mometasone and the predicted indication.

However, no mometasone-specific data in cutaneous T-cell lymphoma were provided. The high TxGNN score is a computational prediction only, and it should be treated as a hypothesis rather than as evidence of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25442255](https://pubmed.ncbi.nlm.nih.gov/25442255/) | 2015 | Case report | Journal of Cutaneous Pathology | An 11-year-old boy with a 7-year history of slowly progressive CD8+CD56+ mycosis fungoides (cytotoxic immunophenotype); the report concerns diagnosis and presentation of childhood disease, and the abstract provided does not show a mometasone-specific finding |
| [40821495](https://pubmed.ncbi.nlm.nih.gov/40821495/) | 2025 | Case report | Proceedings (Baylor University Medical Center) | Cutaneous pseudolymphoma (a benign mimic of lymphoma, not a lymphoma) on the nose that did not respond to mometasone and tacrolimus, then was treated with tapinarof; it does not support mometasone efficacy |

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA075919 | MOMETASONE FUROATE | FOUGERA PHARMS | Lotion; topical | Valid |
| ANDA076067 | MOMETASONE FUROATE | PADAGIS US | Ointment; topical | Valid |
| ANDA076481 | MOMETASONE FUROATE | ENCUBE | Ointment; topical | Valid |
| ANDA076499 | MOMETASONE FUROATE | ENCUBE | Lotion; topical | Valid |
| ANDA076679 | MOMETASONE FUROATE | SUN PHARMA CANADA | Cream; topical | Valid |

Showing 5 of 35 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

All are metered nasal sprays. No topical formulation is represented in the data compiled for this report.

<!-- review:begin us-lic-20261105-mometasone-1 -->

> **Review correction (2026-11-05)**: Originally stated: "The drug is marketed in the US, and all 4 licenses are valid. All are metered nasal sprays." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-05). The FDA data list 35 FDA applications or NDC listings for this drug, 20 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261105-mometasone-1 -->

## Safety Considerations

- **Drug Interactions**: The only interaction record is pharmacological, not drug-drug: mometasone acts on the glucocorticoid receptor (NR3C1). No specific interacting drugs were identified.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction (primary cutaneous T-cell lymphoma, score 0.9936) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It rests on a plausible class-level mechanism (topical corticosteroids in early mycosis fungoides). There are no clinical trials and no supportive mometasone-specific literature; one case report even describes treatment failure in a benign mimic. The drug is marketed in the US.

<!-- review:begin us-lic-20261106-mometasone-2 -->

> **Review correction (2026-11-06)**: Originally stated: "The drug is marketed in the US with 4 valid licenses, but the available products are nasal sprays, which are not suited to skin-directed therapy." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 35 FDA applications or NDC listings for this drug, 20 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-mometasone-2 -->

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- Mometasone-specific clinical or observational data in mycosis fungoides or other cutaneous T-cell lymphoma
- Comparison with established topical corticosteroids already used in this setting
- Assessment of route and formulation compatibility

<!-- review:begin us-lic-20261106-mometasone-3 -->

> **Review correction (2026-11-06)**: Originally stated: "Assessment of route and formulation compatibility (topical versus the nasal spray forms in the data) and of the regulatory and commercial implications of the cancelled status" Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 35 FDA applications or NDC listings for this drug, 20 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-mometasone-3 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "The drug is marketed in the US, and all 4 licenses are valid" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "with 4 valid licenses, but the available products are nasal sprays, which are not suited to skin-directed therapy" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "(topical versus the nasal spray forms in the data) and of the regulatory and commercial implications of the cancelled status" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

