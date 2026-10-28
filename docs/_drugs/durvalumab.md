---
layout: default
title: Durvalumab
parent: Model Prediction Only (L5)
nav_order: 635
evidence_level: L5
indication_count: 6
monitor_inn: "DURVALUMAB"
predicted_indications: ["uterine ligament adenocarcinoma", "endocervical carcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma"]
last_modified_at: 2026-10-28
description: "Durvalumab: predicted new indication Uterine ligament adenocarcinoma (evidence level L5). Approved use: Transitional cell carcinoma"
---

# Durvalumab
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

## Durvalumab: From Transitional Cell Carcinoma to Uterine Ligament Adenocarcinoma
{: .text-alpha }

## One-Sentence Summary

Durvalumab is a PD-L1 immune checkpoint inhibitor. The knowledge graph records transitional cell carcinoma as its original indication (a relation recorded in the knowledge graph, not a label-confirmed approval).
The TxGNN model predicts it may be effective for **uterine ligament adenocarcinoma** (top-ranked prediction), but **no clinical trials and no publications** directly support this prediction.
The nearest supported direction is the second-ranked prediction, endocervical carcinoma, which has **1 early-phase clinical trial** and **2 loosely related publications**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Transitional cell carcinoma (relation recorded in the knowledge graph; the US licence record has no indication text) |
| Predicted New Indication | Uterine ligament adenocarcinoma |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of NDAs | 1 (valid: 1) |
| Number of approvals | 1 BLA |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on general knowledge, durvalumab is a monoclonal antibody that blocks PD-L1, which can restore T-cell antitumour activity. The rationale for gynaecologic adenocarcinomas is that PD-L1 blockade could be relevant to tumours that express PD-L1.

For uterine ligament adenocarcinoma specifically, this link is only an inference. The tumour is rare, and no study of any kind was found for it. The prediction should be seen as a hypothesis from the TxGNN model, not as supported evidence.

Among the other predictions, endocervical carcinoma has a clearer biologic rationale. Cervical carcinomas are often HPV-driven and may express PD-L1. Durvalumab combined with radiotherapy and tremelimumab (anti-CTLA-4) has been tested in a small Phase 1 study.

## Clinical Trial Evidence

No clinical trials are registered for the top-ranked prediction, uterine ligament adenocarcinoma. The only trial found relates to the second-ranked prediction, endocervical carcinoma, and is shown for context. It does not directly study the top-ranked disease.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03452332](https://clinicaltrials.gov/study/NCT03452332) | Phase 1 | Completed | 20 | Hypofractionated radiotherapy plus durvalumab and tremelimumab in recurrent or metastatic cervical, vaginal or vulvar cancer. It gives safety and feasibility data only, and no comparator efficacy data. |

## Literature Evidence

No publications were found for uterine ligament adenocarcinoma. The two publications below relate to the second-ranked prediction (cervical cancers) and are shown for context only.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37467967](https://pubmed.ncbi.nlm.nih.gov/37467967/) | 2023 | Review | Biomedical Journal | Review of small cell neuroendocrine carcinoma of the cervix. It notes a lack of clinical trials and that published data are limited to case series and reports. |
| [42518016](https://pubmed.ncbi.nlm.nih.gov/42518016/) | 2026 | Nonrandomized Phase 1 trial | Oncology and Therapy | Ceralasertib plus durvalumab in Chinese patients with advanced solid tumours that are refractory to prior anti-PD-(L)1 therapy or have no standard of care. It is not specific to gynaecologic adenocarcinoma. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761069 | IMFINZI (AstraZeneca Pharmaceuticals LP) | Injection, solution | Not stated in the available licence record |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (PD-L1 checkpoint inhibitor monoclonal antibody), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: 81 interactions are recorded. Examples:
  - **Major**: adalimumab.
  - **Moderate**: systemic corticosteroids (hydrocortisone, prednisone, prednisolone, dexamethasone, methylprednisolone, betamethasone, budesonide, triamcinolone, deflazacort), alefacept, alemtuzumab, anakinra, roflumilast, and some vaccines (tetanus toxoid, anthrax vaccine).
  - **Minor**: zinc salts.

  Corticosteroids and other immunomodulators are particularly relevant, because they may interact with the immune-based mechanism of the drug.

For warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, uterine ligament adenocarcinoma, has a very high model score but no trials or publications, so it is at evidence level L5. Related support exists only for endocervical carcinoma (one small Phase 1 trial), and it does not apply directly to this rare disease.

**To proceed, the following is needed:**
- Mechanism of action data and a mechanistic analysis for this tumour type, including PD-L1 expression data
- Review of FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Preclinical or case-level evidence in uterine ligament adenocarcinoma, or a decision to focus on better-supported gynaecologic indications such as endocervical carcinoma
- Confirmation of the original and approved indications from the FDA label, because the licence record has no indication text
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

