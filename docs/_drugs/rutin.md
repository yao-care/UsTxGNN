---
layout: default
title: Rutin
parent: Model Prediction Only (L5)
nav_order: 1139
evidence_level: L5
indication_count: 8
monitor_inn: "Rutin"
predicted_indications: ["breast fibrocystic disease", "apocrine adenosis of breast", "blunt duct adenosis of breast", "benign mammary dysplasia", "vulvovaginal candidiasis", "fat necrosis of breast", "breast abscess", "vaginitis (disease)"]
last_modified_at: 2026-11-12
description: "Rutin: predicted new indication Breast fibrocystic disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Rutin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Rutin: Breast fibrocystic disease
{: .text-alpha }

## One-Sentence Summary

Rutin is a flavonoid compound whose original indications are ascorbic acid deficiency and scurvy.
The TxGNN model predicts it may be effective for **breast fibrocystic disease**,
but currently there are **0 clinical trials** and **0 publications** supporting this prediction, so it remains a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Breast fibrocystic disease |
| TxGNN Prediction Score | 0.9974 |
| Evidence Level | L5 |
| US Market Status | Marketed (no FDA-approved application; OTC monograph / unapproved listings: 16) |
| Number of FDA Applications | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, rutin is a flavonoid with reported antioxidant and vascular-protective (capillary fragility) properties. This could plausibly relate to inflammation or microvascular changes in breast tissue, but this link is speculative.

The high TxGNN score is a computational prediction only. Several other benign breast conditions also appear among the top predictions (apocrine adenosis, blunt duct adenosis, benign mammary dysplasia, fat necrosis of breast). Their identical or near-identical scores may reflect similarities the TxGNN model (deep learning) learned between related diseases, not biological evidence or independent lines of evidence. No clinical trials or publications support any of them.

Other predicted indications include vulvovaginal candidiasis, breast abscess and vaginitis. Flavonoids have some reported in vitro antifungal and anti-inflammatory activity, but nothing in the data compiled for this report supports this for rutin specifically. The two publications retrieved for vaginitis concern plant extracts in rat models of polycystic ovarian syndrome, not rutin and not vaginitis, so they offer no meaningful support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| NDC 63083-1541 | Rutin 1541 | Professional Complementary Health Formulas | Liquid | NDC listing, no FDA application (unapproved homeopathic) |
| NDC 87650-002 | JinXianLian Hepato-Enzyme Regulating Agent | Jiangxi Linyao Ecology Agriculture & Forestry Development… | Extract | NDC listing, no FDA application (unapproved drug other) |
| NDC 13411-861 | St. Paul Brands Verestor | Advanced Pharmaceutical Services, Inc. Dba Affordable… | Capsule | NDC listing, no FDA application (unapproved drug other) |
| NDC 13411-862 | JBA Verestor Mega Fiber Powder | Advanced Pharmaceutical Services, Inc. Dba Affordable… | Powder | NDC listing, no FDA application (unapproved drug other) |
| NDC 59088-003 | Bruselix Bruising | Puretek Corporation | Tablet | NDC listing, no FDA application (unapproved drug other) |

Showing 5 of 16 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

No approved indication text is recorded for any of them.

<!-- review:begin us-lic-20261106-rutin-1 -->

> **Review correction (2026-11-06)**: Originally stated: "All three authorizations are valid, and no approved indication text is recorded for any of them." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 0 FDA applications or NDC listings for this drug, 0 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-rutin-1 -->

## Safety Considerations

- **Knowledge-graph contraindication signals** (these come from the TxGNN knowledge graph, not from label text): sickle cell anemia, hereditary persistence of fetal hemoglobin, primary hyperoxaluria, hereditary hemochromatosis, hemosiderosis, iron metabolism disease, Wilson disease.

Please refer to the package insert for further safety information, including warnings and drug interactions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score (L5). There are no clinical trials or relevant publications, the mechanism of action is unavailable. Label-based safety information is also missing, which blocks safety screening.

<!-- review:begin us-lic-20261106-rutin-2 -->

> **Review correction (2026-11-06)**: Originally stated: "There are no clinical trials or relevant publications, the mechanism of action is unavailable, and all US authorizations are valid." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 0 FDA applications or NDC listings for this drug, 0 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-rutin-2 -->

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (download and parse the label)
- Mechanism of action data (for example, from DrugBank)
- Targeted literature search on rutin or quercetin-glycoside use in benign breast disease
- Preclinical or early clinical evidence for the predicted indication
- Route and formulation compatibility assessment for the predicted indication

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "All three authorizations are valid, and n" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "and all US authorizations are valid" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

