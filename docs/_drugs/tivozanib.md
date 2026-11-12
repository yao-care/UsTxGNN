---
layout: default
title: Tivozanib
parent: Model Prediction Only (L5)
nav_order: 1235
evidence_level: L5
indication_count: 10
monitor_inn: "TIVOZANIB"
predicted_indications: ["endocervical carcinoma", "uterine ligament adenocarcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "cervical adenosquamous carcinoma, glassy cell variant", "uterine ligament endometrioid adenocarcinoma", "uterine ligament mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma", "cervical mucinous adenocarcinoma, minimal deviation variant"]
last_modified_at: 2026-11-12
description: "Tivozanib: predicted new indication Endocervical carcinoma (evidence level L5). Approved use: Renal cell carcinoma (nonpapillary renal cell carcinoma…"
---

# Tivozanib
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

## Tivozanib: From Renal Cell Carcinoma to Endocervical Carcinoma
{: .text-alpha }

## One-Sentence Summary

Tivozanib is an oral VEGF receptor inhibitor originally used to treat advanced renal cell carcinoma.
The TxGNN model predicts it may be effective for **endocervical carcinoma**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Renal cell carcinoma (nonpapillary renal cell carcinoma, renal cell adenocarcinoma, clear cell renal carcinoma) |
| Predicted New Indication | Endocervical carcinoma |
| TxGNN Prediction Score | 0.9981 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 1 of 1) |
| Number of FDA Applications | 1 (active: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on pharmacology information, tivozanib is a tyrosine kinase inhibitor that blocks all three VEGF receptors (VEGFR-1/FLT1, VEGFR-2/KDR and VEGFR-3/FLT4) with equal potency. Its efficacy in renal cell carcinoma, a highly vascularised tumour, is the basis of its original use.

Cervical cancer also depends on VEGF-driven angiogenesis, and anti-VEGF therapy (bevacizumab) has shown benefit in this disease. This gives a plausible mechanistic bridge from renal cell carcinoma to endocervical carcinoma. However, this rationale is unverified: no disease-specific data was supplied, and the high TxGNN score is a computational prediction only.

The other top-ranked predictions are also rare gynaecologic adenocarcinoma subtypes (e.g. uterine ligament adenocarcinomas, rare cervical adenocarcinoma variants), all at Evidence Level L5 with scores of about 0.9980. The high scores likely reflect disease-ontology proximity rather than subtype-specific biology.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| NDA212904 | FOTIVDA | AVEO PHARMS | Capsule; oral | Valid |

<!-- licenses:end -->

Note: Other regulatory sources describe an FDA approval in March 2021 for advanced renal cell carcinoma that has relapsed or is refractory after two or more prior systemic therapies.

<!-- review:begin us-lic-20261106-tivozanib-2 -->

> **Review correction (2026-11-06)**: Originally stated: "Note: Other regulatory sources describe an FDA approval in March 2021 for advanced renal cell carcinoma that has relapsed or is refractory after two or more prior systemic therapies. The NDA is currently listed as cancelled in the compiled data, so its present marketing status should be confirmed." Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 1 FDA application or NDC listing for this drug, 1 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-tivozanib-2 -->

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (VEGFR tyrosine kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions** (7 records found; the 4 below have severity ratings):
  - **Major**: Phenobarbital, St. John's Wort
  - **Moderate**: Riociguat, Medroxyprogesterone acetate
- Target pharmacology: tivozanib inhibits FLT1 (VEGFR-1), KDR (VEGFR-2) and FLT4 (VEGFR-3).

No warnings or contraindications are available in the compiled data. Please refer to the package insert for further safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or publications (Evidence Level L5).

<!-- review:begin us-lic-20261031-tivozanib-1 -->

> **Review correction (2026-10-31)**: Originally stated: "The prediction has no supporting clinical trials or publications (Evidence Level L5). The anti-angiogenic rationale is plausible but unverified, the predicted diseases are mostly rare subtypes where evidence is unlikely to emerge soon, and the only US NDA is cancelled." Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-10-31). The FDA data list 1 FDA application or NDC listing for this drug, 1 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261031-tivozanib-1 -->

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism-of-action data from DrugBank
- Preclinical or clinical evidence of VEGFR inhibition in cervical or endocervical carcinoma, including a literature and trial search
- Confirmation of current US regulatory and marketing status
- Review of the Major interactions (CYP3A4 inducers such as phenobarbital and St. John's Wort) for any future study design

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-10-31 | Removed: "The anti-angiogenic rationale is plausible but unverified, the predicted diseases are mostly rare subtypes where evidence is unlikely to eme" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "The NDA is currently listed as cancelled in the compiled data, so its present marketing status should be confirmed" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

