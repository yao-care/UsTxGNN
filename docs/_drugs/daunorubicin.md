---
layout: default
title: Daunorubicin
parent: Model Prediction Only (L5)
nav_order: 574
evidence_level: L5
indication_count: 10
---

# Daunorubicin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Daunorubicin: From Anthracycline Chemotherapy to Hodgkin Lymphoma

## One-Sentence Summary

Daunorubicin is an anthracycline cytotoxic chemotherapy agent that is currently marketed in the United States as an injection. The TxGNN model predicts it may be effective for **Hodgkin Lymphoma**. The registry and literature searches returned **50 clinical trials** and **20 publications**, but none is a daunorubicin-specific Phase 3 study. The support comes mainly from doxorubicin-based regimens (ABVD, AVD), so it is class-level rather than direct evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the provided license data |
| Predicted New Indication | Hodgkin Lymphoma |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L3 (class-level evidence only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 5 license records (3 distinct application numbers) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the dataset. Daunorubicin belongs to the anthracycline class, which acts by DNA intercalation and topoisomerase II inhibition. It is a core cytotoxic drug class in haematological cancers. A 2003 review notes that daunorubicin with cytarabine made cure of acute myeloid leukaemia possible.

Hodgkin lymphoma is a chemotherapy-sensitive haematological malignancy. Its standard regimens, ABVD and AVD, are built on an anthracycline backbone, and that anthracycline is doxorubicin, not daunorubicin. Mechanistically, the class-level link is plausible, which likely explains the high model score.

Two caveats limit the strength of this link:
- None of the Hodgkin Phase 3 trials found tests daunorubicin.
- The only daunorubicin-specific lymphoma study is a small 1997 liposomal daunorubicin (DaunoXome) Phase 2 study in relapsed or refractory lymphoma. It did not report Hodgkin-specific results.

---

## Clinical Trial Evidence

All trials below use doxorubicin (Adriamycin), not daunorubicin, so they support the anthracycline class only. The list shows the 10 most relevant of 50 Hodgkin-related trials.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04685616](https://clinicaltrials.gov/study/NCT04685616) | Phase 3 | Recruiting | 1042 | RADAR: ABVD vs A2VD, with or without radiotherapy, in early-stage Hodgkin lymphoma (PET-adapted) |
| [NCT01712490](https://clinicaltrials.gov/study/NCT01712490) | Phase 3 | Completed | 1334 | Brentuximab vedotin + AVD vs ABVD in advanced classical Hodgkin lymphoma |
| [NCT00049595](https://clinicaltrials.gov/study/NCT00049595) | Phase 3 | Completed | 552 | BEACOPP vs ABVD in stage III/IV Hodgkin lymphoma |
| [NCT06377566](https://clinicaltrials.gov/study/NCT06377566) | Phase 2 | Recruiting | 71 | BV-AVD, PET-adapted, in early-stage bulky Hodgkin lymphoma |
| [NCT03755804](https://clinicaltrials.gov/study/NCT03755804) | Phase 2 | Active, not recruiting | 232 | Risk- and response-adapted therapy, including doxorubicin, in pediatric classical Hodgkin lymphoma |
| [NCT03527628](https://clinicaltrials.gov/study/NCT03527628) | Phase 2 | Unknown | 220 | ACVD + brentuximab vedotin in PET-2-positive advanced Hodgkin lymphoma |
| [NCT01534078](https://clinicaltrials.gov/study/NCT01534078) | Phase 2 | Completed | 34 | Brentuximab vedotin + AVD in non-bulky limited-stage Hodgkin lymphoma |
| [NCT00352027](https://clinicaltrials.gov/study/NCT00352027) | Phase 2 | Completed | 81 | Stanford V with low-dose radiotherapy in intermediate-risk pediatric Hodgkin lymphoma |
| [NCT00797472](https://clinicaltrials.gov/study/NCT00797472) | Phase 2 | Unknown | 120 | R-mabHD vs ABVD in Hodgkin's disease |
| [NCT01390584](https://clinicaltrials.gov/study/NCT01390584) | Phase 2 | Terminated | 6 | PET-based response-adapted therapy in bulky stage I/II classical Hodgkin lymphoma |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39413375](https://pubmed.ncbi.nlm.nih.gov/39413375/) | 2024 | RCT | N Engl J Med | Nivolumab + AVD in advanced-stage classic Hodgkin lymphoma (doxorubicin backbone) |
| [35830649](https://pubmed.ncbi.nlm.nih.gov/35830649/) | 2022 | RCT follow-up | N Engl J Med | Overall survival with brentuximab vedotin + AVD vs ABVD in stage III/IV disease |
| [9387047](https://pubmed.ncbi.nlm.nih.gov/9387047/) | 1997 | Phase 2 single-arm | Invest New Drugs | Liposomal daunorubicin in 19 relapsed/refractory lymphoma patients: 1 complete and 2 partial responses at the higher dose; no cardiac deterioration seen |
| [28365830](https://pubmed.ncbi.nlm.nih.gov/28365830/) | 2017 | Review | Curr Oncol Rep | Risk-adapted and response-adapted therapy and the role of radiotherapy in early-stage Hodgkin lymphoma |
| [14584273](https://pubmed.ncbi.nlm.nih.gov/14584273/) | 2003 | Review | Gan To Kagaku Ryoho | Haematologic tumour chemotherapy overview: daunorubicin and cytarabine in AML; ABVD as first-line therapy for advanced Hodgkin lymphoma |
| [378369](https://pubmed.ncbi.nlm.nih.gov/378369/) | 1979 | Review | Cancer Treat Rep | Roles and limitations of daunorubicin and adriamycin in cancer treatment (no abstract available) |
| [36271128](https://pubmed.ncbi.nlm.nih.gov/36271128/) | 2022 | Retrospective cohort | Sci Rep | Interim PET/CT predicts outcome in 245 Hodgkin lymphoma patients treated with ABVD |
| [24220522](https://pubmed.ncbi.nlm.nih.gov/24220522/) | 2013 | Review | Br J Hosp Med | Classical Hodgkin lymphoma: past, present and future perspectives |
| [21774715](https://pubmed.ncbi.nlm.nih.gov/21774715/) | 2011 | Commentary | N Engl J Med | Hodgkin's lymphoma as a model for progress in cancer treatment |
| [32053083](https://pubmed.ncbi.nlm.nih.gov/32053083/) | 2020 | Preclinical | Anticancer Agents Med Chem | Benzisothiazolone derivatives inhibit NF-κB and are synergistic with doxorubicin and etoposide in Hodgkin lymphoma cells |

---

## US Market Information

The license data does not include approved indication text for any record.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA 050731 | Daunorubicin Hydrochloride (Hikma Pharmaceuticals USA Inc.) | Injection | Not listed |
| ANDA 208759 | Daunorubicin Hydrochloride (Hisun Pharmaceuticals USA, Inc.) | Injection, solution | Not listed |
| ANDA 065035 | Daunorubicin Hydrochloride (Meitheal Pharmaceuticals Inc.) | Injection, solution | Not listed |

The Hikma and Hisun records each appear twice in the source data, so the five records cover three distinct applications.

---

## Cytotoxicity

The entries below are based on general knowledge of the anthracycline class, not on data in the Evidence Pack. They must be confirmed against the package insert.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (anthracycline; DNA intercalation and topoisomerase II inhibition) |
| Myelosuppression Risk | High (dose-limiting toxicity for the class) |
| Emetogenicity Classification | Moderate |
| Monitoring Items | CBC with differential, cardiac function (e.g., LVEF), liver and renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (99.81%). However, the supporting trials and papers involve doxorubicin-based regimens, and no daunorubicin-specific Hodgkin evidence was found. The package insert warnings and contraindications are also missing, which blocks the safety screening stage. At present this is a research question, not a development candidate.

**To proceed, the following is needed:**
- FDA package insert warnings, contraindications, and approved indications (download and parse the label PDFs)
- Mechanism of action data from DrugBank
- A literature review of daunorubicin-specific use in Hodgkin lymphoma, including liposomal formulations
- A comparison of cardiotoxicity and cumulative-dose considerations between daunorubicin and doxorubicin in Hodgkin regimens
- Manual review of the 40 trials whose relevance grade is still pending

This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

