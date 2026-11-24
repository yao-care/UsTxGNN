---
layout: default
title: Duloxetine
parent: Model Prediction Only (L5)
nav_order: 633
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "DULOXETINE"
predicted_indications: ["benign paroxysmal torticollis of infancy", "agoraphobia", "obsessive-compulsive disorder", "schizotypal personality disorder", "histrionic personality disorder (disease)", "schizoid personality disorder", "paranoid personality disorder", "Ohdo syndrome and variants", "ligneous conjunctivitis", "blepharophimosis - intellectual disability syndrome, Ohdo type"]
description: "Duloxetine: predicted new indication Benign paroxysmal torticollis of infancy (evidence level L5). In the US: 29 FDA applications (21 active)"
---

# Duloxetine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Duloxetine: Benign paroxysmal torticollis of infancy
{: .text-alpha }

## One-Sentence Summary

Duloxetine is a serotonin-norepinephrine reuptake inhibitor (SNRI), originally used for depression, anxiety, fibromyalgia and related conditions.
The TxGNN model predicts it may be effective for **benign paroxysmal torticollis of infancy**, but **no clinical trials and no publications** currently support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Benign paroxysmal torticollis of infancy |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L5 (model prediction only) |
| US Market Status | Marketed (active FDA-approved applications: 21 of 29) |
| Number of FDA Applications | 29 (active: 21) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for duloxetine: "Although the exact mechanisms of the antidepressant, central pain inhibitory and anxiolytic actions of duloxetine in humans are unknown, these actions are believed to be related to its potentiation of serotonergic and noradrenergic activity in the CNS." ([DailyMed: Duloxetine Delayed-Release (duloxetine hydrochloride) prescribing information, Golden State Medical Supply, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=00628e5e-4c5b-2573-e063-6294a90a0e3b), label version 2026-08-20; accessed 2026-11-19.) Duloxetine belongs to the SNRI class, and its efficacy in depression, anxiety and chronic pain conditions is established.

For this specific prediction, no plausible mechanistic link has been identified. Benign paroxysmal torticollis of infancy is a pediatric disorder associated with channelopathy (CACNA1A-related), and nothing connects SNRI pharmacology to its pathophysiology. Duloxetine is also not approved for pediatric use in this setting. The very high score (0.9985) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

The drug is marketed in the US. No approved-indication text is recorded.

<!-- review:begin us-lic-20261106-duloxetine-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The drug is marketed in the US, with seven valid authorizations. No approved-indication text is recorded for any of them." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-duloxetine-1 -->

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA090694 | DULOXETINE HYDROCHLORIDE | LUPIN | Capsule, delayed rel pellets; oral | Valid |
| ANDA090728 | DULOXETINE HYDROCHLORIDE | ZYDUS PHARMS | Capsule, delayed rel pellets; oral | Valid |
| ANDA090739 | DULOXETINE HYDROCHLORIDE | ZYDUS HLTHCARE | Capsule, delayed rel pellets; oral | Valid |
| ANDA090776 | DULOXETINE HYDROCHLORIDE | ACTAVIS ELIZABETH | Capsule, delayed rel pellets; oral | Valid |
| ANDA090778 | DULOXETINE HYDROCHLORIDE | AUROBINDO PHARMA LTD | Capsule, delayed rel pellets; oral | Valid |

Showing 5 of 29 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 100 interactions are recorded. Major-level interactions among those reviewed include **bupropion, lorcaserin, diethylpropion, dolasetron and dexfenfluramine**. Moderate-level examples include epinephrine, morphine, acetylsalicylic acid, cimetidine and dronabinol.
- **Knowledge-graph contraindication associations** (not label text): hypertension, orthostatic hypotension, epilepsy, bipolar disorder, liver disease and cirrhosis, hepatitis, fatty liver disease, gallbladder disease, hyperglycemia, blood coagulation disease, angle-closure glaucoma, serotonin syndrome, neuroleptic malignant syndrome, SIADH, and substance abuse/dependence.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone. There are no clinical trials, no literature, and no plausible mechanism linking an SNRI to this pediatric channelopathy-associated disorder. The drug is marketed in the US. Among the other predictions in the same analysis, obsessive-compulsive disorder has the strongest support (Level L2): a completed Phase 4 trial, a double-blind augmentation RCT and an open-label study, though all are small. It is a more promising direction to pursue instead.

<!-- review:begin us-lic-20261106-duloxetine-2 -->

> **Review correction (2026-11-06)**: Originally stated: "There are no clinical trials, no literature, and no plausible mechanism linking an SNRI to this pediatric channelopathy-associated disorder. The drug is marketed in the US, with seven valid licenses." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-duloxetine-2 -->

**To proceed, the following is needed:**
- Mechanism of action data and a testable biological hypothesis linking duloxetine to this disorder
- FDA package insert warnings and contraindications, particularly for pediatric use
- Any preclinical or case-level evidence in this condition
- Review of the other predicted indications, with OCD as the priority

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "with seven valid authorizations for any of them" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "with seven valid licenses" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Duloxetine Delayed-Release (duloxetine hydrochloride) prescribing information, Golden State Medical Supply, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=00628e5e-4c5b-2573-e063-6294a90a0e3b) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

