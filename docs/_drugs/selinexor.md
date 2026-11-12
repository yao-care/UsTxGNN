---
layout: default
title: Selinexor
parent: Model Prediction Only (L5)
nav_order: 1152
evidence_level: L5
indication_count: 1
monitor_inn: "SELINEXOR"
predicted_indications: ["drug-induced osteoporosis"]
last_modified_at: 2026-11-12
description: "Selinexor: predicted new indication Drug-induced osteoporosis (evidence level L5). Approved use: Not available in the compiled data"
---

# Selinexor
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

## Selinexor: From Oncology Use to Drug-Induced Osteoporosis
{: .text-alpha }

## One-Sentence Summary

Selinexor is an oral anticancer drug (an XPO1/exportin-1 inhibitor), but the data compiled for this report do not list a specific approved indication.
The TxGNN model predicts it may be relevant for **drug-induced osteoporosis**, with **0 clinical trials** and **0 publications** currently supporting this direction.
The prediction rests only on a computational score.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 0.9922 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 1 of 1) |
| Number of FDA Applications | 1 (active: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Selinexor is generally known as an XPO1 (exportin-1) inhibitor, which blocks the nuclear export of regulatory proteins. A possible link to bone biology would run through nuclear export of regulators involved in osteoclast and osteoblast signaling. This is speculative and not supported by the supplied data.

There is also a caution. Selinexor is associated with nausea, anorexia, weight loss, fatigue and cytopenias, which could plausibly worsen bone health in frail oncology patients. No evidence shows that it treats or prevents drug-induced osteoporosis. The high TxGNN score (0.9922) is a computational prediction, not clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| NDA212306 | XPOVIO | KARYOPHARM THERAPS | Tablet; oral | Valid |

<!-- licenses:end -->

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (XPO1 inhibitor); this classification is inferred from the drug's known pharmacology, not from the compiled data |
| Myelosuppression Risk | Cytopenias are reported as an associated adverse effect; please refer to the package insert warnings and precautions for severity |
| Emetogenicity Classification | Nausea and anorexia are associated adverse effects; please refer to the package insert warnings and precautions |
| Monitoring Items | CBC (with differential), body weight and nutritional status; please refer to the package insert for the full list |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: 81 interactions were identified in the DDI screening. Examples of those rated Major:
  - Deferiprone
  - Samarium (153Sm) lexidronam
  - Adalimumab
  - Baricitinib
  - Certolizumab pegol
  - Cladribine
  - Clozapine

  Moderate examples include strontium chloride Sr-89, roflumilast, chloramphenicol, zidovudine, azathioprine, alemtuzumab, anakinra, and several vaccines. Many of these involve myelosuppressive or immunosuppressive combinations.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no clinical trials or publications. Package insert safety data and mechanism data are missing, and the drug's known adverse effects could plausibly worsen bone health.

<!-- review:begin us-lic-20261031-selinexor-1 -->

> **Review correction (2026-10-31)**: Originally stated: "The only US NDA is cancelled. Package insert safety data and mechanism data are missing, and the drug's known adverse effects could plausibly worsen bone health." Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-10-31). The FDA data list 1 FDA application or NDC listing for this drug, 1 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261031-selinexor-1 -->

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action data (for example from DrugBank) to assess any biological link to bone remodeling
- Preclinical or observational evidence on selinexor's effect on bone
- Confirmation of the original approved indication
- Route and formulation compatibility assessment for the proposed indication

<!-- review:begin us-lic-20261106-selinexor-2 -->

> **Review correction (2026-11-06)**: Originally stated: "Confirmation of the original approved indication and the reason for the NDA cancellation" Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 1 FDA application or NDC listing for this drug, 1 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-selinexor-2 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-10-31 | Removed: "The only US NDA is cancelled" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "and the reason for the NDA cancellation" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

