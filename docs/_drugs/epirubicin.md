---
layout: default
title: Epirubicin
parent: Model Prediction Only (L5)
nav_order: 661
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-04
monitor_inn: "EPIRUBICIN"
predicted_indications: ["primary pulmonary lymphoma", "well-differentiated fetal adenocarcinoma of the lung", "small cell lung carcinoma", "pulmonary blastoma", "lung mixed small cell and squamous cell carcinoma", "myeloid leukemia", "upper aerodigestive tract neoplasm"]
description: "Epirubicin: predicted new indication Primary pulmonary lymphoma (evidence level L5). Approved use: Not recorded in the local data"
---

# Epirubicin
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

## Epirubicin: Primary pulmonary lymphoma
{: .text-alpha }

## One-Sentence Summary

Epirubicin is an anthracycline chemotherapy drug (a DNA-intercalating topoisomerase II inhibitor) used in cancer treatment.
The TxGNN model predicts it may be relevant to **原發性肺淋巴瘤 (primary pulmonary lymphoma)**, but **no clinical trials** and **no study that directly tests epirubicin in this disease** are currently available, so the evidence level is **L5** (model prediction only).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Primary pulmonary lymphoma |
| TxGNN Prediction Score | 0.9971 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of FDA Applications | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Based on known pharmacology, epirubicin is an anthracycline, the 4' epimer of doxorubicin. Anthracyclines act by intercalating into DNA and inhibiting topoisomerase II, and they are most active during the S phase of the cell cycle.

Anthracyclines are components of several lymphoma regimens, for example CEOP and VEBEP, which gives a plausible mechanistic link to lymphoma. However, the current standard of care for B-cell lymphomas is rituximab-based CHOP (which uses doxorubicin), with Pola-R-CHP emerging as an option. No study found tests epirubicin specifically in primary pulmonary lymphoma, so the link remains theoretical.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The publications linked to this prediction are general or about other lymphoma settings. None tests epirubicin in primary pulmonary lymphoma.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7686469](https://pubmed.ncbi.nlm.nih.gov/7686469/) | 1993 | Review | Drugs | General review of epirubicin pharmacology and its use in cancer chemotherapy, with activity comparable to doxorubicin in several solid tumours |
| [39192408](https://pubmed.ncbi.nlm.nih.gov/39192408/) | 2024 | Retrospective cohort | Zhongguo Shi Yan Xue Ye Xue Za Zhi | Clinical features and prognosis of primary extranodal DLBCL in the rituximab era; not epirubicin-specific |
| [40728626](https://pubmed.ncbi.nlm.nih.gov/40728626/) | 2025 | Post-hoc analysis | Annals of Hematology | Pola-R-CHP as first-line therapy in 117 DLBCL patients; doxorubicin-based, not epirubicin |
| [10526668](https://pubmed.ncbi.nlm.nih.gov/10526668/) | 1999 | Cohort | Cancer Journal | VEBEP regimen plus radiotherapy in advanced Hodgkin's disease |
| [36237246](https://pubmed.ncbi.nlm.nih.gov/36237246/) | 2022 | Case report | Translational Cancer Research | Misdiagnosed pleural MALT lymphoma |
| [1866500](https://pubmed.ncbi.nlm.nih.gov/1866500/) | 1991 | Case report | Revista de Investigacion Clinica | A single case of non-Hodgkin lymphoma involving the lung |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA050778 | Ellence (Pharmacia & Upjohn Company LLC) | Injection, solution | Not listed |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (anthracycline) |
| Myelosuppression Risk | High (neutropenia and thrombocytopenia are expected; secondary AML/MDS has been reported after adjuvant use) |
| Emetogenicity Classification | Moderate to high |
| Monitoring Items | CBC with differential, liver and renal function, cardiac function (cumulative anthracycline cardiotoxicity) |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

- **Drug Interactions**: 100 interactions were recorded in the data compiled for this report. Major-level examples include cimetidine and dolasetron. Moderate-level examples include clarithromycin, levofloxacin, bupropion, palonosetron, naltrexone and loperamide.
- **Conditions of concern from related records**: liver failure, liver disease, kidney disease, thrombocytopenia, neutropenia, agranulocytosis, myocardial infarction, cardiomyopathy, heart conduction disease, sudden cardiac arrest and stomatitis. These are not taken from label text and should be checked against the package insert.

Please refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but it is purely computational. No clinical trial or study directly tests epirubicin in primary pulmonary lymphoma, and current standard therapy (rituximab-based CHOP) already uses a related anthracycline, doxorubicin. Cardiac and haematological toxicity add to the caution.

**To proceed, the following is needed:**
- Direct clinical or preclinical evidence of epirubicin activity in primary pulmonary lymphoma
- Comparison against current rituximab-based standard regimens
- Mechanism-of-action data and the full package insert warnings and contraindications
- A cardiac and haematological safety monitoring plan

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

