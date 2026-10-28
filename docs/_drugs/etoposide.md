---
layout: default
title: Etoposide
parent: Model Prediction Only (L5)
nav_order: 685
evidence_level: L5
indication_count: 10
monitor_inn: "ETOPOSIDE"
predicted_indications: ["well-differentiated fetal adenocarcinoma of the lung", "primary pulmonary lymphoma", "pulmonary blastoma", "Ewing sarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina", "rhabdomyosarcoma (disease)", "embryonal extrahepatic bile duct rhabdomyosarcoma", "parameningeal embryonal rhabdomyosarcoma", "extrahepatic bile duct rhabdomyosarcoma", "prostate embryonal rhabdomyosarcoma"]
last_modified_at: 2026-10-28
description: "Etoposide: predicted new indication Well-differentiated fetal adenocarcinoma of the lung (evidence level L5). Approved use: Not recorded in the local data"
---

# Etoposide
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

## Etoposide: Well-differentiated fetal adenocarcinoma of the lung
{: .text-alpha }

## One-Sentence Summary

Etoposide is a topoisomerase II inhibitor chemotherapy originally used for small cell lung carcinoma and testicular germ cell tumours.
The TxGNN model predicts it may be effective for **Ewing sarcoma** (the top-ranked prediction with substantial supporting evidence), with **32 registered clinical trials** and **20 publications** currently supporting this direction.
Several other predictions (e.g., rhabdomyosarcoma) are also supported, while many rare-tumour predictions rest on very little evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Well-differentiated fetal adenocarcinoma of the lung |
| TxGNN Prediction Score | 0.9994 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 7 of 7) |
| Number of NDAs | 7 (valid: 7) |
| Recommended Decision | Proceed with Guardrails |

**Note on the prediction list:** The rank-1 prediction is well-differentiated fetal adenocarcinoma of the lung (0.9994), supported only by a single case report/review (L4, Hold). Ewing sarcoma is presented here because it has the strongest evidence of the ten predictions. Rhabdomyosarcoma (rank 6, 0.9979) is also L1 and is summarised below.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, etoposide is a topoisomerase II inhibitor that causes DNA double-strand breaks in rapidly dividing cells. Its efficacy in small cell lung carcinoma and germ cell tumours is established.

Ewing sarcoma is a highly proliferative bone and soft tissue tumour of children and young adults. The literature notes it is highly sensitive to genotoxic agents such as etoposide. A randomised Phase III trial (INT-0154, PMID 12594313) showed that adding ifosfamide and etoposide to standard chemotherapy improved outcomes in newly diagnosed disease. Etoposide-containing regimens are already part of many standard protocols, so this "repurposing" is largely confirmatory.

## Clinical Trial Evidence

Ewing sarcoma: 32 trials were retrieved. The most relevant are listed below. Many trials use etoposide as one part of a multi-drug regimen, so they do not isolate etoposide's own effect.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00002516](https://clinicaltrials.gov/study/NCT00002516) | Phase 3 | Unknown | Not listed | EICESS 92: randomised comparison of combination chemotherapy regimens plus surgery/radiotherapy in Ewing sarcoma |
| [NCT00020566](https://clinicaltrials.gov/study/NCT00020566) | Phase 3 | Unknown | 1200 | EURO-E.W.I.N.G.99: chemotherapy with or without radiotherapy/surgery and stem cell support |
| [NCT00006734](https://clinicaltrials.gov/study/NCT00006734) | Phase 3 | Completed | 587 | Interval-compressed chemotherapy intensification in Ewing sarcoma and related tumours |
| [NCT01231906](https://clinicaltrials.gov/study/NCT01231906) | Phase 3 | Completed | 642 | Adding vincristine-topotecan-cyclophosphamide to a standard 5-drug regimen (including etoposide) in non-metastatic Ewing sarcoma |
| [NCT02063022](https://clinicaltrials.gov/study/NCT02063022) | Phase 3 | Completed | 278 | Dose intensification versus standard treatment in non-metastatic Ewing sarcoma |
| [NCT02306161](https://clinicaltrials.gov/study/NCT02306161) | Phase 3 | Active, not recruiting | 312 | Ganitumab added to multi-agent chemotherapy (including etoposide) in metastatic Ewing sarcoma |
| [NCT00002898](https://clinicaltrials.gov/study/NCT00002898) | Phase 3 | Completed | 400 | MMT 95: chemotherapy regimens in rhabdomyosarcoma and other soft tissue tumours, including Ewing-family tumours |
| [NCT00002466](https://clinicaltrials.gov/study/NCT00002466) | Phase 2 | Completed | Not listed | Cyclophosphamide, doxorubicin, vincristine, etoposide and ifosfamide followed by resection and radiotherapy; single-arm |
| [NCT02727387](https://clinicaltrials.gov/study/NCT02727387) | Phase 2 | Completed | 155 | High-dose chemotherapy, radiotherapy and maintenance in metastatic Ewing sarcoma |
| [NCT01864109](https://clinicaltrials.gov/study/NCT01864109) | Phase 2 | Active, not recruiting | 83 | Irinotecan and temozolomide added to high-dose alkylator-based chemotherapy in newly diagnosed Ewing sarcoma |

A further Phase III trial (NCT00334867) was withdrawn with 0 participants, and NCT06820957 (Phase 2/3, regorafenib added to VDC/IE) was terminated after 2 participants.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12594313](https://pubmed.ncbi.nlm.nih.gov/12594313/) | 2003 | RCT (Phase III) | N Engl J Med | Adding ifosfamide and etoposide to standard chemotherapy for newly diagnosed Ewing sarcoma/PNET of bone |
| [36522207](https://pubmed.ncbi.nlm.nih.gov/36522207/) | 2022 | RCT (Phase 3) | Lancet | EE2012: comparison of two chemotherapy regimens in newly diagnosed Ewing sarcoma |
| [36669140](https://pubmed.ncbi.nlm.nih.gov/36669140/) | 2023 | RCT (Phase III) | J Clin Oncol | Ganitumab with interval-compressed chemotherapy in metastatic Ewing sarcoma (Children's Oncology Group) |
| [23091096](https://pubmed.ncbi.nlm.nih.gov/23091096/) | 2012 | RCT | J Clin Oncol | Interval-compressed chemotherapy (alternating VDC and ifosfamide-etoposide cycles) for localised Ewing sarcoma |
| [31952545](https://pubmed.ncbi.nlm.nih.gov/31952545/) | 2020 | RCT protocol | Trials | Euro Ewing 2012 protocol for newly diagnosed Ewing sarcoma family tumours |
| [37403815](https://pubmed.ncbi.nlm.nih.gov/37403815/) | 2023 | Consensus guideline | Cancer | National Ewing Sarcoma Tumor Board recommendations on management |
| [39713774](https://pubmed.ncbi.nlm.nih.gov/39713774/) | 2024 | Retrospective cohort | Sarcoma | Oral etoposide in 33 adolescent and adult patients with relapsed or refractory Ewing sarcoma |
| [29513652](https://pubmed.ncbi.nlm.nih.gov/29513652/) | 2018 | Preclinical | Nature | EWS-FLI1 causes R-loops and blocks BRCA1 repair, explaining sensitivity to genotoxic agents such as etoposide |
| [20152770](https://pubmed.ncbi.nlm.nih.gov/20152770/) | 2010 | Review | Lancet Oncol | Ewing sarcoma overview; survival improved to about 75% in localised disease with chemotherapy |
| [26304893](https://pubmed.ncbi.nlm.nih.gov/26304893/) | 2015 | Review | J Clin Oncol | Current management and future approaches through collaboration |

### Other predictions at a glance

| Predicted Indication | TxGNN Score | Evidence Level | Decision | Support |
|------|------|------|------|------|
| Well-differentiated fetal adenocarcinoma of the lung | 0.9994 | L5 | Hold | One case report/review |
| Primary pulmonary lymphoma | 0.9994 | L5 | Hold | No trials; literature mostly on other lymphoma subtypes or small cell lung cancer |
| Pulmonary blastoma | 0.9994 | L5 | Research question | Case reports and reviews only |
| Rhabdomyosarcoma | 0.9979 | L1 | Proceed with Guardrails | Phase III trials (NCT00003052, NCT00002898, NCT00876031) and an IRSG randomised study of ifosfamide/etoposide in metastatic disease (PMID 11846301) |
| Botryoid-type embryonal rhabdomyosarcoma of the vagina | 0.9980 | L5 | Hold | One case report/review of cervical disease |
| Parameningeal embryonal rhabdomyosarcoma | 0.9976 | L5 | Research question | Cohort and review, not etoposide-specific |
| Prostate embryonal rhabdomyosarcoma | 0.9974 | L5 | Hold | A single 1987 review |
| Embryonal extrahepatic bile duct rhabdomyosarcoma | 0.9976 | L5 | Hold | Prediction only |
| Extrahepatic bile duct rhabdomyosarcoma | 0.9975 | L5 | Hold | Prediction only |

## US Market Information

Approved indication text was not available.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA075635 | Etoposide (Mylan) | Capsule | Not available |
| ANDA074290 | Etoposide (Hikma) | Injection | Not available |
| ANDA074513 | Etoposide (BluePoint) | Injection | Not available |
| NDA020457 | Etopophos (H2-Pharma) | Lyophilised powder for injection | Not available |
| ANDA074529 | Etoposide (BluePoint) | Concentrated injection solution | Not available |

Two further cancelled authorisations are not shown: NDA220200 (Avopef, Avyxa Pharma) and ANDA074983 (Etoposide, Fresenius Kabi).

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (topoisomerase II inhibitor) |
| Myelosuppression Risk | High. Knowledge-graph contraindication links include neutropenia, thrombocytopenia, leukopenia, anaemia and agranulocytosis; the clinical risk is consistent with this |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count with differential, liver and renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for label safety information.

- **Knowledge-graph contraindication signals** (not label text): thrombocytopenia, neutropenia, agranulocytosis, anaemia, macrocytic anaemia, leukopenia, interstitial lung disease, pulmonary fibrosis, impaired renal function, acidosis/metabolic acidosis, and drug-induced liver injury.
- **Drug interactions:** 100 interactions were identified; 20 are shown in the data compiled. Moderate-level interactions include aprepitant, rolapitant, metronomidazole, tinidazole, eliglustat, rosuvastatin and simvastatin. Levofloxacin is minor. Others (e.g., cimetidine, pantoprazole, morphine, amphotericin B) have unclassified severity.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for Ewing sarcoma and rhabdomyosarcoma; Hold or research question for the remaining predictions)

**Rationale:**
- Ewing sarcoma has multiple randomised Phase III trials and a landmark NEJM trial supporting ifosfamide/etoposide-containing regimens, which are already standard care. Rhabdomyosarcoma has similar Phase III and cooperative group support. Most other predictions rest on case reports or no data.
- Evidence comes from combination regimens, so etoposide's individual contribution is not isolated.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and approved indication text (currently a blocking gap for safety screening)
- Detailed mechanism of action data
- A monitoring plan for myelosuppression and secondary malignancy risk, with paediatric dosing considerations
- For the Hold predictions, prospective or at least systematically collected data before any further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

