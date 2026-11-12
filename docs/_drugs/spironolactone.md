---
layout: default
title: Spironolactone
parent: Model Prediction Only (L5)
nav_order: 1180
evidence_level: L5
indication_count: 2
monitor_inn: "SPIRONOLACTONE"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia"]
last_modified_at: 2026-11-12
description: "Spironolactone: predicted new indication Hypotrichosis simplex of the scalp (evidence level L5). Approved use: Hypertension, congestive heart failure…"
---

# Spironolactone
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

## Spironolactone: From Hypertension and Heart Failure to Hypotrichosis Simplex of the Scalp
{: .text-alpha }

## One-Sentence Summary

Spironolactone is an aldosterone receptor antagonist originally used for hypertension, congestive heart failure, and primary aldosteronism.
The TxGNN model predicts it may be effective for **hypotrichosis simplex of the scalp**,
but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it is a computational hypothesis only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, congestive heart failure, hyperaldosteronism / primary aldosteronism, Bartter disease, Waterhouse-Friderichsen syndrome |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 0.9926 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 18 of 48; OTC monograph / unapproved listings: 1) |
| Number of FDA Applications | 48 (active: 18) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, spironolactone is an aldosterone receptor antagonist that also has anti-androgen activity (androgen receptor blockade and reduced androgen synthesis). This anti-androgen effect is the rationale for its off-label use in androgenetic alopecia and female pattern hair loss.

The link to the predicted indication is weak. Hypotrichosis simplex of the scalp is a rare hereditary hair loss disorder caused by variants in genes such as CDSN, APCDD1, and RPL21. These genes act through Wnt signaling and structural or ribosomal pathways, not through androgen-driven follicle miniaturization. The connection to spironolactone is therefore indirect and speculative.

The high TxGNN score (0.9926) is a computational prediction only. A second prediction, congenital hypotrichosis milia (score 0.9904), likewise has no supporting trials or literature. It appears to be driven by the shared hair-loss phenotype, and no androgen-mediated mechanism has been established for it.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

No approved indication text was available for them.

<!-- review:begin us-lic-20261106-spironolactone-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Eight US authorizations are listed as valid, and no approved indication text was available for them." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 48 FDA applications or NDC listings for this drug, 18 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-spironolactone-1 -->

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA040424 | SPIRONOLACTONE | MYLAN | Tablet; oral | Valid |
| ANDA040750 | SPIRONOLACTONE | OXFORD PHARMS | Tablet; oral | Valid |
| ANDA089424 | SPIRONOLACTONE | SUN PHARM INDUSTRIES | Tablet; oral | Valid |
| ANDA091426 | SPIRONOLACTONE | AMNEAL PHARMS | Tablet; oral | Valid |
| ANDA202187 | SPIRONOLACTONE | AUROBINDO PHARMA | Tablet; oral | Valid |

Showing 5 of 49 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text):** kidney disease, anuria, pancreatitis, systemic lupus erythematosus (including pediatric), potassium deficiency disease, diabetes mellitus, diabetic ketoacidosis, hyperuricemia, gout, hyperparathyroidism, osteitis fibrosa, hypercalcemia, nephrocalcinosis, phosphorus metabolism disease, hepatic coma, hepatic encephalopathy, neonatal jaundice, pyoureter.
- **Drug Interactions:** 100 interactions were identified; the first 20 retrieved are summarized here.
  - **Major:** loperamide.
  - **Moderate:** hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide, metformin, bupropion, morphine, bisacodyl, castor oil, dronabinol, exenatide, and the SGLT2 inhibitors canagliflozin, dapagliflozin, empagliflozin, and ertugliflozin.
  - **Minor:** doxycycline, acetylsalicylic acid, fidaxomicin.

Please refer to the package insert for full warnings and label contraindications, as these were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials or publications, and the proposed mechanism (anti-androgen effect) does not fit the genetic, non-androgen-driven biology of this disorder. The drug is marketed in the US.

<!-- review:begin us-lic-20261106-spironolactone-2 -->

> **Review correction (2026-11-06)**: Originally stated: "The drug is marketed in the US, with 8 valid licenses." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 48 FDA applications or NDC listings for this drug, 18 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-spironolactone-2 -->

**To proceed, the following is needed:**
- Mechanism of action data for spironolactone
- FDA package insert warnings and contraindications
- Evidence that links the genetic causes of hypotrichosis simplex (CDSN, APCDD1, RPL21) to a spironolactone-responsive pathway, such as preclinical or follicle model studies
- Any case reports, trials, or literature in this indication
- Route compatibility and similarity-to-original-indication assessments, which are still pending
- Clarification of current US marketing status

<!-- review:begin us-lic-20261106-spironolactone-3 -->

> **Review correction (2026-11-06)**: Originally stated: "Clarification of current US marketing status, since the drug is marketed with 8 valid licenses" Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 48 FDA applications or NDC listings for this drug, 18 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-spironolactone-3 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "Eight US authorizations are listed as valid, and n" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "with 8 valid licenses" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "since the drug is marketed with 8 valid licenses" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

