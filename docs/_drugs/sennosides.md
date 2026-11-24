---
layout: default
title: Sennosides
parent: Model Prediction Only (L5)
nav_order: 1155
evidence_level: L5
indication_count: 6
monitor_inn: "SENNOSIDES"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "open-angle glaucoma", "primary hereditary glaucoma", "alopecia"]
last_modified_at: 2026-11-24
description: "Sennosides: predicted new indication Hypotrichosis simplex of the scalp (evidence level L5). Approved use: Laxative (inferred from product names"
---

# Sennosides
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Sennosides: From Constipation (Laxative Use) to Hypotrichosis Simplex of the Scalp
{: .text-alpha }

## One-Sentence Summary

Sennosides are stimulant laxatives that act on the colon. The data compiled for this report lists no approved indication text, but the products are marketed as laxatives.
The TxGNN model predicts they may be effective for **hypotrichosis simplex of the scalp**, but **0 clinical trials** and **0 publications** currently support this prediction. It is a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Laxative (inferred from product names; no approved indication text available) |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 0.9929 |
| Evidence Level | L5 |
| US Market Status | Marketed (no FDA-approved application; OTC monograph / unapproved listings: 247) |
| Number of FDA Applications | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, sennosides are anthraquinone stimulant laxatives that act on the colonic mucosa through their active metabolite rheinanthrone. Their efficacy relates to bowel function, not to hair biology.

No mechanistic link to hair follicle biology or to the genetic causes of hypotrichosis simplex (for example CDSN, APCDD1 and RPL21 variants) has been established. The high score is a model prediction only.

The other five predictions (congenital hypotrichosis milia, diffuse alopecia areata, open-angle glaucoma, primary hereditary glaucoma and alopecia) all score between 0.9910 and 0.9923 and also lack supporting evidence. This clustering suggests the scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| NDC 0067-8140 | EX-LAX REGULAR STRENGTH CHOCOLATED STIMULANT LAXATIVE | Haleon US Holdings LLC | Tablet, chewable | NDC listing, no FDA application (OTC monograph drug) |
| NDC 0067-8141 | EX-LAX REGULAR STRENGTH STIMULANT LAXATIVE | Haleon US Holdings LLC | Tablet | NDC listing, no FDA application (OTC monograph drug) |
| NDC 0067-8142 | EX-LAX MAXIMUM STRENGTH STIMULANT LAXATIVE | Haleon US Holdings LLC | Pill | NDC listing, no FDA application (OTC monograph drug) |
| NDC 0067-8143 | Perdiem | Haleon US Holdings LLC | Tablet | NDC listing, no FDA application (OTC monograph drug) |
| NDC 0121-4967 | Senna | PAI Holdings, LLC dba PAI Pharma | Liquid | NDC listing, no FDA application (OTC monograph drug) |

Showing 5 of 247 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

## Safety Considerations

Please refer to the package insert for safety information.

No drug-drug interaction records were found, and no contraindication edges were identified in the knowledge graph.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials or publications, and no plausible mechanism links a stimulant laxative to hair loss. 

<!-- review:begin us-lic-20261124-sennosides-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Neither of the two US licences is currently valid." Removed: it said the US products were cancelled or not valid, but this drug has no FDA application and the NDC Directory lists current products under OTC monograph or unapproved categories (Drugs@FDA and the NDC Directory as of 2026-11-06). The current listings are shown in the Quick Overview and in the table under US Market Information. Source: [openFDA NDC Directory](https://open.fda.gov/data/ndc/); [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/).

<!-- review:end us-lic-20261124-sennosides-1 -->

**To proceed, the following is needed:**
- Mechanism of action data, to test whether any biological link to hair follicle biology exists
- Package insert warnings and contraindications, which are a blocking gap for safety screening
- Preclinical or mechanistic studies, since none currently exist
- Route compatibility assessment, since the available oral forms may not suit a scalp indication
- Review of the other predicted indications for any with better support

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "Neither of the two US licences is currently valid" | Corrected | [openFDA NDC Directory](https://open.fda.gov/data/ndc/); [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

