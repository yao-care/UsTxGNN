---
layout: default
title: Icatibant
parent: Model Prediction Only (L5)
nav_order: 785
evidence_level: L5
indication_count: 6
monitor_inn: "ICATIBANT"
predicted_indications: ["serpinopathy with toxic serpin polymerization", "pseudo-von Willebrand disease", "primary release disorder of platelets", "immune-mediated necrotizing myopathy", "antisynthetase syndrome", "Glanzmann thrombasthenia"]
last_modified_at: 2026-11-12
description: "Icatibant: predicted new indication Serpinopathy with toxic serpin polymerization (evidence level L5). Approved use: Not recorded in the local data"
---

# Icatibant
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

## Icatibant: Serpinopathy with toxic serpin polymerization
{: .text-alpha }

## One-Sentence Summary

Icatibant is a bradykinin B2 receptor antagonist that is marketed in the United States as an injectable product. The TxGNN model predicts it may be relevant to **serpinopathy with toxic serpin polymerization**, with a score of 0.9999. **No clinical trials and no publications** currently support this prediction, so it remains a computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Serpinopathy with toxic serpin polymerization |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 9 of 11) |
| Number of FDA Applications | 11 (active: 9) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From pharmacology records, icatibant is a peptide that acts on the bradykinin B1 and B2 receptors (genes BDKRB1 and BDKRB2). By blocking bradykinin signalling, it reduces the vascular leak and swelling driven by bradykinin.

The high score most likely reflects shared associations with the serpin protein family in the model's network of biological relationships. Toxic serpin polymerization, however, is a different type of problem: proteins misfold and aggregate. It is not primarily driven by bradykinin, and there is no clear reason why B2 receptor blockade would help. The score is therefore a computational prediction without clinical or literature support, and it should be treated as a hypothesis, not as a finding.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA022150 | Firazyr | Injection, solution | Takeda Pharmaceuticals America, Inc. |
| ANDA212446 | Sajazir | Injection | Cycle Pharmaceuticals Ltd-UK |
| ANDA208317 | Icatibant | Injection, solution | Fresenius Kabi USA, LLC |
| ANDA210118 | Icatibant | Injection, solution | Teva Pharmaceuticals USA, Inc. |
| ANDA213773 | Icatibant | Injection | Alembic Pharmaceuticals Inc. |

Only the first 5 are listed here.

<!-- review:begin us-lic-20261105-icatibant-1 -->

> **Review correction (2026-11-05)**: Originally stated: "All 8 licences on record are valid. Only the first 5 are listed here." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-05). The FDA data list 11 FDA applications or NDC listings for this drug, 9 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261105-icatibant-1 -->

## Safety Considerations

- **Drug Interactions**: 12 interaction records were found. Ten ACE inhibitors are flagged at Moderate level: benazepril, captopril, enalapril, perindopril, trandolapril, moexipril, lisinopril, quinapril, ramipril and fosinopril. The remaining two records describe icatibant's pharmacological action on the B1 and B2 bradykinin receptors, not drug-drug interactions.

For warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no supporting trials or publications, and no plausible mechanistic link between bradykinin B2 blockade and toxic serpin polymerization. Evidence is at the model-prediction-only level (L5).

**To proceed, the following is needed:**
- A mechanistic rationale showing how bradykinin signalling contributes to this disease
- Preclinical or published evidence directly studying icatibant in this condition
- Review of the full package insert for warnings and contraindications
- Confirmed mechanism of action data

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "All 8 licences on record are valid" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

