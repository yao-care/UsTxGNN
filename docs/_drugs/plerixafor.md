---
layout: default
title: Plerixafor
parent: Model Prediction Only (L5)
nav_order: 1056
evidence_level: L5
indication_count: 7
---

# Plerixafor
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Plerixafor: From Stem Cell Mobilization to Indolent Plasma Cell Myeloma

## One-Sentence Summary

Plerixafor is a CXCR4 antagonist marketed in the US as an injection, used to mobilize stem cells (the record notes use in multiple myeloma).
The TxGNN model predicts it may be effective for **indolent plasma cell myeloma**, but this prediction has **0 clinical trials** and **0 publications** behind it, so it is a model output only.
A separate, better-supported prediction in the same record is **myeloid leukemia** (rank 7), with **30 clinical trials** and **20 publications**; it is covered in its own section below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hematopoietic stem cell mobilization (license records carry no indication text) |
| Predicted New Indication | Indolent plasma cell myeloma |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 12 (the five listed authorizations are all ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the record. Plerixafor is known to block CXCR4, the receptor for the chemokine CXCL12, and this is the basis of its stem cell mobilization use.

The CXCR4/CXCL12 axis governs how plasma cells home to and stay in the bone marrow, so a link to plasma cell myeloma is plausible. However, mobilizing stem cells in myeloma patients is a different purpose from treating indolent disease. The record contains no trials or publications for this indication, and the score of 99.97% should be read as a graph-based prediction, not as evidence of efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for indolent plasma cell myeloma.

## Literature Evidence

Currently no related literature available for indolent plasma cell myeloma.

---

## Additional Signal: Myeloid Leukemia (Rank 7)

This prediction has a score of 99.02%, evidence level **L2**, and a stage of "Research Question". Plerixafor disrupts CXCL12-mediated retention of leukemic cells in the bone marrow niche. This may mobilize blasts into the circulation and sensitize them to chemotherapy. Most trials are Phase 1 or 1/2 combination studies, so plerixafor's own contribution is often hard to isolate.

### Selected Clinical Trials (10 of 30)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00512252](https://clinicaltrials.gov/study/NCT00512252) | Phase 1/2 | Completed | 52 | AMD3100 (plerixafor) + mitoxantrone, etoposide, cytarabine in relapsed/refractory AML |
| [NCT00906945](https://clinicaltrials.gov/study/NCT00906945) | Phase 1/2 | Completed | 39 | Plerixafor + G-CSF as chemosensitization in relapsed/refractory AML |
| [NCT01435343](https://clinicaltrials.gov/study/NCT01435343) | Phase 1/2 | Completed | 55 | Fludarabine, idarubicin, cytarabine, G-CSF + plerixafor in relapsed/refractory AML (age ≤65) |
| [NCT01352650](https://clinicaltrials.gov/study/NCT01352650) | Phase 1 | Completed | 71 | Decitabine + plerixafor priming in AML patients ≥60 years |
| [NCT00943943](https://clinicaltrials.gov/study/NCT00943943) | Phase 1 | Completed | 33 | G-CSF, plerixafor and sorafenib in FLT3-mutated AML |
| [NCT00990054](https://clinicaltrials.gov/study/NCT00990054) | Phase 1 | Completed | 36 | Plerixafor dose escalation with cytarabine and daunorubicin ("7+3") in newly diagnosed AML |
| [NCT01319864](https://clinicaltrials.gov/study/NCT01319864) | Phase 1 | Completed | 20 | Plerixafor as chemosensitizer with cytarabine and etoposide in pediatric relapsed acute leukemia/MDS |
| [NCT02605460](https://clinicaltrials.gov/study/NCT02605460) | Phase 2 | Unknown | 20 | CXCR4 antagonist chemosensitization before HSCT in acute leukemia in remission |
| [NCT06141304](https://clinicaltrials.gov/study/NCT06141304) | Phase 2 | Unknown | 28 | Plerixafor + donor lymphocyte infusion for relapse after allogeneic HSCT |
| [NCT00822770](https://clinicaltrials.gov/study/NCT00822770) | Phase 1/2 | Completed | 47 | G-CSF + plerixafor with busulfan/fludarabine conditioning for allogeneic transplant in myeloid malignancies |

### Selected Literature (10 of 20)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22308295](https://pubmed.ncbi.nlm.nih.gov/22308295/) | 2012 | Phase 1/2 | Blood | Tested whether CXCR4 inhibition by plerixafor increases AML blast sensitivity to chemotherapy; 52 relapsed/refractory patients treated |
| [29392425](https://pubmed.ncbi.nlm.nih.gov/29392425/) | 2018 | Phase 1/2 | Ann Hematol | PLERIFLAG regimen (FLAG-Ida + high-dose plerixafor) in first early-relapsed or refractory AML |
| [29724902](https://pubmed.ncbi.nlm.nih.gov/29724902/) | 2018 | Phase 1 | Haematologica | Decitabine + escalating plerixafor in 69 older patients with newly diagnosed AML; also assessed effects on leukemia stem cells |
| [32697348](https://pubmed.ncbi.nlm.nih.gov/32697348/) | 2020 | Phase 1 | Am J Hematol | Sorafenib + G-CSF + plerixafor in 28 patients with relapsed/refractory FLT3-ITD AML |
| [30654137](https://pubmed.ncbi.nlm.nih.gov/30654137/) | 2019 | Phase 1 | Biol Blood Marrow Transplant | Safety and tolerability of plerixafor with myeloablative conditioning before allogeneic HCT in AML |
| [32877869](https://pubmed.ncbi.nlm.nih.gov/32877869/) | 2020 | Systematic review / meta-analysis | Leuk Res | Plerixafor with chemotherapy and/or HCT in acute leukemia, covering preclinical and clinical studies |
| [39261603](https://pubmed.ncbi.nlm.nih.gov/39261603/) | 2024 | Review | Leukemia | CXCL12-CXCR4 axis as a therapeutic target in AML |
| [31723817](https://pubmed.ncbi.nlm.nih.gov/31723817/) | 2019 | Clinical study | HemaSphere | Plerixafor stem cell mobilization in poorly mobilizing AML patients (title reports it as safe and effective) |
| [28718760](https://pubmed.ncbi.nlm.nih.gov/28718760/) | 2018 | Clinical analysis | Leuk Lymphoma | CD25 expression and outcomes in older AML patients treated with plerixafor and decitabine; CD25-positive patients had inferior survival |
| [30150522](https://pubmed.ncbi.nlm.nih.gov/30150522/) | 2018 | Case report | Cancers | Complete remission in a 4-year-old with refractory AML after plerixafor, cytarabine and melphalan conditioning |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA215334 | plerixafor | Injection, solution | Amneal Pharmaceuticals LLC |
| ANDA217560 | Plerixafor | Injection, solution | Camber Pharmaceuticals, Inc. |
| ANDA205182 | Plerixafor | Solution | Dr. Reddy's Laboratories Inc |
| ANDA208980 | Plerixafor | Injection | Zydus Lifesciences Limited |
| ANDA215698 | Plerixafor | Solution | Meitheal Pharmaceuticals Inc. |

The record lists 12 authorizations in total, of which 5 are shown. All available products are injectable or solution forms, and none carries approved-indication text in this record.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found for this drug.

---

## Conclusion and Next Steps

**Decision: Hold** (indolent plasma cell myeloma)

**Rationale:**
The prediction rests only on a model score, with no trials or literature, and the mechanistic link is plausible but unproven. The myeloid leukemia signal is much stronger (L2, Research Question stage). It still consists mostly of small Phase 1/2 combination studies, with no randomized evidence that plerixafor itself adds benefit.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- For indolent plasma cell myeloma: any preclinical or clinical evidence, since none is currently available
- For myeloid leukemia: full review of the 30 trials, including those not yet graded for relevance, and a comparative or randomized study that isolates plerixafor's contribution
- Verification of the ambiguous "CMM7" label against the ontology before evaluating it

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

