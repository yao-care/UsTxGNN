---
layout: default
title: Ramucirumab
parent: Model Prediction Only (L5)
nav_order: 1108
evidence_level: L5
indication_count: 10
monitor_inn: "Ramucirumab"
predicted_indications: ["uterine ligament adenocarcinoma", "endocervical carcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "cervical adenosquamous carcinoma, glassy cell variant", "uterine ligament endometrioid adenocarcinoma", "uterine ligament clear cell adenocarcinoma", "uterine ligament mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma"]
last_modified_at: 2026-11-12
description: "Ramucirumab: predicted new indication Uterine ligament adenocarcinoma (evidence level L5). Approved use: Non-small cell lung carcinoma, gastric adenocarcinoma…"
---

# Ramucirumab
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

## Ramucirumab: From Non-Small Cell Lung Cancer and Gastric Adenocarcinoma to Uterine Ligament Adenocarcinoma
{: .text-alpha }

## One-Sentence Summary

Ramucirumab is a monoclonal antibody originally used to treat solid tumours such as non-small cell lung carcinoma, gastric adenocarcinoma and hepatocellular carcinoma.
The TxGNN model predicts it may be effective for **uterine ligament adenocarcinoma**,
but currently there are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-small cell lung carcinoma, gastric adenocarcinoma, hepatocellular carcinoma (the data compiled for this report contains no approved-indication text from the license record) |
| Predicted New Indication | Uterine ligament adenocarcinoma |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 1 of 1) |
| Number of FDA Applications | 1 (active: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general drug knowledge, ramucirumab is a VEGFR-2 antagonist, and its established indications (gastric adenocarcinoma, non-small cell lung cancer, hepatocellular carcinoma) are tumours in which VEGF/VEGFR-2 signalling and angiogenesis play a role. This mechanistic description is an inference and is not drawn from the supplied data.

Uterine ligament adenocarcinoma is a gynaecological adenocarcinoma, so an anti-angiogenic rationale is plausible. However, no direct data were available for this entity, and the link between the original and new indications remains theoretical.

Nine other gynecological adenocarcinoma predictions (such as endocervical carcinoma and several rare cervical and uterine ligament subtypes) received similarly high scores (0.9994–0.9995). Some of these, such as the signet ring cell and intestinal variants, share histology with gastrointestinal adenocarcinoma, which may partly explain the high scores. Histologic overlap is not evidence of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125477 | CYRAMZA (Eli Lilly and Company) | Solution | Not available; status: valid |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (monoclonal antibody against VEGFR-2) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: The interaction query identified 100 interacting drugs in total; 20 were returned in the compiled data. Most are rated **Major**, and many involve bleeding risk, including:
  - Antiplatelet and antithrombotic agents: acetylsalicylic acid, clopidogrel, cilostazol, cangrelor, abciximab, caplacizumab, defibrotide
  - Anticoagulants and thrombolytics: apixaban, betrixaban, bivalirudin, dalteparin, antithrombin III, alteplase
  - Others rated Major: deferasirox, and the radiolabelled agents ibritumomab tiuxetan and tositumomab
  - Rated Moderate: dexfenfluramine, fenfluramine, sibutramine

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN score (Evidence Level L5), with no clinical trials or publications for uterine ligament adenocarcinoma.

<!-- review:begin us-lic-20261031-ramucirumab-1 -->

> **Review correction (2026-10-31)**: Originally stated: "The prediction is supported only by the TxGNN score (Evidence Level L5), with no clinical trials or publications for uterine ligament adenocarcinoma. The only US licence on record is cancelled, and warnings and contraindications are not available, so safety screening cannot proceed." Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-10-31). The FDA data list 1 FDA application or NDC listing for this drug, 1 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261031-ramucirumab-1 -->

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- Preclinical or clinical evidence in uterine ligament or related gynaecological adenocarcinomas, such as a literature and trial registry search
- Clarification of current availability
- A bleeding-risk management plan given the many major interactions with anticoagulant and antiplatelet drugs

<!-- review:begin us-lic-20261106-ramucirumab-2 -->

> **Review correction (2026-11-06)**: Originally stated: "Clarification of the cancelled US licence status and current availability" Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 1 FDA application or NDC listing for this drug, 1 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-ramucirumab-2 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-10-31 | Removed: "The only US licence on record is cancelled, and warnings and contraindications are not available, so safety screening cannot proceed" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "the cancelled US licence status and" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

