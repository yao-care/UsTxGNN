---
layout: default
title: Ferric Carboxymaltose
parent: Model Prediction Only (L5)
nav_order: 701
evidence_level: L5
indication_count: 1
monitor_inn: "FERRIC CARBOXYMALTOSE"
predicted_indications: ["bronchitis"]
last_modified_at: 2026-11-12
description: "Ferric Carboxymaltose: predicted new indication Bronchitis (evidence level L5). Approved use: Iron deficiency and iron deficiency anemia"
---

# Ferric Carboxymaltose
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

## Ferric Carboxymaltose: From Iron Deficiency to Bronchitis
{: .text-alpha }

## One-Sentence Summary

Ferric carboxymaltose is an intravenous iron replacement product, used to correct iron deficiency and iron deficiency anemia.
The TxGNN model predicts it may be effective for **bronchitis**,
but **no clinical trials and no publications** currently support this direction, so the prediction is computational only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Iron deficiency and iron deficiency anemia (the approved indication text is not recorded in the compiled license data) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 0.9900 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 4 of 4) |
| Number of FDA Applications | 4 (active: 4) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ferric carboxymaltose is an intravenous iron replacement product, and its use in correcting iron deficiency and iron deficiency anemia is established. No mechanistic link to bronchitis has been established.

A speculative connection could involve iron status and host immune function or susceptibility to respiratory infection. This is only a hypothesis with no supporting data here. Intravenous iron may also carry infection-related concerns, which argues against assuming a benefit in bronchitis.

The high TxGNN score (0.9900) is a computational prediction only. It is not backed by any clinical or literature evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA212572 | FERRIC CARBOXYMALTOSE | MYLAN LABS LTD | Solution; intravenous | Valid |
| ANDA217076 | FERRIC CARBOXYMALTOSE | MYLAN | Solution; intravenous | Valid |
| ANDA217769 | FERRIC CARBOXYMALTOSE | MYLAN | Solution; intravenous | Valid |
| NDA203565 | INJECTAFER | AM REGENT | Solution; intravenous | Valid |

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 5 interactions were identified, one major and four moderate.
  - **Major**: Dimercaprol
  - **Moderate**: Iron, ferrous fumarate, ferrous gluconate, chloramphenicol

Please refer to the package insert for other safety information, including warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials, no literature, and no established mechanistic link to bronchitis.

<!-- review:begin us-lic-20261031-ferric_carboxymaltose-1 -->

> **Review correction (2026-10-31)**: Originally stated: "The prediction rests only on a model score, with no clinical trials, no literature, and no established mechanistic link to bronchitis. The only US license is cancelled, and the possible infection-related concerns with intravenous iron argue against assuming a benefit." Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-10-31). The FDA data list 4 FDA applications or NDC listings for this drug, 4 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261031-ferric_carboxymaltose-1 -->

**To proceed, the following is needed:**
- Mechanism of action data, and a plausible biological rationale linking iron replacement to bronchitis
- Supporting preclinical, observational or clinical evidence in bronchitis
- Package insert warnings and contraindications for safety screening, with particular attention to infection risk
- Assessment of route and formulation compatibility, since the product is injectable only
- Clarification of the current US regulatory status of the product

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-10-31 | Removed: "The only US license is cancelled, and the possible infection-related concerns with intravenous iron argue against assuming a benefit" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

