---
layout: default
title: Doxorubicin
parent: High Evidence (L1-L2)
nav_order: 626
evidence_level: L2
indication_count: 8
last_modified_at: 2026-10-31
monitor_inn: "DOXORUBICIN"
predicted_indications: ["Ewing sarcoma", "well-differentiated fetal adenocarcinoma of the lung", "primary pulmonary lymphoma", "pulmonary blastoma", "monocytic leukemia", "botryoid-type embryonal rhabdomyosarcoma of the vagina", "parameningeal embryonal rhabdomyosarcoma", "rhabdomyosarcoma (disease)"]
description: "Doxorubicin: predicted new indication Ewing sarcoma (evidence level L2). Approved use: Not recorded in the local data"
---

# Doxorubicin
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **8** 
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

## Doxorubicin: Ewing sarcoma
{: .text-alpha }

## One-Sentence Summary

Doxorubicin is an anthracycline chemotherapy drug originally used for lymphomas (Hodgkin and non-Hodgkin) and acute lymphoblastic leukemia.
The TxGNN model predicts it may be effective for **Ewing sarcoma**,
with **28 clinical trials** and **20 publications** currently supporting this direction. Doxorubicin is already part of standard multi-agent Ewing sarcoma regimens (VDC/IE, VAC).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Ewing sarcoma |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L2 |
| US Market Status | Marketed (valid licenses on record: at least 12) |
| Number of FDA Applications | at least 12 |
| Recommended Decision | Proceed with Guardrails |

Note: the data compiled for this report assigns L2. By the stated rules, the several completed Phase 3 trials in the list would argue for L1, but most do not report doxorubicin-specific results and their relevance grading is pending. L2 is retained as the conservative level.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on established pharmacology, doxorubicin is a topoisomerase II inhibitor and DNA intercalator. It damages DNA in rapidly dividing cells, so chemosensitive tumors are susceptible.

Ewing sarcoma is a chemosensitive small round cell tumor of bone and soft tissue, mostly affecting children, adolescents and young adults. Doxorubicin is already a backbone of standard multi-agent regimens (vincristine-doxorubicin-cyclophosphamide alternating with ifosfamide-etoposide). The original indications (lymphomas and leukemias) are also rapidly proliferating, chemosensitive malignancies, which is the mechanistic common ground.

The main limiting factor is cumulative cardiotoxicity, which requires dose limits or cardioprotection with dexrazoxane.

## Clinical Trial Evidence

The data lists 28 trials; the 10 most relevant are shown below. Trials with a pending relevance grade are summarized from their registry descriptions only.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00006734](https://clinicaltrials.gov/study/NCT00006734) | Phase 3 | Completed | 587 | Interval-compressed chemotherapy vs standard in Ewing sarcoma and related tumors |
| [NCT01231906](https://clinicaltrials.gov/study/NCT01231906) | Phase 3 | Completed | 642 | Adding vincristine-topotecan-cyclophosphamide to standard 5-drug chemotherapy (including doxorubicin) in non-metastatic disease |
| [NCT02063022](https://clinicaltrials.gov/study/NCT02063022) | Phase 3 | Completed | 278 | Dose intensification vs standard treatment in non-metastatic Ewing sarcoma |
| [NCT02306161](https://clinicaltrials.gov/study/NCT02306161) | Phase 3 | Active, not recruiting | 312 | Ganitumab (IGF-1R antibody) added to multi-agent chemotherapy including doxorubicin in metastatic disease |
| [NCT00020566](https://clinicaltrials.gov/study/NCT00020566) | Phase 3 | Unknown | 1200 | EURO-E.W.I.N.G.99: chemotherapy with or without radiation, surgery or stem cell transplant |
| [NCT00038142](https://clinicaltrials.gov/study/NCT00038142) | Phase 2 | Terminated | 46 | Randomized VAC plus dexrazoxane with or without ImmTher in high-risk disease; terminated, limited evidence |
| [NCT00003667](https://clinicaltrials.gov/study/NCT00003667) | Phase 2 | Completed | Not reported | Randomized VAC with dexrazoxane, with or without ImmTher, in high-risk disease |
| [NCT00002466](https://clinicaltrials.gov/study/NCT00002466) | Phase 2 | Completed | Not reported | Multi-agent regimen including doxorubicin, followed by resection and radiotherapy |
| [NCT00949325](https://clinicaltrials.gov/study/NCT00949325) | Phase 1/2 | Completed | 24 | Liposomal doxorubicin plus temsirolimus in recurrent soft tissue and bone sarcomas (mixed population) |
| [NCT06820957](https://clinicaltrials.gov/study/NCT06820957) | Phase 2/3 | Terminated | 2 | VIrR added to VDC/IE in metastatic Ewing sarcoma; terminated with 2 patients, uninformative |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12594313](https://pubmed.ncbi.nlm.nih.gov/12594313/) | 2003 | RCT | N Engl J Med | Adding ifosfamide and etoposide to standard chemotherapy in newly diagnosed Ewing sarcoma and PNET of bone |
| [23091096](https://pubmed.ncbi.nlm.nih.gov/23091096/) | 2012 | RCT | J Clin Oncol | Interval-compressed chemotherapy (VDC/IE) in localized Ewing sarcoma |
| [36522207](https://pubmed.ncbi.nlm.nih.gov/36522207/) | 2022 | RCT | Lancet | EE2012: comparison of two chemotherapy regimens in newly diagnosed Ewing sarcoma |
| [36669140](https://pubmed.ncbi.nlm.nih.gov/36669140/) | 2023 | RCT | J Clin Oncol | Ganitumab with interval-compressed chemotherapy in metastatic Ewing sarcoma |
| [31952545](https://pubmed.ncbi.nlm.nih.gov/31952545/) | 2020 | RCT protocol | Trials | EURO EWING 2012 protocol design |
| [42537000](https://pubmed.ncbi.nlm.nih.gov/42537000/) | 2026 | Cohort | J Clin Oncol | Long-term outcomes of patients in Euro-EWING99 |
| [37651654](https://pubmed.ncbi.nlm.nih.gov/37651654/) | 2023 | Long-term follow-up | J Clin Oncol | Long-term outcomes of interval-compressed chemotherapy in localized disease (AEWS0031) |
| [37403815](https://pubmed.ncbi.nlm.nih.gov/37403815/) | 2023 | Review | Cancer | Consensus recommendations on Ewing sarcoma management |
| [20152770](https://pubmed.ncbi.nlm.nih.gov/20152770/) | 2010 | Review | Lancet Oncol | Survival improved from about 10% before chemotherapy to about 75% for localized disease |
| [1833556](https://pubmed.ncbi.nlm.nih.gov/1833556/) | 1991 | Dose-intensity analysis | J Natl Cancer Inst | Influence of doxorubicin dose intensity on response and outcome in osteogenic and Ewing sarcoma |

## US Market Information

The drug is marketed in the US, and 12 US authorizations are currently valid. Approved-indication text is not available for any of them. Five representative entries are listed.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA050629 | Doxorubicin Hydrochloride (Pfizer) | Injection, solution | Not available |
| NDA050718 | Doxorubicin Hydrochloride Liposome (Baxter) | Injection, suspension, liposomal | Not available |
| ANDA062975 | Doxorubicin Hydrochloride (Hikma) | Injection, solution | Not available |
| ANDA208888 | Doxorubicin Hydrochloride (Amneal) | Injection, powder, lyophilized, for solution | Not available |
| ANDA203263 | Doxorubicin Hydrochloride (Sun Pharmaceutical) | Injectable, liposomal | Not available |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (anthracycline; topoisomerase II inhibitor and DNA intercalator) |
| Myelosuppression Risk | High (neutropenia, thrombocytopenia, leukopenia and anemia appear among the knowledge-graph contraindications) |
| Emetogenicity Classification | Moderate to high (typical for anthracyclines in combination regimens; not stated in the compiled data) |
| Monitoring Items | CBC with differential, liver function and bilirubin, cardiac function (echocardiography or LVEF, cumulative-dose tracking) |
| Handling Protection | Must follow cytotoxic drug handling regulations |

Please also refer to the package insert warnings and precautions.

## Safety Considerations

Package insert warnings and contraindications were not available in the compiled data (this is a blocking data gap for formal safety screening). The following come from other sources.

- **Knowledge-graph contraindications** (from the TxGNN graph, not label text): liver failure and liver disease, hyperbilirubinemia, thrombocytopenia, neutropenia, leukopenia, agranulocytosis, anemia, heart disease, cardiomyopathy, congestive heart failure, heart conduction disease, sudden cardiac arrest, and active infectious disease including fungal infection.
- **Drug interactions**: 100 interactions were found. Major ones listed include dolasetron, cisapride and papaverine. Moderate ones include ondansetron, granisetron, palonosetron, aprepitant, rolapitant, dexamethasone, clarithromycin, levofloxacin and famotidine. Many of the antiemetic and QT-related combinations are common in chemotherapy supportive care and need review.
- **Cardiotoxicity**: cumulative cardiotoxicity requires dexrazoxane or cumulative-dose limits.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Doxorubicin is already a component of standard Ewing sarcoma regimens, supported by multiple randomized Phase 3 trials and RCT publications. However, those trials mostly test the regimen or an added agent rather than doxorubicin on its own, and all US listings are cancelled.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (blocking gap)
- Mechanism of action data from DrugBank
- Confirmation of current US availability, since all 12 listings are cancelled
- A cardiac monitoring plan with cumulative-dose limits and dexrazoxane use, especially in children and young adults
- Review of major drug interactions, particularly QT-prolonging agents

## Other Predicted Indications (Brief)

| Predicted Indication | Score | Evidence Level | Decision |
|---|---|---|---|
| Rhabdomyosarcoma | 0.9970 | L1 | Research question (strongest evidence is in adult and non-rhabdomyosarcoma soft tissue sarcoma; the role in rhabdomyosarcoma is uncertain) |
| Pulmonary blastoma | 0.9985 | L3 | Research question (mostly case reports and registry data) |
| Primary pulmonary lymphoma | 0.9985 | L4 | Hold |
| Ganglioneuroblastoma | 0.9970 | L4 | Hold |
| Monocytic leukemia | 0.9974 | L4 | Hold (preclinical only) |
| Parameningeal embryonal rhabdomyosarcoma | 0.9971 | L5 | Hold |
| Botryoid-type embryonal rhabdomyosarcoma of the vagina | 0.9972 | L5 | Hold |
| Well-differentiated fetal adenocarcinoma of the lung | 0.9986 | L5 | Hold (no trials or literature) |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

