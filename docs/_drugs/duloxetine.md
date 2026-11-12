---
layout: default
title: Duloxetine
parent: Model Prediction Only (L5)
nav_order: 633
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
monitor_inn: "DULOXETINE"
predicted_indications: ["benign paroxysmal torticollis of infancy", "agoraphobia", "obsessive-compulsive disorder", "schizotypal personality disorder", "histrionic personality disorder (disease)", "schizoid personality disorder", "paranoid personality disorder", "Ohdo syndrome and variants", "ligneous conjunctivitis", "blepharophimosis - intellectual disability syndrome, Ohdo type"]
description: "Duloxetine: predicted new indication Benign paroxysmal torticollis of infancy (evidence level L5). Approved use: Not recorded in the local data"
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

Currently, detailed mechanism of action data is not available in the data compiled for this report. Duloxetine belongs to the SNRI class, and its efficacy in depression, anxiety and chronic pain conditions is established.

For this specific prediction, no plausible mechanistic link has been identified. Benign paroxysmal torticollis of infancy is a pediatric disorder associated with channelopathy (CACNA1A-related), and nothing connects SNRI pharmacology to its pathophysiology. Duloxetine is also not approved for pediatric use in this setting. The very high score (0.9985) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

The drug is marketed in the US. No approved-indication text is recorded.

<!-- review:begin us-lic-20261106-duloxetine-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The drug is marketed in the US, with seven valid authorizations. No approved-indication text is recorded for any of them." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 29 FDA applications or NDC listings for this drug, 21 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-duloxetine-1 -->

| Authorization Number | Product Name | Dosage Form | Manufacturer | Status |
|---------|------|------|------|------|
| ANDA203197 | Duloxetine | Delayed-release capsule | Ascend Laboratories, LLC | Valid |
| ANDA090694 | Duloxetine | Delayed-release capsule | A-S Medication Solutions | Valid |
| NDA212516 | Drizalma Sprinkle | Delayed-release capsule | Sun Pharmaceutical Industries, Inc. | Valid |
| ANDA090776 | Duloxetine | Delayed-release capsule pellets | Preferred Pharmaceuticals Inc. | Valid |
| ANDA090739 | Duloxetine | Delayed-release capsule | Zydus Lifesciences Limited | Valid |

## Safety Considerations

- **Drug Interactions**: 100 interactions are recorded. Major-level interactions among those reviewed include **bupropion, lorcaserin, diethylpropion, dolasetron and dexfenfluramine**. Moderate-level examples include epinephrine, morphine, acetylsalicylic acid, cimetidine and dronabinol.
- **Knowledge-graph contraindication associations** (not label text): hypertension, orthostatic hypotension, epilepsy, bipolar disorder, liver disease and cirrhosis, hepatitis, fatty liver disease, gallbladder disease, hyperglycemia, blood coagulation disease, angle-closure glaucoma, serotonin syndrome, neuroleptic malignant syndrome, SIADH, and substance abuse/dependence.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone. There are no clinical trials, no literature, and no plausible mechanism linking an SNRI to this pediatric channelopathy-associated disorder. The drug is marketed in the US. Among the other predictions in the same analysis, obsessive-compulsive disorder has the strongest support (Level L2): a completed Phase 4 trial, a double-blind augmentation RCT and an open-label study, though all are small. It is a more promising direction to pursue instead.

<!-- review:begin us-lic-20261106-duloxetine-2 -->

> **Review correction (2026-11-06)**: Originally stated: "The drug is marketed in the US, with seven valid licenses. Among the other predictions in the same analysis, obsessive-compulsive disorder has the strongest support (Level L2): a completed Phase 4 trial, a double-blind augmentation RCT and an open-label study, though all are small." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 29 FDA applications or NDC listings for this drug, 21 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-duloxetine-2 -->

**To proceed, the following is needed:**
- Mechanism of action data and a testable biological hypothesis linking duloxetine to this disorder
- FDA package insert warnings and contraindications, particularly for pediatric use
- Any preclinical or case-level evidence in this condition
- Review of the other predicted indications, with OCD as the priority

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "with seven valid authorizations for any of them" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "with seven valid licenses" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

