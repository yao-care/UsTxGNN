---
layout: default
title: Paliperidone
parent: Model Prediction Only (L5)
nav_order: 1010
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-12
description: "Paliperidone: predicted new indication Retinal dystrophy with or without extraocular anomalies (evidence level L5). Approved use: Schizophrenia, schizoaffective disorder, schizophreniform disorder…"
monitor_inn: "PALIPERIDONE"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "myopia X-linked", "syndromic myopia", "hydranencephaly (disease)", "congenital disorder of glycosylation with defective fucosylation", "myopia 26, X-linked, female-limited", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "atypical glycine encephalopathy"]
---

# Paliperidone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Paliperidone: From Schizophrenia to Retinal Dystrophy with or without Extraocular Anomalies
{: .text-alpha }

## One-Sentence Summary

Paliperidone is an atypical antipsychotic originally used to treat schizophrenia and related psychotic disorders.
The TxGNN model predicts it may be effective for **retinal dystrophy with or without extraocular anomalies**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia, schizoaffective disorder, schizophreniform disorder, psychotic disorder, mental disorder |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 16 of 20) |
| Number of FDA Applications | 20 (active: 16) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Paliperidone is known to be the active metabolite of risperidone (9-hydroxyrisperidone) and acts as a dopamine D2 and serotonin 5-HT2A antagonist. Its efficacy in schizophrenia and related psychotic disorders is established.

No plausible link between this receptor pharmacology and inherited retinal dystrophy has been shown. Retinal dystrophies are mostly monogenic degenerative conditions of the retina. The very high TxGNN score (0.9992) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. No trial or publication was found to support the connection, and the similarity between the original and predicted indications could not be assessed.

For this reason the prediction should be treated as a computational hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

The table lists five of them, and approved indication text was not available for any of them.

<!-- review:begin us-lic-20261105-paliperidone-1 -->

> **Review correction (2026-11-05)**: Originally stated: "All 12 authorizations are valid. The table lists five of them, and approved indication text was not available for any of them." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-05). The FDA data list 20 FDA applications or NDC listings for this drug, 16 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261105-paliperidone-1 -->

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022264 | INVEGA SUSTENNA | Injection | Not specified |
| NDA207946 | INVEGA TRINZA | Injection, suspension, extended release | Not specified |
| NDA216352 | Erzofri extended-release | Injection | Not specified |
| ANDA203802 | Paliperidone | Tablet, film coated, extended release | Not specified |
| ANDA204707 | Paliperidone | Tablet, extended release | Not specified |

Available dosage forms include extended-release oral tablets and extended-release injectables.

## Safety Considerations

- **Conditions flagged in the knowledge graph (not label text):** The knowledge graph links paliperidone to the following conditions as contraindications or cautions:
  - Cardiovascular: long QT syndrome (including familial), torsades de pointes, orthostatic hypotension, postural orthostatic tachycardia syndrome, hypotensive disorder, myocardial infarction, coronary thrombosis.
  - Metabolic: diabetes mellitus, diabetic ketoacidosis, hyperglycemia, hyperlipidemia (including familial), obesity disorder, potassium deficiency disease.
  - Neurological: epilepsy, basal ganglia disease, multiple system atrophy, focal hand dystonia, blepharospasm.
  - Haematological: neutropenia, agranulocytosis, hemoglobinopathy.
  - Gastrointestinal: Crohn disease, inflammatory bowel disease.
  - Other: impaired renal function disease, female breast carcinoma.
- **Drug Interactions:** 100 interactions were recorded. The two classified as **Major** are:
  - Bupropion
  - Morphine

  Notable Moderate interactions include:
  - Antidiabetic agents (metformin, pioglitazone, alogliptin, canagliflozin, chlorpropamide, acarbose, albiglutide)
  - Anticholinergic agents (atropine, hyoscyamine, glycopyrronium)
  - Epinephrine
  - Hydrocortisone
  - Famotidine
  - Loperamide
  - Amphotericin B
  - Lorcaserin
  - Bisacodyl

Please refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no clinical trials or publications and no demonstrated mechanism linking paliperidone to retinal dystrophy. The drug is marketed.

<!-- review:begin us-lic-20261106-paliperidone-3 -->

> **Review correction (2026-11-06)**: Originally stated: "The drug is marketed, with 12 valid authorizations." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 20 FDA applications or NDC listings for this drug, 16 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-paliperidone-3 -->

**To proceed, the following is needed:**
- Mechanism of action data and a biological rationale connecting dopaminergic or serotonergic antagonism to retinal degeneration
- Preclinical evidence (for example, retinal disease models) before any clinical consideration
- Package insert warnings and contraindications to complete the safety review

<!-- review:begin us-lic-20261106-paliperidone-2 -->

> **Review correction (2026-11-06)**: Originally stated: "Package insert warnings and contraindications to complete the safety review / Verification of the cancelled market status and its effect on development feasibility" Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 20 FDA applications or NDC listings for this drug, 16 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-paliperidone-2 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "All 12 authorizations are valid" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "Verification of the cancelled market status and its effect on development feasibility" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "with 12 valid authorizations" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

