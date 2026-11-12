---
layout: default
title: Zileuton
parent: Model Prediction Only (L5)
nav_order: 1305
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-12
monitor_inn: "ZILEUTON"
predicted_indications: ["bronchitis", "atopic eczema", "bronchial neoplasm (disease)", "Laubry-Pezzi syndrome", "heart disease", "interventricular septum aneurysm", "genetic syndromic Pierre Robin syndrome"]
description: "Zileuton: predicted new indication Bronchitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Zileuton
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Zileuton: Bronchitis
{: .text-alpha }

## One-Sentence Summary

Zileuton is an oral 5-lipoxygenase inhibitor that reduces leukotriene synthesis.
The TxGNN model predicts it may be effective for **bronchitis**, with a score of **0.9999**.
However, there are currently **no clinical trials and no publications** for this specific prediction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 4 of 8) |
| Number of FDA Applications | 8 (active: 4) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Zileuton inhibits 5-lipoxygenase, the enzyme that produces leukotrienes. Leukotrienes are inflammatory mediators that act on the airways, so lowering their production could in theory dampen airway inflammation. Detailed mechanism-of-action data were not available in the data compiled for this report, so this reasoning rests on the known pharmacology of the drug class.

Bronchitis is an inflammatory condition of the bronchial airways, so a drug that reduces leukotriene-driven inflammation is mechanistically plausible. The TxGNN score is very high, but no study has tested zileuton in bronchitis. The prediction is therefore a hypothesis and not a demonstrated benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

<!-- review:begin us-lic-20261105-zileuton-1 -->

> **Review correction (2026-11-05)**: Originally stated: "All three licences are currently valid, and the drug is marketed in the United States." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-05). The FDA data list 8 FDA applications or NDC listings for this drug, 4 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261105-zileuton-1 -->

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA215742 | Zileuton (Camber Pharmaceuticals) | Tablet, film coated, extended release | Not specified; status valid |
| ANDA212670 | Zileuton (Strides Pharma Science) | Tablet, multilayer, extended release | Not specified; status valid |
| ANDA204929 | Zileuton (Rising Pharma Holdings) | Tablet, extended release | Not specified; status valid |

## Safety Considerations

- **Drug Interactions**: 56 interactions were identified in total. The only one rated Major is **terfenadine**. Examples rated Moderate include theophylline, aminophylline, oxtriphylline, warfarin, tacrolimus, cisapride, astemizole, roflumilast, pentoxifylline, naltrexone, and deferasirox.

Please refer to the package insert for warnings and contraindications, as label-based safety text was not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but there are no clinical trials or publications for bronchitis, so the evidence level is L5 and the prediction is purely computational.

**To proceed, the following is needed:**
- Literature review and preclinical data on 5-lipoxygenase inhibition in bronchitis
- Detailed mechanism-of-action data
- Review of the package insert warnings and contraindications, particularly liver-related safety
- A drug interaction management plan, especially for terfenadine and theophylline-type agents

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "All three licences are currently valid, and the drug is marketed in the United States" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

